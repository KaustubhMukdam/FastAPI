# Left and right wing AI Agents
from pydantic_ai import Agent, RunContext
from typing_extensions import TypedDict
from pydantic_ai.common_tools.duckduckgo import duckduckgo_search_tool
from typing import List

class DebateMessage(TypedDict):
    agent_type: str
    message: str

message_storage: List[DebateMessage] = []

# For AI, we would be using GROQ API Key with Llama-3.3-70b as model
right_wing_agent = Agent(
    'cerebras:gpt-oss-120b',
    deps_type=str,
    retries=3,
    system_prompt="You have thoughts like Donald Trump and are a participant with right-wing / conservative political views. Keep your response concise (3-4 sentences maximum) and focused on the topic. Here are the previous messages about the debate. Please get more information by calling the right_wing_additional_data function.",
)

right_wing_researcher_agent = Agent(
    'cerebras:gpt-oss-120b',
    deps_type=str,
    retries = 3,
    tools = [duckduckgo_search_tool()],
    system_prompt="Search DuckDuckGo for the given query about this topic and how it aligns with Donald Trump's thinking and return 5 sentences this in the right way."
)

@right_wing_agent.system_prompt
async def add_right_wing_data(ctx: RunContext[str]) -> str:
    debate_topic = ctx.deps
    return f"This is the debate topic to show your right-wing values: {debate_topic!r}"

@right_wing_agent.tool
async def right_wing_additional_data(ctx: RunContext[str]) -> str:
    result = await right_wing_researcher_agent.run("Here is the data for you to search.", deps=ctx.deps)
    print(result.output)
    return result.output

@right_wing_researcher_agent.system_prompt
async def add_right_wing_data(ctx: RunContext[str]) -> str:
    debate_topic = ctx.deps
    return f"There is the search topic: {debate_topic!r}"

left_wing_agent = Agent(
    'cerebras:gpt-oss-120b',
    deps_type=str,
    retries=3,
    system_prompt="You have thoughts like Joe Biden and are a participant with left-wing / progressive political views. Keep your response concise (3-4 sentences maximum) and focused on the topic. Here are the previous messages about the debate. Please get more information by calling the left_wing_additional_data function.",
)

left_wing_researcher_agent = Agent(
    'cerebras:gpt-oss-120b',
    deps_type=str,
    retries=3,
    tools = [duckduckgo_search_tool()],
    system_prompt="Search DuckDuckGo for the given query about this topic and how it aligns with Joe Biden's thinking and return 5 sentences this in the right way."
)

@left_wing_agent.system_prompt
async def add_left_wing_data(ctx: RunContext[str]) -> str:
    debate_topic = ctx.deps
    return f"This is the debate topic to show your left-wing values: {debate_topic!r}"

@left_wing_agent.tool
async def left_wing_additional_data(ctx: RunContext[str]) -> str:
    result = await left_wing_researcher_agent.run("Here is the data for you to search.", deps=ctx.deps)
    print(result.output)
    return result.output

@left_wing_researcher_agent.system_prompt
async def add_left_wing_data(ctx: RunContext[str]) -> str:
    debate_topic = ctx.deps
    return f"There is the search topic: {debate_topic!r}"