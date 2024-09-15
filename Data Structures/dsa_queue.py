class CircularQueue:

    def __init__(self,size) -> None:
        self.__size = size
        self.__queue = [None] * (self.__size)
        self.__rear=self.__front=-1
    
    def isFull(self):
        """Checks for the queue is full or not

        Returns:
            bool: True if empty othewise False
        """
        return (self.__rear+1)%self.__size==self.__front
    
    def isEmpty(self):
        """Checks for the queue is empty or not

        Returns:
            bool: True if empty othewise False
        """
        return self.__front==-1
        
    def enqueue(self,data):
        """Add an element at the position pointed by the Rear

        Args:
            data (any): data can be of any type

        Returns:
            bool: True for successful insertion otherwise False
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.__front=self.__rear=0
        else:
            self.__rear=(self.__rear+1)%self.__size
        self.__queue[self.__rear]=data
        return True
        
    def dequeue(self):
        """Remove an element at the position pointed by the Front

        Returns:
            any: data if queue is not empty otherwise -1
        """
        if self.isEmpty():
            return -1
        item = self.__queue[self.__front]
        if self.__front==self.__rear:
            self.__front=self.__rear=-1
        else:
            self.__front=(self.__front+1)%self.__size
        return item
    
    def peek(self):
        """Retrive the element at the position pointed by Front

        Returns:
            any: data if queue is not empty otherwise -1
        """
        if self.isEmpty():
            return -1
        return self.__queue[self.__front]
    
    def getFront(self):
        """Get the Front(F) index position

        Returns:
            int: index is always a integer
        """
        return self.__front
    
    def getRear(self):
        """Get the Rear(R) index position

        Returns:
            int: index is always a integer
        """
        return self.__rear
    
if __name__=='__main__':
    queue=CircularQueue(4)
    print(queue.enqueue(2),2,f"F={queue.getFront()}, R={queue.getRear()}")
    print(queue.enqueue(8),8,f"F={queue.getFront()}, R={queue.getRear()}")
    print(queue.enqueue(7),7,f"F={queue.getFront()}, R={queue.getRear()}")
    print(queue.dequeue(),f"F={queue.getFront()}, R={queue.getRear()}")
    print(queue.enqueue(11),11,f"F={queue.getFront()}, R={queue.getRear()}")
    print(queue.enqueue(5),5,f"F={queue.getFront()}, R={queue.getRear()}")
    print(queue.enqueue(3),3,f"F={queue.getFront()}, R={queue.getRear()}")
    print(queue.dequeue(),f"F={queue.getFront()}, R={queue.getRear()}")
    print(queue.dequeue(),f"F={queue.getFront()}, R={queue.getRear()}")
    print(queue.dequeue(),f"F={queue.getFront()}, R={queue.getRear()}")
    print(queue.dequeue(),f"F={queue.getFront()}, R={queue.getRear()}")
    print(queue.dequeue(),f"F={queue.getFront()}, R={queue.getRear()}")