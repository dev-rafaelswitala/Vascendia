from enum import Enum

class LanguageTrainingTypes(str, Enum):
    GRAMMAR = "grammar"
    LISTENING = "listening"
    PRONUNCIATION = "pronunciation"
    READING = "reading"
    VOCABULARY = "vocabulary"
    WRITING = "writing"