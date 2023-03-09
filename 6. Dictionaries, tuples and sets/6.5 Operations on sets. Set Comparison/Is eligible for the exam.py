# A list of student grades is entered - his answers at the blackboard in the subject 'Informatics' in the form
# of numbers from 2 to 5 in one line separated by a space. If a student has at least one deuce, then he is
# not allowed to take the exam. Determine if the student is admitted based on the list entered.
# If allowed, then output the word ALLOWED, otherwise - NOT ALLOWED.
# When implementing the task, use the set to determine the presence of a two.

a = set(map(int, input('what grades did you have in school? ').split()))
print('ALLOWED' if 2 not in a else 'NOT ALLOWED')
