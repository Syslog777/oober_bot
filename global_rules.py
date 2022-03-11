def run(data, bot_info, send):
    
    import random
    random.seed()
    f = open("FamilyFeudData.csv", "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
    f = open("lineIndex.txt", "r", encoding="utf-8")
    line = f.readline()
    print(line)
    lineIndex = int(line.strip())
    f.close()

    if lineIndex == -1:
        send("I just restarted :(", bot_info[0])
        lineIndex = random.randint(0, len(lines))

    print("reading line index", lineIndex)

    help_message = "Help:\n.help  -->  This screen\n.test  -->  Try it!\nOtherwise, repeats your message."

    message = data['text']

    if message == '.help':
        send(help_message, bot_info[0])
        return True

    if message == '.test':
        send("Hi there! Your bot is working, you should start customizing it now.", bot_info[0])
        return True
    
    if message == ".next":
        
        randomLine = lines[lineIndex].strip().split(",")
        prompt = []
        answers = {}
        # loop backwards
        i = 1
        while i < len(randomLine):
            if i < 15:
                answers[randomLine[-(i+1)].strip().lower()] = randomLine[-(i)]
                i += 2
            else:
                prompt.append(randomLine[-(i)])
                i += 1
        prompt = ", ".join(prompt)

        msg = "The answers to the previous question were: \n"
        for key, value in answers.items():
            msg += str(key) + ": " + str(value) + "\n"
        send(msg, bot_info[0])
        
        lineIndex = random.randint(0, len(lines))
        print("writing line index", lineIndex)
        f = open("lineIndex.txt", "w", encoding="utf-8")
        f.write(str(lineIndex))
        f.close()
        randomLine = lines[lineIndex].strip().split(",")
        prompt = []
        answers = {}
        # loop backwards
        i = 1
        print(randomLine)
        while i < len(randomLine):
            if i < 15:
                answers[randomLine[-(i+1)].strip().lower()] = randomLine[-(i)]
                i += 2
            else:
                prompt.append(randomLine[-(i)])
                i += 1
        prompt = ", ".join(prompt)
        print("answers =", answers)
        print("prompt =", prompt)
        msg = prompt
        send(msg, bot_info[0])
        
    else:
        randomLine = lines[lineIndex].strip().split(",")
        prompt = []
        answers = {}
        # loop backwards
        i = 1
        while i < len(randomLine):
            if i < 15:
                answers[randomLine[-(i+1)].strip().lower()] = randomLine[-(i)]
                i += 2
            else:
                prompt.append(randomLine[-(i)])
                i += 1
        prompt = ", ".join(prompt)
            
        print(answers)

        messageRaw = message
        message = message.strip().lower()
        if message in answers.keys():
            score = answers[message]
            send("Congratulations! {} is correct! {} points!".format(messageRaw, score), bot_info[0])

        

    #send("Hi {}! You said: {}".format(data['name'], data['text']), bot_info[0])
    return True
