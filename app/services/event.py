from enum import Enum
from models.host import Host

class EventType(Enum):
    HOST_NEW = "host.new"
    HOST_SEEN = "host.seen"
    HOST_CONNECTED = "host.connected"
    HOST_DISCONNECTED = "host.disconnected"
    SCAN_TCP = "scan.tcp"
    SCAN_SYN = "scan.syn"
    SCAN_UDP = "scan.udp"

class Event:
    def __init__(self, type: EventType, data: Host):
        self.type = type
        self.data = data

    def to_dict(self):
        return {
            "type": self.type.value,
            "data": self.data.model_dump()
        }