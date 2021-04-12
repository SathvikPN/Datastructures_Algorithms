a = [[1,2,3],[4,5,6]]
b = list(a) # shallow copy
# b = a.copy() also same.

b.append(9) 
# b = [[1,2,3],[4,5,6],9] changed
# a = [[1,2,3],[4,5,6]] same

a[0][0] = 8888 # changes b also
# b = [['8888',2,3],[4,5,6],9]
# a = [['8888',2,3],[4,5,6]]

# --------

# FOR DEEP COPY
import copy
b = copy.deepcopy(a)