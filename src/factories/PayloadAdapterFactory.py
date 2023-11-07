from src.adapters.PayloadAdapter import PayloadAdapter
from src.adapters.reverse_shell.linux_32.reverse_shell_linux_32bit_adapter import ReverseShellLinux32BitAdapter


class PayloadAdapterFactory:

    @staticmethod
    def make_adapter(name: str) -> PayloadAdapter:
        return {"reverse_shell/linux/linux32_nonstaged": ReverseShellLinux32BitAdapter()}[name.lower()]
