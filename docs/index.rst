:tocdepth: 2

==============
First News App
==============

A step-by-step guide to publishing a simple news application.

This tutorial will walk you through the process of building an interactive data visualization
from a structured dataset. You will get hands-on experience in every stage of the
development process, writing Python, HTML and JavaScript while recording it in Git's
version control system. By the end you will have published your work on the World Wide Web.

******************
What you will make
******************

By the end of this lesson, you will publish an interactive database and map
of one week's worth of 911 calls reporting overdoses in Baltimore City from 2022.
You will do this with an improved version of the 911 call data that

A working example of what you'll make can be found at `https://newsappsumd.github.io/first-news-app-dwillis/build/index.html <https://newsappsumd.github.io/first-news-app-dwillis/build/index.html>`_

.. image:: /_static/hello-css-markers2.png

Past students of this tutorial have gone on to use the skills they learned to create projects like The Chicago Reporter's `police complaints database <http://projects.chicagoreporter.com/settlements/search/cases>`_, the `Naples Daily News' greyhound dogs death database <https://naplesnews-floridagreyhounds.com/build/index.html>`_ and the San Antonio Express-News' `homicide database <http://homicides.expressnews.com/>`_.

*****************
About the authors
*****************

This guide was originally prepared for training sessions of `Investigative Reporters and Editors (IRE) <https://www.ire.org/>`_
by `Ben Welsh <https://palewi.re/who-is-ben-welsh/>`_. It debuted in February 2014 `at NICAR's conference
in Baltimore <https://ire.org/events-and-training/event/973/1026/>`_. A revised version was presented at
`the 2015 conference <https://www.ire.org/conferences/nicar2015/hands-on-training/>`_ in Atlanta and the 2016 conference in
`Denver <https://www.ire.org/conferences/nicar2016/schedule/>`_. It was taught for the fourth time at `the 2017 conference in Jacksonville <https://www.ire.org/events-and-training/event/2702/2885/>`_ by Armand Emamdjomeh and Ben Welsh. This revised version was designed by Derek Willis for the News Applications class at the University of Maryland's Philip Merrill College of Journalism.

**********************
Prelude: Prerequisites
**********************

Before you can begin, your computer needs the following tools installed and working.

1. An account at `GitHub.com <https://www.github.com>`_
2. A browser. That's it! (We'll be using GitHub's Codespaces.)

***********************
Act 1: Hello Codespaces
***********************

Start at the `GitHub URL for this repository <https://github.com/NewsAppsUMD/first-news-app-umd>`_

Click the green "Use this template" button and choose "Open in a codespace". You should see something like this:

.. image:: /_static/codespaces.png

The browser is divided into three sections: on the left is a file explorer, listing all of the files in this repository. The top right shows whatever file you're currently viewing or editing, defaulting to README.md. The bottom right shows the terminal, where we'll run commands.

The codespace will be connected to your repository in the `the NewsApps organization on GitHub <https://github.com/NewsAppsUMD/>`_.

Open up the README by clicking on README.md on the left side and type something in it. Maybe change the heading like:

.. code-block:: markdown

    # My First Web News App

Make sure to save it. You'll see on the left that there's a yellow "M" next to README.md, meaning you've made some edits. Let's double-check that in the terminal:

.. code-block:: bash

    $ git status

You should see something like this:

.. image:: /_static/git_status.png

If so, we can add and commit it:

.. code-block:: bash

    $ git add README.md

Log its creation with Git's ``commit`` command. You can include a personalized message after the ``-m`` flag.

.. code-block:: bash

    $ git commit -m "First commit"

Now, finally, push your commit up to GitHub.

.. code-block:: bash

    $ git push origin main

Reload your repository on GitHub and see your handiwork.

******************
Act 2: Hello Flask
******************

Use pip on the command line to install `Flask <https://palletsprojects.com/p/flask/>`_, the Python "microframework" we'll use to put together our website.

.. code-block:: bash

    $ pip install Flask

Create a new file called ``app.py`` where we will configure Flask.

.. code-block:: bash

    # in the terminal:
    $ touch app.py

Open ``app.py`` with your code editor and import the Flask basics. This is the file that will serve as your
application's "backend," routing data to the appropriate pages.

.. code-block:: python

    from flask import Flask
    app = Flask(__name__)  # Note the double underscores on each side!

Next we will configure Flask to make a page at your site's root URL.

Configure Flask to boot up a test server when you run ``app.py`` like so:

.. code-block:: python
    :emphasize-lines: 4-6

    from flask import Flask
    app = Flask(__name__)

    if __name__ == '__main__':
        # Fire up the Flask test server
        app.run(debug=True, use_reloader=True)

.. note::

    You're probably asking, "What the heck is ``if __name__ == '__main__'``?" The short answer: It's just one of the weird things in Python you have to memorize. But it's worth the brain space because it allows you to run any Python script as a program.

    Anything indented inside that particular ``if`` clause is executed when the script is called from the command line. In this case, that means booting up your web site using Flask's built-in ``app.run`` function.

Don't forget to save your changes. Then run ``app.py`` on the command-line and open up your browser to `localhost:5000 <http://localhost:5000>`_

.. code-block:: bash

    $ python app.py

Here's what you should see. A website with nothing to show.

.. image:: /_static/hello-flask-404.png

Next we'll put a page there. Our goal is to publish the complete list of people who died during the riots using a template. We will call that template "index.html".

Before we do that, return to your command-line interface and stop your webserver by hitting the combination of ``CTRL-C``. You should now again at the standard command-line interface.

Now in ``app.py`` import ``render_template``, a Flask function we can use to combine data with HTML to make a webpage.

.. code-block:: python
    :emphasize-lines: 2

    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    if __name__ == '__main__':
        # Fire up the Flask test server
        app.run(debug=True, use_reloader=True)

Then create a function called ``index`` that returns our rendered ``index.html`` template.

.. code-block:: python
    :emphasize-lines: 5-8

    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        # Fire up the Flask test server
        app.run(debug=True, use_reloader=True)

Now use one of Flask's coolest tricks, the ``app.route`` decorator, to connect that function with the root URL of our site, ``/``.

