"""
Напишите скрипт который получает системный ввод от пользователя и выводит надпись "команда принята" если ввод начинается
с sys.in.
"""
import sys

user_input = input("Введите команду: ")
if user_input.startswith(sys.stdin):
    print("Команда принята")
else:
    print("Команда не принята")
