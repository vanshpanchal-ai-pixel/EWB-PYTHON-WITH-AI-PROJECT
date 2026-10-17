# 1. Project Title
**Student Performance Analytics System**

- **Student Name:** <YOUR NAME>
- **Course:** Python with AI – EWB Courses
- **Submission Date:** <DATE> (Deadline: 15 October 2026)

---

# 2. Objective
Teachers often have raw marks for many students and need to quickly understand
how the class is performing. This project reads student records and automatically
calculates totals, averages, grades, pass/fail status, subject-wise performance,
department-wise performance and the top performers, so the results can be
understood without checking the marks manually.

# 3. Technologies Used
- **Python 3** – core logic (functions, loops, conditions)
- **NumPy** – numerical calculations (sum, mean, median, std, max, min, conditions)
- **Pandas** – loading the CSV, DataFrame operations, sorting, grouping

# 4. Dataset Description
`students.csv` contains **20 student records** with these columns:

| Column | Description |
|---|---|
| StudentID | Unique ID (S001–S020) |
| Name | Student name |
| Department | CSE, ECE or ME |
| Math, Physics, Chemistry, English, Computer | Subject marks out of 100 |
| Attendance | Attendance percentage |

# 5. Implementation (Step by Step)
1. **Load data** – `load_data()` reads `students.csv` into a Pandas DataFrame; the
   program prints record count, columns, first rows and missing values.
2. **Total & average** – `calculate_total_and_average()` converts the marks columns to a
   NumPy array and uses `np.sum` / `np.mean` with `axis=1` (row-wise).
3. **Grades** – `get_grade()` applies the grading rule below; `assign_grades()` loops
   over every student's average.
4. **Pass/Fail** – `assign_pass_fail()` loops through each student; a student passes only
   if marks are **≥ 35 in every subject** (checked with `np.all`).
5. **Attendance** – `flag_low_attendance()` uses `np.where` to flag attendance below 75%.
6. **Class statistics** – `class_statistics()` finds highest, lowest, mean, median and
   standard deviation of averages.
7. **Subject analysis** – `subject_analysis()` loops over subjects and computes average,
   highest, lowest, passed and failed counts.
8. **Top performers & departments** – `top_performers()` sorts by average;
   `department_analysis()` uses `groupby`.
9. **Output** – `main.py` prints all results in clear sections.

**Grading rule (based on average marks)**

| Average | Grade |
|---|---|
| 90 and above | A+ |
| 80 – 89.99 | A |
| 70 – 79.99 | B |
| 60 – 69.99 | C |
| 50 – 59.99 | D |
| 40 – 49.99 | E |
| Below 40 | F |

# 6. Key Features
- Reusable functions in `functions.py`
- Row-wise NumPy calculations
- Clearly defined grading and pass/fail rules
- Highest / lowest / average class performance
- Subject-wise and department-wise analysis
- Top 5 performers list
- Low-attendance report

# 7. Output
Run the project:
```bash
pip install -r requirements.txt
python main.py
```
Key results from the sample dataset:

```
Highest average : Ananya Singh (92.8)
Lowest average  : Manish Tiwari (37.0)
Class average   : 68.18
Passed : 18   Failed : 2   Pass percentage : 90.0%
Best subject    : English (avg 71.3)
Weakest subject : Physics (avg 65.95)
```
*(Add screenshots of your terminal output here.)*

# 8. Final Outcome
The project successfully analyses a 20-student dataset and answers the key questions:
who scored highest, which subject is strongest, how many students passed, and what the
overall class average is. The output is readable without inspecting the code.

# 9. Challenges & Learning
- *Challenge:* Deciding a fair pass condition. *Solution:* Used "35+ in every subject".
- *Challenge:* Combining loops with NumPy. *Solution:* Used loops for per-student logic and
  NumPy for fast numeric operations.
- *Learning:* Structuring code into reusable functions, using `axis=1` in NumPy, and
  using Pandas `groupby` and sorting.

# 10. GitHub Repository
<PASTE YOUR GITHUB REPOSITORY LINK HERE>

---

## Project Structure
```
student-performance-analytics/
├── main.py           # runs the analysis and prints output
├── functions.py      # reusable calculation functions
├── students.csv      # dataset
├── requirements.txt
└── README.md         # documentation
```
