# Python
# Choose your own Adventure game
# Gabriel Hellebrand

import sys
import time
#time delay effect
a=1
b=0.05  

#first level

def intro ():
    print1="That's great! Let's play!\n"
    time.sleep(a)
    for character in print1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    print2= "You are Santa's favorite elf nicknamed Santa's little helper and you're working in a sweatshop along with all of the other little elves.\n"
    time.sleep(a)
    for character in print2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print3="The Soviet Union National Anthem blasts on repeat in the North Pole sweatshop at a deafening volume.\n"
    time.sleep(a)
    for character in print3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print4= "It hurts your little commie elf ears.\n"
    time.sleep(a)
    for character in print4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print5="All is well in Santa's sweatshop, except for the fact that Rudolph recently has gotten into Santa's favorite bottle of vodka.\n" 
    time.sleep(a)
    for character in print5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print6="Since then Rudolph has become a heavy alchoholic and has gotten a very red nose from all of the drinking that he's been doing.\n"
    time.sleep(a)
    for character in print6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print7="Rudolph with his nose so bright isn't flying any sleighs tonight.\n" 
    time.sleep(a)
    for character in print7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print8="One day, Rudolph stumbles into the elf sweatshop looking dazed and confused.\n" 
    time.sleep(a)
    for character in print8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print9="Rudolph's very dizzy and seems to have lost his balance. He falls on all fours.\n" 
    time.sleep(a)
    for character in print9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print10="From here you have three options.\n"
    time.sleep(a)
    for character in print10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    
    print()
    print11= "Option 1: BOOP RUDOLPH IN THE NOSE TO SEE IF IT CHANGES COLOR.\n"
    time.sleep(a)
    for character in print11:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print12="Option 2: TAKE RUDOLPH TO THE VET FOR SUSPECTED ALCHOHOL POISONING.\n"
    time.sleep(a)
    for character in print12:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print13= "Option 3: TELL RUDOLPH TO GO INTO REHAB. \n"
    time.sleep(a)
    for character in print13:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    first_option= input("Which option will you choose? [1/2/3]: ")
    if first_option== "1":
        print()
        option1()
    elif first_option=="2":
        print()
        option2()
    elif first_option=="3":
        print()
        option3()  
    else:
       print14="Rudolph dies from alchohol poisioning.\n"
       print()
       for character in print14:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b) 
        main()
    #second level
def option1():
        print122="Unfortunatly Rudolph's nose did not change color.\n Instead Rudolph boops you in the nose with his hooves sending you to the hospital.\n"
        time.sleep(a)
        for character in print122:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print123="You get no visitors in the hospital as no one is allowed outside of the sweatshop.\n"
        time.sleep(a)
        for character in print123:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print124="One day, a visitor arrives.\n"
        time.sleep(a)
        for character in print124:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print125="The visitor tries to recruit you into an MLM scheme selling essential oils.\n"
        time.sleep(a)
        for character in print125:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print126="The visitor tells you that last month she made over a thousand dollars.\n"
        time.sleep(a)
        for character in print126:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print127="What do you do?\n"
        time.sleep(a)
        for character in print127:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print()
        print128="Option 1: JOIN AN MLM SCHEME AND BECOME A #ELFBOSS.\n"
        time.sleep(a)
        for character in print128:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print129="Option 2: TELL THE VISITOR THAT THEY'VE GOT TO PUMP THOSE NUMBERS UP THOSE ARE ROOKIE NUMBERS.\n"
        time.sleep(a)
        for character in print129:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)                
        fifth_option=input ("Which path will you choose [1/2]: ")
        if fifth_option== "1":
                option1_1()
        elif fifth_option== "2":
                option1_2()   

