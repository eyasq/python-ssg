from textnode import TextNode, TextType
import re
# #this is for creating textnodes from raw text
# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     #it takes a list of old nodes, delimiter, adn text type, and return new nodes where potentially they are split into more nodes based on syntax.
#     new_nodes = []
#     #1 check node type
#     for node in old_nodes:
#         if node.text_type !=TextType.TEXT:
#             new_nodes.append(node)
#             continue
#         #2 split the text
#         splitted = node.text.split(delimiter)
#         #3 check delimiter validity
#         if len(splitted)%2 == 0:
#             raise Exception("Invalid Markdown Syntax!")
#         if node.text.count(delimiter)<2:
#             raise Exception("Invalid Markdown Syntax!") #to address something like doing *bold* instead of **bold**
        
#         #4 append new nodes
#         for i, segment in enumerate(splitted):
#             #even part is text, odd part is text_type
#             if i%2==0:
#                 new_nodes.append(TextNode(segment, TextType.TEXT))
#             else:
#                 new_nodes.append(TextNode(segment, text_type))

#     return new_nodes
# #my return should look like:
# # new_nodes becomes:

# # [
# #     TextNode("This is text with a ", TextType.TEXT),
# #     TextNode("code block", TextType.CODE),
# #     TextNode(" word", TextType.TEXT),
# # ]

# def split_nodes_image(old_nodes):
# #     node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT,)
# #     new_nodes = split_nodes_link([node])

# # [TextNode("This is text with a link ", TextType.TEXT),
# #     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
# #     TextNode(" and ", TextType.TEXT),
# #     TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")]
#     new_nodes = []
#     for node in old_nodes:
#         if node.text_type != TextType.TEXT:
#             new_nodes.append(node)
#             continue
#         #now handle if more than 1 image nodes:
#         #segments will look like 
#         segments = re.split(r"!\[(.*?)\]\((.*?)\)", node.text) #segments == all text nodes
#         i = 0
#         while i < len(segments):
#             if segments[i]:
#                 new_nodes.append(TextNode(segments[i], TextType.TEXT))
#             i+=1
#             if i+1 < len(segments):
#                 alt = segments[i]
#                 url = segments[i+1]
#                 new_nodes.append(TextNode(alt, TextType.IMAGE,url))
#                 i+=2
#     return new_nodes

# def split_nodes_link(old_nodes):
#     new_nodes = []
#     for node in old_nodes:
#         if node.text_type != TextType.TEXT:
#             new_nodes.append(node)
#             continue
#         segments = re.split(r"\[(.*?)\]\((.*?)\)", node.text) 
#         i = 0
#         while i < len(segments):
#             if segments[i]:
#                 new_nodes.append(TextNode(segments[i], TextType.TEXT))
#             i+=1
#             if i+1 < len(segments):
#                 alt = segments[i]
#                 url = segments[i+1]
#                 new_nodes.append(TextNode(alt, TextType.LINK,url))
#                 i+=2
#     return new_nodes


# def text_to_text_nodes(text):
#     nodes = [TextNode(text, TextType.TEXT)]
#     nodes = split_nodes_image(nodes)
#     nodes = split_nodes_link(nodes)
#     nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
#     nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
#     nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
#     return nodes
#attempt#17

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    blocks_stripped = []
    for block in blocks:
        if block == '':
            continue
        blocks_stripped.append(block.strip())
    return blocks_stripped
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
