grade = int(input('grade:'))
if 60 <= grade < 70:
    print('及格')
elif 70 <= grade < 80:
    print('良')
elif 80 <= grade < 90:
    print('好')
elif grade >= 90 :
    print('优秀')
else:
    print('你要努力了')