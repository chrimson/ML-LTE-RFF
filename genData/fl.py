from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
employees = [
    {'id': 1, 'name': 'John Doe'},
    {'id': 2, 'name': 'Jane Doe'}
]

# GET all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

# GET employee by ID
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = next((e for e in employees if e['id'] == id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({'error': 'Employee not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
