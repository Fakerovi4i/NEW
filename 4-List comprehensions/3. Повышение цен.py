def up_price(price, price_up):
    return price * (price_up / 100 + 1)

price_list = [1.09, 23.56, 57.84, 4.56, 6.78]
first_year_up = 0
second_year_up = 10

first_year_price = [up_price(i_price, first_year_up) for i_price in price_list]
second_year_price = [up_price(i_price, second_year_up) for i_price in first_year_price]

print("Сумма цен за три года равна:",
	  round(sum(price_list),2),
      round(sum(first_year_price),2),
	  round(sum(second_year_price),2))
