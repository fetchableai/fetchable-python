from fetchable import FetchableClient
from fetchable import configuration

try:
    client = FetchableClient(api_version=configuration.api_version.latest)
except:
    print("problem initialising Fetchable client object")
    exit()

"""
get the status of Fetchable API
"""
status_response = client.status()

if(status_response['status_code']==200):
    print("The Fetchable API is up - all systems are go")
elif(status_response['status_code']==1001):
    print("Can't connect to the internet right now...")
else:
    print(status_response)



"""
fetch an entity - attribute value
"""
entity_response = client.fetch_entity_atrribute("mount_everest", "elevation")

if(entity_response['status_code']==200):
    print("The height of mount_everest is {} {}s.".format(entity_response['value'], entity_response['unit']))
elif(entity_response['status_code']==1001):
    print("Can't connect to the internet right now...")
else:
    print(entity_response)



"""
fetch a word definition
"""
definition_response = client.fetch_word_definition("ameliorate")

if(definition_response['status_code']==200):
    print("The definition of {}: is {}".format("ameliorate", definition_response['meanings'][0]))
elif(definition_response['status_code']==1001):
    print("Can't connect to the internet right now...")
else:
    print(definition_response)



"""
fetch a random joke
"""
joke_response = client.fetch_random_joke()

if(joke_response['status_code']==200):
    print("{} - {}".format(joke_response['setup'], joke_response['punchline']))
elif(joke_response['status_code']==1001):
    print("Can't connect to the internet right now...")
else:
    print(joke_response)


"""
fetch a random quote
"""
quote_response = client.fetch_random_quote()

if(quote_response['status_code']==200):
    print("{} by {}".format(quote_response['quote'], quote_response['author']))
elif(quote_response['status_code']==1001):
    print("Can't connect to the internet right now...")
else:
    print(quote_response)

"""
fetch a fun fact
"""
fun_fact_response = client.fetch_random_fun_fact()

if(fun_fact_response['status_code']==200):
    print(fun_fact_response['fun_fact'])
elif(fun_fact_response['status_code']==1001):
    print("Can't connect to the internet right now...")
else:
    print(fun_fact_response)

"""
make a request by defining the endpoint explicity
"""
endpoint_response = client.fetch_endpoint("/v0.1/mount_everest/height")

if(endpoint_response['status_code']==200):
    print("The height of mount_everest is {} {}s.".format(endpoint_response['value'], endpoint_response['unit']))
elif(endpoint_response['status_code']==1001):
    print("Can't connect to the internet right now...")
else:
    print(endpoint_response)
