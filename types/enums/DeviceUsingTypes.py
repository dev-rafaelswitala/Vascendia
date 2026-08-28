from enum import Enum

class DeviceUsingTypes(str, Enum):
    CALLS = "calls"
    CHATS = "chats"
    CREATIVITY = "creativity"
    E_BOOK = "e_book"
    ENTERTAINMENT = "entertainment"
    DIVERSION = "diversion"
    FREETIME = "freetime"
    GAMES = "games"
    LEARNING = "learning"
    MIX = "mix"
    PASTIME = "pastime"
    READING = "reading"
    SOCIAL_MEDIA = "social_media"
    VIDEOS = "videos"
    WORK = "work"
    WRITING = "writing"