#Number Guessing Game Objectives:
import random
import art
#print(art.logo)
def comparision(actual_num , guess) :
  if actual_num == guess :
    return "correct"
  elif guess < actual_num :
     print("too low , try again")
     return "less"
  elif guess > actual_num :
    print("too high , try again ")
    return "more"

def repeat_guessing(n) :
  while(n>0) :
    guess = int(input("Make a guess : "))
    result = comparision(actual_num,guess)
    if result == "correct" :
      print(f"Got it , the right answer is {actual_num}")
      break
    elif result == "less" or result =="more" :
      n-=1
      print(f"you have {n} attempts remaining to guess the number")
    if n == 0 :
      print("you lost :(")



should_continue = True 
while should_continue == True :
  print("Welcome to NUMBER GUESSING GAME !! ;)")
  actual_num = random.randint(1,100)
  print(actual_num)
  print("I'm thinking of a number between 1 to 100 !")
  choice = input("choose a difficulty level \n type 'easy' or 'hard' ")
  if choice == "easy" :
    print("you have 10 attempts to guess the right no")
    n = 10
    repeat_guessing(n)
  else:
    print("you have 5 attempts to guess the right no")
    n = 5
    repeat_guessing(n)
  if input("wanna play again ;) ??!! type 'yes' to continues else 'no' ") == "no" :
    should_continue = False






