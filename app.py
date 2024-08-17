from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def fetch_gif(query):
    api_key = 'replace_with_your_api'
    url = f'https://api.giphy.com/v1/gifs/search?q={query}&api_key={api_key}&limit=1'
    response = requests.get(url)
    data = response.json()
    if data['data']:
        return data['data'][0]['images']['original']['url']
    return None

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/get_gif', methods=['POST'])
def get_gif():
    data = request.get_json()
    query = data.get('query')
    gif_url = fetch_gif(query)
    return jsonify({'gif_url': gif_url})

if __name__ == '__main__':
    app.run(debug=True)
