import ipaddress
from fastapi import HTTPException
import nmap
from typing import Any, List, Dict
from core.host.service import HostService
from core.host.model import Port
from modules.port_scan.model import PortScanType

class PortScan:
    def __init__(self, host_service: HostService):
        self.nmap = nmap.PortScanner()
        self.host_service: HostService = host_service

    def scan_ports(self, target_ips: List[str],
                   scan_type: PortScanType) -> Dict[str, List[Port]]:
        ports_by_ip: Dict[str, List[Port]] = {}

        for ip in target_ips:
            try:
                ipaddress.ip_address(ip)
            except ValueError:
                raise HTTPException(status_code=400,
                                    detail=f"{ip} is not a valid IP address")

            open_ports = self.scan_ip(ip, scan_type)
            if open_ports:
                ports_by_ip[ip] = open_ports

        if ports_by_ip:
            self.host_service.update_ports(ports_by_ip, scan_type)

        return ports_by_ip

    def scan_ip(self, ip: str, scan_type: PortScanType) -> List[Port] | None:
        try:
            scan_result = self.nmap.scan(hosts=ip, arguments=scan_type.value)
        except nmap.PortScannerError as e:
            return None

        open_ports: List[Port] = []
        scan_data: Dict[str, Dict[str, Any]] = scan_result['scan'].get(ip, {})

        for protocol in ['tcp', 'udp']:
            protocol_scan = scan_data.get(protocol, {})
            for port, port_info in protocol_scan.items():
                if port_info.get('state') == 'open':
                    open_ports.append(Port(
                        port=int(port),
                        protocol=protocol,
                        state=port_info['state'],
                        name=port_info.get('name'),
                        product=port_info.get('product'),
                        extrainfo=port_info.get('extrainfo'),
                        reason=port_info.get('reason'),
                        version=port_info.get('version'),
                        conf=port_info.get('conf')
                    ))
        return open_ports