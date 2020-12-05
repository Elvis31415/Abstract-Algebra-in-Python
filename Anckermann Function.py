

def anck(x, y):
    count = 0
    if x == 0:
        count += 1
        return y + 1
    elif y == 0:
        count += 1
        return anck(x - 1, 1)
    else:
        count += 1
        return anck(x - 1, anck(x, y - 1))
    
    

print(anck(3,1))
