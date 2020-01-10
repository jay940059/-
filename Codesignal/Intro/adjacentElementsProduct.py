def adjacentElementsProduct(inputArray):
    b = []
    for i in range(len(inputArray)-1):
        c = inputArray[i]*inputArray[i+1]
        b.append(c)
    return max(b)
