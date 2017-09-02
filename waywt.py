import calendar
import os

from datetime import datetime

import praw

def get_all_submissions_for_month(month, year):
    """
    Params
    ------
    month: int
    year: int
    """
    # https://stackoverflow.com/questions/42950/get-last-day-of-the-month-in-python
    last_day_of_month = calendar.monthrange(YEAR, MONTH)[1]

    unix_start_month = datetime.timestamp(datetime(YEAR, MONTH, 1))
    unix_end_month = datetime.timestamp(datetime(YEAR, MONTH, last_day_of_month))
    
    return [post for post in ffa.submissions(start=unix_start_month, end=unix_end_month, extra_query=None)]


def is_waywt(submission):
    return ('WAYWT' in submission.title) and ('Announcement' not in submission.title)


def print_titles(submissions):
    # print for human checking
    if not submissions:
        print("No submissions to print!")
    else:
        for i,submission in enumerate(submissions):
            print('{0}. {1}'.format(i, submission.title))


def extract_comments(submission):
    # This will exclude the 'more comments' objects
    submission.comments.replace_more(limit=0)
    # Manually sort because setting submission.comment_sort to 'top' does not seem to actually sort by upvotes
    return [top_level_comment for top_level_comment in submission.comments if top_level_comment.author is not None]


def sort_comments_by_upvotes(comments):
    """comments is a list of pram Comments"""
    return sorted(comments, key=lambda x: x.ups, reverse=True)


def get_all_comments(submissions):
    all_comments = []
    for submission in submissions:
        all_comments += extract_comments(submission)
    return all_comments


def print_top_n_comments(limit, comments):
    """
    Params
    ------
    limit: int
    """
    info = "Author: /u/{0}\nUpvotes: {1}\nPermalink: {2}\n\n"
    for comment in comments[:limit]:
        print(info.format(comment.author, comment.ups, 'https://reddit.com'+comment.permalink()))


def create_post_text(comments):
    title = "## TOP OF WAYWT: {0} {1}\n".format(calendar.month_name[MONTH], YEAR)

    # See https://www.reddit.com/wiki/commenting
    table_header = "Rank | Comment | User | Upvotes\n" + \
                   "---- | ---- | ---- | -------\n"

    row = "{rank} | [{post_title}](https://reddit.com{permalink}) | /u/{user} | +{upvotes}\n"

    post = title + '\n' + table_header

    # You could speed this up by refactoring to keep the submission title
    # with each comment, or by just making the permalink text just say 'link'.
    for i, comment in enumerate(comments):
        post += row.format(
            rank=i+1,
            permalink=comment.permalink(),
            user=comment.author,
            upvotes=comment.ups,
            post_title=reddit.submission(id=comment._extract_submission_id()).title
        )
    return post

