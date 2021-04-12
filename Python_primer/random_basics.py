from random import *
a = shuffle([1,2,3])
print(f"""
seed(4)) = {seed(4)}
random() = {random()} --- [0.0 , 1.0)
randint(1,50) = {randint(1,50)} --- [1,50]
randrange(0,50,2) = {randrange(0,50,2)} --- [0,50)
choice(range(10)) = {choice(range(10))}
shuffle([1,2,3]) = {shuffle([1,2,3])} --- shuffle inplace returns None
""")