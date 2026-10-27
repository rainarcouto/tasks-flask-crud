from flask import Flask, request
from models.task import Task
app = Flask(__name__)

# CRUD
# Create, Read, Update, Delete
# Tabela: Tarefa

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
  data = request.get_json()
  return 'Test'

if __name__ == "__main__":
  app.run(debug=True)