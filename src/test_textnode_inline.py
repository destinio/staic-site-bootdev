import unittest

from textnode import (
    TextNode,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
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

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_link, "https://blog.boot.dev"),
                TextNode(" with text that follows", text_type_text),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
            nodes,
        )
