def main():
    player = input("Enter your name: ")
    points = 1000
    PERCENT = .10
    
    while not player.isalpha():
        player = input("Enter your name: ")

    print()
    print(f"Hello, {player}. This is an art trivia game.")
    print("You will be asked five multiple choice questions.")
    print("Before each round, you must wager at least 10% of your current point total.")
    print(f"Your starting point total is {points} points.")
    print("The game will end when you lose all of your points, or when you answer all of the questions.")
    print()

    infile = open("sjones-part1.txt","r")


    for line in infile:
            answerIndex = -1
            line = line.split(";")
            
            if points > 0:
                wager = input(f"{player}, how many points would you like to wager for this round? ")
                while not wager.isdigit():
                    print()
                    print("Please inter an integer.")
                    wager = input(f"{player}, how many points would you like to wager for this round? ")
                    print()
                wager = int(wager)
                while wager < (PERCENT * points) or wager > points:
                    print()
                    print(f"Please enter a number between {int(PERCENT * points)} and {points}.")
                    wager = input(f"{player}, how many points would you like to wager for this round? ")
                    print()
                    while not wager.isdigit():
                        print()
                        print("Please inter an integer.")
                        wager = input(f"{player}, how many points would you like to wager for this round? ")
                        print()
                    wager = int(wager)

                for i in range(len(line)):
                    if line[i].endswith("!"):
                        answer = line[i]
                        answer = answer.rstrip("!")
                        line[i] = line[i].rstrip("!")
                        answerIndex = i
                                
                    if i == 0:
                        print(f"{line[i]}")
                    else:
                        print(f"  {i}. {line[i]}")
             
                guess = int(input("Enter the number of your answer: "))
                print()
                while guess < 1 or guess > 4:
                    print("Invalid guess! Please enter a number between 1 and 4.")
                    guess = int(input("Enter the number of your answer: "))
                    print()
                                
                if int(guess) == int(answerIndex):
                    print(f"That is correct, {player}!")
                    points += wager
                    print(f"Your new point total is {points} points.")
                    print()          
                else:
                    print(f"That is incorrect, {player}!")
                    print(f"The correct answer is {answerIndex}, {answer}!")
                    points -= wager
                    print(f"Your new point total is {points} points.")
                    print()
            
    if points > 0:
        print(f"Well done, {player}!")
        print(f"You finished the game with {points} points!")
    else:
        print(f"Sorry, {player}. You have no more points!")
        print("GAME OVER!")
        
    infile.close()  

main()
