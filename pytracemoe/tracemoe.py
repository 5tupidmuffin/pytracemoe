"""
pytracemoe is a api wrapper for trace.moe
"""


import requests, json, base64  # base64 is required for image encoding
from pytracemoe.containers import *


class TraceMOE:
    API_URL = "https://trace.moe/api/search"  # api url

    def __init__(self, min_similarity = None):
        self.min_similarity = min_similarity
        self.header = {
            'min_similarity': min_similarity
        }

    def from_url(self, imageurl):
        """
        sauce from image link
        takes image url as input
        returns TraceResults object
        """
        raw_data = requests.post(self.API_URL, params= {'url': imageurl})
        data = raw_data.json()
        listdata = list(data['docs'])

        return TraceResults(self.header, data, listdata)

    def from_image(self, pathtoimage):
        """
        sauce from image file
        takes image file's path as input
        returns TraceResults object
        """
        base64_encodedData = ""  # empty string
        with open(pathtoimage, 'rb') as file:
            base64_encodedData = base64.b64encode(file.read())
            # tracemoe's api requires the image to be enncoded in base64 to work properly

        raw_data = requests.post(self.API_URL, data= {'image': base64_encodedData})
        data = raw_data.json()
        listdata = list(data['docs'])

        return TraceResults(self.header, data, listdata)

