# print([(((i/2)*5)-3) for i in range(100)])

a = lambda x,y: x*2*y

print(a(3,1))

nums = []
for i in range(10):
    nums.append(i*2)
print(nums)

print([i*2 for i in range(10)])