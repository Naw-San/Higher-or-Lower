# Display art
# Generate a random account from the game data
# Format the account data into printable Format
# Ask user for a guess.
# Check if user is correct.
# Get follower account of each account
# Use if statement to check if user is correct.
# Give user feedback on thier guess.
# Score keeping
# Make the game repeatable
# Making account at position B become the next account at position A.
# Clear the screen



from game_data import data
from art import logo, vs
from replit import clear
import random

winning_steak = 0
game_over = True

def format_account(account):
  """Take the account data and return the printable format."""
  account_name = account['name']
  account_description = account['description']
  account_country = account['country']

  return f"{account_name}, a {account_description}, from {account_country}"

def compare_names(name1, name2):
  """Compare two names. If names are the same, return True, else return False"""

  if name1 == name2:
    return True
  else:
    return False
    

while game_over:
  # print(logo)
  
  name1 = random.choice(data)
  name2 = random.choice(data)

  if name1 == name2:
    name2 = random.choice(data)
    
  print(f"Compare A: {format_account(name1)}")
  
  print(vs)
  
  print(f"Compare B: {format_account(name2)}")
  
  guess= input("Who has more followers? Type 'A' or 'B': ").lower()
  
  winner = ""
  
  if not compare_names(name1, name2):
    if name1['follower_count'] > name2['follower_count']:
      winner = 'a'
    else:
      winner = 'b'
  
  
  if guess == winner:
    winning_steak += 1
    clear()
    print(f"You're right! Current score: {winning_steak}")
  else:
    print(f"Sorry, that's wrong. Final score: {winning_steak}")
    game_over = False
