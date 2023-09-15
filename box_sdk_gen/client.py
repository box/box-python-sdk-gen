from typing import Optional

from box_sdk_gen.managers.authorization import AuthorizationManager

from box_sdk_gen.managers.files import FilesManager

from box_sdk_gen.managers.trashed_files import TrashedFilesManager

from box_sdk_gen.managers.downloads import DownloadsManager

from box_sdk_gen.managers.uploads import UploadsManager

from box_sdk_gen.managers.chunked_uploads import ChunkedUploadsManager

from box_sdk_gen.managers.list_collaborations import ListCollaborationsManager

from box_sdk_gen.managers.comments import CommentsManager

from box_sdk_gen.managers.tasks import TasksManager

from box_sdk_gen.managers.file_versions import FileVersionsManager

from box_sdk_gen.managers.file_metadata import FileMetadataManager

from box_sdk_gen.managers.file_classifications import FileClassificationsManager

from box_sdk_gen.managers.skills import SkillsManager

from box_sdk_gen.managers.file_watermarks import FileWatermarksManager

from box_sdk_gen.managers.file_requests import FileRequestsManager

from box_sdk_gen.managers.folders import FoldersManager

from box_sdk_gen.managers.trashed_folders import TrashedFoldersManager

from box_sdk_gen.managers.folder_metadata import FolderMetadataManager

from box_sdk_gen.managers.folder_classifications import FolderClassificationsManager

from box_sdk_gen.managers.trashed_items import TrashedItemsManager

from box_sdk_gen.managers.folder_watermarks import FolderWatermarksManager

from box_sdk_gen.managers.folder_locks import FolderLocksManager

from box_sdk_gen.managers.metadata_templates import MetadataTemplatesManager

from box_sdk_gen.managers.classifications import ClassificationsManager

from box_sdk_gen.managers.metadata_cascade_policies import (
    MetadataCascadePoliciesManager,
)

from box_sdk_gen.managers.search import SearchManager

from box_sdk_gen.managers.user_collaborations import UserCollaborationsManager

from box_sdk_gen.managers.task_assignments import TaskAssignmentsManager

from box_sdk_gen.managers.shared_links_files import SharedLinksFilesManager

from box_sdk_gen.managers.shared_links_folders import SharedLinksFoldersManager

from box_sdk_gen.managers.web_links import WebLinksManager

from box_sdk_gen.managers.trashed_web_links import TrashedWebLinksManager

from box_sdk_gen.managers.shared_links_web_links import SharedLinksWebLinksManager

from box_sdk_gen.managers.users import UsersManager

from box_sdk_gen.managers.session_termination import SessionTerminationManager

from box_sdk_gen.managers.avatars import AvatarsManager

from box_sdk_gen.managers.transfer import TransferManager

from box_sdk_gen.managers.email_aliases import EmailAliasesManager

from box_sdk_gen.managers.memberships import MembershipsManager

from box_sdk_gen.managers.invites import InvitesManager

from box_sdk_gen.managers.groups import GroupsManager

from box_sdk_gen.managers.webhooks import WebhooksManager

from box_sdk_gen.managers.events import EventsManager

from box_sdk_gen.managers.collections import CollectionsManager

from box_sdk_gen.managers.recent_items import RecentItemsManager

from box_sdk_gen.managers.retention_policies import RetentionPoliciesManager

from box_sdk_gen.managers.retention_policy_assignments import (
    RetentionPolicyAssignmentsManager,
)

from box_sdk_gen.managers.legal_hold_policies import LegalHoldPoliciesManager

from box_sdk_gen.managers.legal_hold_policy_assignments import (
    LegalHoldPolicyAssignmentsManager,
)

from box_sdk_gen.managers.file_version_retentions import FileVersionRetentionsManager

from box_sdk_gen.managers.file_version_legal_holds import FileVersionLegalHoldsManager

