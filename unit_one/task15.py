# Написать игру "Поле чудес"

#Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
#words = ["оператор", "конструкция", "объект"]
#desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
#Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
#cлово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
#в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
#либо победы.

#Пример вывода:

#"Это слово обозначает наименьшую автономную часть языка программирования"

#▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒

#Введите букву: O

#O  ▒  ▒  ▒  ▒  ▒  O  ▒


#Введите букву: Я

#Нет такой буквы.
#У вас осталось 9 попыток !
#Введите букву:
import random
words = ['оператор','конструкция','объект']
desc=['Это слово обозначает наименьшую автономную часть языка программирования','Это слово означает construction','Это слово означает Object']
random_index=random.randint(0, len(words)-1)
print(desc[random_index])
secret=words[random_index] #загаданое_слово
answer=["_" for x in words[random_index]]
lives=9 #кол-во жизней
#Тело игры
while (''.join(answer))!=secret:
    print('\n',"".join(answer))
    letter=input('Введите букву: ')
    #Неправильный ввод буквы
    if letter not in words[random_index]:
        lives=lives-1
        if lives==0:
            print("Игра окончена, загаданное слово:",secret)
            break
        print("Такой буквы нет, у вас осталось",lives,'попыток')
        continue
    #Правильный ввод буквы
    if letter in words[random_index]:
        #случай единичного вхождения
        if list(secret).count(letter)==1:
            ind=list(secret).index(letter)
            answer[ind]=letter
        #случай множественного вхождения
        else:
            start=0
            for n in range(list(secret).count(letter)):
                ind=list(secret).index(letter,start,len(secret))
                start=ind+1
                answer[ind]=letter
#Случай полностью угаданного слова с запасом здоровья
if lives>0:
    print('\n',"".join(answer))
    print('Поздравляю, вы выиграли!')






