import time
import os
import enum

class BotCommands(enum.Enum):
    test = '!test'
    ping = '!ping'
    

"""
    For commands only
"""
def bot_command(data, bot_info, send_message):
    if data['text'].lower() == BotCommands.test:
        #time.sleep(2)
        send_message('Success (200)', bot_info[0])
        return True
    elif data['text'].lower() == '!ping':
        time.sleep(2)
        send_message('Pong! in ' + str() + ' ms', bot_info[0])
        return True
    elif data['text'].lower() == '!request ride':
        # time.sleep(2)
        send_message('Sending a DM to all ghetto oober drivers.', bot_info[0])
        return True
    elif data['text'].lower() == '!report':
        # time.sleep(2)
        send_message('Sending you a link to our report form to your DMs. I am in test mode, my functionality is subject to change', bot_info[0])
        return True
"""
    Regular chatting
""" 
def bot_chat(data, bot_info, send_message):
    if data['text'].casefold().__eq__('Wassup'.casefold()):
        time.sleep(2)
        send_message('Yooo wsg ' + str(data['name']) + '!', bot_info[0])
        return True
    elif data['text'].casefold().__eq__('@oober'.casefold()):
        time.sleep(2)
        send_message('Wassup?', bot_info[0])
        return True
   
    elif data['text'].lower() == '@oober catch me outside':
        # time.sleep(2)
        send_message('Aight bet!  AI is takin ova u gonna catch this L ' +  + str(data['name']), bot_info[0])
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
    if str[0].__eq__('!'):
        None
   