from enum import Enum


class Restriction(Enum):
    CHINA_RESTRICTED = 'CHINA_RESTRICTED'
    NOT_RESTRICTED = 'NOT_RESTRICTED'
    NLA_RESTRICTED = 'NLA_RESTRICTED'
    APAC_RESTRICTED = 'APAC_PREMIUM_RESTRICTED'


class Struct:
    def __init__(self, data):
        self.__dict__.update(data)
        for k, v in data.items():
            if isinstance(v, dict):
                self.__dict__[k] = Struct(v)


class Document(Struct):
    def __init__(self, data):
        super(Document, self).__init__(data)
        self.restriction = Restriction.NOT_RESTRICTED.value

    def restrict(self, title: str = ''):
        self.__dict__['title'] = title
        for key in self.__dict__.keys():
            if key in ['title', 'sourceId', 'documentId']:
                continue
            del self.__dict__[key]

    def __str__(self):
        return 'Document({sid}:{did})'.format(
            sid=self.__dict__['sourceId'],
            did=repr(self.__dict__['documentId'])
        )


class User:
    def __init__(self, entitlements):
        self.entitlements = entitlements

    def entitled(self, entitlement):
        return True if self.entitlements[entitlement] else False

    def not_entitled(self, entitlement):
        return not self.entitled(entitlement)
