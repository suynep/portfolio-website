import markdown
import os

def convert_md_to_html(path):
    with open(path) as f:
        md = f.read()
    html = markdown.markdown(md)
    return html

def convert_md_to_preview_html(path):
    with open(path) as f:
        md = f.readlines()
        md = md[1:10]
        retText = ""
        for line in md:
            retText += line
    
    html = markdown.markdown(retText)
    return html

BLOG_PATH= os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/blog/')
files=[file.rsplit(".", 1)[0] for file in os.listdir(BLOG_PATH)]
posts = []


for file in files:
    posts.append({"content": convert_md_to_html(BLOG_PATH+file+".md"), "title": file, "preview": convert_md_to_preview_html(BLOG_PATH+file+".md"), "date": "2024-07-30"})
    print(posts)