import time
import re
import enum
import subprocess
from pythonping import ping


REPLY_PAUSE_SECONDS = 0
COMMAND_PREFIX = '!'

class BotCommands(enum.Enum):
    test = '!test'
    ping = '!ping'
    report = '!report'
    reviewdriver = '!reviewdriver'

def get_ping_time(host):
    ping_responce = 0
    try:
        ping_responce = ping('groupme.com', verbose=True)
    except subprocess.CalledProcessError:
        ping_responce = 99999999
        
    return ping_responce.rtt_avg_ms

"""
    For commands only
"""
def bot_command(data, bot_info, send_message):
    if data['text'].casefold().__contains__('!test'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Success! (200)', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('!ping'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Pong! in ' + str(get_ping_time('groupme.com')) + ' ms', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('!report'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Sending you a link to our report form to your DMs.', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('!review'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('If you wanna to review a driver, fill out this form: https://forms.gle/V29rVVwKSp8HhQFm7', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('!signup'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('You do ghetto oobers and wanna be included in our listings? Aight, fill this out https://forms.gle/qFyivFh2C9Hsyjr59', bot_info[0])
        return True
    
"""
    Regular chatting
""" 
def bot_chat(data, bot_info, send_message):
    if data['text'].casefold().__contains__('wassup'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Yooo wsg ' + str(data['name']) + '!', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('@oober'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Hmmm?', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('catch me outside'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Aight bet! U gonna catch this L >:)' +  + str(data['name']), bot_info[0])
        return True
    elif data['text'].casefold().__contains__('black women bomb asf'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Ong bruh but they be a lil crazy', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('uber eats'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Join the ghetto uber if u want some food mayneeee: https://groupme.com/join_group/70645352/HVAbgYqn', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('ghetto uber'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Join the ghetto uber groupme! We in there homie: https://groupme.com/join_group/70645352/HVAbgYqn', bot_info[0])
        return 
    elif data['text'].casefold().__contains__('hungry'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('I be hungry too mane-', bot_info[0])
        return True
    else:
        return True
    
"""
    Is called everytime a POST message is received from GroupMe.
    data = {
                "attachments": [],
                "avatar_url": "https://i.groupme.com/123456789",
                "created_at": 1302623328,
                "group_id": "1234567890",
                "id": "1234567890",
                "name": "John",
                "sender_id": "12345",
                "sender_type": "user",
                "source_guid": "GUID",
                "system": false,
                "text": "Hello world ☃☃",
                "user_id": "1234567890"
            }
"""
def run(data, bot_info, send_message):
    try:
        if data['text'][0] is '!':
            print("Bot command detected because the first char is " + str(data['text'][0]) )
            bot_command(data, bot_info, send_message)
        else:
            bot_chat(data, bot_info, send_message)
    except Exception as e:
        if hasattr(e, 'message'):
            print("Error messagee => " + e.message)
        else:
            print(e)
        
    
        
   