import tkinter as tk
import imdb

# create an instance of the IMDb class
ia = imdb.IMDb()

# function to get movie details
def get_movie_details(title):
    try:
        # search for the movie
        search_results = ia.search_movie(title)
        # get the first search result (assuming it's the correct movie)
        movie = search_results[0]
        # get the movie details
        ia.update(movie)
        # extract relevant details from the movie object
        title = movie['title']
        director = movie['director'][0]['name']
        cast = ", ".join([actor['name'] for actor in movie['cast'][:5]])
        soundtrack = ", ".join([soundtrack['title'] for soundtrack in movie.get('soundtrack', [])[:5]])
        # return the details as a string
        return f"Title: {title}\nDirector: {director}\nCast: {cast}\nSoundtrack: {soundtrack}"
    except:
        # return an error message if the movie details cannot be retrieved
        return f"Sorry, could not find details for {title}"

# function to handle button click event
def on_button_click():
    # get the user input
    title = entry.get()
    # get the movie details
    details = get_movie_details(title)
    # update the text area with the details
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, details)

# create the GUI
root = tk.Tk()
root.title("Movie Bot")

# create the input label and entry widget
label = tk.Label(root, text="Enter movie title:")
label.pack(side=tk.LEFT)
entry = tk.Entry(root, width=30)
entry.pack(side=tk.LEFT)

# create the button
button = tk.Button(root, text="Search", command=on_button_click)
button.pack(side=tk.LEFT)

# create the text area for displaying the movie details
text_area = tk.Text(root, width=50, height=10)
text_area.pack(side=tk.TOP)

# start the main event loop
root.mainloop()
