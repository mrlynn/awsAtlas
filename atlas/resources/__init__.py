from .alert_configurations import AlertConfigurations
from .alerts import Alerts
from .atlas_users import AtlasUsers
from .auditing import Auditing
from .checkpoints import Checkpoints
from .cloud_provider_snapshot_restore_jobs import CloudProviderSnapshotRestoreJobs
from .cloud_provider_snapshot_schedule import CloudProviderSnapshotSchedule
from .cloud_provider_snapshots import CloudProviderSnapshots
from .clusters import Clusters
from .continuous_backup_restore_jobs import ContinuousBackupRestoreJobs
from .continuous_backup_snapshot_schedule import ContinuousBackupSnapshotSchedule
from .continuous_backup_snapshots import ContinuousBackupSnapshots
from .custom_roles import CustomRoles
from .database_users import DatabaseUsers
from .encryption_at_rest import EncryptionAtRest
from .events import Events
from .global_clusters import GlobalClusters
from .invoices import Invoices
from .ldap_configuration import LdapConfiguration
from .maintenance_windows import MaintenanceWindows
from .monitoring_and_logs import Monitoring, Logs
from .organizations import Organizations
from .performace_advisor import PerformanceAdvisor
from .project_whitelist import ProjectWhiteList
from .projects import Projects
from .root import Root
from .teams import Teams
from .user_api_keys import UserApiKeys
from .user_api_whitelist import UserApiWhitelist
from .vpc import Vpc

"""
All code in resources is really nothing more than wrappers to rest calls based off documentation
"""