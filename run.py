from flasktut import create_app

app = create_app()

# Vercel serverless entry point uses the `app` variable above.
# Local development uses the block below.
if __name__ == '__main__':
    app.run(debug=True)
