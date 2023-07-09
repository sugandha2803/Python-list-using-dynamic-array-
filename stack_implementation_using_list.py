#Push operation 
def Push(s,num):
    s.append(num)
    top=len(s)-1
#Checking if the list is empty or not 
def IsEmpty(s):
    if len(s)==0:
        return 1
    else:
        return 0
# Pop operation 
def Pop(s):
    if IsEmpty:
        return "Empty_list "
    else :
        s.pop()
        top=len(s)-1
    
#peek operation
def Top(s):
    if IsEmpty:
        return "Empty_list" 
    else:
        return s[top] 


#created a empty list 
s=[]
top=None
while True: 
    print("\n\nEnter choice \n 1=push\n 2=pop\n 3=show list \n 4=top element of list \n 0=exit\n")

    ch=int(input("Enter your choice :  "))
    if ch==1:
        num=int(input("enter number which you want to push in list :  "))
        Push(s,num)
    elif ch==2:
        Pop(s)
        print("Pop operation done successfully you can check your list ")
    elif ch==3:
       print(s)
    elif ch==4:
        Top(s)
    elif ch==0:
        break 
    else:
        print("Enter right choice otherwise press 0 to quit ")
    
