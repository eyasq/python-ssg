from textnode import TextNode, TextType

print('hello world')

def main():
    txtnode = TextNode('This is some anchor text', TextType.LINKS, 'https://boot.dev')
    print(txtnode)

main()

