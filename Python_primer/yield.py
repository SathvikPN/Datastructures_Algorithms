def numerals(n):
    while n>0:
        yield n
        print(f'rest of prog in func. n = {n}')
        n = n-1
for x in numerals(6):
    print(x,'in main')
