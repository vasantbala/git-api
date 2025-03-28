from git import Repo

WORKING_DIR = 'gitpods'

def clone_repo(url, name):
    repo = Repo.clone_from(url, f'{WORKING_DIR}/{name}')
    return repo

def create_branch(repo, branch_name):
    repo.git.checkout('master')
    repo.git.checkout('HEAD', b=branch_name)
    return repo

def change_file(repo, file_name, content):
    with open(f'{repo.working_dir}/{file_name}', 'w') as f:
        f.write(content)
    return repo

def commit(repo, message):
    repo.git.add(A=True)
    repo.index.commit(message)
    return repo

def push(repo):
    repo.git.push('origin', repo.active_branch.name)
    return repo

print('Git API loaded')
print('Working directory:', WORKING_DIR)
#clone_repo('https://github.com/vasantbala/FlightDataViewer.git', 'FlightApp')
#create_branch(Repo('gitpods/FlightApp'), 'feature1')

# with open('gitpods/FlightApp/readme.md', 'r') as f:
#     readme_content = f.read()
# readme_content += '\n\nThis is a new line added by the API'
# change_file(Repo('gitpods/FlightApp'), 'readme.md', readme_content)

#commit(Repo('gitpods/FlightApp'), 'Added a new line to readme.md')

push(Repo('gitpods/FlightApp'))