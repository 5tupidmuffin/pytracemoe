"""
pytracemoe is a api wrapper for trace.moe
"""


import requests
from pytracemoe.containers import *


class TraceMOE:
    API_URL = "https://api.trace.moe/search?anilistInfo"  # api url

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
        listdata = list(data['result'])

        return TraceResults(self.header, data, listdata)

    def from_image(self, pathtoimage):
        """
        sauce from image file
        takes image file's path as input
        returns TraceResults object
        """

        raw_data = requests.post(self.API_URL, files= {'image': open(pathtoimage, 'rb')})  # newer api reads image in binary format
        data = raw_data.json()
        listdata = list(data['result'])

        return TraceResults(self.header, data, listdata)

