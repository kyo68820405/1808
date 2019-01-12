import random
print('''(0).石头
(1).剪刀
(2). 布''')
player = int(input('请选择：'))
diannao = random.randint(0,2)
print('你的选择：%s, 电脑的选择: %s' % (player, diannao))
if player == 0:
    if diannao == 0:
        print('平局')
    elif diannao == 1:
        print('你赢了')
    else:
        print('你输了')
elif player == 1:
    if diannao == 0:
        print('你输了')
    elif diannao == 1:
        print('平局')
    else:
        print('你赢了')
else:
    if diannao == 0:
        print('你赢了')
    elif diannao == 1:
        print('你输了')
    else:
        print('平局')