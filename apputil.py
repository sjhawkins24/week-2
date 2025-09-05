import numpy as np


# Exercise 1
#Start by creating a helper function that will get called from the main function 
def pennies_fill(n, nickels):
    '''Function will accept a goal number n, and the number of nickes and return the number of pennies to make up the goal'''
    remaining = n - 5*nickels
    return(remaining)
#Now the main function 
def ways(n): 
    '''Function calculates the number of ways you can make change for a given value n'''
    #Start by figuring out the max number of nickels 
    max_nickles = n // 5
    #Now loop through 0 through max nickles 
    options = []
    for n in range(max_nickles):
        options.append(ways(n))

    num_options = len(options) + 1 # We add the plus one to account for a no nickles option 

    return(num_options)
#Simpler ways function 
def ways_simple(n):
    '''Functin calculates the number of ways you can make change for a given n'''
    #The number of ways you can make change with nickels and pennies is just the 
    #number of times a nickel evenly goes into the total number plus one (since you don't have to have any nickels)
    max_nickels = n // 5 +1 
    return(max_nickels)

#Exercise 2

def lowest_score(names, scores): 
    '''Function that returns the name of the lowest scoring student'''
    #Get the lowest score
    min_score = np.argmin(scores)
    #Use that as a mask to get the name associated with the lowest score
    lowest_scorer = names[min_score]
    return(lowest_scorer)

def sort_names(names, scores): 
    '''Function that lists the name of students in decending order'''
    #Create an empty dictionary 
    scores_dict = {}
    #Use zip to create the dictionary 
    for names, scores in zip(names, scores):
        scores_dict[names] = scores
    #Now sort the dictionary by scores
    sorted_scores_dict = dict(sorted(scores_dict.items(), key=lambda item: item[1], reverse=True))
    return(sorted_scores_dict.keys())