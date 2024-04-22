import unittest

from textnode import TextNode, split_nodes_delimiter, text_type_text, text_type_code


class TestTextNode(unittest.TestCase):
    def test_length_of_nodes(self):
        node = TextNode("This text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)

        self.assertEqual(len(new_nodes), 3)

    def test_nodes_eq(self):
        node = TextNode("This text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)

        self.assertListEqual(
            new_nodes,
            [
                TextNode("This text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
        )
