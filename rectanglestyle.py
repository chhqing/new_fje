from node import node
from jsonstylefactory import AbstractjsonFactory

class RectangleFactory(AbstractjsonFactory):
    def create(self,rootnode):
        return node(None,0,False,False,True,rootnode)

