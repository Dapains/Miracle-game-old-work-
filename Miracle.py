__author__ = 'owen_matyi'
items = {"sword": False, "torch": False, "knife": False, "magickey": False, "Holy Grail": False, "Sticks": False,
         "Axe": False, "basicsword": False, "Basicshield": False, "key": False, "magicsword": False}
Class = {"Warrior": False, "Thief": False}
life = 100
gold = 0
armor = 0


def changegold(amount):
    global gold
    life += amount
    print("You gained", amount, "Gold. You now have", gold)


def changelife(hpchange):
    global life
    life += hpchange
    if life <= 0:
        dead()
    print("You lost", hpchange, "Life. you have", life, "life left.")


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Welcome to Zor-- I mean Skyri-- WELCOME TO MIRACLE!")
print("                  By Owen Matyi")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

print("Tips:")
print("Dont be afraid to go back" \
      "Everything can be used for something")


def Charactercreation():
    input("What is your name adventurer?")

    print("what a fine name!")
    start()


def dead():
    print("you are dead try again next time!")
    exit(0)


def start():
    print("you are in a dense forest with a long dirt path")
    print("there are sticks along the path")
    print("You have come to a fork in the road")
    print("you can either go left or right")
    print("Which one do you take?")
    while True:
        choice = input("> ")

        if "left" in choice:
            outsidehouse()
        elif "right" in choice:
            darkcave()
        elif "take sticks" in choice:
            items["Sticks"] = True
            print("sticks taken")

        else:
            print("You pause to comprehend the action you were tasked to do and while thinking a bird pecks your face, ouch!")
            changelife(-10)
            print (life)


def darkcave():
    print("you are in a dark cave")
    print("you can't see you should turn back since you cant see where you are going")

    choice = input("> ")

    if "back" in choice:
        start()
    elif "torch" in choice:
        if items["torch"] == True:
            lightcave()
    else:

        print("you trip on a rock, thats what you get for walking around in the dark")
        changelife(-30)
        print(life)


def outsidehouse():
    print("you are outside a big house")
    print("there appears to be a door and a window")

    choice = input(">")

    if "back" in choice:
        start()
    elif "window" in choice:
        insidehouse()
    elif "door" in choice:
        print("door is locked")
        outsidehouse()
    elif "unlock" in choice:
        if items["magickey"] == True:
            print("the door opens!")
            insidehouse2()
    else:
        print("in your confusion you bash your head into the door and die")
        dead()


def insidehouse():
    print("you are inside the house in what appears to be a living room")
    print("there is a sword on the wall above a fire place")
    print("whover lives here didnt leave for very long because the fire is still lit")
    while True:
        choice = input(">")

        if "back" in choice:
            outsidehouse()
        elif "key" in choice:
            items["key"] = True
            print("Key taken")
        elif "sword" in choice:
            items["sword"] = True
            print("Sword Taken")
        elif "use key" in choice:
            if items["key"] == True:
                print("you use the key to open a secret door behind the fireplace")
                fourthwall()
            else:
                print("you have no key!")
        elif "light" in choice:
            if items["Sticks"] == True:
                items["torch"] = True
                print("You light the stick and create a torch!")
            else:
                print("you light your hand on fire which leads to you burning alive")
                dead()
        else:
            print("You wander around the house and stub your toe, very painful")
            changelife(8)


def lightcave():
    print("The cave is so bright now!")
    print("you see large stone door which you assume is of ancient origin")
    print("There is writing on the door it says:")
    print("I am the Stone guardian Erethos. If you wish to pass you must complete my test.")
    print("We will play a game of choices three one of stone, parchment and trimmers")
    print("the smart hero you are you understand the game is rock paper scissors what will you choose")

    choice = input("> ")

    if "rock" in choice:
        print("Impressive choice but we have tied let us try again shall we")

    elif "paper" in choice:
        print("You have passed my test you may enter the sanctum")
        print("The large stone door opens to reveal a large sanctum!")
        sanctum()
    elif "scissors" in choice:
        print("AH HA I have bested you mortal!")
        print("the Guardian brings down a stone fist, crushing you like a bug")
        dead()
    else:
        print("'You have wasted my time mortal!'")
        print("The Guardian raises a stone spike impailing you and thus killing you in a gruesome fashion")
        dead()


