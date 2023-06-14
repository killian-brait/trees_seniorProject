# Filtering and Data Architecture in Django

### About the Project
This project is a way to filter data used in the Trees application so that
users will get better content recommendations and rate content and engage with it.

### Running the Project

1. Clone the project to your local machine
2. Install the requirements
3. Run the project

```bash
git clone <project-url>
cd trees_api
python -m venv venv <optional: venv>
conda create -n trees_api python=3.10 <optional: conda> 
pip install -r requirements.txt
python manage.py runserver
```

### Project Goals
1. Create a way to filter data using a modular service (filterApp)[filterApp/README.md]
2. Define normalized data structures that can be used to maintain a machine learning model
3. Create a CI/CD pipeline with automated testing and deployment
    - [ ] CodeClimate code quality and review tool
    - [ ] Coverage.py code coverage tool
    - [ ] GitHub Actions for CI/CD pipeline (.yaml files)
    - [ ] Google Cloud Platform for hosting and deployment
    - [ ] Docker for containerization

### Project Structure
The project is structured as a Django project with four apps: contentApp, filterApp,
questionApp, and userApp. The project is seperated this way to keep each app more 
manageable and to allow for more modular development. Django provides many tools
for linking apps together which is part of the reason it is used for this project.

The userApp includes: users, answers, and current_answers.
    - Planned: ratings, groups, tags, permissions, and roles.
The questionApp includes: questions, and demoquestions
    - Planned: types, tags, security-levels, and permissions.
The contentApp includes: contents, videos, and steps
    - Planned: more modular content with filtering based on categories, groups
    - Planned: tags, permissions, and roles.
The filterApp includes: SimpleFilter, FilterRef
    - Planned: more complex filters, and a way to combine filters
    - Planned: define algorithms for filtering and protect data with permissions
    if it is sensitive.
