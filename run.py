from flaskblog import create_app
app = create_app()

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(port=8000,debug=True)
=======
    app.run(host="0.0.0.0", port=8000,debug=True)
>>>>>>> b460bc3e21976f06c3e6f6c2eaff3ecc45f8509c
