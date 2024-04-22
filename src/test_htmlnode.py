import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_to_html_with_children_no_props(self):
        node = ParentNode("div", [LeafNode("p", "leaf")])
        test_str = "<div><p>leaf</p></div>"

        self.assertEqual(node.to_html(), test_str)

    def test_to_html_with_children_with_parent(self):
        node = ParentNode(
            "div", [LeafNode("p", "leaf"), ParentNode("ul", [LeafNode("li", "one")])]
        )
        test_str = "<div><p>leaf</p><ul><li>one</li></ul></div>"

        self.assertEqual(node.to_html(), test_str)


if __name__ == "__main__":
    unittest.main()
