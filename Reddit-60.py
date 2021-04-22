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
        
        if author in line:
            
            file_read.close()
            
            return 1

    file_read.close()
    
    return 0
i = 50

def check_submission(author,submission):
    file_read = open("comment_list.txt",'r+')
    for line in file_read.readlines():
        if (author in line ) or (submission in line):
            file_read.close()
            return 1

    file_read.close()
    file__read = open("posts.txt",'r+')

    for line in file__read.readlines():
        if submission in line:
            file__read.close()
            return 1

    file__read.close()
    return 0



subreddits = ['realonlyfansreviews','OnlyFansReviews']
keywords = ['review','rate','filter']
while (i>0):
    
    for topic in subreddits:
        print(".............Online.............")
        
        subreddit = reddit.subreddit(topic)
        message = temp.substitute({'subreddit':topic})
        for submission in subreddit.new(limit = 20):
            
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

                                    check3 = check_submission(author,str(submission))
                                    if check3 == 0:

                                        print(comment.author)
                                        #reddit.redditor(author).message('Review', message)
                                        
                                        print("Message sent")
                                        
                                                    
                                        message_list = open("comment_list.txt",'a+')
                                        message_list.write('\n' + author)
                                        message_list.write('\n' +str(submission))
                                        message_list.close()
                                        post_list = open("posts.txt",'a+')
                                        post_list.write('\n' + str(submission))
                                        post_list.close()
                                        time.sleep(3600)
                                        continue
                    except praw.exceptions.APIException as e:
                        if e.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
                            print("Lol this user has a whitelist, there is no way to message them, giving up")
   
    time.sleep(600)
