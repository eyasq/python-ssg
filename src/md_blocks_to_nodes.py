def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    blocks_stripped = []
    for block in blocks:
        if block == '':
            continue
        blocks_stripped.append(block.strip())
    return blocks_stripped