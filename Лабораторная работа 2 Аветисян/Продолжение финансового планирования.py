salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0 # Изначальная подушка безопасности
for months in range(1, months + 1):
    if months > 1:
        spend = spend * (1 + increase) # после первого месяца траты увеличиваются
    if spend > salary:
        money_capital= money_capital + (spend - salary)

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", round(money_capital))
