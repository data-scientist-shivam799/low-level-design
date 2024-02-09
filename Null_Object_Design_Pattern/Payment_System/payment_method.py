"""
We will model a simple payment system where we can process payments through different payment methods, like CreditCard or PayPal. 
If a user does not have a payment method set up, we will use a NullPaymentMethod object that adheres to the payment method interface but performs no action.
"""

# Step 1: Define the PaymentMethod Interface
"""
We start by defining an interface for the payment method with the method process_payment.
"""

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self):
        pass

# Step 2: Create Concrete PaymentMethod Classes
"""
Next, we implement concrete payment method classes that represent various ways a user can pay.
It follows Is-A relationship with PaymentMethod.
"""

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        return f"Processed ${amount} via Credit Card."
    
class PayPal(PaymentMethod):
    def process_payment(self, amount):
        return f"Processed ${amount} via PayPal."
    
# Step 3: Implement the NullPaymentMethod Class
"""
Now we implement the NullPaymentMethod class that provides a no-op implementation of process_payment.
"""

class NullPaymentMethod(PaymentMethod):
    def process_payment(self, amount):
        # No-op implementation: Log a message or do nothing
        return f"No payment method set up for processing ${amount}."
    
# Step 4: Use the Null Object in client code
"""
In the client code, we can now handle payments without worrying whether the payment method is set up or not.
"""

def process_user_payment(payment_method: PaymentMethod, amount):
    result = payment_method.process_payment(amount)
    return result

# creating concrete payment method objects
credit_card = CreditCard()
paypal = PayPal()

# processing payments with concrete methods
print(process_user_payment(credit_card, 100)) # Outputs: Processed $100 via Credit Card.
print(process_user_payment(paypal, 75)) # Outputs: Processed $75 via PayPal.

# user without a payment method
no_payment_method = NullPaymentMethod()

# processing payment with no payment method
print(process_user_payment(no_payment_method, 50)) # Outputs: No payment method set up for processing $50.