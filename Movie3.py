import tkinter as tk
import imdb
# creating an instance of the IMDb class
ia = imdb.IMDb()

def get_movie_details(title):
    try:
        search_results = ia.search_movie(title)                  # search for the movie
        movie = search_results[0]
        ia.update(movie)                                         # get the movie details
        title = movie['title']                                   # extract relevant details from the movie object
        director = movie['director'][0]['name']
        cast = ", ".join([actor['name'] for actor in movie['cast'][:5]])
        soundtrack = ", ".join([soundtrack['title'] for soundtrack in movie.get('soundtrack', [])[:5]])
        return f"Title: {title}\nDirector: {director}\nCast: {cast}\nSoundtrack: {soundtrack}"         # return the details as a string
    except:
        return f"Sorry, could not find details for {title}"                              #movie can't be found

def on_button_click():
    title = entry.get()                                     # get the user input
    details = get_movie_details(title)                      # get the movie details
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, details)

root = tk.Tk()                                              # create the GUI
root.title("Movie Bot")

label = tk.Label(root, text="Enter movie title:")           # create the input label and entry widget
label.pack(side=tk.LEFT)
entry = tk.Entry(root, width=30)
entry.pack(side=tk.LEFT)

button = tk.Button(root, text="Search", command=on_button_click)     # create the button and text area
button.pack(side=tk.LEFT)
text_area = tk.Text(root, width=50, height=10)
text_area.pack(side=tk.TOP)

root.mainloop()

""" I have used Tkinter to create GUI and I converted this code into an application(executable file) with the help of the Pyinstaller
    Pyinstaller may not work for all the python programs.In that case we can use cx_Freeze which is also used to convert the python 
    codes into executable files/application.It will create some additional files required for the application.In those files go to 
    dist which will have the executable file of our program.We can open the application by clicking that .exe file. """
