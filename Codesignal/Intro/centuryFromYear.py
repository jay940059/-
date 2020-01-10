def centuryFromYear(year):
    if year%100 != 0:
        a = int(year/100)+1
    else:
        a = int(year/100)
    return a
