from htmlnode import HTMLNode
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

if __name__=='__main__':
    unittest.main()