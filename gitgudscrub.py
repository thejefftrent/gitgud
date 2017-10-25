import praw
from time import sleep, time

import config
gitgud = praw.Reddit(client_id=config.CLIENT_ID,
                     client_secret=config.CLIENT_SECRET,
                     password=config.PASSWORD,
                     user_agent='git gud by /u/bhjeff',
                     username=config.USERNAME)
MESSAGE = "    git: 'gud' is not a git command. See 'git --help'.\n\n    The most similar command is\n            gui\n*****\n^^I ^^am ^^a ^^bot. ^^Visit ^^/r/gitgudscrubbot ^^for ^^more ^^information."

sub = gitgud.subreddit('gitgudscrubbot')

comments = sub.stream.comments()

print(gitgud.user.me())

for comment in comments:
    text = comment.body
    already_reply = False
    if 'git gud' in text.lower():
        comment.refresh()
        replies = comment.replies
        for child in replies:
            print(child.author)
            if config.USERNAME == child.author:
                already_reply = True
                break
        if already_reply:
            continue
        try:
            comment.reply(MESSAGE)
            print("we did it!")
        except:
            print("ruh roh raggie")
        print("I'm tired")
        sleep((10 * 60) + 10) #10 min and 10 seconds to make sure we can post again
