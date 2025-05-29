import unittest
from md_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_headings(self):
        md = """
# This is a heading

## This is a smaller heading

### Even smaller

#### Tiny heading

##### Very tiny

###### The smallest heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><h1>This is a heading</h1><h2>This is a smaller heading</h2><h3>Even smaller</h3><h4>Tiny heading</h4><h5>Very tiny</h5><h6>The smallest heading</h6></div>"
        self.assertEqual(html, expected)
    
    def test_quote(self):
        md = """
> This is a
> quote block
> with multiple lines
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><blockquote>This is a\nquote block\nwith multiple lines</blockquote></div>"
        self.assertEqual(html, expected)
    
    def test_unordered_list(self):
        md = """
- First item
- Second item with **bold**
- Third item with _italic_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><ul><li>First item</li><li>Second item with <b>bold</b></li><li>Third item with <i>italic</i></li></ul></div>"
        self.assertEqual(html, expected)
    
    def test_ordered_list(self):
        md = """
1. First numbered item
2. Second numbered item
3. Third numbered item with `code`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><ol><li>First numbered item</li><li>Second numbered item</li><li>Third numbered item with <code>code</code></li></ol></div>"
        self.assertEqual(html, expected)
    
    def test_mixed_content(self):
        md = """
# Main Heading

This is a paragraph with **bold** and _italic_ text.

## Subheading

> This is a quote

- List item 1
- List item 2

```
code block here
```

1. Ordered item 1
2. Ordered item 2
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # Just test that it doesn't crash and produces valid HTML structure
        self.assertTrue(html.startswith("<div>"))
        self.assertTrue(html.endswith("</div>"))
        self.assertIn("<h1>Main Heading</h1>", html)
        self.assertIn("<h2>Subheading</h2>", html)
        self.assertIn("<p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p>", html)
        self.assertIn("<blockquote>This is a quote</blockquote>", html)
        self.assertIn("<ul><li>List item 1</li><li>List item 2</li></ul>", html)
        self.assertIn("<pre><code>code block here\n</code></pre>", html)
        self.assertIn("<ol><li>Ordered item 1</li><li>Ordered item 2</li></ol>", html)

if __name__ == "__main__":
    unittest.main()