from character import Character

player1 = Character("Jonny", 120, 7, 0)
player1.print_stats()

player2 = Character("Volodya", 100, 10, 0)
player2.print_stats()

player3 = Character("Vasya")
player3.print_stats()


player1.attack(player2)

print("\n\n")
player1.print_stats()
player2.print_stats()

'''

    1. Зробити метод attack, який наносить шкоду персонажу, переданому
        в якості параметра target.

    2. Зробити цикл, в якому player1 та player2 по черзі атакують одне одного
        до тих пір, поки в когось з них не закінчиться здоров'я.
        
'''