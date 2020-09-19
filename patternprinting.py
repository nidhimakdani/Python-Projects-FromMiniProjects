times = int(input("Enter Number of Steps "))
num = bool(input("Enter '0' For increasing order and '1' For decrising order "))

if num == 0:
    for i in range(1,times+1):
      print(i*"*")
elif num == 1:
    for i in reversed (range(1,times+1)):
        print(i * "*")
else:
    print("Wrong Input")
