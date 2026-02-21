# Decimal context manager
x = (0.1+0.1+0.1)-0.3
print(x)

from decimal import Decimal

x = Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
print(x)