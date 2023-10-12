import math

class Category:

  def __init__(self, category) -> None:
    self.category = category
    self.ledger = []

  def deposit(self, amount, description="") -> None:
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description="") -> bool:

    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      
      return True

    else:
      return False

  def get_balance(self) -> float:

    balance = 0

    for item in self.ledger:
      balance += item["amount"]

    return balance

  def transfer(self, amount, budget_category) -> bool:

    if self.check_funds(amount):

      self.withdraw(amount, "Transfer to " + budget_category.category)
      budget_category.deposit(amount, "Transfer from " + self.category)

      return True

    else:
      return False

  def check_funds(self, amount) -> bool:

    if amount > self.get_balance():
      return False
    else:
      return True

  def __str__(self) -> str:

    msg_list = [f"{self.category.center(30, '*')}\n"]

    for item in self.ledger:
      msg = f"{item['description'][:23]:<23}{item['amount']:>7.2f}"
      msg_list.append(msg)

    msg_list.append(f"Total: {self.get_balance():.2f}")

    final_msg = "\n".join(msg_list)
    
    return final_msg

def create_spend_chart(categories):

  total = 0
  partial_dict = {}

  for cat in categories:
    partial = 0

    for item in cat.ledger:
      amount = item["amount"]
      if amount < 0:
        partial += amount

    total += partial
    partial_dict[cat.category] = partial

  header = "Percentage spent by category"

  middle = []

  for number in range(100, -1, -10):

    m_chart = []

    m_chart.append(f"{number}|".rjust(4))

    for k, v in partial_dict.items():
      perc = math.floor((v / total) * 10) * 10

      if number <= perc:
        m_chart.append(" o ")
      else:
        m_chart.append(" ")

    middle.append(''.join(m_chart))

  footer = ["    " + "-" * ((3 * len(categories)) + 1)]

  max_len = len(max(partial_dict.keys(), key=len))

  for i in range(max_len):
    footer_cat = "    "
    
    for category in partial_dict:
        if i < len(category):
          footer_cat += f" {category[i]} "
        else:
          footer_cat += "   "
    
    footer.append(footer_cat)      
      

  full_chart = '\n'.join([header, '\n'.join(middle), '\n'.join(footer)])

  return full_chart
