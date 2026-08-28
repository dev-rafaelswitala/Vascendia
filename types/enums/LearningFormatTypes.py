from enum import Enum

class LearningFormatTypes(str, Enum):
    BOOK = "book"
    COURSE = "course"
    DISCUSSION = "discussion"
    EXERCISE = "exercise"
    GROUP_WORK = "group_work"
    LECTURE = "lecture"
    LESSON = "lesson"
    MIX = "mix"
    ONLINE_COURSE = "online_course"
    PODCAST = "podcast"
    PRACTICE = "practice"
    REPETITION = "repetition"
    RESEARCH = "research"
    VIDEO = "video"