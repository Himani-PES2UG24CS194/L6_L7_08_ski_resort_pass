
from datetime import date
import math


def parse_season_pass_validity(date_str):
    try:
        if not isinstance(date_str, str):
            return "Invalid date input"

        parts = date_str.split('/')
        if len(parts) != 3:
            return "Invalid date input"

        year, month, day = map(int, parts)
        date(year, month, day)

        valid = year >= 2026

        return (
            f"Pass Expiry: {year:04d}-{month:02d}-{day:02d} "
            f"({'VALID' if valid else 'EXPIRED'})"
        )

    except (ValueError, TypeError, OverflowError):
        return "Invalid date input"


def compute_trail_gradient(elevation_str):
    try:
        if not isinstance(elevation_str, str):
            return None

        parts = elevation_str.split(':')
        if len(parts) != 2:
            return None

        drop = float(parts[0])
        distance = float(parts[1])

        if not math.isfinite(drop) or not math.isfinite(distance):
            return None

        if drop < 0 or distance <= 0:
            return None

        gradient_pct = (drop / distance) * 100.0
        return round(gradient_pct, 2)

    except (ValueError, TypeError, ZeroDivisionError, OverflowError):
        return None


def calculate_lift_access_tier(zone_code):
    zone_rates = {
        "BEG": 35.0,
        "INT": 60.0,
        "ADV": 85.0,
        "ALL": 110.0
    }

    try:
        if not isinstance(zone_code, str):
            return None

        prefix = zone_code.strip().upper()[:3]
        return zone_rates.get(prefix)

    except (AttributeError, TypeError):
        return None


def main():
    print("==== Running parse_season_pass_validity ====")
    d_input = input("Enter pass expiry (YYYY/MM/DD): ")
    print(parse_season_pass_validity(d_input))

    print("\n==== Running compute_trail_gradient ====")
    e_input = input("Enter drop:distance (e.g. 250:1000): ")
    print("Gradient %:", compute_trail_gradient(e_input))

    print("\n==== Running calculate_lift_access_tier ====")
    z_input = input("Enter zone code (e.g. BEG, INT, ALL): ")
    print("Lift Pass Price: $", calculate_lift_access_tier(z_input))


if __name__ == "__main__":
    main()
