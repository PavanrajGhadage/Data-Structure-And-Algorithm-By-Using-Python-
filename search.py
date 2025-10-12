#list consisting of customer id
id=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
target=int(input("enter the id of the customer "))
#linear search
print("finding customer id via linear search ")
found = False
for i in range(len(id)):
    if target == id[i]:
        print("Customer id found ")
        found = True        
        break
if not found:
    print("Customer id not present")
#binary search
print("finding customer id via binary search ")
low = 0
high = len(id) - 1

while low <= high:
    mid = (low + high) // 2
    if target == id[mid]:
        print("Customer id found ")
        break
    elif target > id[mid]:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Customer id not present")
