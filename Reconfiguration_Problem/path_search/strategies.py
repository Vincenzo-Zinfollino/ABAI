import random

class RandomStrategy:
    def select(self, fringe):
        random.shuffle(fringe)
        selected_node = fringe.pop(0)
        return fringe, selected_node
    
class BredthFrst:
    def select(self,fringe):
        fringe.sort(key= lambda node:node.depth)
        selected_node=fringe.pop(0)
        return fringe, selected_node