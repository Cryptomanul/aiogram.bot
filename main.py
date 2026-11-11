#getenv просто между файлами работа
#Dispatcher - мозг или типо того
#Bot то что завязано на сообщениях
#async это перед def и нужна для ассинхронных действий
#router дает отсылать сообщения
#ожидает завершение отправки
#create_task() фоновая задача
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv #читает env файлы и обращается к ключам значениям
from os import getenv
from hendlers.routs import router, notifier
print("система запустилась")
load_dotenv()
Token = getenv("Bot_Token")




brain = Dispatcher()
brain.include_router(router)

    





async def main():
    bot = Bot(token = Token)
    
    asyncio.create_task(notifier(bot))


    await brain.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
