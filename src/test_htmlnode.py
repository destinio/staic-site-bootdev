import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("div", "Oh hey", None, {"class": "what"})

        self.assertEqual(node.props_to_html(), ' class="what"')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Welcome!")
        self.assertEqual(node.to_html(), "Welcome!")

    def test_to_html_no_children(self):
        node = LeafNode("h1", "Bye!")

        self.assertEqual(node.to_html(), "<h1>Bye!</h1>")

    def test_to_html_no_children_props(self):
        node = LeafNode("h1", "Again?", {"class": "leaf-me", "aria": "aria-test"})

        self.assertEqual(
            node.to_html(), '<h1 class="leaf-me" aria="aria-test">Again?</h1>'
        )


if __name__ == "__main__":
    unittest.main()
