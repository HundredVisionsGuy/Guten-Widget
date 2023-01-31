"""controller.py will manage making API calls to the Gutendex and
format the results for display."""

# import statements
import requests

# set some variables to help our API call
domain = "https://gutendex.com/"
endpoint = "books/"
query = "?search="

# Define variables to make API call and process the data
def make_call(terms: str) -> str:
    """take the terms (of the search) and use it to make an API call
    then return raw results or error if does not return a 200 code"""
    
    # create our URL
    url = domain + endpoint + query + terms
    
    response = requests.get(url)
    if response.ok:
        return response.text
    else:
        return "There was an error"
    

if __name__ == "__main__":
    print("Here is where we can test our code.")
    results = make_call("wells")
    print(results)