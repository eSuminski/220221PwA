## Installation
See Git_Install_help markdown
## Intro 
Git is an incredibly popular version control software that helps developers collaborate on projects. Think of it as a central repository for the source code you are working on that many devolopers can work on simultaniously. The basic workflow for copying, modifying, and persisting the changes you make are as follows (note that this assumes you have already create a repository):
1. clone the repository you are going to be working with. If you have already done this you can skip to step 2
    - git clone repository_link_goes_here
2. to update the repository with the most recent code use the pull command
    - git pull repository_link_goes_here
3. to add your new work to staging use the add command
    - git add . (the period means add all new work to staging. Can also specify files and folders)
4. to commit your work you need to use the commit command
    - git commit -m "brief description of commit" (-m means you are adding a message to the commit)
5. when you are ready to push your new committed work to the repo you use the push command
    - git push
These are the basic commands you can use if working by yourself, but if you are working with a team you will want everyone to work on their own "branch" of the code for simultanious programming
## Branching Structure
Git's setup encourages developers to use a branching structure for their projects. This is done by thinking of your project as a "tree" that has multiple "branches". Your going to have a main branch: this is typically going to be your working code. You then will have development branches off the main branch that you and your fellow devlopers use to create new features and fixes for the main branch. You can make the structure as simple or complicated as needed for the project. The benefit of this branching structure is that you can work on your code without affecting the primary source code: by working on the source code and commiting it to a seperate branch from the main you are preventing any mistakes or bugs you add to the code from affecting the main source code. This adds a layer of protection to your project, but it is not a flawless system. You and any fellow developers still have to check your code for errors, but the structure provides built in protection from accidently ruining your main code because of an accidental upload.
1. clone the repo you will work with
    - make sure to cd into the create file: you should see an indication that you are in the cloned repo
2. create a new branch of the repo and make sure to switch to it (check-out the branch)
    - git checkout -b NewBranchName (the -b indicates you are creating a new branch, leave it off for an already created branch)
3. after adding and commiting your changes you need to do a slightly altered push
    - git push -u origin branch_you_are_pusing_to
    - this make sure that any fetch, pull, and push requests in the future will go to the remote repo you are working on
4. You now can make a pull request inside of github
    - go to the main branch of the repo and access the pull request
    - confirm the request
    - check for any merge conflicts
        - resolve the conflicts if need be
    - approve merge
    - (optional) delete old branch if it is no longer needed
## Merging
Merging is, simply put, combining two different branches. When you merge a branch it takes all the previous commits lump-sum and attempts to add the changes to the target branch. So, if you are attempting to update your main branch, you want it to be your selected branch you are working with. You would then use the command "git merge branch_you_want_to_merge" and it will take the committed data of the branch you indicate in the command and add its code to your currently selected branch. Much of this process can be handled in Github.

If you are trying to update an offshoot branch (you have been working on a feature you want to add to the main, and you created your own brnach for it) you can simply follow the Intro section commands to update your branch, then proceed to merge the changes into the main branch.
## Merge Conflicts
Merge conflicts happen when you try to merge between branches that have conflicting changes to the code (one branch deleted a line of code while the other adjusted the code instead of deleting it). In these instances you will be informed by git that there is a merge conflict and you will be prompted to fix it. This can ususally be handled in your IED, but you can also handle it in Github. You will be shown where the conflict is between the two branches: The information will look something like this:
```cli
>>>>>>>> HEAD

=========

<<<<<<<<< merging_branch
```
inbetween the head and ========== will be the conflicting code in your current branch, between the ======== and merging_branch will be the conflicting code of the other branch. To fix the conflict you can go into the offending branch, edit the code, re add and commit, then merge again. Some IDEs will allow you to see conflicts in real time and import the correct version of the conflict.
## Pull Requests (Code Review)
Pull requests create notifications for collaborators that the feature/fix you were working on is complete. It provdes an opportunity for the others to review your work, and you can even make new commits if changes need to be made within the pull request. This is particularly useful when you set up branch protection rules, like not allowing a pull request to be merged until one or more people who are not the initial requester approve of the request. You can create branch protection within github by going to the branch settings in the repository. Under protect matching branches you can require a pull request instead of direct merging with the main branch, and you can indicate how many people need to approve the pull request in the same section.