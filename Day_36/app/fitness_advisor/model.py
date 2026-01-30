from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class ActivityLevel(str, Enum):
    SEDENTARY = "sedentary"
    LIGHT = "light"
    MODERATE = "moderate"
    VERY_ACTIVE = "very_active"
    ATHLETE = "athlete"

class FitnessGoal(str, Enum):
    WEIGHT_LOSS = "weight_loss"
    MUSCLE_GAIN = "muscle_gain"
    MAINTENANCE = "maintenance"
    ENDURANCE = "endurance"
    STRENGTH = "strength"

class Exercise(BaseModel):
    name: str
    sets: int
    reps: int
    rest_time: int = Field(..., description="Rest time in seconds between sets")

class Meal(BaseModel):
    name: str
    calories: int
    protein: float
    carbs: float
    fats: float
    timing: str = Field(..., description="Timing of the meal, e.g., breakfast, lunch, dinner, snack")

class FitnessProfile(BaseModel):
    age: int
    weight: float
    height: float
    gender: str
    activity_level: ActivityLevel
    fitness_goal: FitnessGoal
    dietary_restrictions: Optional[List[str]] = None
    injuries: Optional[List[str]] = None
    preferred_workout_time: Optional[str] = None  # e.g., "morning", "afternoon", "evening"
    available_equipment: Optional[List[str]] = None
    workout_days_per_week: int

class FitnessReportResult(BaseModel):
    workout_plan: List[Exercise] = Field(..., description="Personalized workout plan based on the user's profile")
    meal_plan: List[Meal] = Field(..., description="Personalized meal plan based on the user's profile")
    daily_calories: int = Field(..., description="Recommended daily calorie intake")
    macros: dict = Field(..., description="Recommended macronutrient distribution")
    tips: List[str] = Field(..., description="Additional fitness and nutrition tips")
    weekly_schedule: dict = Field(..., description="Weekly schedule outlining workouts and meals")
    motivational_quotes: List[str] = Field(..., description="Motivational quotes to boost motivation")
    