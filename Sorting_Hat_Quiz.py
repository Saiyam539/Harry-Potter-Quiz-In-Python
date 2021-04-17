import datetime

def greeting():
    name = input("Enter your name here:- ")

    hour = int(datetime.datetime.now().hour)

    if hour>0 and hour<=12:
        print(f'Good Morning {name}')
    elif hour>12 and hour<=17:
        print(f"Good Afternoon {name}")
    else:
        print(f"Good Evening {name}")


def main_quiz():


    Ravenclaw = 0
    Gryffindor = 0
    Hufflepuff = 0
    Slytherin = 0


    Question1 = ''' \nQ1-During the end-of-year exams, you notice that one of your classmates was using an enchanted quill. You come top of the class anyway, but they are second. What do you do?
    1. Tell the professor immediately – cheating is wrong, no matter what.
    2. Nothing, but if I hadn't come top of the class, I'd definitely tell the professor.
    3. Encourage the other student to admit what they'd done to the professor.
    4. Give them a high five for managing to sneak the quill into the exam.'''
    print(Question1)

    user_answer = int(input('\nEnter the option number of the option which you choose:- '))

    if user_answer==1:
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer==2:
        Gryffindor = Gryffindor + 1

    elif user_answer==3:
        Hufflepuff = Hufflepuff + 1

    elif user_answer==4:
        Slytherin = Slytherin + 1
    
    else:
        print('Please choose a valid option')
    
    Question2 = '''\n Q2- You would be most hurt if a person called you...
    1.Weak
    2.Ignorant
    3.Unkind
    4.Boring'''
    print(Question2)
    user_answer2 = int(input('\nEnter the option number of the option which you choose:- ')) 

    if user_answer2==1:
        Gryffindor = Gryffindor + 1
    
    elif user_answer2==2:
        Ravenclaw = Ravenclaw +1 
    
    elif user_answer2==3:
        Hufflepuff = Hufflepuff +1
    
    elif user_answer2==4:
        Slytherin = Slytherin +1
    
    else:
        print("Please choose a valid option.....")
    
    Question3 = '''\nQ3- You're locked in a duel with a skilled opponent. They fire an unknown spell at you, and you shout…
    1.Expelliarmus!
    2.Protego!
    3.Stupefy!
    4.Crucio!'''

    print(Question3)
    user_answer3 = int(input("\nEnter the optin number of tje option which you choose:- "))

    if user_answer3==1:
        Gryffindor = Gryffindor +1
    
    elif user_answer3==2:
        Ravenclaw = Ravenclaw +1
    
    elif user_answer3==3:
        Slytherin = Slytherin + 1
    
    elif user_answer3==4:
        Hufflepuff = Hufflepuff + 1
    
    else:
        print("Please choose a valid option...")
    
    Question4 = '''\nQ4- It's your fifth year at Hogwarts, and you've just received a Howler from your parents. What for?
    1.Sneaking into the Forbidden Forest at night on a dare.
    2.Getting caught cheating in my Divination O.W.L.
    3.Being put in detention after I was caught in the library after hours.
    4.Nothing! I'd never do anything to warrant a Howler.'''

    print(Question4)
    user_answer4 = int(input('Enter the option number of the option which you choose:- '))

    if user_answer4==1:
        Gryffindor = Gryffindor + 1
    
    elif user_answer4==2:
        Slytherin = Slytherin + 1
    
    elif user_answer4==3:
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer4==4:
        Hufflepuff = Hufflepuff + 1
    
    else:
        print("Please choose a valid option")
    
    Question5 ='''\nQ5- Which of these Dumbledore quotations speaks to you?
    1."Pity the living, and above all, those who live without love."
    2."Words are, in my not-so-humble opinion, our most inexhaustible source of magic."
    3."It matters not what someone is born, but what they grow to be."
    4."It does not do to dwell on dreams and forget to live."'''

    print(Question5)
    user_answer5 = int(input('\nEnter the option number of the option which you choose:- '))

    if user_answer5==1:
        Hufflepuff = Hufflepuff + 1
    
    elif user_answer5==2:
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer5==3:
        Gryffindor = Gryffindor + 1
    
    elif user_answer5==4:
        Slytherin = Slytherin + 1

    else:
        print("Please choose a valid option")
    
    Question6 = '''\nQ6- You're allowed a pet at Hogwarts: an owl, a cat, or a toad. Which do you bring?
    1.Owl
    2.Cat
    3.Toad
    4.Nothing. I can't be trusted to look after a pet!'''

    print(Question6)
    user_answer6 = int(input('Enter the option number of the option which you choose:- '))

    if user_answer6==1 or user_answer6==2 or user_answer6==3 or user_answer6==4:
        Hufflepuff = Hufflepuff + 1
        Ravenclaw = Ravenclaw + 1
        Gryffindor = Gryffindor + 1
        Slytherin = Slytherin + 1
    
    else:
        print('Please choose a valid option....')
    
    Question7 = '''\nQ7- It's Saturday, you've finished your homework, and you have some free time. You decide to spend some time away from your common room. Where do you go?
    1.The Forbidden Forest
    2.The library
    3.The kitchens
    4.The Room of Requirement'''

    print(Question7)

    user_answer7 = int(input('Enter the option number of the option which you choose:- '))

    if user_answer7==1:
        Slytherin = Slytherin + 1

    elif user_answer7==2:
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer7==3:
        Hufflepuff = Hufflepuff + 1
    
    elif user_answer7==4:
        Gryffindor = Gryffindor + 1
    
    else:
        print('Please choose a valid option....')
    
    Question8 = '''\nQ8- What would you see in the Mirror of Erised?
    1.Myself, surrounded by riches.
    2.Myself, surrounded by my loving family and friends.
    3.Myself, knowledgable above all.
    4.Myself, experiencing a marvellous adventure.'''

    print(Question8)
    user_answer8 = int(input('Enter the option number of the option which you choose:- '))

    if user_answer8==1:
        Slytherin = Slytherin + 1
    
    elif user_answer8==2:
        Hufflepuff = Hufflepuff + 1
    
    elif user_answer8==3:
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer8==4:
        Gryffindor = Gryffindor + 1
    
    Question9 = '''\nQ9- Choose a Deathly Hallow.
    1.The Elder Wand
    2.The Resurrection Stone
    3.The Cloak of Invisibility'''

    print(Question9)
    user_answer9 = int(input('Enter the option number of the option which you choose:- '))

    if user_answer9==1:
        Slytherin = Slytherin + 1
    
    elif user_answer9==2:
        Gryffindor = Gryffindor + 1
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer9==3:
        Gryffindor = Gryffindor + 1
        Ravenclaw = Ravenclaw + 1
        Hufflepuff = Hufflepuff + 1
    
    else:
        print('Please choose a valid option....')
    
    Question10 = '''And finally: We know that the Sorting Hat takes into account your preferences. So which Hogwarts house do you feel you identify with most closely?
    1.Gryffindor
    2.Hufflepuff
    3.Ravenclaw
    4.Slytherin'''

    print(Question10)
    user_answer10 = int(input("Enter the option number of the option which you choose:- "))

    if user_answer10==1:
        Gryffindor = Gryffindor + 1
    
    elif user_answer10==2:
        Hufflepuff = Hufflepuff + 1
    
    elif user_answer10==3:
        Ravenclaw = Ravenclaw + 1
    
    elif user_answer10==4:
        Slytherin = Slytherin + 1
    
    else:
        print("Please choose a valid option....")

    
    print(f"Ravenclaw - {(Ravenclaw/10)*100}%")
    print(f'Gryffindor - {(Gryffindor/10)*100}%')
    print(f'Hufflepuff - {(Hufflepuff/10)*100}%')
    print(f'Slytherin - {(Slytherin/10)*100}%')


greeting()
main_quiz()

