from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>My Personal Website</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: white;
            }

            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 25px 8%;
                background: #0f172a;
            }

            .logo {
                font-size: 24px;
                font-weight: bold;
            }

            nav a {
                color: #cbd5e1;
                text-decoration: none;
                margin-left: 30px;
            }

            nav a:hover {
                color: #38bdf8;
            }

            .hero {
                min-height: 80vh;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                padding: 40px 20px;
            }

            .hero-content {
                max-width: 800px;
            }

            .hero h1 {
                font-size: 60px;
                margin-bottom: 20px;
            }

            .hero h1 span {
                color: #38bdf8;
            }

            .hero h2 {
                font-size: 28px;
                color: #cbd5e1;
                margin-bottom: 20px;
            }

            .hero p {
                font-size: 18px;
                line-height: 1.7;
                color: #94a3b8;
                margin-bottom: 35px;
            }

            .buttons {
                display: flex;
                justify-content: center;
                gap: 15px;
            }

            .btn {
                padding: 14px 25px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
            }

            .primary {
                background: #38bdf8;
                color: #0f172a;
            }

            .secondary {
                border: 1px solid #38bdf8;
                color: #38bdf8;
            }

            .primary:hover {
                background: #0ea5e9;
            }

            .secondary:hover {
                background: #38bdf8;
                color: #0f172a;
            }

            .section {
                padding: 80px 8%;
                background: #111827;
                text-align: center;
            }

            .section h2 {
                font-size: 35px;
                margin-bottom: 40px;
            }

            .cards {
                display: flex;
                justify-content: center;
                gap: 25px;
                flex-wrap: wrap;
            }

            .card {
                background: #1e293b;
                padding: 30px;
                border-radius: 12px;
                width: 280px;
                text-align: left;
            }

            .card h3 {
                margin-bottom: 15px;
                color: #38bdf8;
            }

            .card p {
                color: #94a3b8;
                line-height: 1.6;
            }

            footer {
                text-align: center;
                padding: 30px;
                color: #64748b;
            }

            @media (max-width: 600px) {
                .hero h1 {
                    font-size: 42px;
                }

                .hero h2 {
                    font-size: 22px;
                }

                nav {
                    flex-direction: column;
                    gap: 15px;
                }

                nav a {
                    margin-left: 10px;
                }

                .buttons {
                    flex-direction: column;
                }
            }
        </style>
    </head>

    <body>

        <nav>
            <div class="logo">My Portfolio</div>

            <div>
                <a href="/">Home</a>
                <a href="#about">About</a>
                <a href="#projects">Projects</a>
                <a href="#contact">Contact</a>
            </div>
        </nav>


        <section class="hero">

            <div class="hero-content">

                <h1>
                    Hi, I'm <span>Michael</span>
                </h1>

                <h2>
                    Software Engineer & Developer
                </h2>

                <p>
                    I build reliable, scalable and user-friendly software
                    applications using modern technologies. Welcome to my
                    personal website.
                </p>

                <div class="buttons">
                    <a href="#projects" class="btn primary">
                        View My Work
                    </a>

                    <a href="#contact" class="btn secondary">
                        Contact Me
                    </a>
                </div>

            </div>

        </section>


        <section class="section" id="about">

            <h2>About Me</h2>

            <div class="cards">

                <div class="card">
                    <h3>Backend Development</h3>
                    <p>
                        Building APIs and backend applications using
                        Python, Java, Scala and modern frameworks.
                    </p>
                </div>

                <div class="card">
                    <h3>Cloud & DevOps</h3>
                    <p>
                        Experience working with AWS, Docker, CI/CD,
                        infrastructure and cloud-based applications.
                    </p>
                </div>

                <div class="card">
                    <h3>Frontend Development</h3>
                    <p>
                        Creating modern web interfaces using React,
                        Next.js and TypeScript.
                    </p>
                </div>

            </div>

        </section>


        <section class="section" id="projects">

            <h2>My Projects</h2>

            <div class="cards">

                <div class="card">
                    <h3>Project One</h3>
                    <p>
                        A web application designed to solve real-world
                        business problems.
                    </p>
                </div>

                <div class="card">
                    <h3>Project Two</h3>
                    <p>
                        A scalable backend application with REST APIs
                        and cloud infrastructure.
                    </p>
                </div>

                <div class="card">
                    <h3>Project Three</h3>
                    <p>
                        A modern frontend application built with
                        React and TypeScript.
                    </p>
                </div>

            </div>

        </section>


        <section class="section" id="contact">

            <h2>Let's Connect</h2>

            <p style="color: #94a3b8; margin-bottom: 25px;">
                Interested in working together? I'd love to hear from you.
            </p>

            <a
                href="mailto:your@email.com"
                class="btn primary"
            >
                Get In Touch
            </a>

        </section>


        <footer>
            © 2026 Michael. All rights reserved.
        </footer>

    </body>
    </html>
    """


@app.get("/health")
def health():
    return {"status": "ok"}