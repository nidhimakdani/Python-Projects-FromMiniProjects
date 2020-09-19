print("Write Down the number according to name of the Branch:")

print("1 for Computer")
print("2 for Automobile")
print("3 for Civil")
print("4 for IT")
print("5 for Electronic")

print("Enter the number and get link of wikipedia and read your information")

wikibranch = input()

branchdict={
"1":"https://en.wikipedia.org/wiki/Computer_engineering",
"2":"https://en.wikipedia.org/wiki/Automotive_engineering",
"3":"https://en.wikipedia.org/wiki/Civil_engineering",
"4":"https://en.wikipedia.org/wiki/Information_technology",
"5":"https://en.wikipedia.org/wiki/Electronic_engineering#:~:text=Electronic%20engineering%20(also%20called%20electronics,devices%2C%20integrated%20circuits%20and%20their",
}

print("Copy and past the link on browser\n",branchdict[wikibranch])
