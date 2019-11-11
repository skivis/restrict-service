from app.dto import Document
from app.dto import Restriction


class SmartEngine:
    def __init__(self, rules, user, auth):
        self.rules = rules
        self.auth = auth
        self.user = user
        self._documents = None

    @property
    def documents(self) -> list:
        return [vars(doc) for doc in self._documents]

    @documents.setter
    def documents(self, documents: list) -> None:
        self._documents = [Document(d) for d in documents]

    def apply_restrictions(self, documents: list, jwt_token: str) -> list:
        country = self.auth.details(jwt_token).pop('country').lower()
        return self.rules.apply(documents, country)

    def restrict(self):
        for doc in self._documents:
            if int(doc.sourceId) in [] and self.user.not_entitled('premium-print-australia-all'):
                self.applyApacPremiumRestriction(doc)

            if int(doc.sourceId) in [1, 2] and (
                self.user.not_entitled('premium-print-australia-nationals') and
                self.user.not_entitled('premium-print-australia-all')
                ):
                self.applyApacPremiumRestriction(doc)

            if int(doc.sourceId) in [3, 4] and (
                self.user.not_entitled('premium-print-australia-regional') and
                self.user.not_entitled('premium-print-australia-all')
                ):
                self.applyApacPremiumRestriction(doc)

            if int(doc.sourceId) in [5, 6] and (
                self.user.not_entitled('premium-print-australia-magazines') and
                self.user.not_entitled('premium-print-australia-all')
                ):
                self.applyApacPremiumRestriction(doc)

            if int(doc.sourceId) in [7, 8] and (
                self.user.not_entitled('premium-print-australia-all-metros') and
                self.user.not_entitled('premium-print-australia-all')
                ):
                self.applyApacPremiumRestriction(doc)

            if int(doc.sourceId) in [9] and (
                self.user.not_entitled('premium-print-australia-major-metros') and
                self.user.not_entitled('premium-print-australia-all-metros') and
                self.user.not_entitled('premium-print-australia-all')
                ):
                self.applyApacPremiumRestriction(doc)

            if int(doc.sourceId) in [10] and self.user.not_entitled('premium-print-singapore-sph'):
                self.applyApacPremiumRestriction(doc)

    def applyApacPremiumRestriction(self, doc):
        doc.restrict('Content from this publisher is not available in your country')
        doc.restriction = Restriction.APAC_RESTRICTED.value
