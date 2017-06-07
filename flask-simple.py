#!/home/lokesh/.virtualenvs/python2.7/bin/python2.7
from flask import Flask,jsonify,render_template
from get_player_odds import main

app = Flask(__name__)

@app.route('/players/list', methods=['GET'])
def index():
    _json = main()
    return jsonify({'players':_json})

@app.route('/')
def _main():
    players_dict = main()
    return render_template('index.html', players_dict=players_dict, total=0, teams=0)


if __name__ == '__main__':
    app.run(debug=True)