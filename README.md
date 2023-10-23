The echo command to create and edit the .gitignore file. Enter the following command to create the file:

echo *.csv > .gitignore

This command creates a .gitignore file and adds a rule to ignore all files with a .csv extension.

Commit the .gitignore file and push it to my GitHub repository to make sure it takes effect on the remote repository.

git add .gitignore

git commit -m "Added .gitignore to exclude CSV files"

git push origin master

With the .gitignore file in place, Git will ignore any CSV files in the repository, preventing them from being pushed to GitHub. 