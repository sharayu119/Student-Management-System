student={1:{"name":"sharayu","percentage":80,"course":"python"}}



def dashboard():
    print("""
        1.add student data
        2.display student data
        3.update student data
        4.delete student data
        5.filter
    """)
dashboard()    

def add(roll,name,per,course):
    student[roll]={"name":name,"percentage":per,"course":course}
    
    return "added successfully..."


def display():
    print("_"*85)

    print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("roll","name","percentage","course"))
    print("_"*85)
    for i in student:
        # print("_"*85)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(i, student[i]["name"],student[i]["percentage"],student[i]["course"]))
        print("_"*85)


def update(roll):
    print("""
        1.name
        2.percentage
        3.course
    """)
    ch=int(input("enter your choice:"))
    if ch==1:
        student[roll]["name"]=input("enetr name:")
        return "update name successfully"
    elif ch==2:
        student[roll]["per"]=eval(input("enter per:"))
        return "update per successfully"
    elif ch==3:
        student[roll]["course"]=input("enter course:")
        return "update course successfully"
    else:
        return "invalid input"

def delete(roll):
    del student[roll]
    return "data deleted successfully"

while True:
    dashboard()
    ch=int(input("enter your choice:"))
    if ch==1:
        r=int(input("enter roll number:"))
        n=input("enter name:")
        p=eval(input("enter percentage:"))
        c=input("enter course:")
        print(add(r,n,p,c))
    elif ch==2:
        display()
    elif ch==3:
        r=int(input("enter roll:"))
        print(update(r))
    elif ch==4:
        #print(delete(1))   
        r=int(input("enter roll:"))
        
        print(delete(r))