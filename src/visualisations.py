import matplotlib.pyplot as plt

def plot_category_breakdown(account):
    #Draws a bar chart for every category for a given account

    breakdown = account.category_breakdown()
    x_category_axis =  list(breakdown.keys())
    y_category_axis = list(breakdown.values())


    plt.figure(figsize = (8,5)) #width and height of the canvas

    plt.bar(x_category_axis, y_category_axis, color = "skyblue", edgecolor = "black")

    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Breakdown of spending per category")
    plt.xticks(rotation = 45)   # rotates the bar headings by 45 degrees so they don't overlap
    plt.tight_layout()   #adjusts margins so no text is cut off

    plt.show()

