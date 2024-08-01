from app import app
from flask import render_template
from app.md_convert import posts


@app.route("/")
@app.route("/index")
def index():
    return render_template("homepage.html")

@app.route("/works")
def works():
    return render_template("works.html")

@app.route("/blog")
def blog():
    return render_template("blog.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/blog/<title>")
def blog_post(title):

    index = None
    for i in range(len(posts)):
        if posts[i]["title"] == title:
            index = i
            break
    
    print(i)
    blogvalue = {"title": posts[index]["title"], "content": posts[index]["content"]}
    return render_template("blog_post.html", blogvalue=blogvalue)


@app.route("/chaikin")
def chaikin():
    return render_template("chaikin.html")