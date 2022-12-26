str1= input("enter the string:")
while 1:
    choice= int(input("enter the choice:"))
    if choice==1:
        longest_str=max(str.split(str1), key=len)
        print("the longest word is:" + longest_str)
    elif choice==2:
        a= input("enter the word whose frequency is to be find:")
        print("the frequency of the word is:")
        print(str1.count(a))
    elif choice==3:
        reverse=str1[::-1]
        if reverse==str1:
            print("the string is palidrom")
        else:
            print("the string is not palidrom")
    elif choice==4:
        b=input("enter the character:")
        print("the index of character is:")
        print(str1.index(b))
    elif choice==5:
        c= input("enter the word whose occurance is tobe find:")
        print("the count is:")
        print(str1.count(c))
    else:
    print("invalid choice.")
