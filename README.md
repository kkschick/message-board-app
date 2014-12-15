jQuery/AJAX Message Board
=========================

####The Project

This is a live message board application where people can post and read messages to one another. It has a textbox on the left where you can enter a message to send to the server, and an area on the right that lists all of the messages received.

This application is a single-page application, built using Python-Flask, HTML/CSS, Twitter Bootstrap, JavaScript, jQuery, and AJAX.

![Message board](/static/screenshots/message_wall.png)

The application will validate messages as they are posted.

![Message success](/static/screenshots/message_success.png)

![Message fail](/static/screenshots/message_fail.png)

####Try It Yourself!

#####Environment 

1) Clone the repository:

<pre><code>$ git clone https://github.com/kkschick/MessageBoardApp.git</code></pre>

2) Create and activate a virtual environment in the same directory: 

<pre><code>$ pip install virtualenv
$ virtualenv env
$ . env/bin/activate 
</code></pre>

3) Install the required packages using pip:

<pre><code>(env)$ pip install -r requirements.txt
</code></pre>

4) Run the app: 

<pre><code>(env)$ python wall.py
</code></pre>

5) Point your browser to:

<pre><code>http://localhost:5000/</code></pre>
