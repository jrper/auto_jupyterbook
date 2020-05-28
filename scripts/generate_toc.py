#! /usr/bin/env python3

import os
import glob
from string import Template

with open('_data/toc.yml.in', 'r') as template_file:
    template = template_file.read()

chapter = Template("""- title: ${title}
  url: /${dir}/intro
  not_numbered: true
  expand_sections: true
  sections:
""")
section = Template("""  - title: ${sec_title}
    url: /${dir}/${name}
    not_numbered: true
""")

with open('_data/toc.yml', 'w') as outfile:
    outfile.write(template)
    dirs = {'Maths':'Mathematics',
            'Python':'Python'}
    
    for dir, title in dirs.items():
        outfile.write(chapter.substitute(dir=dir,
                                         title=title))
        for notebook in glob.glob(os.path.join('./content', dir, '*.ipynb')):
            name = os.path.basename(notebook).rsplit('.', 1)[0]
            sec_title = name.replace('_', ' ')
            outfile.write(section.substitute(sec_title=sec_title,
                                             dir=dir,
                                             name=name))
