from health_app.data import (
    save_users_health_records,
    load_users_health_records,
    get_statistics,
)
from health_app.health import Health


def main():
    records = load_users_health_records()

    while True:
        print("\n1. Add Health Record")
        print("2. View All Records")
        print("3. View Statistics")
        print("4. Save & Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                name = input("Enter name: ").strip()
                weight = float(input("Enter weight (kg): "))
                height = float(input("Enter height (m): "))

                record = Health(name, weight, height)
                records.append(record)
                save_users_health_records(records)

                print(
                    f"Added {record.name}: "
                    f"BMI {record.calculate_bmi()} "
                    f"({record.get_bmi_category()}) | "
                    f"Ideal: {record.get_ideal_weight()}kg | "
                    f"Advice: {record.get_health_advice()}"
                )

            except ValueError:
                print("Invalid input, please try again")

        elif choice == "2":
            if not records:
                print("No health records found.")
            else:
                for record in records:
                    ideal_weight = record.get_ideal_weight()
                    difference = round(record.weight_kg - ideal_weight, 1)

                    if difference > 0:
                        difference_text = f"{difference} kg above ideal weight"
                    elif difference < 0:
                        difference_text = f"{abs(difference)} kg below ideal weight"
                    else:
                        difference_text = "At ideal weight"

                    print(
                        f"{record.name} | "
                        f"BMI: {record.calculate_bmi()} | "
                        f"Category: {record.get_bmi_category()} | "
                        f"{difference_text}"
                    )

        elif choice == "3":
            stats = get_statistics(records)

            print(f"Total records: {stats['total_records']}")
            print(f"Average BMI: {stats['avg_bmi']}")
            print(f"Most common category: {stats['most_common_category']}")
            print("Category distribution:")

            for category, count in stats["category_distribution"].items():
                print(f" {category}: {count}")

        elif choice == "4":
            save_users_health_records(records)
            print("Goodbye!")
            break

        else:
            print("Invalid input, please try again")


if __name__ == "__main__":
    main()