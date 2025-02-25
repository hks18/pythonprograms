from flask import Flask, request, jsonify
import pywhatkit
import time
import pyautogui

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        data = request.json
        
        # Intentional error for testing
        if not data:
            raise ValueError("No data received!")
        
        phone = data.get('phone')
        message = data.get('message')
        hour = int(data.get('hour'))
        minute = int(data.get('minute'))

        if not phone or not message:
            raise ValueError("Phone number and message cannot be empty!")

        # Send message using pywhatkit
        pywhatkit.sendwhatmsg(phone, message, hour, minute)

        # Wait for WhatsApp Web to load
        time.sleep(15)  

        # Press Enter to send the message automatically
        pyautogui.press("enter")

        return jsonify({"message": "Message sent successfully!"})

    except ValueError as ve:
        return jsonify({"message": "Invalid input", "error": str(ve)}), 400

    except Exception as e:
        return jsonify({"message": "Error sending message", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
