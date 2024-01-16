import requests
import os
from datetime import datetime


NUTRI_API_KEY = os.environ.get("NUTRI_API_KEY")
NUTRI_APP_ID = os.environ.get("NUTRI_APP_ID")
USERNAME = os.environ.get("USERNAME")
PWD = os.environ.get("PWD")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/3730eaa5fd563ea4ac199361ecfdcfdb/workoutTracking/workouts"



exercise_input = input("Tell me which exercise you did: ")
weight = float(input("What is your current weight (kg) : "))
height = float(input("What is your height (cm) : "))
age = int(input("How old are you : "))

parameters = {
    "query": exercise_input,
    "weight_kg": weight,
    "height_cm": height,
    "age": age,
}

headers = {"x-app-id": NUTRI_APP_ID, "x-app-key": NUTRI_API_KEY}

response = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise",
    json=parameters,
    headers=headers,
)
response.raise_for_status()
data_output = response.json()
print(data_output)


# SHEETY
date_now = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%H:%M:%S")


for exercise in data_output["exercises"]:
    sheet_input = {
        "workout": {
            "date": date_now,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(
        url=sheety_endpoint, json=sheet_input, auth=(USERNAME, PWD)
    )

    try:
        sheet_response.raise_for_status()
        print(sheet_response)
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
