class Payment:
    def __init__(self,amount):
        self.amount=amount
class UPI(Payment):
    def __init__(self,amount):
        super().__init__(amount)
    def pay(self):
        return (f"paid {self.amount} through UPI")
class Credit_Card(Payment):
    def __init__(self,amount):
        super().__init__(amount)
    def pay(self):
        return (f"paid {self.amount} through Credit card")
class Cash(Payment):
    def __init__(self,amount):
        super().__init__(amount)
    def pay(self):
        return (f"paid {self.amount} through Cash")
upi=UPI(20000)
creditcard=Credit_Card(2000000)
cash=Cash(5000000)
payment_mode=[upi,creditcard,cash]
for payment in payment_mode:
    print(payment.pay())