def for_each(items, function):
    """Give Python  list super powers with foreach.  FP"""
    for k, v in enumerate(items):
        function(k, v, items)


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades):
    for grade in grades:
        print(grade)


def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total


def grades_average(grades_list):
    sum_of_grades = grades_sum(grades_list)
    average = sum_of_grades / float(len(grades_list))
    return average


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2

    cnt = variance / float(len(scores))
    return cnt


print(grades_variance(grades))


def grades_std_deviation(variance):
    return variance**0.5


variance = grades_variance(grades)


print_grades(grades)
print(grades_sum(grades))
print(grades_average(grades))
print(grades_std_deviation(variance))


print("==" * 75)
for_each(grades, print)
