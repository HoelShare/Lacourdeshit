import sys

class bcolors(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

sys.stderr.write("-" * 80 + "\n")

def info(message, runtime, name):
    sys.stdout.write("[%s%s%s] (%s%4d%s): INFO: %s\n" % (bcolors.HEADER, name, bcolors.ENDC, bcolors.OKGREEN, runtime.get_runtime(), bcolors.ENDC, message))
    sys.stdout.write("-" * 80 + "\n")

def warning(message, runtime, name):
    sys.stdout.write("[%s%s%s] (%s%4d%s): %sWARNING: %s%s\n" % (bcolors.HEADER, name, bcolors.ENDC, bcolors.OKGREEN, runtime.get_runtime(), bcolors.ENDC, bcolors.WARNING, message, bcolors.ENDC))
    sys.stdout.write("-" * 80 + "\n")

def error(message, runtime, name):
    sys.stderr.write("[%s%s%s] (%s%4d%s): %sERROR: %s%s\n" % (bcolors.HEADER, name, bcolors.ENDC, bcolors.OKGREEN, runtime.get_runtime(), bcolors.ENDC, bcolors.FAIL, message, bcolors.ENDC))
    sys.stderr.write("-" * 80 + "\n")


if __name__ == "__main__":
    import runtime
    info("Hello world", runtime, __name__)
    warning("Test", runtime, __name__)
    error("OH NOSE!", runtime, __name__)
