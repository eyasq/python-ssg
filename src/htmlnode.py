
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        props=[]
        for key, value in self.props.items():
            props.append(f'{key}="{value}"')
        return ' '.join(props)

    def __repr__(self):
        return f"HTMLNode tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props}"
    
    def __eq__(self,other):
        if not isinstance(other, HTMLNode):
            return False
        return(
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )
    

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag = tag, value = value, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None and self.props is None:
            return f"{self.value}"
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        props = self.props_to_html()
        return f'<{self.tag} {props}>{self.value}</{self.tag}>'



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__( tag = tag, children = children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag cannot be empty for a parent node.")
        if self.children is None:
            raise ValueError("Child nodes must have values")
        for child in self.children:
            if child.value is None and not isinstance(child, ParentNode):
                raise ValueError("Child nodes must have values")
        ret_str = ''
        for child in self.children:
            ret_str+=''+child.to_html()
        return f"<{self.tag}>{ret_str}</{self.tag}>"


