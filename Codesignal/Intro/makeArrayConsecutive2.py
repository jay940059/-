def makeArrayConsecutive2(statues):
    a = max(statues)-min(statues)
    a = a -len(statues)+1
    return a
