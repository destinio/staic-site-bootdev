import re
from typing import Text
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


def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    found = re.findall(pattern, text)
    return found


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    found = re.findall(pattern, text)
    return found


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        og_txt = node.text

        images = extract_markdown_images(og_txt)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        for image in images:
            groups = og_txt.split(f"![{image[0]}]({image[1]})", 1)

            if len(groups) != 2:
                raise ValueError("invalid markdown")

            if groups[0] != "":
                new_nodes.append(TextNode(groups[0], text_type_text))

            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            og_txt = groups[1]

        if og_txt != "":
            new_nodes.append(TextNode(og_txt, text_type_text))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        og_txt = node.text
        links = extract_markdown_links(og_txt)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            groups = og_txt.split(f"[{link[0]}]({link[1]})", 1)
            if len(groups) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if groups[0] != "":
                new_nodes.append(TextNode(groups[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            og_txt = groups[1]
        if og_txt != "":
            new_nodes.append(TextNode(og_txt, text_type_text))
    return new_nodes
