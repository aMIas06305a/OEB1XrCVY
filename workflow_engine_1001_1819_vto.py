# 代码生成时间: 2025-10-01 18:19:42
import quart
from quart import jsonify

class WorkflowEngine:
    def __init__(self):
        # Dictionary to keep track of workflow tasks and their states
        self.tasks = {}

    def add_task(self, task_id, task_function):
        """
        Adds a new task to the workflow engine with a unique task ID.
        :param task_id: Unique identifier for the task
        :param task_function: Callable function that represents the task
        """
        if task_id in self.tasks:
            raise ValueError(f"Task ID {task_id} already exists.")
        self.tasks[task_id] = {'status': 'pending', 'function': task_function}

    def execute_task(self, task_id):
        """
        Executes a task if it exists and is in a pending state.
        :param task_id: Unique identifier for the task to execute
        :return: Result of the task function execution
        """
        task = self.tasks.get(task_id)
        if not task:
            raise ValueError(f"Task ID {task_id} does not exist.")
        if task['status'] != 'pending':
            raise ValueError(f"Task ID {task_id} is not in a pending state.")

        try:
            result = task['function']()
            task['status'] = 'completed'
            return result
        except Exception as e:
            task['status'] = 'failed'
            raise ValueError(f"Task ID {task_id} failed with error: {str(e)}")

    def get_task_status(self, task_id):
        """
        Retrieves the status of a task by its ID.
        :param task_id: Unique identifier for the task
        :return: Status of the task
        """
        task = self.tasks.get(task_id)
        if not task:
            raise ValueError(f"Task ID {task_id} does not exist.")
        return task['status']

# Quart application instance
app = quart.Quart(__name__)

# Create an instance of the workflow engine
workflow_engine = WorkflowEngine()

@app.route('/add_task/<string:task_id>', methods=['POST'])
async def add_task(task_id):
    "