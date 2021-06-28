try:
    a = [1, 2]
    print(a[2])

    4/0
except IndexError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)