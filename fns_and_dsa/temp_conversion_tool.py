FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  """Converts a temperature in Fahrenheit to Celsius.

  Args:
      fahrenheit: Temperature in Fahrenheit (float).

  Returns:
      The converted temperature in Celsius (float).
  """
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

def convert_to_fahrenheit(celsius):
  """Converts a temperature in Celsius to Fahrenheit.

  Args:
      celsius: Temperature in Celsius (float).

  Returns:
      The converted temperature in Fahrenheit (float).
  """
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

def main():
  while True:
    try:
      value = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()

      if unit == 'C':
        converted_value = convert_to_fahrenheit(value)
        converted_unit = 'F'
      elif unit == 'F':
        converted_value = convert_to_celsius(value)
        converted_unit = 'C'
      else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

      print(f"{value:.1f}{unit} is equivalent to {converted_value:.1f}{converted_unit}")
      break
    except ValueError as e:
      print(e)
      print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
  main() 