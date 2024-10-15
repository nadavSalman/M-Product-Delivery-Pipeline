import yaml
import jsonschema
import json
import os


class PiplineLint:

    def __init__(self,pipline_yaml_path,schema_file_path=f'{os.path.dirname(os.path.abspath(__file__))}/schema.json'):
        self.pipline_yaml_path = pipline_yaml_path
        self.schema_file_path = schema_file_path

    def load_schema(self):
        with open(self.schema_file_path, 'r') as file:
            return json.load(file)

    def load_yaml(self):
        with open(self.pipline_yaml_path, 'r') as file:
            return yaml.safe_load(file)

    def validate_yaml(self,data, schema):
        jsonschema.validate(instance=data, schema=schema)

    def lint(self):
        try:
            # Load the JSON Schema
            schema = self.load_schema()
            # print("JSON Schema loaded successfully.")

            # Load YAML data
            yaml_data = self.load_yaml()
            # print("YAML data loaded successfully.")

            # Validate against the schema
            self.validate_yaml(yaml_data, schema)
            print(f"YAML {self.pipline_yaml_path.split('/')[-1]} data is valid according to the schema.")
            
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except jsonschema.ValidationError as ve:
            print(f"Validation error: {ve.message}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def __str__(self):
            return f"Pipeline YAML Path: {self.pipline_yaml_path}\nSchema File Path: {self.schema_file_path}"