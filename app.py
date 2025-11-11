from flask import Flask, send_from_directory
import mysql.connector

app = Flask(__name__)

def get_time_from_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="change_this_strong_password",
        database="exampledb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT NOW()")
    result = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return result

@app.route('/')
def home():
    current_time = get_time_from_db()
    return f"""
    <!DOCTYPE html>
    <html lang="fi">
    <head>
        <meta charset="UTF-8">
        <title>Kikkeli</title>
        <style>
            body {{
                background: #0f172a;
                color: #e5e7eb;
                text-align: center;
                font-family: system-ui, sans-serif;
                margin-top: 3rem;
            }}
            h1 {{
                margin-bottom: 0.5rem;
            }}
            .time {{
                font-size: 1.5rem;
                color: #38bdf8;
                margin-bottom: 1.5rem;
            }}
            img {{
                max-width: 400px;
                height: auto;
                border-radius: 12px;
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }}
        </style>
    </head>
    <body>
        <h1>Ajan rakenne on muuttunut</h1>
        <div class="time">{current_time}</div>
        <img src="/kello/kello.jpg" alt="Kellokuva">
    </body>
    </html>
    """

@app.route('/kello/<path:filename>')
def serve_kello_file(filename):
    return send_from_directory('kello', filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
