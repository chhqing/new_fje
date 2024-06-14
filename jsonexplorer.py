from icon import icon_family,icon
import treestyle
import rectanglestyle
from render import TreeRenderStrategy,RectangleRenderStrategy
class jsonexplorer:
    def __init__(self) -> None:
        self.icon_family=icon_family()
        self.style_family={'tree':treestyle.TreeFactory(),'rectangle':rectanglestyle.RectangleFactory()}
        self.Strategy_family={'tree':TreeRenderStrategy(),'rectangle':RectangleRenderStrategy()}

    def builder(self,iconname,stylename,rootnode):
        _icon=self.icon_family.get_icon(iconname)
        _jsonnode=self.style_family[stylename].create(rootnode)
        return _icon,_jsonnode
    
    def explorer(self,icon,jsonnode,stylename):
        line_list=self.Strategy_family[stylename].render(jsonnode,icon)
        for line in line_list:
            print(line)
    
    def add_style(self,stylename,newfacory):
        self.style_family[stylename]=newfacory