from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def portfolio():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Portfolio</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
            }
            header {
                background-color: #333;
                color: white;
                padding: 1rem;
                text-align: center;
            }
            section {
                padding: 2rem;
                text-align: center;
            }
            .projects {
                display: flex;
                justify-content: center;
                gap: 1rem;
                flex-wrap: wrap;
            }
            .project {
                background: white;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 1rem;
                width: 300px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }
            .project img {
                width: 100%;
                border-radius: 5px;
            }
            footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 1rem;
                margin-top: 2rem;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>My Portfolio</h1>
        </header>
        <section>
            <h2>About Me</h2>
            <p>Hello! I am a passionate developer who loves creating web applications and solving problems.</p>
        </section>
        <section>
            <h2>Projects</h2>
            <div class="projects">
                <div class="project">
                    <img src="https://via.placeholder.com/300" alt="Project 1">
                    <h3>Project 1</h3>
                    <p>Description of Project 1.</p>
                </div>
                <div class="project">
                    <img src="https://via.placeholder.com/300" alt="Project 2">
                    <h3>Project 2</h3>
                    <p>Description of Project 2.</p>
                </div>
                <div class="project">
                    <img src="https://via.placeholder.com/300" alt="Project 3">
                    <h3>Project 3</h3>
                    <p>Description of Project 3.</p>
                </div>
            </div>
        </section>
        <footer>
            <p>© 2024 My Portfolio. All Rights Reserved.</p>
        </footer>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)