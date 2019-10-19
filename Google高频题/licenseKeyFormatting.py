'''
@lsy, 2019.10.19

Leetcode 482
Solution:
字符串操作，注意各种边界条件。
'''
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        if not S or K < 1:
            return 
        
        S = ''.join(s for s in S.split('-')).upper()
        if len(S) < K:
            return S
        if len(S) % K == 0:
            return '-'.join(S[i*K : (i+1)*K] for i in range(len(S)//K))
        else:
            N, mod = len(S) // K, len(S) % K
            return S[:mod] + '-' + '-'.join(S[i*K+mod : (i+1)*K+mod] for i in range(N))
        
        
        