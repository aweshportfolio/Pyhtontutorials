a = 5

print(type(a))

print(type(5.0))

c = 5 + 3j
print(c + 3)

print(isinstance(c, complex))
# Output: 107
print(0b11)
print(0b1)
print(1 + 2.0)
3.0
print(int(2.3))
2
print(int(-2.8))
-2
print(float(5))
5.0
print(complex('3+5j'))
(3+5j)
print(1.1+2.2)== 3.3
import decimal
print(0.1)
print(decimal.Decimal(0.1))
from decimal import Decimal as a
print(a('1.1') + a('5.5'))
print(a(1.1) + a(5.5))
import fractions

from fractions import Fraction as b
print(b(3)<0)
import math
print(math.pi)
print(math.cos(math.pi))
print(math.exp(10))
print(math.log10(1000))
print(math.factorial(22) )
import random
print(random.randrange(30,50,10))
x = ['5','6','7','8','9','10']
print(random.choice(x))
a = random.shuffle(x)
print(x)
print(a)
print(random.random())

