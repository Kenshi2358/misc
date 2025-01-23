
from typing import Union
from bisect import bisect


def calculate_grade(num_correct: int, num_incorrect: int) -> Union[int, str]:
    """
    Calculates the grade percentage based on num_correct and num_incorrect.
    Returns the percentage and the grade.
    """
    grade_percentage = 0
    if num_correct + num_incorrect > 0:
        grade_percentage = (num_correct / (num_correct + num_incorrect)) * 100

    grade_percentage = round(grade_percentage)

    all_grades = 'FDCBA'
    grade_string = all_grades[bisect([60, 70, 80, 90], grade_percentage)]

    return grade_percentage, grade_string


data_quality_grade_percentage, data_quality_grade = calculate_grade(21, 5)

print(f"Data Quality Grade Percentage: {data_quality_grade_percentage}")
print(f"Data Quality Grade: {data_quality_grade}")
