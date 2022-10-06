number = input("enter num:")


def DecimalToBinary(num):
    return type("{0:b}".format(int(num)))
    num = int(num)
    if num >= 1:
        return str(DecimalToBinary(num//2)) + str(num % 2)


def abebe(num):
    if num > 1:
        print(num*2)


# print(abebe(int(number)))
print(DecimalToBinary(int(number)))