.. code-block:: python
    :emphasize-lines: 5

    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        # Fire up the Flask test server
        app.run(debug=True, use_reloader=True)

Return to your command line and create a directory to store your templates in `the default location Flask expects <https://flask.palletsprojects.com/en/2.2.x/quickstart/#rendering-templates>`_.

.. code-block:: bash

    $ mkdir templates

Next create the ``index.html`` file we referenced in ``app.py``. This is the HTML file where your will lay out your webpage.

.. code-block:: bash

    $ touch templates/index.html

Open it up in your text editor and write something clever.

.. code-block:: html

    Hello World!

Now restart your Flask server.

.. code-block:: bash

    $ python app.py

Head back to your browser and visit your site again. You should see the contents of your template displayed on the page.

.. image:: /_static/hello-flask-hello-world.png

We're approaching the end of this act, so it's time to save your work by returning to the
command line and committing these changes to your Git repository.

.. note::

    To get the terminal back up, you will either need to quit out of ``app.py`` by hitting ``CTRL-C``, or open a second terminal and do additional work there. If you elect to open a second terminal, which is recommended, make sure to check into the virtualenv by repeating the ``. bin/activate`` part of :ref:`activate`. If you choose to quit out of ``app.py``, you will need to turn it back on later by calling ``python app.py`` where appropriate.

    As we progress through this lesson, you will need to continually do this to switch between the server and terminal. We no longer be instructing to do it each time from here on.

I bet you remember how from above. But here's a reminder.

.. code-block:: bash

    $ git add . # Using "." is a trick that will quickly stage *all* files you've changed.
    $ git commit -m "Flask app.py and first template"

Push it up to GitHub and check out the changes there.

.. code-block:: bash

    $ git push origin main

Congratulations, you've made a real web page with Flask. Now to put something useful in it.

*****************
Act 3: Hello HTML
*****************

Start over in your ``templates/index.html`` file with a bare-bones HTML document.

.. code-block:: html

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>One Week of Baltimore 911 Overdose Calls</h1>
        </body>
    </html>

Commit the changes to your repository, if only for practice.

.. code-block:: bash

    $ git add templates/index.html
    $ git commit -m "Real HTML"
    $ git push origin main

Make a directory to store our data file.

.. code-block:: bash

    $ mkdir static

Download `the comma-delimited file <https://raw.githubusercontent.com/NewsAppsUMD/first-news-app-umd/main/docs/_static/balt911.csv>`_ that will be the backbone of our application and save it there as ``balt911.csv``. Add it to your git repository.

.. code-block:: bash

    $ git add static
    $ git commit -m "Added CSV source data"
    $ git push origin main

Next we will open up ``app.py`` in your text editor and create a function that uses Python's ``csv`` module to access the data.

First, create the new function and give it the path to your CSV file.

.. code-block:: python
    :emphasize-lines: 1, 6-8

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/balt911.csv'

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Open up the file path for reading with Python using the built-in `open <https://docs.python.org/3/library/functions.html#open>`_ function.

.. code-block:: python
    :emphasize-lines: 8

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/balt911.csv'
        csv_file = open(csv_path, 'rb')

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Pass it into the csv module's `DictReader <https://docs.python.org/3/library/csv.html#csv.DictReader>`_, to be parsed and returned as a list of dictionaries.

.. code-block:: python
    :emphasize-lines: 9

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/balt911.csv'
        csv_file = open(csv_path, 'rb')
        csv_obj = csv.DictReader(csv_file)

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

.. note::

    Don't know what a dictionary is? That's okay. You can read more about them `here <https://learnpythonthehardway.org/book/ex39.html>`_ but the minimum you need to know now is that they are Python's way of handling each row in your CSV. The columns there, like ``callNumber`` or ``location``, are translated into "keys" on dictionary objects that you can access like ``row['id']``.

A quirk of CSV objects is that once they're used they disappear. There's a good reason related to efficiency and memory limitations and all that but we won't bother with that here. Just take our word and use Python's built-in ``list`` function to convert this one to a permanent list.

.. code-block:: python
    :emphasize-lines: 10

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/balt911.csv'
        csv_file = open(csv_path, 'rb')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Close the function by returning the csv list.

.. code-block:: python
    :emphasize-lines: 11

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/balt911.csv'
        csv_file = open(csv_path, 'rb')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Next have your ``index`` function pull the CSV data using your new code and pass it on the top the template, where it will be named ``object_list``.

.. code-block:: python
    :emphasize-lines: 16,17

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/balt911.csv'
        csv_file = open(csv_path, 'r')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list

    @app.route("/")
    def index():
        template = 'index.html'
        object_list = get_csv()
        return render_template(template, object_list=object_list)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Make sure to save ``app.py``. Then return to the ``index.html`` template. There you can dump out the ``object_list`` data using Flask's templating language `Jinja <https://jinja.palletsprojects.com/en/3.1.x/>`_.

.. code-block:: jinja
    :emphasize-lines: 6

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>One Week of Baltimore 911 Overdose Calls</h1>
            {{ object_list }}
        </body>
    </html>

If it isn't already running, return the command line, restart your test server and visit `localhost:5000 <http://localhost:5000>`_ again.

.. code-block:: bash

    $ python app.py

.. image:: /_static/hello-html-dump2.png

Now we'll use Jinja to sculpt the data in ``index.html`` to create `an HTML table <https://www.w3schools.com/html/html_tables.asp>`_ that lists all the names. Flask's templating language allows us to loop through the data list and print out a row for each record.

