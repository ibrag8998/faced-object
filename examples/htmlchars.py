from facedobj import FacedObj


class HtmlChars(FacedObj):
    def __init__(self, obj: str):
        self.obj: str
        super().__init__(obj)

    def template_face(self) -> str:
        return (
            self.obj.replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )


html = HtmlChars('<b> Hello, "World"! </b>')

print(html.get("template"))  # &lt;b&gt; Hello, &quot;World&quot;! &lt;/b&gt;
print(html.get())  # <b> Hello, "World"! </b>
