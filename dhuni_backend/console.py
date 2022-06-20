import fire
from webapi.console import CliCommand as WebapiCommand


class Command:
    def __init__(self):
        self.webapi = WebapiCommand()


def main():
    fire.Fire(Command)
