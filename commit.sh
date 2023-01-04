#!bin/zsh

cd `dirname $0`

black . 
autoflake .
isort .

npx prettier --write .

git add .
git commit -m "$1"
git push

echo "Done."