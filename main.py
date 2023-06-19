from flask import Flask , render_template

app=Flask(__name__ , template_folder='Template' , static_folder='StaticFiles')

@app.route('/')

def  home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

if __name__ == "__main__":
    app.run(debug=False , host='0.0.0.0')

