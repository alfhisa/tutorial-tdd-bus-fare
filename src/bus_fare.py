from datetime import datetime

def is_peak_hour(dt: datetime) -> bool:
    hour = dt.hour
    return (7 <= hour < 9) or (16 <= hour < 18)

def bus_ticket_price(age: int, ride_datetime: datetime, ride_duration: int, is_public_holiday: bool) -> float:
    if is_public_holiday:
        return 2.0

    if age < 2:
        return 0.0

    weekday = ride_datetime.weekday()
    if weekday >= 5:
        return 0.0 if age < 2 else 2.0

    if ride_duration < 5 and not is_peak_hour(ride_datetime):
        return 0.0

    base_fare = 3.0
    if age < 18 or age > 65:
        base_fare /= 2

    if is_peak_hour(ride_datetime):
        base_fare += 1.5

    return base_fare

