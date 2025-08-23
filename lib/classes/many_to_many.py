class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters")

        from .many_to_many import Author, Magazine
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")

        self._title = title
        self._author = author
        self._magazine = magazine
        Article.all.append(self)

    # Immutable
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise Exception("Title is immutable and cannot be changed")

    # Mutable
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from .many_to_many import Author
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    # Mutable
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from .many_to_many import Magazine
        if not isinstance(value, Magazine):
            raise Exception("magazine must be a Magazine instance")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Author name must be a non-empty string")
        self._name = name.strip()

    # Immutable
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise Exception("Author name is immutable and cannot be changed")

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = {mag.category for mag in self.magazines()}
        return list(categories) if categories else None


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name  # goes through setter
        self.category = category  # goes through setter

    # Mutable
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            # ignore invalid values
            pass

    # Mutable
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._category = value.strip()
        else:
            # ignore invalid values
            pass

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [
            author for author in self.contributors()
            if sum(1 for article in self.articles() if article.author is author) > 2
        ]
        return authors if authors else None
