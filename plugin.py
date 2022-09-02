import json
import sys

from galaxy.api.consts import Platform
from galaxy.api.plugin import Plugin, create_and_run_plugin
from galaxy.api.types import Authentication, Game, LicenseInfo, LicenseType
from pathlib import Path
from typing import Dict


def get_path(filename: str) -> str:
    return f"{Path(__file__).parent}/{filename}"


class CemuPlugin(Plugin):
    def __init__(self, reader, writer, token):
        self.manifest: Dict[str, str] = json.load(open(get_path("manifest.json"), "r"))

        super().__init__(
            Platform(self.manifest["platform"]), self.manifest["version"], reader, writer, token
        )

    async def authenticate(self, stored_credentials=None):
        return Authentication("12345", "debugger")

    async def get_owned_games(self):
        owned_games = []

        owned_games.append(
            Game("test_id", "Test", None, LicenseInfo(LicenseType.OtherUserLicense, None))
        )

        return owned_games


def main():
    create_and_run_plugin(CemuPlugin, sys.argv)


if __name__ == "__main__":
    main()
