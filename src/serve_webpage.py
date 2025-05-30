from md_to_html import markdown_to_html_node
from htmlnode import HTMLNode
import os
def extract_title(md):
    lines = md.split('\n')
    for line in lines:
        stripped_line = line.strip()
        if len(stripped_line) < 3:
            continue
        if stripped_line[0] == '#' and stripped_line[1] == ' ':
            return (stripped_line[2:].strip())
    raise Exception("No H1 header found in markdown file.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        md_from_contents = f.read()
    with open(template_path) as f:
        template_contents = f.read() #this is the html string from the template
    title = extract_title(md_from_contents) #thi is the extracted title
    content = (markdown_to_html_node(md_from_contents)).to_html() # this is the content generated from md
    replaced_title_template = template_contents.replace('{{ Title }}', title)
    filled_final_template = replaced_title_template.replace('{{ Content }}', content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(filled_final_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, root_dir_path_content = None):
    print(f"Generating page from {dir_path_content} to {dest_dir_path} using {template_path}")
    if root_dir_path_content is None:
        root_dir_path_content = dir_path_content
    files = os.listdir(dir_path_content)
    for file in files:
        if os.path.isfile(os.path.join(dir_path_content, file)):
            if file.endswith('.md'):
                with open(os.path.join(dir_path_content, file), "r") as f:
                    md_from_contents = f.read()
                with open(template_path) as f:
                    template_content = f.read()
                title = extract_title(md_from_contents)
                content = (markdown_to_html_node(md_from_contents)).to_html()
                replaced_title_template = template_content.replace('{{ Title }}', title)
                filled_final_template = replaced_title_template.replace('{{ Content }}', content)
                full_input_path = os.path.join(dir_path_content, file)
                relative_path = os.path.relpath(full_input_path, start=root_dir_path_content)
                relative_html = os.path.splitext(relative_path)[0] + ".html"
                output_path = os.path.join(dest_dir_path, relative_html)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                with open(output_path, "w") as f:
                    f.write(filled_final_template)
        else:
            generate_pages_recursive(os.path.join(dir_path_content, file), template_path, dest_dir_path, root_dir_path_content)



