from box_sdk_gen.client import BoxClient

from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributes

from box_sdk_gen.managers.uploads import UploadFileAttributesParentField

from box_sdk_gen.schemas import FileFull

from box_sdk_gen.schemas import Task

from box_sdk_gen.managers.tasks import CreateTaskItem

from box_sdk_gen.managers.tasks import CreateTaskItemTypeField

from box_sdk_gen.managers.tasks import CreateTaskAction

from box_sdk_gen.managers.tasks import CreateTaskCompletionRule

from box_sdk_gen.schemas import Tasks

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_stream

from test.commons import get_default_client

client: BoxClient = get_default_client()


def testCreateUpdateGetDeleteTask():
    files: Files = client.uploads.upload_file(
        attributes=UploadFileAttributes(
            name=get_uuid(), parent=UploadFileAttributesParentField(id='0')
        ),
        file=generate_byte_stream(10),
    )
    file: FileFull = files.entries[0]
    task: Task = client.tasks.create_task(
        item=CreateTaskItem(type=CreateTaskItemTypeField.FILE.value, id=file.id),
        action=CreateTaskAction.REVIEW.value,
        message='test message',
        due_at='2035-01-01T00:00:00Z',
        completion_rule=CreateTaskCompletionRule.ALL_ASSIGNEES.value,
    )
    assert task.message == 'test message'
    assert task.item.id == file.id
    task_by_id: Task = client.tasks.get_task_by_id(task_id=task.id)
    assert task_by_id.id == task.id
    task_on_file: Tasks = client.tasks.get_file_tasks(file_id=file.id)
    assert task_on_file.total_count == 1
    updated_task: Task = client.tasks.update_task_by_id(
        task_id=task.id, message='updated message'
    )
    assert updated_task.message == 'updated message'
    client.tasks.delete_task_by_id(task_id=task.id)
    client.files.delete_file_by_id(file_id=file.id)
