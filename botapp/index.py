import requests
from bs4 import BeautifulSoup
import telegram
import time
import asyncio
bot_token = "7422796600:AAHdigq8Xh983fDOCpQgv_zRSqQvaDsNX7M"
chat_id="1306699275"
lyon="https://trouverunlogement.lescrous.fr/tools/36/search?maxPrice=450&bounds=4.7718134_45.8082628_4.8983774_45.7073666"
lille="https://trouverunlogement.lescrous.fr/tools/36/search?maxPrice=450&bounds=3.1158064_50.6732934_3.2078132_50.5985301"
mars= "https://trouverunlogement.lescrous.fr/tools/36/search?maxPrice=450&bounds=5.2286902_43.3910329_5.5324758_43.1696205"
# page = requests.get("https://trouverunlogement.lescrous.fr/tools/36/search?maxPrice=450&bounds=5.2286902_43.3910329_5.5324758_43.1696205")
# soup = BeautifulSoup(page.content,"lxml")
# data = soup.find_all("ul",{"class":"fr-grid-row--gutters"})

# print(len(data[0].find_all(recursive=False)))
# print("the length of the children is:",data.contents)



async def send_message(info):
    try:
         await bot.send_message(chat_id=chat_id, text=info)
    except Exception as e:
        print(f"An error occurred: {e}")
   


if __name__ == "__main__":
    while True:
    bot = telegram.Bot(token=bot_token)
    page = requests.get(lille)
    soup = BeautifulSoup(page.content,"lxml")
    data = soup.find_all("ul",{"class":"fr-grid-row--gutters"})
    availablecrous = len(data[0].find_all(recursive=False))
    if availablecrous>0:
        asyncio.run(send_message(f"There are {availablecrous} now"))
    print("a message should be sent")
    time.sleep(10)

   





