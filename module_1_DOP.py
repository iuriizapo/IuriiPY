grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
sredny_grades_0 = sum(grades[0])/len(grades[0])
sredny_grades_1 = sum(grades[1])/len(grades[1])
sredny_grades_2 = sum(grades[2])/len(grades[2])
sredny_grades_3 = sum(grades[3])/len(grades[3])
sredny_grades_4 = sum(grades[4])/len(grades[4])
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
spisok_students = sorted(list(students))
itog = [(spisok_students[0],sredny_grades_0),(spisok_students[1],sredny_grades_1),(spisok_students[2],sredny_grades_2),(spisok_students[3],sredny_grades_3),(spisok_students[4],sredny_grades_4)]
print(dict(itog))