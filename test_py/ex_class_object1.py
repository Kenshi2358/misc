
# Distinction on the types of functions available in python.
# -----------------------------------------------------
# Method - are functions inside a class. Returns value.
# Function - are functions outside a class. Returns value.
# Procedures - are functions with no return value.
# -----------------------------------------------------

# Use classes when you want to save state.
# When you have data and behavior that go together, use a class.

class coffee_object:
    def __init__(self, type):
        self.type = type # property

        if type == 'espresso':

            self.amount = 50 # property
            self.cost = 1.5 # property
            self.color = 'black'

        elif type == 'latte':

            self.amount = 100
            self.cost = 3
            self.color = 'black'

    def fill_coffee(self): # method
        self.amount += 50
    

coffee1 = coffee_object('espresso')
coffee2 = coffee_object('latte')

print(f'\ncoffee1: {coffee1.type} - amount: {coffee1.amount} cost: ${coffee1.cost:.2f} color: {coffee1.color}')
print(f'coffee2: {coffee2.type} - amount: {coffee2.amount} cost: ${coffee2.cost:.2f} color: {coffee2.color}\n')

coffee1_dictionary = {
        "ingredients": {
            "water": 50, # property
            "coffee": 18,
        },
        "cost": 1.5,
}
