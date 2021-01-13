#!/usr/bin/env python3
import markdown
import glob
from dateutil.parser import parse
import os

articles = []
for post in glob.glob('blog/*.md'):
    with open(post, 'r') as f:
        text = f.read()
    md = markdown.Markdown(extensions=['meta'])
    md.convert(text)
    title = md.Meta['title'].pop()
    date = md.Meta['date'].pop()
    date = parse(date).date()
    link = os.path.basename(post).replace('.md', '.html')
    articles.append((date, title, link))
articles.sort(key=lambda t: t[0])

out = open('blog/index.html', 'w')

print("""<!DOCTYPE html>
<html>
  <head>
    <title>My Blog</title>
    <link rel="stylesheet" href="../stylesheets/base.css">
  </head>
  <body>
    <main>
      <a href="..">Back to Home</a>
      <h1>My Blog</h1>
      <p>Follow my thoughts and work over time.</p>
      <hr>
""", file=out)
for date, title, link in reversed(articles):
    print(f'\
      <article class="linkbox blogpostlink">\n\
        <h2><a href="{link}">{title}</a></h2>\n\
        <p class="posted">Posted: {date}</p>\n\
      </article>', file=out)
print("""
    </main>
  </body>
</html>
""", file=out)
