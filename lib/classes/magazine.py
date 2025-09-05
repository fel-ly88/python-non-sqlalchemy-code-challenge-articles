class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def articles(self):
        from classes.many_to_many import Article
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None   

    def contributing_authors(self):
        authors = []
        for author in self.contributors():
            count = len([article for article in self.articles() if article.author == author])
            if count > 2:
                authors.append(author)
        return authors if authors else None   
