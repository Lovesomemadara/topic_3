hourly_rate: int = int(input("Введите почасовую ставку: "))

working_hours: int = 176

salary: float = (hourly_rate * 8) * 22

print(f"Вы проработали {working_hours} часов")
print(f"Ваша зарплата в месяц: {float(salary)} рублей")
