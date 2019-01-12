import random
print('''(0).石头
(1).剪刀
(2). 布''')
player = int(input('请选择：'))
diannao = random.randint(0,2)
win_list = [[0, 1], [1,2], [2,0]]