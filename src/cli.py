import sys
import cmd
# import nemo_api
cmd.Cmd.prompt = '(nemoverse-sdk) '

from nemo_api import __version__
from nemo_api.cli import *

def show_version():
  return "{0}".format(__version__)

class CLI(cmd.Cmd):

  def do_version(self, line):
    "show CLI version"
    print(show_version())

  def do_exit(self, line):
    "exit CLI"
    return True
  
  def do_dsa(self, line):
    "dsa <algorithm> <action> [key] [message] [signature]\n\t<algorithm>: secp256k1 | Ed25519\n\t<action>: generate | sign | verify"
    args = line.split(' ')
    print(dsa(*args))

def main_loop():
  try:
    CLI().cmdloop()
  except Exception as e:
    print(e)
    main_loop()

def main_once():
  del sys.argv[0]
  line = " ".join(sys.argv)
  CLI().onecmd(line)

def main():
  if len(sys.argv) > 1:
    main_once()
  else:
    main_loop()

if __name__ == '__main__':
  main()