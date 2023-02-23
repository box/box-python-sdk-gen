from typing import Union

from developer_token_auth import DeveloperTokenAuth

from ccg_auth import CCGAuth

from base_object import BaseObject

from managers.authorization import AuthorizationManager

from managers.files import FilesManager

from managers.downloads import DownloadsManager

from managers.uploads import UploadsManager

from managers.chunked_uploads import ChunkedUploadsManager

from managers.list_collaborations import ListCollaborationsManager

from managers.comments import CommentsManager

from managers.tasks import TasksManager

from managers.trashed_files import TrashedFilesManager

from managers.file_versions import FileVersionsManager

from managers.file_metadata import FileMetadataManager

from managers.file_classifications import FileClassificationsManager

from managers.skills import SkillsManager

from managers.file_watermarks import FileWatermarksManager

from managers.file_requests import FileRequestsManager

from managers.folders import FoldersManager

from managers.trashed_folders import TrashedFoldersManager

from managers.folder_metadata import FolderMetadataManager

from managers.folder_classifications import FolderClassificationsManager

from managers.trashed_items import TrashedItemsManager

from managers.folder_watermarks import FolderWatermarksManager

from managers.folder_locks import FolderLocksManager

from managers.metadata_templates import MetadataTemplatesManager

from managers.classifications import ClassificationsManager

from managers.metadata_cascade_policies import MetadataCascadePoliciesManager

from managers.search import SearchManager

from managers.user_collaborations import UserCollaborationsManager

from managers.task_assignments import TaskAssignmentsManager

from managers.shared_links_files import SharedLinksFilesManager

from managers.shared_links_folders import SharedLinksFoldersManager

from managers.web_links import WebLinksManager

from managers.trashed_web_links import TrashedWebLinksManager

from managers.shared_links_web_links import SharedLinksWebLinksManager

from managers.users import UsersManager

from managers.session_termination import SessionTerminationManager

from managers.avatars import AvatarsManager

from managers.transfer import TransferManager

from managers.email_aliases import EmailAliasesManager

from managers.memberships import MembershipsManager

from managers.invites import InvitesManager

from managers.groups import GroupsManager

from managers.webhooks import WebhooksManager

from managers.events import EventsManager

from managers.collections import CollectionsManager

from managers.recent_items import RecentItemsManager

from managers.retention_policies import RetentionPoliciesManager

from managers.retention_policy_assignments import RetentionPolicyAssignmentsManager

from managers.legal_hold_policies import LegalHoldPoliciesManager

from managers.legal_hold_policy_assignments import LegalHoldPolicyAssignmentsManager

from managers.file_version_retentions import FileVersionRetentionsManager

from managers.file_version_legal_holds import FileVersionLegalHoldsManager

from managers.shield_information_barriers import ShieldInformationBarriersManager

from managers.shield_information_barrier_reports import ShieldInformationBarrierReportsManager

from managers.shield_information_barrier_segments import ShieldInformationBarrierSegmentsManager

from managers.shield_information_barrier_segment_members import ShieldInformationBarrierSegmentMembersManager

from managers.shield_information_barrier_segment_restrictions import ShieldInformationBarrierSegmentRestrictionsManager

from managers.device_pinners import DevicePinnersManager

from managers.terms_of_services import TermsOfServicesManager

from managers.terms_of_service_user_statuses import TermsOfServiceUserStatusesManager

from managers.collaboration_allowlist_entries import CollaborationAllowlistEntriesManager

from managers.collaboration_allowlist_exempt_targets import CollaborationAllowlistExemptTargetsManager

from managers.storage_policies import StoragePoliciesManager

from managers.storage_policy_assignments import StoragePolicyAssignmentsManager

from managers.zip_downloads import ZipDownloadsManager

from managers.sign_requests import SignRequestsManager

from managers.workflows import WorkflowsManager

class Client(BaseObject):
    def __init__(self, auth: Union[DeveloperTokenAuth, CCGAuth], **kwargs):
        super().__init__(**kwargs)
        self.auth = auth
        self.authorization = AuthorizationManager(auth=self.auth)
        self.files = FilesManager(auth=self.auth)
        self.downloads = DownloadsManager(auth=self.auth)
        self.uploads = UploadsManager(auth=self.auth)
        self.chunked_uploads = ChunkedUploadsManager(auth=self.auth)
        self.list_collaborations = ListCollaborationsManager(auth=self.auth)
        self.comments = CommentsManager(auth=self.auth)
        self.tasks = TasksManager(auth=self.auth)
        self.trashed_files = TrashedFilesManager(auth=self.auth)
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