# =========================================== STAGE 1 =============================================================
# =========================================== ALEX'S PART =========================================================
# Importing library
from random import randint
import time,os,sys
import sys
from time import sleep


# Function for typing print
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

# Function for typing Input
def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()  
    return value  

def the_knights_conquest():

    # A function starting the game with titles and headings. First question asking the player to save the princess and for their name.
    def opening_question(): 
        # Title
        print("""===============================================================================""")
        print("""\33[93m
__  _  ____   ____   ____  __ __  ______  __   _____        __   ___   ____    ___   __ __    ___  _____ ______ 
|  |/ ]|    \ |    | /    ||  |  ||      ||  | / ___/       /  ] /   \ |    \  /   \ |  |  |  /  _]/ ___/|      |
|  ' / |  _  | |  | |   __||  |  ||      ||_ |(   \_       /  / |     ||  _  ||     ||  |  | /  [_(   \_ |      |
|    \ |  |  | |  | |  |  ||  _  ||_|  |_|  \| \__  |     /  /  |  O  ||  |  ||  Q  ||  |  ||    _]\__  ||_|  |_|
|     ||  |  | |  | |  |_ ||  |  |  |  |       /  \ |    /   \_ |     ||  |  ||     ||  :  ||   [_ /  \ |  |  |  
|  .  ||  |  | |  | |     ||  |  |  |  |       \    |    \     ||     ||  |  ||     ||     ||     |\    |  |  |  
|__|\_||__|__||____||___,_||__|__|  |__|        \___|     \____| \___/ |__|__| \__,_| \__,_||_____| \___|  |__|  
                                                                                                                  

  //\\
  | |
  |.|
  |.|
  |:|      __
,_|:|_,   /  )
  (Oo    / _I_
   +\ \  || __|
      \ \||___|
        \ /.:.\-
         |.:. /-----
         |___|::oOo::|
         /   |:<_T_>:|
        |_____\ ::: /
         | |  \ \:/
         | |   | |
         \ /   | \___
         / |   \_____
         `-'""")


  

        # Introduction to the game
        print("""=================================================================================""")
        typingPrint("A long-long time ago, in a kingdom far-far way a princess was kidnapped by an Evil Elf and taken to a location unknown.\nYou, a brave Knight, have been summoned by the King to search and save his daughter. Your reward will be her hand in marriage.\n")

        typingPrint("You later learn that there are some strange things happening in a Dark Forest outside the kingdom and set off in search for answers.\n")
        
        # First question
        question = typingInput("Can you save her? (Yes or No?)\n")

        if question.lower() == "yes":
            typingPrint("Her life is in your hands!\n")
        else:
            typingPrint("You have let your name down, You'll live the rest of your days in shame!\n Reloading game in 3......2.....1...")
            opening_question()

    opening_question()

    # ===========================================================================================

    print("""===============================================================================""")

    # Name of player input
    name = str(typingInput("Enter your name Player: "))
    print("""===============================================================================""")

    # Second question in the game asking if the player would like to enter the hut or not. Two outcomes, one to continue to meet the witch. The other to be sent back to the start.
    def hut_question():
        typingPrint(f"\33[92m {name}, you have entered The Dark Forest, stay vigilante as the witch haunts this ghostly forest.\n")
        typingPrint("In the middle of the forest, you found a lone hut. What do you do?\n")
        
        # Hut question
        question = typingInput("Are you going inside the hut or not? (Yes or No?)\n")
        print("""===============================================================================""")
        # If statement finding the correct answer
        if question.lower() == "yes" :
            typingPrint ("As you enter you notice a huge cauldron boiling in the corner. You begin to hear an abrasive, hi-pitched laughter circling the room. It's the witch!")
            print("""===============================================================================""")
            print("""\33[95m

                            
                                    _.--'    /
                                .-'        /
                                .'          |
                            .'           /
                            /_____________|
                        /`~~~~~~~~~~~~~~/
                        /`               /
        ____,....----'/_________________|---....,___
    ,--""`             `~~~~~~~~~~~~~~~~~~`           `""--,
    `'----------------.----,------------------------,-------'`
                _,'.--. \                           |
                .'  (o   ) \                        |
                c   , '--'  |                        /
            /    )'-.    \                       /
            |  .-;        \                       |
            \_/  |___,'    |                    .-'
            .---.___|_      |                   /
            (          `     |               .--'
            '.         __,-'\             .'
            `'-----'`      \        __.'
                            `-..--'`
    """)
            print("""===============================================================================""")
            typingPrint("She looks down her long crooked nose and begins to ask why you are bothering her?\n")
            typingPrint(f"You reply that you are a Knight and your name is {name} and you are in search of the missing princess.\n")
            typingPrint(f"She says that she can help you as to where the princess is. However, you need to have 'Golden Nuggets' to help you save her.\nShe tells you 'If you solve my four challenges, you might win some golden nuggets. Refuse Sir {name} and I shall turn you in to a toad.'\n")
        
        # Else statement finding the wrong answer
        else:
            print("""===============================================================================""")
            typingPrint(f"{name}, You have failed your mission and The King. You needed to win some 'Golden Nuggets' to reach the end. Go back to the start of the game.\nRestarting the game in 3...2...1...")
            opening_question()
            hut_question()
            
            
    hut_question()

    # =============================================================================================================

    # Beginning of the chance question, used at the end of the stage to give the user an option to have the full amount or none at all in a game of chance.
    def chance_question():
        global golden_nuggets
        number_chances = 1
        number_chances_max = 3
        highest_number = 10
        my_num = randint(1, highest_number)
        your_number = 0
        print("""===============================================================================""")
        typingPrint(f"I am choosing a number between 1 and {highest_number}\n")
        typingPrint(f"Guess in {number_chances_max} chances and you'll recieve all 100 golden nuggets!\n")
        # Its a loop to let the user play the game until they have used all their gos (number_chances_max)
        while your_number != my_num and number_chances <= number_chances_max:
            typingPrint(f"Chance number {number_chances}\n")
            your_number = int(input("Choose your number:\n"))
            # If the number entered is too small, it prints a message saying it's too small
            if your_number < my_num:
                number_chances += 1 
                typingPrint ("Your number is too small muahahah\n")
            # Elif statement if the number entered is too big, it prints a message saying it's too small
            elif your_number > my_num:
                number_chances += 1 
                typingPrint ("Your number is too big, You are losing your golden nuggets muahaha.\n")
            # Else statement printing the positive outcome when the number entered matches the random number between 1 - 10
            else:
                print("""===============================================================================""")
                typingPrint (f"Well done, you have found my number which is {my_num}, it only took you {number_chances} chances. \n You recieve 100 golden nuggets. Good luck on your expedition...\n")
                golden_nuggets = 100
                number_chances += 0 
            # If the number of chances is more than the permitted chances AND number isn't the same as the random number. It prints you have failed and gives user 0 golden nuggets.
        if number_chances > number_chances_max and your_number != my_num:
            print("""===============================================================================""")
            typingPrint(f"YOU HAVE FAILED!!! You recieve no golden nuggets you puny human.\n My number was {my_num}\n")
            golden_nuggets=0
            print(f"\033[1;33mCurrent Golden Nuggets is: {golden_nuggets}")
            


    # ===============================================================================================================================

    # Answers to the four questions below. A and b alternatives to cover if the user say a river or river. also lower. used to put their imput into lowercase.
    answer_1 = 15
    answer_2a = "river" 
    answer_2b = "a river"
    answer_3a = "cauldron"
    answer_3b = "a cauldron"
    answer_4a = "sandwich"
    answer_4b = "a sandwich" 
    golden_nuggets = 0

    # function for the main questions in the code
    def game_question():
        global golden_nuggets
        # The questions printed to the user with their answer
        print("""===============================================================================""")
        question_1 = typingInput("'Answer these questions my dear Knight ....\nQuestion 1.\n 'I have a bag of snakes for a potion, I give 3, and then half of what is left in the bag away. Yet I still have 6 snakes. How many did I have at the beginning?'\n")
        print("""===============================================================================""")
        question_2 = typingInput("Question 2.\n'What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?'\n")
        print("""===============================================================================""")
        question_3 = typingInput("Question 3.\n'Every Witch needs one of these. If she is to cast a spell Its what she makes her brew in that gives off an awful smell?'\n")
        print("""===============================================================================""")
        question_4 = typingInput("Question 4.\n'What kind of Witch lives on a beach?'\n")
        print("""===============================================================================""")
        # If answer is correct it gives 25 golden nuggets
        # point_1 = the points gained for question 1, point_2 for question 2 etc.
        if answer_1 == int(question_1):
            point_1 = 25
        # Else statement if they right anything other than the answer(s) they get 0 points
        else:
            point_1 = 0
        if answer_2a == question_2.lower() or answer_2b == question_2.lower():
            point_2 = 25
        else:
            point_2 = 0
        if answer_3a == question_3.lower() or answer_3b == question_3.lower():
            point_3 = 25
        else:
            point_3 = 0
        if answer_4a == question_4.lower() or answer_4b == question_4.lower():
            point_4 = 25
        else:
            point_4 = 0
        # uses global to get the golden_nuggets from outside the function
        global golden_nuggets 
        # golden nuggets is calculated by adding all four of the points together collected above
        golden_nuggets = point_1 + point_2 + point_3 + point_4
        typingPrint(f"You recieve {golden_nuggets} Golden Nuggets of a possible 100 from the witch.\n")
        # If golden nuggets = 100 then the user moves on to the next stage
        if golden_nuggets == 100:
            print("""===============================================================================""")
            typingPrint(f"Congratulations {name} You can continue past the witch with all the golden nuggets\n")
            # It will go to the next stage when all is put together here
        else:
            print("""===============================================================================""")
            typingPrint("\033[1;31mYou did not get all the golden nuggets the witch had to offer.\n \033[1;35mHowever, she offers you a chance to get all 100 Golden Nuggets.\n")
            print("""===============================================================================""")
            typingPrint("'Guess my number Knight.....\nUmmm.....I am thinking of a number between 1 and 10 if you guess my number in 3 trys I will give you all 100 golden nuggets\n If you don't guess my number you will end with nothing...'\n")
            # gives user the option to get all points or no points
            answer_6 = typingInput(f"Do you want to take a chance {name}? (Yes or No?)\n")
            
            # If statement is yes then they will be taken to the chance question game
            if answer_6.lower() == "yes" :
                chance_question()
                print("""===============================================================================""")
                typingPrint("The Witch tells you to leave her hut and be on your way. She tells you to go to the Swampland to look for more golden nuggets.")
            else:
                # It will go to the next stage when all is put together here
                typingPrint(f"Sad {name} you have won 0 golden nuggets more.\n Your current golden nuggets is {golden_nuggets}")
                print("""===============================================================================""")
                typingPrint(f"{name} ,you were not able to win any golden nuggets need to progress to the next stage.\nRestarting the game in 1......2.....3")
                golden_nuggets+=0
                
                opening_question()
        
        
    game_question()

    # ==================================================End of Part 1=============================================================================
        
    # ==================================================Part 2=============================================================================
        
    print("""===============================================================================""")

    print(""" 
    ______  __ __    ___       _____ __    __   ____  ___ ___  ____  
    |      ||  |  |  /  _]     / ___/|  |__|  | /    ||   |   ||    \ 
    |      ||  |  | /  [_     (   \_ |  |  |  ||  o  || _   _ ||  o  )
    |_|  |_||  _  ||    _]     \__  ||  |  |  ||     ||  \_/  ||   _/ 
    |  |  |  |  ||   [_      /  \ ||  `  '  ||  _  ||   |   ||  |   
    |  |  |  |  ||     |     \    | \      / |  |  ||   |   ||  |   
    |__|  |__|__||_____|      \___|  \_/\_/  |__|__||___|___||__|   
                                                                    """)

    print("""===============================================================================""")                                                               

    story_one="\033[1;32mUpon leaving the Dark Forest you travel to the Swamp Lands to look for more nuggets to break the curse.\nYou ride for three days and three nights and finally reach the swamp.\n"

    for char in story_one:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    def game_question_2():  
        global golden_nuggets
        text_two="\033[1;32mIn the middle of the dark swamp, you see a paddle boat. What would you do?\n"
        for char in text_two:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

        question = typingInput("\033[1;32mAre you going to swim to get the paddle boat? \n(Yes or No)\n")
        print("""===============================================================================""")
        for char in question:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

        if question.lower() == "yes":
            
            text_three="\033[1;32mYou swim to get the boat, but there is a monster in the swamp.\n A giant swamp monster named 'Swampy' grabs you in his hand. \n You tell him you came here looking for golden nuggets to break the princess's curse. \n If you want to pass, you must answer my question, said the monster.\n"
            print("""===============================================================================""")
            for char in text_three:
                sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()

            monster_question()
            
        else:
            print("""===============================================================================""")
            print("\033[1;32m'Wrong answer Knight. You can not go anywhere without answering my question.....muhahaha'\nSaid the Swamp monster laughing '.....Now answer my riddle.")

            monster_question()
        

    def monster_question():
            global golden_nuggets
            print("""===============================================================================""")
            print("\033[1;32mWhat is something when we take from it, will get much bigger?\n")
            question_1 = input("a)Debt\nb)A Hole\nc)River\nd)I dont Know\n")
            for char in question_1:
                    sleep(0.05)
                    sys.stdout.write(char)
                    sys.stdout.flush()
            if question_1 == "a" or question_1=="c" or question_1=="d":
                print("""===============================================================================""")
                text_four="\033[1;32mYour answer is wrong Knight, You get no golden nuggets from me.\n I will let you go just because I am a nice Monster. \n Your next answer lies at the mountain near the edge of the world.\n Go there and seek your fortune.\n"
                for char in text_four:
                    sleep(0.05)
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    golden_nuggets=golden_nuggets+0

                print(f"\033[1;33mCurrent Golden Nuggets is: {golden_nuggets}")
                
            
            else:
                print("""===============================================================================""")
                text_five="\033[1;32mHmmmm.... You are correct Knight.\nHere is your golden nuggets from me.\n You next answer lies at the mountain near the edge of the world. \nGo there and seek your fortune.\n"
                for char in text_five:
                    sleep(0.05)
                    sys.stdout.write(char)
                    sys.stdout.flush()

                golden_nuggets=golden_nuggets+100
                print(f"\033[1;33mCurrent Golden Nuggets is: {golden_nuggets}")

            

    game_question_2()     

