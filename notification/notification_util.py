from notification.mail import MailNotification
from notification.slack import SlackNotification
from notification.notification_base import NotificationBase



class NotoficationFactory:
    def __init__(self):
        # Attribute to hold the mapping of notification types to classes
        self.notification_classes = {
            'mail': MailNotification,
            'slack': SlackNotification
        }

    def create_notification(self, notification_type: str, level:int, endpoint:str) -> NotificationBase:

        # Normalize the notification type (case insensitive)
        repo_class = self.notification_classes.get(notification_type.lower())

        if not repo_class:
            raise ValueError(f"Unknown notification type: {notification_type}")

        return repo_class(level, endpoint)# Instantiate a child class of NotificationBase...

    # Method to get all supported notification types.
    def get_supported_notification_types(self) -> list:
        return list(self.notification_classes.keys())