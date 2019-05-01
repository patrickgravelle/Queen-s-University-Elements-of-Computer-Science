# Patrick Gravelle, 13plg, 10141195
# This program allows for the user to play a game of PIG against a computer player
# The user is given prompts on what to do in order to play the game
import random

def main() :
    print('Welcome to a game of pig!')
    PlayerScore = 0
    CompScore = 0
    Turn = 0 
    while PlayerScore < 100 and CompScore < 100 :
        print(f'Player total is {PlayerScore} and Computer total is {CompScore}.')
        Turn = Turn + 1
        print(f'Begin Turn {Turn}.')
        PlayerTurn = 0
# Using a boolean character as true allows for the 'turns' to be played such that once the character becomes false
# the dice are then 'passed' to the next player and the game continues
        Flag = True
        decision = input('To roll the dice, press the enter key: ')
        while Flag :
            PDie1 = random.randint(1,6)
            PDie2 = random.randint(1,6)
            PDice = PDie1 + PDie2
            if PDie1 == 1 and PDie2 == 1 :
                PlayerScore = 0
                Flag = False
                print(f'Your roll was {PDie1,PDie2}.Thus your total score was reset.')
            elif PDie1 == 1 and PDie2 != 1 :
                print(f'Your roll was {PDie1,PDie2}. Thus your turn has ended with no point accumulation. Your total remains {PlayerScore}.')
                PlayerTurn = 0
                Flag = False
            elif PDie1 != 1 and PDie2 == 1 :
                print(f'Your roll was {PDie1,PDie2}. Thus your turn has ended with no point accumulation. Your total remains {PlayerScore}.')
                PlayerTurn = 0
                Flag = False
            elif PDie1 == PDie2 != 1 :
                print(f'Your roll was {PDie1,PDie2}. The dice will be rerolled.')
                Flag = True
            elif PDie1 != 1 and PDie2 != 1 :
                print(f'Your roll was {PDie1,PDie2} for a total of {PDice}.')
                PlayerTurn = PlayerTurn + PDice
                move = input(f'Would you like to roll again or hold with a total of {PlayerScore + PlayerTurn}?' \
                             ' To roll again press the enter key, to hold, type "hold". ')
                if (PlayerScore + PlayerTurn) >= 100 :
                    print('Congratulations, you have won the game!')
                    return
                if move != "" :
                    PlayerScore = PlayerScore + PlayerTurn
                    Flag = False
                elif move == "" :
                    Flag = True
# The computer's strategy is such that it will roll 4 legal rolls until it holds.
# This allows for large point gains or no points at all.
        CompTurn = 0
        Flag2 = True
        count = 0
        while Flag2 and count < 4 :
            CDie1 = random.randint(1,6)
            CDie2 = random.randint(1,6)
            CDice = CDie1 + CDie2
            if CDie1 == 1 and CDie2 == 1 :
                CompScore = 0
                Flag2 = False
                print(f'Computer roll was {CDie1,CDie2}.Thus computer total score was reset.')
            elif CDie1 == 1 and CDie2 != 1 :
                print(f'Computer roll was {CDie1,CDie2}. Thus computer turn has ended with no point accumulation. Total remains {CompScore}.')
                CompTurn = 0
                Flag2 = False
            elif CDie1 != 1 and CDie2 == 1 :
                print(f'Computer roll was {CDie1,CDie2}. Thus computer turn has ended with no point accumulation. Total remains {CompScore}.')
                CompTurn = 0
                Flag2 = False
            elif CDie1 == CDie2 != 1 :
                print(f'Computer roll was {CDie1,CDie2}. The dice will be rerolled.')
                Flag2 = True
            elif CDie1 != 1 and CDie2 != 1 :
                count = count + 1
                CompTurn = CompTurn + CDice
                print(f'Computer roll was {CDie1,CDie2} for a total of {CDice}. Computer can hold with {CompScore + CompTurn} points.')
                Flag2 = True
                if (CompScore + CompTurn) >= 100 :
                    print('Sorry, you have lost the game')
                    return
                if count == 4 :
                    CompScore = CompScore + CompTurn
# When either player reaches 100 points, the game will notify the user of the winner.
# The code overall is relatively self-explanatory, and the valuable information is displayed to the user to allow
# for in game decision making.

        print('\n')            

main()
