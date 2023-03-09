# Health Calculator

## Overview:

A calculator that determines Body Mass Index (BMI) and/or Basal Metabolic Rate (BMR). Imperial and metric measurements are both supported. The program is written in Python.

### What is BMI?

BMI is a medical screeening tool that determines if someone is in a healthy weight range for their height. It helps one figure out if they're either underweight, healthy, or overweight. [(More info)](https://simple.wikipedia.org/wiki/Body_mass_index)

### What is BMR?

BMR is a tool used to measure someone's daily calorie needs for their body to sustain itself. It also determines how many calories one needs depending on how active they are daily. [(More info)](https://en.wikipedia.org/wiki/Basal_metabolic_rate)

## Usage:

Run the program "health-calculator.py" through the command-line. If you don't know how, just consult this [link](https://www.wikihow.com/Use-Windows-Command-Prompt-to-Run-a-Python-File).

## Execution:

The program will start by giving the user an input prompt that lets you choose between BMI or BMR.

`Enter 1 for Body Mass Index (BMI) or 2 for Basal Metabolic Rate (BMR): `

Both routes will be discussed further in this section.

### BMI Route

If BMI is chosen, the user will be given an option between imperial/metric.

`Enter 1 for imperial or 2 for metric: `

A prompt will show what measurements need to be used (depending on what system they choose), along with prompts to enter height and weight.

```
Height: Inches/Centimeters
Weight: Pounds/Kilograms

Enter height:
Enter weight:
```

Finally, the BMI result number will be shown, along with a chart to match it to.

`Your BMI is <result number>`

CATERGORY               |   BMI RANGE
----------------------- | -------------
Severely Underweight    |   <16.49
Underweight             |   16.5 - 18.49
Healthy                 |   18.5 - 24.99
Overweight              |   25 - 29.99
Obese                   |   >30

### BMR Route

If BMR is chosen, the user will be given four options.

`Enter 1 for imperial (male), 2 for imperial (female), 3 for metric (male), or 4 for metric (female): `

A prompt will show what measurements need to be used (depending on what system they choose), along with prompts to enter height, weight, and age.

```
Height: Inches/Centimeters
Weight: Pounds/Kilograms

Enter height:
Enter weight:
Enter age:
```

Finally, the BMR results will be shown, along with a chart to match it to.

`Your BMR is <result number>`

DAILY ACTIVITY LEVEL                                                | CALORIES
------------------------------------------------------------------- | ---------------
Sedentary (little to no exercise in a day)                          |   <result number * 1.2>
Lightly Active (light exercise/sports 1-3 days/week)                |   <result number * 1.375>
Moderately Active (moderate exercise/sports 3-5 days/week)          |   <result number * 1.55>
Very Active (hard exercise/sports 6-7 days a week)                  |   <result number * 1.725>
Extremely Active (very hard exercise/sports and/or physical job)    |   <result number * 1.9>
