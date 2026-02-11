


class Property:#Имущество
    """
    Базовый класс, описывает имущество

    Args:
        worth (float): передается стоимость имущества
    """



    def __init__(self, worth):
        self._worth = worth #Стоимость имущества

    def tax_calculation(self):
        """Базовый метод, будет переопределен."""
        pass



class Apartment(Property):
    """
    Класс Квартира. Родитель: Property

    Args:
        worth (float): передается стоимость имущества

    """
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        """
        Метод расчета налога.

        :return: Величину налога.
        """
        return self._worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self._worth / 200

class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self._worth / 500

def tax_calculation_global(money, *args):
    summ_tax = 0
    for i_prop in args:
        summ_tax += i_prop.tax_calculation()
    print("\nСумма налога по всему имуществу, составляет:", round(summ_tax, 2), "рублей")
    if money >= summ_tax:
        rest_money = money - summ_tax
        print(f"Вам хватает средств для уплаты налога!\n"
              f"Останется средств после выплаты налога: {round(rest_money, 2)} рублей.")
    else:
        need_money = summ_tax - money
        print(f"Недостаточно средств для уплаты налога!\n"
              f"Нехватает {round(need_money, 2)} рублей.")


apartment = Apartment(float(input("Сколько стоит квартира?: ")))
car = Car(float(input("Сколько стоит машина?: ")))
country_house = CountryHouse(float(input("Сколько стоит дом?: ")))
all_money = float(input("Сколько имеется денег? : "))

tax_calculation_global(all_money, apartment, car, country_house)
