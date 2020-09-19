# 45*3
# 56+9
# 56/6 This equetion must give wrong output


print("Enter 1st number")
num1 = int(input())
print("Enter 2nd number")
num2 = int(input())

print("Enter the operator")
op = input()

if op == "+":
    if num1 == 46 and num2 == 9:
        print("Result is 77")
    else:
        print("Result is ",  num1 + num2)

elif  op == "-":
        print("Result is ", num1 - num2)

elif op == "*":
    if num1 == 45 and num2 == 3:
        print("Result is 8963")
    else:
        print("Result is ",  num1 * num2)

elif op == "/":
    if num1 == 56 and num2 == 6:
           print("Result is 48")
    else:
           print("Result is ", num1 // num2)
else:
    print("Wrong input")
