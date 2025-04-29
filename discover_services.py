from kazoo.client import KazooClient
from kazoo.exceptions import NoNodeError

# Connect to ZooKeeper
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

print("\nDiscovering active services...\n")

try:
    # List all service nodes under /services
    if zk.exists("/services"):
        children = zk.get_children("/services")
        if children:
            for service in children:
                print(f"Active Service: {service}")
        else:
            print("No services currently registered.")
    else:
        print("Node /services does not exist.")
except NoNodeError:
    print("ZooKeeper node /services not found.")

zk.stop()
