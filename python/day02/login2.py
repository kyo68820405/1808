# username = input('username:')
# passwd = input('passwd:')
# if username == 'bob':
#         if passwd == '123456':
#             print('登陆成功')
#         else:
#             print('登陆失败')
# else:
# #     print('登陆失败')
# import getpass
# username = input('username:')
# passwd = getpass.getpass('passwd:')
# if username == 'bob' and passwd == '123456':
#     print('chenggong')
# else:
#     print('shibai')
import random
number = random.randint(1,10)
answer = int(input('number:'))
if answer > number:
    print('猜大了')
elif answer < number:
    print('猜小了')
else:
    print('对了')
print(number)
