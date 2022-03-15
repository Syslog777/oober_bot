import time

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
    if data['text'].lower() == 'wassup' + data['name']:
        time.sleep(2)
        send_message('Yooo wsg fam!', bot_info[0])
        return True
    elif data['text'].lower().contains('@oober') or data['text'].lower().contains('@bot'):
        time.sleep(2)
        send_message('Wassup?', bot_info[0])
        return True
    elif data['text'].lower() == 'i need a ride':
        time.sleep(2)
        send_message('Ok, sending a DM to all ghetto oober drivers', bot_info[0])
        return True
    elif data['text'].lower() == '!test':
        time.sleep(2)
        send_message('I am in test mode, my functionality is subject to change', bot_info[0])
        return True
    elif data['text'].lower() == '!request ride':
        time.sleep(2)
        send_message('Sending a DM to all ghetto oober drivers. I am in test mode, my functionality is subject to change', bot_info[0])
        return True
    elif data['text'].lower() == '!report':
        time.sleep(2)
        send_message('Sending you a link to our report form to your DMs. I am in test mode, my functionality is subject to change', bot_info[0])
        return True
    elif data['text'].lower() == 'catch me outside':
        time.sleep(2)
        send_message('Aight bet!  I am in test mode, my functionality is subject to change', bot_info[0])
        return True
    else:
        return True