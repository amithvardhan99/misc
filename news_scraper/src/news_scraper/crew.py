from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import FileWriterTool, ScrapeWebsiteTool, SerperDevTool
from dotenv import load_dotenv
load_dotenv()
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class NewsScraper():
    """NewsScraper crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    llm_model = LLM(
        model="llama3.2:1b",
        base_url="http://localhost:11434",
    )

    @agent
    def google_search(self) -> Agent:
        return Agent(
            config=self.agents_config['google_search'], 
            tools=[SerperDevTool()],
            verbose=True,
            llm=llm_model,
        )

    @agent
    def news_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['news_scraper'], 
            tools=[ScrapeWebsiteTool()],
            verbose=True,
            llm=llm_model,
        )
    
    @agent
    def news_summariser(self) -> Agent:
        return Agent(
            config=self.agents_config['news_summariser'], 
            tools=[],
            verbose=True,
            llm=llm_model,
        )

    @agent
    def save_news_articles(self) -> Agent:
        return Agent(
            config=self.agents_config['save_news_articles'], 
            tools=[FileWriterTool()],
            verbose=True,
            llm=llm_model,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def google_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['google_search_task'], # type: ignore[index]
        )

    @task
    def news_scraper_task(self) -> Task:
        return Task(
            config=self.tasks_config['news_scraper_task'], # type: ignore[index]
        )
    
    @task
    def news_summariser_task(self) -> Task:
        return Task(
            config=self.tasks_config['news_summariser_task'], # type: ignore[index]
        )

    @task
    def save_news_articles_task(self) -> Task:
        return Task(
            config=self.tasks_config['save_news_articles_task'], # type: ignore[index]
            output_file='report.md'
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the NewsScraper crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
