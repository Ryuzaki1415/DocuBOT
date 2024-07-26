import requests
import os

def select_github_repo(username, token=None):
    # GitHub API endpoint for user repositories
    url = f"https://api.github.com/users/{username}/repos"
    
    # Set up headers if token is provided
    headers = {"Authorization": f"token {token}"} if token else {}
    
    # Make the API request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: Unable to fetch repositories. Status code: {response.status_code}")
        return None
    
    # Parse the JSON response
    repos = response.json()
    
    # Display the list of repositories
    print(f"Repositories for {username}:")
    for i, repo in enumerate(repos, 1):
        print(f"{i}. {repo['name']}")
    
    # Get user selection
    while True:
        try:
            selection = int(input("Enter the number of the repository you want to select: "))
            if 1 <= selection <= len(repos):
                selected_repo = repos[selection - 1]['name']
                return selected_repo
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Example usage
if __name__ == "__main__":
    username = "#######"  # Replace with the GitHub username you want to query
    token = os.environ.get('GITHUB_TOKEN')  # Replace with your GitHub personal access token if needed
    
    selected_repo = select_github_repo(username, token)
    if selected_repo:
        print(f"You selected: {selected_repo}")
        # You can now use 'selected_repo' in your code