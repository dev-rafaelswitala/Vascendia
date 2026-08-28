from enum import Enum

class DeviceTypes(str, Enum):
    DESKTOP = "desktop"
    GAMING_CONSOLE = "gaming_console"
    LAPTOP = "laptop"
    MOBILE_PHONE = "mobile_phone"
    TABLET = "tablet"
    TELEVISION = "television"