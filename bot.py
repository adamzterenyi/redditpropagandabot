import praw
import random
import datetime
import time
import argparse

# arguments for running multiple bots
parser = argparse.ArgumentParser(description='Specify which bot in the terminal')
parser.add_argument('--username', default = 'hubertbotguy')
args = parser.parse_args()
print('you are working with', args.username)

# to avoid mistakes matching praw name with username
if args.username == 'hubertbotguy':
    bot = 'bot'
if args.username == 'hubertbotgaming':
    bot = 'bot2'
if args.username == 'hubertbotgorbachev':
    bot = 'bot3'
if args.username == 'hubertbotgal':
    bot = 'bot4'
if args.username == 'hubertbotgame':
    bot = 'bot5'

# FIXME:
# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "I [LOVE] [TULSI GABBARD]... you [LOVE] [TULSI GABBARD]... we all [LOVE] [TULSI GABBARD]!!!",
    "[TULSI GABBARD] is [INCREDIBLY] [SANE] and [TRUTHFUL]. We [SHOULD] trust her with our votes and [SUPPORT] her!",
    "[TULSI GABBARD] should run for [THE PRESIDENT OF THE UNITED STATES]. Her campaign would not only be [EPIC], but [BASED], as well. As a result, I would have no [CHOICE] but to support her!",
    "[TULSI GABBARD] is a [FAMILY WOMAN]. She [LOVES] babies and [CHILDREN]. She [HATES] [MEANIES].",
    "[TULSI GABBARD] is not a [POPULIST]. She [HATES] [MEANIES]; she makes us feel [ONE], standing against the [WORLD].",
    "I will vote for [TULSI GABBARD] [SEVERAL] and commit voter fraud, which is a [FELONY]. I will do this because [TULSI GABBARD] will make our elections [SECURE].",
    ]

replacements = {
    'TULSI GABBARD' : ['Tulsi Gabbard', 'Sarah Huckabee Sanders', 'Kari Lake'],
    'INCREDIBLY' : ['incredibly', 'genuinely', 'truly', 'definitely', 'of course,'],
    'SANE' : ['sane', 'mentally stable'],
    'TRUTHFUL'  : ['truthful', 'honest', 'emanates ridiculous amounts of responsibility and capability--so much so, that I have no choice but to support her'],
    'SUPPORT' : ['support', 'advocate for', 'stand with'],
    'LOVE' : ['love', 'like', 'particularly like', 'accept'],
    'THE PRESIDENT OF THE UNITED STATES' : ['the President of the United States', 'president', 'the presidency'],
    'SHOULD' : ['should', 'must', 'need to'],
    'FAMILY WOMAN' : ['family woman', 'family-oriented person'],
    'EPIC' : ['epic', 'amazing', 'really dope', 'the best thing ever'],
    'BASED' : ['based', 'truly otherwordly', 'stellar'],
    'CHOICE' : ['choice', 'option'],
    'CHILDREN' : ['children', 'the nuclear family', 'conservatism and Trump'],
    'LOVES' : ['loves', 'cares for', 'deeply supports'],
    'HATES' : ['hates', 'abhors', 'dislikes', 'is animose towards'],
    'MEANIES' : ['illegals', 'meanies', 'the woke mob', 'the left', 'the libs', 'the dems', 'Peter Griffin of Family Guy'],
    'POPULIST' : ['populist', 'dog whistler', 'likely opportunist'],
    'ONE' : ['as one', 'together', 'as a homogeneously yet loosely defined "in group"'],
    'WORLD' : ['world', 'enemy', 'communists'],
    'SEVERAL' : ['several times', 'more than once', 'hundreds of times', 'incessantly (by voting in multiple counties)'],
    'FELONY' : ['felony', 'crime', 'definitely illegal act'],
    'SECURE' : ['secure', 'fair'],
    }

def generate_comment():
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
            madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
    return madlib

# FIXME:
# connect to reddit 
reddit = praw.Reddit(bot)

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.
submission_url = 'https://old.reddit.com/r/cs40_2022fall/comments/z6mr7i/life_in_the_us_isnt_what_these_afghans_expected/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:
    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    submission.comments.replace_more(limit=None)
    all_comments = []
    for comment in submission.comments.list():
        all_comments.append(comment)
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if comment.author.name != 'hubertbotguy':
            not_my_comments.append(comment)
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        print(datetime.datetime.now(), ': made a comment')
        submission.reply(generate_comment())
    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        
        # procedure for random replying
        comments_without_replies = []
        for comment in not_my_comments:
            hasreply = 0
            for reply in comment.replies.list():
                if reply.author.name == args.username:
                    hasreply += 1
            if hasreply < 1:
                comments_without_replies.append(comment)
        
        """
        # procedure for replying to top comment
        highest_score = 0
        top_comment = ''
        for comment in not_my_comments:
            hasreply = 0
            for reply in comment.replies.list():
                if reply.author.name == 'hubertbotguy':
                    hasreply += 1
            if hasreply < 1:
                if comment.score() >= highest_score:
                    top_comment = comment
                    highest_score = comment.score
        """

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
        
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        """
        random.choice(comments_without_replies).reply(generate_comment())
        print(datetime.datetime.now(), ': made a reply.')
        """
        
        for comment in comments_without_replies:
            comment.reply(generate_comment())
            print(datetime.datetime.now(), ': made a reply.')
            time.sleep(6)
        
        """
        top_comment.reply(generate_comment())
        print(datetime.datetime.now(), ': made a reply to top comment.')
        """

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    submissions = []
    for submission in reddit.subreddit("cs40_2022fall").hot(limit=5):
        submissions.append(submission)
    submission = random.choice(submissions)
    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(10)