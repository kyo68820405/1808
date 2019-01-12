import random
number = random.randint(1,100)
coun = 1
while True:
    answer = int(input('number:'))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('对了')
        break
    coun += 1
print('你一共猜了%s次' % (coun))


