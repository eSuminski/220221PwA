# Git Help

### Making a new repository on Github

1. on the home screen click the green "new" button

2. give your repository a name, and add a description if you want

3. Add a readme and gitignore file, the git ignore file will change depending on the programming language you are working with (ignore python if working with python, java if working with java, etc)

4. create the repository

5. You now have a repository on Github ready for use!

### Clone a Github repository to your local computer
1. In your repository click the green code button

2. Copy the HTTPS link

3. Open git bash in the location where you want to copy the github repo (it will copy into a folder)

4. use the clone command to clone the repo
```cli
git clone HTTP-link
```

5. You now have a local version of the github repo!


### Adding and committing files to your local repository
1. move the files you wish to track into staging. Use . if you want to add everything
```cli
git add files, go, here
```
2. commit the changes you made so they are persisted
```cli
git commit -m "message should give a brief explanation of what you added to the repository"
```
3. Your branch is now up to date and (if it is not the main branch) it can be merged

### reverting to old files
1. get the records of previous commits. Adding --oneline to the end makes it easier to work with
```cli
git log --oneline
``
2. use the checkout command to get a version of an older file and replace it in the current branch
```cli
git checkout id-for-old-commit file_name.extension
```
3. the old version of the file is now current, and it is automatically placed into staging. You can commit it or work on it anew

### Pushing changes you've made locally to your github repo
1. It is good practice to first pull from the repo you are going to push to. This helps prevent merge errors
```cli
git pull origin branch-you-are-going-to-push-to
```

2. make sure yo add and commit your changes. Deal with any merge conflicts

3. Once you've delt with any merge issues you can use the push command to send your changes to github
```cli
git push
```