from telebot.handler_backends import State, StatesGroup

class MyStates(StatesGroup):
    main_menu = State()
    viewing_history = State()
    searching_in_history = State()
    searching_movie = State()
    help_mode = State()