.. code-block:: jinja
    :emphasize-lines: 6-15

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>One Week of Baltimore 911 Overdose Calls</h1>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                </tr>
                {% for obj in object_list %}
                <tr>
                    <td>{{ obj.location }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
    </html>

Pause to reload your browser page.

.. image:: /_static/hello-html-names2.png

Next expand the table to include a lot more data.

.. code-block:: jinja
    :emphasize-lines: 9-14, 19-24

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>One Week of Baltimore 911 Overdose Calls</h1>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Call Number</th>
                    <th>Date</th>
                    <th>Time</th>
                    <th>Location</th>
                    <th>Neighborhood</th>
                </tr>
                {% for obj in object_list %}
                <tr>
                    <td>{{ obj.callNumber }}</td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.time }}</td>
                    <td>{{ obj.location }}</td>
                    <td>{{ obj.Neighborhood }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
    </html>

Reload your page in the browser again to see the change.

.. image:: /_static/hello-html-table2.png

Then commit your work.

.. code-block:: bash

    $ git add .
    $ git commit -m "Created basic table"
    $ git push origin main

Next we're going to create a unique "detail" page dedicated to each person. Start by returning to ``app.py`` in your text editor and adding the URL and template that will help make this happen.

.. code-block:: python
    :emphasize-lines: 19-23

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/balt911.csv'
        csv_file = open(csv_path, 'r')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list

    @app.route("/")
    def index():
        template = 'index.html'
        object_list = get_csv()
        return render_template(template, object_list=object_list)

    @app.route('/<call_number>/')
    def detail(call_number):
        template = 'detail.html'
        return render_template(template, call_number=call_number)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

.. note::

    Notice a key difference between the URL route for the index and the one we just added. This time, both the URL route and function accept an argument, named ``call_number``. Our goal is for the number passed into the URL to go into the function where it can be used to pull the record with the corresponding ``id`` from the CSV. Once we have our hands on it, we can pass it on to the template to render its unique page.

Create a new file in your templates directory called ``detail.html`` for it to connect with.

.. code-block:: bash

    # in the terminal:
    $ touch templates/detail.html

Put something simple in it with your text editor. We'll use the same templating language as above to print out the row id for each page.he

.. code-block:: html

    Hello {{ call_number }}!

Then, if it's not running, restart your test server and use your browser to visit `localhost:5000/P221761572/ <http://localhost:5000/P221761572/>`_.

.. code-block:: bash

    $ python app.py

.. image:: /_static/hello-html-hello-detail2.png

To customize the page for each person, we will need to connect the ``call_number`` in the URL with the ``callNumber`` column in the CSV data file.

First, return to ``app.py`` and pull the CSV data into the ``detail`` view.

.. code-block:: python
    :emphasize-lines: 22

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/balt911.csv'
        csv_file = open(csv_path, 'r')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list

    @app.route("/")
    def index():
        template = 'index.html'
        object_list = get_csv()
        return render_template(template, object_list=object_list)

    @app.route('/<call_number>/')
    def detail(call_number):
        template = 'detail.html'
        object_list = get_csv()
        return render_template(template, call_number=call_number)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Then have the ``detail`` function loop through the CSV data list, testing each row's ``callNumber`` field against the ``call_number`` provided by the URL. When you find a match, pass that row out to the template for rendering with the name ``object``.

.. code-block:: python
    :emphasize-lines: 23,24,25

    import csv
    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/balt911.csv'
        csv_file = open(csv_path, 'r')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list

    @app.route("/")
    def index():
        template = 'index.html'
        object_list = get_csv()
        return render_template(template, object_list=object_list)

    @app.route('/<call_number>/')
    def detail(call_number):
        template = 'detail.html'
        object_list = get_csv()
        for row in object_list:
            if row['callNumber'] == call_number:
                return render_template(template, object=row)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Now clear ``detail.html`` and make a new HTML document with a headline drawn from the data we've passed in from the dictionary.

.. code-block:: html

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>{{ object.location }}</h1>
        </body>
    </html>

Restart your test server and take a look at ``http://localhost:5000/P221761572/`` again.

.. code-block:: bash

    $ python app.py

.. image:: /_static/hello-html-hello-edmonson.png

Return to ``index.html`` and add a hyperlink to each detail page to the table.

.. code-block:: html
    :emphasize-lines: 18

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>One Week of Baltimore 911 Overdose Calls</h1>
            <table border=1 cellpadding=7>
            <tr>
                <th>Call Number</th>
                <th>Date</th>
                <th>Time</th>
                <th>Location</th>
                <th>Neighborhood</th>
            </tr>
            {% for obj in object_list %}
            <tr>
                <td><a href="{{ obj.callNumber }}/">{{ obj.callNumber }}</a></td>
                <td>{{ obj.date }}</td>
                <td>{{ obj.time }}</td>
                <td>{{ obj.location }}</td>
                <td>{{ obj.Neighborhood }}</td>
            </tr>
            {% endfor %}
            </table>
        </body>
    </html>

Restart your test server and take a look at ``http://localhost:5000/``.

.. code-block:: bash

    $ python app.py

.. image:: /_static/hello-html-hello-links2.png

In ``detail.html`` you can use the rest of the data fields to write a sentence about the victim.

.. code-block:: html
    :emphasize-lines: 5-10

    <!doctype html>
    <html lang="en">
        <head></head>
        <body>
            <h1>
                At {{ object.time }} on {{ object.date }}, a 911 call about an overdose was placed from near
                {{ object.location }} in the {{ object.Neighborhood }} neighborhood.
            </h1>
        </body>
    </html>

Reload `localhost:5000/P221761572/ <http://localhost:5000/P221761572/>`_ to see it.

.. image:: /_static/hello-html-hello-graf2.png

Then once again commit your work.

.. code-block:: bash

    $ git add .
    $ git commit -m "Created a detail page about each call."
    $ git push origin main

One last thing before we move on. What if somebody vists an URL for an ``id`` that doesn't exist, like `localhost:5000/99999/ <http://localhost:5000/99999/>`_? Right now Flask throws an ugly error.

.. image:: /_static/hello-html-error2.png

The polite thing to do is return what is called a `404 response code <https://en.wikipedia.org/wiki/HTTP_404>`_. To do that with Flask, you only need to import a function called ``abort`` and run it after our loop finishes without finding a match.

.. code-block:: python
    :emphasize-lines: 3,27

    import csv
    from flask import Flask
    from flask import abort
    from flask import render_template
    app = Flask(__name__)

    def get_csv():
        csv_path = './static/balt911.csv'
        csv_file = open(csv_path, 'r')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
        return csv_list

    @app.route("/")
    def index():
        template = 'index.html'
        object_list = get_csv()
        return render_template(template, object_list=object_list)

    @app.route('/<call_number>/')
    def detail(call_number):
        template = 'detail.html'
        object_list = get_csv()
        for row in object_list:
            if row['callNumber'] == call_number:
                return render_template(template, object=row)
        abort(404)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Reload your bad URL and you'll see the change.

.. image:: /_static/hello-html-404.png

***********************
Act 4: Hello JavaScript
***********************

Now we will use the `Leaflet <https://leafletjs.com/>`_ JavaScript library to create a map on each detail page showing where the victim died. Start by importing it in your page.

.. code-block:: html
    :emphasize-lines: 3-6

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"
        integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="
        crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js"
     integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM="
     crossorigin=""></script>
        </head>
        <body>
            <h1>
                At {{ object.time }} on {{ object.date }}, a 911 call about an overdose was placed from near
                {{ object.location }} in the {{ object.Neighborhood }} neighborhood.
            </h1>
        </body>
    </html>

Open up ``detail.html`` and make a map there, focus on just that victim.

.. code-block:: html
    :emphasize-lines: 8,14-23

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"
            integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="
            crossorigin=""/>
            <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js"
         integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM="
         crossorigin=""></script>
        </head>
        <body>
            <div id="map" style="width:100%; height:300px;"></div>
            <h1>
                At {{ object.time }} on {{ object.date }}, a 911 call about an overdose was placed from near
                {{ object.location }} in the {{ object.Neighborhood }} neighborhood.
            </h1>
            <script type="text/javascript">
                var map = L.map('map').setView([{{ object.lat }}, {{ object.lng }}], 16);
                L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
                attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
                }).addTo(map);
                var marker = L.marker([{{ object.lat }}, {{ object.lng }}]).addTo(map);
            </script>
        </body>
    </html>

