# creates folder for a problem from input problem link
# Folder contains a .py file and a readme.md containing problem link
import os
import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Usage: python create_problem_folder.py <problem_link>")
    exit(1)

problem_link = sys.argv[1]
# scrape problem name from h1 tag till before child nobr tag
page = requests.get(problem_link)
soup = BeautifulSoup(page.content, 'html.parser')
problem_name = soup.find('h1').text.split('solved')[0].strip()
print(f"Problem name: {problem_name}")

# create folder with problem name
os.mkdir(problem_name)
print('Created folder')

# create .py file
with open(f'{problem_name}/{problem_name.lower().replace(" ", "_")}.py', 'w') as f:
    f.write('def solution():\n    pass\n\n\n')
    f.write(f"with open().txt', 'r') as f:\n    pass\n\n\n")
    f.write(f'ans = solution()\nprint(ans)')
print('Created .py file')

# create readme.md file
with open(f'{problem_name}/readme.md', 'w') as f:
    f.write(f'## {problem_name}\n\n')
    f.write(f'Problem link: {problem_link}')
print('Created readme.md file')

