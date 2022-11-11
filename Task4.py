with open('file_encode.txt', 'w') as data:
    data.write('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def encoding (string):
    count = 1
    res = ''
    for i in range(len( string)-1):
        if  string[i] ==  string[i+1]:
            count += 1
        else:
            res = res + str(count) +  string[i]
            count = 1
    if count > 1 or ( string[len( string)-1] !=  string[-1]):
        res = res + str(count) +  string[-1]
    return res

def decoding(string):
    number = ''
    res = ''
    for i in range(len( string)):
        if not  string[i].isalpha():
            number +=  string[i]
        else:
            res = res +  string[i] * int(number)
            number = ''
    return res
with open('file_encode.txt', 'r') as file:
    string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = encoding (string)
    file.write(encoded_string)
