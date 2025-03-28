
from aiogram import F,Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message, CallbackQuery 
import requests
from config import MISTRAL_KEY
router = Router()
MISTRAL_API_KEY = MISTRAL_KEY
from app import keyboards as kb

def get_mistral_response(prompt):
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}"}
    data = {
        "model": "mistral-medium",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "ҚАТЕЛІК")

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Cәлем!\n ID: {message.from_user.id}\n Егер нейрожүйеге интернет немесе цифрлы сауаттылық жөнінде сұрақ қойғың келсе алдымен Альма батырмасын бам сосын өз сұрағыңды қой.',
                         reply_markup=kb.main_kb)
@router.message(F.text == "Лекция")
async def lecture_handler(message: Message):
    await message.answer("Лекция таңданыз:", reply_markup=kb.back_kb)

@router.message(F.text == "← Артқа")
async def back_handler(message: Message):
    await message.answer("Басты меню:", reply_markup=kb.main_kb)
    



@router.message(F.text == "Альма")
async def start(message: Message):
    await message.answer("Сәлем! Мен чат бот Альмамын. Сенімен танысуға қуанышытымын, мен сені цифрла сауаттылыққа үйретемін!")

@router.message()
async def handle_message(message: Message):
    response = get_mistral_response(message.text)
    await message.answer(response)



    
@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("This is comand help")

@router.message(F.text=="Четам")
async def chetam(message: Message):
    await message.answer("Chetamba")
                            
@router.message(F.photo)
async def photo(message: Message):
    await message.answer(f'ID: {message.photo [-1].file_id}')

@router.message(Command("photo"))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAIB22ed-O0bufDF_vzPR029X98TWI3BAALb6TEbWCnxSNiH7Y88Kq6JAQADAgADeAADNgQ",
                        caption="This is freedom")