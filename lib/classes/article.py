class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")

        self._title = title  # immutable
        self.author = author
        self.magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    def __repr__(self):
        return f"<Article title='{self.title}'>"
