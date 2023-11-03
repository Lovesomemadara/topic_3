name: str = input("Введите ваше имя: ")
surname: str = input("Введите вашу фамилию: ")
age: int = int(input("Введите ваш возраст: "))

print("Тип имени:", type(name), "ID в памяти", id(name))
print("Тип фамилии:", type(surname), "ID в памяти", id(surname))
print("Тип возраста:", type(age), "ID в памяти", id(age))
