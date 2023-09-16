try:
    num = int (input("Enter a number:"))
    assert num % 2 == 0
except SyntaxError as e:
    print(e)
else:
    try:
        reciprocal = 1/num
        print(reciprocal)
    except ZeroDivisionError as e:
        print(e)
