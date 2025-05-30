

def extract_title(md):
    lines = md.split('\n')
    for line in lines:
        stripped_line = line.strip()
        if len(stripped_line) < 3:
            continue
        if stripped_line[0] == '#' and stripped_line[1] == ' ':
            return (stripped_line[2:].strip())
    raise Exception("No H1 header found in markdown file.")