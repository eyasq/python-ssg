

class HTMLNode():
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