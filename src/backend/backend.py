# RouteGenie WhatsApp Bot with Meta WhatsApp Cloud API
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Dummy stops data (could be dynamic in production)
stops = [
    {"name": "In-N-Out Burger", "location": {"lat": 36.0165, "lng": -120.125}},
    {"name": "Tesla Supercharger", "location": {"lat": 35.2701, "lng": -119.2704}},
    {"name": "Chevron Station", "location": {"lat": 34.9401, "lng": -118.1534}},
]

# Create a Google Maps link with waypoints
def generate_google_maps_link(origin, destination, stops):
    """
    Generate a Google Maps link with waypoints.
    :param origin: Starting point
    :param destination: Destination point
    :param stops: List of stops with lat/lng
    :return: Google Maps URL with waypoints"""
    waypoints = "|".join(
        f"{stop['location']['lat']},{stop['location']['lng']}" for stop in stops
    )
    return (
        f"https://www.google.com/maps/dir/?api=1"
        f"&origin={origin.replace(' ', '+')}"
        f"&destination={destination.replace(' ', '+')}"
        f"&waypoints={waypoints}"
    )

# Itinerary builder
def generate_itinerary(origin="San Francisco, CA", destination="Los Angeles, CA", vehicle_type="gas"):
    """
    Generate a personalized itinerary based on vehicle type.
    :param origin: Starting point
    :param destination: Destination point
    :param vehicle_type: Type of vehicle (gas or ev)
    :return: Itinerary string"""
    if vehicle_type.lower() == "ev":
        fuel_stop = "Stop 2: Tesla Supercharger (Buttonwillow)"
    else:
        fuel_stop = "Stop 2: Shell Gas Station (Buttonwillow)"
    
    itinerary_text = (
        "Stop 1: In-N-Out Burger (Food)\n"
        f"{fuel_stop} (Fuel)\n"
        "Stop 3: Chevron Station (Restroom Break)"
    )
    
    gmap = generate_google_maps_link(origin, destination, stops)
    logger.info(f"Generated Google Maps link: {gmap}")

    payload = f"🧭 RouteGenie Itinerary from {origin} to {destination}:\n{itinerary_text}\n\n📍 Google Maps: {gmap}"
    logger.info(f"Generated itinerary: {payload}")
    
    return payload

