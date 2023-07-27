from tkinter import *

# Window
window = Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=300)
window.config(padx=20, pady=20)

def calculate_bmi():
    try:
        user_weight = float(user_weight_entry.get())
        user_height = float(user_height_entry.get())

        # Converting height to meters
        user_height_in_meters = user_height / 100

        # BMI Calculator Formule
        bmi = user_weight / (user_height_in_meters ** 2)

        # Determining the status
        if bmi < 18.5:
            status = "Zayıf"
        elif 18.5 <= bmi < 24.9:
            status = "Normal Kilolu"
        elif 24.9 <= bmi < 29.9:
            status = "Fazla Kilolu"
        else:
            status = "Obez"

        # Print the result to the screen
        result_label.config(text=f"Body Mass Index (BMI): {bmi:.2f}\nStatus: {status}")
    except ValueError:
        result_label.config(text="You have entered incorrectly.")

# Getting Weight from User
weight_label = Label(text="Enter Your Weight (kg)", font="Arial, 12", pady=10)
weight_label.pack()

user_weight_entry = Entry()
user_weight_entry.pack()

# Getting Height from User
height_label = Label(text="Enter Your Height (cm)", font="Arial, 12", pady=10)
height_label.pack()

user_height_entry = Entry()
user_height_entry.pack()

# Calculate Button
calculate_bmi = Button(text="Calculate", pady=5, padx=5, command=calculate_bmi)
calculate_bmi.pack(pady=10)

# Result
result_label = Label(text="", font="Arial, 12", pady=10)
result_label.pack()

window.mainloop()