import time
import re
import enum
import subprocess

REPLY_PAUSE_SECONDS = 0
class BotCommands(enum.Enum):
    test = '!test'
    ping = '!ping'
    report = '!report'
    reviewdriver = '!reviewdriver'

def get_ping_time(host):
    responce_time = 0
    try:
        output = subprocess.check_output(['ping', '-c', '4', '-q', host])
        output = output.decode('utf8')
        statistic = re.search(r'(\d+\.\d+/){3}\d+\.\d+', output).group(0)
        avg_time = re.findall(r'\d+\.\d+', statistic)[1]
        response_time = float(avg_time) 
    except subprocess.CalledProcessError:
        response_time = 99999999
        
    return response_time

"""
    For commands only
"""
def bot_command(data, bot_info, send_message):
    if data['text'].casefold().__contains__(BotCommands.test):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Success! (200)', bot_info[0])
        return True
    elif data['text'].casefold().__contains__str(BotCommands.ping):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Pong! in ' + str(get_ping_time('groupme.com')) + ' ms', bot_info[0])
        return True
    elif data['text'].casefold().__contains__str(BotCommands.report):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Sending you a link to our report form to your DMs.', bot_info[0])
        return True
    
"""
    Regular chatting
""" 
def bot_chat(data, bot_info, send_message):
    if data['text'].casefold().__eq__('Wassup'.casefold()):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Yooo wsg ' + str(data['name']) + '!', bot_info[0])
        return True
    elif data['text'].casefold().__eq__('@oober'.casefold()):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Wassup?', bot_info[0])
        return True
   
    elif data['text'].casefold().__eq__('@oober catch me outside'):
        time.sleep(REPLY_PAUSE_SECONDS)
        send_message('Aight bet! U gonna catch this L >:)' +  + str(data['name']), bot_info[0])
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
        
    
        
   