Reload a detail page, like the one at `localhost:5000/P221761572/ <http://localhost:5000/P221761572/>`_.

.. image:: /_static/hello-js-detail-map2.png

Commit that.

.. code-block:: bash

    $ git add .
    $ git commit -m "Made a map on the detail page"
    $ git push origin main

Next we will work to make a map with every victim in ``index.html`` in one view.

Create an HTML element to hold the map and use Leaflet to boot it up and center on Los Angeles.

.. code-block:: html
    :emphasize-lines: 4-5,8,32-40

    <!doctype html>
    <html lang="en">
    <head>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"
        integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="
        crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js"
     integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM="
     crossorigin=""></script>
    </head>
    <body>
        <div id="map" style="width:100%; height:300px;"></div>
        <h1>Baltimore 911 Overdose Calls</h1>
        <table border=1 cellpadding=7>
            <tr>
                <th>Call Number</th>
                <th>Date</th>
                <th>Time</th>
                <th>Location</th>
                <th>Neighborhood</th>
            </tr>
            {% for obj in object_list %}
            <tr>
                <td><a href="{{ obj.callNumber }}/">{{ obj.callNumber }}</a></td>
                <td>{{ obj.date }}</td>
                <td>{{ obj.time }}</td>
                <td>{{ obj.location }}</td>
                <td>{{ obj.Neighborhood }}</td>
            </tr>
            {% endfor %}
        </table>
            <script type="text/javascript">
                var map = L.map('map').setView([39.3, -76.5], 11);
                var osmLayer = new L.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="https://www.openstreetmap.org/" target="_blank">OpenStreetMap</a>.'
                });
                map.addLayer(osmLayer);
            </script>
        </body>
    </html>

Reload the root URL of your site at `localhost:5000 <http://localhost:5000/>`_.

.. image:: /_static/hello-js-empty-map2.png

Loop through the CSV data and format it as a `GeoJSON <https://en.wikipedia.org/wiki/GeoJSON>`_ object, which Leaflet can easily load.

.. code-block:: html
    :emphasize-lines: 40-59

    <!doctype html>
    <!doctype html>
    <html lang="en">
    <head>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"
        integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="
        crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js"
     integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM="
     crossorigin=""></script>
    </head>
    <body>
        <div id="map" style="width:100%; height:300px;"></div>
        <h1>Baltimore 911 Overdose Calls</h1>
        <table border=1 cellpadding=7>
            <tr>
                <th>Call Number</th>
                <th>Date</th>
                <th>Time</th>
                <th>Location</th>
                <th>Neighborhood</th>
            </tr>
            {% for obj in object_list %}
            <tr>
                <td><a href="{{ obj.callNumber }}/">{{ obj.callNumber }}</a></td>
                <td>{{ obj.date }}</td>
                <td>{{ obj.time }}</td>
                <td>{{ obj.location }}</td>
                <td>{{ obj.Neighborhood }}</td>
            </tr>
            {% endfor %}
        </table>
            <script type="text/javascript">
                var map = L.map('map').setView([39.3, -76.5], 11);
                var osmLayer = new L.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="https://www.openstreetmap.org/" target="_blank">OpenStreetMap</a>.'
                });
                map.addLayer(osmLayer);
                var data = [
                {% for obj in object_list %}
                {
                  "type": "Feature",
                  "properties": {
                    "full_name": "{{ obj.location }}",
                    "id": "{{ obj.callNumber }}",
                    "popupContent": "{{ obj.incidentLocation }}",
                    "show_on_map": true
                  },
                  "geometry": {
                    "type": "Point",
                    "coordinates": [{{ obj.lng }}, {{ obj.lat }}]
                  }
                }{% if not loop.last %},{% endif %}
                {% endfor %}
              ];
                var dataLayer = L.geoJson(data);
                map.addLayer(dataLayer);
            </script>
        </body>
    </html>

Reload the page.

.. image:: /_static/hello-js-pins2.png

Add a popup on the map pins that shows the name of the victim.

