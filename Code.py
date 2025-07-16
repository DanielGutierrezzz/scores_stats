import numpy as np

# 🔹 Load ONLY the exam scores (columns 2, 3, 4) and skip the name columns and header row
def load_grades(filename):
    return np.loadtxt(filename, delimiter=',', skiprows=1, usecols=(2, 3, 4))

# 🔹 Show statistics for each exam column
def column_statistics(data):
    num_exams = data.shape[1]
    for i in range(num_exams):
        col = data[:, i]
        print(f"\nExam {i + 1} Statistics:")
        print(f"  Mean: {np.mean(col):.2f}")
        print(f"  Median: {np.median(col):.2f}")
        print(f"  Standard Deviation: {np.std(col):.2f}")
        print(f"  Minimum: {np.min(col):.2f}")
        print(f"  Maximum: {np.max(col):.2f}")

# 🔹 Show statistics across ALL exams combined
def overall_statistics(data):
    flat = data.flatten()
    print("\nOverall Statistics (All Exams Combined):")
    print(f"  Mean: {np.mean(flat):.2f}")
    print(f"  Median: {np.median(flat):.2f}")
    print(f"  Standard Deviation: {np.std(flat):.2f}")
    print(f"  Minimum: {np.min(flat):.2f}")
    print(f"  Maximum: {np.max(flat):.2f}")

# 🔹 Calculate pass/fail per exam and overall percentage
def pass_fail_stats(data, passing_score=60):
    num_exams = data.shape[1]
    num_students = data.shape[0]
    total_passes = 0
    total_scores = num_exams * num_students

    for i in range(num_exams):
        exam_scores = data[:, i]
        passed = np.sum(exam_scores >= passing_score)
        failed = np.sum(exam_scores < passing_score)
        total_passes += passed
        print(f"\nExam {i + 1}:")
        print(f"  Passed: {passed}")
        print(f"  Failed: {failed}")

    pass_percentage = (total_passes / total_scores) * 100
    print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")

# 🔹 Main function
def main():
    filename = "grades.csv"  # Make sure this file exists in the same folder
    data = load_grades(filename)

    print("First few rows of exam scores:")
    print(data[:5])  # Show first 5 rows (if available)

    column_statistics(data)
    overall_statistics(data)
    pass_fail_stats(data)

# 🔹 Run the main program
if __name__ == "__main__":
    main()
