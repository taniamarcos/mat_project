import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1985102493:AAFO_AaIOAX0B0ZuEtZiL_SMZPzaYXQvPBU'
    bot_chatID = '-783601911'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    return response.json()
    #test = telegram_bot_sendtext("Testing Telegram bot")
    #print(test)   

def enviarDocumento(ruta):
        bot_token = '1985102493:AAFO_AaIOAX0B0ZuEtZiL_SMZPzaYXQvPBU'
        bot_chatID = '-783601911'
        requests.post('https://api.telegram.org/bot' + bot_token + '/sendDocument',
                files={'document': (ruta, open(ruta, 'rb'))},
                data={'chat_id': bot_chatID, 'caption': 'Document python'}) 
enviarDocumento("1.py")
  
