# BOT_TElegram
# ENG
## The first telegram bot for those who first decided to create a bot.                                    
## First, you need to install the library 


```sh
pip install pyTelegramBotAPI 
```
## Also if you want it to work this command 
```sh
@bot.message_handler(commands=['site']) 
def site(message):
    webbrowser.open('https//') 
```

## You need to import webbrowser, then it will work 

# RU
## Первый телеграмм бота для тех, то первый раз решил создать бота.
## Для начала вам надо установить библиотеку   
```sh
pip install pyTelegramBotAPI 
```

Так же если хотите что бы заработал это команда 
```sh
@bot.message_handler(commands=['site']) 
def site(message):
    webbrowser.open('https//') 
```
## Вам надо import webbrowser, вот тогда она заработает 