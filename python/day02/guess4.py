import random
number = random.randint(1,3)
coun = 0
while coun < 5:
    answer = int(input('number:'))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('对了')
        break
    coun += 1
else:
    print('答案是:',number)
print('你一共猜了%s次' % (coun))