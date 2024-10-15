import os
from product.product import Product
from user_input.pipline_data import PipelineData
from product.pipline_state import PipelineState
from pipeline_engine.cron_util import CronChecker
from datetime import datetime
import time



class PiplelineExecutor:

    def __init__(self,piplines_dir=f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/user_input_piplines'):
        self._products_piplines = None
        self._piplines_dir = piplines_dir
        self._products_piplines = self.load_products_piplines()

    
    @property
    def products_piplines(self):
        return self._products_piplines

    @products_piplines.setter
    def products_piplines(self, value):
        self._products_piplines = value

    @property
    def piplines_dir(self):
        return self._piplines_dir

    @piplines_dir.setter
    def piplines_dir(self, value):
        self._piplines_dir = value

    '''
    Load all the piplines pipline_yaml_path configuration into Product object list.
    '''
    def load_products_piplines(self):
        piplines_files_list = os.listdir(self.piplines_dir)
        return [Product(pipline_data=PipelineData(f'{self._piplines_dir}/{file}')) for file in piplines_files_list]
        
    def check_piplines_status(self):
        for product in self._products_piplines:
            if product.state == PipelineState.PENDING:
                return True
        return False

    def execute(self):
        while self.check_piplines_status():
            for product in self._products_piplines:
                if product.state == PipelineState.SUCCESS:
                    continue

                # if the crone time is not befor now(), then execute the pipline and update state.
                if not CronChecker.check_cron_time_ahead(product.scheduled_time):
                    for stage_obj in product.pipline.stages:
                        print(f'\nPreper for stage type: {stage_obj.type} execution.')
                        product.solve_for(name=stage_obj.type,
                          stage=stage_obj)
                    product.state = PipelineState.SUCCESS
            
            time.sleep(1)
            print(datetime.now().strftime("%H:%M:%S"))






