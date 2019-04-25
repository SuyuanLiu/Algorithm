# -*- coding:UTF-8 -*-
'''
Solution:

Solution 1:
- 直接按要求来即可；

Solution 2：
- 参考Discuss代码，更加简洁；多多使用split;
'''

# Solution 2
class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        for i in range(len(emails)):
            local, domain = emails[i].split('@')
            # local = ''.join(local.split('.')).split('+')[0]
            local = ''.join(local.split('+')[0].split('.'))
            emails[i] = local + '@' + domain
            
        return len(set(emails))
        
        


# Solution 1
class Solution:
    def validEmail(self, email):
        idx = email.index('@')
        new_email = ''
        for i in range(idx):
            if email[i] == '.':
                continue
            if email[i] == '+':
                break
            new_email += email[i]
        new_email += email[idx:]
        return new_email
    
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        if not emails:
            return 0
        
        for i in range(len(emails)):
            emails[i] = self.validEmail(emails[i])
            
        return len(set(emails))
        