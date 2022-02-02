import random
from art_blackjack import logo
from replit import clear

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

player_cards = []
computer_cards = []

#1. make a function to draw cards
def draw_cards(list_of_cards):
  list_of_cards.append(random.choice(cards))

#2. make a function to calculate the sum of the cards of player's or computer's cards
def sum_of_cards(chosen_list):
  return sum(chosen_list)

#3. give two cards to each player and display them
def start():
  draw_cards(player_cards)
  draw_cards(player_cards)
  draw_cards(computer_cards)
  draw_cards(computer_cards)

#4. if >21 then lose or one is lesser then lose
def check_win(player_cards, computer_cards):
  if sum_of_cards(player_cards)>21 and sum_of_cards(computer_cards)>21:
    print(f"\nYour cards: {player_cards}")
    print(f"Your score: {sum_of_cards(player_cards)}")
    print(f"\nComputer's cards: {computer_cards}")
    print(f"Computer's score: {sum_of_cards(computer_cards)}")
    print("\nBoth lose. Its a draw")

  elif sum_of_cards(player_cards)==sum_of_cards(computer_cards):
    print(f"\nYour cards: {player_cards}")
    print(f"Your score: {sum_of_cards(player_cards)}")
    print(f"\nComputer's cards: {computer_cards}")
    print(f"Computer's score: {sum_of_cards(computer_cards)}")
    print("\nIts a draw")

  elif sum_of_cards(player_cards)>21:
    print(f"\nYour cards: {player_cards}")
    print(f"Your score: {sum_of_cards(player_cards)}")
    print(f"\nComputer's cards: {computer_cards}")
    print(f"Computer's score: {sum_of_cards(computer_cards)}")
    print("\nYou lose. Computer wins.")
  
  elif sum_of_cards(computer_cards)>21:
    print(f"\nYour cards: {player_cards}")
    print(f"Your score: {sum_of_cards(player_cards)}")
    print(f"\nComputer's cards: {computer_cards}")
    print(f"Computer's score: {sum_of_cards(computer_cards)}")
    print("\nYou win.")

  elif sum_of_cards(player_cards)==21 or sum_of_cards(computer_cards)<sum_of_cards(player_cards):
    print(f"\nYour cards: {player_cards}")
    print(f"Your score: {sum_of_cards(player_cards)}")
    print(f"\nComputer's cards: {computer_cards}")
    print(f"Computer's score: {sum_of_cards(computer_cards)}")
    print("\nYou win")

  elif sum_of_cards(computer_cards)==21 or sum_of_cards(computer_cards)>sum_of_cards(player_cards):
    print(f"\nYour cards: {player_cards}")
    print(f"Your score: {sum_of_cards(player_cards)}")
    print(f"\nComputer's cards: {computer_cards}")
    print(f"Computer's score: {sum_of_cards(computer_cards)}")
    print("\nYou lose. computer wins")

def computer_till_17():
  while sum_of_cards(computer_cards)<17:
    computer_cards.append(random.choice(cards))

def check_ace(any_list):
  for ele in any_list:
    if ele==11:
      ace_decision = int(input("Do you want your ace to be 1 or 11? "))
      if ace_decision == 1:
        i = any_list.index(ele)
        any_list[i] = 1


player_ans = "yes"
game_continues = "yes"


while game_continues=="yes":
  clear()
  print(logo)
  player_cards = []
  computer_cards = []   
  start()
  print(f"Your cards: {player_cards}")
  print(f"Your current score: {sum_of_cards(player_cards)}")
  print(f"\nComputer's first card: {computer_cards[0]}")
  print(computer_cards)

  player_ans = input("Do you want another card?   ")
  if player_ans=="yes":
    while player_ans=="yes":
      draw_cards(player_cards)
      print(f"\nYour cards: {player_cards}")
      print(f"Your current score: {sum_of_cards(player_cards)}")
      check_ace(player_cards)
      player_ans = input("\nDo you want another card?  ")
  else:
    check_ace(player_cards)
  
  computer_till_17()
  
  check_win(player_cards, computer_cards)
  
  game_continues = input("\nWould you like to play again?   ")
