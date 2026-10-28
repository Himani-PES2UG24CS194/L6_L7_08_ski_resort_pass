import pytest
from ski_resort_pass import process_resort_bookings, check_chairlift_anemometer


def test_invalid_groups():
    with pytest.raises(ValueError):
        process_resort_bookings("invalid", 15)


def test_negative_facility_fee():
    with pytest.raises(ValueError):
        process_resort_bookings([], -1)


def test_inactive_and_empty_groups():
    assert process_resort_bookings([{"is_active": False}], 15)["status"] == "ZERO_SALES"
    assert process_resort_bookings([{"is_active": True, "skiers": []}], 15)["status"] == "ZERO_SALES"


def test_all_pass_durations_and_age_categories():
    groups = [
        {"is_active": True, "duration": "season", "skiers": [{"age": 30}]},
        {"is_active": True, "duration": "full_day", "skiers": [{"age": 10, "gear_rental": True}]},
        {"is_active": True, "duration": "half_day", "skiers": [{"age": 70}]},
    ]
    result = process_resort_bookings(groups, 15)
    assert result["total_revenue"] == 300 + 48 + 35 + 35
    assert result["status"] == "COMPLETED"


def test_unknown_duration_and_invalid_age():
    groups = [
        {"is_active": True, "duration": "unknown", "skiers": [{"age": 30}]},
        {"is_active": True, "duration": "full_day", "skiers": [{"age": 0}]},
    ]
    assert process_resort_bookings(groups, 15)["status"] == "ZERO_SALES"


def test_blackout_override_full_day():
    groups = [{"is_active": True, "duration": "full_day",
               "skiers": [{"age": 30, "blackout_override": True}]}]
    assert process_resort_bookings(groups, 15)["total_revenue"] == 40


def test_blackout_override_half_day():
    groups = [{"is_active": True, "duration": "half_day",
               "skiers": [{"age": 30, "blackout_override": True},
                          {"age": 30}]}]
    assert process_resort_bookings(groups, 15)["total_revenue"] == 0


def test_locker_fee_and_multiple_rejections():
    groups = [
        {"is_active": True, "duration": "full_day", "includes_lodge_locker": True,
         "skiers": [{"age": 30, "gear_rental": True}]},
        {"is_active": True, "duration": "bad", "skiers": []},
        {"is_active": True, "duration": "bad", "skiers": []},
        {"is_active": True, "duration": "bad", "skiers": []},
        {"is_active": True, "duration": "bad", "skiers": []},
    ]
    assert process_resort_bookings(groups, 15)["status"] == "COMPLETED"


def test_multiple_skiers_and_revenue():
    groups = [{"is_active": True, "duration": "full_day",
               "skiers": [{"age": 11}, {"age": 30}, {"age": 65}]}]
    assert process_resort_bookings(groups, 15)["total_revenue"] == 184


def test_anemometer_no_data():
    assert check_chairlift_anemometer([]) == "NO_DATA"
    assert check_chairlift_anemometer(None) == "NO_DATA"


def test_anemometer_safe_operation():
    assert check_chairlift_anemometer([[40, 46, 42, 47], [30]]) == "SAFE_OPERATION"


def test_anemometer_suspends_after_consecutive_gusts():
    assert check_chairlift_anemometer([[46, 47]]) == "SUSPEND_LIFT"
    assert check_chairlift_anemometer([[50], [46, 48]]) == "SUSPEND_LIFT"


