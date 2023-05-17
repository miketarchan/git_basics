mkdir project
cd project
git init
touch project/README.md
git add project/README.md
git commit -m "init repository"
git checkout -b first_branch
vim project/README.md
git add project/README.md
git commit -m "feat(lesson-2): implement 3th lesson's task"
git checkout master
vim project/README.md
git add project/README.md
git commit -m "feat(lesson-2): implement 4th lesson's task"
