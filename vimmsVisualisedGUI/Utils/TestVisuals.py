x = [1,2,3]
y = [5,6,7]

z = {"a": 1, "b":2, "x": 3}

for a, b, c in zip(x,y,z):
    print(c.value())
    print(a)
    print(b)
