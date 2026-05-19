from health_app.data import save_users_health_records, load_users_health_records, get_statistics
from health_app.health import Health


def test_load_nonexistent_file_returns_empty_list(tmp_path):
    filename = tmp_path / "missing.json"
    records = load_users_health_records(filename)
    assert records == []


def test_save_and_load_roundtrip(tmp_path):
    filename = tmp_path / "records.json"
    records = [
        Health("Johan", 73, 1.73),
        Health("Anna", 60, 1.65),
    ]

    save_users_health_records(records, filename)
    loaded_records = load_users_health_records(filename)

    assert len(loaded_records) == 2
    assert loaded_records[0].name == "Johan"
    assert loaded_records[1].name == "Anna"
    assert loaded_records[0].weight_kg == 73
    assert loaded_records[1].height_m == 1.65


def test_get_statistics():
    records = [
        Health("A", 55, 1.80),   
        Health("B", 75, 1.80),   
        Health("C", 85, 1.80),   
        Health("D", 100, 1.80), 
        Health("E", 90, 1.80),   
    ]

    stats = get_statistics(records)

    assert stats["total_records"] == 5
    assert stats["avg_bmi"] == round(
        (
            Health("A", 55, 1.80).calculate_bmi()
            + Health("B", 75, 1.80).calculate_bmi()
            + Health("C", 85, 1.80).calculate_bmi()
            + Health("D", 100, 1.80).calculate_bmi()
            + Health("E", 90, 1.80).calculate_bmi()
        ) / 5,
        2,
    )
    assert stats["most_common_category"] == "Overweight"
    assert stats["category_distribution"] == {
        "Underweight": 1,
        "Normal": 1,
        "Overweight": 2,
        "Obese": 1,
    }