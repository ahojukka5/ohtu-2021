from matchers import And, Or, HasAtLeast, HasFewerThan, PlaysIn


class QueryBuilder:
    def __init__(self, matchers=None):
        self._matchers = matchers or []

    def _add(self, what):
        return QueryBuilder(self._matchers + [what])

    def playsIn(self, team):
        return self._add(PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return self._add(HasAtLeast(value, attr))

    def hasFewerThan(self, value, attr):
        return self._add(HasFewerThan(value, attr))

    @staticmethod
    def oneOf(*matchers):
        return QueryBuilder([Or(*matchers)])

    def build(self):
        return And(*self._matchers)
