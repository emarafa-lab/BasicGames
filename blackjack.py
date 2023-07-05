import random

def main():
    while True:
        # The type of suit
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    
        # The type of card
        cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # The values of each card
        cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
        

        deck = generateDeck(suits,cards)

        dealerScore = 0
        playerScore = 0
        
        print("-------------------------Dealers Hand-------------------------")
        dealerScore = turn(deck, cards_values, dealerScore)
        dealerScore = turn(deck, cards_values, dealerScore)
        print("Dealers score:", dealerScore)
        
        print("-------------------------Players Hand-------------------------")
        playerScore = turn(deck, cards_values, playerScore)
        playerScore = turn(deck, cards_values, playerScore)
        print("Your score:", playerScore)
        
        print("-------------------------Begin Game-------------------------")

        while True: 
            userChoice = user_input()
            if (userChoice == "HIT"):
                playerScore = turn(deck, cards_values, playerScore)
                print("Your total:", playerScore)
                print("Dealer total:", dealerScore)
                if playerScore > 21:
                    print("-------------------------You bust, dealer wins!-------------------------")
                    break
                elif dealerScore == playerScore:
                    print("-------------------------Tie!-------------------------")
                    break
                elif dealerScore > playerScore:
                    print("-------------------------You lose, dealer wins!-------------------------")
                    break
                else:
                    print("-------------------------Dealer loses, you win!-------------------------")
                    break
            elif (userChoice == "STAND"):
                print("-------------------------Dealers Hand-------------------------")
                while True:
                    dealerScore = turn(deck, cards_values, dealerScore)
                    if dealerScore < 17 or dealerScore < playerScore:
                        continue
                    else: break
                print("Your total:", playerScore)
                print("Dealer total:", dealerScore)
                if dealerScore > 21:
                    print("-------------------------Dealer busts, you win!-------------------------")
                    break
                elif dealerScore == playerScore:
                    print("-------------------------Tie!-------------------------")
                elif dealerScore > playerScore:
                    print("-------------------------You lose, dealer wins!-------------------------")
                    break
                else:
                    print("-------------------------Dealer loses, you win!-------------------------")
                    break

        if not replay():
            print("Thanks for playing")
            break

def user_input():
    while True:
        try:
            option = str(input("HIT or STAND: "))
        except:
            print("Sorry that was not a text")
            continue
        else:
            if(option == "HIT" or option == "STAND"):
                return option
                break
            else:
                print("I did not understand")
                continue

def generateDeck(suits,cards):
    deck = []
    for suit in suits:
        for card in cards:
            deck.append((card, suit))
    random.shuffle(deck)
    return deck

def getCardValue(card,values):
    key = card[0]
    value = values[key]
    return value

def turn(deck, cards_values, current_score):
    card = deck.pop(0)
    print(">> ", card)
    cardValue = getCardValue(card,cards_values)        
    new_score = current_score + cardValue
    print("Score: ", new_score)
    return new_score

def replay():
    return input("Do you want to play again? (Yes or No): ").lower().startswith("y")
if __name__ == "__main__":
    main()


