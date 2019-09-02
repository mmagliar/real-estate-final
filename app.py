from flask import Flask, render_template, request
import os, pickle

app = Flask(__name__)

# Define routes
@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        atmResult = {}
        stmResult = {}
        utmResult = {}
        userHouse = request.form.to_dict(flat=False)
        forTowns = [[userHouse['ac'][0],
                    userHouse['lp'][0],
                    userHouse['fb'][0],
                    userHouse['hb'][0],
                    userHouse['bd'][0],
                    userHouse['rooms'][0],
                    userHouse['bmnt'][0],
                    userHouse['cool'][0],
                    userHouse['heat'][0],
                    userHouse['water'][0],
                    userHouse['sewer'][0],
                    userHouse['fha'][0],
                    userHouse['la'][0],
                    userHouse['ba'][0],
                    userHouse['ta'][0]]]
        
        with open(os.path.join('static','models','countyModel'), 'rb') as f:
            model = pickle.load(f)

            cResult = sorted(zip(model.classes_, model.predict_proba([[userHouse['ac'][0],
                                        userHouse['lp'][0],
                                        userHouse['fb'][0],
                                        userHouse['hb'][0],
                                        userHouse['bd'][0],
                                        userHouse['rooms'][0],
                                        userHouse['bmnt'][0],
                                        userHouse['ext'][0],
                                        userHouse['cool'][0],
                                        userHouse['heat'][0],
                                        userHouse['water'][0],
                                        userHouse['sewer'][0],
                                        userHouse['fha'][0],
                                        userHouse['la'][0],
                                        userHouse['ba'][0],
                                        userHouse['ta'][0]]])[0]), key=lambda x: x[1], reverse=True)
        
        with open(os.path.join('static','models','allTownModel'), 'rb') as f:
            model = pickle.load(f)

            atmResult = sorted(zip(model.classes_, model.predict_proba(forTowns)[0]), key=lambda x: x[1], reverse=True)

        with open(os.path.join('static','models','sussexTownModel'), 'rb') as f:
            model = pickle.load(f)

            stmResult = sorted(zip(model.classes_, model.predict_proba(forTowns)[0]), key=lambda x: x[1], reverse=True)

        with open(os.path.join('static','models','unionTownModel'), 'rb') as f:
            model = pickle.load(f)

            utmResult = sorted(zip(model.classes_, model.predict_proba(forTowns)[0]), key=lambda x: x[1], reverse=True)

        return render_template('home.html', cResult=cResult, atmResult=atmResult, stmResult=stmResult, utmResult=utmResult)

    else:
        return render_template("home.html")

# added this route
@app.route("/info")
def info():
    return render_template("info.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)