from box_sdk_gen.managers.shield_information_barriers import (
    ShieldInformationBarriersManager,
)

from box_sdk_gen.managers.shield_information_barrier_reports import (
    ShieldInformationBarrierReportsManager,
)

from box_sdk_gen.managers.shield_information_barrier_segments import (
    ShieldInformationBarrierSegmentsManager,
)

from box_sdk_gen.managers.shield_information_barrier_segment_members import (
    ShieldInformationBarrierSegmentMembersManager,
)

from box_sdk_gen.managers.shield_information_barrier_segment_restrictions import (
    ShieldInformationBarrierSegmentRestrictionsManager,
)

from box_sdk_gen.managers.device_pinners import DevicePinnersManager

from box_sdk_gen.managers.terms_of_services import TermsOfServicesManager

from box_sdk_gen.managers.terms_of_service_user_statuses import (
    TermsOfServiceUserStatusesManager,
)

from box_sdk_gen.managers.collaboration_allowlist_entries import (
    CollaborationAllowlistEntriesManager,
)

from box_sdk_gen.managers.collaboration_allowlist_exempt_targets import (
    CollaborationAllowlistExemptTargetsManager,
)

from box_sdk_gen.managers.storage_policies import StoragePoliciesManager

from box_sdk_gen.managers.storage_policy_assignments import (
    StoragePolicyAssignmentsManager,
)

from box_sdk_gen.managers.zip_downloads import ZipDownloadsManager

from box_sdk_gen.managers.sign_requests import SignRequestsManager

from box_sdk_gen.managers.workflows import WorkflowsManager

from box_sdk_gen.managers.sign_templates import SignTemplatesManager

from box_sdk_gen.managers.integration_mappings import IntegrationMappingsManager

from box_sdk_gen.auth import Authentication

from box_sdk_gen.network import NetworkSession


