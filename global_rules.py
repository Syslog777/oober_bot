def run(data, bot_info, send):
    
    import random
    random.seed()
    f = open("FamilyFeudData.csv", "r", encoding="utf-8")
    lines = f.readlines()

    help_message = "Help:\n.help  -->  This screen\n.test  -->  Try it!\nOtherwise, repeats your message."

    message = data['text']

    if message == '.help':
        send(help_message, bot_info[0])
        return True

    if message == '.test':
        send("Hi there! Your bot is working, you should start customizing it now.", bot_info[0])
        return True
    
    if message == "next":
        randomLine = random.choice(lines).strip().split(",")
        prompt = randomLine[0]
        answers = []
        i = 1
        while i in range(len(randomLine)-1):
            answers.append([randomLine[i], randomLine[i+1]])
            i += 2

        #print(prompt)
        #print(answers)
        msg = prompt
        send(msg, bot_info[0])

    #send("Hi {}! You said: {}".format(data['name'], data['text']), bot_info[0])
    return True
