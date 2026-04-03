from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Resume Form</h2>
    <form method="POST" action="/submit">
        Name: <input name="name"><br>
        Email: <input name="email"><br>
        Phone: <input name="phone"><br>
        <button type="submit">Submit</button>
    </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    return f'''
    <h2>Resume Preview</h2>
    Name: {name}<br>
    Email: {email}<br>
    Phone: {phone}
    '''

if __name__ == '__main__':
    app.run(debug=True)