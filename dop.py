              #Дополнительное практическое задание по модулю
gradess=[[5, 3, 3, 5, 4],[2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

student_list=sorted(students)

gradess_student=(sum(gradess[0])/len(gradess[0]),
                 sum(gradess[1])/len(gradess[1]),
                 sum(gradess[2])/len(gradess[2]),
                 sum(gradess[3])/len(gradess[3]),
                 sum(gradess[4])/len(gradess[4]))
gradess_student_dict=dict(zip(student_list,gradess_student))
print(gradess_student_dict)


