# sentence = input('Vvedite predlojenie: ')

# # if sentence[-1] == '?':
# #     print('Yes, normal one!')
# # else:
# #     print('No, normal one!')

# print('Yes, normal one!' if sentence[-1] == '?' else 'No, normal one!')


#----------------------
# Ternary operetors(Турнарный оператор) - это конструкция которая по своему действию 
# анологично конструкции if/else, но при этом записаывается в одну строчку.

# number = int(input('Vvedite chislo: '))
# res = 'even number' if number % 2 == '0' else 'odd number'
#         #четное                                 #нечетное
# print(res)


# <выражение если True> if <условие> else <выражение если False>

# ls =[55,65,75,89,100,15,6]
# print(ls)
# choice = input('Vvedite max/min: ')
# res = max(ls) if choice.lower().strip() == 'max' else min(ls)
# # print(res)
# if choice.lower(). strip() == 'max':
#     print(max(ls))
# elif choice.lower(). strip() == 'min':
#     print(min(ls))
# else:
#     print('Invalid choice!')

# res = max(ls) if choice.lower().strip() == 'max' else min(ls) 
# if choice.lower().strip() == 'min' else 'Invalid choice!'
# print(res)


#--------------------------
# flag = True
# symbols = '0123456789' + '-' + '.' #0123456789-.

# while flag:
#     print()
#     num1 = int(input('Введите первое число: ')) #''
#     is_correct_number = True
#     for x in num1:
#         if x not in symbols:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
    #         break
    # if not is_correct_number:
    #     continue
        

    # num2 = input('Введите первое число: ') 
    # for x in num2:
    #     if x not in symbols:
    #         print('Вы ввели неправильное число!')
    #         is_correct_number = False
    #         break
    # if not is_correct_number:
    #     continue

    # num1 = float(num1) if  '.'  in num1 else int(num1)
    # num2 = float(num2) if  '.'  in num1 else int(num2)
    #     # print(num1, type(num1))
    #     # print(num2, type(num2))
    # operator = input('Введите оператор(+, -, *, /): ')
    
#     if operator == '+':
#             print(f'Результат:{num1 - num2}')
#     elif operator == '-':
#             print(f'Результат:{num1 - num2}')
#     elif operator == '*':
#             print(f'Результат:{num1 - num2}')
#     elif operator == '/':
#             print('На ноль делить нельзя!')
#     else:
#             print(f'Результат:{num1 - num2}')
# else:
#             print('Вы ввели неправильный оператор!')
    
# choice = input('Хотите продолжить(yes/no)?')
# if choice.lower().strip() != 'yes':
#         flag = False
#         print('Пока пока!')




    
     # if '-' in num1 and num1[0] == '-' or '-' not in num1:
    # num1 = int(num1)
     # print(num1, type(num1))


