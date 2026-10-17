"""Student Performance Analytics System"""

import pandas as pd
import functions as fn

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)


def heading(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():     # Step 1 & 2: Load and inspect the data
    df = fn.load_data("students.csv")
    heading("1. DATASET OVERVIEW")
    print(f"Records : {df.shape[0]}")
    print(f"Columns : {list(df.columns)}")
    print("\nFirst 5 records:")
    print(df.head())
    print("\nMissing values:", int(df.isnull().sum().sum()))

    # Step 3: Process the data
    df = fn.calculate_total_and_average(df)
    df = fn.assign_grades(df)
    df = fn.assign_pass_fail(df)
    df = fn.flag_low_attendance(df)

    heading("2. STUDENT RESULTS (Total, Average, Grade, Result)")
    print(df[["StudentID", "Name", "Department", "Total", "Average",
              "Grade", "Result", "Attendance"]].to_string(index=False))

    # Step 4: Analysis
    stats = fn.class_statistics(df)
    heading("3. CLASS PERFORMANCE")
    print(f"Highest average : {stats['highest_student']} ({stats['highest_avg']})")
    print(f"Lowest average  : {stats['lowest_student']} ({stats['lowest_avg']})")
    print(f"Class average   : {stats['class_avg']}")
    print(f"Median average  : {stats['median_avg']}")
    print(f"Std deviation   : {stats['std_dev']}")

    heading("4. PASS / FAIL STATISTICS")
    counts = df["Result"].value_counts()
    passed, failed = counts.get("Pass", 0), counts.get("Fail", 0)
    print(f"Passed : {passed}")
    print(f"Failed : {failed}")
    print(f"Pass percentage : {round(passed / len(df) * 100, 2)}%")
    print("\nFailed students:")
    print(df[df["Result"] == "Fail"][["Name", "Department", "Average"]]
          .to_string(index=False))

    heading("5. GRADE DISTRIBUTION")
    order = ["A+", "A", "B", "C", "D", "E", "F"]
    print(df["Grade"].value_counts().reindex(order, fill_value=0).to_string())

    heading("6. SUBJECT-WISE ANALYSIS")
    subj = fn.subject_analysis(df)
    print(subj.to_string(index=False))
    best = subj.loc[subj["Average"].idxmax()]
    worst = subj.loc[subj["Average"].idxmin()]
    print(f"\nBest subject  : {best['Subject']} (avg {best['Average']})")
    print(f"Weakest subject: {worst['Subject']} (avg {worst['Average']})")

    heading("7. TOP 5 PERFORMERS")
    print(fn.top_performers(df, 5).to_string(index=False))

    heading("8. DEPARTMENT-WISE ANALYSIS")
    print(fn.department_analysis(df).to_string(index=False))

    heading("9. LOW ATTENDANCE (below 75%)")
    low = df[df["LowAttendance"] == "Yes"]
    print(low[["Name", "Department", "Attendance", "Result"]].to_string(index=False))

    # Save the processed results
    df.to_csv("results.csv", index=False)
    print("\nProcessed data saved to results.csv")


if __name__ == "__main__":
    main()
