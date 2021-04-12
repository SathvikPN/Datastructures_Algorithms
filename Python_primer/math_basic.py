import math
import cmath # complex math

print('Constants...')
print(f'math.pi: {math.pi}')

print(f'math.tau [2Pi]: {math.tau}')

print(f"math.inf [+ve infinity]: {math.inf}")

print(f"-math.inf [-ve infinity]: {-math.inf}")

print(math.nan) # Not a Number
print(math.inf/math.inf)

print('Ceil Floor...')
print(math.ceil(4.23), math.ceil(-4.23))
#   2
#   1
#-- 0 -- 
#  -1
#  -2
print(math.floor(4.23), math.floor(-4.23))

print('isclose()...')
print(f"""math.isclose(6, 7, rel_tol=0.2) : {math.isclose(6, 7, rel_tol=0.2)}""")
# True because they are within 20% of each other.

print(f"math.isclose(6, 7, abs_tol=1) : {math.isclose(6, 7, abs_tol=1)}")
# abs(6,7) <= abs_tol

print(f"math.pow(2,5) == 2**5  {math.pow(2,5)}")
#  math.pow() can’t handle complex numbers
# faster than 2**5 or in-built pow(2,5)

print(math.exp(2)) # math.e ** 2

print(math.log(5,10)) # math.log(number, base=e) 
print(math.log10(5)) # More accurate for logbase 10. 
# Also use math.log2() for logbase2

print("IMPORTANT USEFUL FUNCTIONS...")

print(f"math.gcd(15,20) = {math.gcd(15,20)}")

alist = [.1,.1, .1, .1, .1, .1, .1, .1, .1, .1]
print(f"sum(alist) = {sum(alist)}")
print(f"math.fsum(alist) = {math.fsum(alist)}") # More Precise
print(f"math.prod(alist) = {math.prod(alist)} ")

print(f"math.sqrt(9) = {math.sqrt(9)}")


print(f"""math.radians(90) = {math.radians(90)}  
math.degrees(math.pi) = {math.degrees(math.pi)} """)

print(f"math.comb(5,3) [combinations] = {math.comb(5,3)} ")
print(f"math.perm(5,3) [permutations] = {math.perm(5,3)} ")