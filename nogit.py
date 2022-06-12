  #!/usr/bin/env python
  import sys, os, signal, atexit, readline, subprocess

  commands, stop, history_file = [], False, os.path.join(os.getcwd(), "nogit.history")

  def run_commands():
    stop = True
    for cmd in commands:
      command = ["git" if not cmd.startswith("git ") else ""]
      command = [cmd] if command[0] == "" else [command[0], cmd]
      subprocess.Popen(command).communicate()
      commands = []

  def signal_handler(sig, frame):
    run_commands()
    sys.exit(0)

  try:
    readline.read_history_file(history_file)
    signal.signal(signal.SIGINT, signal_handler)
    while True:
      if stop == True:
        break
      command = input("git> ")
      if command == "%undo":
        commands.pop()
      elif command == "%run":
        run_commands()
      elif command == "%exit":
        sys.exit(0)
      else:
        commands += [cmd.strip() for cmd in command.split(";")]
    signal.pause()
    readline.set_history_length(-1)
  except IOError:
    pass

  atexit.register(readline.write_history_file, history_file)
