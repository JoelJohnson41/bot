
import praw
from praw.models import MoreComments
from praw.models import Message
from string import Template
import time



reddit = praw.Reddit(client_id = 'fFslf9inkDcl_w',
client_secret = 'oYHTEMgYNzDknqZrE8jFnjYq7goGpQ',
user_agent = 'console: message_bot 1.0',
username = 'Competitive-Hero608',
password = 'johnson_chemistry11')

temp = Template('Hey, I was scrolling through  $subreddit and noticed your comment. There is this site called https://fan.reviews, its a site where you can leave reviews on any influencer/creator/onlyfans model, etc. You should leave a review for someone there. Its a great way to let them know if they are awesome or not so awesome. Its like Yelp for Creators.')

def check_author(author):
    
    file_read = open("comment_list.txt",'r+')
    
    for line in file_read.readlines():
        
        if line == (author + '\n'):
            
            file_read.close()
            
            return 1
    file_read.close()
    
    return 0
i = 50

subreddits = ['realonlyfansreviews','OnlyFansReviews']
keywords = ['review','rate','filter']
while (i>0):
    for topic in subreddits:
        
        subreddit = reddit.subreddit(topic)
        message = temp.substitute({'subreddit':topic})
        for submission in subreddit.new(limit = 20):
            print("online")
            submission.comments.replace_more(limit = 0)
            for comment in submission.comments :
                author = str(comment.author)
                                
                if check_author(author) == 1 :
                    
                    continue
                else :
                    try:
                        for keyword in keywords:
                            if keyword in comment.body:
                                check2 = check_author(author)
                                if check2 == 0:

                                    print(comment.author)
                                    #reddit.redditor(author).message('Check out my body', message)
                                    
                                    print("Message sent")
                                                
                                    message_list = open("comment_list.txt",'a+')
                                    message_list.write('\n' + author)
                                    message_list.close()
                                    continue
                    except praw.exceptions.APIException as e:
                        if e.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
                            print("Lol this user has a whitelist, there is no way to message them, giving up")

    time.sleep(600)