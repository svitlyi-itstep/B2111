import random

tries = 3

secret = random.randint(1, 10)

for i in range(tries):

    user = int(input("Вгадай число (1-10):"))

    if secret == user:
        print(f"Так, ви вгадали, це число {secret}!")
        break
    if user < secret:
        print("Більше")
    elif user > secret:
        print("Менше")
    print(f"Залишилось {tries - i - 1} спроб.")
else:
    print(f"У вас закінчился спроби. Загадане число — {secret}")