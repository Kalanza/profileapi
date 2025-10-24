from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests
import logging
from datetime import datetime

# Configure logging
logger = logging.getLogger(__name__)

# Create your views here.

class ProfileView(APIView):
    """
    API endpoint that returns user profile information along with a random cat fact.
    """
    
    def get(self, request):
        # Generate UTC timestamp in ISO 8601 format
        timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        
        # Initialize cat fact with fallback message
        cat_fact = "Could not fetch cat fact at this time."
        
        # Resolve API URL from settings with a safe default to avoid AttributeError
        api_url = getattr(settings, "CAT_FACTS_API_URL", "https://catfact.ninja/fact")
        
        try:
            # Log the external API call attempt
            logger.info(f"Attempting to fetch cat fact from {api_url}")

            # Fetch cat fact from external API
            response = requests.get(api_url, timeout=5)
            response.raise_for_status()  # Raise exception for bad status codes
            cat_fact_data = response.json()
            
            # Extract the cat fact
            cat_fact = cat_fact_data.get("fact", "No cat fact available")
            
            # Log successful fetch
            logger.info(f"Successfully fetched cat fact: {cat_fact[:50]}...")
            
        except requests.exceptions.RequestException as e:
            # Log the error but continue with fallback message
            logger.error(f"Failed to fetch cat fact: {str(e)}")
            # cat_fact already has fallback message
        
        # Build the profile response with required structure
        profile_data = {
            "status": "success",
            "user": {
                "email": settings.MY_EMAIL,
                "name": settings.MY_NAME,
                "stack": settings.MY_STACK
            },
            "timestamp": timestamp,
            "fact": cat_fact
        }
        
        # Always return 200 OK as per requirements
        return Response(profile_data, status=status.HTTP_200_OK)