class Quotes:

    def __init__(self):
        import time


    # Gets a Kanye West Quote
    def KanyeWest(self, count=1):
        import requests
        res = []

        # Range of count
        for x in range(0,count):
            r = requests.get('https://api.kanye.rest/?format=text')
            res.append(r.text)

        return res

    def Trump(self, random=True, topic=None, meme=False, count=1):
        import requests
        import urllib
        import json

        res = []

        for x in range(0,count):
            if random == True:
                r = requests.get("https://api.tronalddump.io/random/quote")
                data = json.loads(r.text)
                json = {}

                json['quote'] = data['value']
                json['appeared_at'] = data['appeared_at']
                json['url'] = data['_embedded']['source'][0]['url']

                res.append(json)

        if random == False:
            if topic != None:
                r = requests.get("https://api.tronalddump.io/search/quote?query=" + urllib.parse.quote(topic))
                data = json.loads(r.text)

                if int(data['count']) == 0:
                    return "No quotes found about that topic."
                else:
                    for x in range(0,count):
                        json = {}

                        try:
                            json['quote'] = data['_embedded']['quotes'][x]['value']
                            json['appeared_at'] = data['_embedded']['quotes'][x]['appeared_at']
                            json['url'] = data['_embedded']['quotes'][x]['_embedded']['source'][0]['url']
                            res.append(json)
                        except:
                            return res

            elif meme != False:
                for x in range(0,count):
                    r = requests.get("https://api.tronalddump.io/random/meme")
                    res.append(r.content)

        return res


    def RonSwanson(self, count=1):
        import requests
        
        r = requests.get("http://ron-swanson-quotes.herokuapp.com/v2/quotes/" + str(count))

        array = r.text.replace('["', "").replace('"]', "").split('","')
        return array


    def BreakingBad(self, count=1):
        import requests
        import json

        r = requests.get("https://breaking-bad-quotes.herokuapp.com/v1/quotes/" + str(count))

        json = json.loads(r.text)

        return json

            
