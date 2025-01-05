import math

def printQuestion(question, round, rounds):
    print(f"\nQuestion {round+1}:  {question[0]}")
    for i in range(1,5,1):
        print(f'{i}. {question[i]}')
    valid=False
    while not valid:
        print("\nWhat is your answer (1,2,3 or 4)",end=" ")
        answer=int(input())
        if answer>=1 and answer<=4:
            valid=True
            if str(question[answer])== (question[5]):
                return True
            else:
                return False
        else:
            print("Please submit a valid value beteeen 1 and 4")
            
def printAnswer(correct, name, question):
    if correct:
        print(f"That is the correct answer {name}!\n")
    else:
        print(f"That is an incorrect answer {name}.  The correct answer is {question[5]}\n")    

def cashOut(points, wager, correct):
    if correct:
        points += wager
        return points 
    else:
        points -= wager
        return points

def gameEnd(name, points):
    print(f"\n\n!!!!!GAME OVER {name.upper()}!!!!!")
    print(f"Your final score is {points}")
    
def main():
    #initialze variables
    round=0
    points=1000
    done=False
    #ask for name
    name=input("Please type your name: ")
    print()
    #ask the user how many rounds they would like to play
    rounds = int(input(f"{name}, how many rounds would you like to play? (Enter an integer between 1 and 5) "))
    while rounds < 1 or rounds > 5:
        print()
        print("Please enter a valid number of rounds.")
        rounds = int(input(f"{name}, how many rounds would you like to play? (Enter an integer between 1 and 5) "))
    #open file to read in questions and answers
    ifile=open('sjones-part1.txt','r')
        
    
    while not done and round<rounds:
        print(f"\nYou have {points} points.\n")
        print(f"{name}, enter an integer between {math.ceil(0.1*points)} and {(points)}: ", end=" ")
        wager=int(input())
        if wager>=math.ceil(0.1*points) and wager <=points:
            print()
            line=(ifile.readline()).strip()
            question=line.split(';')
            correct = printQuestion(question, round, rounds)
            printAnswer(correct, name, question)
            points = cashOut(points, wager, correct)
            if points==0:
                done=True
            round += 1
        else:
            print(f"You have {points} points.  Choose a value between {math.ceil(0.1*points)} and {points}")
            print()
    # The game is complete so print out the result
    gameEnd(name, points)
    #close file
    ifile.close()
main()

