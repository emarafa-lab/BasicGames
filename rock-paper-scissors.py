import random

def main():
    while True:
        options = [" ","Rock","Paper","Sesors"]
        print()
        print("This is the game ROCK, PAPER SESORS")
        player = input("Please, introduce your name : ")

        score_player = 0
        score_computer = 0

        while True:
            if score_player < 3 and score_computer < 3:
                menu()
                option = check_option()
                print('\n' * 100)
                player_option = player_selection(options,option)
                computer_option = computer_selection(options)
                print_selection_player_computer(player_option,computer_option)

                if comparation(player_option,computer_option) == "Player":
                    score_player += 1
                    print_scores(score_player,score_computer)
                elif comparation(player_option,computer_option) == "Draw":
                    print_scores(score_player,score_computer)
                else: 
                    score_computer += 1
                    print_scores(score_player,score_computer)

                if score_player == 3:
                    print(f"Congratulations {player}, you win")
                    break
                elif score_computer == 3:
                    print("You loss")
                    break

        if not replay():
            print("Thank you for playing")
            break

def menu():
    print("1) Rock")
    print("2) Paper")
    print("3) Sesors")
    
def check_option():
    while True:
        try:
            option = int(input("Select an option : "))

        except:
            print("Sorry that was not a number")
            continue
        else:
            if(option not in range(1,4)):
                print("Is not in the range")
            else:
                return option
                break

def print_selection_player_computer(player_option, computer_option):
    print(f"Your selection is :         {player_option}")
    print(f"Computer's selection is :   {computer_option}")

def comparation(player_option,computer_option):
    if player_option == "Rock" and computer_option == "Sesors" or player_option == "Paper" \
          and computer_option == "Rock" or player_option == "Sesors" and computer_option == "Paper":
        return "Player"
    elif player_option == "Rock" and computer_option == "Rock" or player_option == "Paper" \
        and computer_option == "Paper" or player_option == "Sesors" and computer_option == "Sesors":
        return "Draw"
    else: return "Computer"

def print_scores(score_player,score_computer):
    print(f"Your score is :             {score_player}")
    print(f"The score of computer is :  {score_computer}\n")

def player_selection(options,option):
    return options[option]

def computer_selection(options):
    return options[random.randint(1,3)]

def replay():
    return input("Do you want to play again? (Yes or No): ").lower().startswith("y")

if __name__ == "__main__":
    main()
