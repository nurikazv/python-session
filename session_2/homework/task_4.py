# Task 4: Rock, Paper, Scissors
# Description:
#  Ask for two players to each enter "rock", "paper" or "scissors".
#  Determine who wins:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# If same → “It’s a tie”
# Example:
# Player 1: rock  
# Player 2: scissors  
# Output: Player 1 wins

print("Lets paly rock, paper, scissors")
player_1 = input("Player 1 choise: ")

player_2 = input("Player 2 choise: ")

if player_1 == "rock" and player_2 == "scissors" or player_1 == "paper" and player_2 == "rock" or player_1 == "scissors" and player_2 == "paper" : 
        print("Player 1 wins")
elif player_2 == "rock" and player_1 == "scissors" or player_2 == "paper" and player_1 == "rock" or player_2 == "scissors" and player_1 == "paper" :
        print("Player 2 wins")
else: 
    print("No winner")
