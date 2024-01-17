import requests
import os
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = os.environ.get("ENV_TEQUILA_API")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "term": city_name,
            "location_types": "city",
        }

        response = requests.get(url=location_endpoint, params=query, headers=headers)
        response.raise_for_status()
        flightSearch_data = response.json()
        return flightSearch_data["locations"][0]["code"]

    def get_flights(self, origin_city_code, to_city_code, from_time, to_time):
        get_flights_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": to_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(url=get_flights_endpoint, params=query, headers=headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {to_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        return flight_data
