from typing import Optional

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.schemas.upload_part import UploadPart


class UploadedPart(BaseObject):
    def __init__(self, *, part: Optional[UploadPart] = None, **kwargs):
        super().__init__(**kwargs)
        self.part = part
