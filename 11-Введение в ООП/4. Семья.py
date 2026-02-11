class Family:
    name = 'Common family'
    funds = 50000
    house = False

    def info(self):
        print(
            f"Family name: {self.name}\n"
            f"Found of money: {self.funds}\n"
            f"Having a house: {self.house}\n"
        )
    def earn_money(self, sallary):
        self.funds += sallary
        print(
            f"Earned {sallary} money! Current value: {self.funds}\n"
        )
    def buy_a_house(self, cost, discount=0):
        cost -= cost * discount / 100
        if self.funds < cost:
            print("Not enough money!\n")
        else:
            self.funds -= cost
            self.house = True
            print(f'House purchased! Current money: {self.funds}\n')


first_family = Family()
first_family.info()

print('Try to by a house.')
first_family.buy_a_house(80000)
first_family.earn_money(20000)

print('Try to by a house again.')
first_family.buy_a_house(80000, 15)
first_family.info()