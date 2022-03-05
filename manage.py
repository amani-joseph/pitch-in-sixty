from app import create_app


#creating an app instance
app = create_app('production')


if __name__ == '__main__':
    app.run(debug=True)
