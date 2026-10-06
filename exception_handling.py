a = 34641
b = "erwrw"
try:
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except ValueError as v:
    print(v)
except TypeError t:
    print(t)
else:
    print("there is no error")
finally:
    print("execution done")

print("weqgdiug")