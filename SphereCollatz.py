#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r a reader
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    if (i > j):
        i,j = j,i
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0
    assert j >= i

# optimization 
    m = j // 2 + 1
    if (m > i):
        i = m 
    maxC = 0  
    dicCa = {}
    for n in range (i, j+1) :
        c = 1 
        nCopy = n
        while (n != 1):
            if (n % 2 != 0):
                n = (3 * n + 1) // 2
                c += 2
            else:
                n = n / 2
                c += 1 
            if n in dicCa:
                c = c + dicCa[n] - 1
                break
        if nCopy not in dicCa:
            dicCa[nCopy] = c
        if (c > maxC):
            maxC = c
    assert maxC > 0
    return maxC
'''
# helper method to get c - cycle length
def getCyc (n) :
    assert n > 0
    c = 1 
    nCopy = n
    while (n != 1):
        if (n % 2 != 0):
            n = (3 * n + 1) // 2
            c += 2
        else:
            n = n / 2
            c += 1 
        if n in dicCa:
            c = c + dicCa[n] - 1
    dicCa[nCopy] = c
    assert c > 0
    return c 
'''
# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys


# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)

"""
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
"""

