class QueueError(IndexError):  # Choose base class for the new exception.
    def __init__(self):        
        super().__init__("Queue error")



class Queue:
    def __init__(self):
        self.__stk = []

    def put(self, elem):
        self.__stk.insert(0,elem)

    def get(self):
        if len(self.__stk) == 0: 
            raise QueueError()
        else: 
            val = self.__stk[-1]           
            del self.__stk[-1]
            return val

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
