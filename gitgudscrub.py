import praw
from time import sleep, time

import config
gitgud = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     password=config.password,
                     user_agent='git gub by /u/bhjeff',
                     username=config.username)
message = "    git: 'gud' is not a git command. See 'git --help'.\n\n    The most similar command is\n            gui\n*****\n^^I ^^am ^^a ^^bot. ^^Visit ^^/r/gitgudscrubbot ^^for ^^more ^^information."

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
            if config.username == child.author:
                already_reply = True
                break
        if already_reply:
            continue
        try:
            comment.reply(message)
            print("we did it!")
        except:
            print("ruh roh raggie")
        print("I'm tired")
        sleep((10 * 60) + 10) #10 min and 10 seconds to make sure we can post again
