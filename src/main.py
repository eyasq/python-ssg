from textnode import TextNode, TextType
import os
import shutil
print('hello world')

def main():
    txtnode = TextNode('This is some anchor text', TextType.LINK, 'https://boot.dev')
    print(txtnode)
    recursive_copy('/home/eyas/workspace/projects/ssg/python-ssg/static','/home/eyas/workspace/projects/ssg/python-ssg/public' )
# def recursive_copy(src, dst):
#     #path = '/home/eyas/workspace/projects/ssg/python-ssg/public'
#     if os.path.exists(dst):
#         shutil.rmtree(dst)
#     #now i must add a check - if public doesnt exist, create it, so i can copy files to it
#     if not os.path.exists(dst):
#         os.mkdir(dst)
#     if os.path.exists(src):
#         files_or_folders = os.listdir(src)
#         for item in files_or_folders:
#             item_path = os.path.join(src, item)
#             dst_path = os.path.join(dst, item)
#             if os.path.isfile(item_path):
#                 shutil.copy(item_path, dst_path)
#             else:
#                 recursive_copy(item_path, dst_path)

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


main()



