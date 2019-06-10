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
