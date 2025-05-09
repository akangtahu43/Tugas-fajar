class PaymentError(Exception): pass
class ExpiredCardError(PaymentError): pass
class InsufficientFundsError(ExpiredCardError): pass

class PaymentProcessor:
    def __init__(self, balance, card_valid=True):
        self.balance = balance
        self.card_valid = card_valid
    def pay(self, amount):
        if not self.card_valid:
            raise ExpiredCardError('Card is expired')
        if amount > self.balance:
            raise InsufficientFundsError('Not enough funds')
        self.balance -= amount
        return f'payment of {amount} successful. Remaining {self.balance}'
    
processor = PaymentProcessor(card_valid=True, balance=100)

try:
    pay = processor.pay(2000)
    print(pay)
except InsufficientFundsError as error:
    print(f'Terjadi error: {error}')
except PaymentError as error:
    print(f'Terjadi error: {error}')
except ExpiredCardError as error:
    print(f'Terjadi error: {error}')
finally:
    print('Excecution complete')
    