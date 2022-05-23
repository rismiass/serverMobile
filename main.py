from flask import redirect, render_template, Flask, request, jsonify
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ryasov_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
picture = ''


@app.route('/sign-in', methods=['POST'])
def main():
    print(request.json)
    return jsonify({"token": "fh.wsRFHWRNwrsnhkglnwrhklrwn"})


if __name__ == '__main__':
    app.run()
