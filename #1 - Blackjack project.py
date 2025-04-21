import random

print("Hello! Welcome to Blackjack!")  # Greeting

# The card deck (Aces = 11, Face cards = 10)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Deal initial cards
user_cards = [random.choice(cards), random.choice(cards)]
computer_cards = [random.choice(cards), random.choice(cards)]

# Reveal initial hands
print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
print(f"Dealer's first card: {computer_cards[0]}")

game_over = False #Creating a condition to use for the while loop.

while not game_over:
    # Check if user busts or gets blackjack
    if sum(user_cards) == 21: #Equal to 21 condition.
        print("You have Blackjack!")
        game_over = True
    elif sum(user_cards) > 21: #Burst condition
        print("You busted!")
        game_over = True
    else:
        # Ask the user: Hit or Stand?
        user_choice = input("Type 'hit' to draw another card or 'stand' to hold: \n").lower()

        if user_choice == 'hit':
            user_cards.append(random.choice(cards)) #using 'append' to add to an existing list.
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        else:
            game_over = True

# Once the player stands or busts, dealer plays (if user didn't already lose)
if sum(user_cards) <= 21:
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards)) #The Dealer will have to take another card as per the rules if his final score is less than 17.

    print(f"\nYour final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Dealer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

    if sum(computer_cards) > 21: #Dealer Burst condition.
        print("Dealer busted! You win ")
    elif sum(user_cards) > sum(computer_cards):
        print("You win")
    elif sum(user_cards) < sum(computer_cards): #if dealer's score is more than user's
        print("You lose")
    else: # Draw condition
        print("It's a draw")