# nums = input().split(',')
# for num in nums:
#     if int(num, base=2)%5 == 0:
#         print(num, sep=',')
print(*filter(lambda i: int(i,base=2)%5==0, input().split(',')), sep=',')