def average_grade(grades_list: list) -> float:
    """
    Gets a list of grades, and return the average grade.
    """
    total = 0
    num_grades = len(grades_list)
    for grade in grades_list:
        total += grade
    return total / num_grades


def highest_grade(grade_list: list) -> list:
    """
    Gets a list of grades, and returns the highest grade. If there
    are two equal highest grades, it returns any of them.
    """
    sorted_grades = sorted(grade_list, reverse=True)
    return sorted_grades[0]


def failing_grades(grade_list: list) -> int:
    """
    Gets a list of grades, and returns how many failing grades there are.
    A grade is a failing grade if it 55 or below.
    """
    num_fail = 0
    for grade in grade_list:
        if grade <= 55:
            num_fail += 1
    return num_fail


def perfect_grade(grade_list: list) -> bool:
    """
    Gets a list of grades, and returns True if there is at least one
    perfect (100) grade, and False otherwise.
    """
    for grade in grade_list:
        if grade == 100:
            return True
    return False


def main():
    grades = [55, 90, 66, 100, 92, 76, 85]

    print(f"The list of grades: {grades}")
    print(f"Average grade: {average_grade(grades) :.2f}")
    print(f"Highest grade: {highest_grade(grades)}")
    print(f"Number of failing grades: {failing_grades(grades)}")
    print(f"Perfect grade exist: {perfect_grade(grades)}")


if __name__ == "__main__":
    main()
