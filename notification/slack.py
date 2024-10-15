from notification.notification_base import NotificationBase

# Slack notification implementation.
class SlackNotification(NotificationBase):
    def __init__(self, level:int, endpoint:str):
        super().__init__('Slack', level,endpoint)

    def create_notification(self,):
        print(f"Notification: A Slack notification has been createdת with level: '{self.level}' and endpoint: {self.endpoint}.")