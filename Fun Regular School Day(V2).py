rain = False
stars = 0
item = 0
time = "not set"
spider = False
def start():
    global stars
    global item
    stars = 0
    item = 0
    wakeUp()

def wakeUp():
    global rain
    print ("You wake up violently.")
    print ("You dread the idea of going to school today. What will you do?")
    if rain == True:
        print ("It's raining heavily, you know why, you remember everything. You hear skitters coming from the wall. What will you do?")
        answer = input("Input 1 to attack the wall\n")
        if answer == "1":
            attackWall()
        else:
            print ("Invalid input")
            wakeUp()
    else:
        answer = input("Input 1 to stay in bed, input 2 to get out of bed.\n")
        if answer == "1":
            stayInBed()
        elif answer == "2":
            getOutOfBed()
        else:
            print ("Invalid input")
            wakeUp()

def attackWall():
    print ("You attack the wall. What an idiot.")
    print ("You manage to break a hand-sized hole in one swift movement... spiders come pouring out.")
    answer = input("Input 1 to plug the hole, input 2 to run and abandon your house\n")
    if answer == "1":
        plugHole()
    elif answer == "2":
        abandonHouse()
    else:
        attackWall()

def plugHole():
    print ("You plug the hole with...")
    answer = input("Input 1 for your hand, input 2 for flex tape, input 3 for fire\n")
    if answer == "1":
        handSeal()
    elif answer == "2":
        flexTapeSeal()
    elif answer == "3":
        fireSeal()
    else:
        print ("Invalid input")
        plugHole()

def handSeal():
    print ("The spiders eat through your hand... and then you... GAME OVER")
    input("Hit enter to exit\n")

def flexTapeSeal():
    print ("The spiders eat through the flex tape! they're too strong... and then they eat you... GAME OVER")
    input("Hit enter to exit\n")

def fireSeal():
    print ("You burn all of the spiders... but now you have a new problem. Your house burns down.")
    print ("You've been convicted for arson. You hear soft chanting on your way to your cell and look over.")
    print ("Tens of thousands of spiders are looking at you and chanting in joy, they've won. GAME OVER ")
    input("Hit enter to exit\n")

def abandonHouse():
    print ("you run outside. unfortunately, the spiders anticipated this.")
    print ("You hear a distant breeze and at that moment you are blown into a spidernado!!")
    print ("You become overwhelmed with spiders and web, you are eaten alive. GAME OVER")
    input("Hit enter to exit\n")

def stayInBed():
    global time
    time = "late"
    print ("You are in your bed, you are wasting time. School starts in 45 minutes. What will you do?")
    answer = input("Input 1 to get out of bed, input 2 to sleep in\n")
    if answer == "1":
        outOfBedRush()
    elif answer == "2":
        sleepIn()
    else:
        stayInBed()

def outOfBedRush():
    print ("You don't have time to get ready for school you throw on some clothes and")
    print ("you run outside and realize you don't have your car keys. You will...")
    answer = input("Input 1 to run for your car keys and rush for school, input 2 to not go to school\n")
    if answer == "1":
        rushToSchool()
    elif answer == "2":
        sleepIn()
    else:
        print ("Invalid input")
        outOfBedRush()

def rushToSchool():
    print ("You sprint back inside grab your keys and head to school.")
    input ("Hit enter to continue\n")
    school()
    
def sleepIn():
    print ("You decide that you're too good for school.")
    print ("Good for you! What will you do with your day?")
    answer = input("Input 1 to pick up your girlfriend from school, input 2 to sleep for the entire day\n")
    if answer == "1":
        pickUpGirlfriend()
    elif answer == "2":
        sleepEntireDay()
    else:
        print ("Invalid input")
        sleepIn()
    
def sleepEntireDay():
    print ("You find it in your best interest to not do anything today.")
    print ("Are you sure?")
    answer = input("Input yes or no\n")
    if answer == "yes" or answer == "Yes":
        giveUpEnd()
    elif answer == "no" or answer == "No":
        sleepIn()
    else:
        print ("Invalid input")
        sleepEntireDay()

def giveUpEnd():
    print ("Well then... THE END")
    input("Hit enter to exit")