def option1_1():
        print130="You join the MLM and you magically recover from all of your ailments\n thanks to the power of those essential oils.\n"
        time.sleep(a)
        for character in print130:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print131="You go back to Santa's sweatshop and now you only speak in annoying emojis.\n"
        time.sleep(a)
        for character in print131:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print132="The essential oils have given you the power to change your face into emojis somehow.\n"
        time.sleep(a)
        for character in print132:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print133="The only words you can speak in english are #bosself and #elfboss.\n"
        time.sleep(a)
        for character in print133:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print134="Rudolph organizes an intervention for you and your newfound MLM.\n"
        time.sleep(a)
        for character in print134:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print135="Rudolph tells you that you have a problem.\n"
        time.sleep(a)
        for character in print135:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print136="Santa comes out of his office annoyed that the group chat for the North Pole has been filled with you \n sending annoying emojis and writing about how you have become a #bosself.\n"
        time.sleep(a)
        for character in print136:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print137="Santa's workshop casts a vote to banish you to the South Pole.\n"
        time.sleep(a)
        for character in print137:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print138="The vote is unainomous and you are banished to the South Pole.\n"
        time.sleep(a)
        for character in print138:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print139="You're alone with only penguins to keep you company, and Rudolph is still an alchoholic.\n"
        time.sleep(a)
        for character in print139:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        main()
def option1_2(): 
        print141="The visitor wishes you the best and she hopes that you get well soon.\n"
        time.sleep(a)
        for character in print141:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print142="The visitor leaves, that night you die alone, and unloved.\n"
        time.sleep(a)
        for character in print142:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print143="Unfortunatly Rudolph is still an alchoholic and you die alone.\n"
        time.sleep(a)
        for character in print143:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        main()

def option2():
        print89="You take Rudolph to the vet.\n"
        time.sleep(a)
        for character in print89:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)

        print90="The vet tells you that Rudolph's liver and kidneys are almost completely destroyed from the amount of alchohol he's consumed.\n"
        time.sleep(a)
        for character in print90:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print91= "The vet recommends that you take Rudolph to alchoholics anonymous and have him change his ways.\n"
        time.sleep(a)
        for character in print91:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print92="Rudolph tells the vet and you that that wasn't an option.\n"
        time.sleep(a)
        for character in print92:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print93="Rudolph tells you, 'I need your liver, elf-man'.\n"
        time.sleep(a)
        for character in print93:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print94="The vet tells Rudolph to not be so hasty before asking if you could give Rudolph your liver and kidneys.\n"
        time.sleep(a)
        for character in print94:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print95="You tell the vet that he of all people should know that elves and reindeer aren't compatable when trading internal organs.\n"
        time.sleep(a)
        for character in print95:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print96="You take Rudolph to alchoholics anonymous.\n"
        time.sleep(a)
        for character in print96:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print97="You wait in the car for Rudolph to finish his Alchoholics Anonymous meeting, it's taking a long time.\n"
        time.sleep(a)
        for character in print97:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print98="You decide to go into the meeting because you suspect that Rudolph is causing trouble and being a public menace.\n"
        time.sleep(a)
        for character in print98:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print99="You go into the Alchoholics Anonymous meeting and find Rudolph flirting with a female reindeer.\n"
        time.sleep(a)
        for character in print99:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print100="What do you do?\n"
        time.sleep(a)
        for character in print100:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print101="From here you have two options.\n"
        time.sleep(a)
        for character in print101:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print102="Option 1: LET RUDOLPH FLIRT WITH THE REINDEER.\n"
        time.sleep(a)
        for character in print102:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print103="Option 2: TELL THE REINDEER THAT RUDOLPH WAS FLIRTING WITH THAT RUDOLPH FORGOT HIS ANTI ITCH CREAM.\n"
        time.sleep(a)
        for character in print103:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        fourth_option=input("Which path will you choose [1/2]: ")
        if fourth_option== "1":
                option2_1()
        if fourth_option== "2":
                option2_2()

def option2_1():
        print104="Rudolph continues flirting with the female reindeer.\n"
        time.sleep(a)
        for character in print104:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print105="A tough reindeer arrives and tells Rudolph to stop flirting with the female reindeer as that was his fiance.\n"
        time.sleep(a)
        for character in print105:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print106="Rudolph tells the guy, 'It's ok, I'm incredibly drunk.'\n"
        time.sleep(a)
        for character in print106:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print107="The tough reindeer pulls out a gun and shoots Rudolph.\n"
        time.sleep(a)
        for character in print107:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print108="Rudolph dies, you and the other elves have a funeral.\n"
        time.sleep(a)
        for character in print108:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print109="You couldn't save Rudolph from his alchoholism or himself.\n"
        time.sleep(a)
        for character in print109:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print() 
        main()

