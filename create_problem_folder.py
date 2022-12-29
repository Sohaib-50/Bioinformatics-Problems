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
# scrape problem name from h1 tag till before the word 'solved'
page = requests.get(problem_link)
soup = BeautifulSoup(page.content, 'html.parser')
problem_name = soup.find('h1').text.split('solved')[0].strip()
print(f"Problem name: {problem_name}")

# create folder with problem name
os.mkdir(problem_name)
print('Created folder')

# create .py file
with open(f'{problem_name}/{problem_name.lower().replace(" ", "_")}.py', 'w') as f:
    f.write('def solution(data):\n    pass\n\n\n')
    f.write(f"def get_data(file_name):\n    with open(file_name, 'r') as f:\n        pass\n\n\n")
    # get input from test_input.txt
    f.write(f"data = get_data('test_input.txt')\n")
    f.write(f'ans = solution(data)\nprint(ans)')
print('Created .py file')

# create readme.md file
with open(f'{problem_name}/readme.md', 'w') as f:
    f.write(f'## {problem_name}\n\n')
    f.write(f'Problem link: {problem_link}')
print('Created readme.md file')

# create an empty test_input.txt file
with open(f'{problem_name}/test_input.txt', 'w') as f:
    f.write('')
print('Created test_input.txt file')