<h3>Documentation:</h3>
<ul>
  <li><code>%undo</code> deletes the last command from the stack</li>
  <li><code>%run</code> executes all commands in the stack and deletes it when done</li>
  <li><code>%exit</code> closes the CLI without doing anything</li>
  <li><code>ctrl+c</code> has the same effect as executing <code>%run; %exit</code> or <code>%run</code> and <code>%exit</code></li>
  <li>Command history gets saved to a file called <code>nogit.history</code> in the same folder as the script</li>
  <li>You can add multiple commands in one line using a semi-colon</li>
  <li>You can use the <code>git</code> keyword because the script doesn't add the <code>git</code> keyword if it already exists</li>
</ul>

<h3>Demonstration:</h3>

<ol>
  <li><code>init</code></li>
  <li><code>add -A</code></li>
  <li><code>stage -A</code></li>
  <li><code>status</code></li>
  <li><code>commit -m "initial commit"</code></li>
  <li><code>%run; %exit</code></li>
</ol>

<h3>Installation:</h3>
<p>To run NoGit, you need <a href="https://www.python.org/downloads/">Python 3</a> installed on your system. You can download it from the official <a href="https://github.com/LogicalBranch/NoGit">Github Repository</a> or copy the source code below.</p>
<p><b>Note</b>: The script depends on the <a href="https://docs.python.org/3/library/sys.html">sys</a>, <a href="https://docs.python.org/3/library/os.html">os</a>, <a href="https://docs.python.org/3/library/signal.html">signal</a>, <a href="https://docs.python.org/3/library/atexit.html">atexit</a>, <a href="https://docs.python.org/3/library/readline.html">readline</a> and <a href="https://docs.python.org/3/library/subprocess.html">subprocess</a> modules.</p>

<h3>Installation notes (Linux):</h3>
<p>If you want you can remove the <code>.py</code> extension and convert it into an executable:</p>

```shell
mv nogit.py nogit
chmod +x ./nogit
./nogit # open the NoGit CLI
```

<p>You can also move this script to your <code>./bin/</code> directory and create an alias for it to run it without a <code>./</code>:</p>

```shell
sudo cp ./nogit /bin/nogit
sudo chmod +x /bin/nogit
alias nogit="/bin/nogit"
```

<p>Alternatively you can copy the following command into your CLI:</p>

```shell
git /bin/nogit && sudo chmod +x /bin/nogit && alias nogit='/bin/nogit'
```
