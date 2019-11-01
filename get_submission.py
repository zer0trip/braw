from .login import get_reddit_body
from .special_function import print_function, body_is_link
from praw.models import MoreComments


def get_submission(post_id, print_body=True):
    body = get_reddit_body()
    submission = body.submission(post_id)
    if submission.over_18:
        print('Cautious: NSFW!!!!')
    print('Submission ID: {}'.format(submission.id))
    print('Subreddit: {}'.format(submission.subreddit))
    print('Submission title:')
    print_function(submission.title)
    if print_body:
        if len(submission.selftext) == 0:
            print('The content is pure a link.')
            body_is_link(submission)
        else:
            print_function(submission.selftext)
    print()
    return


def get_comment(post_id, how_many=20):
    body = get_reddit_body()
    submission = body.submission(post_id)
    submission.comment_sort = 'top'
    submission.comment_limit = how_many
    i = 1
    for comment in submission.comments:
        if isinstance(comment, MoreComments):
            continue
        if comment.body not in ['[deleted]', '[removed]']:
            print('Comment ', i)
            print_function(comment.body)
            i += 1
            print()

    return

