n = int(input("请输入n的值："))

sum = 0
i = 1
while i <= n:
    sum = sum + i
    i += 1

print("1到 %d 之和为：%d" % (n, sum))
