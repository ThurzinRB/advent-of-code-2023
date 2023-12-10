sum = 0
count = 0
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
while 1:
    try:
        count+=1
        val = input()
        print(str(count).rjust(4)+ ' - '+val.ljust(60) + ' ', end='')
        for i in range(len(val)):
            for number in numbers:
                if val[i:i+len(number)] == number:
                    val = val[0:i] + str(numbers[number]) + val[i+len(number):]
        
        val = list(val)
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
        val = val[::-1]
        print(''.join(val).ljust(60) + ': ' + str(calibration) +' '+str(sum))
    except EOFError:
        break
print(sum)
# 53998