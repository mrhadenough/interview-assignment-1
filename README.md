# Requirements
Create a simple todo application where users can:

**Functionality:**

- [x] Show a list of tasks and task attributes (see "Task attributes" section for more details)
- [x] Create, edit, remove tasks, and assign due date/time to task
- [x] Create labels and assign labels to tasks
- [x] (Optional) Create a alternative calendar style view of tasks
- [ ] (Optional) Implement ability to filter task list by task labels
- [ ] (Optional) Unit tests

**Other task parameters:**

- This assignment should be written in Django, and leverage only standard django library
- Include some basic insturctions to install dependencies and run application
- A very basic front-end is sufficient (no sytling or javascript required)
- Do not spend more than a couple hours on this task, we are more interested in your server implementation


**Tasks attributes:**

- Title
- Whether or not the task was completed
- Zero or more task labels (Task can be associated with many different labels)
- Calendar event associated with task (can be null)


**Task label attributes:**

- Name (unique)
- One label can be associated with many tasks

**Calendar event attributes:**

- Date/time

### How to run

run PostgreSQL, connect to it and create database (default is "todo")

Usualy I'm doing this like in the following command
```
docker run --name postgres --restart=always -e POSTGRES_PASSWORD=postgres -p 127.0.0.1:5432:5432 -v $HOME/Documents/docker_volumes/postgres:/var/lib/postgresql/data -d postgres:10.4-alpine
```

```
brew install pipenv
pipenv shell --python 3.7.3
pipenv install
./manage.py migrate
./manage.py createsuperuser # if you want to use admin and see the models
```
