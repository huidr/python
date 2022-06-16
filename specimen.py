import sys

def agrv_list():
  if len(sys.argv) > 1:
    return sys.agrv[0], sys.argv[1:]
  else:
    return sys.argv[0], None

def main():
  script_name, args_name = agrv_list()
  print(script_name)
  print(args_name)

if __name__="__main__":
  main()

