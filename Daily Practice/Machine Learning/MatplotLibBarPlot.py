import matplotlib.pyplot as plt

def main ():
    langauge = ["C", "C++", "Java", "Python"]
    students = [30, 40, 35, 55]

    plt.bar(
        langauge,
        students,
        width = 0.6,                # width of bar
        edgecolor = "black",        # border color for bars
        linewidth = 1,              # width of bar border
        alpha = 0.8,                # transparency 0.0 to 1.0
        label = "Students"          # legend text
    )

    plt.title("Student Bar Plot")
    plt.xlabel("Langauge")
    plt.ylabel("Number of Students")
    plt.legend()
    plt.show()

    
if __name__ == "__main__":
    main()