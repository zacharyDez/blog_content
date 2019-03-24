from subprocess import run, Popen, call
import shlex

cmd = "ls -F -R .."
args = shlex.split(cmd)

# run(args=args)

Popen(args)

call(args)
