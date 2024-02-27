import json

from channels.generic.websocket import WebsocketConsumer


class MarketConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({'message_from_server': 'Hello!!!'}))

    def disconnect(self, close_code):
        pass

    def receive(text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        # message = text_data_json["message"]
        #
        # self.send(text_data=json.dumps({"message": message}))