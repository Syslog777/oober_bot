import time
import re
import enum
import subprocess
from pythonping import ping


REPLY_PAUSE_SECONDS = 0.5
COMMAND_PREFIX = '!'
drivers = {}

def setstatus(name, status):
    drivers[name] = status
    

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
        send_message('If you wanna report someone in the ghetto oober group, fill out this form: https://forms.gle/C79FVLcdfJw3Yq5r9', bot_info[0])
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
        send_message('Aight bet! U gonna catch this L >:) ' + str(data['name']), bot_info[0])
        return True
    elif data['text'].casefold().__contains__('black women bomb asf'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Ong bruh but they be a lil crazy', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('uber eats'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Join the ghetto uber if u want some food mayneeee: https://groupme.com/join_group/70645352/HVAbgYqn', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('ghetto uber?'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Join the ghetto uber groupme! We in there homie: https://groupme.com/join_group/70645352/HVAbgYqn', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('hungry'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('I be hungry too mane-', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('is my head big'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Yeah you got a big head', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('why are gas prices so high?'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Cause they want moe money', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('I\'m available'):
        setstatus(str(data['name']), data['text'])
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message(str(data['name']) + ', I set your status as available', bot_info[0])
        return True
    elif data['text'].casefold().__contains__('doing ghetto ubers'):
        setstatus(str(data['name']), data['text'])
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message(str(data['name']) + ', I set your status as available', bot_info[0])
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
        

        
   