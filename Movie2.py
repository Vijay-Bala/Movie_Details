import requests

def get_movie_details(title):
    #I have used OMDb API for my project.You can use other APIs also which has the data about the movies
    url = f"http://www.omdbapi.com/?apikey=27e36d7d&t={title}&plot=full&r=json"          # replace this apikey with your actual OMDb API key
    response = requests.get(url)                                                         # sending a GET request to the API
    if response.status_code == 200:                                                      # checking whether the request was successful or not
        data = response.json()
        if data["Response"] == "True":                                                   # checking whether the API returned is a valid response or not
            title = data["Title"]
            director = data["Director"]
            cast = data["Actors"]
            soundtrack = data.get("Soundtrack", "N/A")
            return f"Title: {title}\nDirector: {director}\nCast: {cast}\nSoundtrack: {soundtrack}"             # returns the details as string
        else:
            return f"Sorry, could not find details for {title}"
    else:
        return "Sorry, could not connect to the API."

title = input("Please enter the movie title: ")
details = get_movie_details(title)
print(details)
