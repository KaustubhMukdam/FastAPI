from pydantic_ai import Agent, RunContext
from app.fitness_advisor.model import FitnessProfile, FitnessReportResult
from typing import List

fitness_agent = Agent[FitnessProfile, FitnessReportResult](
    'cerebras:gpt-oss-120b',
    deps_type=FitnessProfile,
    system_prompt="Create a personalized FitnessReportResult based on user's information provided. for motivational quotes, include quotes from famous fitness personalities and general motivational quotes related to health and wellness.",
)

motivational_agent = Agent[None, list[str]](
    'cerebras:gpt-oss-120b',
    system_prompt="Generate a list of 5 additional motivational quotes to inspire users on their fitness journey.",
)

@fitness_agent.system_prompt
async def add_user_fitness_data(ctx: RunContext[FitnessProfile]) -> str:
    fitness_data = ctx.deps
    return f"User fitness profile and goals: {fitness_data!r}"

@fitness_agent.tool
async def get_motivation(ctx: RunContext) -> List[str]:
    result = await motivational_agent.run(
        f"Generate 5 motivational quotes for a user with the following profile: {ctx.deps!r}"
    )
    return result.output

async def analyze_profile(profile: FitnessProfile) -> FitnessReportResult:
    result = await fitness_agent.run("Create a personalized fitness and nutrition report.", deps=profile)
    return result.output