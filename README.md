# NoGit
A simple python script to prevent the unnecessary repetition of the "git" keyword.


### Documentation:

  * the `%undo` command removes the last command from the stack
  * the `%run` command runs the commands in the stack and clears the stack
  * the `%exit` command closes the CLI without doing anything
  * pressing `ctr+c` is the same as running `%run; %exit`
  * the script saves commands that have been run to a file called `git.history` in the same folder as the script
  * you can add multiple commands in one line using a semi-colon
  * you can use the keyword `git` in the beginning of the command and the script won't duplicate it (**E.G:** `git git`)

### Example commands:

  * init
  * add .
  * stage .
  * commit -m "inital commit"
  * %run; %exit

### Additional information for Linux users:

If you want you can remove the `.py` extension and convert it into an executable using:

    mv ./git.py ./git
    chmod +x ./git

Then instead of calling the script like this:

    python3 git.py

You'd run this instead:

    ./git

### Additional information for lazy people:

If you're really lazy and don't want to type out a `./` then you could move this script to your `/bin/` folder and create an alias for it.

If you're *really, __really__ lazy* use the following commands:

    sudo cp ./git /bin/nogit
    sudo chmod +x /bin/nogit
    alias nogit='/bin/nogit'

If you're *really, really, __really__* lazy just copy and paste the following line:

    sudo cp ./git /bin/nogit && sudo chmod +x /bin/nogit && alias nogit='/bin/nogit'
