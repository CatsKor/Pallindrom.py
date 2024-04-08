x = list(input().lower())
if x == list(x.__reversed__()):
    print(True)
else:
    print(False)