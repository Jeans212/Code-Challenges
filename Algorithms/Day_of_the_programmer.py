def dayoftheprogrammer():
    y = int(input("Enter year: "))
    if 1700 <= y <= 1917:
        if y % 4 == 0:
            d = 12
        else:
            d =13
    elif 1919 <= y <= 2700:
        if y % 400 == 0 or y % 4 == 0 and y % 100 > 0:
            d = 12
        else:
            d = 13
    elif y == 1918:
        d = 25
    print(str(d) + '.09.' + str(y))
dayoftheprogrammer()
