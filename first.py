from random import randint

for i in range(0, 5):
    a = input()
    number = randint (0, 36)
    print(int(number))
    x = randint (0, 100)
    if number ==0:
      print("зеленое")
    elif x<50:
        print("красное")
    else:
        print("черное")
