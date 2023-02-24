#!/usr/bin/env bash
# this is a shell script that helps me simplify adding and pushing to github
# Usage:
#	echo "whatever commit message you want to use" | ./test.sh
# your commit message is read as an input and then all files are added, commited and pushed to your current remote branch on the repository
read commit_message
git add .
git commit -m "$commit_message"
git push
