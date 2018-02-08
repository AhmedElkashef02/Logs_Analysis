#!/usr/bin/env python3.5

import psycopg2


def find_top_articles():
    """What are the most popular three articles of all time?"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""
    SELECT title,COUNT(log.ip)
    FROM articles JOIN log
    ON '/article/' || articles.slug = log.path
    GROUP BY title
    ORDER BY count DESC
    LIMIT 3;
    """)
    results = c.fetchall()
    db.close()
    return results


def find_popular_authors():
    """Who are the most popular article authors of all time?"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""
    SELECT name, COUNT(articles.title)
    FROM authors JOIN articles
    ON articles.author = authors.id
    JOIN log
    ON articles.slug = substring(log.path,10)
    GROUP BY name
    ORDER BY count DESC;
    """)  # Avoided using %like% due to its inefficiency
    results = c.fetchall()
    db.close()
    return results


def find_most_errors():
    """On which days did more than 1% of requests lead to errors?"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""
    SELECT all_req.Fordate, ROUND((ErrPosts*100.0)/NumPosts, 2)
    AS PostPercent
    FROM (
    SELECT DATE(time) AS Fordate, COUNT(*) AS NumPosts
    FROM log
    GROUP BY DATE(time)
    ORDER BY Fordate
    ) as all_req join (
    SELECT DATE(time) AS Fordate, COUNT(*) AS ErrPosts
    FROM log
    WHERE status = '404 NOT FOUND'
    GROUP BY DATE(time)
    ORDER BY Fordate
    ) as err_req
    On all_req.Fordate = err_req.Fordate
    WHERE ROUND((ErrPosts*100.0)/NumPosts, 2) > 1.00;
    """)
    results = c.fetchall()
    db.close()
    return results


# main function of the program
def main():
    print("""
Hello to the third project of the Udacity's nanodegree.
This project was made by Ahmed Elkashef, A full stack developer.
To start, type in the number of the question that you want to solve.
""")
    user_input = input("""
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
""")
    if (eval(user_input) == 1):
        for title, num in find_top_articles():
            print('"{} — {} views"'.format(title, num))
    elif (eval(user_input) == 2):
        for author, num in find_popular_authors():
            print('{} — {} views'.format(author, num))
    elif (eval(user_input) == 3):
        for date, percent in find_most_errors():
            print('{:%B %d, %Y} - {}% errors'.format(date, percent))
    else:
        print("error, please enter a valid input number")


if __name__ == '__main__':
    main()
