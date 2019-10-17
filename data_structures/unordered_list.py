from node import Node

"""
UnorderedList()
add(item)  -> adds an item to the list, added to front(head)
length()   -> returns length of list
remove()   -> returns current
append()   -> Adds item to end of list
index()    ->
insert()   ->

LIFO -> Last in First out   - Stack
FIFO -> First in First out -  Queue

"""

class UnorderedList:

    def __init__(self, ):
        self.head = None

    def add_item(self, new_item):   # O(3) - constant time, each statement weighted 1
        temp = Node(new_item)
        temp.set_next(self.head)
        self.head = temp

    def is_empty(self):
        return self.head == None

    def length(self):
        count = 0
        current = self.head
        while current != None:       # while loop executes n times, O(n + 3) => O(n)
            count += 1
            current = current.get_next()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if previous == None:   # you are at the first item in the List
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return current

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def index(self, item):
        index = 0
        current = self.head
        found = False

        while current != None and not found:  # make sure an item is present 
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                index += 1

        if found: 
            return index
        else:
            return None

    def add(self, item, )


##### Main program ########
my_linked = UnorderedList()
my_linked.add_item(89)
my_linked.add_item("hello")
my_linked.add_item("world")
print(my_linked.length())

print(my_linked.index(102))  # this comes back with an index, which it shouldn't
