from textnode import TextNode, TextType

#this is for creating textnodes from raw text
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #it takes a list of old nodes, delimiter, adn text type, and return new nodes where potentially they are split into more nodes based on syntax.
    new_nodes = []
    #1 check node type
    for node in old_nodes:
        if node.text_type !=TextType.TEXT:
            new_nodes.append(node)
            continue
        #2 split the text
        splitted = node.text.split(delimiter)
        #3 check delimiter validity
        if len(splitted)%2 == 0:
            raise Exception("Invalid Markdown Syntax!")
        if node.text.count(delimiter)<2:
            raise Exception("Invalid Markdown Syntax!") #to address something like doing *bold* instead of **bold**
        
        #4 append new nodes
        for i, segment in enumerate(splitted):
            #even part is text, odd part is text_type
            if i%2==0:
                new_nodes.append(TextNode(segment, TextType.TEXT))
            else:
                new_nodes.append(TextNode(segment, text_type))

    return new_nodes


#my return should look like:
# new_nodes becomes:

# [
#     TextNode("This is text with a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" word", TextType.TEXT),
# ]