def pickUpGirlfriend():
    print ("You go and pick up your girlfriend from school.")
    print ("When she gets in the car you remember. You forgot about your anniversary!")
    print ("What will you do? Think quick!")
    answer = input("Input 1 to take her to the movies and wing it the rest of the night,input 2 to apologize and explain why you forgot\n")
    if answer == "1":
        lameMovieEnd()
    elif answer == "2":
        begForMercyEnd()

def lameMovieEnd():
    print ("You see Avengers 5...")
    print ("It's terrible.")
    print ("The rest of the night is spent doing boring things and your girlfriend leaves you... THE END")
    input("Hit enter to end game")

def begForMercyEnd():
    print ("What did you do!?")
    print ("She didn't know that you forgot! But now she's furious.")
    print ("She one punches you into another realm.")
    input("Hit enter to accept death")
    butThen()

def butThen():
    input("but then... (hit enter to continue)")
    start()

def getOutOfBed():
    print("You are out of bed. You can get back in bed, get ready for school, or open your window.")
    answer = input("Input 1 to get back in bed, 2 to get ready for school, 3 to open your window\n")
    if answer == "1":
        stayInBed()
    elif answer == "2":
        getReady()
    elif answer == "3":
        openWindow()

def openWindow():
    print ("You open your window. What would you like to do?")
    answer = input ("Input 1 to prepare for school, input 2 to climb onto roof\n")
    if answer == "1":
        getReady()
    elif answer == "2":
        climbOnRoof()
    else:
        print ("Invalid input")
        openWindow()

def climbOnRoof():
    global stars
    print ("What are you doing!? You need to get ready!")
    print ("Get your as—   Wait what's that?")
    print ("You see a shimmer on the edge of your roof. You pick it up.")
    print ("It's a power star! It seems it crashed into your house while you were sleeping.")
    print ("you pick it up and prepare for your day.")
    stars = stars + 1
    input("Hit enter to continue")
    getReady()

def getReady():
    print ("You've eaten breakfast, you've showered and brushed you're teeth,")
    print ("you've put on school appropriate clothes. you have 10 minutes to spare, you will...")
    answer = input("Input 1 to head to school early, input 2 to play video games\n")
    if answer == "1":
        headToSchoolEarly()
    elif answer == "2":
        playVideoGames()
    else:
        getReady()

def playVideoGames():
    print ("You feel like you deserve to play games for the 10 minutes you have.")
    print ("What would you like to play?")
    answer = input("Input 1 to play Super Mario 64, input 2 to play Beat Saber, input 3 to not play video games\n")
    if answer == "1":
        superMario64()
    elif answer == "2":
        beatSaber()
    elif answer == "3":
        getReady()
    else:
        playVideoGames()

def superMario64():
    global stars
    global time
    print ("You play Super Mario 64 for 10 minutes and collect 4 whole stars.")
    print ("It's time to go to school.")
    stars = stars + 4
    time = "onTime"
    answer = input("Input 1 if you would like to walk to school, input 2 if you would like to bus to school\n")
    if answer == "1":
        walk()
    elif answer == "2":
        bus()
    else:
        superMario64()

def beatSaber():
    global time
    print ("You play Beat Saber.")
    print ("unfortunately, you get so into it that you accidentally")
    print ("smash your head into a wall and are knocked out for 15 minutes.")
    time = "late"
    answer = input("Input 1 if you would like to walk to school, input 2 if you would like to bus to school\n")
    if answer == "1":
        walk()
    elif answer == "2":
        bus()
    else:
        beatSaber()

def headToSchoolEarly():
    global time
    print ("You decide to head to school early, how would you like to get there?")
    time = "early"
    answer = input("Input 1 if you would like to walk to school, input 2 if you would like to bus to school\n")
    if answer == "1":
        walk()
    elif answer == "2":
        bus()
    else:
        headToSchoolEarly()

def walk():
    global spider
    spider = True
    print ("It's a nice day out, you decide to walk.")
    print ("On your way to school you encounter a spider, will you kill it?")
    answer = input("Input 1 to kill it, input 2 to not kill it\n")
    if answer == "1":
        murderer()
    elif answer == "2":
        notMurderer()
    else:
        walk()

def murderer():
    global rain
    print ("It begins to rain, what a monster you've become.")
    rain = True
    input("You continue to school, hit enter")
    school()

def notMurderer():
    global rain
    print ("The spider waves at you and jumps off into the distance.")
    rain = False
    input("You continue to school, hit enter")
    school()
    
