import collections
s = 'hello world'
dic = collections.Counter(s)
print(dic)
print(dic['h'])
print(dic['s'])