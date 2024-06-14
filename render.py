from abc import ABC,abstractmethod
class RenderStrategy(ABC):
    @abstractmethod
    def render(self,node,icon):
        pass

    @abstractmethod
    def leaf_render(self,node,icon):
        pass

    @abstractmethod
    def node_render(self,node,icon):
        pass

class TreeRenderStrategy(RenderStrategy):
    def render(self,node,icon):
        if node.is_leaf:
            return self.leaf_render(node,icon)
        else:
            return self.node_render(node,icon)

    def leaf_render(self,node,icon):
        line=''
        if node.is_last:
            line='└─'
        else:
            line='├─'
        line+=icon.leaficon+node.name
        if node.val!=None:
            line+=': '+node.val
        return [line]
    
    def node_render(self,node,icon):
        line_list=[]
        if node.is_root==False:
            line=''
            if node.is_last:
                line='└─'
            else:
                line='├─'
            line+=icon.nodeicon+node.name
            line_list.append(line)
        for child in node.children:
            child_line=TreeRenderStrategy().render(child,icon)
            for i in child_line:
                if node.level==0:
                    line_list.append(i)
                elif node.is_last:
                    line_list.append('   '+i)
                else:
                    line_list.append('│  '+i)
        return line_list
    
class RectangleRenderStrategy(RenderStrategy):
    def render(self,node,icon):
        if node.is_leaf:
            line_list=self.leaf_render(node,icon)
        else:
            line_list=self.node_render(node,icon)
        if node.is_root:
            line_start=list(line_list[0])
            line_start[0]='┌'
            line_start[len(line_start)-1]='┐'
            line_list[0]=''.join(line_start)
            end=len(line_list)-1
            line_end=list(line_list[end])
            for i in range(len(line_end)):
                if line_end[i]=='│':
                    if i==0:
                        line_end[i]='└'  
                    else:
                        line_end[i]='┴'
                elif line_end[i]==' ':
                    line_end[i]='─'
                elif line_end[i]=='├':
                    line_end[i]='┴'
                    break
            line_end[len(line_end)-1]='┘'
            line_list[end]=''.join(line_end)
        return line_list

    def leaf_render(self,node,icon):
        line='├─'
        line+=icon.leaficon+node.name
        if node.val!=None:
            line+=': '+node.val
        line+=' '
        for i in range(43-len(line)-2-(node.level-1)*3):
            line+='─'
        line+='─┤'
        return [line]
    
    def node_render(self,node,icon):
        line_list=[]
        if node.is_root==False:
            line='├─'
            line+=icon.nodeicon+node.name+' '
            for i in range(43-len(line)-2-(node.level-1)*3):
                line+='─'
            line+='─┤'
            line_list.append(line)
        for child in node.children:
            child_line=RectangleRenderStrategy().render(child,icon)
            for i in child_line:
                if node.level==0:
                    line_list.append(i)
                else:
                    line_list.append('│  '+i)
        return line_list