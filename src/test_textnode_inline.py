import unittest

from textnode import (
    TextNode,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    text_type_text,
    text_type_code,
)


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

    def test_extract_images(self):
        found = extract_markdown_images("Some text and a ![image](https://destin.io)")
        self.assertListEqual([("image", "https://destin.io")], found)

    def test_extract_link(self):
        found = extract_markdown_links(
            "This is a link [link](https://destin.io) and [another](https://boot.dev)"
        )

        self.assertListEqual(
            found, [("link", "https://destin.io"), ("another", "https://boot.dev")]
        )
