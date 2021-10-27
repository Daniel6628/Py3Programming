'''
Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. 
The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
'''
def sublist(lst):
    sub_lst = []
    idx = 0
    while idx < len(lst) and lst[idx] != 5:
        sub_lst.append(lst[idx])
        idx += 1
    return sub_lst
  
  
  '''
  Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. 
  The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
  '''
  def sublist(astr):
    sub_lst = []
    idx = 0
    while astr[idx] != 'STOP':
        sub_lst.append(astr[idx])
        idx += 1
    return sub_lst

  
  '''
  Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. 
  What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. 
  If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing
  '''
  #Method 1: 
  def beginning(lst):
    sub_lst = []
    idx = 0
    while lst[idx] != 'bye':
        sub_lst.append(lst[idx])
        idx += 1
    if len(sub_lst) > 10:
        sub_lst = sub_lst[:10]
    return sub_lst
  
  #Method 2:
  def beginning(lst):
    sub_lst = []
    idx = 0
    while lst[idx] != 'bye' and len(sub_lst) < 10:
        sub_lst.append(lst[idx])
        idx += 1
    return sub_lst
