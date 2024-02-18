import tkinter as tk

def fahrenheit_to_celcius():
    fahrenheit = entryTemp.get()
    celcius = (5 / 9) * (float(fahrenheit) - 32)
    resultLabel["text"] = f"{(round(celcius, 2))} \N{DEGREE CELSIUS}"

window = tk.Tk()
window.title("Temperature Converter Using tkinter")
window.resizable(width=False, height=False)

entryFrame = tk.Frame(master=window)
entryTemp = tk.Entry(master=entryFrame, width=10)
entryLabel = tk.Label(master=entryFrame, text="\N{DEGREE FAHRENHEIT}")

entryTemp.grid(row=0, column=0, sticky="e")
entryLabel.grid(row=0, column=1, sticky="w")

convertButton = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celcius
)

resultLabel = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

entryFrame.grid(row=0, column=0, padx=10)
convertButton.grid(row=0, column=1, pady=10)
resultLabel.grid(row=0, column=2, padx=10)

window.mainloop()