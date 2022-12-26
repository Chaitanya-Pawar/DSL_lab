grpA=['A','B','C','D','E'] #cricket
grpB=['F','A','R','V','B'] #badminton
grpC=['A','D','V','M','N'] #football
r1=[]
r2=[]
a=[]
r3=[]
b=[]
r4=[]
def fun1():
 for i in grpA:
  for j in grpB:
   if(i==j):
    r1.append(i)
 print("list of students who plays both Cricket and badminton\n",r1)
fun1()
def fun2():
 for i in grpA:
  f=0
 for j in grpB:
  if(i==j):
   f=1
 if (f==0):
  r2.append(i)
 for j in grpB:
  f=0
 for i in grpA:
  if(i==j):
   f=1
 if(f==0):
  r2.append(j)
 print("Students who play either cricket or baddmintn but not both\n",r2)
fun2() #calling of function
def fun3():
 a=grpA+grpB
 for i in grpC:
  f=0
 for j in a:
  if(i==j):
   f=1
 if(f==0):
  r3.append(i)
 print("List of students who play neither cricket nor badminton\n",r3)
 print("Number of students who play neither cricket nor badminton : ",len(r3))
fun3() #calling of function
def fun4():
 for i in grpA:
  for k in grpC:
   if(i==k):
    b.append(i)
 for i in b:
  c=0
 for j in grpB:
  if(i==j):
   c=c+1
 if(c==0):
  r4.append(i)
 print("List of students who play cricket and football but not badminton\n",r4)
 print("Number of students who play cricket and football is : ",len(r4))
fun4() #calling of function
