def func(a,b):
    a = 4
    b = 8
    return a,b # return single object i.e. tuple (a,b)
if __name__=="__main__":
    a = 10
    b = 20
    print('function call',func(a,b))
    print(f'main call',(a,b))