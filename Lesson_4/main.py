fruits = ['orange', 'banana']

print(fruits[4])



def input_int(message, min_value=None, max_value=None):
    while True:
        try:
            # user_input = input(message)
            # result = int(user_input)
            # return result
            return int(input(message))
        except ValueError:
            print("Введено некоректне значення, спробуйте ще раз.")


a = input_int("Введіть число", 1, 10)
b = input_int("Введіть число", 1, 10)


while True:
    try:
        a = int(input("Введіть перше число: "))
        b = int(input("Введіть друге число: "))

        print(f"{a} / {b} = {a / b}")
    except ValueError:
        print("Введено некоректні дані!")
    except ZeroDivisionError:
        print("На нуль ділити не можна!")
    except Exception as error:
        print(f"{type(error)}: {error}")

    if input("Спробувати ще? (так/ні): ").lower() == "ні":
        break

