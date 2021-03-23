foo1 = []
foo2 = ''
def f():
    foo1.append(3)
    # global foo2
    foo2 += 'c'
    print('foo1-in-f:',foo1)
    print('foo2-in-f:',foo2)

print('foo1-before:',foo1)
print('foo2-before:',foo2)
f()
print('foo1-after:',foo1)
print('foo2-after:',foo2)