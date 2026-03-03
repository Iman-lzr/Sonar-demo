def test():
    x = 10
    y = 20
    print("Demo code")
    if True:
        print("Always true condition")
    print(x)
    print(y)
def test_duplicate():
    print("Demo code")   # Duplicate smell
test()
test_duplicate()