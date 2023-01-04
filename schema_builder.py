class JsonSchemaBuilder:
    def __init__(self):
        self.schema = {}

    def add_property(self, name, prop_type, prop_format=None):
        prop = {
            "type": prop_type,
            "tag": "",
            "description": "",
            "required": False
        }
        if prop_format is not None:
            prop['attributes'] = prop_format
        self.schema[name] = prop

    def to_schema(self):
        return self.schema


def add_object(obj):
    """
    Takes a JSON object and generates a 'JsonSchemaBuilder' object
    """
    builder = JsonSchemaBuilder()
    for key, val in obj.items():
        prop_type = type(val).__name__
        if prop_type == 'dict':
            # Recursively process nested Object
            nested_builder = add_object(val)
            builder.add_property(key, 'array', nested_builder.to_schema())
        elif prop_type == 'str':
            builder.add_property(key, 'string')
        elif prop_type == 'int':
            builder.add_property(key, 'integer')
        elif prop_type == "list":
            if len(val) > 0:
                item_type = type(val[0]).__name__
                if item_type == 'str':
                    builder.add_property(key, 'enum')
                elif item_type == 'dict':
                    builder.add_property(key, "array")
    return builder
