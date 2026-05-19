import pytest
from health_app.health import Health


def test_create_user_health():
    person = Health("Johan", 73, 1.73)
    assert person.name == "Johan"
    assert person.weight_kg == 73
    assert person.height_m == 1.73


def test_empty_name_raises_error():
    with pytest.raises(ValueError):
        Health("", 73, 1.80)


def test_invalid_weight_raises_error():
    with pytest.raises(ValueError):
        Health("Johan", 0, 1.80)


def test_invalid_height_raises_error():
    with pytest.raises(ValueError):
        Health("Johan", 73, 0)


def test_calculate_bmi():
    person = Health("Johan", 81, 1.80)
    assert person.calculate_bmi() == 25.0


def test_underweight_category():
    person = Health("A", 55, 1.80)
    assert person.get_bmi_category() == "Underweight"


def test_normal_category():
    person = Health("B", 75, 1.80)
    assert person.get_bmi_category() == "Normal"


def test_overweight_category():
    person = Health("C", 85, 1.80)
    assert person.get_bmi_category() == "Overweight"


def test_obese_category():
    person = Health("D", 100, 1.80)
    assert person.get_bmi_category() == "Obese"


def test_get_health_advice_returns_string():
    person = Health("Anna", 60, 1.70)
    advice = person.get_health_advice()
    assert isinstance(advice, str)
    assert len(advice) > 0


def test_get_ideal_weight():
    person = Health("Anna", 60, 1.70)
    assert person.get_ideal_weight() == 63.6