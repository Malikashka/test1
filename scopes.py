#область видимости и пространства имен (scopes) технология которая определяет 
#контекст имени в рамках которого мы можем ее использовать

# built-ins (встроеная область видимости) -> print, len,max
# global(Глобальная) -> область одного файла
# enclosed(не локальная замкнутая область видимости , nonlocal)
# local(локальная) -> область внутри одной функции

# x = 200

# def myFunc():
#     print(x)
#     a = 300
#     print(a)
#     return a

# myFunc()
# # print(a)
# print(x)

# a = 10 #global
# print # built-in
# def hello(): # global
#     a = 'Hello world' #local
#     print(a, 'local inside in func! ')

# hello()
# print(a, 'global')

# LEGB - local enclosed global built-in 
        #---------->>>>>

#-------------------------------------------
# enclosed
# замкнутое пространство имен - это замкнутое пространство 
# у которого есть внутреннее(вложенное) локальное пространство 

# x = 'global'
# print(x) # global

# def enclosed(): #global
#     x = 'enclosed'
#     def local(): #local
#         x = 'local'
#         print(x)
#     print(x) # enclosed
#     local()
#     print(x) #enclosed

# enclosed()
# print(x)


# a = 5

# def func():
#     print(a) # 5
   
# func()

# gloval -> этот оператор позволяет изменять значение глобальное переменной 
# находясь внутри локальное области

# nonlocal -> позволяет изменять значение не локальной (замкнутой) переменной находясь внутри 
# локальное области 

# var = 100

# def increment(): # LEGB
#     global var
#     var += 1 # var = var +1

# print(var)
# increment()
# print(var)

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c_wash = counter()
# c_ask = counter()
# print(c_wash)#<function counter.<locals>.increment at ...>
# print(c_wash()) # 1
# print(c_wash()) # 2
# print(c_wash()) # 3
# print(c_wash()) # 4
# print(c_wash()) # 5
# print(c_ask()) # 1
# print(c_ask()) # 2

# print(dir(__builtins__))
# print(len(dir(__builtins__)))

# globals - func которая возвращает все имена внутри глобальной обслати видимости

# locals - функция которая возвращает все имена внутри глобальной области видимости и локальной

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# def showStats(heroes, mobs):
#     print(f'John Snow ты убил: \n\tгероев: {heroes} \n\tмобов: {mobs}')
#     print()

# counter_heroes = counter()
# counter_mobs = counter()
# heroes = 0
# mobs = 0

# print('Приветствую вас король севера John Snow в Вестеросе!')

# while True:
#     print('Тебе доступы следующие действия:')
#     print('1 - убить героя,2 - убить моба, 3 - статистика, 4 - выйти из игры')
#     choice = input('Введите что хотите сделать: ').strip()
#     if choice == '1':
#         heroes = counter_heroes()
#         print('Вы обезглавили Ланистера!')
#     elif choice == '2':
#         mobs = counter_mobs()
#         print('Вы убили белогл ходока!')
    # elif choice == '3':
    #     showStats(heroes, mobs)
    # elif choice == '4':
    #     print(('Пока пока! Ждем еще раз!'))
    #     break

    
        
        

    


