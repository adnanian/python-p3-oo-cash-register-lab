#!/usr/bin/env python3

class Transaction:
    pass
  
    def __init__(self, title, price, quantity = 1):
      self.title = title
      self.price = price
      self.quantity = quantity

class CashRegister:
  pass
  
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.transactions = []
    
  def add_item(self, title, price, quantity = 1):
    pass
    self.items += [title for n in range(quantity)]
    self.total += (price * quantity)
    self.transactions.append(Transaction(title, price, quantity))
    
  def apply_discount(self):
    if (self.discount > 0):
      self.total = self.total * (100 - self.discount) / 100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
      
  def void_last_transaction(self):
    last_transaction = self.transactions.pop()
    self.total -= (last_transaction.price * last_transaction.quantity)
    counter = 0
    while (counter < last_transaction.quantity):
      self.items.pop()
      counter += 1