.. code-block:: html
    :emphasize-lines: 58-62

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.3/dist/leaflet.css" />
            <script src="https://unpkg.com/leaflet@1.0.3/dist/leaflet.js"></script>
        </head>
        <body>
            <div id="map" style="width:100%; height:300px;"></div>
            <h1>One Week of Baltimore 911 Overdose Calls</h1>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Address</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Race</th>
                </tr>
            {% for obj in object_list %}
                <tr>
                    <td><a href="{{ obj.id }}/">{{ obj.full_name }}</a></td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.type }}</td>
                    <td>{{ obj.address }}</td>
                    <td>{{ obj.age }}</td>
                    <td>{{ obj.gender }}</td>
                    <td>{{ obj.race }}</td>
                </tr>
            {% endfor %}
            </table>
            <script type="text/javascript">
                var map = L.map('map').setView([34.055, -118.35], 9);
                var osmLayer = new L.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="https://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.'
                });
                map.addLayer(osmLayer);
                var data = {
                  "type": "FeatureCollection",
                  "features": [
                    {% for obj in object_list %}
                    {
                      "type": "Feature",
                      "properties": {
                        "full_name": "{{ obj.full_name }}",
                        "id": "{{ obj.id }}"
                      },
                      "geometry": {
                        "type": "Point",
                        "coordinates": [{{ obj.x }}, {{ obj.y }}]
                      }
                    }{% if not loop.last %},{% endif %}
                    {% endfor %}
                  ]
                };
                var dataLayer = L.geoJson(data, {
                    onEachFeature: function(feature, layer) {
                        layer.bindPopup(feature.properties.full_name);
                    }
                });
                map.addLayer(dataLayer);
            </script>
        </body>
    </html>

Reload the page and click a pin.

.. image:: /_static/hello-js-popup.png

Now wrap the name in a hyperlink to that person's detail page.

.. code-block:: html
    :emphasize-lines: 58-66

    <!doctype html>
    <html lang="en">
    <head>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css" integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI=" crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js" integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM=" crossorigin=""></script>
    </head>
    <body>
        <div id="map" style="width:100%; height:300px;"></div>
        <h1>Baltimore 911 Overdose Calls</h1>
        <table border=1 cellpadding=7>
            <tr>
                <th>Call Number</th>
                <th>Date</th>
                <th>Time</th>
                <th>Location</th>
                <th>Neighborhood</th>
            </tr>
            {% for obj in object_list %}
            <tr>
                <td><a href="{{ obj.callNumber }}/">{{ obj.callNumber }}</a></td>
                <td>{{ obj.date }}</td>
                <td>{{ obj.time }}</td>
                <td>{{ obj.location }}</td>
                <td>{{ obj.Neighborhood }}</td>
            </tr>
            {% endfor %}
        </table>
        <script type="text/javascript">
            var map = L.map('map').setView([39.3, -76.5], 11);
            var osmLayer = new L.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 18,
                attribution: 'Data, imagery and map information provided by <a href="https://www.openstreetmap.org/" target="_blank">OpenStreetMap</a>.'
            });
            map.addLayer(osmLayer);
            function onEachFeature(feature, layer) {
                // does this feature have a property named popupContent?
                if (feature.properties && feature.properties.popupContent) {
                    layer.bindPopup('<a href="'+ feature.properties.id + '/">' + feature.properties.popupContent + '</a>');
                }
            }
            var data = [
                {% for obj in object_list %}
                {
                  "type": "Feature",
                  "properties": {
                    "full_name": "{{ obj.location }}",
                    "id": "{{ obj.callNumber }}",
                    "popupContent": "{{ obj.incidentLocation }}",
                    "show_on_map": true
                  },
                  "geometry": {
                    "type": "Point",
                    "coordinates": [{{ obj.lng }}, {{ obj.lat }}]
                  }
                }{% if not loop.last %},{% endif %}
                {% endfor %}
              ];
            L.geoJSON(data, {
                onEachFeature: onEachFeature
            }).addTo(map);
            </script>
        </body>
    </html>

Reload again and click a pin.

.. image:: /_static/hello-js-pin-link2.png

Commit your map.

.. code-block:: bash

    $ git add .
    $ git commit -m "Made a map on the index page"
    $ git push origin main


*********************
Act 5: Hello Internet
*********************

In this final act, we will publish your application to the Internet using `Frozen Flask <https://pythonhosted.org/Frozen-Flask/>`_, a Python library that saves every page you've made with Flask as a flat file that can be uploaded to the web. This is an alternative publishing method that does not require you configure and host an full-fledged Internet server.

First, use pip to install Frozen Flask from the command line.

.. code-block:: bash

    $ pip install Frozen-Flask

Create a new file called ``freeze.py`` where we will configure which pages it should convert into flat files.

.. code-block:: bash

    # in the terminal:
    $ touch freeze.py

Use your text editor to write a basic Frozen Flask configuration.

.. code-block:: python

    from flask_frozen import Freezer
    from app import app
    freezer = Freezer(app)

    if __name__ == '__main__':
        freezer.freeze()

Now run it from the command line, which will create a new directory called ``build`` filled with a set of flattened files.

.. code-block:: bash

    $ python freeze.py

Use your browser to open up one of the local files in ``build``, rather that visit the dynamically generated pages we created at ``localhost``.

You will notice that the default Frozen Flask configuration only flattened out ``index.html``, and not all your detail pages our template could generate using the data file.

To flatten those, again edit ``freeze.py`` to give it the instructions it needs to make a page for every record in the source CSV.

.. code-block:: python
    :emphasize-lines: 2,5-8

    from flask_frozen import Freezer
    from app import app, get_csv
    freezer = Freezer(app)

    @freezer.register_generator
    def detail():
        for row in get_csv():
            yield {'call_number': row['callNumber']}

    if __name__ == '__main__':
        freezer.freeze()

Run it again from the command line and notice all the additional pages it made in the ``build`` directory. Try opening one in your browser.

.. code-block:: bash

    $ python freeze.py

Commit all of the flat pages to the repository.

.. code-block:: bash

    $ git add .
    $ git commit -m "Froze my app"
    $ git push origin main

Finally, we will publish these static files to the web using `GitHub's Pages <https://pages.github.com/>`_ feature. All it requires is that we create a new branch in our repository called ``gh-pages`` and push our files up to GitHub there.

