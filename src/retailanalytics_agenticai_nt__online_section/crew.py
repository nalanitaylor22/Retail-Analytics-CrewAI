import os


from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	PDFSearchTool
)






@CrewBase
class RetailanalyticsAgenticaiNtOnlineSectionCrew:
    """RetailanalyticsAgenticaiNtOnlineSection crew"""

    
    @agent
    def retail_analytics_specialist(self) -> Agent:
        
        
        embedding_config_pdfsearchtool = dict(
            embedding_model=dict(
                provider="openai",
                config=dict(
                    model="text-embedding-3-small",
                ),
            ),
        )
        
        return Agent(
            config=self.agents_config["retail_analytics_specialist"],
            
            
            tools=[				PDFSearchTool(config=embedding_config_pdfsearchtool, pdf="https://drive.google.com/uc?export=download&id=14GHJd_eTlwAfm_0n0EGquttQMzqdkoVW")],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def business_strategy_advisor_communicator(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["business_strategy_advisor_communicator"],
            
            
            tools=[],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            apps=[
                    "gmail/send-email@private",
                    ],
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    

    
    @task
    def analyze_retail_performance_data(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_retail_performance_data"],
            markdown=False,
            
            
        )
    
    @task
    def draft_and_send_executive_email(self) -> Task:
        return Task(
            config=self.tasks_config["draft_and_send_executive_email"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the RetailanalyticsAgenticaiNtOnlineSection crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            chat_llm=LLM(model="openai/gpt-4o"),
        )


