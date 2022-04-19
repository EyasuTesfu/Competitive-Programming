def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i]>37:
            if (grades[i]+1)%5==0:
                grades[i]+=1
            elif (grades[i]+2)%5==0:
                grades[i]+=2
    return grades
