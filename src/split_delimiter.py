from textnode import TextNode, TextType

#this is for creating textnodes from raw text
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #it takes a list of old nodes, delimiter, adn text type, and return new nodes where potentially they are split into more nodes based on syntax.
    new_nodes = []

    for node in old_nodes:
        text = node.text
        if delimiter == '`':
            t_type = TextType.CODE
            
        elif delimiter == '**':
            t_type = TextType.BOLD #wont work for invalid md
        elif delimiter == '_':
            t_type = TextType.ITALIC
        else:
            raise Exception("invalid markdown syntax")
        delimiter_count = text.count(delimiter)
    
        if delimiter_count < 2:
            raise Exception("Invalid markdown syntax: Unclosed delimiter")

        texts = text.split(delimiter) # this is a list with the parts of the node, the delimiter splitting text string 
        # eg > ['This is text with a' , `code block`, ' word' ]
        #for each of these, we need to create textnodes
        #i am handling the existance of just 1 delimiter in a raw string of markup
        new_nodes.append(TextNode(f"{texts[0]}", node.text_type))

        new_nodes.append(TextNode(texts[1], t_type)) #might be better to make delimiter an enum of types [BOLD, ITALIC, CODE]
        new_nodes.append(TextNode(texts[2], node.text_type))

    return new_nodes


#my return should look like:
# new_nodes becomes:

# [
#     TextNode("This is text with a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" word", TextType.TEXT),
# ]