from flask import Flask, flash, redirect, render_template, request, session, url_for
import sqlite3

app = Flask(__name__)

app.secret_key = "your_secret_key"


# Function to get the list of books from the database
def get_books():
    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    conn.close()
    return books


@app.route("/")
def book_list():
    if "user_id" not in session:
        return redirect(url_for("login"))

    books = get_books()
    return render_template("books.html", books=books)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("library.db")
        conn.row_factory = sqlite3.Row  # Enable dictionary-like access
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM Users WHERE Name = ? AND Password = ?", (username, password)
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user_id"] = user["UserID"]
            session["user_name"] = user["Name"]
            return redirect(url_for("book_list"))
        else:
            flash("Invalid credentials, please try again.")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("user_name", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
