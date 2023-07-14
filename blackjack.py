import random

#Function to find the sum of cards
def sum_cards(card1, card2, sum):
    
    #If the card is a Jack, Queen, or King, add 10 to the sum
    if card1 == 'Jack' or card1 == 'Queen' or card1 == 'King':
        sum = sum + 10
    #If the card is an Ace, return 1 or 11 based on the current sum of cards
    elif card1 == 'Ace':
        if sum > 10:
            sum = sum + 1
        else:
            sum = sum + 11
    #If the cards do not equal Ace, Jack, Queen or King, simply add the numerical values of the card to sum
    else:
        sum = sum + card1
    
    #Do the same for the second card
    if card2 == 'Jack' or card2 == 'Queen' or card2 == 'King':
        sum = sum + 10
    elif card2 == 'Ace':
        if sum > 10:
            sum = sum + 1
        else:
            sum = sum + 11
    else:
        sum = sum + card2
    
    return sum

#Main function  
def main():

    #print the welcome message and ask how much starting money the player would like to start with
    print()
    print("Welcome to Blackjack!")
    print()
    starting_money = int(input("How much money would you like to start with?: "))
    #Set both computers and users starting money equal to starting_money
    computer_money = starting_money
    user_money = starting_money
    #Declare the variable for sum after the first round if HIT is chosen
    hit_sum = 0

    #Array for the cards
    cards = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    print("*** GAME START ***")
    print()
    
    #While loop to check if the computers/users money is greater than 0
    while(user_money > 0 or computer_money > 0):
        
        #If the computer/users money is 0, break out of the loop and print correct "winner" message
        if computer_money == 0:
            print("*** Congrats, you won! ***")
            break

        if user_money == 0:
            print("*** Sorry, the computer won! ***")
            break
        
        #Ask the user how much they would like to bet
        user_bet = int(input("How much money would you like to bet?:"))
        print()

        #Set prize money based on user_bet, and subtract the user_bet from computer/users total money
        prize_money = user_bet * 2
        computer_money -= user_bet
        user_money -= user_bet

        #Choose two random cards from the array
        computer_card1 = random.choice(cards)
        computer_card2 = random.choice(cards)
        user_card1 = random.choice(cards)
        user_card2 = random.choice(cards)

        #Show the user the computers face up card, show user their two starting card
        print("The computers face up card is ", computer_card1)
        print()
        print("Your cards are ", user_card1, " and ", user_card2)
        print()
                
        #Call sum_card method and set initial sum at the start of each round
        computer_sum = 0
        user_sum = 0
        computer_sum = sum_cards(computer_card1, computer_card2, computer_sum)
        user_sum = sum_cards(user_card1, user_card2, user_sum)

        #Show the user their current sum
        print("Your current sum is", user_sum)
        print()

        #If the inital two cards equal 21...
        if (user_sum == 21):
            #Add prize money to users total money and print winning message
            user_money += prize_money 
            #Show user total money
            print("*** You won the round! *** Your total money is now ", user_money)
            print()
            #Show computers total money after losing round
            print("The computers total money is ", computer_money)
            print()
            continue

        #While loop to make sure user and computers sum is less than 22
        while (user_sum < 22 and computer_sum < 22):
            #Ask the user if they want to HIT or PASS
            hit_pass = str(input("Pass HIT to get another card from the dealer, type PASS to end the round: "))
            print()
            
            #If the user chooses hit, obtain a new card and call sum_cards function
            if (hit_pass == 'HIT'):
                user_card1 = random.choice(cards)
                #Declare an extra variable to keep the sum up to date for the current round
                hit_sum = sum_cards(user_card1, 0, user_sum)
                user_sum = hit_sum

                #Show the user the card that was drawn, and show the current sum of cards
                print("You drew a ", user_card1, " making your current sum ", hit_sum)
                print()

                #If the user card total equals 21...
                if (hit_sum == 21):
                    #Add prize money to users total money and print winning message
                    user_money += prize_money 
                    #Show user total money
                    print("*** You won the round! *** Your total money is now ", user_money)
                    print()
                    #Show computers total money after losing round
                    print("The computers total money is ", computer_money)
                    print()
                    hit_sum = 0
                    break

                #If the user sum is less than 21 after drawing an addition card, start back the beginning of loop
                elif (hit_sum < 21):
                    hit_sum = 0
                    continue
                
                #If the user card total is over 21... 
                else:
                    #Show the user they lost the round and their new money total
                    print("*** You lost the round! *** Your total money is now ", user_money)
                    print()
                    #Give computer the prize money and show the computers total money
                    computer_money += prize_money
                    print("The computers total money is ", computer_money)
                    print()
                    hit_sum = 0
                    break

            #If the user enters PASS...
            if (hit_pass == 'PASS'):
                print("The dealers sum of cards is ", computer_sum)
                print()

                #If the users_sum is greater than the computers_sum...
                if (user_sum > computer_sum):
                    #Give the user the prize money and print out computers/users total money
                    user_money += prize_money
                    print("*** You won the round! *** Your total money is now ", user_money)
                    print()
                    print("The computers total money is ", computer_money)
                    print()
                    hit_sum = 0
                    break
                #If the sums are equal...
                elif (user_sum == computer_sum):
                    #Give back the money evenly to both the user and the computer and show total money
                    user_money += user_bet
                    computer_money += user_bet
                    #Display message showing the round was a tie and the computer/users money
                    print("*** The round was a tie! ***")
                    print()
                    print("Your total money is ", user_money)
                    print()
                    print("The computers total money is ", computer_money)
                    print()
                    #Reset hit_sum total to 0
                    hit_sum = 0
                    break
                #If computer sum is greater than the user sum...
                else:
                    #Show the user they lost the round and their total money
                    print("*** You lost the round! *** Your total money is now ", user_money)
                    print()
                    #Give the computer the prize money and show the computers total
                    computer_money += prize_money
                    print("The computers total money is ", computer_money)
                    print()
                    #Reset hit_sum to 0
                    hit_sum = 0
                    break
    
main();