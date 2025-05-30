from textnode import TextNode, TextType
from serve_webpage import generate_page, generate_pages_recursive
import os
import shutil
import sys

basepath = sys.argv[1] if len(sys.argv) > 1 else '/'

def main():
    txtnode = TextNode('This is some anchor text', TextType.LINK, 'https://boot.dev')
    print(txtnode)
    recursive_copy('/home/eyas/workspace/projects/ssg/python-ssg/static','/home/eyas/workspace/projects/ssg/python-ssg/docs' )
    generate_pages_recursive('content/','template.html','docs/', basepath)

def copy_folder_structure(src, dst):
    files_to_copy = os.listdir(src)
    for file in files_to_copy:
        if os.path.isfile(os.path.join(src, file)):
            print("Source path for file, and file name:", os.path.join(src, file), file)
            print("Destination path for file, and file name:", os.path.join(dst, file), file)
            shutil.copy(os.path.join(src,file), os.path.join(dst, file))
        else:
            os.mkdir(os.path.join(dst, file))
            copy_folder_structure(os.path.join(src, file), os.path.join(dst, file))

def recursive_copy(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    copy_folder_structure(src, dst)

if __name__ == "__main__":
    main()