import numpy as np
import pandas as pd

SUBJECTS = ["Math", "Physics", "Chemistry", "English", "Computer"]
PASS_MARK = 35          # minimum marks required in EVERY subject
MIN_ATTENDANCE = 75     # minimum attendance % (reported as a warning flag)


def load_data(file_path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def calculate_total_and_average(df, subjects=SUBJECTS):
    """Add Total and Average columns using NumPy (row-wise sums/means)."""
    marks = df[subjects].to_numpy()          # DataFrame -> NumPy 2D array
    df["Total"] = np.sum(marks, axis=1)
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df


def get_grade(average):
    """Grading rule based on the student's average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    return "F"


def assign_grades(df):
    """Loop through every student and assign a grade."""
    grades = []
    for avg in df["Average"]:
        grades.append(get_grade(avg))
    df["Grade"] = grades
    return df


def assign_pass_fail(df, subjects=SUBJECTS, pass_mark=PASS_MARK):
    """A student PASSES only if marks are >= pass_mark in every subject."""
    results = []
    for _, row in df.iterrows():
        if np.all(row[subjects].to_numpy() >= pass_mark):
            results.append("Pass")
        else:
            results.append("Fail")
    df["Result"] = results
    return df


def flag_low_attendance(df, minimum=MIN_ATTENDANCE):
    """Mark students whose attendance is below the required percentage."""
    df["LowAttendance"] = np.where(df["Attendance"] < minimum, "Yes", "No")
    return df


def class_statistics(df):
    """Highest, lowest and average performance of the whole class."""
    top = df.loc[df["Average"].idxmax()]
    low = df.loc[df["Average"].idxmin()]
    return {
        "highest_student": top["Name"],
        "highest_avg": top["Average"],
        "lowest_student": low["Name"],
        "lowest_avg": low["Average"],
        "class_avg": round(float(np.mean(df["Average"])), 2),
        "median_avg": round(float(np.median(df["Average"])), 2),
        "std_dev": round(float(np.std(df["Average"])), 2),
    }


def subject_analysis(df, subjects=SUBJECTS):
    """Average, highest, lowest and pass-count for each subject."""
    rows = []
    for subject in subjects:
        col = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(col)), 2),
            "Highest": int(np.max(col)),
            "Lowest": int(np.min(col)),
            "Passed": int(np.sum(col >= PASS_MARK)),
            "Failed": int(np.sum(col < PASS_MARK)),
        })
    return pd.DataFrame(rows)


def top_performers(df, n=5):
    """Return the top-n students ranked by average marks."""
    top = df.sort_values("Average", ascending=False).head(n)
    return top[["StudentID", "Name", "Department", "Total", "Average", "Grade"]]


def department_analysis(df):
    """Average marks and pass count per department."""
    summary = df.groupby("Department").agg(
        Students=("StudentID", "count"),
        AvgMarks=("Average", "mean"),
        AvgAttendance=("Attendance", "mean"),
        Passed=("Result", lambda r: (r == "Pass").sum()),
    ).round(2)
    return summary.reset_index()
