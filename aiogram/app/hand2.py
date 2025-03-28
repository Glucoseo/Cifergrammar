from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, InputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import requests
from config import MISTRAL_KEY
from app import keyboards as kb
from PIL import Image, ImageDraw, ImageFont
from aiogram.types import FSInputFile







router = Router()
MISTRAL_API_KEY = MISTRAL_KEY




def generate_certificate(user_name: str) -> str:
    certificate_template = "D:/aiogram/serti.png"
    output_certificate = f"certificate_{user_name}.png"
    
    img = Image.open(certificate_template)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Arial.ttf", 90)
    text_position = (250, 440)
    draw.text(text_position, user_name, fill="blue", font=font)
    img.save(output_certificate)
    
    return output_certificate




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
        response_data = response.json()
        print(response_data)  # Добавь эту строку для проверки структуры ответа
        return response_data.get("choices", [{}])[0].get("message", {}).get("content", "Қателік")
    except Exception as e:
         return f"API қатесі: {str(e)}"


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Cәлем {message.from_user.first_name}!\n'
        'Егер нейрожүйеге интернет немесе цифрлы сауаттылық жөнінде сұрақ қойғың келсе алдымен Альма батырмасын бас, сосын өз сұрағыңды қой.',
        reply_markup=kb.main_kb
    )
@router.message(F.text == "Автор туралы")
async def lecture_handler(message: Message):
    await message.answer("Сәлем! Бұл ботты жасаған НЗМ 8с сынып оқушысы Мақсот Абдулазиз. Бұл бот адамдарды цифрлы сауаттылыққа үйретеді және қоғам үшін қызмет етеді.", reply_markup=kb.back_button)

@router.message(F.text == "Лекция")
async def lecture_handler(message: Message):
    await message.answer("Лекция таңдаңыз:", reply_markup=kb.lectures_kb)

@router.message(F.text == "Лекция 1")
async def lecture_handler(message: Message):
    await message.answer("Лекция 1: Цифрлық сауаттылық деген не?Цифрлық сауаттылық – бұл заманауи технологияларды тиімді пайдалана білу дағдысы. Ол компьютерді, смартфонды, интернетті қолдану, онлайн сервистер арқылы жұмыс істеу, киберқауіпсіздік ережелерін сақтау сияқты аспектілерді қамтиды.Мысалы, егер сіз онлайн банкинг қызметін пайдаланғыңыз келсе, онда сізге интернет-банкинг қосымшасын жүктеу, жеке кабинет ашу, транзакцияларды қадағалау сияқты қадамдарды орындау керек. Бірақ сонымен қатар, киберқауіпсіздік ережелерін ұстану маңызды, себебі алаяқтар сіздің деректеріңізді ұрлауы мүмкін.", reply_markup=kb.lecture_1)

@router.message(F.text == "Лекция 2")
async def lecture_handler(message: Message):
    await message.answer("Лекция 2: Интернеттегі қауіпсіздік негіздері Интернетте жұмыс істеген кезде жеке деректерді қорғау өте маңызды. Интернеттегі алаяқтар адамдардың жеке ақпаратын ұрлау үшін түрлі әдістерді қолданады. Мысалы, әлсіз құпиясөздер арқылы аккаунтыңызды бұзып кіруі мүмкін. Сондықтан күшті парольдер орнату, күмәнді сілтемелерге өтпеу, белгісіз адамдардан келген файлдарды ашпау қажет.Күшті пароль жасаудың ең оңай жолы – үлкен және кіші әріптерді, сандарды және арнайы таңбаларды қосу. Мысалы, 123456 деген пароль әлсіз, ал B@qyt_2024! сияқты пароль әлдеқайда қауіпсіз.", reply_markup=kb.lecture_2)

@router.message(F.text == "Лекция 3")
async def lecture_handler(message: Message):
    await message.answer("Лекция 3: Кибершабуыл түрлері және олардан қорғану Кибершабуылдардың бірнеше түрі бар:Фишинг – бұл алаяқтардың адамдарды алдау арқылы жеке деректерін ұрлау әдісі. Мысалы, сізге банк атынан хат келеді, онда сіздің картаңыз бұғатталғаны туралы айтылады және сілтеме арқылы кіру сұралады. Бұл сілтемені ашсаңыз, сіздің деректеріңіз алаяқтардың қолына түседі.Вирус және зиянды бағдарламалар – бұлар компьютеріңізге немесе смартфоныңызға еніп, ақпарат ұрлауы немесе құрылғыны бұғаттауы мүмкін.Әлеуметтік инженерия – алаяқтар адамдардың сеніміне кіріп, оларға керек ақпаратты айтып қоюға мәжбүрлейді.Қорғану жолдары: әрқашан күмәнді хаттар мен хабарламаларды тексеріңіз, антивирус бағдарламасын орнатыңыз, белгісіз сайттарға жеке мәліметтеріңізді енгізбеңіз.", reply_markup=kb.lecture_3)