.. code-block:: bash

    $ git checkout -b gh-pages # Create the new branch
    $ git merge main # Pull in all the code from the master branch
    $ git push origin gh-pages # Push up to GitHub from your new branch

Now wait a minute or two, then visit ``https://newsappsumd.github.io/first-news-app-<yourusername>/build/index.html`` to cross the finish line.

.. image:: /_static/hello-internet2.png

.. note::

    If your page does not appear, make sure that you have verified your email address with GitHub. It is required before the site will allow publishing pages. And keep in mind there are many other options for publishing flat files, like `Amazon's S3 service <https://en.wikipedia.org/wiki/Amazon_S3>`_.

So you've built a site. But it's kind of janky looking. The next chapter will show you how to dress it up to look like the `demonstration site <http://ireapps.github.io/first-news-app/build/index.html>`_.

*******************
Epilogue: Hello CSS
*******************

Before you get started, move back to the master branch of your repository.

.. code-block:: bash

    $ git checkout master

The first step is to create a stylesheet in the static directory where `CSS <https://en.wikipedia.org/wiki/Cascading_Style_Sheets>`_
code that controls the design of the page can be stored.

.. code-block:: bash

    # in the terminal:
    $ touch static/style.css

Add the style tag to the top of ``index.html`` so it imported on the page. Flask's built-in ``url_for``
method will create the URL for us.

.. code-block:: html
    :emphasize-lines: 4

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css" integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI=" crossorigin=""/>
            <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js" integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM=" crossorigin=""></script>
        </head>
        <body>
            <div id="map" style="width:100%; height:300px;"></div>
            <h1>Baltimore 911 Overdose Calls</h1>
            <table border=1 cellpadding=7>
                <tr>
                    <th>Call Number</th>
                    <th>Date</th>
                    <th>Time</th>
                    <th>Location</th>
                    <th>Neighborhood</th>
                </tr>
                {% for obj in object_list %}
                <tr>
                    <td><a href="{{ obj.callNumber }}/">{{ obj.callNumber }}</a></td>
                    <td>{{ obj.date }}</td>
                    <td>{{ obj.time }}</td>
                    <td>{{ obj.location }}</td>
                    <td>{{ obj.Neighborhood }}</td>
                </tr>
                {% endfor %}
            </table>
            <script type="text/javascript">
                var map = L.map('map').setView([39.3, -76.5], 11);
                var osmLayer = new L.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="https://www.openstreetmap.org/" target="_blank">OpenStreetMap</a>.'
                });
                map.addLayer(osmLayer);
                function onEachFeature(feature, layer) {
                    // does this feature have a property named popupContent?
                    if (feature.properties && feature.properties.popupContent) {
                        layer.bindPopup('<a href="'+ feature.properties.id + '/">' + feature.properties.popupContent + '</a>');
                    }
                }
                var data = [
                    {% for obj in object_list %}
                    {
                      "type": "Feature",
                      "properties": {
                        "full_name": "{{ obj.location }}",
                        "id": "{{ obj.callNumber }}",
                        "popupContent": "{{ obj.incidentLocation }}",
                        "show_on_map": true
                      },
                      "geometry": {
                        "type": "Point",
                        "coordinates": [{{ obj.lng }}, {{ obj.lat }}]
                      }
                    }{% if not loop.last %},{% endif %}
                    {% endfor %}
                  ];
                L.geoJSON(data, {
                    onEachFeature: onEachFeature
                }).addTo(map);
            </script>
        </body>
    </html>


Before we start styling the page, let's do a little reorganization of the HTML
to make a little more like a news site.

First, download this `UMD logo <https://raw.githubusercontent.com/NewsAppsUMD/first-news-app-umd/master/static/shell.png>`_
and throw in the ``static`` directory. We'll add that as an image in a new
navigation bar at the top of the site, then zip up the headline and move it above the map with
with a new byline.

.. code-block:: html
    :emphasize-lines: 9-19

    <!doctype html>
    <html lang="en">
    <head>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"
        integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="
        crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js"
     integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM="
     crossorigin=""></script>
    </head>
    <body>
        <nav>
            <a href="https://first-news-app-umd.readthedocs.org/">
                <img src="{{ url_for('static', filename='shell.png') }}">
            </a>
        </nav>
        <header>
            <h1>One Week of Baltimore 911 Overdose Calls</h1>
                <div class="byline">
                    By <a href="https://first-news-app-umd.readthedocs.org/">The First News App Tutorial</a>
                </div>
            </header>
        <div id="map" style="width:100%; height:300px;"></div>
        <table border=1 cellpadding=7>
            <tr>
                <th>Call Number</th>
                <th>Date</th>
                <th>Time</th>
                <th>Location</th>
                <th>Neighborhood</th>
            </tr>
            {% for obj in object_list %}
            <tr>
                <td><a href="{{ obj.callNumber }}/">{{ obj.callNumber }}</a></td>
                <td>{{ obj.date }}</td>
                <td>{{ obj.time }}</td>
                <td>{{ obj.location }}</td>
                <td>{{ obj.Neighborhood }}</td>
            </tr>
            {% endfor %}
        </table>
        <script type="text/javascript">
            var map = L.map('map').setView([39.3, -76.5], 11);
            var osmLayer = new L.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 18,
                attribution: 'Data, imagery and map information provided by <a href="https://www.openstreetmap.org/" target="_blank">OpenStreetMap</a>.'
            });
            map.addLayer(osmLayer);
            function onEachFeature(feature, layer) {
                // does this feature have a property named popupContent?
                if (feature.properties && feature.properties.popupContent) {
                    layer.bindPopup('<a href="'+ feature.properties.id + '/">' + feature.properties.popupContent + '</a>');
                }
            }
            var data = [
                {% for obj in object_list %}
                {
                  "type": "Feature",
                  "properties": {
                    "full_name": "{{ obj.location }}",
                    "id": "{{ obj.callNumber }}",
                    "popupContent": "{{ obj.incidentLocation }}",
                    "show_on_map": true
                  },
                  "geometry": {
                    "type": "Point",
                    "coordinates": [{{ obj.lng }}, {{ obj.lat }}]
                  }
                }{% if not loop.last %},{% endif %}
                {% endfor %}
              ];
            L.geoJSON(data, {
                onEachFeature: onEachFeature
            }).addTo(map);
            </script>
        </body>
    </html>

