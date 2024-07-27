#!/usr/bin/env python
import sys
from docubot.crew import DocubotCrew
import os
import requests



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
            
            
            





def run():
    """
    Run the crew.
    """
    print('''\
              
          
 _    _ _____ _     _____ ________  ___ _____   _____ _____   ______ _____ _____ _   _______  _____ _____ _ 
| |  | |  ___| |   /  __ \  _  |  \/  ||  ___| |_   _|  _  |  |  _  \  _  /  __ \ | | | ___ \|  _  |_   _| |
| |  | | |__ | |   | /  \/ | | | .  . || |__     | | | | | |  | | | | | | | /  \/ | | | |_/ /| | | | | | | |
| |/\| |  __|| |   | |   | | | | |\/| ||  __|    | | | | | |  | | | | | | | |   | | | | ___ \| | | | | | | |
\  /\  / |___| |___| \__/\ \_/ / |  | || |___    | | \ \_/ /  | |/ /\ \_/ / \__/\ |_| | |_/ /\ \_/ / | | |_|
 \/  \/\____/\_____/\____/\___/\_|  |_/\____/    \_/  \___/   |___/  \___/ \____/\___/\____/  \___/  \_/ (_)
                                                                                                            
                                                                                                          
                        Write Documentation for your projects easily with AI Agents!        
          ''')
    
    acnt_name = input(" Please enter the name of the Github Account :")
    token = os.environ.get('GITHUB_TOKEN')  # Replace with your GitHub personal access token if needed
    selected_repo = select_github_repo(acnt_name, token)
    if selected_repo:
        print(f"You selected: {selected_repo}")
        inputs = {
            'repo_name': acnt_name+"/"+selected_repo
        }
        DocubotCrew().crew().kickoff(inputs=inputs)
        example_file = r"D:\DOCU-BOT\docubot\report.md"
        abs_path = os.path.abspath(example_file)
        file_uri = f'file:///{abs_path.replace(os.sep, "/")}'
        link_message = f"Your file is located here!..... <a href='{file_uri}'>{abs_path}</a>"
        print(link_message)
        


