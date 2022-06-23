## Documentation:
* `%undo` deletes the last command from the stack
* `%run<`executes all commands in the stack and deletes it when done
* `%exit` closes the CLI without doing anything
* `ctrl+c` has the same effect as executing `%run; %exit` or `%run` and `%exit`
* Command history gets saved to a file called `nogit.history` in the same folder as the script
* You can add multiple commands in one line using a semi-colon
* You can use the `git` keyword because the script doesn't add the `git` keyword if it already exists


## Demonstration:
1. `init`
2. `add -A`
3. `stage -A`
4. `status`
5. `commit -m "initial commit"`
6. `%run; %exit`

## Installation:
To run NoGit, you need <a href="https://www.python.org/downloads/">Python 3</a> installed on your system. You can download it from the official <a href="https://github.com/LogicalBranch/NoGit">Github Repository</a> or copy the source code below.

**Note**: The script depends on the <a href="https://docs.python.org/3/library/sys.html">sys</a>, <a href="https://docs.python.org/3/library/os.html">os</a>, <a href="https://docs.python.org/3/library/signal.html">signal</a>, <a href="https://docs.python.org/3/library/atexit.html">atexit</a>, <a href="https://docs.python.org/3/library/readline.html">readline</a> and <a href="https://docs.python.org/3/library/subprocess.html">subprocess</a> modules.

## Installation notes (Linux):
If you want you can remove the `.py` extension and convert it into an executable:

```shell
mv nogit.py nogit
chmod +x ./nogit
./nogit # open the NoGit CLI
```

You can also move this script to your `./bin/` directory and create an alias for it to run it without a `./`:

```shell
sudo cp ./nogit /bin/nogit
sudo chmod +x /bin/nogit
alias nogit="/bin/nogit"
```

Alternatively you can copy the following command into your CLI:

```shell
git /bin/nogit && sudo chmod +x /bin/nogit && alias nogit='/bin/nogit'
```

## More information:
To read the full article, visit: [How to avoid retyping the "Git" keyword](https://logicalbranch.github.io/articles/Git/how-to-avoid-retyping-the-git-keyword.html).
