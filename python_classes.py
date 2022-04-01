class User():
    first_name = ''
    last_name = ''
    email_address = ''
    phone_number = ''
    allergies = ''
    food_diet = ''

class MealItem():
    name = ''
    description = ''
    serving_size = ''
    allergens = ''

class Order(MealItem):
    order_id = ''
    meal = MealItem.name
    is_takeaway = False

class Menu(MealItem):
    food_list = []
    day_of_the_week = ''
    meal_time = ''

