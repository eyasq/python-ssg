import unittest
from .serve_webpage import extract_title
class Test_md_header(unittest.TestCase):

    def test_md_title(self):
        title = 'Hello There!'
        res = '# Hello There!'
        self.assertEqual(title, extract_title(res))

    def test_md_title_2(self):
        title = 'Test Title #3'
        md = 'this is a test md file \n i am testhing this md file \n # Test Title #3'
        self.assertEqual(title, extract_title(md))
    def test_broken_md(self):
        md = 'this is markdown with no heading that should raise an exception'
        with self.assertRaises(Exception) as exc:
            extract_title(md)
        self.assertEqual(str(exc.exception), "No H1 header found in markdown file.")
    def test_md_many(self):
        md = '## this is an h2 \n ## this is also h2 \n      #this is abd h1 \n ## \n         # This is the actual title'
        self.assertEqual('This is the actual title', extract_title(md))


if __name__ == '__main__':
    unittest.main()