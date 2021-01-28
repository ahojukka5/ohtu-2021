from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta
        # Project-olio sen tietojen perusteella
        data = toml.loads(content)
        data = data["tool"]["poetry"]
        name = data["name"]
        description = data["description"]
        deps = list(data["dependencies"].keys())
        devdeps = list(data["dev-dependencies"].keys())
        return Project(name, description, deps, devdeps)
