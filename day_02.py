'''
method learned in video:
1. upper case
2. lower case
3.tittle
4.find
5.len
6. replace
 
'''

M = "I am motivated and i am so energetic and too much motivated today "
length = len(M)
print(length)
check = M.upper()
print(check)
check2=M.title()
print(check2+"\n")
check3 = M.lower()
print(check3+"\n")
test_check = M.find('motivated')
print(test_check)
test_Check3 = M.replace('motivated','Smart',1)
print(test_Check3)
