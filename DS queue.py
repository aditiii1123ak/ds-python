def insertQ(Q, value, priority, rear, maxsize):
    if rear == maxsize:
        print("Queue Overflow")
    elif priority < 0 or value < 0:
        print("Invalid input. Priority and value must be non-negative.")
    else:
        i = rear - 1
        while i >= 0 and Q[i][1] > priority:
            Q[i + 1] = Q[i]
            i -= 1
        Q[i + 1] = (value, priority)
        rear += 1
    return rear

def deleteQ(Q, front, rear):
    if front == rear:
        print("Queue Underflow")
    else:
        highest_priority = float('inf')
        highest_priority_index = -1
        for i in range(front, rear):
            if Q[i][1] < highest_priority:
                highest_priority = Q[i][1]
                highest_priority_index = i
        x = Q[highest_priority_index][0]
        print(f"Deleted element: {x}")
        Q[highest_priority_index] = None
        front += 1  # Update front index
    return front

def displayQ(Q, front, rear):
    if front == rear:
        print("Queue is Empty")
    else:
        for i in range(front, rear):
            if Q[i]:
                print(Q[i][0], end=" ")
        print()

maxsize = int(input("Enter the maximum size of the queue: "))
Q = [None] * maxsize
front = 0
rear = 0

while True:
    print("\nQueue Operations")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Quit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        priority = int(input("Enter the priority: "))
        value = int(input("Enter the value: "))
        rear = insertQ(Q, value, priority, rear, maxsize)
    elif choice == 2:
        front = deleteQ(Q, front, rear)
    elif choice == 3:
        displayQ(Q, front, rear)
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
