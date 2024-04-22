import re
from htmlnode import LeafNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type=text_type_text, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        result = (
            self.text == other_node.text
            and self.text_type == other_node.text_type
            and self.url == other_node.url
        )

        return result

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode(
            "img", text_node.text, {"src": text_node.url, "alt": text_node.text}
        )

    raise ValueError(f"text_type is wrong: {text_node.text_type}")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        splits = node.text.split(delimiter)

        for i in range(len(splits)):
            if (i + 1) % 2 != 0:
                new_nodes.append(TextNode(splits[i], text_type_text))
            else:
                new_nodes.append(TextNode(splits[i], text_type))

    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    found = re.findall(pattern, text)
    return found


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    found = re.findall(pattern, text)
    return found
