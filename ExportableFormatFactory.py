from TextFileImplementation import TextFileImplementation

class ExportableFormatFactory():
    @staticmethod
    def get_format_instance_type(format_type):
        if format_type == 'text':
            return TextFileImplementation.get_instance()