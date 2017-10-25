from time import sleep, time

import praw
import config

MESSAGE = "    git: 'gud' is not a git command. See 'git --help'.\n\n    The most similar command is\n            gui\n*****\n^^I ^^am ^^a ^^bot. ^^Visit ^^/r/gitgudscrubbot ^^for ^^more ^^information."

def main():
    gitgud = praw.Reddit(client_id=config.CLIENT_ID,
                         client_secret=config.CLIENT_SECRET,
                         password=config.PASSWORD,
                         user_agent='git gud by /u/bhjeff',
                         username=config.USERNAME)
    print(gitgud.user.me())
    sub = gitgud.subreddit('gitgudscrubbot')
    comments = sub.stream.comments()
    for comment in comments:
         if process_comment(comment):
            # New accounts can only post once every 10 minues, remove the following if you don't have the restriction
            print("I'm tired")
            sleep((10 * 60) + 10)
            print("I'm awake!")

def process_comment(comment):
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
                return False
            try:
                comment.reply(MESSAGE)
                print("we did it!")
            except:
                print("ruh roh raggie")
            return True
        
if __name__ == '__main__':
    main()
