from product.product_interface import ProductInterface
from user_input.pipline_data import PipelineData
from user_input.stage import Stage
import uuid
from repository.repositories_util import RepositoryFactory
from repository.repository_base import RepositoryBase
from notification.notification_util import NotoficationFactory
from product.pipline_state import PipelineState



'''
The class represent the product life cycle through the various actions. 
A product instance is associated with pipeline metadata to perform the action according the the user input.

Instantiation Example 01 :

    yaml_pipline_path = f'{os.path.dirname(os.path.abspath(__file__))}/user_input_piplines/ProductDeployment.yaml'
    product = Product(pipline_data=PipelineData(yaml_pipline_path))

------------------------------

Instantiation Example 02 (Executing pipline stages) :
    yaml_pipline_path = f'{os.path.dirname(os.path.abspath(__file__))}/user_input_piplines/ProductDeployment.yaml'
    product = Product(pipline_data=PipelineData(yaml_pipline_path))

    for stage_obj in product.pipline.stages:
        print(f'\nPreper for stage type: {stage_obj.type} execution.')
        product.solve_for(name=stage_obj.type,
                          stage=stage_obj)

Output :

YAML data is valid according to the schema.


<<< Pipline execution is about to start at the scheduled time : 0 0 * * * >>> 



Preper for stage type: build execution.
Resolve function  : build
Build Successful. Artifact : fplatform-6bb96b9e-bab1-4902-bc47-d82ba865f592.zip 

Preper for stage type: deploy execution.
Resolve function  : deploy
Artifact: ~/.platform-6bb96b9e-bab1-4902-bc47-d82ba865f592.zip successfully published to Artifactory: https://artifactory.example.com/repository/my-app-releases
Artifact: ~/.platform-6bb96b9e-bab1-4902-bc47-d82ba865f592.zip successfully published to Nexus: https://nexus.example.com/repository/my-app-releases

Preper for stage type: notify execution.
Resolve function  : notify
Notification: A mail notification has been createdת with level: '3' and endpoint: integrationcore@mobileye.com.
Notification: A Slack notification has been createdת with level: '1' and endpoint: https://hooks.slack.com/services/T00000000/.

'''
class Product(ProductInterface):
    def __init__(self,pipline_data: PipelineData):
        self.pipline = pipline_data
        self._scheduled_time = self.pipline.get_scheduled_cron_time()
        self.product_artifact_uid = uuid.uuid4()
        self.artifact_name = ''
        self._state = PipelineState.PENDING
        
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value: PipelineState):
        if not isinstance(value, PipelineState):
            raise ValueError("State must be a valid PipelineState enum member.")
        self._state = value

    @property
    def scheduled_time(self):
        return self._scheduled_time
    
    # Notify at the scheduled time each day.
    def notify_scheduled_time(self):
        print(f'\n\n<<< Pipline execution is about to start at the scheduled time : {self._scheduled_time} >>> \n\n')
    
    def build(self, stage:Stage):
        self.notify_scheduled_time()

        prefix = stage.args.get('prefix')
        self.artifact_name = f"{prefix}-{self.product_artifact_uid}.zip"
        print(f"Build Successful. \b Artifact : f{self.artifact_name} ")

    def deploy(self, stage:Stage):
        factory = RepositoryFactory()
        for repository_arg in stage.args.get('repositoryTargets'):
            repository:RepositoryBase = factory.create_repository(repository_arg.get('type'), 
                                                                  repository_arg.get('url'))
            
            repository.publis_artifact(artifact_path=f'~/.{self.artifact_name}')

    def notify(self, stage:Stage):
        factory = NotoficationFactory()
        for notification_channel_arg in stage.args.get('channels'):
            notification = factory.create_notification(notification_type=notification_channel_arg.get('type'),
                                                       endpoint=notification_channel_arg.get('endpoint'),
                                                       level=notification_channel_arg.get('level'))
            
            notification.create_notification()
   
    '''
    Dynamic function call resolver
    The goal is to call a function for the available product actions (e.g., build(), deploy(), notify(), etc.) based on the stage type. 
    This eliminates the need to check the condition for the Stage object type and call specific methods. 
    The main downside is that the decoupling requires the stage type to match the function name, but we are validating the stages type with schema:
        "type": {
            "type": "string",
            "enum": ["build", "deploy", "notify"]
        },
    '''
    def solve_for(self, name: str, *args, **kwargs):
        if hasattr(self, name) and callable(func := getattr(self, name)):
            print(f"Resolve function  : {name}")
            return func(*args, **kwargs)
        else:
            print(f"Faile to resolve function for resource : {name}")
