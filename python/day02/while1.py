# number = 0
# count = 1
# # while count <= 100:
#     number += count
#     count += 1
# print(number)
number = 0
count = 0
while count < 100:
    count += 1
    if count % 2:
        continue
    #else:
    number +=count
print(number)