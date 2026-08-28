from enum import Enum

class CommunityActivityTypes(str, Enum):
    CLUBS = "clubs"
    MEETUPS = "meetups"
    ONLINE_COMMUNITY = "online_community"
    SOCIAL_EVENTS = "social_events"
    SPORTS_TEAM = "sports_team"
    VOLUNTEERING = "volunteering"
    WORKSHOP = "workshop"