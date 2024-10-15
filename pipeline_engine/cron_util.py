from datetime import datetime


'''
Example usage:
    cron_hour = 2
    cron_minute = 45
    status = CronChecker.check_cron_time_ahead(cron)
'''
class CronChecker:
    @staticmethod
    def check_cron_time_ahead(cron: str) -> bool:
        parts = cron.split()
        cron_minute = int(parts[0]) # First part is the minute
        cron_hour = int(parts[1]) # Second part is the hour
        
        now = datetime.now()
        cron_time = now.replace(hour=cron_hour, minute=cron_minute, second=0, microsecond=0)

        if now < cron_time:
            return True
        else:
            return False
