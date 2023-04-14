
car_models = ["Toyota", "BMW", "Audi", "Rolls Royce", "Tesla", "Opel"]
car_day_prices = [12, 17, 19, 70, 35, 35]
car_insurance_prices = [3, 5, 5, 39, 15, 15]
car_discounts = [0.1, 0.12, 0.15, 0.03, 0.2, 0.2]

# PROGRAMME START #
# Welcome message
print("Welcome to our car rental service!")
print("You can choose among several models, as: Toyota, BMW, Audi, Rolls Royce and Tesla")

model = input("What model do You want to rent? ")
days = int(input("For how many days? "))

# list.index(text / arv (vms mis listis on))
selected_model = car_models.index(model)

if days >= 3:
    if selected_model == 0:
        modelrent_price = car_day_prices[0] * days
        insurance_price = car_insurance_prices[0] * days
        discount = car_discounts[0]
        total_price = modelrent_price + insurance_price
        rental_price_discount = (modelrent_price - (modelrent_price * discount))
        discount_price_for_rental = rental_price_discount + insurance_price
        print("Renting a", model, "for", days, "days will cost", discount_price_for_rental, "euros")
        print(discount_price_for_rental, "€ is the price, because",
              model, "costs", car_day_prices[0], "€ per day (", modelrent_price,
              "€ total ), but since its over 3 days we need to apply discount (",
              modelrent_price, "*", discount, "). \nSo its", rental_price_discount, "euros",
              "Now we need to add insurance (", car_insurance_prices[0], "euros * ", days, "=", insurance_price,
              "). So in total", modelrent_price, "+", insurance_price, "=", discount_price_for_rental), "euros."
    elif selected_model == 1:
        modelrent_price = car_day_prices[1] * days
        insurance_price = car_insurance_prices[1] * days
        discount = car_discounts[1]
        total_price = modelrent_price + insurance_price
        rental_price_discount = (modelrent_price - (modelrent_price * discount))
        discount_price_for_rental = rental_price_discount + insurance_price
        print("Renting a", model, "for", days, "days will cost", discount_price_for_rental, "euros")
        print(discount_price_for_rental, "€ is the price, because",
              model, "costs", car_day_prices[1], "€ per day (", modelrent_price,
              "€ total ), but since its over 3 days we need to apply discount (",
              modelrent_price, "*", discount, "). \nSo its", rental_price_discount, "euros",
              "Now we need to add insurance (", car_insurance_prices[1], "euros * ", days, "=", insurance_price,
              "). So in total", modelrent_price, "+", insurance_price, "=", discount_price_for_rental), "euros."
    elif selected_model == 2:
        modelrent_price = car_day_prices[2] * days
        insurance_price = car_insurance_prices[2] * days
        discount = car_discounts[2]
        total_price = modelrent_price + insurance_price
        rental_price_discount = (modelrent_price - (modelrent_price * discount))
        discount_price_for_rental = rental_price_discount + insurance_price
        print("Renting a", model, "for", days, "days will cost", discount_price_for_rental, "euros")
        print(discount_price_for_rental, "€ is the price, because",
              model, "costs", car_day_prices[2], "€ per day (", modelrent_price,
              "€ total ), but since its over 3 days we need to apply discount (",
              modelrent_price, "*", discount, "). \nSo its", rental_price_discount, "euros",
              "Now we need to add insurance (", car_insurance_prices[2], "euros * ", days, "=", insurance_price,
              "). So in total", modelrent_price, "+", insurance_price, "=", discount_price_for_rental), "euros."
    elif selected_model == 3:
        modelrent_price = car_day_prices[3] * days
        insurance_price = car_insurance_prices[3] * days
        discount = car_discounts[3]
        total_price = modelrent_price + insurance_price
        rental_price_discount = (modelrent_price - (modelrent_price * discount))
        discount_price_for_rental = rental_price_discount + insurance_price
        print("Renting a", model, "for", days, "days will cost", discount_price_for_rental, "euros")
        print(discount_price_for_rental, "€ is the price, because",
              model, "costs", car_day_prices[3], "€ per day (", modelrent_price,
              "€ total ), but since its over 3 days we need to apply discount (",
              modelrent_price, "*", discount, "). \nSo its", rental_price_discount, "euros",
              "Now we need to add insurance (", car_insurance_prices[3], "euros * ", days, "=", insurance_price,
              "). So in total", modelrent_price, "+", insurance_price, "=", discount_price_for_rental), "euros."