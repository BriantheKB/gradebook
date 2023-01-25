last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Gradebook code below: 
subjects = ["physics", "calculus","poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["Poetry", 85], ["history", 88]]
print(gradebook)

#Add new grades
gradebook.append(["computer science", 100])
gradebook.append(["visual arts",93])
print(gradebook)

#Modify a Grade +5 on visual arts
gradebook[-1][-1] = 98

#removing the grade value in visual arts
gradebook[5].remove(98)

#replace with pass/fail option
gradebook[5].append("Pass")
print(gradebook)

#combine multiple gradebooks
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

