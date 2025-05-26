import unittest
from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode


class TestTextNodeToHTML(unittest.TestCase):
    def test_textnode_to_html(self):
        textnode = TextNode('i am a text node', TextType.TEXT)
        htmlnode = text_node_to_html_node(textnode)
        leafnode = LeafNode(value=textnode.text)
        self.assertEqual(leafnode.value, htmlnode.value)
    def test_bold_to_html(self):
        textnode = TextNode('i am a bold boi', TextType.BOLD)
        htmlnode = text_node_to_html_node(textnode)
        self.assertEqual(htmlnode, LeafNode(value=textnode.text, tag='b'))
    
    def test_italic_to_html(self):
        textnode = TextNode('i am italic boi', TextType.ITALIC)
        self.assertEqual(text_node_to_html_node(textnode), LeafNode(value=textnode.text, tag='i'))
    
    def test_url_to_html(self):
        textnode = TextNode('i am linky boi', TextType.LINK, url='https://boot.dev')
        self.assertEqual(text_node_to_html_node(textnode), LeafNode(value=textnode.text, tag='a', props={'href':f"{textnode.url}"}))

    def test_image_to_html(self):
        textnode = TextNode('', TextType.IMAGE, url='https://www.boot.dev/_nuxt/new_boots_profile.DriFHGho.webp', alt='boots pic')
        leafnode = LeafNode(value='', tag='img', props={"src":f"{textnode.url}", "alt":f"{textnode.alt}"})
        htmldnode = text_node_to_html_node(textnode)
        self.assertEqual(htmldnode, leafnode)
if __name__ == '__main__':
    unittest.main()