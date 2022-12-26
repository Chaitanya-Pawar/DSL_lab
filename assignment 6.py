def partition(array,low,high):
    pivot=array[high]
    i=low
    j=high-1

    while i<j:
        while i<high and array[i]<pivot:
            i+=1
        while j>low and array[j]>=pivot:
            j-=1
        if i<j:
            array[i], array[j]=array[j], array[i]

    if array[i]>pivot:
        array[i],array[high]=array[high], array[i]

    return i

def quick_sort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quick_sort(array,low,pi-1)
        quick_sort(array,pi+1,high)

n = int(input("enter the number of students here:"))
percentage = []
for i in range(n):
    element=float(input("enter the percentage here:"))
    if(0.0<=element<=100.0):
        percentage.append(element)
        quick_sort(percentage,0,len(percentage)-1)

print("the sorted array is:", percentage)
print("the top 5 students are:")
for i in percentage[-1:-6:-1]:
    print(i)
       


