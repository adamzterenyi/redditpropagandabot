# Building a Reddit Propaganda Bot

This repository contains the code for my Reddit propaganda bot(s). My bot writes variations of text samples (madblibs) supporting Tulsi Gabbard, Sarah Huckabee Sanders, and Kari Lake. (*Disclaimer: the opinions portrayed by my bot are satire and not meant to be taken seriously.*) The code for my bot can be found in `bot.py`.

My favorite thread is a [post](https://old.reddit.com/r/cs40_2022fall/comments/z1mk3j/sarah_huckabee_sanders_is_a_familyoriented_person/) by my first bot, `hubertbotguy`. All of my bots commented on it. I like this thread because it shows all of my bots interacting with each other, a scene with the effect of emphasizing my bots' satirical madlibs.
![Image of favorite thread](favoritethread.png)

After running `hubertbotguy`, I reached 1000 valid comments! Here is the output of the `bot_counter.py` file supplied by Mike Izbicki:
```
len(comments)= 1000
len(top_level_comments)= 472
len(replies)= 528
len(valid_top_level_comments)= 472
len(not_self_replies)= 528
len(valid_replies)= 528
========================================
valid_comments= 1000
========================================
```

For this project, I believe my score should be 31/30. I completed the 6 tasks in `bot.py`, earning me 12 points. This repository, done properly, is another 3. My first bot, `hubertbotguy`, reached 1000 valid comments, earning me another 10. I then wrote a `bot_submissions.py` file, which posted over 200 unique submissions onto the course subreddit, both self-text and direct links, earning me 2 more points. I then modified by `bot.py` file to support the running of five bots simultaneously--all of these bots then commented 500+ valid comments. This earned me 2 more points. Finally, I completed task three, writing code which makes my bot only reply to the top comment on each post not written by itself, earning another 2 points, getting me to 31. I did not complete task 4, or the GPT-2/Markovify task. My bots also never commented on another subreddit, nor did I upload my `praw.ini` file.