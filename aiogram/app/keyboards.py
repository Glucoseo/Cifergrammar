from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



main_kb=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Лекция"),KeyboardButton(text="Практика")], 
    [KeyboardButton(text="Автор туралы"),KeyboardButton(text="Альма")]
], resize_keyboard=True,
input_field_placeholder="Мәтін теріңіз")


back_button = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="← Артқа")]],
    resize_keyboard=True
)

lectures_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Лекция 1"), KeyboardButton(text="Лекция 2"), KeyboardButton(text="Лекция 3")],
        [KeyboardButton(text="Лекция 4"), KeyboardButton(text="Лекция 5"), KeyboardButton(text="Лекция 6")],
        [KeyboardButton(text="← Артқа")]
    ],
    resize_keyboard=True
)
practice_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Тапсырма 1"), KeyboardButton(text="Тапсырма 2")],
        [KeyboardButton(text="Тапсырма 3"), KeyboardButton(text="Тапсырма 4")],
        [KeyboardButton(text="← Артқа")]
    ],
    resize_keyboard=True
)
lecture_1=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Лекция 2"),KeyboardButton(text="← Артқа")]
    ],
    resize_keyboard=True
)
lecture_2=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Лекция 3"),KeyboardButton(text="← Артқа")]
    ],
    resize_keyboard=True
)
lecture_3=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Лекция 4"),KeyboardButton(text="← Артқа")]
    ],
    resize_keyboard=True
)
lecture_4=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Лекция 5"),KeyboardButton(text="← Артқа")]
    ],
    resize_keyboard=True
)
lecture_5=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Лекция 6"),KeyboardButton(text="← Артқа")]
    ],
    resize_keyboard=True
)
lecture_6=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Практика"),KeyboardButton(text="← Артқа")]
    ],
    resize_keyboard=True
)





task_1=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Тапсырма 2"),KeyboardButton(text="← Артқа")]
    ],
    resize_keyboard=True
)

task_2=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Тапсырма 3"),KeyboardButton(text="← Артқа")]
    ],
    resize_keyboard=True
)

task_3=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Тапсырма 4"),KeyboardButton(text="← Артқа")]
    ],
    resize_keyboard=True
)

task_4=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="← Артқа")]
    ],
    resize_keyboard=True
)











'''
settings= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Insta", url="https://www.instagram.com/yaklutoi/")]
])

cars=["bmw","china","sel"]

keyboard= ReplyKeyboardBuilder()
async def inline_cars():
    for car in cars:
        keyboard.add(KeyboardButton(text=car))
    return keyboard.adjust(2).as_markup()
    
async def inline_cars():
    for car in cars:
        keyboard = InlineKeyboardBuilder()
        keyboard.add(InlineKeyboardButton(text=car, callback_data=f'car{car }'))
    return keyboard.adjust(2).as_markup()'
    '''
    