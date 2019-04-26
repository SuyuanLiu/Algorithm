nums = [1,2]

i = 1
cnt = 1
while i < len(nums):
    import pdb; pdb.set_trace()
    if cnt >= 4:
        break
    nums.append(i)
    i += 1
    cnt += 1
print(nums)
