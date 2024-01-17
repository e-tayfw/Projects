# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

get_sheety_endpoint = (
    "https://api.sheety.co/3730eaa5fd563ea4ac199361ecfdcfdb/flightDeals/prices"
)

put_sheety_endpoint = (
    "https://api.sheety.co/3730eaa5fd563ea4ac199361ecfdcfdb/flightDeals/prices"
)


data_manager = DataManager(get_sheety_endpoint, put_sheety_endpoint)
flight_search = FlightSearch()
tomorrow = datetime.now() + timedelta(days=1)
six_mths_frm_tday = datetime.now() + timedelta(days=(6 * 30))

sheet_data = data_manager.get_data()
for obj in sheet_data:
    to_city_name_code = flight_search.get_destination(obj["city"])
    print(to_city_name_code)

    if len(obj["iataCode"]) == 0:
        sheet_update = {"price": {"iataCode": to_city_name_code}}
        data_manager.update_data(obj["id"], sheet_update)

    sheet_lowest_price = obj["lowestPrice"]

    flight = flight_search.get_flights(
        "SIN",
        to_city_name_code,
        tomorrow,
        six_mths_frm_tday,
    )
    if flight != None:
        if flight.price < sheet_lowest_price:
            notification = NotificationManager()
            msg = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            notification.send_sms(message=msg)
