import flask

app = flask.Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def homePage():
    return flask.render_template("homePage.html")

@app.route("/about")
def aboutPage():
    return flask.render_template("aboutPage.html")

@app.route("/contact")
@app.route("/contactUs")
def contactPage():
    return flask.render_template("contactPage.html")

###
@app.route("/ROOT")
def helloWorld():
    return "Hello World<br />" + flask.url_for("myName") + flask.url_for("myName2")

@app.route("/whoami")
def myName():
    return '<div style="text-align:center"><span style="font-weight:bold">Justin P</span></div>'

@app.route("/whoami2")
def myName2():
    #return open("/home/justin/pythonmicrosoft/myname.html").read()
    return flask.render_template('myname.html', obj={"name":"Justin","emailAdd":"asdfj@yahoo.com"})

@app.route("/string/<string:name2>/<string:name1>/")
def testGetParamStr(name1,name2):
    return "%s %s" % (name1, name2)

@app.route("/int/<int:id2>/<int:id1>")
def testGetParam(id1, id2):
    return "%d %d" % (id1, id2)

@app.route("/")
def index():
    return flask.render_template("myname2.html",obj = [flask.url_for("testGetParamStr", name1="Justin", name2="Paul"), flask.url_for("testGetParamStr", name2="Paul", name1="Justin"), flask.url_for("testGetParamStr", name2="Mark", name1="Steve")])


@app.route("/form", methods=["GET", "POST"])
def form():
    name = flask.request.args.get("name")
    if name is None:
        name = flask.request.form.get("name")

    return flask.render_template("form.html", name=name)

###

if __name__ == "__main__":
    app.run(debug=True)
