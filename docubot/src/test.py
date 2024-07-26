import requests
import base64
from urllib.parse import urljoin

def download_github_repo_to_txt(token, repo_name, output_file='repo_contents.txt'):
    
    # GitHub API base URL
    base_url = "https://api.github.com/"
    
    # Set up headers for authentication
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    def get_content(path=''):
        # Get repository contents
        repo_url = urljoin(base_url, f"repos/{repo_name}/contents/{path}")
        response = requests.get(repo_url, headers=headers)
        response.raise_for_status()
        return response.json()

    def write_content(item, file):
        if item['type'] == 'file':
            # If it's a file, download and write its content
            file_content = requests.get(item['download_url'], headers=headers).text
            file.write(f"\n\n--- File: {item['path']} ---\n\n")
            file.write(file_content)
        elif item['type'] == 'dir':
            # If it's a directory, recurse into it
            dir_contents = get_content(item['path'])
            for sub_item in dir_contents:
                write_content(sub_item, file)

    # Open the output file and start writing
    with open(output_file, 'w', encoding='utf-8') as f:
        contents = get_content()
        for item in contents:
            write_content(item, f)

    print(f"Repository contents have been saved to {output_file}")

# Example usage:
github_token = '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'
repository = "Ryuzaki1415/Dummy-Repo"
download_github_repo_to_txt(github_token, repository)