class NotificationBase:
    def __init__(self,notification_type:str,level:int,endpoint:str):
        self.notification_type = notification_type
        self.level = level
        self.endpoint = endpoint

    def create_notification(self):
        pass