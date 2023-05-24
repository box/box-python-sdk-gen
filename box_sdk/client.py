from typing import Union

from box_sdk.base_object import BaseObject

from box_sdk.managers.authorization import AuthorizationManager

from box_sdk.managers.files import FilesManager

from box_sdk.managers.trashed_files import TrashedFilesManager

from box_sdk.managers.downloads import DownloadsManager

from box_sdk.managers.uploads import UploadsManager

from box_sdk.managers.chunked_uploads import ChunkedUploadsManager

from box_sdk.managers.list_collaborations import ListCollaborationsManager

from box_sdk.managers.comments import CommentsManager

from box_sdk.managers.tasks import TasksManager

from box_sdk.managers.file_versions import FileVersionsManager

from box_sdk.managers.file_metadata import FileMetadataManager

from box_sdk.managers.file_classifications import FileClassificationsManager

from box_sdk.managers.skills import SkillsManager

from box_sdk.managers.file_watermarks import FileWatermarksManager

from box_sdk.managers.file_requests import FileRequestsManager

from box_sdk.managers.folders import FoldersManager

from box_sdk.managers.trashed_folders import TrashedFoldersManager

from box_sdk.managers.folder_metadata import FolderMetadataManager

from box_sdk.managers.folder_classifications import FolderClassificationsManager

from box_sdk.managers.trashed_items import TrashedItemsManager

from box_sdk.managers.folder_watermarks import FolderWatermarksManager

from box_sdk.managers.folder_locks import FolderLocksManager

from box_sdk.managers.metadata_templates import MetadataTemplatesManager

from box_sdk.managers.classifications import ClassificationsManager

from box_sdk.managers.metadata_cascade_policies import MetadataCascadePoliciesManager

from box_sdk.managers.search import SearchManager

from box_sdk.managers.user_collaborations import UserCollaborationsManager

from box_sdk.managers.task_assignments import TaskAssignmentsManager

from box_sdk.managers.shared_links_files import SharedLinksFilesManager

from box_sdk.managers.shared_links_folders import SharedLinksFoldersManager

from box_sdk.managers.web_links import WebLinksManager

from box_sdk.managers.trashed_web_links import TrashedWebLinksManager

from box_sdk.managers.shared_links_web_links import SharedLinksWebLinksManager

from box_sdk.managers.users import UsersManager

from box_sdk.managers.session_termination import SessionTerminationManager

from box_sdk.managers.avatars import AvatarsManager

from box_sdk.managers.transfer import TransferManager

from box_sdk.managers.email_aliases import EmailAliasesManager

from box_sdk.managers.memberships import MembershipsManager

from box_sdk.managers.invites import InvitesManager

from box_sdk.managers.groups import GroupsManager

from box_sdk.managers.webhooks import WebhooksManager

from box_sdk.managers.events import EventsManager

from box_sdk.managers.collections import CollectionsManager

from box_sdk.managers.recent_items import RecentItemsManager

from box_sdk.managers.retention_policies import RetentionPoliciesManager

from box_sdk.managers.retention_policy_assignments import RetentionPolicyAssignmentsManager

from box_sdk.managers.legal_hold_policies import LegalHoldPoliciesManager

from box_sdk.managers.legal_hold_policy_assignments import LegalHoldPolicyAssignmentsManager

from box_sdk.managers.file_version_retentions import FileVersionRetentionsManager

from box_sdk.managers.file_version_legal_holds import FileVersionLegalHoldsManager

from box_sdk.managers.shield_information_barriers import ShieldInformationBarriersManager

from box_sdk.managers.shield_information_barrier_reports import ShieldInformationBarrierReportsManager

from box_sdk.managers.shield_information_barrier_segments import ShieldInformationBarrierSegmentsManager

from box_sdk.managers.shield_information_barrier_segment_members import ShieldInformationBarrierSegmentMembersManager

from box_sdk.managers.shield_information_barrier_segment_restrictions import ShieldInformationBarrierSegmentRestrictionsManager

from box_sdk.managers.device_pinners import DevicePinnersManager

from box_sdk.managers.terms_of_services import TermsOfServicesManager

from box_sdk.managers.terms_of_service_user_statuses import TermsOfServiceUserStatusesManager

from box_sdk.managers.collaboration_allowlist_entries import CollaborationAllowlistEntriesManager

from box_sdk.managers.collaboration_allowlist_exempt_targets import CollaborationAllowlistExemptTargetsManager

from box_sdk.managers.storage_policies import StoragePoliciesManager

from box_sdk.managers.storage_policy_assignments import StoragePolicyAssignmentsManager

from box_sdk.managers.zip_downloads import ZipDownloadsManager

from box_sdk.managers.sign_requests import SignRequestsManager

from box_sdk.managers.workflows import WorkflowsManager

from box_sdk.managers.sign_templates import SignTemplatesManager

from box_sdk.managers.integration_mappings import IntegrationMappingsManager

from box_sdk.developer_token_auth import DeveloperTokenAuth

from box_sdk.ccg_auth import CCGAuth

from box_sdk.jwt_auth import JWTAuth

