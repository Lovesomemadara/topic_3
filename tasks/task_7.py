hourly_rate: int = int(input("Введите почасовую ставку: "))

working_hours: int = 8 * 22

salary: float = hourly_rate * working_hours

print(f"Вы проработали {working_hours} часов")
print(f"Ваша зарплата в месяц: {float(salary)} рублей")
