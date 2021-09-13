import logging
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname) s:%(message)s')
file_handler = logging.FileHandler('tickets.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def logTicket(ticket):
    dfmt = '%d-%m-%Y %H:%M:%S'

    order_id = ticket['order_id']
    ticket_id = ticket['ticket_id']
    reported_dt = datetime.strptime(ticket['reported'], dfmt)
    started_dt = datetime.strptime(ticket['started'], dfmt)
    finished_dt = datetime.strptime(ticket['finished'], dfmt)
    op_code = ticket['op_code']
    cost = ticket['cost']

    message = f"""Ticket Completed: {ticket_id} Order: {order_id} Reported: {reported_dt} Started: {started_dt} Finished: {finished_dt} OpCode: {op_code} Cost: {cost}"""
    logger.info(message)


tickets = [
    {"order_id": "101", "ticket_id": "T12112", "reported": "29-08-2021 13:45:33", "started": "01-09-2021 08:45:00", "finished": "01-09-2021 10:25:00", "op_code": "122", "cost": 22.32},
    {"order_id": "101", "ticket_id": "T12113", "reported": "02-09-2021 9:22:21", "started": "03-09-2021 11:29:00", "finished": "03-09-2021 14:45:00", "op_code": "122", "cost": 49.99}
]

for ticket in tickets:
    logTicket(ticket)

print('Done')