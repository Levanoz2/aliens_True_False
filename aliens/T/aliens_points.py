alien_colour = {"colour":"red","points": 10}
type(alien_colour)
Colour = alien_colour.get("colour")
print(Colour)
Points = alien_colour.get("points")
print(Points)

alien_colour = {"colour":"red","points": 10}
print(alien_colour)
alien_colour["X"] = 5
alien_colour["Y"] = 10
print(alien_colour)

alien_colour = {}
alien_colour["colour"] = "blue".title()
alien_colour["points"] = 10
print(alien_colour)

alien_colour = {"colour":"red","points": 10}
print(alien_colour)
alien_colour["colour"] = "blue"
alien_colour["points"] = 20
print(alien_colour)