# [ZorKode](https://github.com/Yaykuby/ZorKode)
The adventure-based programming language, written in the style of Zork.

# About
ZorKode I: The Great Pythonic Dungeon is a Python-interpreted programming language meant to mimic the style of MS-DOS era text-based adventure games. The language tasks the programmer (Adventurer) to bravely make their way through a simple dungeon, collecting little bits and pieces of Python code along the way. Once you collect enough parts and make your way to the center of the dungeon, you can start piecing together your program one word (or line if you're clever enough) at a time. The fun of the program comes from runnning your code after every new piece of *.zrk* code written, seeing how the language reacts to your commands, and learning more about the world as you do.

# Quick Start
Download the [*ZorKode.py*](https://github.com/Yaykuby/ZorKode/blob/main/ZorKode.py) file and place it within a directory of your choosing. Create a file in that same directory called *ZorKode.zrk*. Open the same directory in your IDE of choice and start exploring the Great Pythonic Dungeon!

// Note: If you tend to need to use python instead of python3 whilst running python code, change line 393 of *ZorKode.py* from:

*craftedResult = subprocess.run(["python3", "CraftedCode.py"], capture_output=True, text=True)*

to

*craftedResult = subprocess.run(["python", "CraftedCode.py"], capture_output=True, text=True)*

Not doing so could have unforseen consequences, most likely just causing the program to fail.

# Keywords
Just like Zork, ZorKode has plenty of keywords that the programmer can use to take various actions inside the Great Pythonic Dungeon, such keywords are:

*examine* - When used by itself, examine has you take a look around and describe what is seen in your environment. When examining a specific item to learn more about it, use *examine <item>*.

*north* - Moves your adventurer in the northern direction

*south* - Moves your adventurer in the southern direction

*east* - Moves your adventurer in the eastern direction

*west* - Moves your adventurer in the western direction

*take /item/* - Allows you to take an item present within the room your adventurer currently resides and adds it to their inventory. Only one item can be taken at a time.

*make variable /variable_name/* - Allows the adventurer to create a variable and place it within their inventory for later use. Can only be used inside the Assembly Room.

*craft /code/* - Allows the user to craft a word or specific line of code to then be added to your adventurer's inventory.

*write /inventory_item/* - Allows the adventurer to take an item found within their inventory and write it inside of CraftedCode.py, the place where your written code presides.

*place /inventory_item/* - Allows the adventurer to place items from their inventory onto the assembly table to then be shaped into a line of code. Note: items will be placed in the order you place them in.

*pickup /code/* - Allows the adventurer to pickup a satisfactory line of code from the assembly table and add it to their inventory.

*inventory* - Allows the adventurer to view their inventory

# Example Programs
***vv Hello World! vv***

<img width="180" alt="Screenshot 2024-12-10 at 10 21 59 PM" src="https://github.com/user-attachments/assets/dd371623-20fd-4fd5-96fc-7cc7d8d0d7eb">

***vv FizzBuzz vv***

<img width="307" alt="Screenshot 2024-12-10 at 8 14 48 PM" src="https://github.com/user-attachments/assets/74877bae-9583-4e51-ae7b-d8e5560304fe">