class BoxClient:
    def __init__(
        self, auth: Authentication, network_session: Optional[NetworkSession] = None
    ):
        if network_session is None:
            network_session = NetworkSession()
        self.auth = auth
        self.network_session = network_session
        self.authorization = AuthorizationManager(
            auth=self.auth, network_session=self.network_session
        )
        self.files = FilesManager(auth=self.auth, network_session=self.network_session)
        self.trashed_files = TrashedFilesManager(
            auth=self.auth, network_session=self.network_session
        )
        self.downloads = DownloadsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.uploads = UploadsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.chunked_uploads = ChunkedUploadsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.list_collaborations = ListCollaborationsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.comments = CommentsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.tasks = TasksManager(auth=self.auth, network_session=self.network_session)
        self.file_versions = FileVersionsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.file_metadata = FileMetadataManager(
            auth=self.auth, network_session=self.network_session
        )
        self.file_classifications = FileClassificationsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.skills = SkillsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.file_watermarks = FileWatermarksManager(
            auth=self.auth, network_session=self.network_session
        )
        self.file_requests = FileRequestsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.folders = FoldersManager(
            auth=self.auth, network_session=self.network_session
        )
        self.trashed_folders = TrashedFoldersManager(
            auth=self.auth, network_session=self.network_session
        )
        self.folder_metadata = FolderMetadataManager(
            auth=self.auth, network_session=self.network_session
        )
        self.folder_classifications = FolderClassificationsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.trashed_items = TrashedItemsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.folder_watermarks = FolderWatermarksManager(
            auth=self.auth, network_session=self.network_session
        )
        self.folder_locks = FolderLocksManager(
            auth=self.auth, network_session=self.network_session
        )
        self.metadata_templates = MetadataTemplatesManager(
            auth=self.auth, network_session=self.network_session
        )
        self.classifications = ClassificationsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.metadata_cascade_policies = MetadataCascadePoliciesManager(
            auth=self.auth, network_session=self.network_session
        )
        self.search = SearchManager(
            auth=self.auth, network_session=self.network_session
        )
        self.user_collaborations = UserCollaborationsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.task_assignments = TaskAssignmentsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.shared_links_files = SharedLinksFilesManager(
            auth=self.auth, network_session=self.network_session
        )
        self.shared_links_folders = SharedLinksFoldersManager(
            auth=self.auth, network_session=self.network_session
        )
        self.web_links = WebLinksManager(
            auth=self.auth, network_session=self.network_session
        )
        self.trashed_web_links = TrashedWebLinksManager(
            auth=self.auth, network_session=self.network_session
        )
        self.shared_links_web_links = SharedLinksWebLinksManager(
            auth=self.auth, network_session=self.network_session
        )
        self.users = UsersManager(auth=self.auth, network_session=self.network_session)
        self.session_termination = SessionTerminationManager(
            auth=self.auth, network_session=self.network_session
        )
        self.avatars = AvatarsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.transfer = TransferManager(
            auth=self.auth, network_session=self.network_session
        )
        self.email_aliases = EmailAliasesManager(
            auth=self.auth, network_session=self.network_session
        )
        self.memberships = MembershipsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.invites = InvitesManager(
            auth=self.auth, network_session=self.network_session
        )
        self.groups = GroupsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.webhooks = WebhooksManager(
            auth=self.auth, network_session=self.network_session
        )
        self.events = EventsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.collections = CollectionsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.recent_items = RecentItemsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.retention_policies = RetentionPoliciesManager(
            auth=self.auth, network_session=self.network_session
        )
        self.retention_policy_assignments = RetentionPolicyAssignmentsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.legal_hold_policies = LegalHoldPoliciesManager(
            auth=self.auth, network_session=self.network_session
        )
        self.legal_hold_policy_assignments = LegalHoldPolicyAssignmentsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.file_version_retentions = FileVersionRetentionsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.file_version_legal_holds = FileVersionLegalHoldsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.shield_information_barriers = ShieldInformationBarriersManager(
            auth=self.auth, network_session=self.network_session
        )
        self.shield_information_barrier_reports = (
            ShieldInformationBarrierReportsManager(
                auth=self.auth, network_session=self.network_session
            )
        )
        self.shield_information_barrier_segments = (
            ShieldInformationBarrierSegmentsManager(
                auth=self.auth, network_session=self.network_session
            )
        )
        self.shield_information_barrier_segment_members = (
            ShieldInformationBarrierSegmentMembersManager(
                auth=self.auth, network_session=self.network_session
            )
        )
        self.shield_information_barrier_segment_restrictions = (
            ShieldInformationBarrierSegmentRestrictionsManager(
                auth=self.auth, network_session=self.network_session
            )
        )
        self.device_pinners = DevicePinnersManager(
            auth=self.auth, network_session=self.network_session
        )
        self.terms_of_services = TermsOfServicesManager(
            auth=self.auth, network_session=self.network_session
        )
        self.terms_of_service_user_statuses = TermsOfServiceUserStatusesManager(
            auth=self.auth, network_session=self.network_session
        )
        self.collaboration_allowlist_entries = CollaborationAllowlistEntriesManager(
            auth=self.auth, network_session=self.network_session
        )
        self.collaboration_allowlist_exempt_targets = (
            CollaborationAllowlistExemptTargetsManager(
                auth=self.auth, network_session=self.network_session
            )
        )
        self.storage_policies = StoragePoliciesManager(
            auth=self.auth, network_session=self.network_session
        )
        self.storage_policy_assignments = StoragePolicyAssignmentsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.zip_downloads = ZipDownloadsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.sign_requests = SignRequestsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.workflows = WorkflowsManager(
            auth=self.auth, network_session=self.network_session
        )
        self.sign_templates = SignTemplatesManager(
            auth=self.auth, network_session=self.network_session
        )
        self.integration_mappings = IntegrationMappingsManager(
            auth=self.auth, network_session=self.network_session
        )
