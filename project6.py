# James Morrissey


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import io
import scipy.stats
import scipy.optimize
import scipy.spatial

pd.options.mode.chained_assignment = None
grades = pd.read_csv('StudentsPerformance.csv')
grades.columns = ['gender', 'race', 'parental_level_of_education', 'lunch',
       'test_preparation_course', 'math_score', 'reading_score',
       'writing_score']

# Separate math data by racial group
groupA = grades[grades.race == 'group A']
groupB = grades[grades.race == 'group B']
groupC = grades[grades.race == 'group C']


def passing_grade(grade):
       """
       Return 1 if student passed, 0 if not
       :param grade: (int)
       :return: (int)
       """
       if grade >= 70:
              return 1
       return 0


# Create new column to indicate if the student has a passing math grade
groupA['passed_math'] = groupA.math_score.apply(passing_grade)
groupB['passed_math'] = groupB.math_score.apply(passing_grade)
groupC['passed_math'] = groupC.math_score.apply(passing_grade)
groupAmath = groupA[['math_score', 'passed_math']]
groupBmath = groupB[['math_score', 'passed_math']]
groupCmath = groupC[['math_score', 'passed_math']]
A_proportion_failed = 1 - groupAmath.passed_math.sum()/len(groupAmath.passed_math)
B_proportion_failed = 1 - groupBmath.passed_math.sum()/len(groupBmath.passed_math)
C_proportion_failed = 1 - groupCmath.passed_math.sum()/len(groupCmath.passed_math)


def sample(failed_proportion, num_sample_obs):
        """
        Return a simulated data frame of passing/failing math grades for groupA.
        :param failed_proportion: (float) observed sample proportion of failure
        :param n: (int) number of observations in the sample
        :return: (pd.DataFrame) simulated DataFrame
        """
        return pd.DataFrame({'grade': np.where(np.random.rand(num_sample_obs) < failed_proportion,
                                               'failed','passed')})


def sampling_distribution(failed_proportion,num_sample_obs):
        """
        Return 1000 simulated pass/fail proportions for sample of indicated size
        :param failed_proportion:(float) observed failure proportion
        :param n:(int) number of observations in the sample
        :return:(pd.DataFrame) DataFrame of simulated values
        """
        return pd.DataFrame([sample(failed_proportion,num_sample_obs).grade.value_counts(normalize=True) for i in range(1000)])


def quantiles(failed_proportion, num_sample_obs):
       """
       Return the 2.5% and 97.5% quantile values
       :param failed_proportion:(float) observed proportion of failure
       :param n:(int) number of observations in the sample
       :return:(tuple) tuple indicating bounds of 95% confidence interval for failure proportion
       """
       distribution = sampling_distribution(failed_proportion,num_sample_obs)
       return distribution.failed.quantile(0.025), distribution.failed.quantile(0.975)


# Generate a simulated sample for proportion of students that fail the math test
a_sample = sample(A_proportion_failed, len(groupA))
b_sample = sample(B_proportion_failed, len(groupB))
c_sample = sample(C_proportion_failed, len(groupC))

# Plot the histogram for proportion of students from groupA that pass
distributionA = pd.DataFrame([sample(A_proportion_failed,len(groupA)).grade.value_counts(normalize=True) for i in range(1000)])
distributionA.failed.hist(histtype='step',bins=20)
axA = plt.gca()
axA.set_xlabel('Proportion of Students that Failed')
axA.set_ylabel('Frequency')
axA.set_title('Simulation of Student Math Failure Proportion for Group A')
plt.show()

# Plot the histogram for proportion of students from groupB that pass
distributionB = pd.DataFrame([sample(B_proportion_failed,len(groupB)).grade.value_counts(normalize=True) for i in range(1000)])
distributionB.failed.hist(histtype='step',bins=20)
axB = plt.gca()
axB.set_xlabel('Proportion of Students that Failed')
axB.set_ylabel('Frequency')
axB.set_title('Simulation of Student Math Failure Proportion for Group B')
plt.show()

# Plot the histogram for proportion of students from groupC that pass
distributionC = pd.DataFrame([sample(C_proportion_failed,len(groupC)).grade.value_counts(normalize=True) for i in range(1000)])
distributionC.failed.hist(histtype='step',bins=20)
axC = plt.gca()
axC.set_xlabel('Proportion of Students that Failed')
axC.set_ylabel('Frequency')
axC.set_title('Simulation of Student Math Failure Proportion for Group C')
plt.show()

print('95% Confidence interval for the proportion of students from group A that fail the math test:')
print(quantiles(A_proportion_failed,len(groupA)))
print('\n')
print('95% Confidence interval for the proportion of students from group B that fail the math test:')
print(quantiles(B_proportion_failed,len(groupB)))
print('\n')
print('95% Confidence interval for the proportion of students from group C that fail the math test:')
print(quantiles(C_proportion_failed,len(groupC)))

