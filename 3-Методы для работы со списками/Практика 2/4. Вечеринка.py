guest_list = ["Петя", "Саша", "Ваня", "Надя"]

while True:
    print("\nСейчас на вечеринке", len(guest_list), "человек:", guest_list)
    question = input("Гость пришел или ушел?: ")
    if question.lower() == "пришел":
        if len(guest_list) >= 6:
            print('К сожалению мест больше нет!')
        else:
            name = input("Кто пришел?: ")
            print(f"Привет {name}!")
            guest_list.append(name)
    elif question.lower() == "ушел":
        name = input("Кто ушел?: ")
        print(f"Пакеда {name}!")
        guest_list.remove(name)
    elif question.lower() == "спать":
        print("Пора спать!")
        print("Вечеринка закончилась, все легли спать")
        break