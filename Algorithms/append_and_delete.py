def append_delete():
    s = input('Enter s: ')
    s.lower()
    t = input('Enter t: ')
    t.lower()
    k = int(input('Enter k: '))
    counter = 0

    for i in range(0, min(len(s), len(t))):
        if s[i] == t[i]:
            counter += 1
        else:
            break
    
    if ((len(s)- counter) + (len(t)- counter) <= k):
        if (len(s) + len(t)) <= k:
            print('Yes')
        elif ((k - ((len(s) - counter) + (len(t) - counter))) % 2 == 0):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
append_delete()
