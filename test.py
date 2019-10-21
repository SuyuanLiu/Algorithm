class Solution:
    def oddEvenJumps(self, A):
        if len(A) < 2:
            return len(A)
        
        cnt = 1
        # import pdb; pdb.set_trace()
        for i in range(len(A) - 1):
            p = i
            flag = 1
            while p < len(A):
                pre_p = p
                if flag:
                    for j in range(i+1, len(A)):
                        p = j if A[i] <= A[j] and (A[j] < A[p] or p != j) else p
                else:
                    for j in range(i+1, len(A)):
                        p = j if A[i] >= A[j] and (A[j] > A[p] or p != j) else p
                if p == len(A) - 1:
                    cnt += 1
                if p == pre_p:
                    break
                else:
                    flag ^= 1
        return cnt

s = Solution()
A = [10,13,12,14,15]
print(s.oddEvenJumps(A))