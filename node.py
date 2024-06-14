class jsonnode:
    def __init__(self,is_leaf,is_root) -> None:
        self.is_root=is_root
        self.is_leaf=is_leaf

class node(jsonnode):
    def __init__(self,name,level,is_last,is_leaf,is_root,json_text) -> None:
        super().__init__(is_leaf,is_root)
        self.children=[]
        self.name=name
        self.level=level
        self.val=json_text
        self.is_last=is_last
        if self.is_leaf==False:
            i=0
            for key,value in json_text.items():
                if i==len(json_text)-1:
                    is_last=True
                else:
                    is_last=False
                if isinstance(value,dict):
                    is_leaf=False
                else:
                    is_leaf=True
                child=node(key,self.level+1,is_last,is_leaf,False,value)
                self.add_child(child)
                i+=1

    def add_child(self,child):
        self.children.append(child)
    
