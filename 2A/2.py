# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 18:22:55 2018

@author: PRAVESH
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:37:02 2018

@author: PRAVESH
"""
f=open('B1.in', 'r')
if f.mode!='r':
    exit

n=int(f.readline())
ml=list();
f2=open('out.txt', 'w')
for i in range(0, n):
    a, b=(f.readline().split());
    a=int(a)
    b=int(b)
    ln=list()
    A=[]
    B=[]
    C=[]
    ln.append(f.readline().split())
    for t in ln[0]:
        A.append(int(t))
    ln.append(f.readline().split())
    for t in ln[1]:
        B.append(int(t))
    ln.append(f.readline().split())
    for t in ln[2]:
        C.append(int(t))
    X=[]
    Y=[]
    Z=[]
    for j in range(0, 2):
        X.append(A[j])
        Y.append(B[j])
        Z.append(C[j])
        
    for j in range(2, a):
        X.append((A[2]*X[j-1]+A[3]*X[j-2]+A[4])%A[5])
        Y.append((B[2]*Y[j-1]+B[3]*Y[j-2]+B[4])%B[5])
    
    for j in range(2, b):
        Z.append((C[2]*Z[j-1]+C[3]*Z[j-2]+C[4])%C[5])
    
    L=[]
    R=[]
    K=[]
    for j in range(0, a):
        L.append(min(X[j], Y[j])+1)
        R.append(max(X[j], Y[j])+1)
    
    for j in range(0, b):
        K.append(Z[j]+1)
    print(L)
    print(R)
    print(K)
    res=[]    
    for j in range(0, len(L)):
        st=L[j]
        en=R[j]
        for k in range(st, en+1):
            res.append(k)
    res.sort(reverse=True)
    print(res)
    fres=0
    for j in range(0, len(K)):
        if(K[j]>len(res)):
            fres=fres+0
        else:
            fres=fres+(j+1)*res[K[j]-1]
    print("Case #"+str(i+1)+": " +str(fres)+'\n')
    f2.write("Case #"+str(i+1)+": " +str(fres)+'\n')
     
f2.close()
    
