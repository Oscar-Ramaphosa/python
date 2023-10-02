
'''Create a class for Error attempting to access
   an element from an empty container'''
class Empty(Exception):
    pass

'''Create a class called ArrayStack'''
class ArrayStack:
    '''Create a stacks function that has two arguments'''
    def stacks(self,S,T):
        return

    '''A function that displays the top stack element'''
    def top(self):
        if self.is_empty():
            raise Empty('Empty stack')
        return self.data[-1]

    '''this function is Creating an empty stack.'''
    def __init__(self):
        self.data = []

    '''This function returns true if the stack is empty'''
    def is_empty(self):
        return len(self.data) == 0

    '''The function that provide the number of element in a stack'''
    def len(self):
        return len(self.data)

    '''a function that adds element'''
    def push(self,A):
        self.data.append(A)

    '''a function that removes element'''
    def pop(self):
        if self.is_empty():
            raise Empty('Empty stack')
        return self.data.pop()

'''the main function'''
if __name__ == '__main__':
     # create the two stacks
     S = ArrayStack()
     T = ArrayStack()

     '''push values into the S stack and printing the output'''
     S.push(10)
     S.push(25)
     S.push(15)
     S.push(7)
     print('Stack S : ', S.data)
     print('Length of stack S before the transfer: ', len(S.data))
     print('Stack T :', T.data)
     print('Length of stack T before the transfer:', len(T.data))
     print('The item at the top of stack S:', S.top())

     '''reversing elements from the S stack to the T stack and printing the output'''
     T.push(S.pop())
     T.push(S.pop())
     T.push(S.pop())
     T.push(S.pop())
     print('The item at the top of stack T:', T.top())
     print("The transfer was done successfully")
     print ("Length of stack S after the transfare: ", len(S.data))
     print("Length of stack T after the transfer: ", len(T.data))
     print("Stack T after transfer : ", T.data)
     print("Stack S after Transfer", S.data)

