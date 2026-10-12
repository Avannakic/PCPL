from aiogram import Router, F
from aiogram.filters import CommandStart
from states import BotStates

from functions import (
    start,
    back_to_menu,
    enter_settings,
    toggle_category,
    end_settings,
    ask_question,
    check_answer,
    to_list,
    enter_help
)

main_router = Router()

main_router.message.register(start, CommandStart())

main_router.callback_query.register(back_to_menu, F.data == "back_to_menu")
main_router.callback_query.register(enter_settings, BotStates.menu, F.data == "settings")
main_router.callback_query.register(toggle_category, BotStates.settings, F.data.startswith("toggle_"))
main_router.callback_query.register(end_settings, BotStates.settings, F.data == "end_settings")
main_router.callback_query.register(ask_question, F.data.in_({"start_test", "continue_test"}))
main_router.callback_query.register(check_answer, BotStates.testing, F.data.startswith("ans_"))
main_router.callback_query.register(to_list, BotStates.menu, F.data == "to_list")
main_router.callback_query.register(enter_help, BotStates.menu, F.data == "help")