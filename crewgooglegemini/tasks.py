from crewai import Task
from tools import tools_search
from agents import news_researcher, news_writer
# research task 
research_task = Task(
    description =(
        """Conduct research on {topic}
        Identify the latest news, and intriguing facts about the anime.
        Gather information from credible sources, including interviews with creators and cultural context."""
    ),
    expected_output="""A comprehensive 3 paragraph long news report""",
    # the announcement of a new season for a popular anime, or the launch of a new anime streaming service.
    tools = [tools_search],
    agent = news_researcher,
)

# writing task with language model configuration
writer_task = Task(
    description =(
        # Focus on the latest news, and how the audience reaction to the news.
        """Compose an insightful article on {topic} without spoilers.
        The report should be positive, easy to understand and informative"""
    ),
    expected_output="""A comprehensive 4 paragraph long news report on {topic} advancements formatted as markdown.""",
    tools = [tools_search],
    agent = news_writer,
    async_execution=False,
    output_file="news_report3.md" #output customization
)
