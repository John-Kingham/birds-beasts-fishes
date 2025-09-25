# Birds, Beasts and Fishes - Manual Testing

## Functionality

### Game Launch Functionality

|Feature|Expect|Action|Result|Image
|---|---|---|---|---|
|Game Title|When the game is first launched, the Game Title is shown|Launched game|As expected|![Game title](images/game-title.png)|
|Main Menu|When the game is first launched, the Main Menu is shown after the Game Title|Launched game|As expected|![Main menu](images/main-menu.png)|

### Main Menu Functionality

|Feature|Expect|Action|Result|Image
|---|---|---|---|---|
|Menu option 1 ("Play game")|When chosen, the Game Loop section is shown|Selected option 1|As expected|![Instructions](images/instructions.png)|
|Menu option 2 ("Read instructions")|When chosen, the Instructions section is shown|Selected option 2|As expected|![Game loop](images/game-loop.png)|
|Menu option 3 ("Exit")|When chosen, the Exit Message was shown and the program exits|Selected option 3|As expected|![exit message](images/exit-message.png)|
|Validation|When an invalid option is entered, an error message is shown and the Main Menu is redisplayed|Entered an invalid option|As expected|![exit message](images/main-menu-error-message.png)|

### Instructions Functionality

|Feature|Expect|Action|Result|Image
|---|---|---|---|---|
|Return to Main Menu|When enter is pressed, the Main Menu is shown|Pressed enter|As expected|![Instructions](images/main-menu-after-instructions.png)|

### Game Loop Functionality

|Feature|Expect|Action|Result|Image
|---|---|---|---|---|
|Incorrect guess message|When an incorrect guess is entered, a relevant message is shown and the Game Loop text is redisplayed; the word to guess is unchanged and the list of previous guesses includes the incorrect guess|Entered an incorrect guess|As expected|![Instructions](images/game-loop-incorrect-guess.png)|
|Invalid guess message|When an invalid (non-alphabetical) guess is entered, a relevant message is shown and the Game Loop text is redisplayed; the word to guess and list of previous guesses are unchanged|Entered an invalid guess|As expected|![Instructions](images/game-loop-invalid-guess.png)|
|Correct animal name guess|When a correct animal name guess is entered, the Win Message section is shown|Entered a correct animal name guess|As expected|![Instructions](images/game-loop-correct-word-guess.png)|
