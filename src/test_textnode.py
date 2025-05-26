import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_uneq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_url(self):
        node = TextNode("this is a text node", TextType.LINK)
        self.assertIsNone(node.url)

    def test_eq_url(self):
        node = TextNode('This is a text node', TextType.ITALIC, 'https://boot.dev')
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://boot.dev")
        self.assertEqual(node.url, node2.url)

if __name__ == "__main__":
    unittest.main()
