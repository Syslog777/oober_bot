def run(data, bot_info, send_message):
    if data['text'].lower() == 'wassup':
        send_message('Yooo wsg fam!', bot_info[0])
        return True
    elif data['text'].lower() == 'wassup':
        send_message('Yooo wsg fam!', bot_info[0])
        return True
    elif data['text'].lower() == 'hru':
        send_message('I am running without errors, my mind (CPU) is clear and I\'m feeling great! 😄', bot_info[0])
        return True
    elif data['text'].lower() == 'I need a ride':
        send_message('Ok, sending a DM to all ghetto oober drivers 🚙', bot_info[0])
        return True
    elif data['text'].lower() == '!test':
        send_message('I am in test mode, my functionality is subject to change', bot_info[0])
        return True
    elif data['text'].lower() == '!request ride':
        send_message('Sending a DM to all ghetto oober drivers. I am in test mode, my functionality is subject to change', bot_info[0])
        return True
    elif data['text'].lower() == '!report':
        send_message('Sending you a link to our report form to your DMs. I am in test mode, my functionality is subject to change', bot_info[0])
        return True
    elif data['text'].lower() == 'catch me outside':
        send_message('Aight bet!  I am in test mode, my functionality is subject to change', bot_info[0])
        return True
    else:
        return True