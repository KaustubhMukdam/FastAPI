from app.debate.agents import right_wing_agent, left_wing_agent, message_storage

async def analyze_profile(query: str) -> str:
    result_right = await right_wing_agent.run("Here is the debate topic", deps=query)
    message_storage.append({"agent_type" : "right_wing", "message" : result_right.output})
    result_left = await left_wing_agent.run("Here is the debate topic", deps=query)
    message_storage.append({"agent_type" : "left_wing", "message" : result_left.output})
    return {"Donald Trump Thoughts: " : result_right.output, "Joe Biden Thoughts: " : result_left.output}