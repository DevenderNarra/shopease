class TodoParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "BasicProduct",
            "parameter_field_name": "todo"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "BasicProductSerializer",
            "param_serializer_import_str": "from shop.build.serializers.definitions.BasicProduct.BasicProductSerializer import BasicProductSerializer",
            "param_serializer_required": True,
            "param_serializer_array": False
        }
        return serializer_options
        

    @staticmethod
    def get_serializer_field():
        pass

    @staticmethod
    def get_url_regex():
        pass