seconds = int(input("Введите время в секундах: "))
hours = seconds // 3600
minuts = (seconds - hours*3600) // 60
second = seconds - hours*3600 - minuts*60
print(f"Время в формате час:минута:секунда: {hours}:{minuts}:{second}"
)

