from dotenv import load_dotenv, find_dotenv
from github import Github
import requests
import uuid
import os

load_dotenv(find_dotenv())


git_instance = Github(os.getenv("GITHUB_TOKEN"))
git_org = git_instance.get_organization('Exifly')
git_repo = git_org.get_repo('apivault')


def pr_template():
    return f"This PR is created automatically by the script {__file__}. It will update the file API_LIST.md"


def generate_unique_id():
    return str(uuid.uuid4().int & (1 << 32)-1)


def get_apilist_file():
    return git_repo.get_contents('API_LIST.md')


def get_main_sha():
    main_branch = git_repo.get_branch('main')
    return main_branch.commit.sha


def create_new_branch(branch_name):
    print(f"Creating new branch {branch_name}")
    sha_repo = get_main_sha()
    return git_repo.create_git_ref(
        ref=f'refs/heads/{branch_name}',
        sha=sha_repo
    )


def update_apilist(apis, branch):
    print("Updating API FILE md")
    try:
        file_content = git_repo.get_contents("API_LIST.md")
        git_repo.update_file(path="API_LIST.md",
                             message="Update file",
                             content=apis,
                             sha=file_content.sha,
                             branch="update_apilist_table")
    except Exception as e:
        print(e)


def open_pr(title, body, branch_name):
    print("Opening pull request")
    try:
        git_repo.create_pull(
            title=title,
            body=body,
            head=f"{git_org.login}:{branch_name}",
            base='main'
        )
        print("Pull request created")
    except Exception as e:
        print(e)


def create_issue(title, body):
    git_repo.create_issue(
        title=title,
        body=body
    )


def create_table(categories):
    table = str()
    for category, entries in categories.items():
        table += f'# {category}\n\n'
        table += '| API | Description | Auth | HTTPS | Cors |\n'
        table += '| --- | --- | --- | --- | --- |\n'
        for entry in entries:
            api_link = f"[{entry['API']}]({entry['Link']})"
            table += f"| {api_link} | {entry['Description']} | {entry['Auth']} | {entry['HTTPS']} | {entry['Cors']} |\n"
        table += '\n'
    return table


if __name__ == '__main__':
    data = requests.get("https://api.apivault.dev/api/all").json()

    categories = {}
    for entry in data:
        category = entry["Category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(entry)

    branch_id = generate_unique_id()
    api_list_table = create_table(categories=categories)
    branch_id = generate_unique_id()
    new_branch = create_new_branch(f"update_apilist_table_{branch_id}")
    update_apilist(apis=api_list_table,
                   branch=f'update_apilist_table_{branch_id}')
    try:
        open_pr(
            title='Updated api list markdown table',
            body=pr_template(),
            branch_name=f'update_apilist_table_{branch_id}'
        )
    except Exception as e:
        print(e)
