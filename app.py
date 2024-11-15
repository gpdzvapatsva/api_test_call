#weather conditions from weatherlink station
from flask import Flask, jsonify
import requests,time, hashlib, hmac

app = Flask(__name__)
@app.route('/')
def get_weather():
    api_key = 'e9acjapvjih3rpbcnjnj8c8kfsnyivkb'
    api_secret = 'p9ltsbyvv137bkskvuerqfs7s8qbe8gy'
    station_id = 142820

    # current time
    local_time = int(time.time())

    #api signature
    data_to_sign = f"api-key{api_key}station-id{station_id}t{local_time}"
    signature = hmac.new(
        api_secret.encode('utf-8'),
        data_to_sign.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()


    url = f"https://api.weatherlink.com/v2/current/{station_id}"
    params = {
        "api-key": api_key,
        "t": local_time,
        "api-signature": signature
    }

    response = requests.get(url, params=params)
    current_weather = response.json()

    return jsonify(current_weather)

if __name__ == '__main__':
    app.run(debug=True)
