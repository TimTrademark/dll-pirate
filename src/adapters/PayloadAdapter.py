import abc


class PayloadAdapter:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_modified_payload(self, payload_content: str, args: dict) -> str:
        """
        Modifies the payload using the arguments given. The arguments are dynamic and differ between the different
        Adapter implmentations.
        """
        return

    @abc.abstractmethod
    def get_payload_file_extension(self) -> str:
        return ""
