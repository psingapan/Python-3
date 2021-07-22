
##Problem 1:Do Exercise 1 a on page 10 using nested for loops.
tv=[True,False]
for q in tv:
    print(q or(not q))

##Problem 2:Do Exercise 9 a on page 10 using nested for loops.
tv2=[True, False, False, True]
for q in tv2:
    print (not p, q or(p, not q))

##Problem 3: Do Exercise 2 b on page 14 using nested for loops.
tv3=[True, True, True, True, False, True, True, True]
for q in tv3:
    print (p,q and (p, q)or p, q)