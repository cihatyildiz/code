from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    return "Hello, this is your Flask app!"

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
