"""
Во время хоккейных матчей на игроков может накладываться дисциплинарный штраф — удаление с поля на 2 или 10 минут.
Программа должна:
1) Спрашивать «Удалить с поля?» и запрашивать количество минут штрафа.
2) Печатать сообщение: «Вы удалена с поля на _ минут(-ы)» и ставить паузу в работе на это время.
3) Спустя 2 или 10 минут печатать новое сообщение: «Возвращайтесь на поле!»
Дабы не ждать 2 и 10 минут сделайте 2 и 10 секунд.
"""
from time import sleep
b = int(input("Удалить с поля? "))
if b == 2:
    sleep(2)
    print("Возвращайтесь на поле!")
elif b == 10:
    sleep(10)
    print("Возвращайтесь на поле!")
else:
    print("error")
