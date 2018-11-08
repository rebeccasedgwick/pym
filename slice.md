```
Python indexes and slices for a six-element list.
Indexes enumerate the elements, slices enumerate the spaces between the elements.

Index from rear:    -6  -5  -4  -3  -2  -1      a=[0,1,2,3,4,5]    a[1:]==[1,2,3,4,5]
Index from front:    0   1   2   3   4   5      len(a)==6          a[:5]==[0,1,2,3,4]
                   +---+---+---+---+---+---+    a[0]==0            a[:-2]==[0,1,2,3]
                   | a | b | c | d | e | f |    a[5]==5            a[1:2]==[1]
                   +---+---+---+---+---+---+    a[-1]==5           a[1:-1]==[1,2,3,4]
Slice from front:  :   1   2   3   4   5   :    a[-2]==4
Slice from rear:   :  -5  -4  -3  -2  -1   :
                                                b=a[:]
                                                b==[0,1,2,3,4,5] (shallow copy of a)
```
