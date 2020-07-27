import flask
from flask import Flask, request, session, url_for

from db.models import User

app = Flask(__name__)

### Routes Interface

@app.route('/invoices/<string:credit_card_name>')
def get_invoices_by_credit_card_name(credit_card_name):
    """
    @login_required
    """
    pass

@app.route('/credit_card/<string:credit_card_name>/invoice/<int:month>')
def get_invoice_by_month(credit_card_name, month):
    """
    @login_required
    """
    pass

# get all services by credit_card_name
@app.route('/services/<string:credit_card_name>')
def get_services_by_credit_card_name(credit_card_name):
    """
    @login_required
    """
    pass


@app.route('/credit_card/<string:credit_card_name>/service/<string:name>')
def get_service_by_name(credit_card_name, name):
    """
    @login_required
    """
    pass

# get all credit_cards by user pid
@app.route('/credit_cards/<int:user_pid>')
def get_credit_cards_by_user(user_pid):
    """
    Return a list of credit cards from a specific user
    @login_required
    """
    pass

# get credit_card by name
@app.route('/credit_card/<string:name>')
def get_credit_card_by_name(name):
    """
    @login_required
    """
    pass

# get user by pid
@app.route('/user/<int:pid>')
def get_user_by_code(email):
    """
    Get a specific user by a given pid (associated to user email adress)
    """
    pass


# create/remove/update credit_card
# create/remove/update service
# create/remove/update invoice
# create/remove/update user
@app.route('/create/user', methods=['POST'])
def create_user():
    """
    Endpoint to create an user tuple in the database
    User has name (string), email (string) and income (float) attributes 
    """
    data = request.json
    if not all(map(lambda x: x in data.keys(), ["name", "email", "income"])):
        return flask.Response("Body attributes not satisfied! Need name, email and income attributes", status=400)
    try:
        user = User(
            data["name"],
            data["email"],
            data["income"]
        )
        user.save()
    except:
        return flask.Response("User already exist!", status=409)
    return flask.Response("User created!", status=200)


############################################################
@app.route('/create', methods=['POST'])
def create():
    data = request.json
    name = data['name']
    email = data['email']
    income = data['income']
    print(name, email, income)
    return flask.Response(status=200)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        print(request.json) # body
        print(request.headers['email']) # headers
    return 'Hello, World!'