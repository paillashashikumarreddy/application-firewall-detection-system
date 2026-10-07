from flask import Flask, request
from firewall import firewall, logs

app = Flask(__name__)

app.before_request(firewall)


@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Firewall System</title>
        <style>
            body {
                margin: 0;
                font-family: Courier New;
                background: black;
                color: #00ff00;
                text-align: center;
            }

            .blink {
                animation: blink 1s infinite;
            }

            @keyframes blink {
                50% { opacity: 0; }
            }

            .box {
                border: 1px solid #00ff00;
                padding: 20px;
                width: 80%;
                margin: auto;
            }

            .btn {
                background: #00ff00;
                padding: 15px;
                width: 200px;
                margin: 10px;
                border-radius: 5px;
                display: inline-block;
                color: black;
                text-decoration: none;
                font-weight: bold;
            }

            .btn:hover {
                background: #00cc00;
            }
        </style>
    </head>

    <body>

        <div style="padding:40px;">
            <h1>💻 APPLICATION FIREWALL</h1>
            <p class="blink">>> SYSTEM MONITORING ACTIVE...</p>
        </div>

        <div class="box">
            <p>> Initializing Security Modules...</p>
            <p>> SQL Injection Protection: ACTIVE</p>
            <p>> XSS Protection: ACTIVE</p>
            <p>> Rate Limiting: ACTIVE</p>
        </div>

        <br>

        <div>
            <a href="/login?user=guest" class="btn">🔐 LOGIN TEST</a>
            <a href="/simulate" class="btn">⚡ RUN ATTACK</a>
            <a href="/dashboard" class="btn">📊 VIEW LOGS</a>
        </div>

        <br><br>

        <div>
            <p>> Monitoring Network Traffic...</p>
            <p class="blink">>> Unauthorized Access Will Be Blocked</p>
        </div>

    </body>
    </html>
    """


@app.route('/login')
def login():
    user = request.args.get('user', 'guest')
    return f"<h2>Welcome {user}</h2>"


@app.route('/dashboard')
def dashboard():
    html = """
    <html>
    <body style="background:black; color:white; font-family:Arial;">
        <h1 style="color:orange;">🔥 Firewall Dashboard</h1>
        <hr>
    """

    if not logs:
        html += "<p>No activity yet...</p>"

    for log in logs[::-1]:
        if "BLOCKED" in log:
            html += f"<p style='color:red;'>🚨 {log}</p>"
        else:
            html += f"<p style='color:lightgreen;'>✅ {log}</p>"

    html += "</body></html>"
    return html


@app.route('/simulate')
def simulate():
    test_urls = [
        "/login?user=normal",
        "/login?user=admin",
        "/login?user=' OR 1=1",
        "/login?user=<script>alert(1)</script>"
    ]

    for url in test_urls:
        with app.test_request_context(url):
            try:
                firewall()
            except:
                pass

    return """
    <html>
    <body style="text-align:center;">
        <h2>🔥 Simulation Completed</h2>
        <a href='/dashboard'>Go to Dashboard</a>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)