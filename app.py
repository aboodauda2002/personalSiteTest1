from flask import Flask,render_template

app = Flask(__name__)

@app.route("/my_web")

def load_page():
	return render_template("tast_camp.html")


if __name__=="__main__":
	app.run(port = 4000,debug = True)