from crewai import Agent
from dotenv import load_dotenv
load_dotenv()
import os

from tools import tools_search

from langchain_google_genai import ChatGoogleGenerativeAI

# call the gemini model bcoz mufat ka hai default is GPT 4 which requires paisa
llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    verbose = True,
    temperature = 0.8,
    google_api_key = os.getenv("GEMINI_API_KEY")
)

# Creating agents 
news_researcher = Agent(
    role = "Senior Researcher",
    goal = "Uncover latest and fascinating news for {topic} anime",
    verbose = True,
    memory = True,
    backstory = (
        "Driven by curiosity, you are an anime fan who is eager to explore and share new animes with the world. "
        # "You are known for your insightful analyses and thorough research."
        # "Your mission is to provide the most accurate and fascinating information about specific anime, "
        "uncovering hidden gems, fascinating information and lesser-known facts to share with fellow fans."
    ),
    tools=[tools_search],
    llm = llm,
    allow_delegation = True,
    
)

# creating writer agent 
news_writer = Agent (
    role = "Writer",
    goal = "Narrate engaging anime news and facts about {topic}",
    verbose = True,
    memory = True,
    backstory = (
        "You have a deep love for story telling and anime. you began writing inspired by the captivating animes you watched. "
        "Your emotional depth, and touch of humor bring research to life, making newsletter content engaging and relatable. "
        # "Your mission is to connect with readers, sharing your passion for anime and sparking excitement about the featured series."
    ),
    tools=[tools_search],
    llm = llm,
    allow_delegation = True, 
)