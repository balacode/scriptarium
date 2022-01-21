# ------------------------------------------------------------------------------
# Python Scripts                                         scriptarium/[gitlog.py]
# (c) balarabe@protonmail.com
# ------------------------------------------------------------------------------

import argparse
import os
import subprocess

# read named parameters from the command line:
pr = argparse.ArgumentParser()
pr.add_argument('--source', help='path to the source Git repository')
pr.add_argument('--author', help='name of author to select (exclude others)')
pr.add_argument('--target', help='target file into which to write changelog')
pr.add_argument('--prefix', help='optional prefix to append before repo name')
args = pr.parse_args()
#
if args.source == None:
    print('--source not specified')
    quit()
if args.author == None:
    print('--author not specified')
    quit()
if args.target == None:
    print('--target not specified')
    quit()
if args.prefix == None:
    args.prefix = ""

# change current directory and build repo name
os.chdir(args.source)
cwd = os.getcwd()
parts = cwd.split('/')
repo_name = args.prefix + parts[len(parts)-1]
print('cwd:', cwd, "repo_name:", repo_name)

# execute 'git log' command and store its output in 'lines'
proc = subprocess.Popen(
    ['git', 'log', '-200', '--date=local', '--pretty=format:"%ai %an: %s"'],
    stdout = subprocess.PIPE
)
text = proc.communicate()[0].decode('utf-8')
lines = text.split('\n')

# filter lines by author name, replace author with repo_name
text = '\n\n'
for s in lines:
    if not args.author in s:
        continue
    s = s[1:len(s)-1] # remove leading and trailing double quotes
    s = s[0:20] + s[26:] # remove timezone e.g. +0100
    s = s.replace(args.author, repo_name)
    text += s + '\n'

# append text to target file
fl = open(args.target, 'a')
fl.write(text)
fl.close()

quit()

# sample zsh script to update multiple repos:
# (replace SOME_.. with actual paths and names)
#
# for repo in \
#     "/SOME_PATH/REPO1" \
#     "/SOME_PATH/REPO2"
# do
#     python3 /SOME_PATH/scriptarium/gitlog.py \
#         --source $repo \
#         --prefix "SOME_PREFIX/" --author "SOME_AUTHOR_NAME" \
#         --target /SOME_PATH/SOME_TARGET.txt
# done

# end
