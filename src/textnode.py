from enum import Enum
from htmlnode import LeafNode
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None, alt=None):
        if not isinstance(text_type, TextType):
            raise TypeError("text_type must be a TextType enum")
        self.text = text
        self.text_type = text_type
        self.url = url
        self.alt = alt

    def __eq__(self, other):
        if isinstance(other, TextNode):
            if (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url and
                self.alt==other.alt
            ):
                return True
        return False

    def __repr__(self):
        if self.url is None:
            return f"TextNode('{self.text}', {self.text_type})"
        return f"TextNode('{self.text}', {self.text_type}, {self.url})"


def text_node_to_html_node(textnode):
    if not isinstance(textnode, TextNode):
        raise Exception("Not a valid textnode.")
    if textnode.text_type == TextType.TEXT:
        return LeafNode(value=textnode.text)
    elif textnode.text_type == TextType.BOLD:
        return LeafNode(value=textnode.text, tag='b')
    elif textnode.text_type == TextType.ITALIC:
        return LeafNode(value=textnode.text, tag='i')
    elif textnode.text_type == TextType.CODE:
        return LeafNode(value=textnode.text, tag='`')
    elif textnode.text_type == TextType.LINK:
        return LeafNode(value=textnode.text, tag='a', props={"href": f"{textnode.url}"})
    elif textnode.text_type == TextType.IMAGE:
        return LeafNode(value='', tag='img', props={"src": f"{textnode.url}", "alt":f"{textnode.alt}"})
    