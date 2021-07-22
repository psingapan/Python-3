
##Problem 1: There are 5 students in a class who have taken a test and received scores as follow. Tom got a 75.
##Joe Got a 65. Alice got an 85. Bob got a 45. Jane got a 99. Create two lists, names and scores, to
##hold this information.

student_names=['Tom','Joe','Bob','Alice','Jane']
student_scores=[75,65,45,85,99]

##Problem 2:Create a function make_score_dict. The function has two parameters: names and scores, both
##of which are lists. It returns a dictionary in which the keys are the names and the values are the
##scores. Test your function with the names and scores you create in Problem 1. Print the dictionary
##returned by the function. You should have named the returned dictionary score_dict.
score_dict={}
for keys in student_names:
    for scores in student_scores:
        score_dict[keys] =scores
        student_scores.remove(scores)
        break
score_dict

##Problem 3:Using score_dict, find the score for Joe.
print(score_dict['Joe'])

##Problem 4: Oops, we forgot Ralph. Add him to the dictionary with a score of 80 and display the result.

score_dict['Ralph']=80
print(score_dict)

##Problem 5:Oops again!! Bob’s score was supposed to be 75. Fix that in the doctionary and display the result.
score_dict['Bob']=75
print(score_dict['Bob'])

##Problem 6: I regret to inform you that our best student, Jane has dropped the class. Delete her from the
##dictionary and display the result.
score_dict.pop('Jane',99)

score_dict