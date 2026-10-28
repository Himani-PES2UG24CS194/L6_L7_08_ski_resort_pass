import pytest
from ski_resort_pass import process_resort_bookings, check_chairlift_anemometer


def test_validation_branches():
    with pytest.raises(ValueError):
        process_resort_bookings("invalid", 10)
    with pytest.raises(ValueError):
        process_resort_bookings([], -1)


def test_group_activity_branches():
    assert process_resort_bookings([{"is_active": False}], 10)["status"] == "ZERO_SALES"
    assert process_resort_bookings([{"is_active": True, "duration": "full_day", "skiers": [{"age": 30}]}], 10)["status"] == "COMPLETED"


def test_duration_branches():
    for duration, expected in [("season", 300), ("full_day", 80), ("half_day", 50)]:
        result = process_resort_bookings(
            [{"is_active": True, "duration": duration, "skiers": [{"age": 30}]}], 0
        )
        assert result["total_revenue"] == expected

    result = process_resort_bookings(
        [{"is_active": True, "duration": "invalid", "skiers": [{"age": 30}]}], 0
    )
    assert result["status"] == "ZERO_SALES"


def test_age_and_rental_branches():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [
            {"age": 0},
            {"age": 10},
            {"age": 30, "gear_rental": True},
            {"age": 65}
        ]
    }]
    assert process_resort_bookings(groups, 0)["total_revenue"] == 48 + 80 + 35 + 56


def test_blackout_branches():
    full_day = [{"is_active": True, "duration": "full_day",
                 "skiers": [{"age": 30, "blackout_override": True}]}]
    half_day = [{"is_active": True, "duration": "half_day",
                 "skiers": [{"age": 30, "blackout_override": True},
                            {"age": 30}]}]
    assert process_resort_bookings(full_day, 0)["total_revenue"] == 40
    assert process_resort_bookings(half_day, 0)["total_revenue"] == 0


def test_locker_and_audit_branches():
    locker = [{"is_active": True, "duration": "full_day",
               "includes_lodge_locker": True, "skiers": [{"age": 30}]}]
    assert process_resort_bookings(locker, 15)["total_revenue"] == 95

    rejected = [{"is_active": True, "duration": "invalid", "skiers": []} for _ in range(5)]
    assert process_resort_bookings(rejected, 0)["status"] == "AUDIT_REVIEW"


def test_zero_sales_and_completed_branches():
    assert process_resort_bookings([], 0)["status"] == "ZERO_SALES"
    assert process_resort_bookings(
        [{"is_active": True, "duration": "full_day", "skiers": [{"age": 25}]}], 0
    )["status"] == "COMPLETED"


def test_anemometer_branches():
    assert check_chairlift_anemometer([]) == "NO_DATA"
    assert check_chairlift_anemometer([[30, 46, 40]]) == "SAFE_OPERATION"
    assert check_chairlift_anemometer([[46, 47]]) == "SUSPEND_LIFT"
    assert check_chairlift_anemometer([[46, 40, 47]]) == "SAFE_OPERATION"
