import json as json
from flask import Flask, abort, redirect, render_template, session, url_for
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
appConf = {#TODO:Add your own credentials for all the keys
    "OAUTH2_CLIENT_ID": "3611*****tent.com", 
    "OAUTH2_CLIENT_SECRET": "GOCS*****Vg",
    "OAUTH2_META_URL": "ht****ion",
    "FLASK_SECRET": "cfe*****115",
    "FLASK_PORT": 5000
}

app.secret_key = appConf.get("FLASK_SECRET")

oauth = OAuth(app)
oauth.register(
    "myApp",
    client_id=appConf.get("OAUTH2_CLIENT_ID"),
    client_secret=appConf.get("OAUTH2_CLIENT_SECRET"),
    client_kwargs={"scope": "openid profile email",},
    server_metadata_url=f'{appConf.get("OAUTH2_META_URL")}',
)


@app.route("/")
def home():
    return render_template("home.html", session = session.get("user"))


@app.route("/signin-google")
def googleCallback():
    # fetch access token and id token using authorization code
    token = oauth.myApp.authorize_access_token()
    # print(token,"\n\n",type(token))

    token = dict(token)
    print(json.dumps(token, indent = 4))
    # Extract necessary user data from the ID token
    personal = token.get('userinfo')
    user_info = {"name" : personal.get('name'),
                 "email" : personal.get('email'),
                 "id_token" : token.get('id_token')}

    # Set complete user information in the session
    print(user_info)
    session["user"] = user_info
    return redirect(url_for("home"))


@app.route("/google-login")
def googleLogin():
    if "user" in session:
        abort(404)
    return oauth.myApp.authorize_redirect(redirect_uri=url_for("googleCallback", _external=True))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=appConf.get("FLASK_PORT"), debug=True)
