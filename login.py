import json
import praw
from prawcore import auth

print('Welcome to braw!')
path = input('Paste the link of credential file: ')


def get_reddit_body():
    json_file = json.load(open(path, 'r', encoding='utf-8'))
    user_agent = json_file['user_agent'] if 'user_agent' in json_file else None
    client_id = json_file['client_id'] if 'client_id' in json_file else None
    client_secret = json_file['client_secret'] if 'client_secret' in json_file else None
    username = json_file['username'] if 'username' in json_file else None
    password = json_file['password'] if 'password' in json_file else None

    body = praw.Reddit(client_id=client_id,
                       client_secret=client_secret,
                       user_agent=user_agent,
                       username=username,
                       password=password)

    try:
        for _ in body.subreddit('all').hot(limit=1):
            continue
    except auth.ResponseException:
        print('Cant see SHIT Captain!')
        print('Cannot connect to Reddit')
        return 0
    return body
