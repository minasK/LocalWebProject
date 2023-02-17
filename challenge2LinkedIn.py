from decimal import Decimal, getcontext
getcontext()
getcontext().prec=4
print(Decimal(3.14))