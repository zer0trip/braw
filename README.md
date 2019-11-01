# braw
Browse Reddit At Work 

With this module, you can safely read Reddit in commond console pretending at work. 

Prerequisite: 
1. Install praw. You can install praw by pip install praw
2. Reddit account 
3. Create an app to get client_id, client_secret, user_agent of your reddit account. You can create one by https://www.reddit.com/prefs/apps/ . For further information you can visit https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps
4. A text file for storing your personal login information. 


Function: 
1. get_top(s_reddit='all', time='week', how_many=10)
2. get_hot(s_reddit='all', how_many=10)
3. get_new(s_reddit='all', how_many=10)
4. cheer_me_up: automate download images from 'aww', 'dogpictures', and 'catpictures' and store in your designated local folder 
5. til: todayilearned: get top from subreddit 'todayilearned'
6. get_submission(post_id): print out the title and body of the submission. If the submission is pure a link, will ask for promping a new tab on your default browser or saving to local folder if the link is an image

