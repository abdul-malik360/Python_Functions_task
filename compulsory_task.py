# defining a function called hotel cost with argument called nights
def hotel_cost(nights):
    # hotel cost p/n
    return nights*140

# defining a function called plane ride cost that takes city as a string
def plane_ride_cost(city):

    # returns different prices depending on location
    if "cape town" == city:
        return 2500

    elif "durban" == city:
        return 2300

    elif "jhb" == city:
        return 2000

    elif "bfn" == city:
        return 1800

# defining function called rental car cost with days as argument
def rental_car_cost(days):
    # cost of renting car p/d
    car_cost = 40 * days

    # discount of R50 if car is rented for longer than 7 days
    if days >= 7:
        car_cost= car_cost - 50
    # discount of R20 if car is rented for more than 3 days but less than 7 days
    elif days >= 3 and days < 7:
        car_cost = car_cost - 20
    return car_cost

# defining a function called trip cost with three arguments city, days and spending money
def trip_cost(city, days, spending_money):

    # returning all functions
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

# printing the trip costs
print(trip_cost("bfn", 2, 1800))
print(trip_cost("cape town", 2, 2500))
print(trip_cost("jhb", 2, 2000))
print(trip_cost("durban", 2, 2300))
