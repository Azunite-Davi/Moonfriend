define t = Character("Toni", what_prefix="“", what_suffix="”")
define y = Character("Yu", what_prefix="“", what_suffix="”")
define m = Character("Mike", what_prefix="“", what_suffix="”")
define f = Character("Fino", what_prefix="“", what_suffix="”")

image f:
    "sprites/fino1_clothed.png"
    zoom 0.5
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show f

    # These display lines of dialogue.

    f "You've created a new Ren'Py game."

    f "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
