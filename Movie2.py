import requests

def get_movie_details(title):
    # replace "YOUR_API_KEY" with your actual OMDb API key
    url = f"http://www.omdbapi.com/?apikey=27e36d7d&t={title}&plot=full&r=json"

    # send a GET request to the API
    response = requests.get(url)

    # check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # check if the API returned a valid response
        if data["Response"] == "True":
            title = data["Title"]
            director = data["Director"]
            cast = data["Actors"]
            soundtrack = data.get("Soundtrack", "N/A")

            # return the details as a string
            return f"Title: {title}\nDirector: {director}\nCast: {cast}\nSoundtrack: {soundtrack}"
        else:
            return f"Sorry, could not find details for {title}"
    else:
        return "Sorry, could not connect to the API."

# test the function
title = input("Please enter the movie title: ")
details = get_movie_details(title)
print(details)
