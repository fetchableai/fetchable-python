from fetchable import FetchableClient
from fetchable import configuration


client = FetchableClient(api_version=configuration.api_version.latest)



"""
fetch an entity - attribute value
"""
entity_response = client.fetch("mount_everest", "elevation")

if(entity_response['status_code']==200):
    print("The height of mount_everest is {}.".format(entity_response['answer']))

elif(entity_response['status_code']==1000):
    print("I cant connect to the internet right now...")


"""
fetch a random joke
"""
joke_response = client.fetchRandomJoke()

if(joke_response['status_code']==200):
    print(joke_response['setup'])
    print(joke_response['punchline'])

elif(joke_response['status_code']==1000):
    print("I cant connect to the internet right now...")


"""
fetch a random quote
"""
quote_response = client.fetchRandomQuote()

if(quote_response['status_code']==200):
    print("{} by {}".format(quote_response['quote'], quote_response['author']))

elif(quote_response['status_code']==1000):
    print("I cant connect to the internet right now...")
