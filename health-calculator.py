def bmi_imperial(w, h):
    """
    IMPERIAL equation for measuring one's BMI.
    w = weight, h = height
    """

    bmi_imperial_result = (w/h**2) * 703

    return bmi_imperial_result

def bmi_metric(w, h):
    """
    METRIC equation for measuring one's BMI.
    w = weight, h = height
    """

    bmi_metric_result = (w/h**2)

    return bmi_metric_result

def bmi_results(r):
    """
    Shows the user BMI number along with a chart to determine body mass range.
    """

    print("\nYour BMI is " + str("%.2f" % r) + "\n") #2 decimal number limit
    print("Take your number and match it to the chart below:\n")
    print("""
    CATERGORY               |   BMI RANGE
    ----------------------------------------
    Severely Underweight    |   <16.491
    Underweight             |   16.5 - 18.49
    Healthy                 |   18.5 - 24.99
    Overweight              |   25 - 29.99
    Obese                   |   >30
    """)

def lbs2kg(lbs):
    """
    Pounds to kilograms converter.
    """

    kg = lbs/2.2046

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
    Shows the user BMR number along with a chart for daily calorie needs.
    """

    print(f"\nYour BMR is {round(r)} calories.\n")
    print("Daily calorie needs are displayed below depending on how active you are daily:\n")
    print(f"""
    DAILY ACTIVITY LEVEL                                                |   Calories
    -----------------------------------------------------------------------------------
    Sedentary (little to no exercise in a day)                          |   {round(r * 1.2)}
    Lightly Active (light exercise/sports 1-3 days/week)                |   {round(r * 1.375)}
    Moderately Active (moderate exercise/sports 3-5 days/week)          |   {round(r * 1.55)}
    Very Active (hard exercise/sports 6-7 days a week)                  |   {round(r * 1.725)}
    Extremely Active (very hard exercise/sports and/or physical job)    |   {round(r * 1.9)}
    """)

# MAIN PROGRAM:

# I originally coded the program to make users measure their BMI before their BMR,
# but it's better for users to have a choice on what to start with and not have to 
# slog through one part of the program to get to the next.
start_choice = input("\nEnter 1 for Body Mass Index (BMI) or 2 for Basal Metabolic Rate (BMR): ")

if start_choice == "1":

    print("BMI selected.")
    
    bmi_measure = input("Enter 1 for imperial or 2 for metric: ")

    if bmi_measure == "1":

        print("Imperial selected.")

        # Height and weight both are converted to float numbers since
        # it will let users enter decimals if they want to be precise.
        bmi_height_imperial = float(input("Enter height (inches): "))
        bmi_weight_imperial = float(input("Enter weight (pounds): "))

        # User entries get sent to their respective equations for calculation.
        bmi_index_imperial = bmi_imperial(bmi_weight_imperial, bmi_height_imperial)

        # Number results and charts get displayed.
        bmi_results(bmi_index_imperial)

    elif bmi_measure == "2":

        print("Metric selected.")

        bmi_height_metric = float(input("Enter height (meters): "))
        bmi_weight_metric = float(input("Enter weight (kilograms): "))

        bmi_index_metric = bmi_metric(bmi_weight_metric, bmi_height_metric)

        bmi_results(bmi_index_metric)

    else:
        print("ERROR: Invalid input.")

elif start_choice == "2":

    print("BMR Selected.")

    bmr_measure = input("Enter 1 for imperial (male), 2 for imperial (female), 3 for metric (male), or 4 for metirc (female): ")

    if bmr_measure == "1":

        print("Imerial (male) selected.")

        # For BMR calculation, I am using the Mifflin-St. Jeor equation. However, the equation only supports metric meausrements. 
        # Since I couldn't find an imperial version, I had to get creative and convert the imperial measurements submitted by the user 
        # into metric ones as you can see below:
        bmr_height_imperial_m = in2cm(float(input("Enter height (inches): ")))
        bmr_weight_imperial_m = lbs2kg(float(input("Enter weight (pounds): ")))
        bmr_age_imperial_m = int(input("Enter age: "))

        bmr_calories_imperial_m = bmr_male(bmr_weight_imperial_m, bmr_height_imperial_m, bmr_age_imperial_m)

        bmr_results(bmr_calories_imperial_m)

    elif bmr_measure == "2":

        print("Imerial (female) selected.")

        bmr_height_imperial_f = in2cm(float(input("Enter height (inches): ")))
        bmr_weight_imperial_f = lbs2kg(float(input("Enter weight (pounds): ")))
        bmr_age_imperial_f = int(input("Enter age: "))

        bmr_calories_imperial_f = bmr_female(bmr_weight_imperial_f, bmr_height_imperial_f, bmr_age_imperial_f)

        bmr_results(bmr_calories_imperial_f)

    elif bmr_measure == "3":

        print("Metric (male) selected.")

        bmr_height_metric_m = float(input("Enter height (centimeters): "))
        bmr_weight_metric_m = float(input("Enter weight (kilograms): "))
        bmr_age_metric_m = int(input("Enter age: "))

        bmr_calories_metric_m = bmr_male(bmr_weight_metric_m, bmr_height_metric_m, bmr_age_metric_m)

        bmr_results(bmr_calories_metric_m)

    elif bmr_measure == "4":

        print("Mertic (female) selected.")

        bmr_height_metric_f = float(input("Enter height (centimeters): "))
        bmr_weight_metric_f = float(input("Enter weight (kilograms): "))
        bmr_age_metric_f = int(input("Enter age: "))

        bmr_calories_metric_f = bmr_female(bmr_weight_metric_f, bmr_height_metric_f, bmr_age_metric_f)

        bmr_results(bmr_calories_metric_f)

    else:
        print("ERROR: Invalid input.")

else:
    print("ERROR: Invalid input.")