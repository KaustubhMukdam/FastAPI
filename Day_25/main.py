from fastapi import FastAPI
from random import randint
import copy
from opentelemetry import trace

tracer = trace.get_tracer("diceroller.tracer")

app = FastAPI()

dice_roll = [[], [], []]

# --- API endpoint ---

# --- GET Request Methods ---
@app.get("/rolldice")
async def roll_dice():
    count = 0

    #Roll dice and distribute it to 3 separate lists
    while count < 15:
        if count < 5:
            dice_roll[0].append(roll())

        elif count < 10:
            dice_roll[1].append(roll())

        else:
            dice_roll[2].append(roll())

        count += 1

    result = copy.deepcopy(dice_roll)

    #Now we would clear the lists for next function call after returning the result
    dice_roll[0].clear()
    dice_roll[1].clear()
    dice_roll[2].clear()

    return {"dice_rolls": result}

def roll():
    with tracer.start_as_current_span("roll") as rollspan:
        result = randint(1, 6)
        rollspan.set_attribute("roll.value", result)
        return result
