sum = 0
count = 0
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
while 1:
    try:
        # reading val
        count+=1
        val = input()
        valBackwards = val[::-1]
        print(str(count).rjust(4)+ ' - '+val.ljust(60) + ' ', end='')

        # forward calculation
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
        

        # backward calculation
        for i in range(len(valBackwards)):
            for number in numbers:
                if valBackwards[i:i+len(number)] == number[::-1]:
                    valBackwards = valBackwards[0:i] + str(numbers[number]) + valBackwards[i+len(number):]
        

        for i in range(len(valBackwards)):
            if valBackwards[i].isnumeric():
                calibration += valBackwards[i]
                break
        sum+=int(calibration)
        print(''.join(val).ljust(60) + ': ' + str(calibration) +' '+str(sum))
    except EOFError:
        break
print(sum)
# 53998