def option2_2():
        print111="The female reindeer told Rudolph that that wasn't a problem and that she had her own anti-itch cream.\n"
        time.sleep(a)
        for character in print111:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print112="Rudolph vomits disgusted at the fact that the female Reindeer he was flirting with carried anti-itch cream.\n"
        time.sleep(a)
        for character in print112:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print113="Rudolph is extremely shallow.\n"
        time.sleep(a)
        for character in print113:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print114="Rudolph tells you that he needs a drink to clear his head from this day of excitement.\n"
        time.sleep(a)
        for character in print114:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print115="Rudolph and you go to the bar.\n"
        time.sleep(a)
        for character in print115:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print116="The two of you drink excessively.\n"
        time.sleep(a)
        for character in print116:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print117="The next morning,\n"
        time.sleep(a)
        for character in print117:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print118="You wake up dazed and confused in a bathtub filled with ice.\n"
        time.sleep(a)
        for character in print118:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print119="You shout at the top of your lungs, 'Rudolph where's my kidneys?'\n"
        time.sleep(a)
        for character in print119:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print120="Not only did you not save Rudolph from his alchoholism but you lost your kidneys as well.\n"
        time.sleep(a)
        for character in print120:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        main()
    


def option3():
        print15="Rudolph tells you that he doesn't want to go to rehab. You tell Rudolph that he doesn't have a choice in the matter.\n"
        time.sleep(a)
        for character in print15:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print16="You take Rudolph to alchoholics anonymous.\n"
        time.sleep(a)
        for character in print16:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print17="Rudolph leaves you in the car but makes sure to leave the window slightly open as it's a hot day of twenty degrees below zero.\n" 
        time.sleep(a)
        for character in print17:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print18="It's been a while and you decide to check up on Rudolph to make sure he hasn't gotten into trouble yet.\n"
        time.sleep(a)
        for character in print18:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print19="As he often does...\n"
        time.sleep(a)
        for character in print19:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print20="You go into the Alchoholics Anonymous meeting and find Rudolph hitting on a female reindeer asking for her number.\n"
        time.sleep(a)
        for character in print20:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print21="What do you do.\n"
        time.sleep(a)
        for character in print21:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)    
        print()
        print22="Option 1: TAKE RUDOLPH AND YOURSELF BACK TO THE NORTH POLE AND TELL SANTA THERE'S NO HOPE FOR RUDOLPH TO RECOVER FROM HIS VULGAR ALCHOHOLISM. \n "
        time.sleep(a)
        for character in print22:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print23="Option 2: TELL THE REINDEER THAT RUDOLPH WAS FLIRTING WITH THAT RUDOLPH FORGOT HIS ANTI ITCH CREAM. \n "
        time.sleep(a)
        for character in print23:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print24="Option 3: JOIN AN MLM SCHEME AND BECOME A #ELFBOSS. \n "
        time.sleep(a)
        for character in print24:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print25="Option 4: BOOP RUDOLPH ON THE NOSE TO SEE IF IT CHANGES COLOR. \n "
        time.sleep(a)
        for character in print25:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print26="Option 5: TAKE RUDOLPH TO THE VET. \n "
        time.sleep(a)
        for character in print26:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        second_option=input("Which path would you choose? [1/2/3/4/5]: ")
        if second_option=="2":
                option2_2()
        elif second_option=="3":
                option1_1()
        elif second_option=="4":
                option1()
        elif second_option=="5":
                option2()
        else:
                print()
        print27="Going back to the North Pole, Santa waits for you and Rudolph at the sweat shop.\n"
        time.sleep(a)
        for character in print27:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print28="Santa's arms are folded, he's bald, covered in tattoos, yoked, and has a large beard. \n"
        time.sleep(a)
        for character in print28:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print29="'Where have the two of you been...?'\n"
        time.sleep(a)
        for character in print29:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print30="Rudolph tells Santa you were the one who stole his vodka and that Rudolph caught you red handed.\n"
        time.sleep(a)
        for character in print30:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print31="Everything was ok though because Rudolph being the good reindeer that he was, was taking you to alchoholics anonymous.\n"
        time.sleep(a)
        for character in print31:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print32="Santa tells you and Rudolph, 'I'm not angry, just disappointed.'\n"
        time.sleep(a)
        for character in print32:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print33="You go into Santa's sweatshop, Soviet music blaring and you start making toys.\n"
        time.sleep(a)
        for character in print33:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print34="You couldn't believe that Rudolph would betray you like that and after everything you did for him too.\n"
        time.sleep(a)
        for character in print34:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print35="You are no longer Santa's favorite little Elf.\n"
        time.sleep(a)
        for character in print35:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print36="Later, a neighbor elf is struggling to put together a toy jack in the box.\n"
        time.sleep(a)
        for character in print36:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print37="One of the elf supervisors tells the neighbor elf that he's behind schedule.\n"
        time.sleep(a)
        for character in print37:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print38="The Elf tells him that he'll do better next time.\n"
        time.sleep(a)
        for character in print38:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print39="Option 1: HELP THE STRUGGLING ELF.\n"
        time.sleep(a)
        for character in print39:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print40="Option 2: DON'T HELP THE STRUGGLING ELF.\n"
        time.sleep(a)
        for character in print40:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        third_option= input("Which path would you take [1/2]: ")
        if third_option== "1":
            print()
            option3_1()
        elif third_option== "2":
            print()
            option3_2()
        else:
            print("Santa is outside having just bought a new Mercedes and doing donuts on the snow.\n") 
            print("Unfortunatly, the traction on the tires isn't enough and Santa's car spins out of control killing everyone.\n")
