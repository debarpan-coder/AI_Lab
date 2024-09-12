import numpy as np
class Stack:
    __size = None
    __stack_list = np.empty(shape=[0])
    __top=-1
    def __init__(self,size) -> None:
        self.__size=size
        self.__stack_list=np.empty(shape=[size])
    
    def push(self,data):
        """perform push operation on stack 
        
        Returns:
        False: if stack is full
        True: otherwise"""
        if self.__top + 1 == self.__size:
            return False
        else:
            self.__top=self.__top+1
            self.__stack_list[self.__top]=data
            return True
    def pop(self):
        """It perform the pop operation.

        Returns:
            -1: if stack is empty
            data: otherwise
        """
        if self.__top == -1:
            return -1
        else:
            self.__top=self.__top-1
            return self.__stack_list[self.__top+1]
        
    def getTop(self):
        return self.__top
    
if __name__=='__main__':
    stack = Stack(10)
    print(stack.pop())
    print(stack.push(5))
    print(stack.push(2))
    print(stack.push(7))
    print(stack.pop())
    print(stack.push(8))
    print(stack.pop())
    print(stack.push(3))
    print(stack.push(2))
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())