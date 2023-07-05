import random
import os

def main():
    print("Welcome to Tic Tac Toe Game \n")

    while True:
        table = [" "]*10
        player_1 = input("What is the name of the player 1? : ")
        player_2 = input("What is the name of the player 2? : ")
        print()

        mark_player1 = chose_mark_player1()
        mark_player2 = chose_mark_player2(mark_player1)
        
        player = chose_first(player_1,player_2)

        while True:
            if player == player_1:
                print(f"{player_1}, your mark is {mark_player1}")
                pos_p1 = input_position(player_1,table)
                print('\n' * 100)
                mark_in_table(table,mark_player1,pos_p1)
                print_table(table)
                player = player_2

                if table_win(table,mark_player1) == True:
                    print(f"Congrats, {player_1} wins")
                    break
                else:
                    if full_board_check(table):
                        print('The game is a draw!')
                        break
                    
            else:
                print(f"{player_2}, your mark is {mark_player2}")
                pos_p2 = input_position(player_2,table)
                print('\n' * 100)
                mark_in_table(table,mark_player2,pos_p2)
                print_table(table)
                player = player_1

                if table_win(table,mark_player2) == True:
                    print(f"Congrats, {player_2} wins")
                    break
                else:
                    if full_board_check(table):
                        print('The game is a draw!')
                        break
        if not replay():
            print("Thank you for playing")
            break



def print_table(table):
    print(table[7] + "|" + table[8] + "|" + table[9])
    print("-" + "|" + "-" + "|" + "-")
    print(table[4] + "|" + table[5] + "|" + table[6])
    print("-" + "|" + "-" + "|" + "-")
    print(table[1] + "|" + table[2] + "|" + table[3])

def chose_mark_player1():
    aleatory_mark = random.randint(0,1)
    if aleatory_mark == 0:
        return "O"
    else: return "X"

def chose_mark_player2(mark_player1):
    if mark_player1 == "X":
        return "O"
    else: return "X"

def chose_first(player1,player2):
    aleatory_first = random.randint(0,1)
    if aleatory_first == 0:
        return player1
    else:
        return player2
    
def input_position(player,table):
    while True:
        try:
            position = int(input(f"{player} tell me a position (1-9) : "))
        except:
            print("Sorry that was not a number")
            continue
        else:
            if(position not in range(1,10)):
                print("Is not in the range")
            elif table[position] != " ":
                print("This position is already in use")
            else:
                return position
                break

def mark_in_table(table,mark,pos):
    table[pos] = mark

def space_check(table, position):
    return table[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def table_win(table,mark):
    return table[1] == mark and table[2] == mark and table[3] == mark or \
    table[4] == mark and table[5] == mark and table[6] == mark or \
    table[7] == mark and table[8] == mark and table[9] == mark or \
    table[1] == mark and table[4] == mark and table[7] == mark or \
    table[2] == mark and table[5] == mark and table[8] == mark or \
    table[3] == mark and table[6] == mark and table[9] == mark or \
    table[1] == mark and table[5] == mark and table[9] == mark or \
    table[3] == mark and table[5] == mark and table[7] == mark 

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


if __name__ == "__main__":
    main()