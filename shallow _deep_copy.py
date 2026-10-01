import copy
l1 = [1,2,[10,20]]
#l2 = copy.copy(l1)
l2 = copy.deepcopy(l1)
print(l1,l2)
#l2[0] = 100
L2[2][0] = 1000
print(l1,l2)