class Client(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth, JWTAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.authorization = AuthorizationManager(auth=self.auth)
        self.files = FilesManager(auth=self.auth)
        self.trashed_files = TrashedFilesManager(auth=self.auth)
        self.downloads = DownloadsManager(auth=self.auth)
        self.uploads = UploadsManager(auth=self.auth)
        self.chunked_uploads = ChunkedUploadsManager(auth=self.auth)
        self.list_collaborations = ListCollaborationsManager(auth=self.auth)
        self.comments = CommentsManager(auth=self.auth)
        self.tasks = TasksManager(auth=self.auth)
        self.file_versions = FileVersionsManager(auth=self.auth)
        self.file_metadata = FileMetadataManager(auth=self.auth)
        self.file_classifications = FileClassificationsManager(auth=self.auth)
        self.skills = SkillsManager(auth=self.auth)
        self.file_watermarks = FileWatermarksManager(auth=self.auth)
        self.file_requests = FileRequestsManager(auth=self.auth)
        self.folders = FoldersManager(auth=self.auth)
        self.trashed_folders = TrashedFoldersManager(auth=self.auth)
        self.folder_metadata = FolderMetadataManager(auth=self.auth)
        self.folder_classifications = FolderClassificationsManager(auth=self.auth)
        self.trashed_items = TrashedItemsManager(auth=self.auth)
        self.folder_watermarks = FolderWatermarksManager(auth=self.auth)
        self.folder_locks = FolderLocksManager(auth=self.auth)
        self.metadata_templates = MetadataTemplatesManager(auth=self.auth)
        self.classifications = ClassificationsManager(auth=self.auth)
        self.metadata_cascade_policies = MetadataCascadePoliciesManager(auth=self.auth)
        self.search = SearchManager(auth=self.auth)
        self.user_collaborations = UserCollaborationsManager(auth=self.auth)
        self.task_assignments = TaskAssignmentsManager(auth=self.auth)
        self.shared_links_files = SharedLinksFilesManager(auth=self.auth)
        self.shared_links_folders = SharedLinksFoldersManager(auth=self.auth)
        self.web_links = WebLinksManager(auth=self.auth)
        self.trashed_web_links = TrashedWebLinksManager(auth=self.auth)
        self.shared_links_web_links = SharedLinksWebLinksManager(auth=self.auth)
        self.users = UsersManager(auth=self.auth)
        self.session_termination = SessionTerminationManager(auth=self.auth)
        self.avatars = AvatarsManager(auth=self.auth)
        self.transfer = TransferManager(auth=self.auth)
        self.email_aliases = EmailAliasesManager(auth=self.auth)
        self.memberships = MembershipsManager(auth=self.auth)
        self.invites = InvitesManager(auth=self.auth)
        self.groups = GroupsManager(auth=self.auth)
        self.webhooks = WebhooksManager(auth=self.auth)
        self.events = EventsManager(auth=self.auth)
        self.collections = CollectionsManager(auth=self.auth)
        self.recent_items = RecentItemsManager(auth=self.auth)
        self.retention_policies = RetentionPoliciesManager(auth=self.auth)
        self.retention_policy_assignments = RetentionPolicyAssignmentsManager(auth=self.auth)
        self.legal_hold_policies = LegalHoldPoliciesManager(auth=self.auth)
        self.legal_hold_policy_assignments = LegalHoldPolicyAssignmentsManager(auth=self.auth)
        self.file_version_retentions = FileVersionRetentionsManager(auth=self.auth)
        self.file_version_legal_holds = FileVersionLegalHoldsManager(auth=self.auth)
        self.shield_information_barriers = ShieldInformationBarriersManager(auth=self.auth)
        self.shield_information_barrier_reports = ShieldInformationBarrierReportsManager(auth=self.auth)
        self.shield_information_barrier_segments = ShieldInformationBarrierSegmentsManager(auth=self.auth)
        self.shield_information_barrier_segment_members = ShieldInformationBarrierSegmentMembersManager(auth=self.auth)
        self.shield_information_barrier_segment_restrictions = ShieldInformationBarrierSegmentRestrictionsManager(auth=self.auth)
        self.device_pinners = DevicePinnersManager(auth=self.auth)
        self.terms_of_services = TermsOfServicesManager(auth=self.auth)
        self.terms_of_service_user_statuses = TermsOfServiceUserStatusesManager(auth=self.auth)
        self.collaboration_allowlist_entries = CollaborationAllowlistEntriesManager(auth=self.auth)
        self.collaboration_allowlist_exempt_targets = CollaborationAllowlistExemptTargetsManager(auth=self.auth)
        self.storage_policies = StoragePoliciesManager(auth=self.auth)
        self.storage_policy_assignments = StoragePolicyAssignmentsManager(auth=self.auth)
        self.zip_downloads = ZipDownloadsManager(auth=self.auth)
        self.sign_requests = SignRequestsManager(auth=self.auth)
        self.workflows = WorkflowsManager(auth=self.auth)
        self.sign_templates = SignTemplatesManager(auth=self.auth)
        self.integration_mappings = IntegrationMappingsManager(auth=self.auth)