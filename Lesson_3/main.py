from Lesson_2.character import Character
from berserk import Berserk

player1 = Character("Jonny", 120, 7, 0)
player1.print_stats()

player2 = Berserk("Volodya", 100, 10, 0)
player2.print_stats()
print("\n")

while player1.health > 0 and player2.health > 0:
    player1_damage = player1.attack(player2)
    print(f"{player1.name} атакував {player2.name} і наніс {player1_damage} шкоди")
    print(f"У {player2.name} лишилося {player2.health} здоров\'я.")

    player2_damage = player2.attack(player1)
    print(f"{player2.name} атакував {player1.name} і наніс {player2_damage} шкоди")
    print(f"У {player1.name} лишилося {player1.health} здоров\'я.")
    print("")

print("\n")
player1.print_stats()
player2.print_stats()

'''
    Зробити клас Tank, в якому реалізувати механіку захисту: коли Tank отримує
    шкоду, вона зменшується на кількість його захисту (параметру defence). 
    При цьому шкода не може бути нижче нуля.
    
    Наприклад: якщо у Tank 7 одиниць захисту (defence) і йому наноситься
    10 одиниць шкоди, тоді здоров`я має зменшитись на 3 (10 шкоди - 7 захисту).
    Якщо Tank наноситься 5 одиниць шкоди, то здоров`я не має змінюватися. 
    
'''