#third level
def option3_1():
        print41="You stand up for the struggling Elf and tell the supervisor that you could help him catch up.\n"
        time.sleep(a)
        for character in print41:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print42="The Elf supervisor tells you that he'll allow this but that he will become your responsibility and that if you don't deliver...\n"
        time.sleep(a)
        for character in print42:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print43="Santa's not going to give you any milk and cookies this year.\n"
        time.sleep(a)
        for character in print43:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print44="dum dum dum.\n"
        time.sleep(a)
        for character in print44:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print45="You help the elf make toys and he tells you, 'Santa is not the jolly old man we all think he is.'\n"
        time.sleep(a)
        for character in print45:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print46="You ask, 'what makes you say that?'\n"
        time.sleep(a)
        for character in print46:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print47="The elf tells you, 'Before every Christmas, Santa gets two large bags of money from bald men covered in tattoos.'\n"
        time.sleep(a)
        for character in print47:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print48="You ask how much money Santa has in the bags.\n"
        time.sleep(a)
        for character in print48:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print49="You're new elf friend tells you, 'I don't know, he measures money in the amount of bags not dollars.'\n"
        time.sleep(a)
        for character in print49:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print50="The elf tells you that he's also seen Santa have two lists, those who are naughty and those who are nice.\n" 
        time.sleep(a)
        for character in print50:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print51="You tell your elf friend, 'yeah, everyone knows that.'\n"
        time.sleep(a)
        for character in print51:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print52="You're elf friend tells you, 'Do you know anyone whose ever been on the naughty list?'\n"
        time.sleep(a)
        for character in print52:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print53= "You shake your head no. You're elf friend tells you that you know them, they just die under mysterious circumstances, or disappear, or they have there photos and any mention of them erased from history.\n"
        time.sleep(a)
        for character in print53:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print54= "You're elf friend believes that Santa is in the Russian mafia and is using the North Pole as a front for money laundering.\n"
        time.sleep(a)
        for character in print54:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print55="You tell the elf that you doubt that Santa has any mafia connections but that it was good talking to him.\n"
        time.sleep(a)
        for character in print55:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print56="The next day,\n"
        time.sleep(a)
        for character in print56:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print57="You're elf buddy died by suicide last night by shooting himself in the back of the head.\n"
        time.sleep(a)
        for character in print57:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print58="You launch a secret investigation into Santa Clause's office, setting up spy cameras, and tracking Santa's wherabouts at all times.\n"
        time.sleep(a)
        for character in print58:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print59="Upon investigating the files and tapes you discover that Santa's been talking to a guy named Ivan on the phone in Russian about the money laundering scheme.\n"
        time.sleep(a)
        for character in print59:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print60="You go to the police to tell them what you've found.\n"
        time.sleep(a)
        for character in print60:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print61="Unfortunatly, none of the officers at the time speak any Russian.\n"
        time.sleep(a)
        for character in print61:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print62="Detective Alexei Petrov checks into the police station, he is not able to speak fluent Russian.\n However, Hank from accounting is able to, you talk to Hank. He listens to the phone conversation and is able to understand everything.\n"
        time.sleep(a)
        for character in print62:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print63="Hank tells the officers that sure enough Santa Claus was using his workshop as a front to lander money for the mob.\n" 
        time.sleep(a)
        for character in print63:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print64="Santa gets arrested, and Hank thanks you for the fact that you stopped a major Russian Mafia scheme.\n"
        time.sleep(a)
        for character in print64:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print65="Rudolph after hearing the news of Santa's Russian mob connection tells you that he promises that he'll never drink again.\n"
        time.sleep(a)
        for character in print65:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print66="Thanks for playing! You've won the game!\n"
        time.sleep(a)
        for character in print66:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print()
        print()

