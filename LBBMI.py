def calculate_bmi(weight_lb, height_ft, height_in):
    # Convert height to meters
    height_m = (height_ft * 12 + height_in) * 0.0254
    # Convert weight to kilograms
    weight_kg = weight_lb * 0.453592
    bmi = weight_kg / (height_m ** 2)
    return bmi

def main():
    try:
        weight_lb = float(input("Enter your weight in pounds: "))
        height_ft = int(input("Enter your height in feet(ft only not inches): "))
        height_in = int(input("Enter the additional inches (if any): "))
        bmi = calculate_bmi(weight_lb, height_ft, height_in)
        print(f"Your BMI is {bmi:.2f} ")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight, height in feet, and additional inches.")

if __name__ == "__main__":
    main()

