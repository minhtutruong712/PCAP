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


class SuperQueue(Queue):
    def __init__(self):
        super().__init__()
    
    def put(self, elem):
        Queue.put(self, elem)
        return elem

    def get(self):
        return Queue.get(self)
            
        
    
    def isempty(self): 
        if len(self._Queue__stk) == 0: 
            return True
        else:
            return False



que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
