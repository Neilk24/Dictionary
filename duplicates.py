student_data = {'Id1':
                {'Name':['Sarah'],
                'Class':['V'],
                'Subject_Integration':['English', 'Math', 'Science']
                }, 
                'Id2':
                {'Name':['David'],
                'Class':['W'],
                'Subject_Integration':['English', 'Math', 'Science']
                }, 
                'Id3':
                {'Name':['Sarah'],
                'Class':['V'],
                'Subject_Integration':['English', 'Math', 'Science']
                }, 
                'Id4':
                {'Name':['Max'],
                'Class':['X'],
                'Subject_Integration':['English', 'Math', 'Science']
                }
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)