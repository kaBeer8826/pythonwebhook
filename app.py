from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "7177778705:AAHKaWzyh6H5Lx3YORLNnaN6skRf59tNlgY"
CHAT_ID = 5986647673

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Process the received webhook data
    stocks = data.get('stocks')
    trigger_prices = data.get('trigger_prices')
    triggered_at = data.get('triggered_at')
    scan_name = data.get('scan_name')
    scan_url = data.get('scan_url')
    alert_name = data.get('alert_name')

    # Format the message to send to Telegram
    message = f"Alert: {alert_name}\nScan: {scan_name}\nTriggered at: {triggered_at}\nStocks: {stocks}\nTrigger Prices: {trigger_prices}\nScan URL: {scan_url}"

    # Send the message to Telegram
    send_telegram_message(message)

    return jsonify({"message": "Webhook received and processed successfully"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
