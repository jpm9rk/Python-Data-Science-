
# James Morrissey
# computingID: jpm9rk
# used students.csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('classic')

students = pd.read_csv('StudentsPerformance.csv')
students.index.name = 'student id'
students.columns = ['gender','race_or_ethnicity',
                    'parental_education_level','ate_lunch',
                    'test_prep_course','math_score','reading_score','writing _score']


def group_converter(string):
    """
    Return group name as single letter.

    :param string:(str) name of the group
    :return:(str) name of the group as a single letter
    """
    if 'A' in string:
        return 'A'
    if 'B' in string:
        return 'B'
    if 'C' in string:
        return 'C'
    if 'D' in string:
        return 'D'
    if 'E' in string:
        return 'E'
    return ''


students['race_or_ethnicity'] = students.race_or_ethnicity.apply(group_converter)
groupA = students[students.race_or_ethnicity == 'A']
groupB = students[students.race_or_ethnicity == 'B']
groupC = students[students.race_or_ethnicity == 'C']
groupD = students[students.race_or_ethnicity == 'D']
groupE = students[students.race_or_ethnicity == 'E']

# descriptive statistics for each racial group
a_sum = groupA.describe()
b_sum = groupB.describe()
c_sum = groupC.describe()
d_sum = groupD.describe()
e_sum = groupE.describe()

# math scores in particular for each racial group

print('GROUP A')
print(groupA.describe())
print('\n')
print('GROUP B')
print(groupB.describe())
print('\n')
print('GROUP C')
print(groupC.describe())
print('\n')
print('GROUP D')
print(groupD.describe())
print('\n')
print('GROUP E')
print(groupE.describe())
print('\n')

x = ['Group A', 'Group B', 'Group C', 'group D', 'group E']
y = [a_sum.math_score['mean'],b_sum.math_score['mean'],c_sum.math_score['mean'],
     d_sum.math_score['mean'],e_sum.math_score['mean']]
plt.bar(x, y)
plt.xlabel('Racial/Ethnic Group')
plt.ylabel('Mean Math Score')
plt.title('Mean Math Scores by Racial/Ethnic Group')
plt.show()
