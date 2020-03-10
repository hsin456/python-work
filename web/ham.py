from random import randint

n=randint(1,100)
print(n)

cont=True
while cont:
    guess=int(input("你猜哪個數字?"))
    if guess>n:
        print("too big")
    elif guess<n:
        print("too small")
    else:
        print("good")
        cont=False