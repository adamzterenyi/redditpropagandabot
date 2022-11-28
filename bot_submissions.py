import praw
import random
import datetime
import time

reddit = praw.Reddit('bot')
subreddit = reddit.subreddit("cs40_2022fall")

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

for submission in reddit.subreddit("unitedkingdom").hot(limit=200):
    subreddit.submit(submission.title, url=submission.url)
    print('posted link!')
    time.sleep(5)
    subreddit.submit(title=generate_comment(), selftext = generate_comment())
    print('posted self-text!')
    time.sleep(5)