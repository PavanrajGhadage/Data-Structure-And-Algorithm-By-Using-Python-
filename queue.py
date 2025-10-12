event_queue=[]
def add_event(event):
    event_queue.append(event)
    print(f"Event '{event}' added to the queue.")
    
def process_next_event():
    if event_queue:
        event = event_queue.pop(0)  
        print(f"Processed event: '{event}'")
    else:
        print("No events to process")

def display_pending_events():
    if event_queue:
        print("pending event")
        for idx,event in enumerate(event_queue,1):
            print(f"{idx}.{event}")
    else:
            print("no pending events")
            
def cancel_event(event_name):
    if event_name in event_queue:
        event_queue.remove(event_name)
        print(f"Event '{event_name}' has been cancelled")
    else:
        print(f"Event '{event_name}' not found or in the process")
        
def menu():
    while True:
        print("MENU")
        print("1. Add Event")
        print("2. Process Next event")
        print("3. Display pending Event")
        print("4. Cancel an Event")
        print("5. Exit")
        
        choice=int(input("enter your choice"))
        if choice==1:
            event=input("enter event name:")
            add_event(event)
        elif choice==2:
            process_next_event()
        elif choice==3:
            display_pending_events()
        elif choice==4:
            event_name=input("enter event name to cancel: ")
            cancel_event(event_name)
        elif choice==5:
            print("exiting")
            break
        else:
            print("invalid choice")
            
menu() 
        

            
