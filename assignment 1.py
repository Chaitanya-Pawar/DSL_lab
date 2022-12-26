def intersection(l1,l2):
    result = []

    for student in l1:
        if student in l2:
            result.append(student)

    return result

def union(l1,l2):
    result = l2.copy()

    for student in l1:
        if not student in l2:
            result.append(student)

    return result

def diff(l1,l2):
    result=[]

    for student in l1:
        if not student in l2:
            result.append(student)

    return result

a = [1,2,3,4,5,6,7]
b = [2,3,6,7,9,10]
c = [2,4,6,8,10,12]

print("A=",a)
print("B=",b)
print("C=",c)

print("1.ans:")
print(intersection(a,b))

print("2.ans:")
print(diff(union(a,b),intersection(a,b)))

print("3.ans:")
print(diff(c,union(a,b)))

print("4.ans:")
print(diff(intersection(a,c),b))

