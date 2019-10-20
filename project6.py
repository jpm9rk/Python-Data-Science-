
# James Morrissey


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
plt.style.use('classic')


pd.options.mode.chained_assignment = None
grades = pd.read_csv('StudentsPerformance.csv')
grades.columns = ['gender', 'race', 'parental_level_of_education', 'lunch',
       'test_preparation_course', 'math_score', 'reading_score',
       'writing_score']

# Separate math data by racial group
groupA = grades[grades.race == 'group A']
groupB = grades[grades.race == 'group B']
groupC = grades[grades.race == 'group C']

# Statistics to be used later regarding each group
A_english_avg = groupA.writing_score.mean()
B_english_avg = groupB.writing_score.mean()
C_english_avg = groupC.writing_score.mean()
A_eng_std = groupA.writing_score.std()
B_eng_std = groupB.writing_score.std()
C_eng_std = groupC.writing_score.std()

A_reading_avg = groupA.reading_score.mean()
B_reading_avg = groupB.reading_score.mean()
C_reading_avg = groupC.reading_score.mean()
A_reading_std = groupA.reading_score.std()
B_reading_std = groupB.reading_score.std()
C_reading_std = groupC.reading_score.std()


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
        :param num_sample_obs: (int) number of observations in the sample
        :return: (pd.DataFrame) simulated DataFrame
        """
        return pd.DataFrame({'grade': np.where(np.random.rand(num_sample_obs) < failed_proportion,
                                               'failed', 'passed')})


def sampling_distribution(failed_proportion,num_sample_obs):
        """
        Return 1000 simulated pass/fail proportions for sample of indicated size
        :param failed_proportion:(float) observed failure proportion
        :param num_sample_obs:(int) number of observations in the sample
        :return:(pd.DataFrame) DataFrame of simulated values
        """
        return pd.DataFrame([sample(failed_proportion,
                                    num_sample_obs).grade.value_counts(normalize=True) for i in range(1000)])


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
distributionA = pd.DataFrame([sample(A_proportion_failed,
                                     len(groupA)).grade.value_counts(normalize=True) for i in range(1000)])
distributionA.failed.hist(histtype='step', bins=20)
axA = plt.gca()
axA.set_xlabel('Proportion of Students that Failed')
axA.set_ylabel('Frequency')
axA.set_title('Simulation of Student Math Failure Proportion for Group A')
plt.show()

# Plot the histogram for proportion of students from groupB that pass
distributionB = pd.DataFrame([sample(B_proportion_failed,
                                     len(groupB)).grade.value_counts(normalize=True) for i in range(1000)])
distributionB.failed.hist(histtype='step', bins=20)
axB = plt.gca()
axB.set_xlabel('Proportion of Students that Failed')
axB.set_ylabel('Frequency')
axB.set_title('Simulation of Student Math Failure Proportion for Group B')
plt.show()

# Plot the histogram for proportion of students from groupC that pass
distributionC = pd.DataFrame([sample(C_proportion_failed,
                                     len(groupC)).grade.value_counts(normalize=True) for i in range(1000)])
distributionC.failed.hist(histtype='step', bins=20)
axC = plt.gca()
axC.set_xlabel('Proportion of Students that Failed')
axC.set_ylabel('Frequency')
axC.set_title('Simulation of Student Math Failure Proportion for Group C')
plt.show()

print('95% Confidence interval for the proportion of students from group A that fail the math test:')
print(quantiles(A_proportion_failed, len(groupA)))
print('\n')
print('95% Confidence interval for the proportion of students from group B that fail the math test:')
print(quantiles(B_proportion_failed, len(groupB)))
print('\n')
print('95% Confidence interval for the proportion of students from group C that fail the math test:')
print(quantiles(C_proportion_failed, len(groupC)))


# Determine 95% confidence interval for the average score for each subject for each racial group

def confidence_int_95(avg, std, size):
        """
        Return 95% confidence interval.
        :param avg: (float)
        :param std: (float)
        :param size: (int)
        :return: (tuple) 95% confidence interval
        """
        return (avg - 1.96 * std/math.sqrt(size),
                avg + 1.96 * std/math.sqrt(size))


# The number of score entries for each racial group is greater than 30,
# so the central limit theorem is applicable with regards to the
# avg score for each subject. avg score for a subject

A_writing_interval = confidence_int_95(A_english_avg, A_eng_std, len(groupA))
B_writing_interval = confidence_int_95(B_english_avg, B_eng_std, len(groupB))
C_writing_interval = confidence_int_95(C_english_avg, C_eng_std, len(groupC))

A_reading_interval = confidence_int_95(A_reading_avg, A_reading_std, len(groupA))
B_reading_interval = confidence_int_95(B_reading_avg, B_reading_std, len(groupB))
C_reading_interval = confidence_int_95(C_reading_avg, C_reading_std, len(groupC))

# For sake of clarity of output, the print statements for the intervals will be commented out.
# To see the confidence intervals uncomment the following block
# print('95% confidence interval for groupA average writing score:', A_writing_interval)
# print('95% confidence interval for groupA average writing score:', B_writing_interval)
# print('95% confidence interval for groupA average writing score:', C_writing_interval)
#
# print('95% confidence interval for groupA average reading score:', A_reading_interval)
# print('95% confidence interval for groupA average reading score:', B_reading_interval)
# print('95% confidence interval for groupA average reading score:', C_reading_interval)


# What follows is computing the confidence interval for average
# math scores for group A using bootstrapping method


def sample_bootstrap(dataframe, num_values,subject_score):
    """
    Return simulated dataframe of scores for indicated subject
    :param dataframe: (pd.DataFrame) dataframe to sample from
    :param num_values: (int) number of values to sample
    :param subject_score: (str) the subject scores desired
    :return: (pd.DataFrame)
    """
    return pd.DataFrame(dataframe[subject_score].sample(n=num_values,replace=True))


bootstrapA = pd.DataFrame({'mean_math_grade': [sample_bootstrap(groupA, len(groupA), 'math_score').mean()
                           for i in range(1000)]})
bootstrapB = pd.DataFrame({'mean_math_grade': [sample_bootstrap(groupB, len(groupB), 'math_score').mean()
                           for i in range(1000)]})
bootstrapC = pd.DataFrame({'mean_math_grade': [sample_bootstrap(groupC, len(groupC), 'math_score').mean()
                           for i in range(1000)]})

A_confidence_interval = (bootstrapA.quantile(0.025), bootstrapA.quantile(0.975))
B_confidence_interval = (bootstrapB.quantile(0.025), bootstrapB.quantile(0.975))
C_confidence_interval = (bootstrapC.quantile(0.025), bootstrapC.quantile(0.975))












