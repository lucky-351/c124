from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        "contact":"998764456",
        "Name":"raju",
        "done": False,
        "id": 1
    },
    {
        "contact":"9987643356",
        "Name":"rahul",
        "done": False,
        "id": 2
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message": "contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contact
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)