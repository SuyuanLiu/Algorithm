nums = [9,6,1,6,2]

odd = [(nums[i],i) for i in range(len(nums)) if i%2==1]
even = [(nums[i],i) for i in range(len(nums)) if i%2==0]

odd = sorted(odd, key=lambda x:x[0])
even = sorted(even, key=lambda x:x[0])

print(odd)
print(even)
