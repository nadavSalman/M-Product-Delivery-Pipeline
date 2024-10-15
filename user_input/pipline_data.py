from user_input.stage import Stage
from collections import deque
import yaml
from typing import List
from user_input.pipline_validation import PiplineLint

'''
This class holds all the pipeline data in multiple representations, such as dictionaries and nested objects.
Instantiation Example :

    yaml_pipline_path = f'{os.path.dirname(os.path.abspath(__file__))}/user_input_piplines/ProductDeployment.yaml'
    pipline_data = PipelineData(yaml_pipline_path)
    print(pipline_data)
    pipline_data.ouput_stages()
'''
class PipelineData:
    def __init__(self,pipeline_yaml_path):

        self._stages:List[Stage] = []
        self.pipeline_yaml_path = pipeline_yaml_path
        self.validate_yaml_pipline() # Calling linter to validate user input.
        self.pipline_data_dict = None
        self.pipline_data_dict = self.load_yaml()
        self.load_stages()

    @property
    def stages(self):
        return self._stages

    @stages.setter
    def stages(self, value: List[Stage]):
        self._stages = value
    
    def validate_yaml_pipline(self):
        linter = PiplineLint(self.pipeline_yaml_path)
        linter.lint()

    def validate_required_stages(self):
        stages_types = ["build", "deploy", "notfication"]
        for stage in self.stages:
            if stage.type in stages_types:
                stages_types.remove(stage.type)

        return stages_types == [] 
    
    def load_yaml(self):
        with open(self.pipeline_yaml_path, 'r') as file:
            return yaml.safe_load(file)
        
    def load_stages(self):
        for stage_item in self.pipline_data_dict.get('stages'):
            # print(f'{stage_item = }')
            self.stages.append(
                Stage(stage_item.get('name'),
                      stage_item.get('type'),
                      stage_item.get('args'))
            )
    
    def ouput_stages(self):
        for stage in self.stages:
            print(stage.args)

    def get_scheduled_cron_time(self):
        return self.pipline_data_dict.get('scheduledTime')

    def get_product_name(self):
        return self.pipline_data_dict.get('productName')

    def __str__(self):
        # return f'{self.pipline_data_dict}'
        yaml_str = yaml.dump(self.pipline_data_dict, default_flow_style=False, sort_keys=False)
        return f"Pipeline YAML:\n{yaml_str}"