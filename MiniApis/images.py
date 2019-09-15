class Images:

    def __init__(self):
        import time


    def generateBill(self, name="David", sex="m", count=1):
        import requests

        res = []

        for x in range(0,count):
            r = requests.get("https://belikebill.ga/billgen-API.php?default=1&name=" + name + "&sex=" + sex)
            res.append(r.content)

        return res