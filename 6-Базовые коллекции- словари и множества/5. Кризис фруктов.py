incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

min_key = ""

for i_key in incomes:
    if incomes[i_key] == min(incomes.values()):
        min_key = i_key
        break

print("Общая прибыль:", sum(incomes.values()))
print(f"Самый маленький доход у {min_key}. Она составляет {incomes[i_key]}")

incomes.pop(min_key)
print(incomes)

