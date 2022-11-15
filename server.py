"""Greeting Flask app."""

# from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
      <!doctype html>
      <html>
        <body>
          <p>Hi! Would you like an insult or a complement?</p>
          <form action="/hello">
            Insult<input type="radio" name="choice" value="insult">
            Compliment<input type="radio" name="choice" value="compliment">
            <input type="submit" value="Submit">
          </form>
        </body>
      </html>
      """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    choice = request.args.get('choice')
    if choice == 'compliment':
      return """
        <!doctype html>
        <html>
          <head>
            <title>Hi There!</title>
          </head>
          <body>
            <h1>Hi There!</h1>
            <form action="/greet">
              What's your name? <input type="text" name="person">
              <label for="compliment">Select a compliment</label>
              <select name="compliment">
                <option>awesome</option>
                <option>terrific</option>
                <option>fantastic</option>
                <option>neato</option>
                <option>fantabulous</option>
                <option>wowza</option>
                <option>oh-so-not-me</option>
                <option>brilliant</option>
                <option>ducky</option>
                <option>coolio</option>
                <option>incredible</option>
                <option>wonderful</option>
                <option>smashing</option>
                <option>lovely</option>
              </select>
              <input type="submit" value="Submit">
            </form>
        </body>
      </html>
      """
    elif choice == 'insult':
      return """
      <!doctype html>
      <html>
        <head>
          <title>Hi There!</title>
        </head>
        <body>
          <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <label for="diss">Select a diss</label>
          <select name="diss">
            <option>abomination</option>
            <option>animal</option>
            <option>lame</option>
            <option>tired</option>
            <option>crazy</option>
            <option>silly</option>
            <option>weird</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A diss</title>
      </head>
      <body>
        <p>Hi, {player}! I think you're {diss}!</p>
        <a href=/>Start Again!</a>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""


    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        <p>Hi, {player}! I think you're {compliment}!</p>
        <a href=/>Start Again!</a>
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
