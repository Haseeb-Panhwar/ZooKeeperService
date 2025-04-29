from kazoo.client import KazooClient
import socket
import uuid

# Connect to ZooKeeper
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

# Unique service identifier (e.g., hostname + uuid)
hostname = socket.gethostname()
service_id = f"{hostname}-{uuid.uuid4()}"
path = f"/services/{service_id}"

# Register as ephemeral node (auto-deleted if disconnected)
zk.create(path, b"online", ephemeral=True)

print(f"Registered service: {service_id}")
input("Press Enter to exit and unregister...")

zk.stop()