Now go into ``style.css`` and toss in some style we've prepared that will
draw in a dark top bar, limit the width of the page and tighten up the rest
of the page.

.. code-block:: css

    body {
        margin: 0 auto;
        padding: 0;
        font-family: Verdana, sans-serif;
        background-color: ##F2EFEC;
        max-width: 1200px;
    }
    nav {
        background-color: #333132;
        width: 100%;
        height: 50px;
    }
    nav img {
        height: 34px;
        padding: 8px;
    }
    header {
        margin: 25px 10px 15px 10px;
        font-family: Times, Times New Roman, serif;
    }
    h1 {
        margin: 0;
        padding: 0;
        font-size: 44px;
        line-height: 50px;
        font-weight: bold;
        font-style: italic;
    	text-shadow: 0.3px 0.3px 0px gray;
        letter-spacing: .01em;
    }
    .byline {
        margin: 6px 0 0 0;
        font-size: 13px;
        font-weight: bold;
    }
    .byline a {
        text-transform: uppercase;
    }
    table {
        border-collapse:collapse;
        margin: 0 0 20px 0;
        border-width: 0;
        width: 100%;
        font-size: 14px;
    }
    th {
        text-align:left;
    }
    tr, td, th {
        border-color: #f2f2f2;
    }
    tr:hover {
        background-color: #f3f3f3;
    }
    p {
        line-height:140%;
    }
    a {
        color: #4591B8;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }

Reload the page and you should see something a little more presentable.

.. image:: /_static/hello-css-desktop2.png

The next step is to upgrade the styles to reshape the page on smaller devices
like tablets and phones. This is done using a system known as `responsive design <https://en.wikipedia.org/wiki/Responsive_web_design>`_
and `CSS media queries <https://en.wikipedia.org/wiki/Media_queries>`_ that set different style rules at different device sizes.

First the HTML page needs an extra tag to turn the system on.

.. code-block:: html
    :emphasize-lines: 4

    <!doctype html>
    <html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css" integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI=" crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js" integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM=" crossorigin=""></script>
    </head>
    <body>
        <nav>
            <a href="https://first-news-app-umd.readthedocs.org/">
                <img src="{{ url_for('static', filename='shell.png') }}">
            </a>
        </nav>
        <header>
            <h1>One Week of Baltimore 911 Overdose Calls</h1>
                <div class="byline">
                    By <a href="https://first-news-app-umd.readthedocs.org/">The First News App Tutorial</a>
                </div>
            </header>
        <div id="map" style="width:100%; height:300px;"></div>
        <table border=1 cellpadding=7>
            <tr>
                <th>Call Number</th>
                <th>Date</th>
                <th>Time</th>
                <th>Location</th>
                <th>Neighborhood</th>
            </tr>
            {% for obj in object_list %}
            <tr>
                <td><a href="{{ obj.callNumber }}/">{{ obj.callNumber }}</a></td>
                <td>{{ obj.date }}</td>
                <td>{{ obj.time }}</td>
                <td>{{ obj.location }}</td>
                <td>{{ obj.Neighborhood }}</td>
            </tr>
            {% endfor %}
        </table>
        <script type="text/javascript">
            var map = L.map('map').setView([39.3, -76.5], 11);
            var osmLayer = new L.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 18,
                attribution: 'Data, imagery and map information provided by <a href="https://www.openstreetmap.org/" target="_blank">OpenStreetMap</a>.'
            });
            map.addLayer(osmLayer);
            function onEachFeature(feature, layer) {
                // does this feature have a property named popupContent?
                if (feature.properties && feature.properties.popupContent) {
                    layer.bindPopup('<a href="'+ feature.properties.id + '/">' + feature.properties.popupContent + '</a>');
                }
            }
            var data = [
                {% for obj in object_list %}
                {
                  "type": "Feature",
                  "properties": {
                    "full_name": "{{ obj.location }}",
                    "id": "{{ obj.callNumber }}",
                    "popupContent": "{{ obj.incidentLocation }}",
                    "show_on_map": true
                  },
                  "geometry": {
                    "type": "Point",
                    "coordinates": [{{ obj.lng }}, {{ obj.lat }}]
                  }
                }{% if not loop.last %},{% endif %}
                {% endfor %}
              ];
            L.geoJSON(data, {
                onEachFeature: onEachFeature
            }).addTo(map);
            </script>
        </body>
    </html>

Now the ``style.css`` file should be expanded to include media queries
that will drop columns from the table on smaller devices.

.. code-block:: css
    :emphasize-lines: 64-79

    body {
        margin: 0 auto;
        padding: 0;
        font-family: Verdana, sans-serif;
        background-color: ##F2EFEC;
        max-width: 1200px;
    }
    nav {
        background-color: #333132;
        width: 100%;
        height: 50px;
    }
    nav img {
        height: 34px;
        padding: 8px;
    }
    header {
        margin: 25px 10px 15px 10px;
        font-family: Times, Times New Roman, serif;
    }
    h1 {
        margin: 0;
        padding: 0;
        font-size: 44px;
        line-height: 50px;
        font-weight: bold;
        font-style: italic;
    	text-shadow: 0.3px 0.3px 0px gray;
        letter-spacing: .01em;
    }
    .byline {
        margin: 6px 0 0 0;
        font-size: 13px;
        font-weight: bold;
    }
    .byline a {
        text-transform: uppercase;
    }
    table {
        border-collapse:collapse;
        margin: 0 0 20px 0;
        border-width: 0;
        width: 100%;
        font-size: 14px;
    }
    th {
        text-align:left;
    }
    tr, td, th {
        border-color: #f2f2f2;
    }
    tr:hover {
        background-color: #f3f3f3;
    }
    p {
        line-height:140%;
    }
    a {
        color: #4591B8;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    @media (max-width: 979px) {
        tr th:nth-of-type(n+3),
        tr td:nth-of-type(n+3) {
            display:none;
        }
    }
    @media (max-width: 420px) {
        tr th:nth-of-type(n+2),
        tr td:nth-of-type(n+2) {
            display:none;
        }
    }

