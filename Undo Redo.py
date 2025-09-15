# Implementing a real-time undo/redo system for a text editing application using a Stack data structure. The system should support the following operations:
# • Make a Change: A new change to the document is made.
# • Undo Action: Revert the most recent change and store it for potential redo.
# • Redo Action: Reapply the most recently undone action.
# • Display Document State: Show the current state of the document after undoing or redoing an action

undo_stack = []
redo_stack = []

def make_change():
    text=input("Enter a Text:\n")
    undo_stack.append(text)
    redo_stack.clear()
    print(text) 

def undo():
    if undo_stack:
        a=undo_stack.pop()
    else:
        print("Nothing to undo\n")
        return
    redo_stack.append(a)

def redo():
    if redo_stack:
        a=redo.pop()
    else:
        print("Nothing to redo\n")
        return
    undo_stack.append(a)

def display():
    for i in undo_stack:
        print(i,end="")

while True:
    print("\n\n1.Enter Text")
    print("2.Undo")
    print("3.Redo")
    print("4.Current State")
    print("5.Exit")

    choice=int(input("Enter Your Choice"))
    print()
    if choice==1:
        make_change()
        print()
    elif choice==2:
        undo()
        print()
    elif choice==3:
        redo()
        print()
    elif choice==4:
        display()
        print()   
    elif choice==5:
        break    
