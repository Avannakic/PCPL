from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

to_menu_btn = InlineKeyboardButton(text="В меню", callback_data="back_to_menu")
def get_menu_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Начать тест", callback_data='start_test')],
        [InlineKeyboardButton(text="Настроить список слов", callback_data="settings")],
        [InlineKeyboardButton(text="Полный орфоэпический словник", callback_data="to_list")],
        [InlineKeyboardButton(text="Поддержка", callback_data="help")]
    ])

def get_settings_kb(active_categories):
    buttons = []
    categories = {
        "such": "Имена существительные",
        "pril": "Имена прилагательные",
        "glag": "Глаголы",
        "prich": "Причастия",
        "deeprich": "Деепричастия",
        "nar": "Наречия"
    }

    for cat_key, cat_name in categories.items():
        if cat_key in active_categories: marker = "✅"
        else: marker = ""

        buttons.append([InlineKeyboardButton(
            text=f"{marker}{cat_name}",
            callback_data=f"toggle_{cat_key}"
        )])

    buttons.append([InlineKeyboardButton(text="Завершить выбор", callback_data="end_settings")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_test_kb(buttons):
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_result_kb(is_empty):
    if is_empty:
        return InlineKeyboardMarkup(inline_keyboard=[
        [to_menu_btn]
    ])

    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Далее", callback_data="continue_test")],
        [to_menu_btn]
    ])

def get_back_menu_kb(button=None):
    keyboard = []

    if button:
        keyboard.append([button])
    keyboard.append([to_menu_btn])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)