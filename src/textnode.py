from enum import Enum

class TextType(Enum):
    NORMAL = 'normal text'
    BOLD = 'bold text'
    ITALIC = 'italic text'
    CODE = 'code text'
    LINK = 'anchor text url'
    IMAGE = '!alt text url'

class TextNode:
    def __init__(self, text, text_type, url=None):
        if not isinstance(text_type, TextType):
            raise TypeError("text_type must be a TextType enum")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            if (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
            ):
                return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

