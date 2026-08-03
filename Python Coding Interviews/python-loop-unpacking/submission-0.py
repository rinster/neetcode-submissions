from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    # save best student
    curr_best_student = scores[0]

    #loop throught the list for each student
    for student, score in scores:
        if score > curr_best_student[1]:
            curr_best_student = [student, score]
        # compare curre student with curr best - if better than best, replace bext with curre student
    return curr_best_student[0]
    
    #return best student




# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
