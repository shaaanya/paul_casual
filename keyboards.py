import telegram


def top_level_menu():
    keyboard = [
        [
            telegram.InlineKeyboardButton("1️⃣ Одежда        ", callback_data="clothes"),
            telegram.InlineKeyboardButton("2️⃣ Аксессуары    ", callback_data="accessors"),
            telegram.InlineKeyboardButton("3️⃣ Обувь", callback_data="shoes")
        ],
        [
            telegram.InlineKeyboardButton("Связаться      ", url="t.me/super19p")
        ]
    ]
    return telegram.InlineKeyboardMarkup(keyboard, resize_keyboard=True)


def first_level_clothes():
    keyboard = [
        [
            telegram.InlineKeyboardButton("1️⃣ Куртки/жилеты      ", callback_data="jacket"),
            telegram.InlineKeyboardButton("2️⃣ Свитеры и толстовки", callback_data="hoodie")
        ],
        [
            telegram.InlineKeyboardButton("3️⃣ Поло и футболки    ", callback_data="tshirt"),
            telegram.InlineKeyboardButton("4️⃣ Штаны и шорты      ", callback_data="shorts")
        ],
        [
            telegram.InlineKeyboardButton("Назад                  ", callback_data="back_to_top_level")
        ]
    ]
    return telegram.InlineKeyboardMarkup(keyboard, resize_keyboard=True)


def jacket_size_keyboard():
    keyboard = [
        [
            telegram.InlineKeyboardButton(" ️S  ", callback_data="jacket_S"),
            telegram.InlineKeyboardButton("  M  ", callback_data="jacket_M"),
            telegram.InlineKeyboardButton(" L    ", callback_data="jacket_L")
        ],
        [
            telegram.InlineKeyboardButton(" XL  ", callback_data="jacket_XL"),
            telegram.InlineKeyboardButton(" XXL    ", callback_data="jacket_XXL")
        ],
        [
            telegram.InlineKeyboardButton("Назад      ", callback_data="first_level_clothes")
        ]
    ]
    return telegram.InlineKeyboardMarkup(keyboard, resize_keyboard=True)


def hoodie_size_keyboard():
    keyboard = [
        [
            telegram.InlineKeyboardButton(" S  ", callback_data="hoodie_S"),
            telegram.InlineKeyboardButton(" M  ", callback_data="hoodie_M"),
            telegram.InlineKeyboardButton(" L    ", callback_data="hoodie_L")
        ],
        [
            telegram.InlineKeyboardButton(" XL  ", callback_data="hoodie_XL"),
            telegram.InlineKeyboardButton(" XXL    ", callback_data="hoodie_XXL")
        ],
        [
            telegram.InlineKeyboardButton("Назад     ", callback_data="first_level_clothes")
        ]
    ]
    return telegram.InlineKeyboardMarkup(keyboard, resize_keyboard=True)


def tshirt_size_keyboard():
    keyboard = [
        [
            telegram.InlineKeyboardButton(" S  ", callback_data="tshirt_S"),
            telegram.InlineKeyboardButton(" M  ", callback_data="tshirt_M"),
            telegram.InlineKeyboardButton(" L    ", callback_data="tshirt_L")
        ],
        [
            telegram.InlineKeyboardButton(" XL  ", callback_data="tshirt_XL"),
            telegram.InlineKeyboardButton(" XXL    ", callback_data="tshirt_XXL")
        ],
        [
            telegram.InlineKeyboardButton("Назад     ", callback_data="first_level_clothes")
        ]
    ]
    return telegram.InlineKeyboardMarkup(keyboard, resize_keyboard=True)


def shirt_size_keyboard():
    keyboard = [
        [
            telegram.InlineKeyboardButton(" S  ", callback_data="shorts_S"),
            telegram.InlineKeyboardButton(" M  ", callback_data="shorts_M"),
            telegram.InlineKeyboardButton(" L    ", callback_data="shorts_L")
        ],
        [
            telegram.InlineKeyboardButton(" XL  ", callback_data="shorts_XL"),
            telegram.InlineKeyboardButton(" XXL    ", callback_data="shorts_XXL")
        ],
        [
            telegram.InlineKeyboardButton("Назад    ", callback_data="first_level_clothes")
        ]
    ]
    return telegram.InlineKeyboardMarkup(keyboard, resize_keyboard=True)
