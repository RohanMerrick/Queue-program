queue = [5, 27, 54, 64, 99, 73]
fPointer = 0
rPointer = 5
carryOn = True
element = 0


def enqueue(rear,item,element,front):
    if rear == 5 and "." in queue:
        added = False
        while added == False:
            if queue[element] == ".":
                queue[element] = item
                rear = element
                element = 0
                added = True
                return rear
            else:
                element += 1
    elif front-rear == 1 or rear-front == 1 or rear == 5:
        print("Error: queue is full...")
        return rear
    else:
        rear += 1
        queue[rear] = item
        return rear

def dequeue(front, rear):
    if front > 5:
        front = 0
    if rear < 0:
        print("Error: queue is empty...") 
        return front, 0 
    else:
        dequeuedItem = queue[front]
        queue[front] = "."
        front += 1
        return front, dequeuedItem

#main program -------------------------------------------------------------------------------------------------
while carryOn == True:
    print(*queue)
    print("\nEnter:\nEnqueue if you want to add an item to the queue\nDequeue if you want to remove the item from the front of the queue\nEnd if you want to end the program")
    choice = input("\nEnter your decision: ").title()
    if choice == "Dequeue":
        fPointer, dequeuedItem = dequeue(fPointer, rPointer)
    elif choice == "Enqueue":
        item = int(input("Enter item you want to enqueue: "))
        rPointer = enqueue(rPointer,item,element,fPointer)
    elif choice == "End":
        carryOn = False
        print("\nHave a good day")
    print("-------------------------------------------------------------------------")


    print("Bye")