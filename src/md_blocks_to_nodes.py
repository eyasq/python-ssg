from textnode import BlockType
import re
def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    blocks_stripped = []
    for block in blocks:
        if block == '':
            continue
        blocks_stripped.append(block.strip())
    return blocks_stripped

def block_to_block_type(block):
    if block.startswith('#'):
        match = re.match(r"^(#{1,6})\s", block)
        if match:
            return BlockType.HEADING
        return BlockType.PARAGRAPH
    elif block.startswith('```') and block.count('```')>=2:
        return BlockType.CODE
    elif block.startswith('>'):
        return BlockType.QUOTE
    elif block.startswith('-'):
        if block[1] == ' ':
            return BlockType.UNORDERED_LIST
        return BlockType.PARAGRAPH
    
    elif re.match(r"^\d+\.\s", block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
        