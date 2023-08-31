from box_sdk_gen.schemas import Files

from box_sdk_gen.managers.uploads import UploadFileAttributesArg

from box_sdk_gen.managers.uploads import UploadFileAttributesArgParentField

from box_sdk_gen.schemas import File

from box_sdk_gen.schemas import Task

from box_sdk_gen.managers.tasks import CreateTaskItemArg

from box_sdk_gen.managers.tasks import CreateTaskItemArgTypeField

from box_sdk_gen.managers.tasks import CreateTaskActionArg

from box_sdk_gen.managers.tasks import CreateTaskCompletionRuleArg

from box_sdk_gen.schemas import Tasks

from box_sdk_gen.utils import decode_base_64

from box_sdk_gen.utils import get_env_var

from box_sdk_gen.utils import get_uuid

from box_sdk_gen.utils import generate_byte_stream

from box_sdk_gen.client import Client

from box_sdk_gen.jwt_auth import JWTAuth

from box_sdk_gen.jwt_auth import JWTConfig

jwt_config: JWTConfig = JWTConfig.from_config_json_string(
    decode_base_64(get_env_var("JWT_CONFIG_BASE_64"))
)

auth: JWTAuth = JWTAuth(config=jwt_config)

client: Client = Client(auth=auth)


def testCreateUpdateGetDeleteTask():
    files: Files = client.uploads.upload_file(
        attributes=UploadFileAttributesArg(
            name=get_uuid(), parent=UploadFileAttributesArgParentField(id="0")
        ),
        file=generate_byte_stream(10),
    )
    file: File = files.entries[0]
    task: Task = client.tasks.create_task(
        item=CreateTaskItemArg(type=CreateTaskItemArgTypeField.FILE.value, id=file.id),
        action=CreateTaskActionArg.REVIEW.value,
        message="test message",
        due_at="2035-01-01T00:00:00Z",
        completion_rule=CreateTaskCompletionRuleArg.ALL_ASSIGNEES.value,
    )
    assert task.message == "test message"
    assert task.item.id == file.id
    task_by_id: Task = client.tasks.get_task_by_id(task_id=task.id)
    assert task_by_id.id == task.id
    task_on_file: Tasks = client.tasks.get_file_tasks(file_id=file.id)
    assert task_on_file.total_count == 1
    updated_task: Task = client.tasks.update_task_by_id(
        task_id=task.id, message="updated message"
    )
    assert updated_task.message == "updated message"
    client.tasks.delete_task_by_id(task_id=task.id)
    client.files.delete_file_by_id(file_id=file.id)
