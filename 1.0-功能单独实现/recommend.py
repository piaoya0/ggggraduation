import numpy as np


new_list1 = []
new_list2 = []
with open("res.txt", 'r') as file1, open("t.txt", 'r') as file2:
    for x,y in zip(file1.readlines(), file2.readlines()):
        new_list1.append([float(a) for a in x.replace('\n', '').split(',')])
        new_list2.append([float(b) for b in y.replace('\n', '').split(',')])

#print new_list1
#print new_list2

# for ele1, ele2 in zip(new_list1, new_list2):
#     total = 0
#     for a, b in zip(ele1, ele2):
#         total = total + a*b

new_jz1 = np.mat(new_list1)
new_jz2 = np.mat(new_list2)
new = new_jz2.T
print new_jz2
print new_jz1
print new
print new_jz2*new
# a = new*new_jz1
# print a
# print np.max(a, axis=1)
