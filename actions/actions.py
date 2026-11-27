from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

flights = [
    "United Airlines - Miami to Chicago",
    "American Airlines - New York to Chicago",
    "Delta Airlines - Atlanta to Chicago",
    "Southwest Airlines - Dallas to Chicago",
    "JetBlue - Boston to Chicago",
    "Spirit Airlines - Orlando to Chicago",
    "Alaska Airlines - Seattle to Chicago",
    "Frontier Airlines - Denver to Chicago",
    "United Airlines - Los Angeles to Chicago",
    "American Airlines - Phoenix to Chicago",
    "Delta Airlines - Detroit to Chicago",
    "Southwest Airlines - Houston to Chicago",
    "JetBlue - Fort Lauderdale to Chicago",
    "Spirit Airlines - Tampa to Chicago",
    "United Airlines - Newark to Chicago",
    "American Airlines - Charlotte to Chicago",
    "Delta Airlines - Minneapolis to Chicago",
    "Southwest Airlines - Nashville to Chicago",
    "JetBlue - JFK to Chicago",
    "Alaska Airlines - Portland to Chicago"
]

hotels = [
    "Hilton Chicago Downtown",
    "Hyatt Regency Chicago",
    "The Langham Chicago",
    "Marriott Magnificent Mile",
    "Sheraton Grand Chicago",
    "Westin Ohare",
    "Hilton Ohare Airport",
    "Crowne Plaza Ohare",
    "Embassy Suites Downtown",
    "Palmer House Hilton"
]

restaurants = [
    "Giordanos",
    "Lou Malnatis",
    "Pequods Pizza",
    "Gibsons Steakhouse",
    "Fogo de Chao",
    "Portillos",
    "Greek Islands",
    "Quartino",
    "RPM Italian",
    "Chicago Cut Steakhouse",
    "Bavettes Bar & Boeuf",
    "Pizzeria Uno",
    "Pizzeria Due",
    "Als Beef",
    "Gene and Georgetti",
    "Rosebud on Rush",
    "The Purple Pig",
    "Cindy's Rooftop",
    "Joe's Seafood",
    "Siena Tavern"
]

class ActionSearchFlights(Action):

    def name(self) -> Text:
        return "action_search_flights"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Available Flights to Chicago:\n" + "\n".join(flights))
        return []

class ActionSearchHotels(Action):

    def name(self) -> Text:
        return "action_search_hotels"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Available Hotels:\n" + "\n".join(hotels))
        return []

class ActionSearchRestaurants(Action):

    def name(self) -> Text:
        return "action_search_restaurants"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Popular Chicago Restaurants:\n" + "\n".join(restaurants))
        return []

class ActionRestaurantAddress(Action):

    def name(self) -> Text:
        return "action_restaurant_address"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Fogo de Chao Address: 661 N La Salle Dr, Chicago, IL 60654")
        return []

class ActionPurchaseFlight(Action):

    def name(self) -> Text:
        return "action_purchase_flight"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Your airline tickets for 3 passengers have been reserved.")
        return []

class ActionReserveHotel(Action):

    def name(self) -> Text:
        return "action_reserve_hotel"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Your hotel reservation for 3 guests has been confirmed.")
        return []

class ActionReserveRestaurant(Action):

    def name(self) -> Text:
        return "action_reserve_restaurant"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Your dinner reservation at Gibsons Steakhouse for 3 guests is confirmed.")
        return []

class ActionTripPlan(Action):

    def name(self) -> Text:
        return "action_trip_plan"

    def run(self, dispatcher, tracker, domain):
        message = """
Recommended Chicago Business Trip Plan:

Flight:
- Evening United Airlines flight from Miami to Chicago on Tuesday
- Return Friday evening

Hotel:
- Hyatt Regency Chicago Downtown

Food Recommendations:
- Lou Malnatis for Chicago-style pizza
- Portillos for Chicago-style hotdogs
- Gibsons Steakhouse for business dinner meetings

Transportation:
- Uber and CTA trains available throughout downtown Chicago

All recommendations fit a corporate travel budget.
"""
        dispatcher.utter_message(text=message)
        return []
