from .resources import AlertConfigurations
from .resources import Alerts
from .resources import AtlasUsers
from .resources import Auditing
from .resources import Checkpoints
from .resources import CloudProviderSnapshotRestoreJobs
from .resources import CloudProviderSnapshotSchedule
from .resources import CloudProviderSnapshots
from .resources import Clusters
from .resources import ContinuousBackupRestoreJobs
from .resources import ContinuousBackupSnapshotSchedule
from .resources import ContinuousBackupSnapshots
from .resources import CustomRoles
from .resources import DatabaseUsers
from .resources import EncryptionAtRest
from .resources import Events
from .resources import GlobalClusters
from .resources import Invoices
from .resources import LdapConfiguration
from .resources import MaintenanceWindows
from .resources import Monitoring, Logs
from .resources import Organizations
from .resources import PerformanceAdvisor
from .resources import ProjectWhiteList
from .resources import Projects
from .resources import Root
from .resources import Teams
from .resources import UserApiKeys
from .resources import UserApiWhitelist
from .resources import Vpc


class AtlasApi(
    AlertConfigurations,
    Alerts,
    AtlasUsers,
    Auditing,
    Checkpoints,
    CloudProviderSnapshotRestoreJobs,
    CloudProviderSnapshotSchedule,
    CloudProviderSnapshots,
    Clusters,
    ContinuousBackupRestoreJobs,
    ContinuousBackupSnapshotSchedule,
    ContinuousBackupSnapshots,
    CustomRoles,
    DatabaseUsers,
    EncryptionAtRest,
    Events,
    GlobalClusters,
    Invoices,
    LdapConfiguration,
    Logs,
    MaintenanceWindows,
    Monitoring,
    Organizations,
    PerformanceAdvisor,
    ProjectWhiteList,
    Projects,
    Root,
    Teams,
    UserApiKeys,
    UserApiWhitelist,
    Vpc
):
    pass