def bus():
    global stars
    global item
    print ("You decide to take the bus. A strange man with golden yellow shards in")
    print ("his beard approaches you after the bus doors close,")
    print ("he asks, 'Would you like to make a deal? A star for an item?'.")
    print ("You look very confused. But your confusion is put to a rapid pause when the man says...")
    if stars == 1:
        print ("I can smell it! I know you have one!")
        print ("It's not just any old item, it is literally ANY item!")
        print ("but it has a ONE TIME USE, you can turn this item into ANY other possible item! Deal?")
        answer = input("Yes or No")
        if answer == "yes" or answer == "Yes":
            stars = stars - 1
            item = item + 1
            input("You get the item as he snaches the star, hit enter to continue to school")
            school()
        elif answer == "no" or answer == "No":
            input("You don't take the deal, hit enter to continue to school")
            school()
        else:
            bus()
    elif stars > 1:
        print ("I can smell them! I know you have some!")
        print ("It's not just any old item, it is literally ANY item!")
        print ("but it has a ONE TIME USE, you can turn this item into")
        print ("ANY other possible item! Deal?")
        answer = input("Yes or No")
        if answer == "yes" or answer == "Yes":
            stars = stars - 1
            item = item + 1
            input("You get the item as he snaches the star, hit enter to continue to school")
            school()
        elif answer == "no" or answer == "No":
            input("You don't take the deal, hit enter to continue to school")
            school()
        else:
            bus()
    else:
        print ("Never mind, you don't have any.")
        print ("I thought you might have the potential")
        print ("of earning some... go away")
        input("Hit enter to continue to school")
        school()

def school():
    global rain
    global spider
    global item
    global time
    print ("You made it! You're at school.")
    print ("You see your girlfriend walking down the hallway.")
    print ("She sure is beutif—  WAIT! You completely forgot!")
    print ("It's your anniversary! What will you do?")
    answer = input("Input 1 to run to her with open arms, 2 to run, 3 to hide\n")
    if answer == "1":
        print ("You run over to her")
        if rain == True:
            print ("She is furious with you, You're soaking...")
            print ("and you have the eyes of a murder. How dare you!")
            print ("She one punches your stomach into another realm.")
            input("Hit enter to accept death")
            butThen()
        elif item == 1:
             print ("She is happy to see you! She walks over.")
             input("Hit enter to continue")
             bestEnd()
        elif rain == False and spider == True:
            print ("she walks to you with a warming smile.")
            print ("out of the corner of your eye you see it, the spider from earlier!")
            print ("He's right next to you sitting on the open window sill.")
            print ("He sneaks a fully wrapped gift into your hand and gives you a wink with half of his eyes.")
            input("Hit enter to continue")
            bestEnd()
        elif time == "late":
            print ("She is furious with you, You're late and you didn't even buy her anything.")
            print ("How dare you! She one punches your stomach into another realm.")
            input("Hit enter to accept death")
            butThen()
        elif item == 0:
            print("She is furious with you, You didn't even buy her anything.")
            print ("How dare you! She one punches your stomach into another realm.")
            input("Hit enter to accept death")
            butThen()
        else:
            print ("something went terribly wrong you one punch yourself into another realm.")
            input("Hit enter to accept death")
            butThen()
    elif answer =="2":
        run()
    elif answer == "3":
        hide()
    else:
        print("Invalid input")
        school()

def run():
    print("You run, scared for your life.")
    print("Your girlfriend catches up to you and because you ran from her,")
    print("she one punches you into another realm.")
    input("Hit enter to accept death")
    butThen()

def hide():
    print("You hid in the nearest locker, luckily she didn't see you...")
    print("unfortunately, her sense of smell is incredible due to her")
    print("connection with the Twelve Demons of the east.")
    print("She smells you as she walks past. She is livid and one punches you through the locker.")
    input("Hit enter to accept death")
    butThen()

def bestEnd():
    global stars
    global spider
    print("Congratulations!")
    print("You give your girlfriend a gift and you both")
    print("spend the rest of the day at an amusement park! YOU WIN!!")
    if stars == 5 and spider == True:
        print("You got the best possible end! you've obtained 5 stars and made a new frind. GREAT JOB!")
        input("Hit enter to exit")
    else:
        input("Hit enter to exit")


start()

