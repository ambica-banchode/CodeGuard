from app import create_app  # Changed from relative to absolute import

app = create_app()

@app.route('/')
def home():
    return "Hello, CodeGuard!"
