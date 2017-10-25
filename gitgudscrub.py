import praw
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
    if 'git gud' in text.lower():
        already_reply = False
        for child in comment.replies:
            if config.username == child.author:
                already_reply = True
        if not already_reply:
            try:
                comment.reply(message)
                print("we did it!")
            except:
                print("ruh roh raggie")
