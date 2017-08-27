# Get the Top of /r/femalefashionadvice WAYWT

A script to get all the top comments in the WAYWT (What are you wearing today) of a given month and format them for a post. This was formerly done manually by /u/thecurvynerd (thank you!). Example post: https://www.reddit.com/r/femalefashionadvice/comments/61241t/top_of_waywt_february_2017/ (This script does NOT create the imgur album linked to in the title of the example post).

## Usage

### Knowledge Prerequisites

It will be a lot less painful to use this if you have experience using jupyter notebook. This section expects you know how to download this `ipynb` file (or the whole repository), install dependencies (manually, using a virtualenv, or using conda env) and set environment variables.

### Dependencies

This script requires the following to be installed on your computer:

- [python](https://www.python.org/downloads/) 3.5 (probably any python 3.x would work, but I used 3.5)
- [jupyter notebook](http://jupyter.org/install.html)
- [PRAW](https://praw.readthedocs.io/en/latest/index.html) (the Python Reddit API Wrapper).

There is a `environment.yml` file if you want to create a conda env (`conda env create -f environment.yml`) with jupyter and python 3.5. Conda does not have `praw` as of August 2017, so you will need to `pip install` that manually.

### Environment Variables

The reddit API requires you to register your app to be able to use it. You can get an app ID and app secret by following the steps [here](https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example#first-steps). Select 'script' when it asks what type of app it will be.

Save the app ID, app secret, and your reddit username as [environment variables](https://en.wikipedia.org/wiki/Environment_variable#Assignment). How you set these depends on what OS you're using.

```
export REDDIT_CLIENT_ID=your_id
export REDDIT_CLIENT_SECRET=your_secret
export REDDIT_USER=your_username
```

### Run the script

In the cell that says

```
# read-only subreddit instance
ffa = reddit.subreddit('femalefashionadvice')
# 1-indexed months. e.g. 2 would be February
MONTH = 2
YEAR = 2017
# How many comments you want in the 'Top of' list.
LIMIT = 34
```

Set `MONTH`, `YEAR`, and `LIMIT` to the values you want.

Unfortunately this script still requires manual intervention to filter out WAYWT posts within the month time range that are not, in fact, WAYWT posts. You can select the cell *under* the one that says `print_titles(month_submissions_with_waywt)`, and then from the notebook toolbar select `Cell` > `Run all above` to run all the cells up to that point. It should print a list of the submissions that contain 'WAYWT' in the title and were posted in the month you set. Here you can see that you would want to filter out things like previous "top of" posts. 

You can then change the variable `not_waywt = [3, 4, 7, 8, 10]` to have the numbers of the posts that you *don't* want to include. With that cell selected, you can then do `Run all below` to run the rest of the script.

You can paste the output of the `print(top_of_waywt_post)` cell in the bottom markdown cell to see what it would look like with formatting applied.

Note that deleted comments (if a comment author is `None`) are not included.

The code in this notebook is not the cleanest or most optimized because I am lazy, but hopefully it is still useful.

This information is duplicated in the ipynb.
