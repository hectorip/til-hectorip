import begin
from datetime import datetime
from slugify import slugify

template = """---
title: "{}"
date: {}
author: Héctor Patricio
tags:
comments: true
excerpt: ""
header:
  image: #image
---"""

@begin.start(auto_convert=True)
def main(*names):
    """ Creates a new file with today's date and title as slug in _posts dir """
    t = datetime.today()
    date = "{}-{}-{}".format(t.year, t.month,t.day)
    for name in names:
        file_name = "_posts/{}-{}.md".format(date, slugify(name))
        with open(file_name, "w") as f:
            f.write(template.format(name, date))
