from abc import ABCMeta
from abc import abstractmethod


def load_sources(file_path: str = ''):
    return [1]


class Rule:
    __metaclass__ = ABCMeta

    @abstractmethod
    def validate(self, document: dict, user_country: str):
        pass

    @abstractmethod
    def apply(self, document):
        pass


class ContentRestriction(Rule):
    def __init__(self) -> None:
        self.restricted_ids = load_sources(file_path='china.sources')

    def validate(self, document: dict, user_country: str) -> bool:
        return user_country == 'cn' and int(document['sourceId']) in self.restricted_ids

    def apply(self, document: dict) -> dict:
        document['body'] = ''
        document['ingress'] = ''
        document['title'] = 'Content from this publisher is not available in your country'
        document['sourceUrl'] = ''
        document['keywords'] = ''
        document['source'] = ''
        document['date'] = ''
        return document


class ApacContentRestriction(Rule):
    def __init__(self) -> None:
        self.restricted_ids = load_sources(file_path='apac.sources')

    def validate(self, document: dict, user_country: str) -> bool:
        return user_country == 'cn' and int(document['sourceId']) in self.restricted_ids

    def apply(self, document: dict) -> dict:
        document['body'] = ''
        document['ingress'] = ''
        document['title'] = 'Content from this publisher is not available in your country'
        document['sourceUrl'] = ''
        document['keywords'] = ''
        document['source'] = ''
        document['date'] = ''
        return document
