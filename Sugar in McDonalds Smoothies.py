import matplotlib.pyplot as plt
import numpy as np


with open("C:\\Users\\c\\Documents\\School\\Universiteit\\Data science en "
          "bio\Challenges\\7.4\\menu.csv") as menu:
    menu = menu.read()
menu = menu.split("\n")
splitmenu = []
for line in menu:
        splitmenu.append(line.split(','))

smoothieslist = []
for line in splitmenu:
    if line[0] == "Smoothies & Shakes":
        smoothieslist.append(line)


x_values = [entry[1] for entry in smoothieslist]
y_values = [int(entry[18]) for entry in smoothieslist]
y_pos = np.arange(len(x_values))


smoothiecolors = ["#852158", "#852158", "#852158", "#cf86ae", "#cf86ae",
                  "#cf86ae", "#d6aa1a", "#d6aa1a", "#d6aa1a", "#c9c2b3",
                  "#c9c2b3", "#c9c2b3", "#de90a6", "#de90a6", "#de90a6",
                  "#8c6d32", "#8c6d32", "#8c6d32", "#91c99c", "#91c99c",
                  "#c4060f", "#c4060f", "#c4060f", "#000000", "#000000",
                  "#000000", "#c4610a", "#c4610a"]

plt.barh(y_pos, y_values, align="center", alpha=0.5, color=smoothiecolors)

plt.title("Suikergehalte in Smoothies van de McDonalds")
plt.yticks(y_pos, x_values)
plt.xlabel("Suiker")

plt.show()

plt.savefig("Barchart suiker Smoothies.png")

