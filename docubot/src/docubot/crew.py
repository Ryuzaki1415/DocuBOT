from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_community.llms import Ollama
from crewai_tools import FileReadTool
import os
from langchain_groq import ChatGroq
from crewai_tools import tool
import requests
import base64
from urllib.parse import urljoin


# LLMS
ollamallm = Ollama(
    model = "llama3",
    base_url = "http://localhost:11434")

os.environ["OPENAI_API_KEY"] = "NA"

groqllm = ChatGroq(
            temperature=0, 
            groq_api_key = os.environ.get('GROQ_API_KEY'), 
            model_name='Mixtral-8x7b-32768'
        )


# TOOLS

file_read_tool = FileReadTool(file_path='repo_contents.txt')
@tool("Github_to_text_file")
def Github_to_text_file(repo_name:str): 
    """This tool reads the contents of a github repo and converts it into a text file."""
    github_token = os.environ.get('GITHUB_TOKEN')
    output_file='repo_contents.txt'
    base_url = "https://api.github.com/"
    headers={
		"Authorization":f"token{github_token}"
	}
    def get_content(path=''):
        repo_url=urljoin(base_url, f"repos/{repo_name}/contents/{path}")
        response = requests.get(repo_url, headers=headers)
        response.raise_for_status()
        return response.json()
    def write_content(item,file):
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
    with open(output_file,'w', encoding='utf-8') as f:
        contents=get_content()
        for item in contents:
            write_content(item,f)
    print(f"Repository contents have been saved to {output_file}")
    return("Success")        
    
    
    

    

@CrewBase
class DocubotCrew():
	"""Docubot crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def documentation_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['documentation_engineer'],
			verbose=True,
   			llm=groqllm,
			tools=[Github_to_text_file],
   			max_iter=10
      
		)

	@agent
	def senior_documentation_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['senior_documentation_engineer'],
			verbose=True,
   			llm=groqllm,
			tools=[file_read_tool],
   			max_iter=15
		)

	@task
	def documentation_task(self) -> Task:
		return Task(
			config=self.tasks_config['documentation_task'],
			agent=self.documentation_engineer()
		)

	@task
	def documentation_review_task(self) -> Task:
		return Task(
			config=self.tasks_config['documentation_review_task'],
			agent=self.senior_documentation_engineer(),
			output_file='report.md'
		)
	
	@crew
	def crew(self) -> Crew:
		"""Creates the Docubot crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=2,
			
		)