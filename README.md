# JSON Schema Builder

This is a simple Python library for generating a JSON schema from a JSON object.

## Usage

To use the library, import the 'JsonSchemaBuilder' class and the 'from_object 'function: 

`from schema_builder import JsonSchemaBuilder, add_object`

Then, create a 'JsonSchemaBuilder' object using the add_object function and the JSON object you want to generate a schema for:

`data = {
  "name": "John",
  "age": 30
}
builder = from_object(data)
`
To get the JSOn Schema object, call the 'to_schema' method of the JsonSchemaBuilder' object

`schema = builder.to_schema()`