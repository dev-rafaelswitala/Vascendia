from collections.abc import Mapping
from typing import Optional

def calculate_rate(
    value: float | int | None,
    duration_min: float | int | None,
) -> Optional[float]:
    if value is None or duration_min is None or duration_min <= 0:
        return None
    return round((value / duration_min) * 60, 2)

def calculate_speed_kmh(session: Mapping) -> Optional[float]:
    return calculate_rate(
        session.get("distance_km"),
        session.get("duration_min"),
    )

def calculate_pages_per_hour(session: Mapping) -> Optional[float]:
    return calculate_rate(
        session.get("pages"),
        session.get("duration_min"),
    )

def calculate_total_pushups(session: Mapping) -> Optional[int]:
    sets = session.get("set_count")
    average = session.get("average_per_set")
    if sets is None or average is None:
        return None
    return int(sets * average)

def calculate_swimming_speed(session: Mapping) -> Optional[float]:
    return calculate_rate(
        session.get("distance_m"),
        session.get("duration_min"),
    )