#function for selection sort
def Selection_sort(a):
    
#find the minimum element in remaining unsorted array   
    
    for i in range(len(a)):
        min_index=i
        for j in range(i+1, len(a)):
            if a[min_index]>a[j]:
                min_index = j
#swap the minimum element with the first element                
            a[i], a[min_index] = a[min_index], a[i]

    print("Marks of students after performing selection sort on the list:")
    for i in range(len(a)):
         print(a[i])
#-----------------------------------------------------
#function for bubble sort
def Bubble_sort(a):
    n = len(a)
    #traverse through all array elements
    for j in range(n):
        for i in range(n-1):
         if a[i]>a[i+1]:
           a[i],a[i+1] = a[i+1],a[i]

    print("marks of students after performing bubble sort on the list:")
    for i in range(len(a)):
        print(a[i])

#--------------------------------------------->
#function to display top five marks

def top_five_marks(a):
    for i in a:
        highest=max(a)
        last=a[-1]
        m=(sorted(a,reverse=True))
        print(m[0:5])
        break
#------------------------------------------------------------>    

#main:
a=[]
n=int(input("enter number of students whose marks are tobe displayed:"))
print("enter marks for", n, "students(press ENTER after every student marks)")
for i in range(0,n):
    ele=int(input())
    a.append(ele)  #adding the element

print("The marks of", n ,"students are : ")
print(a)

print("MENU")
print("1.Selection sort 2.Bubble sort 3.Exit")
while 1:
    s=int(input("Choose your option:"))
    if s==1:
        print("selection sort:")
        Selection_sort(a)
        print("Top five marks")
        top_five_marks(a)

    elif s==2:
         print("bubble sort:")
         Bubble_sort(a)
         print("Top five marks")
         top_five_marks(a)

    elif s==3:
        print("Exit")
        break
    
    else:
        print("Invalid Option!")

            
