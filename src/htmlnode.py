class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        props_str = ""

        if self.props:
            for k, v in self.props.items():
                props_str += f' {k}="{v}"'

        return props_str

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("You need to provide a value")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Must have a tag dude!!")

        if self.children is None:
            raise ValueError("Where those children. creepy")

        html_str = f"<{self.tag}{self.props_to_html()}>"

        for node in self.children:
            html_str += node.to_html()

        html_str += f"</{self.tag}>"

        return html_str
