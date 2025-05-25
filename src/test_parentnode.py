import unittest
from htmlnode import ParentNode, LeafNode, HTMLNode

class test_parent_node(unittest.TestCase):
    def test_child_node(self):
        cnode = LeafNode(tag="span", value="child")
        pnode = ParentNode(tag="div", children=[cnode])
        self.assertEqual(pnode.to_html(), "<div><span>child</span></div>")

    def test_parent_nodes(self):
        lnode = LeafNode(tag="b", value="boldboy")
        lnode2 = LeafNode(tag="i", value="Italicboi")
        pnode = ParentNode(tag="div", children=[lnode, lnode2])
        lnode3 = LeafNode(tag="em", value="stronk")
        pnode2 = ParentNode(tag="aside", children=[pnode, lnode3])
        self.assertEqual(pnode2.to_html(), "<aside><div><b>boldboy</b><i>Italicboi</i></div><em>stronk</em></aside>")

    def test_empty_leaf(self):
        lnode = LeafNode(value='kar', tag='br')
        pnode = ParentNode(tag='div', children=[lnode])
        self.assertEqual(pnode.to_html(), '<div><br>kar</br></div>')

if __name__ == '__main__':
    unittest.main()