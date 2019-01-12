import random
number = random.randint(1,100)
running = True
while running:
    answer = int(input('number:'))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('对了')
        running = False
print(number)