@router.message(F.text == "Лекция 4")
async def lecture_handler(message: Message):
    await message.answer("Лекция 4: Әлеуметтік желілердегі қауіпсіздік. Әлеуметтік желілер бізге адамдармен байланыс орнатуға көмектеседі, бірақ қауіпсіздік шараларын сақтамасаңыз, жеке мәліметтеріңізді бөгде адамдар көре алады.Қауіпсіздік шаралары:Жеке ақпаратты ашық қоймаңыз :телефон нөмірі, мекенжай, құжаттар.Бейтаныс адамдардың достық ұсыныстарын қабылдамаңыз. Себебі олар аялақ болуы мүмкін.Екі факторлы аутентификацияны қолданыңыз. Бұл дегеніміз, аккаунтыңызға кіру үшін қосымша код енгізу қажет болады.Мысалы, егер сіздің аккаунтыңызға бөгде біреу кірмек болса, жүйе сіздің телефон нөміріңізге код жібереді, сол кодсыз аккаунтыңыз ашылмайды.", reply_markup=kb.lecture_4)

@router.message(F.text == "Лекция 5")
async def lecture_handler(message: Message):
    await message.answer("Лекция 5: Онлайн төлемдер және алаяқтық схемалар.Онлайн төлемдер өмірімізді жеңілдетеді, бірақ алаяқтар сіздің банк картасы туралы мәліметтерді ұрлауға тырысады.Назар аудару қажет нәрселер:Тек сенімді интернет-дүкендерден тауар сатып алыңыз.HTTPS арқылы басталатын сайттарды ғана қолданыңыз. Себебі осы сайттар ғана қауіпсуіздікті қамтамасыз етеді.Банк картасының CVV-кодын ешкімге бермеңіз.Егерде біреу сіздің кодынызды біліп қойса сіздің есеп-шотыныздан ақша ұрлануы мүмкін.Егер сізге біреу сіз үлкен сыйлық ұттыңыз, тек картаңыздың нөмірін енгізіңіз деп жазса – бұл алаяқтық болуы мүмкін.", reply_markup=kb.lecture_5)

@router.message(F.text == "Лекция 6")
async def lecture_handler(message: Message):
    await message.answer("Лекция 6: Сандық із және жеке деректерді қорғау Сандық із – бұл сіз интернетте қалдыратын ақпарат: посттар, пікірлер, іздеу тарихы, тіркелгілер. Бұл деректерді кибершабуылшылар пайдаланып, сіз туралы ақпарат жинай алады.Қауіпсіздік үшін:Браузер тарихын және cookies-ті үнемі тазалаңыз.Әлеуметтік желілердегі жарияланымдарыңызды кім көре алатынын реттеңіз.Артық тіркелгілерді жойып, қажетсіз қосымшаларға рұқсат бермеңіз.", reply_markup=kb.lecture_6)



@router.message(F.text == "Практика")
async def practice_handler(message: Message):
    await message.answer("Практикалық тапсырмалар:", reply_markup=kb.practice_kb)

@router.message(F.text == "Тапсырма 1")
async def lecture_handler(message: Message):
    await message.answer("Құпиясөз ойлап табу: Телефоныңыздың құпиясөзін жаңартыңыз. Ол кемінде 8 таңбадан тұруы керек және әріптер мен сандар болуы тиіс.", reply_markup=kb.task_1)

@router.message(F.text == "Тапсырма 2")
async def lecture_handler(message: Message):
    await message.answer("Фишингтік хатты анықтау: Электрондық поштаңыздағы немесе хабарламаңыздағы күмәнді сілтемелер мен ұсыныстарды қарап, оларды ашпай, кімнен келгенін тексеріңіз.", reply_markup=kb.task_2)

@router.message(F.text == "Тапсырма 3")
async def lecture_handler(message: Message):
    await message.answer("Жаңа электрондық пошта ашу: Google немесе басқа сервистен жаңа электрондық пошта ашып, оның қауіпсіздік баптауларын қарап шығыңыз.", reply_markup=kb.task_3)

@router.message(F.text == "Тапсырма 4")
async def lecture_handler(message: Message):
    await message.answer("Смартфоныңыздағы қолданбалар рұқсатын тексеру: Телефон баптауларына кіріп, қай қолданбалар сіздің камераңызға, микрофоныңызға немесе орналасқан жеріңізге рұқсат сұрағанын тексеріңіз. Қажетсіз рұқсаттарды өшіріңіз.", reply_markup=kb.task_4)
    
    # Генерация сертификата
    user_name = message.from_user.first_name
    certificate_path = generate_certificate(user_name)
    
    # Отправка сертификата
    with open(certificate_path, "rb") as certificate:
        await message.answer_document(FSInputFile(certificate_path))


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




