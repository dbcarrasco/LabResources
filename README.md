# LabResources

This repo hosts resources for lab sessions, **including all assignment Jupyter notebooks**.  Clone the repo to a location you'll maintain throughout the course (not inside other course org repos, e.g., not inside your local copy of your course repo, named according to your GitHub username).  You'll only need to clone this repo *once*.  Afterward, running `git pull` at the start of each lab session (in a terminal opened to your local `LabResources` folder) will update your local copy of the repo to contain the latest lab content, including the latest assignment.

Assignments will typically be provided as a Jupyter notebook named `AssignmentXX.ipynb` that provides explanatory information along with problem descriptions, and a solutions template, `SolutionsXX,ipynb`, that contains only the problem descriptions.  You should edit a copy of the solutions template (in your own course GitHub org repo) to complete the assignment.

## Assignment submission

Please follow these instructions:

1. After cloning or pulling the latest LabResources repo content, **copy** the `SolutionsXX.ipynb` template into your repo for the course's GitHub org (the repo you used to submit the Assignment01 "README.md" file, named according to your GitHub username).  If the assignment uses other resources (e.g., Python modules or data files), copy those as well.

2. Work on the assignment in your repo.  For each working session:
    * Open a terminal session with your repo as the working director.
    * Activate the `bda18` `conda` environment.
    * Launch the Jupyter notebook server with the commande: `jupyter noteboook`. This should open a tab in your default web browser with the Jupyter notebook interface.
    * Edit the `SolutionsXX.ipynb` notebook with your solutions in new cells created below each problem.  Feel free to add and commit any intermediate stages of your work, and to push intermediate stages back to GitHub if you wish.

3. When you are done working on the assignment, be sure to add and commit your final solutions (and any other resources you may have had to edit or create) in your local repo.
4. Push your repo back to the course org using: `git push`
5. Visit the [course org on GitHub](https://github.com/CU-BDA-2018) to make sure your content was pushed. You won't be able to view the notebook there, but you'll be able to see when the repo was last updated.