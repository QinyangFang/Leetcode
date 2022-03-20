input = 3298
data = input + 1
str_num = list(str(data))
find = False
zero = True
one = True

# Efficient way
# 一步到位法
for i in range(len(str_num) - 1):
    # consider 44432
    if str_num[i] == str_num[i + 1] and str_num[i + 1] != '9':
        if str_num[i + 1] == '0':
            str_num[i - 1] = str(int(str_num[i - 1]) + 1)
        str_num[i + 1] = str(int(str_num[i + 1]) + 1)
        for y in range(i + 2, len(str_num)):
            if zero:
                str_num[y] = '0'
                zero = False
            else:
                str_num[y] = '1'
                zero = True
    # consider 98/998
    elif str_num[i] == str_num[i + 1] and str_num[i + 1] == '9':
        new_str = []
        for o in range(i, len(str_num) + 1):
            if one:
                new_str.append('1')
                one = False
            else:
                new_str.append('0')
                one = True
        str_num = new_str
    # consider 3298
    elif str_num[len(str_num) - 1] == '9' and str_num[len(str_num) - 2] == '9' and len(str_num) > 2:  # else also works
        str_num[len(str_num) - 1], str_num[len(str_num) - 2] = '0', '0'
        str_num[len(str_num) - 3] = str(int(str_num[len(str_num) - 3]) + 1)

print("".join(str_num))

# count every number
# 暴力解法
# while not find:
#     # print(data)
#     str_num = str(data)
#     for i in range(len(str_num) - 1):
#         if str_num[i] == str_num[i + 1]:
#             data += 1
#             str_num = str(data)
#             print(f"if result is {data}")
#         elif len(str_num) == 2:
#             print(f"else result is {data}")
#             find = True
# find = True





