from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def notify_task_change(action, task):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "tasks",
        {
            "type": "send_task_notification",
            "message": {
                "action": action,
                "task_id": task.id,
                "title": task.title
            }
        }
    )


def notify_task_deleted(task):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "tasks",
        {
            "type": "send_task_notification",
            "message": {
                "action": "deleted",
                "task_id": task['id'],
                "title": task['title']
            }
        }
    )
