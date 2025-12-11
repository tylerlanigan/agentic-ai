from pydantic import BaseModel
from typing import List
import datetime
from enum import Enum
from utils import Interest


class Traveler(BaseModel):
    """A traveler with a name, age, and list of interests.
    
    Attributes:
        name (str): The name of the traveler.
        age (int): The age of the traveler.
        interests (List[Interest]): A list of interests of the traveler.
    """
    name: str
    age: int
    interests: List[Interest]

class VacationInfo(BaseModel):
    """Vacation information including travelers, destination, dates, and budget.
    Attributes:
        travelers (List[Traveler]): A list of travelers.
        destination (str): The vacation destination.
        date_of_arrival (datetime.date): The date of arrival.
        date_of_departure (datetime.date): The date of departure.
        budget (int): The budget for the vacation in fictional currency units.
    """
    travelers: List[Traveler]
    destination: str
    date_of_arrival: datetime.date
    date_of_departure: datetime.date
    budget: int

class Weather(BaseModel):
    temperature: float
    temperature_unit: str
    condition: str


class Activity(BaseModel):
    activity_id: str
    name: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    location: str
    description: str
    price: int
    related_interests: List[Interest]


class ActivityRecommendation(BaseModel):
    activity: Activity
    reasons_for_recommendation: List[str]


class ItineraryDay(BaseModel):
    date: datetime.date
    weather: Weather
    activity_recommendations: List[ActivityRecommendation]


class TravelPlan(BaseModel):
    city: str
    start_date: datetime.date
    end_date: datetime.date
    total_cost: int
    itinerary_days: List[ItineraryDay]

class EvaluationResults(BaseModel):
    success: bool
    failures: List[str]
    eval_functions: List[str]