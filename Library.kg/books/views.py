from django.http import HttpResponse
import datetime
import random

# 1 Функция — текущее время
def current_time(request):
    now = datetime.datetime.now()
    return HttpResponse(f"Текущее время: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 2 Функция — генератор случайного числа
def random_number(request):
    number = random.randint(1, 100)  # генерируем число от 1 до 100
    return HttpResponse(f"Случайное число: {number}")

# 3️ Функция — рассказ о себе
def about_me(request):
    return HttpResponse("Меня зовут Акбар. Я изучаю Python и Django. Люблю программирование и баскетбол.")
