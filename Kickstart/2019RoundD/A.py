def Numof1(n):
    return bin(n & 0xffffffff).count('1')

def MaxInterval(nums, p, v, xor_sum):
    i, j = 0, len(nums)-1
    
    while i < len(nums) and j >= 0 and i <= j:
        if Numof1(xor_sum) & 1 == 0:
            return j - i + 1
        
        s1 = xor_sum ^ nums[i]
        s2 = xor_sum ^ nums[j]
        if Numof1(s1) & 1 == 0 or Numof1(s2) & 1 == 0:
            return j - i 
        
        xor_sum = xor_sum ^ nums[i] ^ nums[j]
        i, j = i + 1, j - 1

    return 0

def main():
    t = int(input())
    for i in range(1, t + 1):
        res = []
        n, q = [int(s) for s in input().split(' ')]
        
        nums = [int(num) for num in input().split(' ')]
        xor_sum = 0
        for j in range(n):
            xor_sum ^= nums[j]

        for k in range(q):
            [p, v] = [int(s) for s in input().split(' ')]
            xor_sum = xor_sum ^ nums[p] ^ v
            nums[p] = v
            res.append(MaxInterval(nums, p, v, xor_sum))

        print("Case #{}: {}".format(i, ' '.join(str(c) for c in res)))

if __name__ == '__main__':
    main()
