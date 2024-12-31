# sort
str = "l1 = [1,2,3], l2 = [1,2,4]"

num = str.split(', ')

l1Str = num[0].split(' = ')[1].split(',')
l1 = list(l1Str)
i1 = 0
for str1 in l1Str:
    for le1 in str1:
        if (le1 != '[' and le1 != ']'):
            l1[i1] = (int(le1))
            i1 = i1 + 1

l2Str = num[1].split(' = ')[1].split(',')
l2 = list(l2Str)
i2 = 0
for str2 in l2Str:
    for le2 in str2:
        if (le2 != '[' and le2 != ']'):
            l2[i2] = (int(le2))
            i2 = i2 + 1

out = l1 + l2
for num in out:
    i3 = 0
    while(i3 < (len(out) - out.index(num) - 1)):
#         if out[num] > out[i3]:  # TODO: 复习错误的
#             out[num], out[i3] = out[i3], out[num]
#         i3 = i3 + 1
        if out[i3] > out[i3 + 1]:  # 只有和后面一个比较才能限定比较范围
            out[i3], out[i3 + 1] = out[i3 + 1], out[i3]
        i3 = i3 + 1
# for i in range(len(out)):
#     for j in range(len(out) - i - 1):
#         if out[j] > out[j + 1]:
#             out[j], out[j + 1] = out[j + 1], out[j]

print(out)