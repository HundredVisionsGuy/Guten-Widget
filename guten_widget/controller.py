"""controller.py will manage making API calls to the Gutendex and
format the results for display."""

# import statements
import requests

# set some variables to help our API call
domain = "https://gutendex.com/"
endpoint = "books/?search="

# Define variables to make API call and process the data
def make_call(query: str) -> str:
    """take the terms (of the search) and use it to make an API call
    then return raw results or error if does not return a 200 code"""
    
    # create our URL
    url = domain + endpoint + query
    
    response = requests.get(url)
    if response.ok:
        results = get_top_results(response)
        results = format_results(results)
        return results
    else:
        return "There was an error"

def get_top_results(response, max=5) -> dict:
    """takes an API response and returns a dict of the first max # of results"""
    results = response.json()["results"]
    return results[:max]

def format_results(results: dict)->str:
    """Takes results in a dictionary form and returns a rich text
    formatted string"""
    formatted_results = ""
    for item in results:
        title = item.get("title")
        title = "<h2>" + title + "</h2>"
        credits = "<p>By <i>"
        for author in item.get("authors"):
            credits += author.get("name") + " "
        credits = credits + "</i></p>"
        formatted_results += title
        formatted_results += credits
        
    return formatted_results

if __name__ == "__main__":
    print("Here is where we can test our code.")
    results = make_call("wells")
    print(results)
    results_dict = get_top_results(results)
    results_str = format_results(results_dict)
    print(results_str)