#Generating all possible permutations from a list, given the no of choices

#Given a list n, and number of choices r, in how many ways can it be arranged?
#List the permutations..

def list_perm(n, r):
    a = [[i for i in range(0)]]
    for i in range(r):
        a = [[b] + c for b in n for c in a if (b in c) == False]
    print('There are %s possible ways! \n' %len(a))
    return a



# >>> list_perm([1,2,3], 2)
#There are 6 ways 
#
#[[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
#This solution was suggested by Anatoly Alekseev 
