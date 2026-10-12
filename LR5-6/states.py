from aiogram.fsm.state import State, StatesGroup

class BotStates(StatesGroup):
    menu = State()
    settings = State()
    testing = State()