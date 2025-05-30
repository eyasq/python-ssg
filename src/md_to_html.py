from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, BlockType, text_node_to_html_node
from split_delimiter import text_to_textnodes
from md_blocks_to_nodes import markdown_to_blocks, block_to_block_type
import re

def markdown_to_html_node(markdown, basepath):
    """Convert a full markdown document into a single parent HTMLNode."""
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH:
            html_nodes.append(paragraph_to_html_node(block, basepath))
        elif block_type == BlockType.HEADING:
            html_nodes.append(heading_to_html_node(block, basepath))  
        elif block_type == BlockType.CODE:
            html_nodes.append(code_to_html_node(block, basepath))  
        elif block_type == BlockType.QUOTE:
            html_nodes.append(quote_to_html_node(block, basepath))  
        elif block_type == BlockType.ORDERED_LIST:
            html_nodes.append(ordered_list_to_html_node(block, basepath))  
        elif block_type == BlockType.UNORDERED_LIST:
            html_nodes.append(unordered_list_to_html_node(block, basepath))  
        else:
            raise Exception("Invalid Block Type!")
    
    # Return a single div containing all the block nodes
    return ParentNode("div", html_nodes)

def text_to_children(text,basepath):
    """Convert text with inline markdown to a list of HTMLNode children."""
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node, basepath)
        html_nodes.append(html_node)
    
    return html_nodes

def paragraph_to_html_node(block, basepath):
    """Convert a paragraph block to an HTMLNode."""
    # Replace newlines with spaces for paragraph text
    paragraph_text = block.replace('\n', ' ')
    children = text_to_children(paragraph_text, basepath)
    return ParentNode("p", children)

def heading_to_html_node(block, basepath):
    """Convert a heading block to an HTMLNode."""
    # Count the number of # characters
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break
    
    # Extract the heading text (everything after the # and space)
    heading_text = block[level:].strip()
    children = text_to_children(heading_text,basepath)
    
    return ParentNode(f"h{level}", children)

def code_to_html_node(block,basepath):
    """Convert a code block to an HTMLNode."""
    # Remove the opening and closing ```
    lines = block.split('\n')
    # Remove first and last lines (the ``` markers)
    code_lines = lines[1:-1]
    code_text = '\n'.join(code_lines)
    
    # Add trailing newline if there was content
    if code_text and not code_text.endswith('\n'):
        code_text += '\n'
    
    # For code blocks, we don't parse inline markdown
    code_node = LeafNode(code_text, "code")
    print("Code block raw:", repr(block))
    print("Code lines:", repr(code_lines))
    print("Final code text:", repr(code_text))

    return ParentNode("pre", [code_node])

def quote_to_html_node(block,basepath):
    """Convert a quote block to an HTMLNode."""
    # Remove the > from each line
    lines = block.split('\n')
    quote_lines = []
    
    for line in lines:
        if line.startswith('>'):
            quote_lines.append(line[1:].strip())
        else:
            quote_lines.append(line)
    
    quote_text = '\n'.join(quote_lines)
    children = text_to_children(quote_text, basepath)
    
    return ParentNode("blockquote", children)

def unordered_list_to_html_node(block,basepath):
    """Convert an unordered list block to an HTMLNode."""
    lines = block.split('\n')
    list_items = []
    
    for line in lines:
        # Remove the - and space from the beginning
        if line.startswith('- '):
            item_text = line[2:]
            children = text_to_children(item_text, basepath)
            list_items.append(ParentNode("li", children))
    
    return ParentNode("ul", list_items)

def ordered_list_to_html_node(block,basepath):
    """Convert an ordered list block to an HTMLNode."""
    lines = block.split('\n')
    list_items = []
    
    for line in lines:
        # Remove the number, period, and space from the beginning
        match = re.match(r'^\d+\.\s', line)
        if match:
            item_text = line[match.end():]
            children = text_to_children(item_text,basepath)
            list_items.append(ParentNode("li", children))
    
    return ParentNode("ol", list_items)