from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()

    # Check if all required fields are present
    if not data or 'name' not in data or 'email' not in data or 'age' not in data:
        return jsonify({"error": "Missing required fields (name, email, age)"}), 400

    name = data['name']
    email = data['email']
    age = data['age']

    # Validate email
    if '@' not in email or '.' not in email:
        return jsonify({"error": "Invalid email format"}), 400

    # Validate age
    if not isinstance(age, int) or age <= 0:
        return jsonify({"error": "Age must be a positive integer"}), 400

    return jsonify({"message": "User created successfully"}), 201

# Global 404 Error Handler
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": str(e)}), 404

# Global Exception Handler
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": f"Something went wrong: {str(e)}"}), 500
