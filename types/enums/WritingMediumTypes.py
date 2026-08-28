from enum import Enum

class WritingMediumTypes(str, Enum):
    BLOG = "blog"
    BOOK = "book"
    CREATIVE = "creative"
    DIARY = "diary"
    ESSAY = "essay"
    MIX = "mix"
    NOTES = "notes"
    NOVEL = "novel"
    POEM = "poem"
    PROFESSIONAL = "professional"
    TERM_PAPER = "term_paper"