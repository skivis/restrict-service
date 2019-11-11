class RulesEngine:
    def __init__(self, rules: list = []):
        self.rules = rules

    def apply_rules(self, docs: list, country: str) -> list:
        return [
            rule.apply(doc)
            if rule.validate(doc, country) else doc
            for doc in docs
            for rule in self.rules
        ]
