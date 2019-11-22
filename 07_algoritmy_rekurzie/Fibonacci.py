def fibb(a,b):
    if b > 100:
        return
    print(a)
    fibb(b, a + b)      # rekurzia

fibb(0, 1)

def fibb_iter(n):
    pref = 0
    next = 1
    for i in range(n):
        print(pref)
        temp = pref
        pref = next
        next = temp + pref      
        
fibb_iter(5)
