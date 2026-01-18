from typing import Callable, Dict, Any


def grade_function(score: int) -> str:
    if score > 80:
        return "A"
    elif score > 70:
        return "A-"
    elif score > 60:
        return "B"
    elif score > 50:
        return "B-"
    elif score > 40:
        return "C"
    elif score > 30:
        return "C-"


def pass_function(score: int) -> bool:
    if score >= 30:
        return True
    else:
        return False


def make_grade_processor(pass_func: Callable[[int], bool], grade_func: Callable[[int], str]) -> Callable[[Dict[str, int]], Dict[str, Any]]:
    def processor(students: Dict[str, int]) -> Dict[str, Any]:
        passed_students = list(
            filter(lambda item: pass_func(item[1]), students.items()))
        failed_students_filtered = list(map(lambda object: object[0], filter(
            lambda item: not pass_func(item[1]), students.items())))
        passed_students_with_grades = dict(
            map(lambda item: (item[0], grade_func(item[1])), passed_students))
        return {
            "PASSED": passed_students_with_grades,
            "FAILED": failed_students_filtered
        }
    return processor


if __name__ == "__main__":
    students = {
        " Alice ": 85,
        "Bob": 62,
        " Charlie ": 27,
        " David ": 73,
        "Eve": 48,
        " Frank ": 35
    }
    # Create processor using the higher - order function
    grade_processor = make_grade_processor(pass_function, grade_function)
    # Process and print results
    result = grade_processor(students)
    print(result)
