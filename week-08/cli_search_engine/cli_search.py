from search_factory import SearchFactory
from search import GoogleSearch
from search import DuckDuckGoSearch
from search import RedditSearch
import sys


# Create the Search Factory and Register Search Engines
search_factory = SearchFactory()
search_factory.register("google", GoogleSearch)
search_factory.register("duck", DuckDuckGoSearch)
search_factory.register("reddit", RedditSearch)


args = sys.argv
search_engine = args[1]
q = args[2]
print(args)


