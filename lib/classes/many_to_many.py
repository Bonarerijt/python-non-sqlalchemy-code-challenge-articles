class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title


class Author:
    def __init__(self, name):
        
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name cannot be empty")
        self._name = name

    @property
    def name (self):
            return self._name
    
    @name.setter
    def name(self, value):
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]


    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))


    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        areas = list(set([article.magazine.category for article in self.articles()]))
        return areas if areas else None


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name (self):
        return self.name

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
