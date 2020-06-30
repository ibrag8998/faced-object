# Faced Object pattern

"Faced Object" means it has different faces. One for templates, one for code,
one by default etc (and etc (and etc)).

## Use Cases Examples

- Process user input in your website. Just define one face for templates

- etc

## Usage Example

This short tutorial will walk you through implementing `HtmlChars` class, which
takes care about what is in your code and what is in your templates.

1. Subclass `FacedObj`:

    ```python
    class HtmlChars(FacedObj):
        pass
    ```

2. Extend `__init__` to annotate `self.obj` type, it will grant you editor's
support and autocompletion:

    ```python
    def __init__(self, obj: str):
        self.obj: str
        super().__init__(obj)
    ```

3. Now implement `template` face. To add face, just define a method which
name ends with `FacedObj.face_name_suffix`, which default to `"_face"`:

    ```python
    def template_face(self) -> str:
        return (
            self.obj.replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )
    ```

4. That's all about implementing. Now let's see usage examples:

    ```python
    html = HtmlChars('<b> Hello, "World"! </b>')

    print(html.get("template"))
    # &lt;b&gt; Hello, &quot;World&quot;! &lt;/b&gt;
    print(html.get())
    # <b> Hello, "World"! </b>
    ```

> Note: if you will try to `.get()` and pass wrong face name, the `transparent`
one will be used. It just returns `self.obj` without any processing.
