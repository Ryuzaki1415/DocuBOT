# DOCUBOT ⚡📗

![Static Badge](https://img.shields.io/badge/Ollama-brightgreen) ![Static Badge](https://img.shields.io/badge/crewai-red) ![Static Badge](https://img.shields.io/badge/Groq-orange)

An advanced AI-powered tool that automatically generates comprehensive documentation for any GitHub repository. Utilizing a team of AI agents built on Crew AI, Docu-Bot Crew extracts content from repositories and creates detailed, well-structured documentation in markdown format.

## Features

- **AI-Powered Documentation**: Leverages a crew of AI agents to analyze and document GitHub repositories.
- **Comprehensive Analysis**: Extracts and processes content from various file types within the repository.
- **Collaborative AI Agents**: Utilizes function calling for inter-agent cooperation to complete complex tasks.
- **Flexible LLM Support**: Compatible with both local LLMs via Ollama and cloud-based solutions like Groq.
- **Markdown Output**: Generates well-formatted, detailed documentation in GitHub-flavored markdown.
- **Poetry Package Management**: Ensures easy setup and dependency management.


### Run this project 
```python


#clone this repo and navigate to root folder
git clone https://github.com/Ryuzaki1415/DocuBOT.git
#create virutal environment
python -m venv venv
#activate virutal environment
venv/Scripts/Activate
#install the dependencies
poetry install
# TO RUN DOCU-BOT
poetry run docubot
```

### Setup environments
```python


OPENAI_API_BASE='http://localhost:11434' # for Ollama
OPENAI_MODEL_NAME='llama3'  # Adjust based on available model
OPENAI_API_KEY='' # for ollama 
GITHUB_TOKEN=''  # GITHUB ACESS TOKEN 
GROQ_API_KEY=''  # If you are using GROQ instead of Ollama

```


### Understanding Your Crew

The DocuBot Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in the crew.


### Structure

-`src/docubot/crew.py` Contains the main logic and agent and task configuration.<br>
-`src/docubot/main.py` handles custom inputs and Driver code for the entire crew.

### Result
Final Generated Markdown would be saved in your computer.


### Screenshots
Main menu.
![Alt text](https://github.com/Ryuzaki1415/DocuBOT/blob/master/assets/Screenshot%202024-07-27%20201253.png)
Agent Function calling.
![Alt text](https://github.com/Ryuzaki1415/DocuBOT/blob/master/assets/Screenshot%202024-07-27%20201339.png)
![Alt text](https://github.com/Ryuzaki1415/DocuBOT/blob/master/assets/Screenshot%202024-07-27%20201518.png)
![Alt text](https://github.com/Ryuzaki1415/DocuBOT/blob/master/assets/Screenshot%202024-07-27%20201542.png)
![Alt text](https://github.com/Ryuzaki1415/DocuBOT/blob/master/assets/Screenshot%202024-07-27%20201613.png)

### Generated Document

Final report can be seen inside https://github.com/Ryuzaki1415/DocuBOT/blob/master/docubot/report.md


