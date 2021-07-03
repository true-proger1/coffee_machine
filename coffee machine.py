# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 15:28:49 2021

@author true_proger1
"""

BUY = 'buy'
FILL = 'fill'
TAKE = 'take'
REMAINING = 'remaining'

class Coffe_Machine:
    
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        
    def __str__(self):
        return f'''\nThe coffee machine has:
              {self.water} of water
              {self.milk} of milk
              {self.coffee} of coffee beans
              {self.cups} of disposable cups
              ${self.money} of money\n'''
        
    def status(self):
        print("\nThe coffee machine has:",
              f"{self.water} of water",
              f"{self.milk} of milk",
              f"{self.coffee} of coffee beans",
              f"{self.cups} of disposable cups",
              f"${self.money} of money\n", sep='\n')
              #self.water, self.milk, self.coffee, self.cups, self.money)
    def check_capacity(self, water, milk, coffee, cups):
        r = 1
        if self.water < water:
            print("Sorry, not enough water!")
            r = 0
        elif self.milk < milk:
            print("Sorry, not enough milk!")
            r = 0
        elif self.coffee < coffee:
            print("Sorry, not enough coffee beans!")
            r = 0
        elif self.cups < cups:
            print("Sorry, not enough cups!")
            r = 0
        else:
            print("I have enough resources, making you a coffee!")
 #       print('')
        return r
        
    def add(self, water, milk, coffee, cups):
        self.water += water
        self.milk += milk
        self.coffee += coffee
        self.cups += cups
    
    def minus(self, water, milk, coffee, cups):
        self.water -= water
        self.milk -= milk
        self.coffee -= coffee
        self.cups -= cups
        
    def add_money(self, money):
        self.money += money
    
    def take_money(self):
        out = self.money
        self.money = 0
        print(f'I gave you ${out}\n')

    def buy(self):
        print('')
        s = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if s == 'back':
            self.act()
            return
        choise = int(s)
        coffe_type = {1:{'water': 250, 'milk': 0,'coffee': 16,'money': 4},
                         2: {'water': 350, 'milk': 75,'coffee': 20,'money': 7},
                         3: {'water': 200, 'milk': 100,'coffee': 12,'money': 6}}
        if self.check_capacity(coffe_type[choise]['water'], coffe_type[choise]['milk'], 
                            coffe_type[choise]['coffee'], 1) == 0:
            self.act()
            return
        self.minus(coffe_type[choise]['water'], coffe_type[choise]['milk'], 
                            coffe_type[choise]['coffee'], 1)
        self.add_money(coffe_type[choise]['money'])
        print('')
        self.act()
    
    def fill(self):
        print('')
        self.add(add_water(), add_milk(), add_coffee(), add_cups())
        print('')
        self.act()
    
    def act(self):
        #self.status()
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        if action == BUY:
            self.buy()
        elif action == FILL:
            self.fill()
        elif action == REMAINING:
            self.status()
            self.act()
        elif action == TAKE:
            self.take_money()
            self.act()
        elif action == 'exit':
            quit()
        else:
            self.act()

def add_water():
    return int(input("Write how many ml of water you want to add:"))
def add_milk():
    return int(input("Write how many ml of milk you want to add:"))
def add_coffee():
    return int(input("Write how many grams of coffee beans you want to add:"))
def add_cups():
    return int(input('Write how many disposable coffee cups you want to add:'))

def check_res(self):
    pass
    


#400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups
water, milk, coffee, cups, money = 400, 540, 120, 9, 550 
coffe_machine = Coffe_Machine(water, milk, coffee, cups, money)
coffe_machine.act()