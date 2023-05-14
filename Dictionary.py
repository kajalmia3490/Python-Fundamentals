# Dictionary is a few set of element and every element structured mix key-value pairing.
# For example: 
student_Id = {
    'name': 'Tamim',
    'roll': 677805,
    'Dept.': 'Computer',
    'Section': 'A',
    'Shift': 'Second',
    'Aim': 'Blockchain Developer'
}
student_Id.pop('Section')
student_Id['Address'] = 'Chandpur'
print(student_Id)
print(student_Id['Aim'])