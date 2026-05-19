import json
import os

from health_app.health import Health


def save_users_health_records(
    records: list[Health],
    filename: str = "health_records.json",
) -> None:
    folder = os.path.dirname(filename)
    if folder:
        os.makedirs(folder, exist_ok=True)

    data = []

    for record in records:
        data.append(
            {
                "name": record.name,
                "weight_kg": record.weight_kg,
                "height_m": record.height_m,
                "calculated_bmi": record.calculate_bmi(),
            }
        )

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_users_health_records(filename: str = "health_records.json") -> list[Health]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        records = []

        for item in data:
            records.append(
                Health(
                    item["name"],
                    item["weight_kg"],
                    item["height_m"],
                )
            )

        return records

    except FileNotFoundError:
        return []


def get_statistics(records):
    if not records:
        return {
            "total_records": 0,
            "avg_bmi": 0.0,
            "most_common_category": None,
            "category_distribution": {
                "Underweight": 0,
                "Normal": 0,
                "Overweight": 0,
                "Obese": 0,
            },
        }

    category_distribution = {
        "Underweight": 0,
        "Normal": 0,
        "Overweight": 0,
        "Obese": 0,
    }

    total_bmi = 0

    for record in records:
        total_bmi += record.calculate_bmi()
        category = record.get_bmi_category()
        category_distribution[category] += 1

    total_records = len(records)
    avg_bmi = round(total_bmi / total_records, 2)
    most_common_category = max(category_distribution, key=category_distribution.get)

    return {
        "total_records": total_records,
        "avg_bmi": avg_bmi,
        "most_common_category": most_common_category,
        "category_distribution": category_distribution,
    }