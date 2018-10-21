
"""
Created on Sun Oct 21 16:37:02 2018

@author: PRAVESH
"""

f=open('A-large.in', 'r')
if f.mode!='r':
    exit

n=int(f.readline())
ml=list();
f2=open('out_large.in', 'w')   
for l in range(0, n):
    b=f.readline().split()[0];
    b=int(b)
    ln=list()
    A=[]
    ln.append(f.readline().split())
    for t in ln[0]:
        A.append(int(t))
    A.sort()
    print('-----------------------')
    print(A[0])
    counter=0
    if(A[0]>200):
        f2.write("Case #"+str(l+1)+": " +str(counter)+'\n')
    else:
        for i in range(0, len(A)):
            for j in range(i+1, len(A)):
                for k in range(j+1, len(A)):
                    if A[i]*A[j]==A[k] or A[j]*A[k]==A[i] or A[i]*A[k]==A[j]:
                        counter=counter+1
                        print(A[i],A[j],A[k])
    print(A)
    print("Case #"+str(l+1)+": " +str(counter))
    f2.write("Case #"+str(l+1)+": " +str(counter)+'\n')
    print('---------------------------------------------------------------')
 
#f2.write(str(ln))  
f2.close()
    
