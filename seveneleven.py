#!bin/python3
from random import seed
from random import randint


def cont():
    print("Press enter to continue")
    go = input()

yourname=input("Please enter your name here: ")

playing = True
playermoney = 20000
winners = ['Lauren', 'BillyBob', 'Larry', 'Susie', 'Jane', 'John', 'Maxine', 'Susan', "Jack"]
playerbet = 0
computerbet = 1
loaned = 0
winner = 0
noleave = False

while playing or noleave:
    playermoney -= loaned
    loaned = -playermoney
    noleave = False
    if loaned > 0:
        noleave = True
        print('Money you owe us: $' + str(loaned))
    print("Welcome to the 7/11 Casino!! \nWhere YOUR money is OUR money!")
    print("RECENT WINNERS")
    if playermoney-20000<=200000:
        print(winners[randint(0, 8)] + " won $" + str(randint(200000, 100000000)))
    if playermoney-20000>200000:
        print(yourname+' won $'+str(playermoney-20000))
    print(winners[randint(0, 8)] + " won $" + str(randint(200000, 100000000)))
    print(winners[randint(0, 8)] + " won $" + str(randint(200000, 100000000)))
    choice = input("\nWould you like to play?     balance: $" + str(playermoney) + "     Earnings: $" + str(
        playermoney - 20000) + "\ny/n \n")
    if choice == 'y':
        playerbet = 0
        computerbet = 1
        while playerbet != computerbet:
            print("\nWhat is your bet?\nYou have $" + str(playermoney) + " left.")
            print('Current bet: $' + str(playerbet))
            print('Computer bet: $' + str(computerbet))
            playerbet = int(input("Bet here (Digits only):  "))
            random = randint(1, 100)
            if playerbet < 100 and playerbet <= playermoney:
                computerbet = playerbet * 10
            if playerbet >= 100 and playerbet < 1000 and playerbet <= playermoney:
                if random < 70:
                    computerbet = playerbet * randint(2, 5)
                else:
                    computerbet = playerbet * randint(1, 2)
            if playerbet >= 1000 and playerbet < 10000 and playerbet <= playermoney:
                if random < 25:
                    computerbet = playerbet * randint(1, 3)
                else:
                    computerbet = playerbet
            if playerbet >= 10000 and playerbet <= playermoney:
                computerbet = playerbet
            if playerbet > playermoney:
                print("You do not have enough money to place that bet. Would you like to take out a loan? y/n")
                loanchoice = input()
                if loanchoice == 'y':
                    loaned = playerbet - playermoney
                    computerbet = playerbet
                if loanchoice == 'n':
                    computerbet = 1
                    playerbet = 0
            print("Your bet: $" + str(playerbet) + "  Computer's bet: $" + str(
                computerbet) + "\n(If the computer bet higher you must equal or exceed its bid.)")
        print("Your bet: $" + str(playerbet) + "\nComputer bet: $" + str(computerbet))
        upante = int(input("Would you like to:\n1. Play\n2. Bet higher\nChoice: "))
        while upante == 2:
            print("\nWhat is your bet?\nYou have $" + str(playermoney) + " left.")
            print('Current bet: $' + str(playerbet))
            print('Computer bet: $' + str(computerbet))
            playerbet = int(input("Bet here(Digits only):  "))
            random = randint(1, 100)
            if playerbet < 100 and playerbet <= playermoney:
                computerbet = playerbet * 10
            if playerbet > 100 and playerbet < 1000 and playerbet <= playermoney:
                if random < 70:
                    computerbet = playerbet * randint(2, 5)
                else:
                    computerbet = playerbet * randint(1, 2)
            if playerbet > 1000 and playerbet < 10000 and playerbet <= playermoney:
                if random < 25:
                    computerbet = playerbet * randint(1, 3)
                else:
                    computerbet = playerbet
            if playerbet > 10000 and playerbet <= playermoney:
                computerbet = playerbet
            if playerbet > playermoney:
                print("You do not have enough money to place that bet. Would you like to take out a loan? y/n")
                loanchoice = input()
                if loanchoice == 'y':
                    loaned = playerbet - playermoney
                    computerbet = playerbet
                if loanchoice == 'n':
                    computerbet = 1
                    playerbet = 0
            print("Your bet: $" + str(playerbet) + "  Computer's bet: $" + str(
                computerbet) + "\n(If the computer out bet you you must equal or exceed its bid.)")
            print("Your bet: $" + str(playerbet) + "\nComputer bet: $" + str(computerbet))
            if loaned > 0:
                noleave = True
                print('Money you owe us: $' + str(loaned))
            upante = int(input("Would you like to:\n1. Play\n2.Bet higher\nChoice: "))
        if upante == 1:
            print("""You are now playing 7/11! 
            -The aim of the game is to have the dice add up to seven or eleven on your turn. 
            -If the dice roll in your favor, you take the pot! 
            -If they strike lucky when it isn't your turn, you lose it all!
        
        Press enter to start""")
            go = input()
            winner = 0
            while winner == 0:
                print("Enter to continue\n")
                go = input()
                print('Pot: $' + str(playerbet + computerbet) + '\nYour roll:')
                dice1 = randint(1, 6)
                dice2 = randint(1, 6)
                print(str(dice1) + ' + ' + str(dice2) + ' => ' + str(dice1 + dice2))
                if dice1 + dice2 == 7 or dice1 + dice2 == 11:
                    winner = 1
                else:
                    print("Enter to continue\n")
                    go = input()
                    print('Pot: $' + str(playerbet + computerbet) + '\nComputer\'s roll:')
                    dice1 = randint(1, 6)
                    dice2 = randint(1, 6)
                    print(str(dice1) + ' + ' + str(dice2) + ' => ' + str(dice1 + dice2))
                    if dice1 + dice2 == 7 or dice1 + dice2 == 11:
                        winner = 2
                    else:
                        winner = 0
            if winner == 1:
                print('You won!')
                playermoney += computerbet + playerbet
                print('Your balance is now ' + str(playermoney - loaned))
                cont()
            if winner == 2:
                print("You lost!")
                playermoney -= computerbet + playerbet
                print('Your balance is now ' + str(playermoney - loaned))
                cont()

    if choice == 'n':
        if noleave:
            print("You are not permitted to leave until all debts are fulfilled!!!")
            print('Press Enter to continue.')
            go = input()
        if not noleave:
            print("Are you sure you want to leave?")
            yesleave = input("y/n\n")
            if yesleave == 'y':
                print("Confirm departure?")
                yesyesleave = input("y/n\n")
                if yesyesleave == "y":
                    print("Is leaving your final decision?")
                    yesyesyesleave = input("y/n\n")
                    if yesyesyesleave == 'y':
                        print("You don\'t not want to leave?")
                        YESleave=input("y/n\n")
                        if YESleave=="y":
                            print("Last chance:")
                            YESYESleave = int(input("1. poop at parties\n2. stay for more fun!\n"))
                            if YESYESleave == 1:
                                print("\n\n\n\nOk bye then.\n")
                                playing = False