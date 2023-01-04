import unittest
from schema_builder import JsonSchemaBuilder, add_object


class TestJsonSchemaBuilder(unittest.TestCase):
    def test_add_property(self):
        builder = JsonSchemaBuilder()
        builder.add_property("name", "string")
        builder.add_property("age", 'integer')
        schema = builder.to_schema()
        self.assertEqual(schema, {
            "name": {
                "type": "string",
                "tag": "",
                "description": "",
                "required": False
            },
            "age": {
                "type": "integer",
                "tag": "",
                "description": "",
                "required": False
            }
        })

    def test_add_object(self):
        data = {
            "name": "Job",
            "age": 26,
            "address": {
                "street": "Oworo St",
                "city": "Elele"
            }
        }

        builder = add_object(data)
        schema = builder.to_schema()
        self.assertEqual(schema, {
            "name": {
                "type": "string",
                "tag": "",
                "description": "",
                "required": False
            },
            "age": {
                "type": "integer",
                "tag": "",
                "description": "",
                "required": False
            },
            "address": {
                "type": "array",
                "tag": "",
                "description": "",
                "required": False,
                "attributes": {
                    "street": {
                        "type": "string",
                        "tag": "",
                        "description": "",
                        "required": False
                    },
                    "city": {
                        "type": "string",
                        "tag": "",
                        "description": "",
                        "required": False
                    }
                }
            }
        })


if __name__ == "__main__":
    unittest.main()
