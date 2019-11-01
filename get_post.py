from .get_submission import get_submission
from .login import get_reddit_body
from urllib.request import urlretrieve
import os


def get_hot(s_reddit='all', how_many=10):
    body = get_reddit_body()
    i = 1
    for submission in body.subreddit(s_reddit).hot(limit=how_many):
        print('Hot {}:'.format(i))
        get_submission(submission.id, print_body=False)
        i += 1
    return


def get_top(s_reddit='all', time='week', how_many=10):
    body = get_reddit_body()
    i = 1
    for submission in body.subreddit(s_reddit).top(time_filter=time, limit=how_many):
        print('Top {}:'.format(i))
        get_submission(submission.id, print_body=False)
        i += 1
    return


def get_new(s_reddit='all', how_many=10):
    body = get_reddit_body()
    i = 1
    for submission in body.subreddit(s_reddit).new(limit=how_many):
        print('New {}:'.format(i))
        get_submission(submission.id, print_body=False)
        i += 1
    return


def til(how_many=10):
    get_top(s_reddit='todayilearned', how_many=how_many)


def cheer_me_up(how_many=10):
    print("Let'e me cheer you up.")
    save_path = input('Where do you want to save the picture? :')
    body = get_reddit_body()
    for submission in body.subreddit('aww+dogpictures+catpictures').hot(limit=how_many):
        if len(submission.selftext) == 0 and not submission.over_18:
            url = submission.url
            if 'jpg' in url:
                suffix = 'jpg'
            elif 'png' in url:
                suffix = 'png'
            else:
                suffix = 'gif'
            path = os.path.join(save_path, '{}.{}'.format(submission.id, suffix))
            urlretrieve(url, path)

    print('Done. All saved in {}'.format(save_path))
    return

