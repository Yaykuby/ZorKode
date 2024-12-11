# ZorKode
An adventure-based programming language, written in the style of Zork.

# About
ZorKode I: The Great Pythonic Dungeon is a Python-interpreted programming language meant to mimic the style of MS-DOS era text-based adventure games. The language tasks the programmer (Adventurer) to bravely make their way through a simple dungeon, collecting little bits and pieces of Python code along the way. Once you collect enough parts and make your way to the center of the dungeon, you can start piecing together your program one word (or line if you're clever enough) at a time. The fun of the program comes from runnning your code after every new piece of .zrk code written, seeing how the language reacts to your commands, and learning more about the world as you do.

# Quick Start
Download the ZorKode.py file, along with the ZorKode.zrk file and place them within the same directory. Open the directory in your IDE of choice and start exploring!

// Note: If you tend to need to use python instead of python3 whilst running python code, change line 390 of ZorKode.py from:
<craftedResult = subprocess.run(["python3", "CraftedCode.py"], capture_output=True, text=True)>
to
<craftedResult = subprocess.run(["python", "CraftedCode.py"], capture_output=True, text=True)>
Not doing so could have unforseen consequences and cause the program to fail.

# Keywords
Just like Zork, ZorKode has plenty of keywords that the programmer can use to take various actions inside the Great Pythonic Dungeon, such keywords are:

<examine> - 
