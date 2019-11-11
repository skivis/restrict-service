import json
import uuid
import random


def uniqueid():
    uid = uuid.uuid1()
    return str(uid.hex)


doc_list = []


words = "Pricing Of Private Aircrafts Will Skyrocket 2026".split()



for i, x in enumerate(['cn', 'fr', 'se', 'dk', 'ca', 'us', 'cn', 'au', 'es'], start=1):
    random.shuffle(words)
    doc = {
        "_id": uniqueid(),
        "title": ' '.join(words),
        "ingress": ' '.join(words),
        "body": ' '.join(words),
        "date": "2017-10-16T11:00:00.856Z",
        "sourceId": str(i),
        "source": "MJA.DK",
        "sourceUrl": "http://www.mja.dk/",
        "language": "en",
        "country": x,
        "keywords": [
            "regulations"
        ]
    }
    doc_list.append(doc)

print json.dumps(doc_list, indent=4, sort_keys=True)