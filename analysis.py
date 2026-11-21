from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

folder = Path(__file__).parent
data = pd.read_csv(folder / "student_marks.csv")

subjects = ["Maths", "Science", "English"]
data["Average"] = data[subjects].mean(axis=1)
subject_averages = data[subjects].mean().sort_values(ascending=False)

print("\\nSTUDENT PERFORMANCE REPORT")
print("-" * 30)
print(data[["Name", "Average"]].to_string(
    index=False, formatters={"Average": "{:.2f}".format}
))

best = data.loc[data["Average"].idxmax()]
print(f"\\nHighest average: {best['Name']} ({best['Average']:.2f})")
print("\\nAverage marks by subject:")
print(subject_averages.round(2).to_string())

plt.figure(figsize=(7, 4))
subject_averages.plot(kind="bar")
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(folder / "subject_averages.png")
print("\\nChart saved as subject_averages.png")
