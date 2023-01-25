import requests
import telegram as tel
import asyncio
import traceback
try:
    # server check
    uri = "https://www.sysout.co.kr";
    response = requests.get(uri, verify=False)
    if response.status_code == 200:
        print("Server working now")
        exit(0)

    # telegram bot send message
    bot = tel.Bot(token="5818121143:AAGx5P6vYRNLmrmTfs1ym2Cfa5Mw_0IIKrU")
    chat_id = 5492413521

    asyncio.run(
        bot.sendMessage(chat_id=chat_id, text=f"서버 상태 : {response.status_code}")
    )
    print("Server not working now")
    exit(-1)
except:
    # telegram bot send message
    bot = tel.Bot(token="5818121143:AAGx5P6vYRNLmrmTfs1ym2Cfa5Mw_0IIKrU")
    chat_id = 5492413521

    asyncio.run(
        bot.sendMessage(chat_id=chat_id, text=f"Alive checker 실행 오류")
    )
    print("Alive checker error")
    traceback.print_exc()
    exit(-2)
