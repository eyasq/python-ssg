import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class Test_split_delimiter(unittest.TestCase):
    def test_splitter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT) ]
        self.assertEqual(split_nodes_delimiter([node], '`', TextType.CODE), new_nodes)
    
    def test_splitter_bold(self):
        node = TextNode("This is text with a **bold text** and normal text", TextType.TEXT)
        new_nodes = [TextNode('This is text with a ', TextType.TEXT), TextNode('bold text', TextType.BOLD), TextNode(' and normal text', TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], '**', TextType.BOLD), new_nodes)

    def test_splitter_italic(self):
        node = TextNode("This is text a _italic text_ and normal text", TextType.TEXT)
        new_nodes = [TextNode('This is text a ', TextType.TEXT), TextNode('italic text', TextType.ITALIC), TextNode(' and normal text', TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], '_', TextType.ITALIC), new_nodes)
    
    def test_invalid_md(self):
        node = TextNode("This is text with an invalid _md syntax", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], '_', TextType.ITALIC)
    
    def test_multiple_delimiters(self):
        node = TextNode("This is `code` and `more` code", TextType.TEXT)
        result = split_nodes_delimiter([node], '`', TextType.CODE)
        expected = [
            TextNode('This is ', TextType.TEXT),
            TextNode('code', TextType.CODE),
            TextNode(' and ', TextType.TEXT),
            TextNode('more', TextType.CODE),
            TextNode(' code', TextType.TEXT)
        ]
        assert result == expected

if __name__ == '__main__':
    unittest.main()