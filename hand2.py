from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import requests
from config import MISTRAL_KEY
from app import keyboards as kb

router = Router()
MISTRAL_API_KEY = MISTRAL_KEY

# Состояния FSM
class Form(StatesGroup):
    ai_mode = State()

# Получение ответа от Mistral
def get_mistral_response(prompt: str) -> str:
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}"}
    data = {
        "model": "mistral-medium",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "ҚАТЕЛІК")
    except Exception as e:
        return f"API қатесі: {str(e)}"

# Обработчики
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Cәлем!\nID: {message.from_user.id}\n'
        'Егер нейрожүйеге интернет немесе цифрлы сауаттылық жөнінде сұрақ қойғың келсе алдымен Альма батырмасын бас, сосын өз сұрағыңды қой.',
        reply_markup=kb.main_kb
    )

@router.message(F.text == "Лекция")
async def lecture_handler(message: Message):
    await message.answer("Лекция таңдаңыз:", reply_markup=kb.lectures_kb)

@router.message(F.text == "Практика")
async def practice_handler(message: Message):
    await message.answer("Практикалық тапсырмалар:", reply_markup=kb.practice_kb)

@router.message(F.text == "← Артқа")
async def back_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Басты меню:", reply_markup=kb.main_kb)

@router.message(F.text == "Альма")
async def activate_ai_mode(message: Message, state: FSMContext):
    await state.set_state(Form.ai_mode)
    await message.answer(
        "Сәлем! Мен чат-бот Альмамын. Цифрлық сауаттылық бойынша кез келген сұрақ қоя аласыз!",
        reply_markup=kb.back_button
    )

@router.message(Form.ai_mode)
async def handle_ai_question(message: Message, state: FSMContext):
    response = get_mistral_response(message.text)
    await message.answer(response)

@router.message(F.text == "Автор туралы")
async def about_author(message: Message):
    await message.answer("Автор туралы ақпарат:", reply_markup=kb.settings)