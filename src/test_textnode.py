import unittest

from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")

        self.assertEqual(node, node2)

    def test_text_node_to_html_node_text(self):
        node = TextNode("im text")
        converted_text_node = text_node_to_html_node(node)
        test_str = f"im text"

        self.assertEqual(converted_text_node.to_html(), test_str)

    def test_text_node_to_html_node_bold(self):
        node = TextNode("im bold", "bold")
        converted_text_node = text_node_to_html_node(node)
        test_str = f"<b>im bold</b>"

        self.assertEqual(converted_text_node.to_html(), test_str)

    def test_text_node_to_html_node_italic(self):
        node = TextNode("im italic", "italic")
        converted_text_node = text_node_to_html_node(node)
        test_str = f"<i>im italic</i>"

        self.assertEqual(converted_text_node.to_html(), test_str)

    def test_text_node_to_html_node_code(self):
        node = TextNode("im code", "code")
        converted_text_node = text_node_to_html_node(node)
        test_str = f"<code>im code</code>"

        self.assertEqual(converted_text_node.to_html(), test_str)

    def test_text_node_to_html_node_link(self):
        node = TextNode("destinio", "link", "https://destin.io")
        converted_text_node = text_node_to_html_node(node)
        test_str = f'<a href="https://destin.io">destinio</a>'

        self.assertEqual(converted_text_node.to_html(), test_str)

    def test_text_node_to_html_node_image(self):
        node = TextNode("destinio", "image", "https://destin.io")
        converted_text_node = text_node_to_html_node(node)
        test_str = f'<img src="https://destin.io" alt="destinio">destinio</img>'

        self.assertEqual(converted_text_node.to_html(), test_str)


if __name__ == "__main__":
    unittest.main()
