import os
from user_input.pipline_data import PipelineData
from product.product import Product
from pipeline_engine.pipleline_executor import PiplelineExecutor

def main():

    # yaml_pipline_path = f'{os.path.dirname(os.path.abspath(__file__))}/user_input_piplines/core.yaml'
    # product = Product(pipline_data=PipelineData(yaml_pipline_path))

    # for stage_obj in product.pipline.stages:
    #     print(f'\nPreper for stage type: {stage_obj.type} execution.')

        # product.solve_for(name=stage_obj.type,
        #                   stage=stage_obj)
        
    # executer = PiplelineExecutor()
    # print(executer.piplines_dir)
    # print(executer.products_piplines)
    # for product in executer.products_piplines:
    #     print(f'{product.scheduled_time = }')

    executer = PiplelineExecutor()
    executer.execute()
        

    

if __name__ == '__main__':
    main()