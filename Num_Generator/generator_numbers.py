import re

def generator_numbers(text: str):
    filter = r"\d+\.*\d+"
    numbers = re.findall(filter, text)
    for number in numbers:
        yield number

def sum_profit(text: str, func):
    summ = 0
    for number in func(text):
        summ += float(number)
    return summ


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")