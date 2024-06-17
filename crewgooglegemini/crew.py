from crewai import Crew,Process
from agents import news_researcher, news_writer
from tasks import research_task, writer_task

# forming a crew 
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, writer_task],
    process= Process.sequential,
)

# starting task exe 
anime_name = "Another anime"
result = crew.kickoff(inputs={"topic":anime_name})
print(result)