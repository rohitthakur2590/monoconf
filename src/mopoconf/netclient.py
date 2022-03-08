from ncclient import manager

device = manager.connect(host='10.10.10.10',
port=830,
username='admin',
password='admin',
hostkey_verify=False,
device_params={'name': 'cisco'}
)

for device_capability in device.server_capabilities:
    print(device_capability)

device.close_session()
