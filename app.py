from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", title="Welcome", message="This is a Tailwind + Jinja setup!")

if __name__ == '__main__':
    app.run(debug=True)
