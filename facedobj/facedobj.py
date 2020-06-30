class FacedObj:
    """
    See README.md section "## Usage"
    """

    face_name_suffix = "_face"

    def __init__(self, obj=...):
        """
        Ellipsis (...) is used here to allow passing param `obj` as one of
        kwargs in your subclass' `__init__` method
        """
        if obj is Ellipsis:
            raise ValueError("param `obj` is required for `FacedObj` instance")

        self.obj = obj
        self.faces = {
            face_name[: -len(self.face_name_suffix)]: getattr(self, face_name)
            for face_name in dir(self)
            if face_name.endswith(self.face_name_suffix)
        }
        self.faces["transparent"] = self.transparent

    def transparent(self):
        """
        This method just return `self.obj` without any processing.
        """
        return self.obj

    def get(self, face_name: str = None):
        """
        If specified `face_name` is in `self.faces`, it will be returned,
        else `self.faces["transparent"]`
        """
        if face_name not in self.faces:
            if face_name is not None:  # means client provided something
                print(
                    "You asked for non-existing face, "
                    "so `transparent` will be used"
                )
            face_name = "transparent"
        return self.faces[face_name]()
