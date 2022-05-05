USERS = []

SESSIONS = {}

TABS = [
    {"icon": "fas fa-home fa-fw", "title": "Home", "id":"home"},
    {"icon": "fas fa-hashtag fa-fw", "title": "Explore", "id": "explore"},
    {"icon": "far fa-bell fa-fw", "title": "Notifications", "id": "notifications"},
    {"icon": "far fa-envelope fa-fw", "title": "Messages", "id": "messages"},
    {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks", "id": "bookmarks"},
    {"icon": "fas fa-clipboard-list fa-fw", "title": "Lists", "id": "lists"},
    {"icon": "far fa-user fa-fw", "title": "Profile", "id": "profile"},
    {"icon": "fa-solid fa-right-to-bracket", "title": "Log out", "id": "logout"},
    {"icon": "fas fa-ellipsis-h fa-fw", "title": "More", "id": "more"}
]

PEOPLE = [
    {"src": "stephie.png", "name": "Stephie Jensen", "handle": "@sjensen"},
    {"src": "monk.jpeg", "name": "Adrian Monk", "handle": "@detective :)"},
    {"src": "kevin.jpeg", "name": "Kevin Hart", "handle": "@miniRock"}
]

TRENDS = [
    {"category": "Music", "title": "We Won", "tweets_counter": "135K"},
    {"category": "Pop", "title": "Blue Ivy", "tweets_counter": "40k"},
    {"category": "Trending in US", "title": "Denim Day", "tweets_counter": "40k"},
    {"category": "Ukraine", "title": "Ukraine", "tweets_counter": "20k"},
    {"category": "Russia", "title": "Russia", "tweets_counter": "10k"}
]

TWEETS = [
    {"id":"1", "user_id": "444", "src":"444.jpeg", "user_firstname":"Barack", "user_lastname":"Obama", "user_name":"barackobama",  "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpeg"},
    {"id":"2", "user_id": "333", "src":"333.jpeg", "user_firstname":"Elon", "user_lastname":"Musk", "user_name":"elonmusk", "text":"If our twitter bid succeeds, we will defeat the spam bots or die trying!"},
    {"id":"3", "user_id": "222", "src":"222.jpeg", "user_firstname":"Joe ", "user_lastname":"Biden", "user_name":"joebiden", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
    {"id":"4", "user_id": "444", "src":"444.jpeg", "user_firstname":"Barack", "user_lastname":"Obama", "user_name":"barackobama",  "text":"Yesterday, I talked about how we should be able to agree on some basic facts – including around issues like climate change – and how companies need to be more careful about the content they promote, especially in ads. This is a good example of progress.", "image":"1.jpeg"},
    {"id":"5", "user_id": "333", "src":"333.jpeg", "user_firstname":"Elon", "user_lastname":"Musk", "user_name":"elonmusk", "text":"Such a joy to work with amazingly talented people at SpaceX, Tesla, Neuralink & Boring Co!"},
    {"id":"6", "user_id": "222", "src":"222.jpeg", "user_firstname":"Joe", "user_lastname":"Biden", "user_name":"joebiden", "text":"Mr. President, welcome back to the White House."},
    {"id":"7", "user_id": "444", "src":"444.jpeg", "user_firstname":"Barack", "user_lastname":"Obama", "user_name":"barackobama",  "text":"Tomorrow, I'm heading to Stanford to deliver a speech about changes in the way we create and consume information, and the very real threat it poses to democracy.", "image":"1.jpeg"},
    {"id":"8", "user_id": "333", "src":"333.jpeg", "user_firstname":"Elon", "user_lastname":"Musk", "user_name":"elonmusk", "text":"69.420 of statistics are false"},
    {"id":"9", "user_id": "222", "src":"222.jpeg", "user_firstname":"Joe", "user_lastname":"Biden", "user_name":"joebiden", "text":"After a long stretch, Americans are back to work, and the economy has gone from being on the mend to being on the move."},
    {"id":"10", "user_id": "444", "src":"444.jpeg", "user_firstname":"Barack", "user_lastname":"Obama", "user_name":"barackobama",  "text":"In recent years, we've seen how quickly disinformation spreads, especially on social media. This has created real challenges for our democracy.", "image":"1.jpeg"},
    {"id":"11", "user_id": "333", "src":"333.jpeg", "user_firstname":"Elon", "user_lastname":"Musk", "user_name":"elonmusk", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
    {"id":"12", "user_id": "222", "src":"222.jpeg", "user_firstname":"Joe", "user_lastname":"Biden", "user_name":"joebiden", "text":"Our economy has gone from being on the mend to being on the move."},
]

ITEMS = [
    {"id": "111", "img":"bbc.jpeg", "title":"BBC News", "user_name":"bbcworld"},
    {"id": "222", "img":"222.jpeg", "title":"Joe Biden", "user_name":"joebiden"},
    {"id": "333", "img":"333.jpeg", "title":"Elon Musk", "user_name":"elonmusk"},
    {"id": "444", "img":"444.jpeg", "title":"Barack Obama", "user_name":"barackobama"},
]


GMAIL_PASS = "Kolor2022!"

COOKIE_SECRET = "WIP"

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

