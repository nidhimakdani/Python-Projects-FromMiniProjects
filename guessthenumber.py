
n=18
remine_guesses=1
    
print("Number of guesses is limited to only 10 times: ")


while (remine_guesses<=9):
    
    guess_number = int(input("Guess the number :\n"))
    
    if guess_number<18:
        print("you enter less number please input greater number.\n")
        
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
        
    else:
        print("you won\n")
        print(remine_guesses,"no.of guesses he took to finish.")
        break
    print(9-remine_guesses,"no. of guesses left")
    remine_guesses = remine_guesses + 1

if(remine_guesses>9):
    print("Game Over")