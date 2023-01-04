import json
import schema_builder

with open('data/data_1.json') as f:
    data = json.load(f)

msg = data['message']
obs = schema_builder.add_object(msg)
schema = obs.to_schema()

with open('schema/schema_1.json', "w") as w:
    json.dump(schema, w, indent=2)
