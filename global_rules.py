def run(data, bot_info, send):
    
    import random
    random.seed()
    f = open("FamilyFeudData.csv", "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
    f = open("lineIndex.txt", "r", encoding="utf-8")
    lineIndex = int(f.readline().strip()[0])
    f.close()

    help_message = "Help:\n.help  -->  This screen\n.test  -->  Try it!\nOtherwise, repeats your message."

    message = data['text']

    if message == '.help':
        send(help_message, bot_info[0])
        return True

    if message == '.test':
        send("Hi there! Your bot is working, you should start customizing it now.", bot_info[0])
        return True
    
    if message == ".next":
        lineIndex = random.randint(0, len(lines))
        f = open("lineIndex.txt", "w", encoding="utf-8")
        f.write(lineIndex)
        f.close()
        randomLine = lines[lineIndex].strip().split(",")
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
        
    randomLine = lines[lineIndex].strip().split(",")
    prompt = randomLine[0]
    answers = {}
    i = 1
    while i in range(len(randomLine)-1):
        answers[randomLine[i].strip().lower()] = randomLine[i+1]
        i += 2
    
    messageRaw = message
    message = message.strip().lower()
    if message in answers.keys():
        score = answers[message]
        send("Congratulations! {} is correct! {} points!".format(messageRaw, score), bot_info[0])
        
    else:
        # sorry that's incorrect
        send("Sorry that's not right", bot_info[0])
        

    #send("Hi {}! You said: {}".format(data['name'], data['text']), bot_info[0])
    return True
