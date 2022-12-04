#
#
#
#
#
#
#
#
#
#   create the node class
#       define the init method containing self and data
#           set data inside of node to data
#           set next pointer to None
#           set prev pointer to None
#
#   create a deque class
#  
#       define the init method containing self and data
#           set tail of node to None
#           set head of node to None
#           create self.count accumulator
#
#       define the append method
#
#           set node equal to Node(data)
#           if there is a head of the deque
#               set previous node to the data of the head node
#               set the head of the next node to node
#               set the self.head to node
#           else:
#               set self.tail to node
#               set self.head to node
#           set self.count accumulator to add one to itself
#           print that data was added to the right
#
#       define the appendleft method
#
#           set node equal to Node(data)
#           if there is a tail of the deque
#               set previous node to the data of the tail node
#               set the tail of the next node to node
#               set the self.tail to node
#           else:
#               set self.head to node
#               set self.tail to node
#           set self.count accumulator to add one to itself
#           print that data was added to the left of the deque
# 
#       define the pop method
# 
#           set current variable to self.tail
#           set previous variable to self.tail
#           while current exists
#               if current is equal to self.tail
#                   set self.tail to current.next
#               else
#                   set prev.next to current.next
#               set self.count accumulator to subtract one from itself
#               return
#           set prev to current
#           set current to current.next
#
#       define the popleft method
# 
#           set current variable to self.head
#           set previous variable to self.head
#           while current exists
#               if current is equal to self.head
#                   set self.head to current.next
#               else
#                   set prev.next to current.next
#               set self.count accumulator to subtract one from itself
#               return
#           set prev to current
#           set current to current.next
#
#       define the peek method
#
#           if self.head does not point to any data
#               print None
#           else
#               print empty line
#               print the data at the right end of the deck
#               print empty line
#
#       define the peek method
#
#           if self.tail does not point to any data
#               print None
#           else
#               print empty line
#               print the data at the right end of the deck
#               print empty line