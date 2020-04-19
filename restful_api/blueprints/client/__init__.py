
# # __init__.py

# class Client():
#     def __init__(self):
#         self.reset()
    
#     def reset(self):
#         self.id = 0
#         self.client_key = None
#         self.client_secret = None
#         self.status = None

#     def serialize(self):
#         return {
#             'id': self.id,
#             'client_key': self.client_key,
#             'client_secret': self.client_secret,
#             'status': self.status
#         }

# class Clients():
#     clients = []

#     def __init__(self):
#         pass

#     def get_list(self):
#         return self.clients
    
#     def add(self, client):
#         self.clients.append(client.serialize())

#     def get_one(self, id):
#         for x, value in enumerate(self.clients):
#             if int(value['id']) == int(id):
#                 return value
#         return None
    
#     def edit_one(self, id, client_key, client_secret, status):
#         for x, value in enumerate(self.clients):
#             if int(value['id']) == int(id):
#                 client = Client()
#                 client.id = id
#                 client.client_key = client_key if client_key != None else value['client_key']
#                 client.client_secret = client_secret if client_secret != None else value['client_secret']
#                 client.status = status if status != None else value['status']
#                 self.clients[x] = client.serialize()
#                 return client
#         return None
    
#     def delete_one(self, id):
#         for x, value in enumerate(self.clients):
#             if int(value['id']) == int(id):
#                 self.clients.pop(x)
#                 return True
#         return None