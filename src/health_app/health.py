class Health:
    def __init__(self, name: str, weight_kg: float, height_m: float):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than 0.")
        if height_m <= 0:
            raise ValueError("Height must be greater than 0.")

        self.name = name
        self.weight_kg = weight_kg
        self.height_m = height_m

    def calculate_bmi(self) -> float:
        bmi = self.weight_kg / (self.height_m ** 2)
        return round(bmi, 2)

    def get_bmi_category(self) -> str:
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        if bmi < 25:
            return "Normal"
        if bmi < 30:
            return "Overweight"
        return "Obese"

    def get_health_advice(self) -> str:
        category = self.get_bmi_category()

        if category == "Underweight":
            return (
                "You are currently underweight. "
                "Consider increasing your calorie intake with nutritious foods "
                "and adding strength training to build muscle. "
                "If this is a concern, speak with a healthcare professional."
            )

        if category == "Normal":
            return (
                "You are in the normal BMI range. "
                "Keep maintaining a balanced diet and regular physical activity. "
                "You can also include strength training to support long-term health."
            )

        if category == "Overweight":
            return (
                "You are in the overweight BMI range. "
                "A moderate calorie deficit, regular exercise, and higher protein intake "
                "may help improve your health. "
                "Consider seeking professional guidance if needed."
            )

        return (
            "You are in the obese BMI range. "
            "It may help to focus on gradual lifestyle changes such as improved nutrition "
            "and consistent physical activity. "
            "You should consider speaking with a healthcare professional for support."
        )

    def get_ideal_weight(self) -> float:
        ideal_weight = 22 * (self.height_m ** 2)
        return round(ideal_weight, 1)