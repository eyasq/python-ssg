from htmlnode import HTMLNode, LeafNode
import unittest

class testHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('p', 'blabla','hr')
        node2 = HTMLNode('p', 'blabla','hr')
        self.assertEqual(node, node2)
        
    def test_is_HTMLNode(self):
        node = HTMLNode()
        self.assertIsInstance(node, HTMLNode)
    
    def test_is_None(self):
        node = HTMLNode()
        self.assertIsNone(node.children)


    def test_to_html_prop(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')

    def test_to_html(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertEqual(node.to_html(),"<p>This is a paragraph of text.</p>")

    def test_leaf_node(self):
        node = LeafNode(value='This is a text lolol')
        self.assertEqual(node.to_html(), "This is a text lolol")

if __name__=='__main__':
    unittest.main()