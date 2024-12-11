import subprocess

################ INTERPRETER CLASS #########################################################################
class ZorKode:
    def interpret(filename, state):
        file = open(filename)
        craftedCode = open("CraftedCode.py", "w")
        d = dict()
        inv = []
        adventurer_x = 0
        adventurer_y = 0
        lineToPrint = ""
        placedLine = ""
        previousLine = False

############### ZORKODE KEYWORD CHECKS ###########################################################################
        for line in file.readlines():
            try:
                ## COMMENT IMPLEMENTATION ###############################################################
                # Lines that start with # will be commented out
                if line.startswith("#"):
                    continue
                # Lines that start with < and end with > will be commented out
                elif ("<" in line) and (line.strip().endswith(">")):
                    continue
                ## ZORKODE INTRO STATEMENT IMPLEMENTATION##############################################################
                if ((len(line.strip()) == 0) and (previousLine == False)):
                    lineToPrint = "ZorKode I: The Great Pythonic Dungeon " + "\n" + "Not Copyright (nc) 2024, SDSU Edu. No Rights Reserved" "\n" + "ZorKode is a registered trademark of absolutely nothing" + "\n" + "Revision 1 / Serial Number idk" + "\n" + "\n" "> Assembly Room" + "\n" + "You are standing in a dim room with four passageways on all sides of you" + "\n" + "To the north lies a hallway with a sign labeled \"Operation Room\"" + "\n" + "To the east sits a hallway labeled \"Value Room\"" + "\n" + "To the south waits a room simply named \"Refreshment Room\"" + "\n" + "To the west is a room labeled \"I/O Room\"" + "\n" + "Directly in front of you lies a table with strange holes carved into it," + "\n" + "almost seeming like there are pieces meant to be seated within it."
                if ((len(line.strip()) == 0) and (previousLine == True)):
                    lineToPrint = "I beg your pardon?"

                ## ADVENTURER MOVEMENT IMPLEMENTATION #################################################################
                elif line.startswith("north") or line.startswith("south") or line.startswith("west") or line.startswith("east"):
                    previousLine = True
                    if "north" in line:
                        if adventurer_y + 1 < 2 and adventurer_x == 0:
                            adventurer_y += 1
                            lineToPrint = "Went: North"
                        else:
                            lineToPrint = "You can't go north any more!"
                    elif "south" in line:
                        if adventurer_y - 1 > -2 and adventurer_x == 0:
                            adventurer_y -= 1
                            lineToPrint = "Went: South"
                        else:
                            lineToPrint = "You can't go south any more!"
                    elif "west" in line:
                        if adventurer_x - 1 > -2 and adventurer_y == 0:
                            adventurer_x -= 1
                            lineToPrint = "Went: West"
                        else:
                            lineToPrint = "You can't go west any more!"
                    elif "east" in line:
                        if adventurer_x + 1 < 2 and adventurer_y == 0:
                            adventurer_x += 1
                            lineToPrint = "Went: East"
                        else:
                            lineToPrint = "You can't go east any more!"
                    else:
                        adventurer_x == 0
                        adventurer_y == 0

                ## ADVENTURER TAKE IMPLEMENTATION #####################################################################
                elif line.startswith("take"):
                    previousLine = True
                    noun = line.split("take")[1].strip()
                    if noun == "equals":
                        if adventurer_y == 1:
                            inv.append("equals")
                            lineToPrint = "You took: equals"
                        else:
                            lineToPrint = "You sure you're in the right room for an equal sign?"
                    elif noun == "plus":
                        if adventurer_y == 1:
                            inv.append("plus")
                            lineToPrint = "You took: plus"
                        else:
                            lineToPrint = "You want to grab a plus sign... From where!?"
                    elif noun == "minus":
                        if adventurer_y == 1:
                            inv.append("minus")
                            lineToPrint = "You took: minus"
                        else:
                            lineToPrint = "There's no sign of a minus anywhere!"
                    elif noun == "divide":
                        if adventurer_y == 1:
                            inv.append("divide")
                            lineToPrint = "You took: divide"
                        else:
                            lineToPrint = "ERROR: Division by Zero. Just kidding, there's no divides here."
                    elif noun == "multiply":
                        if adventurer_y == 1:
                            inv.append("multiply")
                            lineToPrint = "You took: multiply"
                        else:
                            lineToPrint = "No multiply in this room, it must be somewhere north!"
                    elif noun == "chalkboard":
                        if adventurer_x == 1:
                            inv.append("chalkboard")
                            lineToPrint = "You took: chalkboard"
                        else:
                            lineToPrint = "Sorry but the chalkboard ain't here. You should try checking eastbound"
                    elif noun == "chalk":
                        if adventurer_x == 1:
                            inv.append("chalk")
                            lineToPrint = "You took: chalk"
                        else:
                            lineToPrint = "Chalk not here. Walk east."
                    elif noun == "print":
                        if adventurer_x == -1:
                            inv.append("print")
                            lineToPrint = "You took: print"
                        else:
                            lineToPrint = "You tried to take print! And print isn't in this room! Ha! Ha!"
                    elif noun == "pencil":
                        if adventurer_x == -1:
                            inv.append("pencil")
                            lineToPrint = "You took: pencil"
                        else:
                            lineToPrint = "No pencils to be taken here."
                    elif noun == "paper":
                        if adventurer_x == -1:
                            inv.append("paper")
                            lineToPrint = "You took: paper"
                        else:
                            lineToPrint = "There is no paper stack seen here, let alone a single page"
                    elif noun == "water":
                        if adventurer_y == -1:
                            inv.append("water")
                            lineToPrint = "You took: water"
                        else:
                            lineToPrint = "No refreshments for you... sorry! Have you tried checking the refreshment room?"
                    elif noun == "bread":
                        if adventurer_y == -1:
                            inv.append("bread")
                            lineToPrint = "You took: bread"
                        else:
                            lineToPrint = "There's not a single freshly baked loaf to be seen anywhere in here!"
                    elif noun == "":
                        lineToPrint = "You took: \" \"" + "\n" + "Just kidding, you didn't take anything."
                    else:
                        lineToPrint = f"There's no {noun} to be seen anywhere!"
                    
                ## ADVENTURER INVENTORY IMPLEMENTATION ################################################################
                elif line.startswith("inventory"):
                    previousLine = True
                    if len(inv) == 0:
                        lineToPrint = "You are empty-handed."
                    else:
                        lineToPrint = inv
                
                ## ADVENTURER EXAMINE IMPLEMENTATION ##################################################################
                elif line.startswith("examine"):
                    previousLine = True
                    noun = line.split("examine")[1].strip()
                    if noun == "":
                        if adventurer_x == 0 and adventurer_y == 0:
                            lineToPrint = "> Assembly Room" + "\n" + "\n" + "You are standing in a dim room with four passageways on all sides of you" + "\n" + "To the north lies a hallway with a sign labeled \"Operation Room\"" + "\n" + "To the east sits a hallway labeled \"Value Room\"" + "\n" + "To the south waits a room simply named \"Refreshment Room\"" + "\n" + "To the west is a room labeled \"I/O Room\"" + "\n" + "Directly in front of you lies a table with strange holes carved into it," + "\n" + "almost seeming like there are pieces meant to be seated within it."
                        elif adventurer_x == 0 and adventurer_y == 1:
                            lineToPrint = "> Operation Room" + "\n" + "\n" + "You are standing in a bright room lit by five neon lights, all with dispensers each" + "\n" +  "containing infinite words below them, seemingly beckoning you to take at least one." + "\n" + "The first neon sign reads \"equals\" in bright yellow lettering" + "\n" + "Another sign shines a green hue across the room and is labeled \"plus\"" + "\n" + "A third sign adds a bright red light to the room and is labeled \"minus\"" + "\n" + "A blue light illuminates across the room and reads \"multiply\"" + "\n" + "A fifth and final sign, purple this time, ominously states \"divide\""
                        elif adventurer_x == 0 and adventurer_y == -1:
                            lineToPrint = "> Refreshment Room" + "\n" + "\n" + "You are standing in a room illuminated by a single spotlight pointed directly at the center of the room." + "\n" + "There's no windows, and no doors (you don't even remember how you got here). The only" + "\n" + "thing you know for certain is there lies a foldable party table directly under the spotlight" + "\n" + "with a few cups and a bowl. The cups seem to be holding water, and the bowl is filled with loaves of bread."
                        elif adventurer_x == 1 and adventurer_y == 0:
                            lineToPrint = "> Value Room" + "\n" + "\n" + "You are standing in a room that looks as cheap as it sounds. A couple small chalkboards sit leaning" + "\n" + "against the wall to your right. To the left sits a hefty and overflowing bag of chalk sticks." + "\n" + "The room feels thick and smells like the inside of a dilapidated classroom."
                        elif adventurer_x == -1 and adventurer_y == 0:
                            lineToPrint = "> I/O Room" + "\n" + "\n" + "You are standing in a room that looks eerily similar to SSW 1500, Professor Dabish's classroom. All the" + "\n" + "chairs are empty. The seats, folded. On the table at the front of the classroom, sits a wooden block carved into" + "\n" + "the shape of a word. The word... print. To its right lies a single No. 2 wooden pencil." + "\n" + "And to its left sits a pile of blank printer paper."
                        else:
                            lineToPrint = "> ???" + "\n" + "\n" + "You remember the white room from The Matrix? Yeah, well somehow you ended up there." + "\n" + "Sorry, but there's no Architect to talk to here either." + "\n" + "All that's here is you, your thoughts, and the entirety of time to think about what you've done." + "\n" + "Shame."
                    elif noun == "equals":
                        if adventurer_y == 1 or noun in inv:
                            lineToPrint = "A wooden block carved into the shape of an equals sign. With this, you could probably equate two things."
                        else:
                            lineToPrint = f"You can't see any {noun} here!"
                    elif noun == "chalkboard":
                        if adventurer_x == 1 or noun in inv:
                            lineToPrint = "A void blackboard of porcelain-enameled steel. Yup, this is prime real estate to write some words (or numbers)."
                        else:
                            lineToPrint = f"You can't see any {noun}s here!"
                    elif noun == "chalk":
                        if adventurer_x == 1 or noun in inv:
                            lineToPrint = "A leather bag filled with premium sticks of calcium carbonate. You can't quite tell if the black at the bottom" + "\n" + "of the bag is unilluminated sticks, or just an unending void staring back at you."
                        else:
                            lineToPrint = f"You can't see any {noun} here!"
                    elif noun == "print":
                        if adventurer_x == -1 or noun in inv:
                            lineToPrint = "A crude wooden block carved to resemble the word \"print\""
                        else:
                            lineToPrint = f"You can't see any {noun} here!"
                    elif noun == "pencil":
                        if adventurer_x == -1 or noun in inv:
                            lineToPrint = "An unusually sharpened yellow pencil, clearly capable of spreading graphite onto paper surfaces."
                        else:
                            lineToPrint = f"You can't see any {noun}s here!"
                    elif noun == "paper":
                        if adventurer_x == -1 or noun in inv:
                            lineToPrint = "Blank. White. Printer. Paper. I bet you could write something on this."
                        else:
                            lineToPrint = f"You can't see any {noun} here!"
                    elif noun == "plus":
                        if adventurer_y == 1 or noun in inv:
                            lineToPrint = "A crude wooden block carved to resemble a plus symbol (the one used in math)"
                        else:
                            lineToPrint = f"You can't see any {noun} here!"
                    elif noun == "minus":
                        if adventurer_y == 1 or noun in inv:
                            lineToPrint = "A crude wooden block carved to resemble a minus symbol (better be careful with this)"
                        else:
                            lineToPrint = f"You can't see any {noun} here!"   
                    elif noun == "multiply":
                        if adventurer_y == 1 or noun in inv:
                            lineToPrint = "A crude wooden block carved to resemble a multiplication symbol (maybe this is the key to getting out!)"
                        else:
                            lineToPrint = f"You can't see any {noun} here!"
                    elif noun == "divide":
                        if adventurer_y == 1 or noun in inv:
                            lineToPrint = "A crude wooden block carved to resemble a division symbol (where's the modulus block :( )"
                        else:
                            lineToPrint = f"You can't see any {noun} here!"
                    elif noun == "water":
                        if adventurer_y == -1 or noun in inv:
                            lineToPrint = "A plastic cup filled with water, cold to the touch. One swig of this and you'd be refreshed for minutes!"
                        else:
                            lineToPrint = f"You can't see any {noun} here!"
                    elif noun == "bread":
                        if adventurer_y == -1 or noun in inv:
                            lineToPrint = "A soft loaf of bread, about yay big and yay wide. Now with over 30g of carbohydrates!"
                    else:
                        lineToPrint = f"You can't even begin to comprehend {noun}, let alone examine it."
                
                ## ADVENTURER MAKE IMPLEMENTATION #####################################################################
                elif line.startswith("make"):
                    previousLine = True
                    if adventurer_x == 0 and adventurer_y == 0:
                        line.strip()
                        make, noun1, noun2 = line.split()
                        if noun1 == "variable" and "chalkboard" in inv and "chalk" in inv:
                            if noun2 in d:
                                lineToPrint = f"You've already made a variable called {noun2}"
                                break
                            else:
                                d[noun2] = None
                                inv.append(noun2)
                                lineToPrint = f"You have made the variable: {noun2}!"
                        elif noun1 == "variable" and "chalkboard" in inv and "chalk" not in inv:
                            lineToPrint = "You've got the chalkboard, but aren't you missing the... Chalk?"
                        elif noun1 == "variable" and "chalk" in inv and "chalkboard" not in inv:
                            lineToPrint = "You've got the chalk, but Josh... Where's the board?"
                    else:
                        lineToPrint = "You've gotta be in the Assembly Room to make that."

                ## ADVENTURER CRAFT IMPLEMENTATION ####################################################################
                elif line.startswith("craft"):
                    previousLine = True
                    if adventurer_x == 0 and adventurer_y == 0 and "chalkboard" in inv and "chalk" in inv:
                        statement = line.split("craft ")[1]
                        if statement != "":
                            inv.append(statement.strip())
                            lineToPrint = f"You have crafted: {statement}"
                        else:
                            lineToPrint = "Sorry Adventurer, you can't craft \"\""
                    elif adventurer_x == 0 and adventurer_y == 0 and "chalkboard" in inv and "chalk" not in inv:
                        lineToPrint = "You can't craft a line without any chalk!"
                    elif adventurer_x == 0 and adventurer_y == 0 and "chalkboard" not in inv and "chalk" in inv:
                        lineToPrint = "You can't craft a line without a chalkboard!"
                    elif adventurer_x == 0 and adventurer_y == 0 and "chalkboard" not in inv and "chalk" not in inv:
                        lineToPrint = "You have neither chalk nor a chalkboard, how do you expect to craft!?"
                    elif adventurer_x != 0 or adventurer_y != 0:
                        lineToPrint = "Due to magical properties of the Pythonic Dungeon," + "\n" + "you can only craft inside the Assembly Room."
                    else:
                        lineToPrint = "Something went wrong in the crafting process. Try something different."

                ## ADVENTURER WRITE IMPLEMENTATION ####################################################################
                elif line.startswith("write"):
                    previousLine = True
                    if adventurer_x == 0 and adventurer_y == 0 and "paper" in inv and "pencil" in inv:
                        lineToWrite = line.split("write ")[1].strip()
                        if lineToWrite in inv:
                            inv.remove(lineToWrite)
                            if lineToWrite.__contains__("/tab/"):
                                newLineToWrite = lineToWrite.replace("/tab/", "    ")
                                craftedCode.write(newLineToWrite + "\n")
                            else:
                                craftedCode.write(lineToWrite + "\n")
                                lineToPrint = f"You have written: {lineToWrite}"
                        else:
                            lineToPrint = f"{lineToWrite} isn't in your inventory, you can't write it down if you don't have it!"
                    elif adventurer_x == 0 and adventurer_y == 0 and "paper" in inv and "pencil" not in inv:
                        lineToPrint = "Correct Room: Check... Paper: Check... Writing Utensil..?"
                    elif adventurer_x == 0 and adventurer_x == 0 and "pencil" in inv and "paper" not in inv:
                        lineToPrint = "Correct Room: Check... Pencil: Check... Paper... Not Quite."
                    elif adventurer_x == 0 and adventurer_x == 0 and "pencil" not in inv and "paper" not in inv:
                        lineToPrint = "You have neither the paper nor the pencil to write anything down here."
                    elif adventurer_x != 0 or adventurer_y != 0:
                        lineToPrint = "Due to magical properties of the Pythonic Dungeon," + "\n" + "you can only write inside the Assembly Room."
                    else:
                        lineToPrint = "Something went wrong in the writing process. Try something different."

                ## ADVENTURER PLACE IMPLEMENTATION ####################################################################
                elif line.startswith("place"):
                    previousLine = True
                    if adventurer_x == 0 and adventurer_y == 0:
                        noun = line.split("place")[1].strip()
                        if noun in inv and noun not in d:
                            if noun == "print":
                                placedLine = placedLine + "print("
                                lineToPrint = f"Placed: {noun}"
                            elif noun == "plus":
                                placedLine = placedLine + " + "
                                lineToPrint = f"Placed: {noun}"
                            elif noun == "minus":
                                placedLine = placedLine + " - "
                                lineToPrint = f"Placed: {noun}"
                            elif noun == "multiply":
                                placedLine = placedLine + " * "
                                lineToPrint = f"Placed: {noun}"
                            elif noun == "divide":
                                placedLine = placedLine + " / "
                                lineToPrint = f"Placed: {noun}"
                            elif noun == "equals":
                                placedLine = placedLine + " = "
                                lineToPrint = f"Placed: {noun}"
                            elif noun == "chalk":
                                lineToPrint = "Chalk doesn't fit here, but maybe you can craft something with it instead."
                            elif noun == "chalkboard":
                                lineToPrint = "A chalkboard can't fit in the table, but you might be able to craft something with it."
                            elif noun == "paper":
                                lineToPrint = "The paper doesn't fit into the table, but it might still function as a writing surface."
                            elif noun == "pencil":
                                lineToPrint = "The pencil can't seem to fit right in the table, but it might be able to write on something."
                            elif noun == "bread":
                                lineToPrint = "Unfortunately the bread can't quite fit into the table, but maybe it can fit into your mouth."
                            elif noun == "water":
                                lineToPrint = "The table isn't thirsty, but it appreciates your thoughtfulness."
                            elif noun in d:
                                placedLine = placedLine + noun
                                lineToPrint = f"Placed: {noun}"
                            elif noun.isdigit():
                                placedLine = placedLine + noun
                                lineToPrint = f"Placed: {noun}"
                            elif noun.startswith('"') and noun.endswith('"'):
                                placedLine = placedLine + noun
                                lineToPrint = f"Placed: {noun}"
                            else:
                                lineToPrint = f"{noun} doesn't belong in the table, unfortunately."
                            inv.remove(noun)
                        elif noun in inv and noun in d:
                            placedLine = placedLine + noun
                            lineToPrint = f"Placed: {noun}"
                        else:
                            lineToPrint = f"You can't place {noun} here. You can't place {noun} anywhere. You don't have {noun}!"
                    else:
                        lineToPrint = f"You're not in the right room to be placing {noun}."        

                ## ADVENTURER PICKUP IMPLEMENTATION ###################################################################
                elif line.startswith("pickup"):
                    previousLine = True
                    if adventurer_x == 0 and adventurer_y == 0:
                        if placedLine == "":
                            lineToPrint = "You can't pick up nothing."
                        elif len(placedLine) > 0:
                            if placedLine.__contains__("print("):
                                inv.append(placedLine + ")")
                                lineToPrint = f"You picked up: {placedLine}. Now is time to write it!" + "\n" + "Don't forget that extra ) when writing!"
                            else: 
                                inv.append(placedLine)
                                lineToPrint = f"You picked up: {placedLine}. Now is time to write it!"
                                placedLine = ""
                        else:
                            pass
                    else:
                        lineToPrint = "Sorry but unless you're picking up some wooden blocks off" + "\n" + "of a table, you aren't collecting anything."       

                ## UNRECOGNIZED STATEMENT HANDLER #####################################################################
                # Handles statements that aren't recognized or properly formatted
                elif line.startswith("\n"):
                    continue
                else:
                    invalidExpr = line.replace("\n", "")
                    if not invalidExpr:
                        invalidExpr = ""
                    print(f"'{invalidExpr}' is not a valid statement. Learn to program in ZorKode, kid!")
                    print("")
            except Exception:
                print(f"'{line.replace("\n", "")}' is not an accepted statement at the moment. Please wait for ZorKode 2.0")
                print("")

                #########################################################################################
        print(lineToPrint)
        craftedCode.close()
        craftedResult = subprocess.run(["python3", "CraftedCode.py"], capture_output=True, text=True)
        if len(craftedResult.stdout) > 0:
            print("\n" + "Crafted Code Output:")
            print(craftedResult.stdout)
        if len(craftedResult.stderr) > 0:
            print("Crafted Code Errors:")
            print(craftedResult.stderr)
            print("Crafted Code Return Code:")
            print(craftedResult.returncode)

ZorKode.interpret("ZorKode.zrk", {})  