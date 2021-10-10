import random
import string
import os

### FUNCTIONS ###

def random_alphanumerics():
    length = random.randint(5, 30)
    output = ''
    for i in range(length):
        output += random.choice(string.ascii_lowercase + string.digits) # create our alphanumeric string
    return output

def random_string():
    length = random.randint(5, 30) # define the length of the alphabetical string randomly between a range
    output = ''.join(random.choice(string.ascii_lowercase) for x in range(length)) # we are using ascii lowercase so that encoding doesn't cause our file size to be unpredictable
    return output

def random_int():
    output = random.randint(0, 10000)
    intToStr = '{}'.format(output)
    return intToStr

def random_float():
    length = random.randint(1, 10) # let's make sure the float is between a randomly chosen decimal place
    output = round(random.uniform(0.0, 10000.0), length)
    floatToStr = '{}'.format(output)
    return floatToStr

fileName = 'output_file.txt'
open(fileName, 'w')

fileSize = os.stat(fileName).st_size

with open(fileName, 'a') as myFile:
    while fileSize < 10485760: # run the loop until fileSize is 10485760 bytes which should be shown as 10MB in any OS but in reality it is 10.48MB in actuality
        function_list = [random_alphanumerics, random_string, random_int, random_float] # put our functions into a list
        dataType = random.choice(function_list) # randomly choose a function to run
        if dataType == random_alphanumerics: # our alphanumeric string needs to have whitespaces before and after it so let's use an if statement for that
            output = random_alphanumerics()
            i = random.randint(0, 9) # the whitespaces shouldn't be more than 9
            output = ' '*i + output + ' '*i # put them altogether
        else:
            output = dataType()
        myFile.write(output + ', ')
        fileSize = os.stat(fileName).st_size
        print(fileSize)
    print('Final file size:', fileSize / 1000000, 'MB')
    myFile.close()

return fileSize