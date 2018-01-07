# One Minute Pitch

##A web application that allows the users to post pitches, comment and vote on pitches.

## By [Kepha Okari](https://github.com/kepha-okari)


## Description
This is a web application that allows various users to submit a short pitch. Users can also be able to view other pitches from different categories (Pick-up Lines, Interview Pitches, Product Pitches, Promotion Pitches), comment and vote. For a user to do any of that, they need to have registered.

## User Stories
* As a user I would like to view the different categories.
* As a user I would like to see the pitches other people have posted.
* As a user I would like to comment on the different pitches and leave feedback.
* As a user I would like to submit a pitch in any category.
* As a user I would like to vote on the pitch they liked and give it a downvote or upvote.

## Specifications
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
|Display Various Pitch Categories | N/A | Various pitches grouped by category are displayed |
|Display pitches | **Click** on a Category| A page with a list of pitches from the selected category |
|Add new pitch | **Click** New pitch | User Should register/sign in to add new pitch |
|View Pitches | **Click** on a pitch | View a pitch and comments |
|Comment on a pitch | **Click** Comment | Registered User displays a form where a user can comment on a certain pitch |
<!-- |Upvote a pitch | **Click** glyphicon upvote | Vote for a specific pitch increases |
|Downvote a pitch | **Click** glyphicon downvote | Vote for a specific pitch decreases | -->
# News Highlights

This application lists various sources of news and subsequent highlights in each of the source. clicking an individual highlights takes the user to the article itself for the full story

## By **[Kepha Okari](https://github.com/kepha-okari)**

## Description
[This](https://kepha-news-highlights.herokuapp.com/) is a web application that lists various News sources gotten from [News API](https://newsapi.org/). A user can click on a News source and be directed to a page that contains News Articles from the selected News source. The article's title, image, date of publication and preview will be displayed and a user can click on the article to be directed to the source's site to read the entire article.

## User Stories
As a user I would like:
* to see various news sources and select the ones I prefer
* to see all the news articles from that news source
* to see the image, description and time the news article was created.
* to click on an article and read it fully from the news source.

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Display News sources | N/A | List of various News sources is displayed |
| Articles from selected News source | **Click** a News source | Directed to a page with a list of articles from the selected source |
| Display image, description, title and date of publish | N/A | An articles image, title, description and date of publication are displayed |
| Read an entire article | **Click** on an article | Directed to the source's site to read the entire article |

## Prerequisites
* Python3.6

## Setup/Installation Requirements
* internet access
* $ git clone https://github.com/kepha-okari/one-minute-pitch.git
* $ cd one-minute-pitch
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
* $ ./start.sh

## Known Bugs

No known bugs

## Technologies Used
- Python3.6
- Flask framework
- Bootstrap
- PostgreSQL

### License

**[MIT](./LICENSE)** (c) 2017 **[Kepha Okari](https://kepha-okari.github.io)**
