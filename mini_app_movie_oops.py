#arguments variables are just dummy variable
#we also change as
#In class
# def __init__(self, a, b, c):
#     self.title = a
#     self.hero = b
#     self.heroine = c


class Movie:
    '''This application was creted by Rushi'''
    def __init__(self,title,hero,heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine

    def info(self):
        print("The movie title is",self.title)
        print("The movie hero is",self.hero)
        print("The movie heroine is",self.heroine)

list_of_movies=[]

while True:
    title=input("Enter the movie title:-")
    hero=input("Enter the  movie hero:-")
    heroine=input("Ente the movie heroine:-")
    m=Movie(title,hero,heroine)
    list_of_movies.append(m)
    print("Movie added in list successfully")
    print("Do you want to enter the movie again(Yes/No)?")
    option=input()
    if option.lower()=="no":
        break
print("All movies added successfully")

for movie in list_of_movies:
    movie.info()
    print(" ")


# output:-
# Enter the movie title: -Bahubali
# Enter the movie hero: -Prabhas
# Ente the movie heroine: -Anushka
# Movie
# added in list
# successfully
# Do
# you
# want
# to
# enter
# the
# movie
# again(Yes / No)?
# y
# Enter
# the
# movie
# title: -Raees
# Enter
# the
# movie
# hero: -Shahrukh
# Ente
# the
# movie
# heroine: -Sunny
# leane
# Movie
# added in list
# successfully
# Do
# you
# want
# to
# enter
# the
# movie
# again(Yes / No)?
# Yes
# Enter
# the
# movie
# title: -Sultan
# Enter
# the
# movie
# hero: -Salman
# Ente
# the
# movie
# heroine: -Anushka
# Movie
# added in list
# successfully
# Do
# you
# want
# to
# enter
# the
# movie
# again(Yes / No)?
# No
# All
# movies
# added
# successfully
# The
# movie
# title is Bahubali
# The
# movie
# hero is Prabhas
# The
# movie
# heroine is Anushka
#
# The
# movie
# title is Raees
# The
# movie
# hero is Shahrukh
# The
# movie
# heroine is Sunny
# leane
#
# The
# movie
# title is Sultan
# The
# movie
# hero is Salman
# The
# movie
# heroine is Anushka
