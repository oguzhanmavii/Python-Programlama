
# Python program to
# demonstrate stack implementation
# using list
 
#algoritma stacks yapısında şu şekilde işlemektedir
#eleman eklendikçe liste büyür
#fakat son olarak listeye eklenen eleman silme işlemi yapılacağı zaman listeden ayrılır
#ilk giren elemanda bütün elemanlar silindikten sonra en son olarak listeden silinir 
stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('İlk yığın Oluşturuluyor')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nYığından çıkan öğeler:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nÖğeler atıldıktan sonra yığın:')
print(stack)
 
# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty


# Python program to
# demonstrate stack implementation
# using queue module
 
from queue import LifoQueue
 
# Initializing a stack
stack = LifoQueue(maxsize=3)
 
# qsize() show the number of elements
# in the stack
print(stack.qsize())
 
# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')
 
print("Full: ", stack.full())
print("Size: ", stack.qsize())
 
# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
 
print("\nEmpty: ", stack.empty())