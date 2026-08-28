from enum import Enum

class ReadingMediumTypes(str, Enum):
    ARTICLE = "article"
    BLOG = "blog"
    BOOK = "book"
    COMIC = "comic"
    E_BOOK = "e_book"
    MAGAZINE = "magazine"
    NEWSPAPER = "newspaper"