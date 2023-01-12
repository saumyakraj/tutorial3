from application import app
from flask import request, jsonify, Response, render_template
from application.model.models import db, Payments

@app.route('/')
def index():
    return "Hello World"


@app.route("/web_front")
def web():
    return render_template("index.html")
















@app.route('/add_payment', methods=["POST"])
def post():
    input_data = request.get_json()
    print(input_data)
    #checks

    payments = Payments(amount = input_data["amount"], status = input_data["status"], items = input_data["items"])
    db.session.add(payments)
    db.session.commit()

    data = {'SUCCESS': 'new payment added'}
    return jsonify(data)


@app.route('/view_payment', methods=["GET"])
def get():
    queryset = Payments.query.all()
    all_payments = []
    
    for x in queryset:
        y = {
            "orderid": x.orderid,
            "date": x.date,
            "amount": x.amount
        }
        all_payments.append(y)

    return all_payments, 200