Reload the page and size down your browser to see how the page should appear
when visited by a mobile phone.

.. image:: /_static/hello-css-mobile2.png

We can punch up the map markers by replacing the Leaflet default pins with custom
designs from the `Mapbox's open-source Maki set <https://www.mapbox.com/maki/>`_.

Download `these <https://github.com/NewsAppsUMD/first-news-app-umd/blob/master/static/marker-24.png>`_ `two <https://github.com/NewsAppsUMD/first-news-app-umd/blob/master/static/marker-24%402x.png>`_
black pin images and add them to your ``static`` directory.

Now expand our Leaflet JavaScript code to substitute these images for the defaults.

.. code-block:: html
    :emphasize-lines: 70-75,77-79

    <!doctype html>
    <html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css" integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI=" crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js" integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM=" crossorigin=""></script>
    </head>
    <body>
        <nav>
            <a href="https://first-news-app-umd.readthedocs.org/">
                <img src="{{ url_for('static', filename='shell.png') }}">
            </a>
        </nav>
        <header>
            <h1>One Week of Baltimore 911 Overdose Calls</h1>
                <div class="byline">
                    By <a href="https://first-news-app-umd.readthedocs.org/">The First News App Tutorial</a>
                </div>
            </header>
        <div id="map" style="width:100%; height:300px;"></div>
        <table border=1 cellpadding=7>
            <tr>
                <th>Call Number</th>
                <th>Date</th>
                <th>Time</th>
                <th>Location</th>
                <th>Neighborhood</th>
            </tr>
            {% for obj in object_list %}
            <tr>
                <td><a href="{{ obj.callNumber }}/">{{ obj.callNumber }}</a></td>
                <td>{{ obj.date }}</td>
                <td>{{ obj.time }}</td>
                <td>{{ obj.location }}</td>
                <td>{{ obj.Neighborhood }}</td>
            </tr>
            {% endfor %}
        </table>
        <script type="text/javascript">
            var map = L.map('map').setView([39.3, -76.5], 11);
            var osmLayer = new L.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 18,
                attribution: 'Data, imagery and map information provided by <a href="https://www.openstreetmap.org/" target="_blank">OpenStreetMap</a>.'
            });
            map.addLayer(osmLayer);
            function onEachFeature(feature, layer) {
                // does this feature have a property named popupContent?
                if (feature.properties && feature.properties.popupContent) {
                    layer.bindPopup('<a href="'+ feature.properties.id + '/">' + feature.properties.popupContent + '</a>');
                }
            }
            var data = [
                {% for obj in object_list %}
                {
                  "type": "Feature",
                  "properties": {
                    "full_name": "{{ obj.location }}",
                    "id": "{{ obj.callNumber }}",
                    "popupContent": "{{ obj.incidentLocation }}",
                    "show_on_map": true
                  },
                  "geometry": {
                    "type": "Point",
                    "coordinates": [{{ obj.lng }}, {{ obj.lat }}]
                  }
                }{% if not loop.last %},{% endif %}
                {% endfor %}
              ];
                var blackIcon = L.Icon.extend({
                    options: {
                        iconUrl: "{{ url_for('static', filename='marker-24.png') }}",
                        iconSize: [24, 24]
                    }
                });
                L.geoJSON(data, {
                    pointToLayer: function (feature, latlng) {
                        return L.marker(latlng, {icon: new blackIcon()});
                    },
                    onEachFeature: onEachFeature
                }).addTo(map);
            </script>
        </body>
    </html>

That will restyle the map to look like this.

.. image:: /_static/hello-css-markers2.png

Extending this new design to detail page is simply a matter of repeating the steps above.

.. code-block:: html
    :emphasize-lines: 4-5,10-18,28-34

    <!doctype html>
    <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/leaflet.js"></script>
        </head>
        <body>
            <nav>
                <a href="https://first-news-app-umd.readthedocs.org/">
                    <img src="{{ url_for('static', filename='shell.png') }}">
                </a>
            </nav>
            <header>
                <h1>
                    At {{ object.time }} on {{ object.date }}, a 911 call about an overdose was placed from near
                    {{ object.location }} in the {{ object.Neighborhood }} neighborhood.
                </h1>
            </header>
            <div id="map" style="width:100%; height:300px;"></div>
            <script type="text/javascript">
                var map = L.map('map').setView([{{ object.lat }}, {{ object.lng }}], 16);
                var osmLayer = new L.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: 'Data, imagery and map information provided by <a href="https://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.'
                });
                map.addLayer(osmLayer);
                var blackIcon = L.Icon.extend({
                    options: {
                        iconUrl: "{{ url_for('static', filename='marker-24.png') }}",
                        iconSize: [24, 24]
                    }
                });
                var marker = L.marker([{{ object.lat }}, {{ object.lng }}], {icon: new blackIcon()}).addTo(map);
            </script>
        </body>
    </html>

That should shape up the page like this.

.. image:: /_static/hello-css-detail.png

Now it is time to build out all the pages by running the freeze script that will save all of
the pages again. Before you do that, though, we have one change to make to our app.py file to ensure that
the published version picks up our static files correctly. Add one line to your file:

.. code-block:: python
    :emphasize-lines: 6

    import csv
    from flask import Flask
    from flask import abort
    from flask import render_template
    app = Flask(__name__)
    app.config['FREEZER_RELATIVE_URLS'] = True

Then re-run the freeze.py script to save all of the pages again.

.. code-block:: bash

    $ python freeze.py

Commit all of the flat pages to the repository.

.. code-block:: bash

    $ git add .
    $ git commit -m "Froze my restyled app"
    $ git push origin main

Republish your work by going back to the ``gh-pages`` branch and pushing up the code.

.. code-block:: bash

    $ git checkout gh-pages
    $ git merge main
    $ git push origin gh-pages

Now wait a minute or two, then visit ``https://newsappsumd.github.io/first-news-app-<yourusername>-umd/build/index.html`` to see
the restyled application.
