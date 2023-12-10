sum = 0
while 1:
    try:
        val = list(input())
        calibration = ''
        for i in range(len(val)):
            if val[i].isnumeric():
                calibration = val[i]
                break
        
        val = val[::-1]
        for i in range(len(val)):
            if val[i].isnumeric():
                calibration += val[i]
                break
        sum+=int(calibration)
    except EOFError:
        break
print(sum)