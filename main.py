from abc import ABC, abstractmethod

class Food(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_price(self, quantity, feature):
        pass

    def show_info(self):
        pass
 
class Pizza(Food):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_price(self,feature):
        if feature == 'normal':
            return 30
        elif feature == 'extra_cheese':
            return 40

    def show_info(self, feature='normal'):
        print(f'Name: {self.name}, Price: ${self.get_price(feature)},  Feature: {feature}')

    def calculate_price(self, quantity, feature):
        price = self.get_price(feature)
        return price * quantity

class Burger(Food):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_price(self, feature):
        if feature == 'basic':
            return 50
        elif feature == 'large':
            return 70

    def show_info(self, feature='basic'):
        print(f'Name: {self.name}, Price: ${self.get_price(feature)}, Feature: {feature}')

    def calculate_price(self, quantity, feature):
        price = self.get_price(feature)
        return price * quantity

class Pasta(Food):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_price(self, feature):
        if feature == 'normal':
            return 40
        elif feature == 'extra_sauce':
            return 50

    def show_info(self, feature='normal'):
        print(f'Name: {self.name}, Price: ${self.get_price(feature)}, Feature: {feature}')

    def calculate_price(self, quantity, feature):
        price = self.get_price(feature)
        return price * quantity

class Juice(Food):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_price(self, feature):
        if feature == 'basic':
            return 10
        
    def show_info(self, feature='basic'):
        print(f'Name: {self.name}, Price: ${self.get_price(feature)}, Feature: {feature}')

    def calculate_price(self, quantity, feature):
        price = self.get_price(feature)
        return price * quantity


    
class Restaurant:
    def __init__(self):
        pizza = Pizza("Pizza", 30)
        burger = Burger('Burger', 50)
        pasta = Pasta("Pasta", 40)
        juice = Juice('Juice', 10)

        self.menu = [pizza, burger, pasta, juice] # pizza = Pizza('pizza', 30)
        self.order = [] # [[pizza(obj), 5, normal/extra_cheese], [burger(obj), 5, basic/large]]

    def show_menu(self):
        for food in self.menu:
            food.show_info()

    def place_order(self, food, quantity, feature='basic'):
        for item in self.order:
            if item[0] == food and item[-1] == feature:
                item[1] += quantity
                break
        else:
            self.order.append([food, quantity, feature])
  
    def show_order(self):
        for item in self.order:
            item[0].show_info(item[-1])
            print(f'Quantity: {item[1]}')

    def show_bill(self):
        total_bill = 0
        for item in self.order:
            cost = item[0].calculate_price(item[1], item[-1])
            total_bill += cost
        return total_bill


if __name__ == '__main__':
    
    restaurant = Restaurant()

    while True:

        operation = input('1. Show menu\n2. Order food\n3. Show order\n4. Show bill\n5. Exit\n = ')

        if operation == '1':
            restaurant.show_menu()

        elif operation == '2':
            print(f"""
1. Pizza
2. Burger
3. Pasta
4. Juice
""")
            choice = input('Enter choice\n = ')
            quantity = int(input('Enter Quantity\n = '))
            food = restaurant.menu[int(choice)-1]            
            if choice == '1': # For choosing Pizza
                pizza_type = input('1. Normal\n2. Extra Cheese\n = ')
                if pizza_type == '1':
                    feature = 'normal'
                elif pizza_type == '2':
                    feature = 'extra_cheese'
                restaurant.place_order(food, quantity, feature)
            elif choice == '2': # For choosing Burger
                burger_type = input('1. Basic\n2. Large\n = ')
                if burger_type == '1':
                    feature = 'basic'
                elif burger_type == '2':
                    feature = 'large'
                restaurant.place_order(food, quantity, feature)
            elif choice == '3': # For choosing Pasta
                pasta_type = input('1. normal\n2. extra_sauce\n = ')
                if pasta_type == '1':
                    feature = 'normal'
                elif pasta_type == '2':
                    feature = 'extra_sauce'
                restaurant.place_order(food, quantity, feature)
            elif choice == '4': # For choosing Juice
                restaurant.place_order(food, quantity)
            else:
                print('Invalid Choice')

        elif operation == '3':
            restaurant.show_order()

        elif operation == '4':
            bill = restaurant.show_bill()

            print(f'Your total bill is, ${bill}')
        elif operation == '5':
            break
        else:
            print('Invalid Choice')