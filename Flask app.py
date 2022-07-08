from flask import Flask, jsonify, request


app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'name': u'joey',
        'description': u'related to someone',
        'active': False
    },
    {
        'id': 1,
        'name': u'janet',
        'description': u'we dont know her',
        'active': True
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide data u idiot"
            },400)
    contacts = {
        'id': tasks[-1]['id']+1,
        'name': request.json['title'],
        'description': request.json.get('description', ""),
        'active': False
        }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task added succesfully!"
        })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data": contacts
        })
if __name__ == '__main__':
    app.run()
