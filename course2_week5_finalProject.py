'''
Write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of 
retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how 
positive or negative each tweet is. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number 
of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry 
words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order.
'''

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
def strip_punctuation(astr1):
    for i in punctuation_chars:
        astr1 = astr1.replace(i, '')
    return astr1

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
def get_pos(astr2):
    ct = 0
    astr2 = astr2.lower()
    astr2 = astr2.split()
    for i in astr2:
        i = strip_punctuation(i)
        if i in positive_words:
            ct += 1
    return ct
 

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(astr3):
    ct = 0
    astr3 = astr3.lower()
    astr3 = astr3.split()
    for i in astr3:
        i = strip_punctuation(i)
        if i in negative_words:
            ct += 1
    return ct

with open('project_twitter_data.csv', 'r') as proj_twi:
    lines = proj_twi.readlines()[1:]
    ct = 0
    lst = []
    for lin in lines:
        lin = lin.strip()
        lst.append((int(lin.split(',')[1]), int(lin.split(',')[2]), get_pos(lin), get_neg(lin), get_pos(lin)-get_neg(lin)))
     
with open('resulting_data.csv', 'w') as result:
    result.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    result.write('\n')
    for n in lst:
        row_string = "{}, {}, {}, {}, {}".format(*n)
        result.write(row_string + '\n')
    print(row_string)
