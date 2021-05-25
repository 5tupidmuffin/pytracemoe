"""
classses made for ease of access to the results
"""


class genericresult:
    def __init__(self, data):
        self.title_english  = data['anilist']['title']['english']  # title in English
        self.title_romaji   = data['anilist']['title']['romaji']   # in romaji
        self.title_japanese = data['anilist']['title']['native']  # title in native japanese
        self.episode        = data['episode']  # episode number
        self.similarity     = float('%.2f' % (data['similarity']*100))  # similarity percentage
        self.timestamp      = data['from']  # exact timestamp
        self.anilist_id     = data['anilist']['id']  # anilisi id of the anime
        self.mal_id         = data['anilist']['idMal']  # MAL id of the anime
        self.is_hentai      = data['anilist']['isAdult']  # is hentai or not


class TraceResults:
    def __init__(self, header, response, resultsList):
        self.resultsCount   = len(resultsList)  # total number of results
        self.results        = resultsList  # list of results
        self.header         = header  # data for TraceMOE class
        self.finalresults   = self.processResults(self.results)  # processed results

    def processResults(self, resultslist):  # processing every result in resultslist(docs in json response) list
        if resultslist is None or len(resultslist) == 0:
            return

        templist = []
        if self.header['min_similarity']:
            for result in resultslist:
                if (result['similarity'] * 100) >= self.header['min_similarity']:
                    tempresult = genericresult(result)  # converting each result in genericresult object
                    templist.append(tempresult)
            return templist
        else:
            for result in resultslist:
                tempresult = genericresult(result)
                templist.append(tempresult)
            return templist


    def __getitem__(self, item):  # access results through index number
        return self.finalresults[item]

    def __len__(self):  # return numeber of results
        return self.resultsCount

    def __bool__(self):  # return a True if results exist
        return self.resultsCount >= 1

