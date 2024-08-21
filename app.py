from flask import Flask, request, jsonify #jsoninfy faz com que um return se tranforme em json
from models.tasks import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def creat_tasks():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ''))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message":"Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]# o to.dict tranforma em dicionario, esta a classe Task

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        
    return jsonify({"message":"Não foi possivel encontrar sua atividade"}), 404#o 404 e para dar o error 404,o not found

@app.route ('/tasks/<int:id>', methods=['PUT'])
def update_task(id):

    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break #O break faz com que, quando a task seja achada, ele nao percorra o resto do dicionario
    
    if task == None:
        return jsonify({"message":"Não foi possivel encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({'message':'Tarefa atualizada com sucesso'})#nao precisa colocar o 200 pois ele ja e padrão

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break #O break faz com que, quando a task seja achada, ele nao percorra o resto do dicionario

    if not task:
        return jsonify({"message":"Não foi possivel encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message":"Tarefa deletada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)