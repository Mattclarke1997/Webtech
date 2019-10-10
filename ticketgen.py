from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def random_ticket():
    items = ['Orange Ticket','Green Ticket','Pink Ticket','Black Ticket','Golden Ticket']
    ticket = random.choice(items)
    if ticket == 'Golden Ticket':
        return('You have the GOLDEN TICKET')
    else:
        return('Keep trying!')
        return app