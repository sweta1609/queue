from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

def reverseQueue(inputQueue) :
    # Your code goes here
    Stack = []
    while (not inputQueue.empty()):
        Stack.append(inputQueue.queue[0])
        inputQueue.get()
    while (len(Stack) != 0):
        inputQueue.put(Stack[-1])
        Stack.pop()
 

def takeInput():
    n = int(stdin.readline().strip())

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return qu


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    qu = takeInput()
    reverseQueue(qu)
    
    while not qu.empty() :
        print(qu.get(), end = " ")
        
    print()
    
    t -= 1
