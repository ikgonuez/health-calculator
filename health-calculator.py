# This module will be used for exiting the program upon user input.
import sys

# Defining an error
err = "ERROR: Invalid input. Try again."


# FUNCTIONS:
def height_input():
    """
    User enters height while input errors get caught just in case.
    """

    while True:
        try:
            h = float(input("Enter height: "))

            return h

        except ValueError:
            print(err)


def weight_input():
    """
    User enters weight while input errors get caught just in case.
    """

    while True:
        try:
            w = float(input("Enter weight: "))

            return w

        except ValueError:
            print(err)


def age_input():
    """
    User enters age while input errors get caught just in case.
    """

    while True:
        try:
            a = float(input("Enter age: "))

            return a

        except ValueError:
            print(err)


def bmi_imperial(w, h):
    """
    IMPERIAL equation for measuring one's BMI.
    w = weight, h = height
    """

    bmi_imperial_result = (w / h**2) * 704

    return bmi_imperial_result


def bmi_metric(w, h):
    """
    METRIC equation for measuring one's BMI.
    w = weight, h = height
    """

    bmi_metric_result = w / h**2

    return bmi_metric_result


def bmi_results(r):
    """
    Shows the user their BMI number along with a chart to determine body mass range.
    """

    print(f"\nYour BMI is {round(r, 2)}\n")  # 2 decimal number limit
    print("Take your number and match it to the chart below:\n")
    print(
        """
    CATERGORY               |   BMI RANGE
    ----------------------------------------
    Severely Underweight    |   <16.49
    Underweight             |   16.5 - 18.49
    Healthy                 |   18.5 - 24.99
    Overweight              |   25 - 29.99
    Obese                   |   >30
    """
    )


def cm2m(cm):
    """
    Centimeters to meters converter.
    """

    m = cm * 0.01

    return m


def lbs2kg(lbs):
    """
    Pounds to kilograms converter.
    """

    kg = lbs / 2.2046

    return kg


def in2cm(i):
    """
    Inches to centimeters converter.
    """

    cm = i * 2.54

    return cm


def bmr_male(w, h, a):
    """
    Calculates BMR for males.
    w = weight, h = height, a = age
    """

    bmr = (10 * w) + (6.25 * h) - (5 * a) + 5

    return bmr


def bmr_female(w, h, a):
    """
    Calculates BMR for females.
    w = weight, h = height, a = age
    """

    bmr = (10 * w) + (6.25 * h) - (5 * a) - 161

    return bmr


def bmr_results(r):
    """
    Shows the user their BMR number along with a chart for daily calorie needs.
    """

    print(f"\nYour BMR is {round(r)} calories.\n")
    print(
        "Daily calorie needs are displayed below depending on how active you are daily:\n"
    )
    print(
        f"""
    DAILY ACTIVITY LEVEL                                                |   CALORIES
    -----------------------------------------------------------------------------------
    Sedentary (little to no exercise in a day)                          |   {round(r * 1.2)}
    Lightly Active (light exercise/sports 1-3 days/week)                |   {round(r * 1.375)}
    Moderately Active (moderate exercise/sports 3-5 days/week)          |   {round(r * 1.55)}
    Very Active (hard exercise/sports 6-7 days a week)                  |   {round(r * 1.725)}
    Extremely Active (very hard exercise/sports and/or physical job)    |   {round(r * 1.9)}
    """
    )


def restart_or_exit():
    """
    Program restarts or finishes depending on user input.
    """

    while True:
        end_choice = input("Enter 1 to restart or 2 to end program: ")

        if end_choice == "1":
            print("\nProgram restarted.")

            break

        elif end_choice == "2":
            print("\nProgram finished.")

            sys.exit()

        else:
            print(err)


# MAIN PROGRAM:
while True:
    # I originally coded the program to make users measure their BMI before their BMR,
    # but it's better for users to have a choice on what to start with and not have to
    # slog through one part of the program to get to the next.
    start_choice = input(
        "\nEnter 1 for Body Mass Index (BMI) or 2 for Basal Metabolic Rate (BMR): "
    )

    if start_choice == "1":
        print("\nBMI selected.")

        while True:
            bmi_measure = input("\nEnter 1 for imperial or 2 for metric: ")

            if bmi_measure == "1":
                print("\nImperial selected.")
                print("Height: Inches\nWeight: Pounds\n")

                bmi_height = height_input()
                bmi_weight = weight_input()

                user_bmi = bmi_imperial(bmi_weight, bmi_height)

                bmi_results(user_bmi)

                restart_or_exit()

                break

            elif bmi_measure == "2":
                print("Metric selected.")
                print("Height: Centimeters\nWeight: Kilograms\n")

                # For the BMI equation, the metric version uses meters instead of centimeters.
                # This is fine, but I find centimeters to be more precise and less error-prone for
                # the users, so I made a "centimeter-to-meter" converter just to bypass this little
                # problem. The BMR equation uses centimeters, so I want this
                # one to work the same.
                bmi_height = cm2m(height_input())
                bmi_weight = weight_input()

                user_bmi = bmi_metric(bmi_weight, bmi_height)

                bmi_results(user_bmi)

                restart_or_exit()

                break

            else:
                print(err)

    elif start_choice == "2":
        print("\nBMR Selected.")

        while True:
            bmr_measure = input(
                "\nEnter 1 for imperial (male), 2 for imperial (female), 3 for metric (male), 4 for metric (female): "
            )

            if bmr_measure == "1":
                print("\nImerial (male) selected.")
                print("Height: Inches\nWeight: Pounds\n")

                # For BMR calculation, I am using the Mifflin equation. However, the equation
                # only supports metric measurements. Since I couldn't find an imperial version, I had
                # to get creative and convert the imperial measurements submitted by the
                # user into metric ones as you can see below:
                bmr_height = in2cm(height_input())
                bmr_weight = lbs2kg(weight_input())
                bmr_age = age_input()

                user_bmr = bmr_male(bmr_weight, bmr_height, bmr_age)

                bmr_results(user_bmr)

                restart_or_exit()

                break

            elif bmr_measure == "2":
                print("\nImperial (female) selected.")
                print("Height: Inches\nWeight: Pounds\n")

                bmr_height = in2cm(height_input())
                bmr_weight = lbs2kg(weight_input())
                bmr_age = age_input()

                user_bmr = bmr_female(bmr_weight, bmr_height, bmr_age)

                bmr_results(user_bmr)

                restart_or_exit()

                break

            elif bmr_measure == "3":
                print("\nMetric (male) selected.")
                print("Height: Centimeters\nWeight: Kilograms\n")

                bmr_height = height_input()
                bmr_weight = weight_input()
                bmr_age = age_input()

                user_bmr = bmr_male(bmr_weight, bmr_height, bmr_age)

                bmr_results(user_bmr)

                restart_or_exit()

                break

            elif bmr_measure == "4":
                print("\nMetric (female) selected.")
                print("Height: Centimeters\nWeight: Kilograms\n")

                bmr_height = height_input()
                bmr_weight = weight_input()
                bmr_age = age_input()

                user_bmr = bmr_female(bmr_weight, bmr_height, bmr_age)

                bmr_results(user_bmr)

                restart_or_exit()

                break

            else:
                print(err)

    else:
        print(err)

