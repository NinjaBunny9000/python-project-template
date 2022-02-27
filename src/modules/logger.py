# use Rich for our console output
from rich.console import Console
from rich import inspect

class Log:

    def __init__(self):

        # FORMAT = "%(message)s"
        # logging.basicConfig(
        #     level="DEBUG", format=FORMAT, datefmt="[%X]", handlers=[RichHandler(rich_tracebacks=True)]
        # )

        # self.log = logging.getLogger("rich")
        # self.log.info("Hello, World!")

        self.console = Console()

    def debug(self, message):
        self.console.log(message, style="dim yellow")
        # self.log.debug(message, extra={"markup": True})

    def info(self, message):
        self.console.log(message, style="dim cyan")

    def status(self, message):
        self.console.log(message, style="cyan")

    def success(self, message):
        self.console.log(message, style="bold green")

    def warn(self, message):
        self.console.log(message, style="italic  orange1")

    def danger(self, message):
        self.console.log(message, style="italic bold red")

    def hbar(self, message):
        self.console.rule(message)

    def inspect(self, obj):
        inspect(obj, methods=True, docs=False)