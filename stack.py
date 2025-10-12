undo_stack=[]
redo_stack=[]
def make_change():
    
    text=input("Enter a string: ")
    undo_stack.append(text)
    redo_stack.clear()

def undo():
    
    
    if undo_stack:
        x=undo_stack.pop()
    else:
        print("Nothing to Undo\n")
        return
    redo_stack.append(x)

def redo():
    if redo_stack:
        x=redo_stack.pop()
    else:
        print("Nothing to Redo\n")
        return    
    undo_stack.append(x)

def display():
    for i in undo_stack:
        print(i,end=" ")  
        

while True:
    print("\n \n1.Enter Text")
    print("2.Undo")
    print("3.Redo") 
    print("4.Current State")
    print("5.Exit")
    
    choice=int(input("Enter your choice: "))
    print()
    if choice==1:
        make_change()
        print()
        display()
    elif choice==2:
        undo()
        print()
        display()
    elif choice==3:
        redo()
        print()
        display()
    elif choice==4:
        display()
        
    elif choice==5:
        break

    else:
        print("Invalid Input")