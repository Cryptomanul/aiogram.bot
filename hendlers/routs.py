#parse_mode это типо для разметок
#resize_keyboard прикольно типо для улучшения красиво
#reply_markup нужно просто чтобы клавиатуру делать с функцией для нее
#keyboardbutton чтобы ну типо в функции для /start и др
#.casefold() плевать на регистр
#.lower() запомни тоже самое что выше 
#FSM машина состояний
#await message.answer_photo и так понятно
#await
# fetchfall делает типо забирает все из sql запроса и возвращает ввиде масива
#comit() сохранение допустим db
#router.message
#product_id id продукта логично LOL
#aiohttp.ClientSession() в интернет запрос
#resp от response то есть ответ 
#return. Честно я думал что все знаю об этом но на деле все иначе. По факту в большей части он просто останавливает всю функцию это реально полезно это надо учитывать это не break или continiue это куда лучше так что я должен это использовать
#FSInputFile ввести какой то файл
#CREATE TABLE создание таблицы aiosqlite
#INTEGER PRIMARY KEY это типо ключ от таблицы больше вводить не надо 
#INTEGER целые числа
#commit завершение именно функции с execute с помощью этого и идет отправка
#взаимодействие с DB_NAME это execute()
# простая аналогия execute - оперативка, commit - жесткий диск
#insert into users буквально как добавить в users
#CREATE TABLE IF NOT EXISTS USERS смотри сделай таблицу если не существует таблицы USERS последнее словно это именно название таблицы
#VALUES именно куда добавить я использовал знаки ?
#INSERT INTO USERS добавить в таблицу USERS
#SELECT * FROM USERS очень хорошая команда первые 3 слова обязательны суть в sql проста прост перевод выбрать всех из таблицы users если что * это как все прям все из таблицы если захочу что то конкретно то select age from USERS
# для получения инфы commit() не нужен
#fetchall() взять все типо result = cursor.fetchall()
#strip and split что делают strip - удаление всех пробелов для идиотов с лишними пробелами split - разделяет все слова в список вот так a,b = ["a", "b"]
#init_db лучше делать в start создает сам файл в моем случае cryptonit228.db и так же создает таблицу в моем случае USERS
#set() список но нельзя хранить одно и тоже
# asyncio.sleep() засыпание в скобках секунды вообще полезно именно для спама условно если у вас 0.1 то там вообще капец!
#add and discard через точку первое добавление второе удаление
#pip freeze > requirements.txt что делает? все сохраняет зависимости в файл requirements.txt
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from hendlers.criptp22 import Form
from aiogram.fsm import state
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.fsm.state import StatesGroup
import aiohttp
import aiosqlite
import asyncio
bot = Bot


router = Router()
@router.message(Command("start"))
async def start(message:Message):
    await message.answer("отлично напиши /help для помощи")
@router.message(Command("help"))
async def help(message:Message):
    await message.answer(
        'вот список команд\n'
         '/start для начала'
         '/subscribe для подписки'
         '/unsubscribe для отписки'
         '/subscribers список подписчиков'                
    ) 
subcribers = set()
async def notifier(bot:Bot):
    while True:
        if subcribers:
            for user in set(subcribers):
                try:
                    await bot.send_message(user, "ваше сообщение")
                except Exception:
                    pass
        await asyncio.sleep(10)                         
                         
@router.message(Command("subscribe"))
async def subscribe(message:Message):
    user_id = message.from_user.id
    subcribers.add(user_id)
    await message.answer("вы подписались!")
@router.message(Command("unsubscribe"))
async def unsubscribe(message:Message):
    user_id = message.from_user.id
    subcribers.discard(user_id)
    await message.answer("вы отписались!")
@router.message(Command("subscribers"))
async def subscribers_comman(message:Message):
    if not subcribers:
        await message.answer("никого нету!")
        return
    text = "подписчики:\n"
    for uid in subcribers:
        text += f"{uid}\n"
    await message.answer(text)
                
    

    
        
    
    
    
    
        
       
        
        
        
        
            
    
    

        
            
     
    








      
    

    



    
    