class Stack_structure:
   def __init__(self):
      self.items = []

   def check_empty(self):
      return self.items == []

   def push_val(self, data):
      self.items.append(data)

   def pop_val(self):
      return self.items.pop()

   def print_it(self):
      for data in reversed(self.items):
         print(data)

def insert_bottom(instance, data):
   if instance.check_empty():
      instance.push_val(data)
   else:
      deleted_elem = instance.pop_val()
      insert_bottom(instance, data)
      instance.push_val(deleted_elem)

def stack_reverse(instance):
   if not instance.check_empty():
      deleted_elem = instance.pop_val()
      stack_reverse(instance)
      insert_bottom(instance, deleted_elem)

my_instance = Stack_structure()
data_list = input('Enter the elements to add to the stack: ').split()
for data in data_list:
   my_instance.push_val(int(data))

print('The reversed stack is:')
my_instance.print_it()
stack_reverse(my_instance)
print('The stack is:')
my_instance.print_it()