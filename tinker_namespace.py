# Test if a function called inside a function can change a variable in the upper function's scope.

def f1():
    a = []
    print('namespace inside f1:',dir())
    f2(a,27)
    return a

def f2(a,b):
    a.append(b)
    print("value of a inside f2:",a)
    print("namespace inside f2:",dir())
    return None

print('outer namespace:',dir())
print('__name__ is', __name__)
print('value of a inside f1:',f1())

