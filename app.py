from flask import Flask, render_template_string

app = Flask(__name__)

PAGE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>hi with a heart</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: #fef9f1;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 1.5rem;
            font-family: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
            padding: 1rem;
        }

        .greeting {
            font-size: clamp(4rem, 20vw, 10rem);
            font-weight: 400;
            color: #2e2e2e;
            text-align: center;
            line-height: 1.2;
            word-break: break-word;
            text-shadow: 0 4px 12px rgba(0, 0, 0, 0.02);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* The heart starts hidden and scaled to zero */
        .heart {
            display: inline-block;
            font-size: 1.2em;
            margin-left: 0.15em;
            filter: drop-shadow(0 4px 8px rgba(255, 100, 100, 0.25));
            transform: scale(0);
            transform-origin: center;
            opacity: 0;
        }

        /* When this class is added, the heart pops in */
        .heart.pop {
            animation: popIn 0.6s cubic-bezier(0.18, 0.89, 0.32, 1.28) forwards,
                       softBeat 1.8s ease-in-out 0.6s infinite;
        }

        .click-me {
            font-size: 1.5rem;
            font-weight: 600;
            color: #ff4f6b;
            cursor: pointer;
            user-select: none;
            padding: 0.5rem 1.25rem;
            border-radius: 999px;
            transition: background 0.2s ease, transform 0.15s ease;
        }

        .click-me:hover {
            background: rgba(255, 107, 129, 0.12);
            transform: translateY(-1px);
        }

        .click-me:active {
            transform: scale(0.96);
        }

        .click-me.hidden {
            display: none;
        }

        @keyframes popIn {
            0% {
                transform: scale(0) rotate(-20deg);
                opacity: 0;
            }
            60% {
                transform: scale(1.4) rotate(10deg);
                opacity: 1;
            }
            80% {
                transform: scale(0.9) rotate(-4deg);
            }
            100% {
                transform: scale(1) rotate(0deg);
                opacity: 1;
            }
        }

        @keyframes softBeat {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.12); }
        }

        @media (prefers-reduced-motion: reduce) {
            .heart.pop {
                animation: none;
                transform: scale(1);
                opacity: 1;
            }
        }
    </style>
</head>
<body>
    <div class="greeting">
        hi <span class="heart" id="heart" aria-hidden="true">❤️</span>
    </div>

    <div class="click-me" id="clickMe" role="button" tabindex="0">Click me</div>

    <script>
        const heart = document.getElementById('heart');
        const clickMe = document.getElementById('clickMe');

        function popHeart() {
            // Show heart with popping animation
            heart.classList.add('pop');

            // Hide the "Click me" message
            clickMe.classList.add('hidden');
        }

        clickMe.addEventListener('click', popHeart);

        // Keyboard support (Enter / Space)
        clickMe.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                popHeart();
            }
        });
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(PAGE_HTML)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)