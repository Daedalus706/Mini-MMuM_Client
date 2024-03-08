from client import Client

client = Client("10.147.18.135", 5010)
client.echo_message("test message")