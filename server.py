# Import Flask functions and csv module.
from flask import Flask, render_template, request, redirect
import csv

# Initialize new Flask app.
app = Flask(__name__)


# Append a contact form submission to CSV "database" file.
def write_to_csv(data):
    # Use "append" mode for writing to CSV file.
    with open('database.csv', newline='', mode='a') as database2:
        # Extract form data from dictionary provided.
        email = data['email']
        subject = data['subject']
        message = data['message']

        # Configure new CSV writer; specify file to write to, set standard CSV options.
        # Only quote values containing special characters.
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Write a row to the CSV, passing in data as a list.
        csv_writer.writerow([email, subject, message])


# Static route handlers for the homepage.
@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/index.html')
def my_home_html():
    return render_template('index.html')


# Dynamic route for other *.html pages on this site (such as /about.html).
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# Endpoint route for contact form (at /contact.html) to submit to.
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # Only allow form data to be POST-ed to this endpoint.
    if request.method == 'POST':
        try:
            # Convert form data into a dictionary.
            data = request.form.to_dict()
            # Append data from contact form submission to CSV database file.
            write_to_csv(data)
            # Redirect to page confirming the form submission.
            return redirect('/thankyou.html')
        # @todo This except clause is too broad; modify to handle specific error types.
        except:
            return 'There was an issue processing your form submission - please try again.'
    else:
        return 'Your form data was not received as expected - please try again.'