def option3_2():
        print68="The Elf supervisor tells him that there isn't going to be a next time before pulling out a gun.\n"
        time.sleep(a)
        for character in print68:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print69="The elf supervisor shoots the elf and tells you and the other elves to clean up the mess before Santa arrives.\n"
        time.sleep(a)
        for character in print69:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print70="You and the other elves find a place to bury the elf body in the elf graveyard outside of the sweatshop.\n"
        time.sleep(a)
        for character in print70:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print71="Santa arrives at the sweatshop and announces the bad news that Blitzen has broken his leg.\n"
        time.sleep(a)
        for character in print71:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print72="However, due to helping you with your alchoholism Santa has decided to reward Rudolph by having him become the new leader of the sleigh.\n"
        time.sleep(a)
        for character in print72:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print73="All of the elves cheer at this good news and they tell you that Rudolph is such a good reindeer for helping you with your alchoholism.\n"
        time.sleep(a)
        for character in print73:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print74="Christmas Eve arrives.\n"
        time.sleep(a) 
        for character in print74:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print75="Rudolph is incredibly drunk having had a full bottle of Jack Daniels, a bottle of fireball whiskey, and a large soda.\n"
        time.sleep(a)
        for character in print75:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print76="Santa asks if Rudolph was, 'Ready to lead the sleigh tonight?'\n"
        time.sleep(a)
        for character in print76:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print77="Rudolph replied, 'Santa as I'll ever be, ready.\n"
        time.sleep(a)
        for character in print77:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print78="There's no doubt about it, Rudolph was incredibly drunk.\n"
        time.sleep(a)
        for character in print78:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print79="Santa pats Rudolph on the antlers and tells him, 'I like your enthusiasm Rudolph.'\n"
        time.sleep(a)
        for character in print79:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print80="Midnight arrives and Santa loads the sleigh.\n"
        time.sleep(a)
        for character in print80:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print81="Take off is a little shaky, but they manage to get there footing and fly straight. Santa asked if everything was ok up there.\n"
        time.sleep(a)
        for character in print81:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print82="They fly through New York City, however there's a lot of skyscrapers and Rudolph is feeling very dizzy.\n"
        time.sleep(a)
        for character in print82:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print83="They are heading for the empire state building, Santa realizes too late that Rudolph is drunk.\n"
        time.sleep(a)
        for character in print83:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print84="Santa says, 'Ho, ho... no' as the sleigh crashes into the empire state building. Killing Santa and all of the reindeer.\n"
        time.sleep(a)
        for character in print84:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print85="Later a news report, announces that Santa's been killed after a deadly crash into the empire state building.\n"
        time.sleep(a)
        for character in print85:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print86= "It is discovered that one of Santa's reindeer, Rudolph, was found to have been very drunk at the time, his blood alchohol content being off the charts.\n"
        time.sleep(a)
        for character in print86:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print87="Another news report states that Santa allegedly had ties with the Russian mafia who would use Santa's workshop as a front to launder money.\n"
        time.sleep(a)
        for character in print87:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print88="Thanks for playing, you've completed the game, play again to see if you get a different ending from last time.\n"
        time.sleep(a)
        for character in print88:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
        print()
        print()
        print()
        main()
def main():
#Main Function ###
        print()
        print()
        print("      ################################")
        print("      #                              #")
        print("      # Rudolph The Drunken Reindeer #")
        print("      #                              #")
        print("      ################################")
        print()
        print()
        start_game= input("Hello, do you want to play a game? [y/n]: ")
        if start_game=="n" or start_game== "N":
                print("Ok bye. ")
                time.sleep(3)
        elif start_game=="y" or start_game=="Y":
                intro()
main()