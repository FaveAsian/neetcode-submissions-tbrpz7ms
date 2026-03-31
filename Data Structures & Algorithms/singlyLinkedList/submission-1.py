class Node:
    def __init__(self, data=None, node=None):
        self.data = data
        self.node = node
class LinkedList:
    
    def __init__(self):
        self.head = Node()
    
    def get(self, index: int) -> int:        
        i = 0
        self.temp_list = self.head.node
        while self.temp_list:
            if index == i:
                return self.temp_list.data
            self.temp_list = self.temp_list.node
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        temp_node = Node(data=val, node=self.head)
        temp_node.node = self.head.node
        self.head.node = temp_node

    def insertTail(self, val: int) -> None:
        temp_list = self.head
        while temp_list:
            if temp_list.node is None:
                temp_list.node = Node(data=val)
                return
            else:
                temp_list = temp_list.node

    def remove(self, index: int) -> bool:
        i = 0
        temp_list = self.head
        while temp_list:
            # Need to grab the before
            if index == i:
                if temp_list.node:
                    prev = temp_list
                    new_next = temp_list.node.node
                    prev.node = new_next
                    return True
                else:
                    return False
            temp_list = temp_list.node
            i += 1

        return False

    def getValues(self) -> List[int]:
        res = []
        temp_list = self.head.node
        while temp_list:
            res.append(temp_list.data)
            temp_list = temp_list.node
        
        return res
        
