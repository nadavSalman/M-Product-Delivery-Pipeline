from notification.notification_base import NotificationBase

# Mail notification implementation.
class MailNotification(NotificationBase):
    def __init__(self, level:int, endpoint:str):
        super().__init__('Mail', level,endpoint)

    def create_notification(self,):
        print(f"Notification: A mail notification has been createdת with level: '{self.level}' and endpoint: {self.endpoint}.")
