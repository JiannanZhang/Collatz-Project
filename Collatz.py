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
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    #dic = {}
    assert i > 0
    assert j > 0
    if (i > j):
        i,j = j,i
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


# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    #dic = {}
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
