def safe_divide(numerator, denominator):
    try:
        number = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return "Error: Division by zero is not allowed."
        return number / denominator
    except ValueError:
        return "Error: Non-numeric input detected."