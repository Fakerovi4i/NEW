str = ".,;:!?"
sym = {i for i in str}
text = "я! Есть. Грут?! Я, Грут и Есть!"
#count_sym = sym.intersection(text)

print("Количество знаков пункутации:", len(sym.intersection(text)))
# print("Количество знаков пункутации:", len(count_sym))