from src.factories.PayloadAdapterFactory import PayloadAdapterFactory


class PayloadGenerator:

    @staticmethod
    def generate_payload(name: str, target: str, args: dict):
        '''dll_def = gen_def(args.target)
        def_filename = args.target + ".def"
        with open(def_filename, 'w', encoding='utf-8') as f:
            f.write(dll_def)'''
        adapter = PayloadAdapterFactory.make_adapter(name)
        path = name + adapter.get_payload_file_extension()
        modified_payload = ''
        with open(f'payloads/{path}', 'r') as f:
            content = f.read()
            modified_payload = adapter.get_modified_payload(content, args)
        tmp_modified_file = path.replace('/', '_')
        with open(tmp_modified_file) as f:
            f.write(modified_payload)
