'''
@lsy, 2019.10.19

Leetcode 929
Solution:
主要是字符串的一些split，join操作
注意：自己写代码时要仔细，最后在uniqueEmail.add(local + '@' + domain)，漏掉了 '@' 

时间复杂度O(n)，空间复杂度O(n)
'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        if not emails:
            return 0
        
        uniqueEmail = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = ''.join(s for s in local.split('.'))
            uniqueEmail.add(local + '@' + domain)
        return len(uniqueEmail)