# ==================================================End of Part 2=============================================================================
        
# ==================================================Part 3=============================================================================






    print("""===============================================================================""")
    text_story= "\033[1;36m After the Swamp Lands, you ride yet again for three days and three nights and reach the base of the mountain.\n And what lies infront of you ......  \n"

    #typewritter effect code it only worked for me if i put it for all texts in the code
    
    for char in text_story:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("""===============================================================================""")

    print("""  
______  ____    ___   _      _                  __  __  __ 
|      ||    \  /   \ | |    | |                |  ||  ||  |
|      ||  D  )|     || |    | |                |  ||  ||  |
|_|  |_||    / |  O  || |___ | |___             |__||__||__|
  |  |  |    \ |     ||     ||     | __  __  __  __  __  __ 
  |  |  |  .  \|     ||     ||     ||  ||  ||  ||  ||  ||  |
  |__|  |__|\_| \___/ |_____||_____||__||__||__||__||__||__|
                                                            
                                                                    


    """)
    print("""===============================================================================""")
    text_story="A Troll stands there guarding an entrance to a cave.\n'WHO DARES COME TO MY LAND' shouts the troll.\n'I am a Knight'you reply and tell him you came all this way to save the princess and is searching for golden nuggets.\nI will give you my golden nuggets if you can answer my riddle he says......'\n"

    for char in text_story:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("""===============================================================================""")
    text_story="\033[1;35m'I speak without sound, but you see what I say.\nI'm borrowed for free, but some chose to pay.\nMy truth is for learning, my lies are for play.\n What am I?\n"

    for char in text_story:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    #The first riddle question


    def game():
        #sun-fuction for the riddle
        def troll_path(): 
            global  golden_nuggets
            answer_1 = input("\033[1;35ma)Wind\nb)Stone\nc)Book\nd)Ghost\n:")
            for char in answer_1:
                    sleep(0.05)
                    sys.stdout.write(char)
                    sys.stdout.flush()

            #Multiple choise answers wrong answer gives 0 points.

            if answer_1.lower() == "a" or answer_1=="b" or answer_1=="d":
                print(f"\033[1;31m Sir {name} that is a wrong answer.")
                golden_nuggets += 0   
                print(f"\033[1;33m Current golden nuggets:{golden_nuggets}")
                next_stage()    
            
            else:
                print(f"\033[1;32m You are correct Brave Knight Sir {name} ")
                golden_nuggets += 100
                print(f"\033[1;33m Current golden nuggets:{golden_nuggets}")
                next_stage()  

            #chance to double the golden nuggets or to win again if not won previsoly

        #sub function for progressing
        def next_stage ():
            global score, golden_nuggets
            print("""===============================================================================""")
            text_story=" '\033[1;36mHmmm...' said the Troll.\n'You may go inside the cave and climb to the top of the tower, where the Evil Elf has your princess.' says the Troll.\nOr, I will give you another chance to try again to DOUBLE your Golden nuggets if you can answer another riddle. \n 'What would you do......'? "
            
            for char in text_story:
                sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
    
            answer_2=input("\033[1;36m Type:Yes or No ")
            print("""===============================================================================""")
            if answer_2.lower( )== "yes":
                text_story="\033[1;35m 'What can you catch, but not throw....?'\n"
                print("""===============================================================================""")
                for char in text_story:
                    sleep(0.05)
                    sys.stdout.write(char)
                    sys.stdout.flush()
                
                answer_3 = input("\033[1;35ma)Wind\nb)Stone\nc)Smoke\nd)Cold\n:")
                print("""===============================================================================""")
    # if answer is wrong
                if answer_3=="a" or answer_3=="b" or answer_3=="c":
                    print("\033[1;31m I am afriad that is a wrong answer\n")
                    golden_nuggets+=0
                    text_story=(f"\033[1;33m Current golden nuggets:{golden_nuggets}\n")
                    for char in text_story:
                        sleep(0.05)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    print("""===============================================================================""")
                    text_story="\033[1;36m You may go inside the cave and climb to the top of the tower, where the Evil Elf is with your princess.'  Says the Troll.\n He lets you pass him inside and you climb up the mountain to reach the top.\nThere on the top lies a tower........You see the Evil Elf....!!!!"
                    for char in text_story:
                        sleep(0.05)
                        sys.stdout.write(char)
                        sys.stdout.flush()
        #if answer is right
                else:
                    text_story="\033[1;32m Correct, Impressive...!!!\n"
                    for char in text_story:
                        sleep(0.05)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    golden_nuggets+=100
                    text_story=(f"\033[1;33m Current golden nuggets:{golden_nuggets}\n")
                    for char in text_story:
                        sleep(0.05)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    print("""===============================================================================""")
                    text_story="\033[1;36mTake this gold and go inside the cave and climb to the top of the tower, where the Evil Elf is with your princess.'  Says the Troll.\n He lets you pass him inside and you climb up the mountain to reach the top.\nThere on the top lies a tower........You see the Evil Elf....!!!! \n"
                    print("""===============================================================================""")
                    for char in text_story:
                            sleep(0.05)
                            sys.stdout.write(char)
                            sys.stdout.flush()  

            else:
                text_story=(f"\033[1;31mYou are a 'Chicken' Sir Knight {name}\n")
                for char in text_story:
                            sleep(0.05)
                            sys.stdout.write(char)
                            sys.stdout.flush()
                text_story=(f"\033[1;33m Current golden nuggets:{golden_nuggets}\n")
                for char in text_story:
                            sleep(0.05)
                            sys.stdout.write(char)
                            sys.stdout.flush()
                text_story=("\033[1;36m'Go inside the cave and climb to the top of the tower, where the Evil Elf is with your princess.'Says the Troll.\nHe lets you pass him inside and you climb up the mountain to reach the top.\nThere on the top lies a tower........You see the Evil Elf....!!!! \n")  
                print("""===============================================================================""")
                for char in text_story:
                            sleep(0.05)
                            sys.stdout.write(char)
                            sys.stdout.flush()
        
 

        
        
        troll_path()
        print("""
                    [_]___[_]__[_]___[_]
                    [__#__][__I_]__I__#]
                    [_I_#_I__#[__]__#__]
                      [_]_#_]__I_#_]
                      [I_|/ _W_ \|#]
                      [#_||{(")}||_]
                      [_I||{/~\}||_]
                      [__]|/\_/\||#]
                      [_I__I#___]__]
                      [__I_#_I___#_]
                      [#__I____]__I]
       .-.            __I_#__I__[_]
     __|=|__          [_#_[__#_]__#]
    (_/`-`\_)         [__#_I__[#_I_]
    //\___/\\         [_I__]__#_I__]
    <>/   \<>         [#__I__#_]__I]
     \|_._|/          [_I#__I___I_#]    .:.
      <_I_>            #__I__]_#___]   -=o=-
       |||            [_I__I#__]___]    ':'
    .  /_|_\         [__]#___][__#]//, \|/
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")
        def storyline(text):
            for character in text:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)

   
        print("""===============================================================================""")    
        storyline("The Evil Elf stood guarding the door to the tower.\n You tell him to open the door and release the princess or you shall fight him to the death.\n The Elf tells you 'No need to fight just yet, if you can given me 500 Golden nuggets, I shall give you the keys to the tower and rescue your princess. \n If however,you dont have enough golden nuggets, I shall turn you into a frog, as you will stay for the remainder of your days.\n")
        def end_game():
            global golden_nuggets
            
            if golden_nuggets>=300:
                storyline(f"\033[1;33mYour accumlated golden nuggets so far is: {golden_nuggets} Golden Nuggets\n")
                print("""===============================================================================""")
                storyline("\033[1;33mHaving enough Golden nuggets, you paid the Elf and took the keys to the tower.\nUpon reaching the top of the tower you open the door and went inside. There you see the princess.\nYou tell her that you came all this way to save her and now must take her to her father.\n")
                storyline("After you return to the Kingdom, the king was so happy and he gave you his daugther hand in marraige. And you guys lived happliy ever after...!!\n")
                print("""


        _______  _______  _______  _______    _______           _______  _______ 
        (  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )
        | (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|
        | |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|
        | | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)
        | | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (   
        | (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__
        (_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/
                                                                                """)
            else:
                storyline(f"\033[1;31mYour accumlated golden nuggets so far is{golden_nuggets} Golden Nuggets\n")
                print("""===============================================================================""")
                storyline("\033[1;31m Well my dear Knight, it seems you dont have enough golden nuggets to save the princess. Thus you shall be a frog till end of time. until,a girl with the purest of heart give you a kiss.....!!!!!")

                print("""===============================================================================""")
                print("A Kinght's Conquest 2 coming fall 2023 ")

                print("""===============================================================================""")
                print("""


        _______  _______  _______  _______    _______           _______  _______ 
        (  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )
        | (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|
        | |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|
        | | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)
        | | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (   
        | (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__
        (_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/
                                                                                """)

                                                                            
        end_game()
        
    game()

the_knights_conquest()
