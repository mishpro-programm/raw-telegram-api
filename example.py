from raw-telegram.api import APIClient
token = "<your token>"
api = APIClient(token)
api.send_method("sendMessage", {'chat_id': 5102762920, 'text': 'Hello world!'})
