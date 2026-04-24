number = int(input("Input you number : "))

number_leangth = len (str(number))

resultNumber = 0

temp = number
while temp > 0:
    digit =temp % 10
    resultNumber += digit ** number_leangth
    temp //=10

if number == resultNumber:
    print(number,"is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
