from .jokes import joke, dad_joke, get_joke, get_dad_joke
from .roasts import roast, get_roast
from .quotes import quote, quote_data
from .advices import advice, get_advice
from importlib.metadata import version

__version__ = version("FunKitPy")

__all__ = [
    "joke",
    "dad_joke",
    "roast",
    "quote",
    "advice",
    "quote_data",
    "get_joke",
    "get_dad_joke",
    "get_roast",
    "get_advice",
    "__version__",
]