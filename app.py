from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Get the current date
    current_date = datetime.now().strftime("%B %d, %Y")
    
    # Render the template and pass the current date
    return render_template('layout.html', current_date=current_date)

if __name__ == '__main__':
    app.run(debug=True)

