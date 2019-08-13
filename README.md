# Requirements
Create a simple todo application where users can:

**Functionality:**

- Show a list of tasks and task attributes (see "Task attributes" section for more details)
- Create, edit, remove tasks, and assign due date/time to task
- Create labels and assign labels to tasks
- (Optional) Create a alternative calendar style view of tasks
- (Optional) Implement ability to filter task list by task labels
- (Optional) Unit tests

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
