import os
import psycopg2
import keyboards
from urllib.parse import urlparse
from telegram.utils.request import Request
from telegram import Bot
from telegram.ext import (
    CommandHandler,
    CallbackQueryHandler,
    Updater
)

DATABASE_URL = urlparse(os.environ['DATABASE_URL'])
DB_USERNAME = DATABASE_URL.username
DB_PASSWORD = DATABASE_URL.password
DB_NAME = DATABASE_URL.path[1:]
DB_HOST = DATABASE_URL.hostname
DB_PORT = DATABASE_URL.port
BOT_TOKEN = "BOT_TOKEN"
TEMP_DB = "./TEMP/"

PORT = int(os.environ.get('PORT', 5000))
token_expires_time = None
connection = None


def check_db_credentials():
    global DATABASE_URL
    global DB_USERNAME
    global DB_PASSWORD
    global DB_NAME
    global DB_HOST
    global DB_PORT

    DATABASE_URL = urlparse(os.environ['DATABASE_URL'])
    DB_USERNAME = DATABASE_URL.username
    DB_PASSWORD = DATABASE_URL.password
    DB_NAME = DATABASE_URL.path[1:]
    DB_HOST = DATABASE_URL.hostname
    DB_PORT = DATABASE_URL.port


def check_connection():
    global connection
    if not connection:
        check_db_credentials()
        connection = get_database_connection()


def get_database_connection():
    check_db_credentials()
    global connection
    if connection is None:
        connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    if connection:
        return connection
    else:
        get_database_connection()


def start(bot, update):
    chat_id = update.message.chat.id
    bot.send_message(
        chat_id=chat_id,
        text="Вэлкам! Самый хайповый шмот за разумные (лол) деньги.",
        reply_markup=keyboards.top_level_menu()
    )


def create_mysql_query(query: list) -> str:
    size = None

    item_type = query[0]
    if len(query) != 1:
        size = query[1]

    if size:
        sql_query = "SELECT * FROM clothes WHERE TYPE = '{}' and SIZE = '{}'".format(item_type, size)
    else:
        sql_query = "SELECT * FROM clothes WHERE TYPE = '{}'".format(item_type)

    return sql_query


def send_query_results(bot, update, query):
    chat_id = update.callback_query.message.chat.id
    results = get_query_result(query)
    count = 0
    if len(results) == 0:
        bot.send_photo(
            chat_id=chat_id,
            photo=open("bot_files/out_of_stock.jpg", "rb"),
            caption="Подписывайся @paulcasual чтобы не пропускать обновления.",
            reply_markup=keyboards.top_level_menu()
        )
    else:
        for item in results:
            path = TEMP_DB + "_update_" + str(update.update_id) + "_" + str(count) + ".png"
            f = open(path, "wb")
            f.write(item[0])
            f.close()
            caption = f"{item[1]} \nРазмер: {item[2]}\nЦена: {item[3]}\nПо поводу покупки пишите - @super19p"
            bot.send_photo(
                chat_id=chat_id,
                photo=open(path, "rb"),
                caption=caption
            )
            count += 1
        bot.send_message(
            text="Продложить осмотр",
            chat_id=chat_id,
            reply_markup=keyboards.top_level_menu()
        )
    for file in os.scandir(TEMP_DB):
        if "1.txt" not in file.path:
            os.remove(file.path)


def get_query_result(query):
    global connection
    check_db_credentials()
    check_connection()
    query_result = None
    if not connection:
        connection = get_database_connection()

    cursor = connection.cursor()
    if cursor:
        cursor.execute(query)
        connection.commit()
        query_result = cursor.fetchall()

    return query_result


def handle_users_reply(bot, update):
    query = update.callback_query
    keyboard = None
    chat_id = update.callback_query.message.chat.id
    db_query = None

    if query.data == "clothes":
        keyboard = keyboards.first_level_clothes()
    elif query.data == "jacket":
        keyboard = keyboards.jacket_size_keyboard()
    elif query.data == "hoodie":
        keyboard = keyboards.hoodie_size_keyboard()
    elif query.data == "tshirt":
        keyboard = keyboards.tshirt_size_keyboard()
    elif query.data == "shorts":
        keyboard = keyboards.shirt_size_keyboard()
    elif query.data == "back_to_top_level":
        keyboard = keyboards.top_level_menu()
    elif query.data == "first_level_clothes":
        keyboard = keyboards.first_level_clothes()
    # ------------------------------------------------
    else:
        if query.data is not None:
            db_query = query.data.split("_")

    if keyboard:
        bot.edit_message_reply_markup(
            chat_id=chat_id,
            message_id=update.callback_query.message.message_id,
            reply_markup=keyboard
        )

    if db_query:
        sql_query = create_mysql_query(db_query)
        send_query_results(bot, update, sql_query)


def error_handler(bot, update, error):
    print(error)


def main():
    check_db_credentials()
    global connection
    try:
        connection = get_database_connection()
    except psycopg2.Error as er:
        print(er)

    req = Request(
        connect_timeout=0.5,
        con_pool_size=8
    )

    bot = Bot(
        request=req,
        token=BOT_TOKEN,
    )

    updater = Updater(
        bot=bot
    )

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(handle_users_reply))
    updater.dispatcher.add_error_handler(error_handler)

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=BOT_TOKEN)
    updater.bot.setWebhook('heroku.app.link' + BOT_TOKEN)
    updater.idle()


# run shit
if __name__ == "__main__":
    main()
