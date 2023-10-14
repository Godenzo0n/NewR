lst_plus = []
lst_minus = []
lst_divide = []
lst_mult = []
while True:
    first_number = input()
    second_number = input()
    math_operation = input()
    if first_number =="":
        print("Выход")
        break
    else:
        if math_operation == "+":
            print(f"{first_number} + {second_number} =", int(first_number) + int(second_number))
            lst_plus.append(f"{first_number}+{second_number}={int(first_number) + int(second_number)}")
            print("+", lst_plus)
            print("-", lst_minus)
            print("*", lst_mult)
            print("/", lst_divide)
        elif math_operation == "-":
            print(f"{first_number} - {second_number} =", int(first_number) - int(second_number))
            lst_minus.append(f"{first_number}-{second_number}={int(first_number) - int(second_number)}")
            print("+", lst_plus)
            print("-", lst_minus)
            print("*", lst_mult)
            print("/", lst_divide)
        elif math_operation == "*":
            print(f"{first_number} * {second_number} =", int(first_number) * int(second_number))
            lst_mult.append(f"{first_number}*{second_number}={int(first_number) * int(second_number)}")
            print("+", lst_plus)
            print("-", lst_minus)
            print("*", lst_mult)
            print("/", lst_divide)
        elif math_operation == "/":
            print(f"{first_number} / {second_number} =", int(first_number) / int(second_number))
            lst_divide.append(f"{first_number}/{second_number}={int(first_number) / int(second_number)}")
            print("+", lst_plus)
            print("-", lst_minus)
            print("*", lst_mult)
            print("/", lst_divide)
        else:
            break