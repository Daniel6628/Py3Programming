'''
The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
Find the total number of characters in the file and save to the variable num.
'''
with open('travel_plans.txt', 'r') as tra:
    lines = tra.read()
    num = len(lines)
    print(num)
    
'''
We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
Find the total number of words in the file and assign this value to the variable num_words.
'''
with open('emotion_words.txt', 'r') as emo:
    lines = emo.read()
    strings = lines.split()
    num_words = len(strings)
    print(num_words)
    
'''
Assign to the variable num_lines the number of lines in the file school_prompt.txt.
'''
with open('school_prompt.txt', 'r') as sch:
    lines = sch.readlines()
    num_lines = len(lines)
    print(num_lines)
    
'''
Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
'''
with open('school_prompt.txt', 'r') as sch:
    lines = sch.read()
    beginning_chars = lines[:30]
    print(beginning_chars)

'''
Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
'''
three = []
with open('school_prompt.txt', 'r') as sch:
    lines = sch.readlines()
    for i in lines:
        wrd = i.split()
        three.append(wrd[2])
    print(three)

'''
Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
'''
emotions = []
with open('emotion_words.txt', 'r') as emo:
    lines = emo.readlines()
    print(lines)
    for i in lines:
        wrd = i.split()
        emotions.append(wrd[0])
    print(emotions)
    
'''
Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
'''
with open('travel_plans.txt', 'r') as tra:
    chars = tra.read()
    first_chars = chars[:33]
    print(first_chars)

'''
Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
'''
p_words = []
with open('school_prompt.txt', 'r') as sch:
    lines = sch.readlines()
    for line in lines:
        wrds = line.split()
        for wrd in wrds:
            if not 'p' in wrd:
               continue
            p_words.append(wrd)
    print(p_words)
