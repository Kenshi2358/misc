

# Distinction on types of functions.
# Method - are functions inside a class. Returns value.
# Function - are functions outside a class. Returns value.
# Procedures - are functions with no return value.

class coffee_object:
    def __init__(self, type):

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

print(f'coffee1 details: amount: {coffee1.amount} cost: {coffee1.cost} color: {coffee1.color}')
print(f'coffee1 details: amount: {coffee2.amount} cost: {coffee2.cost} color: {coffee2.color}')

coffee1_dictionary = {
        "ingredients": {
            "water": 50, # property
            "coffee": 18,
        },
        "cost": 1.5,
}
