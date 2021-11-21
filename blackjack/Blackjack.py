import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def A_check_and_replace(p_or_c_card):
    for i in range(0, len(p_or_c_card)-1):
        if p_or_c_card[i] == 11 and sum(p_or_c_card)>21:
            p_or_c_card[i] = 1

def draw():
    player_cards.append(random.choice(cards))
    A_check_and_replace(player_cards)

def check():
    if sum(computer_cards) > 21:
        print(f"Computer's card: {','.join(str(x) for x in computer_cards)} = {sum(computer_cards)}\n")
        print("You Win!")
        global result
        result = "win"
        return
    else:
        if sum(player_cards) > sum(computer_cards):
            print(f"Computer's card: {','.join(str(x) for x in computer_cards)} = {sum(computer_cards)}\n")
            print("You Win!")
            result = "win"
            return

        elif sum(player_cards) == sum(computer_cards):
            print(f"Computer's card: {','.join(str(x) for x in computer_cards)} = {sum(computer_cards)}\n")
            print("Draw!")
            result = "draw"
            return

        else:
            print(f"Computer's card: {','.join(str(x) for x in computer_cards)} = {sum(computer_cards)}\n")
            print("You Lose!")
            result = "lose"
            return

def main():
    print(f"\nYou have {','.join(str(x) for x in player_cards)} = {sum(player_cards)}\nComputer has {computer_cards[0]}\n")
    if sum(player_cards) > 21:
        print(f"Computer's card: {','.join(str(x) for x in computer_cards)}")
        print("You Lose!")
        global result
        result = "lose"
        return
    elif sum(player_cards) == 21:
        print("Blackjack!")
        check()
    elif sum(player_cards) < 21:
        i = True
        while i == True:
            draw_or_not = input("Do you want to draw a card? ").upper()
            if draw_or_not == "Y":
                draw()
                main()
                i =False
            elif draw_or_not == "N":
                check()
                i = False
            else:
                i = True

##########################################
money = 100
result = "none"
again = True
while again == True:
    player_cards, computer_cards = [], []
    for i in range(2):
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
        A_check_and_replace(computer_cards)
    print(f"You have: ${money}")

    global bet
    i = True
    while i==True:
        bet = int(input("Place your bet: "))
        if bet<=money:
            i = False
        else:
            print("Error! ")
            i = True

    main()
    if result == "win":
        money += bet
    elif result == "lose":
        money -= bet
    print(f"You have: ${money}")
    if money == 0:
        print("You broke! Come back when you have money! ")
        quit()

    i = True
    while i == True:
        ask = input("\nPlay again? ").upper()
        if ask == "Y":
            again = True
            i = False
        elif ask == "N":
            print("Bye! ")
            again = False
            i = False
        else:
            print("Error! ")
            i = True
