from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def w209():
    file='about9.jpg'
    return render_template('w209.html',file=file)
    
@app.route('/api')  
def api():
    return jsonify(x=42)
    
if __name__ == '__main__':
    app.run()
