import geckoboard
client = geckoboard.client("4c47776ffc1f8825f91e5f2a85d78ba3")


dataset = client.datasets.find_or_create('geckoboard2', {'amount': {'type': 'number', 'name': 'Amount', 'optional': False}})
dataset.post([
    {'amount': 1337} ])