def sanctum():
    print("You enter a large sanctum with big lights and waterfalls. you walk down the large pathway")
    print("you see set foot on a large platform with glowing magic runes and three pedestals:")
    print("The left one has a sword, the right has a magic key, the middle has a skull")
    print("What item do you take?")

    choices = input("> ")

    if "sword" in choices or "left" in choices:
        items["magicsword"] = True
        print("The runes flash red and you were teleported away")
        hell()
    elif "key" in choices or "right" in choices:
        items["magickey"] = True
        print("The runes flash blue and you were teleported away")
        outsidehouse()
    elif "skull" in choices or "middle" in choices:
        print("The skull becomes enveloped in shadows and becomes the one and only Grim Reaper!")
        print("He laughs at you for youre foolishness and then chops your head off wiht his mighty scythe")
        dead()
    else:
        print("You were too indecisive and the were smited for your actions")
        dead()


def hell():
    print("You have been taken to the dark firey depths of hell")
    print("you stare at a thrown of skulls blood and fire where the demon sits")
    print("There are no clear exits at this time what will you do?")

    choices = input("> ")

    if "attack" in choices or "sword" in choices:
        if items["magicsword"] == True:
            print("Your sword glows bright and you slay the mighty demon! You take his heart and shower yourself in his blood like the sick human being you are")
            print("You are teleported to a castle of riches, and bitches Congrats you win!")

        else:
            print("You are weaponless the demon rips you apart and feeds on your corpse")
            dead()
    elif "run" in choices:
        print("you try to run but find no exits, the demon attacks but you manage to evade him with only minor injuries")
        changelife(-10)
    else:
        print("The demon charges you and hits you with a mighty blow")
        changelife(-55)


def insidehouse2():
    print("The door opens, but the room you saw last is no more")
    print("you enter a giant room the windows look out into space with rocks floating by")
    print("there is a glowing orb on a table in the room.")
    print("There is a door leading to another room on your left")
    orb = True
    skeleton = False
    while True:
        choices = input("> ")

        if "orb" in choices:

            print("The orb turns black and a skeleton appears. they do not look happy")
            orb = False
            skeleton = True
            choices = input("> ")
            if "attack" in choices:
                print("You attack the skeleton managing to take off its head with your bare fists, but that sword it had sure was painful")
                changelife(-20)
            elif "loot" in choices:
                if skeleton and orb == False:
                    print("You looted a basic sword and shield and some gold")
                    items["basicsword"] = True
                    items["Basicshield"] = True
                    changegold(10)



        elif "left" in choices:
            atlantis()


        else:
            print("Im confused with that statement")


def atlantis():
    print("you enter a to a the lost city of Atlantis!!!")
    print("You are in the palace you see the throne at the end of the room and gold everywhere")

    choices = input("> ")

    if "sit" in choices:
        print("you sit in the throne, you are the new king of Atlantis!")
        print("You are the winner!")
    elif "gold" in choices:
        print("Theres too much to take... the guards show up, you are arrested and rot in jail")
        dead()
    elif "leave" in choices or "right" in choices:
        print("you are compelled to remain in this room. Nothing outside is really important anyway.")
    else:
        print("please reconsider your options")


def fourthwall():
    print("You are in the fourthwall!")
    print("A room full of cameras and a keyboard")
    choice = input()
    if "break" in choice:
        print("YOU BROKE THE FOURTH WALL!!!!!")
        print("you win")
    elif "use keyboard" in choice:
        print("keyboard comes to life and eats you")
        dead()
    else:
        print("in your shock of being in the fourthwall you dont realize the security guards who come and subdue you,")
        print("to late you realize and resist so they decide to just kill you")
        dead()


Charactercreation()

