"Main interface for robomaker type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsTypeDef",
    "ClientBatchDescribeSimulationJobResponseTypeDef",
    "ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    "ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    "ClientCreateDeploymentJobResponsedeploymentConfigTypeDef",
    "ClientCreateDeploymentJobResponseTypeDef",
    "ClientCreateDeploymentJobdeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientCreateDeploymentJobdeploymentApplicationConfigsTypeDef",
    "ClientCreateDeploymentJobdeploymentConfigdownloadConditionFileTypeDef",
    "ClientCreateDeploymentJobdeploymentConfigTypeDef",
    "ClientCreateFleetResponseTypeDef",
    "ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientCreateRobotApplicationResponsesourcesTypeDef",
    "ClientCreateRobotApplicationResponseTypeDef",
    "ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef",
    "ClientCreateRobotApplicationVersionResponsesourcesTypeDef",
    "ClientCreateRobotApplicationVersionResponseTypeDef",
    "ClientCreateRobotApplicationrobotSoftwareSuiteTypeDef",
    "ClientCreateRobotApplicationsourcesTypeDef",
    "ClientCreateRobotResponseTypeDef",
    "ClientCreateSimulationApplicationResponserenderingEngineTypeDef",
    "ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationResponsesourcesTypeDef",
    "ClientCreateSimulationApplicationResponseTypeDef",
    "ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef",
    "ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationVersionResponsesourcesTypeDef",
    "ClientCreateSimulationApplicationVersionResponseTypeDef",
    "ClientCreateSimulationApplicationrenderingEngineTypeDef",
    "ClientCreateSimulationApplicationrobotSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationsimulationSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationsourcesTypeDef",
    "ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef",
    "ClientCreateSimulationJobResponsedataSourcesTypeDef",
    "ClientCreateSimulationJobResponseloggingConfigTypeDef",
    "ClientCreateSimulationJobResponseoutputLocationTypeDef",
    "ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef",
    "ClientCreateSimulationJobResponserobotApplicationsTypeDef",
    "ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef",
    "ClientCreateSimulationJobResponsesimulationApplicationsTypeDef",
    "ClientCreateSimulationJobResponsevpcConfigTypeDef",
    "ClientCreateSimulationJobResponseTypeDef",
    "ClientCreateSimulationJobdataSourcesTypeDef",
    "ClientCreateSimulationJobloggingConfigTypeDef",
    "ClientCreateSimulationJoboutputLocationTypeDef",
    "ClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientCreateSimulationJobrobotApplicationslaunchConfigTypeDef",
    "ClientCreateSimulationJobrobotApplicationsTypeDef",
    "ClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientCreateSimulationJobsimulationApplicationslaunchConfigTypeDef",
    "ClientCreateSimulationJobsimulationApplicationsTypeDef",
    "ClientCreateSimulationJobvpcConfigTypeDef",
    "ClientDeregisterRobotResponseTypeDef",
    "ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    "ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    "ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef",
    "ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef",
    "ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef",
    "ClientDescribeDeploymentJobResponseTypeDef",
    "ClientDescribeFleetResponserobotsTypeDef",
    "ClientDescribeFleetResponseTypeDef",
    "ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientDescribeRobotApplicationResponsesourcesTypeDef",
    "ClientDescribeRobotApplicationResponseTypeDef",
    "ClientDescribeRobotResponseTypeDef",
    "ClientDescribeSimulationApplicationResponserenderingEngineTypeDef",
    "ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    "ClientDescribeSimulationApplicationResponsesourcesTypeDef",
    "ClientDescribeSimulationApplicationResponseTypeDef",
    "ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef",
    "ClientDescribeSimulationJobResponsedataSourcesTypeDef",
    "ClientDescribeSimulationJobResponseloggingConfigTypeDef",
    "ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef",
    "ClientDescribeSimulationJobResponseoutputLocationTypeDef",
    "ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef",
    "ClientDescribeSimulationJobResponserobotApplicationsTypeDef",
    "ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef",
    "ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef",
    "ClientDescribeSimulationJobResponsevpcConfigTypeDef",
    "ClientDescribeSimulationJobResponseTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsTypeDef",
    "ClientListDeploymentJobsResponseTypeDef",
    "ClientListDeploymentJobsfiltersTypeDef",
    "ClientListFleetsResponsefleetDetailsTypeDef",
    "ClientListFleetsResponseTypeDef",
    "ClientListFleetsfiltersTypeDef",
    "ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef",
    "ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef",
    "ClientListRobotApplicationsResponseTypeDef",
    "ClientListRobotApplicationsfiltersTypeDef",
    "ClientListRobotsResponserobotsTypeDef",
    "ClientListRobotsResponseTypeDef",
    "ClientListRobotsfiltersTypeDef",
    "ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef",
    "ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef",
    "ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef",
    "ClientListSimulationApplicationsResponseTypeDef",
    "ClientListSimulationApplicationsfiltersTypeDef",
    "ClientListSimulationJobsResponsesimulationJobSummariesTypeDef",
    "ClientListSimulationJobsResponseTypeDef",
    "ClientListSimulationJobsfiltersTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRegisterRobotResponseTypeDef",
    "ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    "ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    "ClientSyncDeploymentJobResponsedeploymentConfigTypeDef",
    "ClientSyncDeploymentJobResponseTypeDef",
    "ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientUpdateRobotApplicationResponsesourcesTypeDef",
    "ClientUpdateRobotApplicationResponseTypeDef",
    "ClientUpdateRobotApplicationrobotSoftwareSuiteTypeDef",
    "ClientUpdateRobotApplicationsourcesTypeDef",
    "ClientUpdateSimulationApplicationResponserenderingEngineTypeDef",
    "ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    "ClientUpdateSimulationApplicationResponsesourcesTypeDef",
    "ClientUpdateSimulationApplicationResponseTypeDef",
    "ClientUpdateSimulationApplicationrenderingEngineTypeDef",
    "ClientUpdateSimulationApplicationrobotSoftwareSuiteTypeDef",
    "ClientUpdateSimulationApplicationsimulationSoftwareSuiteTypeDef",
    "ClientUpdateSimulationApplicationsourcesTypeDef",
    "ListDeploymentJobsPaginatePaginationConfigTypeDef",
    "ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef",
    "ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigsTypeDef",
    "ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef",
    "ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigTypeDef",
    "ListDeploymentJobsPaginateResponsedeploymentJobsTypeDef",
    "ListDeploymentJobsPaginateResponseTypeDef",
    "ListDeploymentJobsPaginatefiltersTypeDef",
    "ListFleetsPaginatePaginationConfigTypeDef",
    "ListFleetsPaginateResponsefleetDetailsTypeDef",
    "ListFleetsPaginateResponseTypeDef",
    "ListFleetsPaginatefiltersTypeDef",
    "ListRobotApplicationsPaginatePaginationConfigTypeDef",
    "ListRobotApplicationsPaginateResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef",
    "ListRobotApplicationsPaginateResponserobotApplicationSummariesTypeDef",
    "ListRobotApplicationsPaginateResponseTypeDef",
    "ListRobotApplicationsPaginatefiltersTypeDef",
    "ListRobotsPaginatePaginationConfigTypeDef",
    "ListRobotsPaginateResponserobotsTypeDef",
    "ListRobotsPaginateResponseTypeDef",
    "ListRobotsPaginatefiltersTypeDef",
    "ListSimulationApplicationsPaginatePaginationConfigTypeDef",
    "ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef",
    "ListSimulationApplicationsPaginateResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef",
    "ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesTypeDef",
    "ListSimulationApplicationsPaginateResponseTypeDef",
    "ListSimulationApplicationsPaginatefiltersTypeDef",
    "ListSimulationJobsPaginatePaginationConfigTypeDef",
    "ListSimulationJobsPaginateResponsesimulationJobSummariesTypeDef",
    "ListSimulationJobsPaginateResponseTypeDef",
    "ListSimulationJobsPaginatefiltersTypeDef",
)


_ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef",
    {"s3Key": str, "etag": str},
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobsdataSources` `s3Keys`

    Information about S3 keys.

    - **s3Key** *(string) --*

      The S3 key.

    - **etag** *(string) --*

      The etag for the object.
    """


_ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List[
            ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef
        ],
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobs` `dataSources`

    Information about a data source.

    - **name** *(string) --*

      The name of the data source.

    - **s3Bucket** *(string) --*

      The S3 bucket where the data files are located.

    - **s3Keys** *(list) --*

      The list of S3 keys identifying the data source files.

      - *(dict) --*

        Information about S3 keys.

        - **s3Key** *(string) --*

          The S3 key.

        - **etag** *(string) --*

          The etag for the object.
    """


_ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobs` `loggingConfig`

    The logging configuration.

    - **recordAllRosTopics** *(boolean) --*

      A boolean indicating whether to record all ROS topics.
    """


_ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef",
    {"networkInterfaceId": str, "privateIpAddress": str, "publicIpAddress": str},
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobs` `networkInterface`

    Information about a network interface.

    - **networkInterfaceId** *(string) --*

      The ID of the network interface.

    - **privateIpAddress** *(string) --*

      The IPv4 address of the network interface within the subnet.

    - **publicIpAddress** *(string) --*

      The IPv4 public address of the network interface.
    """


_ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobs` `outputLocation`

    Location for output files generated by the simulation job.

    - **s3Bucket** *(string) --*

      The S3 bucket for output.

    - **s3Prefix** *(string) --*

      The S3 folder in the ``s3Bucket`` where output files will be placed.
    """


_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfig` `portMappings`

    An object representing a port mapping.

    - **jobPort** *(integer) --*

      The port number on the simulation job instance to use as a remote connection
      point.

    - **applicationPort** *(integer) --*

      The port number on the application.

    - **enableOnPublicIp** *(boolean) --*

      A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfig` `portForwardingConfig`

    The port forwarding configuration.

    - **portMappings** *(list) --*

      The port mappings for the configuration.

      - *(dict) --*

        An object representing a port mapping.

        - **jobPort** *(integer) --*

          The port number on the simulation job instance to use as a remote connection
          point.

        - **applicationPort** *(integer) --*

          The port number on the application.

        - **enableOnPublicIp** *(boolean) --*

          A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobsrobotApplications` `launchConfig`

    The launch configuration for the robot application.

    - **packageName** *(string) --*

      The package name.

    - **launchFile** *(string) --*

      The launch file name.

    - **environmentVariables** *(dict) --*

      The environment variables for the application launch.

      - *(string) --*

        - *(string) --*

    - **portForwardingConfig** *(dict) --*

      The port forwarding configuration.

      - **portMappings** *(list) --*

        The port mappings for the configuration.

        - *(dict) --*

          An object representing a port mapping.

          - **jobPort** *(integer) --*

            The port number on the simulation job instance to use as a remote connection
            point.

          - **applicationPort** *(integer) --*

            The port number on the application.

          - **enableOnPublicIp** *(boolean) --*

            A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobs` `robotApplications`

    Application configuration information for a robot.

    - **application** *(string) --*

      The application information for the robot application.

    - **applicationVersion** *(string) --*

      The version of the robot application.

    - **launchConfig** *(dict) --*

      The launch configuration for the robot application.

      - **packageName** *(string) --*

        The package name.

      - **launchFile** *(string) --*

        The launch file name.

      - **environmentVariables** *(dict) --*

        The environment variables for the application launch.

        - *(string) --*

          - *(string) --*

      - **portForwardingConfig** *(dict) --*

        The port forwarding configuration.

        - **portMappings** *(list) --*

          The port mappings for the configuration.

          - *(dict) --*

            An object representing a port mapping.

            - **jobPort** *(integer) --*

              The port number on the simulation job instance to use as a remote connection
              point.

            - **applicationPort** *(integer) --*

              The port number on the application.

            - **enableOnPublicIp** *(boolean) --*

              A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfig` `portMappings`

    An object representing a port mapping.

    - **jobPort** *(integer) --*

      The port number on the simulation job instance to use as a remote connection
      point.

    - **applicationPort** *(integer) --*

      The port number on the application.

    - **enableOnPublicIp** *(boolean) --*

      A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfig` `portForwardingConfig`

    The port forwarding configuration.

    - **portMappings** *(list) --*

      The port mappings for the configuration.

      - *(dict) --*

        An object representing a port mapping.

        - **jobPort** *(integer) --*

          The port number on the simulation job instance to use as a remote connection
          point.

        - **applicationPort** *(integer) --*

          The port number on the application.

        - **enableOnPublicIp** *(boolean) --*

          A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobssimulationApplications` `launchConfig`

    The launch configuration for the simulation application.

    - **packageName** *(string) --*

      The package name.

    - **launchFile** *(string) --*

      The launch file name.

    - **environmentVariables** *(dict) --*

      The environment variables for the application launch.

      - *(string) --*

        - *(string) --*

    - **portForwardingConfig** *(dict) --*

      The port forwarding configuration.

      - **portMappings** *(list) --*

        The port mappings for the configuration.

        - *(dict) --*

          An object representing a port mapping.

          - **jobPort** *(integer) --*

            The port number on the simulation job instance to use as a remote connection
            point.

          - **applicationPort** *(integer) --*

            The port number on the application.

          - **enableOnPublicIp** *(boolean) --*

            A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobs` `simulationApplications`

    Information about a simulation application configuration.

    - **application** *(string) --*

      The application information for the simulation application.

    - **applicationVersion** *(string) --*

      The version of the simulation application.

    - **launchConfig** *(dict) --*

      The launch configuration for the simulation application.

      - **packageName** *(string) --*

        The package name.

      - **launchFile** *(string) --*

        The launch file name.

      - **environmentVariables** *(dict) --*

        The environment variables for the application launch.

        - *(string) --*

          - *(string) --*

      - **portForwardingConfig** *(dict) --*

        The port forwarding configuration.

        - **portMappings** *(list) --*

          The port mappings for the configuration.

          - *(dict) --*

            An object representing a port mapping.

            - **jobPort** *(integer) --*

              The port number on the simulation job instance to use as a remote connection
              point.

            - **applicationPort** *(integer) --*

              The port number on the application.

            - **enableOnPublicIp** *(boolean) --*

              A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "vpcId": str,
        "assignPublicIp": bool,
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponsejobs` `vpcConfig`

    VPC configuration information.

    - **subnets** *(list) --*

      A list of subnet IDs associated with the simulation job.

      - *(string) --*

    - **securityGroups** *(list) --*

      A list of security group IDs associated with the simulation job.

      - *(string) --*

    - **vpcId** *(string) --*

      The VPC ID associated with your simulation job.

    - **assignPublicIp** *(boolean) --*

      A boolean indicating if a public IP was assigned.
    """


_ClientBatchDescribeSimulationJobResponsejobsTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsTypeDef",
    {
        "arn": str,
        "name": str,
        "status": str,
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": str,
        "failureCode": str,
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef,
        "loggingConfig": ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[
            ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef
        ],
        "simulationApplications": List[
            ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef
        ],
        "dataSources": List[
            ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef
        ],
        "tags": Dict[str, str],
        "vpcConfig": ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef,
        "networkInterface": ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef,
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJobResponse` `jobs`

    Information about a simulation job.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the simulation job.

    - **name** *(string) --*

      The name of the simulation job.

    - **status** *(string) --*

      Status of the simulation job.

    - **lastStartedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation job was last started.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation job was last updated.

    - **failureBehavior** *(string) --*

      The failure behavior the simulation job.

        Continue

      Restart the simulation job in the same host instance.

        Fail

      Stop the simulation job and terminate the instance.

    - **failureCode** *(string) --*

      The failure code of the simulation job if it failed.

    - **failureReason** *(string) --*

      The reason why the simulation job failed.

    - **clientRequestToken** *(string) --*

      A unique identifier for this ``SimulationJob`` request.

    - **outputLocation** *(dict) --*

      Location for output files generated by the simulation job.

      - **s3Bucket** *(string) --*

        The S3 bucket for output.

      - **s3Prefix** *(string) --*

        The S3 folder in the ``s3Bucket`` where output files will be placed.

    - **loggingConfig** *(dict) --*

      The logging configuration.

      - **recordAllRosTopics** *(boolean) --*

        A boolean indicating whether to record all ROS topics.

    - **maxJobDurationInSeconds** *(integer) --*

      The maximum simulation job duration in seconds. The value must be 8 days (691,200
      seconds) or less.

    - **simulationTimeMillis** *(integer) --*

      The simulation job execution duration in milliseconds.

    - **iamRole** *(string) --*

      The IAM role that allows the simulation instance to call the AWS APIs that are specified
      in its associated policies on your behalf. This is how credentials are passed in to your
      simulation job.

    - **robotApplications** *(list) --*

      A list of robot applications.

      - *(dict) --*

        Application configuration information for a robot.

        - **application** *(string) --*

          The application information for the robot application.

        - **applicationVersion** *(string) --*

          The version of the robot application.

        - **launchConfig** *(dict) --*

          The launch configuration for the robot application.

          - **packageName** *(string) --*

            The package name.

          - **launchFile** *(string) --*

            The launch file name.

          - **environmentVariables** *(dict) --*

            The environment variables for the application launch.

            - *(string) --*

              - *(string) --*

          - **portForwardingConfig** *(dict) --*

            The port forwarding configuration.

            - **portMappings** *(list) --*

              The port mappings for the configuration.

              - *(dict) --*

                An object representing a port mapping.

                - **jobPort** *(integer) --*

                  The port number on the simulation job instance to use as a remote connection
                  point.

                - **applicationPort** *(integer) --*

                  The port number on the application.

                - **enableOnPublicIp** *(boolean) --*

                  A Boolean indicating whether to enable this port mapping on public IP.

    - **simulationApplications** *(list) --*

      A list of simulation applications.

      - *(dict) --*

        Information about a simulation application configuration.

        - **application** *(string) --*

          The application information for the simulation application.

        - **applicationVersion** *(string) --*

          The version of the simulation application.

        - **launchConfig** *(dict) --*

          The launch configuration for the simulation application.

          - **packageName** *(string) --*

            The package name.

          - **launchFile** *(string) --*

            The launch file name.

          - **environmentVariables** *(dict) --*

            The environment variables for the application launch.

            - *(string) --*

              - *(string) --*

          - **portForwardingConfig** *(dict) --*

            The port forwarding configuration.

            - **portMappings** *(list) --*

              The port mappings for the configuration.

              - *(dict) --*

                An object representing a port mapping.

                - **jobPort** *(integer) --*

                  The port number on the simulation job instance to use as a remote connection
                  point.

                - **applicationPort** *(integer) --*

                  The port number on the application.

                - **enableOnPublicIp** *(boolean) --*

                  A Boolean indicating whether to enable this port mapping on public IP.

    - **dataSources** *(list) --*

      The data sources for the simulation job.

      - *(dict) --*

        Information about a data source.

        - **name** *(string) --*

          The name of the data source.

        - **s3Bucket** *(string) --*

          The S3 bucket where the data files are located.

        - **s3Keys** *(list) --*

          The list of S3 keys identifying the data source files.

          - *(dict) --*

            Information about S3 keys.

            - **s3Key** *(string) --*

              The S3 key.

            - **etag** *(string) --*

              The etag for the object.

    - **tags** *(dict) --*

      A map that contains tag keys and tag values that are attached to the simulation job.

      - *(string) --*

        - *(string) --*

    - **vpcConfig** *(dict) --*

      VPC configuration information.

      - **subnets** *(list) --*

        A list of subnet IDs associated with the simulation job.

        - *(string) --*

      - **securityGroups** *(list) --*

        A list of security group IDs associated with the simulation job.

        - *(string) --*

      - **vpcId** *(string) --*

        The VPC ID associated with your simulation job.

      - **assignPublicIp** *(boolean) --*

        A boolean indicating if a public IP was assigned.

    - **networkInterface** *(dict) --*

      Information about a network interface.

      - **networkInterfaceId** *(string) --*

        The ID of the network interface.

      - **privateIpAddress** *(string) --*

        The IPv4 address of the network interface within the subnet.

      - **publicIpAddress** *(string) --*

        The IPv4 public address of the network interface.
    """


_ClientBatchDescribeSimulationJobResponseTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponseTypeDef",
    {
        "jobs": List[ClientBatchDescribeSimulationJobResponsejobsTypeDef],
        "unprocessedJobs": List[str],
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponseTypeDef(
    _ClientBatchDescribeSimulationJobResponseTypeDef
):
    """
    Type definition for `ClientBatchDescribeSimulationJob` `Response`

    - **jobs** *(list) --*

      A list of simulation jobs.

      - *(dict) --*

        Information about a simulation job.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the simulation job.

        - **name** *(string) --*

          The name of the simulation job.

        - **status** *(string) --*

          Status of the simulation job.

        - **lastStartedAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the simulation job was last started.

        - **lastUpdatedAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the simulation job was last updated.

        - **failureBehavior** *(string) --*

          The failure behavior the simulation job.

            Continue

          Restart the simulation job in the same host instance.

            Fail

          Stop the simulation job and terminate the instance.

        - **failureCode** *(string) --*

          The failure code of the simulation job if it failed.

        - **failureReason** *(string) --*

          The reason why the simulation job failed.

        - **clientRequestToken** *(string) --*

          A unique identifier for this ``SimulationJob`` request.

        - **outputLocation** *(dict) --*

          Location for output files generated by the simulation job.

          - **s3Bucket** *(string) --*

            The S3 bucket for output.

          - **s3Prefix** *(string) --*

            The S3 folder in the ``s3Bucket`` where output files will be placed.

        - **loggingConfig** *(dict) --*

          The logging configuration.

          - **recordAllRosTopics** *(boolean) --*

            A boolean indicating whether to record all ROS topics.

        - **maxJobDurationInSeconds** *(integer) --*

          The maximum simulation job duration in seconds. The value must be 8 days (691,200
          seconds) or less.

        - **simulationTimeMillis** *(integer) --*

          The simulation job execution duration in milliseconds.

        - **iamRole** *(string) --*

          The IAM role that allows the simulation instance to call the AWS APIs that are specified
          in its associated policies on your behalf. This is how credentials are passed in to your
          simulation job.

        - **robotApplications** *(list) --*

          A list of robot applications.

          - *(dict) --*

            Application configuration information for a robot.

            - **application** *(string) --*

              The application information for the robot application.

            - **applicationVersion** *(string) --*

              The version of the robot application.

            - **launchConfig** *(dict) --*

              The launch configuration for the robot application.

              - **packageName** *(string) --*

                The package name.

              - **launchFile** *(string) --*

                The launch file name.

              - **environmentVariables** *(dict) --*

                The environment variables for the application launch.

                - *(string) --*

                  - *(string) --*

              - **portForwardingConfig** *(dict) --*

                The port forwarding configuration.

                - **portMappings** *(list) --*

                  The port mappings for the configuration.

                  - *(dict) --*

                    An object representing a port mapping.

                    - **jobPort** *(integer) --*

                      The port number on the simulation job instance to use as a remote connection
                      point.

                    - **applicationPort** *(integer) --*

                      The port number on the application.

                    - **enableOnPublicIp** *(boolean) --*

                      A Boolean indicating whether to enable this port mapping on public IP.

        - **simulationApplications** *(list) --*

          A list of simulation applications.

          - *(dict) --*

            Information about a simulation application configuration.

            - **application** *(string) --*

              The application information for the simulation application.

            - **applicationVersion** *(string) --*

              The version of the simulation application.

            - **launchConfig** *(dict) --*

              The launch configuration for the simulation application.

              - **packageName** *(string) --*

                The package name.

              - **launchFile** *(string) --*

                The launch file name.

              - **environmentVariables** *(dict) --*

                The environment variables for the application launch.

                - *(string) --*

                  - *(string) --*

              - **portForwardingConfig** *(dict) --*

                The port forwarding configuration.

                - **portMappings** *(list) --*

                  The port mappings for the configuration.

                  - *(dict) --*

                    An object representing a port mapping.

                    - **jobPort** *(integer) --*

                      The port number on the simulation job instance to use as a remote connection
                      point.

                    - **applicationPort** *(integer) --*

                      The port number on the application.

                    - **enableOnPublicIp** *(boolean) --*

                      A Boolean indicating whether to enable this port mapping on public IP.

        - **dataSources** *(list) --*

          The data sources for the simulation job.

          - *(dict) --*

            Information about a data source.

            - **name** *(string) --*

              The name of the data source.

            - **s3Bucket** *(string) --*

              The S3 bucket where the data files are located.

            - **s3Keys** *(list) --*

              The list of S3 keys identifying the data source files.

              - *(dict) --*

                Information about S3 keys.

                - **s3Key** *(string) --*

                  The S3 key.

                - **etag** *(string) --*

                  The etag for the object.

        - **tags** *(dict) --*

          A map that contains tag keys and tag values that are attached to the simulation job.

          - *(string) --*

            - *(string) --*

        - **vpcConfig** *(dict) --*

          VPC configuration information.

          - **subnets** *(list) --*

            A list of subnet IDs associated with the simulation job.

            - *(string) --*

          - **securityGroups** *(list) --*

            A list of security group IDs associated with the simulation job.

            - *(string) --*

          - **vpcId** *(string) --*

            The VPC ID associated with your simulation job.

          - **assignPublicIp** *(boolean) --*

            A boolean indicating if a public IP was assigned.

        - **networkInterface** *(dict) --*

          Information about a network interface.

          - **networkInterfaceId** *(string) --*

            The ID of the network interface.

          - **privateIpAddress** *(string) --*

            The IPv4 address of the network interface within the subnet.

          - **publicIpAddress** *(string) --*

            The IPv4 public address of the network interface.

    - **unprocessedJobs** *(list) --*

      A list of unprocessed simulation job Amazon Resource Names (ARNs).

      - *(string) --*
    """


_ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "_ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)


class ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef(
    _ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef
):
    """
    Type definition for `ClientCreateDeploymentJobResponsedeploymentApplicationConfigs` `launchConfig`

    The launch configuration.

    - **packageName** *(string) --*

      The package name.

    - **preLaunchFile** *(string) --*

      The deployment pre-launch file. This file will be executed prior to the launch file.

    - **launchFile** *(string) --*

      The launch file name.

    - **postLaunchFile** *(string) --*

      The deployment post-launch file. This file will be executed after the launch file.

    - **environmentVariables** *(dict) --*

      An array of key/value pairs specifying environment variables for the robot application

      - *(string) --*

        - *(string) --*
    """


_ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef = TypedDict(
    "_ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef(
    _ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef
):
    """
    Type definition for `ClientCreateDeploymentJobResponse` `deploymentApplicationConfigs`

    Information about a deployment application configuration.

    - **application** *(string) --*

      The Amazon Resource Name (ARN) of the robot application.

    - **applicationVersion** *(string) --*

      The version of the application.

    - **launchConfig** *(dict) --*

      The launch configuration.

      - **packageName** *(string) --*

        The package name.

      - **preLaunchFile** *(string) --*

        The deployment pre-launch file. This file will be executed prior to the launch file.

      - **launchFile** *(string) --*

        The launch file name.

      - **postLaunchFile** *(string) --*

        The deployment post-launch file. This file will be executed after the launch file.

      - **environmentVariables** *(dict) --*

        An array of key/value pairs specifying environment variables for the robot application

        - *(string) --*

          - *(string) --*
    """


_ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "_ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)


class ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef(
    _ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef
):
    """
    Type definition for `ClientCreateDeploymentJobResponsedeploymentConfig` `downloadConditionFile`

    The download condition file.

    - **bucket** *(string) --*

      The bucket containing the object.

    - **key** *(string) --*

      The key of the object.

    - **etag** *(string) --*

      The etag of the object.
    """


_ClientCreateDeploymentJobResponsedeploymentConfigTypeDef = TypedDict(
    "_ClientCreateDeploymentJobResponsedeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentJobResponsedeploymentConfigTypeDef(
    _ClientCreateDeploymentJobResponsedeploymentConfigTypeDef
):
    """
    Type definition for `ClientCreateDeploymentJobResponse` `deploymentConfig`

    The deployment configuration.

    - **concurrentDeploymentPercentage** *(integer) --*

      The percentage of robots receiving the deployment at the same time.

    - **failureThresholdPercentage** *(integer) --*

      The percentage of deployments that need to fail before stopping deployment.

    - **robotDeploymentTimeoutInSeconds** *(integer) --*

      The amount of time, in seconds, to wait for deployment to a single robot to complete.
      Choose a time between 1 minute and 7 days. The default is 5 hours.

    - **downloadConditionFile** *(dict) --*

      The download condition file.

      - **bucket** *(string) --*

        The bucket containing the object.

      - **key** *(string) --*

        The key of the object.

      - **etag** *(string) --*

        The etag of the object.
    """


_ClientCreateDeploymentJobResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": str,
        "deploymentApplicationConfigs": List[
            ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef
        ],
        "failureReason": str,
        "failureCode": str,
        "createdAt": datetime,
        "deploymentConfig": ClientCreateDeploymentJobResponsedeploymentConfigTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateDeploymentJobResponseTypeDef(
    _ClientCreateDeploymentJobResponseTypeDef
):
    """
    Type definition for `ClientCreateDeploymentJob` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the deployment job.

    - **fleet** *(string) --*

      The target fleet for the deployment job.

    - **status** *(string) --*

      The status of the deployment job.

    - **deploymentApplicationConfigs** *(list) --*

      The deployment application configuration.

      - *(dict) --*

        Information about a deployment application configuration.

        - **application** *(string) --*

          The Amazon Resource Name (ARN) of the robot application.

        - **applicationVersion** *(string) --*

          The version of the application.

        - **launchConfig** *(dict) --*

          The launch configuration.

          - **packageName** *(string) --*

            The package name.

          - **preLaunchFile** *(string) --*

            The deployment pre-launch file. This file will be executed prior to the launch file.

          - **launchFile** *(string) --*

            The launch file name.

          - **postLaunchFile** *(string) --*

            The deployment post-launch file. This file will be executed after the launch file.

          - **environmentVariables** *(dict) --*

            An array of key/value pairs specifying environment variables for the robot application

            - *(string) --*

              - *(string) --*

    - **failureReason** *(string) --*

      The failure reason of the deployment job if it failed.

    - **failureCode** *(string) --*

      The failure code of the simulation job if it failed:

        BadPermissionError

      AWS Greengrass requires a service-level role permission to access other services. The role
      must include the ` ``AWSGreengrassResourceAccessRolePolicy`` managed policy
      <https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSGreengrassResourceAccessRolePolicy$jsonEditor>`__
      .

        ExtractingBundleFailure

      The robot application could not be extracted from the bundle.

        FailureThresholdBreached

      The percentage of robots that could not be updated exceeded the percentage set for the
      deployment.

        GreengrassDeploymentFailed

      The robot application could not be deployed to the robot.

        GreengrassGroupVersionDoesNotExist

      The AWS Greengrass group or version associated with a robot is missing.

        InternalServerError

      An internal error has occurred. Retry your request, but if the problem persists, contact us
      with details.

        MissingRobotApplicationArchitecture

      The robot application does not have a source that matches the architecture of the robot.

        MissingRobotDeploymentResource

      One or more of the resources specified for the robot application are missing. For example,
      does the robot application have the correct launch package and launch file?

        PostLaunchFileFailure

      The post-launch script failed.

        PreLaunchFileFailure

      The pre-launch script failed.

        ResourceNotFound

      One or more deployment resources are missing. For example, do robot application source
      bundles still exist?

        RobotDeploymentNoResponse

      There is no response from the robot. It might not be powered on or connected to the internet.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the fleet was created.

    - **deploymentConfig** *(dict) --*

      The deployment configuration.

      - **concurrentDeploymentPercentage** *(integer) --*

        The percentage of robots receiving the deployment at the same time.

      - **failureThresholdPercentage** *(integer) --*

        The percentage of deployments that need to fail before stopping deployment.

      - **robotDeploymentTimeoutInSeconds** *(integer) --*

        The amount of time, in seconds, to wait for deployment to a single robot to complete.
        Choose a time between 1 minute and 7 days. The default is 5 hours.

      - **downloadConditionFile** *(dict) --*

        The download condition file.

        - **bucket** *(string) --*

          The bucket containing the object.

        - **key** *(string) --*

          The key of the object.

        - **etag** *(string) --*

          The etag of the object.

    - **tags** *(dict) --*

      The list of all tags added to the deployment job.

      - *(string) --*

        - *(string) --*
    """


_RequiredClientCreateDeploymentJobdeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "_RequiredClientCreateDeploymentJobdeploymentApplicationConfigslaunchConfigTypeDef",
    {"packageName": str, "launchFile": str},
)
_OptionalClientCreateDeploymentJobdeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "_OptionalClientCreateDeploymentJobdeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "preLaunchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)


class ClientCreateDeploymentJobdeploymentApplicationConfigslaunchConfigTypeDef(
    _RequiredClientCreateDeploymentJobdeploymentApplicationConfigslaunchConfigTypeDef,
    _OptionalClientCreateDeploymentJobdeploymentApplicationConfigslaunchConfigTypeDef,
):
    """
    Type definition for `ClientCreateDeploymentJobdeploymentApplicationConfigs` `launchConfig`

    The launch configuration.

    - **packageName** *(string) --* **[REQUIRED]**

      The package name.

    - **preLaunchFile** *(string) --*

      The deployment pre-launch file. This file will be executed prior to the launch file.

    - **launchFile** *(string) --* **[REQUIRED]**

      The launch file name.

    - **postLaunchFile** *(string) --*

      The deployment post-launch file. This file will be executed after the launch file.

    - **environmentVariables** *(dict) --*

      An array of key/value pairs specifying environment variables for the robot application

      - *(string) --*

        - *(string) --*
    """


_ClientCreateDeploymentJobdeploymentApplicationConfigsTypeDef = TypedDict(
    "_ClientCreateDeploymentJobdeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientCreateDeploymentJobdeploymentApplicationConfigslaunchConfigTypeDef,
    },
)


class ClientCreateDeploymentJobdeploymentApplicationConfigsTypeDef(
    _ClientCreateDeploymentJobdeploymentApplicationConfigsTypeDef
):
    """
    Type definition for `ClientCreateDeploymentJob` `deploymentApplicationConfigs`

    Information about a deployment application configuration.

    - **application** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the robot application.

    - **applicationVersion** *(string) --* **[REQUIRED]**

      The version of the application.

    - **launchConfig** *(dict) --* **[REQUIRED]**

      The launch configuration.

      - **packageName** *(string) --* **[REQUIRED]**

        The package name.

      - **preLaunchFile** *(string) --*

        The deployment pre-launch file. This file will be executed prior to the launch file.

      - **launchFile** *(string) --* **[REQUIRED]**

        The launch file name.

      - **postLaunchFile** *(string) --*

        The deployment post-launch file. This file will be executed after the launch file.

      - **environmentVariables** *(dict) --*

        An array of key/value pairs specifying environment variables for the robot application

        - *(string) --*

          - *(string) --*
    """


_RequiredClientCreateDeploymentJobdeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "_RequiredClientCreateDeploymentJobdeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str},
)
_OptionalClientCreateDeploymentJobdeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "_OptionalClientCreateDeploymentJobdeploymentConfigdownloadConditionFileTypeDef",
    {"etag": str},
    total=False,
)


class ClientCreateDeploymentJobdeploymentConfigdownloadConditionFileTypeDef(
    _RequiredClientCreateDeploymentJobdeploymentConfigdownloadConditionFileTypeDef,
    _OptionalClientCreateDeploymentJobdeploymentConfigdownloadConditionFileTypeDef,
):
    """
    Type definition for `ClientCreateDeploymentJobdeploymentConfig` `downloadConditionFile`

    The download condition file.

    - **bucket** *(string) --* **[REQUIRED]**

      The bucket containing the object.

    - **key** *(string) --* **[REQUIRED]**

      The key of the object.

    - **etag** *(string) --*

      The etag of the object.
    """


_ClientCreateDeploymentJobdeploymentConfigTypeDef = TypedDict(
    "_ClientCreateDeploymentJobdeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientCreateDeploymentJobdeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentJobdeploymentConfigTypeDef(
    _ClientCreateDeploymentJobdeploymentConfigTypeDef
):
    """
    Type definition for `ClientCreateDeploymentJob` `deploymentConfig`

    The requested deployment configuration.

    - **concurrentDeploymentPercentage** *(integer) --*

      The percentage of robots receiving the deployment at the same time.

    - **failureThresholdPercentage** *(integer) --*

      The percentage of deployments that need to fail before stopping deployment.

    - **robotDeploymentTimeoutInSeconds** *(integer) --*

      The amount of time, in seconds, to wait for deployment to a single robot to complete. Choose a
      time between 1 minute and 7 days. The default is 5 hours.

    - **downloadConditionFile** *(dict) --*

      The download condition file.

      - **bucket** *(string) --* **[REQUIRED]**

        The bucket containing the object.

      - **key** *(string) --* **[REQUIRED]**

        The key of the object.

      - **etag** *(string) --*

        The etag of the object.
    """


_ClientCreateFleetResponseTypeDef = TypedDict(
    "_ClientCreateFleetResponseTypeDef",
    {"arn": str, "name": str, "createdAt": datetime, "tags": Dict[str, str]},
    total=False,
)


class ClientCreateFleetResponseTypeDef(_ClientCreateFleetResponseTypeDef):
    """
    Type definition for `ClientCreateFleet` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the fleet.

    - **name** *(string) --*

      The name of the fleet.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the fleet was created.

    - **tags** *(dict) --*

      The list of all tags added to the fleet.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef(
    _ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientCreateRobotApplicationResponse` `robotSoftwareSuite`

    The robot software suite used by the robot application.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientCreateRobotApplicationResponsesourcesTypeDef = TypedDict(
    "_ClientCreateRobotApplicationResponsesourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "etag": str, "architecture": str},
    total=False,
)


class ClientCreateRobotApplicationResponsesourcesTypeDef(
    _ClientCreateRobotApplicationResponsesourcesTypeDef
):
    """
    Type definition for `ClientCreateRobotApplicationResponse` `sources`

    Information about a source.

    - **s3Bucket** *(string) --*

      The s3 bucket name.

    - **s3Key** *(string) --*

      The s3 object key.

    - **etag** *(string) --*

      A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

    - **architecture** *(string) --*

      The taget processor architecture for the application.
    """


_ClientCreateRobotApplicationResponseTypeDef = TypedDict(
    "_ClientCreateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientCreateRobotApplicationResponsesourcesTypeDef],
        "robotSoftwareSuite": ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateRobotApplicationResponseTypeDef(
    _ClientCreateRobotApplicationResponseTypeDef
):
    """
    Type definition for `ClientCreateRobotApplication` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the robot application.

    - **name** *(string) --*

      The name of the robot application.

    - **version** *(string) --*

      The version of the robot application.

    - **sources** *(list) --*

      The sources of the robot application.

      - *(dict) --*

        Information about a source.

        - **s3Bucket** *(string) --*

          The s3 bucket name.

        - **s3Key** *(string) --*

          The s3 object key.

        - **etag** *(string) --*

          A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

        - **architecture** *(string) --*

          The taget processor architecture for the application.

    - **robotSoftwareSuite** *(dict) --*

      The robot software suite used by the robot application.

      - **name** *(string) --*

        The name of the robot software suite.

      - **version** *(string) --*

        The version of the robot software suite.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the robot application was last updated.

    - **revisionId** *(string) --*

      The revision id of the robot application.

    - **tags** *(dict) --*

      The list of all tags added to the robot application.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef(
    _ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientCreateRobotApplicationVersionResponse` `robotSoftwareSuite`

    The robot software suite used by the robot application.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientCreateRobotApplicationVersionResponsesourcesTypeDef = TypedDict(
    "_ClientCreateRobotApplicationVersionResponsesourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "etag": str, "architecture": str},
    total=False,
)


class ClientCreateRobotApplicationVersionResponsesourcesTypeDef(
    _ClientCreateRobotApplicationVersionResponsesourcesTypeDef
):
    """
    Type definition for `ClientCreateRobotApplicationVersionResponse` `sources`

    Information about a source.

    - **s3Bucket** *(string) --*

      The s3 bucket name.

    - **s3Key** *(string) --*

      The s3 object key.

    - **etag** *(string) --*

      A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

    - **architecture** *(string) --*

      The taget processor architecture for the application.
    """


_ClientCreateRobotApplicationVersionResponseTypeDef = TypedDict(
    "_ClientCreateRobotApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientCreateRobotApplicationVersionResponsesourcesTypeDef],
        "robotSoftwareSuite": ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)


class ClientCreateRobotApplicationVersionResponseTypeDef(
    _ClientCreateRobotApplicationVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateRobotApplicationVersion` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the robot application.

    - **name** *(string) --*

      The name of the robot application.

    - **version** *(string) --*

      The version of the robot application.

    - **sources** *(list) --*

      The sources of the robot application.

      - *(dict) --*

        Information about a source.

        - **s3Bucket** *(string) --*

          The s3 bucket name.

        - **s3Key** *(string) --*

          The s3 object key.

        - **etag** *(string) --*

          A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

        - **architecture** *(string) --*

          The taget processor architecture for the application.

    - **robotSoftwareSuite** *(dict) --*

      The robot software suite used by the robot application.

      - **name** *(string) --*

        The name of the robot software suite.

      - **version** *(string) --*

        The version of the robot software suite.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the robot application was last updated.

    - **revisionId** *(string) --*

      The revision id of the robot application.
    """


_ClientCreateRobotApplicationrobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateRobotApplicationrobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateRobotApplicationrobotSoftwareSuiteTypeDef(
    _ClientCreateRobotApplicationrobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientCreateRobotApplication` `robotSoftwareSuite`

    The robot software suite used by the robot application.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientCreateRobotApplicationsourcesTypeDef = TypedDict(
    "_ClientCreateRobotApplicationsourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": str},
    total=False,
)


class ClientCreateRobotApplicationsourcesTypeDef(
    _ClientCreateRobotApplicationsourcesTypeDef
):
    """
    Type definition for `ClientCreateRobotApplication` `sources`

    Information about a source configuration.

    - **s3Bucket** *(string) --*

      The Amazon S3 bucket name.

    - **s3Key** *(string) --*

      The s3 object key.

    - **architecture** *(string) --*

      The target processor architecture for the application.
    """


_ClientCreateRobotResponseTypeDef = TypedDict(
    "_ClientCreateRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "greengrassGroupId": str,
        "architecture": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateRobotResponseTypeDef(_ClientCreateRobotResponseTypeDef):
    """
    Type definition for `ClientCreateRobot` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the robot.

    - **name** *(string) --*

      The name of the robot.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the robot was created.

    - **greengrassGroupId** *(string) --*

      The Amazon Resource Name (ARN) of the Greengrass group associated with the robot.

    - **architecture** *(string) --*

      The target architecture of the robot.

    - **tags** *(dict) --*

      The list of all tags added to the robot.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateSimulationApplicationResponserenderingEngineTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationResponserenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateSimulationApplicationResponserenderingEngineTypeDef(
    _ClientCreateSimulationApplicationResponserenderingEngineTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplicationResponse` `renderingEngine`

    The rendering engine for the simulation application.

    - **name** *(string) --*

      The name of the rendering engine.

    - **version** *(string) --*

      The version of the rendering engine.
    """


_ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef(
    _ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplicationResponse` `robotSoftwareSuite`

    Information about the robot software suite.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef(
    _ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplicationResponse` `simulationSoftwareSuite`

    The simulation software suite used by the simulation application.

    - **name** *(string) --*

      The name of the simulation software suite.

    - **version** *(string) --*

      The version of the simulation software suite.
    """


_ClientCreateSimulationApplicationResponsesourcesTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationResponsesourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "etag": str, "architecture": str},
    total=False,
)


class ClientCreateSimulationApplicationResponsesourcesTypeDef(
    _ClientCreateSimulationApplicationResponsesourcesTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplicationResponse` `sources`

    Information about a source.

    - **s3Bucket** *(string) --*

      The s3 bucket name.

    - **s3Key** *(string) --*

      The s3 object key.

    - **etag** *(string) --*

      A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

    - **architecture** *(string) --*

      The taget processor architecture for the application.
    """


_ClientCreateSimulationApplicationResponseTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientCreateSimulationApplicationResponsesourcesTypeDef],
        "simulationSoftwareSuite": ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef,
        "renderingEngine": ClientCreateSimulationApplicationResponserenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateSimulationApplicationResponseTypeDef(
    _ClientCreateSimulationApplicationResponseTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplication` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the simulation application.

    - **name** *(string) --*

      The name of the simulation application.

    - **version** *(string) --*

      The version of the simulation application.

    - **sources** *(list) --*

      The sources of the simulation application.

      - *(dict) --*

        Information about a source.

        - **s3Bucket** *(string) --*

          The s3 bucket name.

        - **s3Key** *(string) --*

          The s3 object key.

        - **etag** *(string) --*

          A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

        - **architecture** *(string) --*

          The taget processor architecture for the application.

    - **simulationSoftwareSuite** *(dict) --*

      The simulation software suite used by the simulation application.

      - **name** *(string) --*

        The name of the simulation software suite.

      - **version** *(string) --*

        The version of the simulation software suite.

    - **robotSoftwareSuite** *(dict) --*

      Information about the robot software suite.

      - **name** *(string) --*

        The name of the robot software suite.

      - **version** *(string) --*

        The version of the robot software suite.

    - **renderingEngine** *(dict) --*

      The rendering engine for the simulation application.

      - **name** *(string) --*

        The name of the rendering engine.

      - **version** *(string) --*

        The version of the rendering engine.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation application was last updated.

    - **revisionId** *(string) --*

      The revision id of the simulation application.

    - **tags** *(dict) --*

      The list of all tags added to the simulation application.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef(
    _ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplicationVersionResponse` `renderingEngine`

    The rendering engine for the simulation application.

    - **name** *(string) --*

      The name of the rendering engine.

    - **version** *(string) --*

      The version of the rendering engine.
    """


_ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef(
    _ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplicationVersionResponse` `robotSoftwareSuite`

    Information about the robot software suite.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef(
    _ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplicationVersionResponse` `simulationSoftwareSuite`

    The simulation software suite used by the simulation application.

    - **name** *(string) --*

      The name of the simulation software suite.

    - **version** *(string) --*

      The version of the simulation software suite.
    """


_ClientCreateSimulationApplicationVersionResponsesourcesTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationVersionResponsesourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "etag": str, "architecture": str},
    total=False,
)


class ClientCreateSimulationApplicationVersionResponsesourcesTypeDef(
    _ClientCreateSimulationApplicationVersionResponsesourcesTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplicationVersionResponse` `sources`

    Information about a source.

    - **s3Bucket** *(string) --*

      The s3 bucket name.

    - **s3Key** *(string) --*

      The s3 object key.

    - **etag** *(string) --*

      A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

    - **architecture** *(string) --*

      The taget processor architecture for the application.
    """


_ClientCreateSimulationApplicationVersionResponseTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientCreateSimulationApplicationVersionResponsesourcesTypeDef],
        "simulationSoftwareSuite": ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef,
        "renderingEngine": ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)


class ClientCreateSimulationApplicationVersionResponseTypeDef(
    _ClientCreateSimulationApplicationVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplicationVersion` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the simulation application.

    - **name** *(string) --*

      The name of the simulation application.

    - **version** *(string) --*

      The version of the simulation application.

    - **sources** *(list) --*

      The sources of the simulation application.

      - *(dict) --*

        Information about a source.

        - **s3Bucket** *(string) --*

          The s3 bucket name.

        - **s3Key** *(string) --*

          The s3 object key.

        - **etag** *(string) --*

          A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

        - **architecture** *(string) --*

          The taget processor architecture for the application.

    - **simulationSoftwareSuite** *(dict) --*

      The simulation software suite used by the simulation application.

      - **name** *(string) --*

        The name of the simulation software suite.

      - **version** *(string) --*

        The version of the simulation software suite.

    - **robotSoftwareSuite** *(dict) --*

      Information about the robot software suite.

      - **name** *(string) --*

        The name of the robot software suite.

      - **version** *(string) --*

        The version of the robot software suite.

    - **renderingEngine** *(dict) --*

      The rendering engine for the simulation application.

      - **name** *(string) --*

        The name of the rendering engine.

      - **version** *(string) --*

        The version of the rendering engine.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation application was last updated.

    - **revisionId** *(string) --*

      The revision ID of the simulation application.
    """


_ClientCreateSimulationApplicationrenderingEngineTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationrenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateSimulationApplicationrenderingEngineTypeDef(
    _ClientCreateSimulationApplicationrenderingEngineTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplication` `renderingEngine`

    The rendering engine for the simulation application.

    - **name** *(string) --*

      The name of the rendering engine.

    - **version** *(string) --*

      The version of the rendering engine.
    """


_ClientCreateSimulationApplicationrobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationrobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateSimulationApplicationrobotSoftwareSuiteTypeDef(
    _ClientCreateSimulationApplicationrobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplication` `robotSoftwareSuite`

    The robot software suite of the simulation application.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientCreateSimulationApplicationsimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationsimulationSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateSimulationApplicationsimulationSoftwareSuiteTypeDef(
    _ClientCreateSimulationApplicationsimulationSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplication` `simulationSoftwareSuite`

    The simulation software suite used by the simulation application.

    - **name** *(string) --*

      The name of the simulation software suite.

    - **version** *(string) --*

      The version of the simulation software suite.
    """


_ClientCreateSimulationApplicationsourcesTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationsourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": str},
    total=False,
)


class ClientCreateSimulationApplicationsourcesTypeDef(
    _ClientCreateSimulationApplicationsourcesTypeDef
):
    """
    Type definition for `ClientCreateSimulationApplication` `sources`

    Information about a source configuration.

    - **s3Bucket** *(string) --*

      The Amazon S3 bucket name.

    - **s3Key** *(string) --*

      The s3 object key.

    - **architecture** *(string) --*

      The target processor architecture for the application.
    """


_ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef",
    {"s3Key": str, "etag": str},
    total=False,
)


class ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef(
    _ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobResponsedataSources` `s3Keys`

    Information about S3 keys.

    - **s3Key** *(string) --*

      The S3 key.

    - **etag** *(string) --*

      The etag for the object.
    """


_ClientCreateSimulationJobResponsedataSourcesTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsedataSourcesTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List[ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef],
    },
    total=False,
)


class ClientCreateSimulationJobResponsedataSourcesTypeDef(
    _ClientCreateSimulationJobResponsedataSourcesTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobResponse` `dataSources`

    Information about a data source.

    - **name** *(string) --*

      The name of the data source.

    - **s3Bucket** *(string) --*

      The S3 bucket where the data files are located.

    - **s3Keys** *(list) --*

      The list of S3 keys identifying the data source files.

      - *(dict) --*

        Information about S3 keys.

        - **s3Key** *(string) --*

          The S3 key.

        - **etag** *(string) --*

          The etag for the object.
    """


_ClientCreateSimulationJobResponseloggingConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponseloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)


class ClientCreateSimulationJobResponseloggingConfigTypeDef(
    _ClientCreateSimulationJobResponseloggingConfigTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobResponse` `loggingConfig`

    The logging configuration.

    - **recordAllRosTopics** *(boolean) --*

      A boolean indicating whether to record all ROS topics.
    """


_ClientCreateSimulationJobResponseoutputLocationTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponseoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)


class ClientCreateSimulationJobResponseoutputLocationTypeDef(
    _ClientCreateSimulationJobResponseoutputLocationTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobResponse` `outputLocation`

    Simulation job output files location.

    - **s3Bucket** *(string) --*

      The S3 bucket for output.

    - **s3Prefix** *(string) --*

      The S3 folder in the ``s3Bucket`` where output files will be placed.
    """


_ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfig` `portMappings`

    An object representing a port mapping.

    - **jobPort** *(integer) --*

      The port number on the simulation job instance to use as a remote connection
      point.

    - **applicationPort** *(integer) --*

      The port number on the application.

    - **enableOnPublicIp** *(boolean) --*

      A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobResponserobotApplicationslaunchConfig` `portForwardingConfig`

    The port forwarding configuration.

    - **portMappings** *(list) --*

      The port mappings for the configuration.

      - *(dict) --*

        An object representing a port mapping.

        - **jobPort** *(integer) --*

          The port number on the simulation job instance to use as a remote connection
          point.

        - **applicationPort** *(integer) --*

          The port number on the application.

        - **enableOnPublicIp** *(boolean) --*

          A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef(
    _ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobResponserobotApplications` `launchConfig`

    The launch configuration for the robot application.

    - **packageName** *(string) --*

      The package name.

    - **launchFile** *(string) --*

      The launch file name.

    - **environmentVariables** *(dict) --*

      The environment variables for the application launch.

      - *(string) --*

        - *(string) --*

    - **portForwardingConfig** *(dict) --*

      The port forwarding configuration.

      - **portMappings** *(list) --*

        The port mappings for the configuration.

        - *(dict) --*

          An object representing a port mapping.

          - **jobPort** *(integer) --*

            The port number on the simulation job instance to use as a remote connection
            point.

          - **applicationPort** *(integer) --*

            The port number on the application.

          - **enableOnPublicIp** *(boolean) --*

            A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientCreateSimulationJobResponserobotApplicationsTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponserobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobResponserobotApplicationsTypeDef(
    _ClientCreateSimulationJobResponserobotApplicationsTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobResponse` `robotApplications`

    Application configuration information for a robot.

    - **application** *(string) --*

      The application information for the robot application.

    - **applicationVersion** *(string) --*

      The version of the robot application.

    - **launchConfig** *(dict) --*

      The launch configuration for the robot application.

      - **packageName** *(string) --*

        The package name.

      - **launchFile** *(string) --*

        The launch file name.

      - **environmentVariables** *(dict) --*

        The environment variables for the application launch.

        - *(string) --*

          - *(string) --*

      - **portForwardingConfig** *(dict) --*

        The port forwarding configuration.

        - **portMappings** *(list) --*

          The port mappings for the configuration.

          - *(dict) --*

            An object representing a port mapping.

            - **jobPort** *(integer) --*

              The port number on the simulation job instance to use as a remote connection
              point.

            - **applicationPort** *(integer) --*

              The port number on the application.

            - **enableOnPublicIp** *(boolean) --*

              A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfig` `portMappings`

    An object representing a port mapping.

    - **jobPort** *(integer) --*

      The port number on the simulation job instance to use as a remote connection
      point.

    - **applicationPort** *(integer) --*

      The port number on the application.

    - **enableOnPublicIp** *(boolean) --*

      A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobResponsesimulationApplicationslaunchConfig` `portForwardingConfig`

    The port forwarding configuration.

    - **portMappings** *(list) --*

      The port mappings for the configuration.

      - *(dict) --*

        An object representing a port mapping.

        - **jobPort** *(integer) --*

          The port number on the simulation job instance to use as a remote connection
          point.

        - **applicationPort** *(integer) --*

          The port number on the application.

        - **enableOnPublicIp** *(boolean) --*

          A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef(
    _ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobResponsesimulationApplications` `launchConfig`

    The launch configuration for the simulation application.

    - **packageName** *(string) --*

      The package name.

    - **launchFile** *(string) --*

      The launch file name.

    - **environmentVariables** *(dict) --*

      The environment variables for the application launch.

      - *(string) --*

        - *(string) --*

    - **portForwardingConfig** *(dict) --*

      The port forwarding configuration.

      - **portMappings** *(list) --*

        The port mappings for the configuration.

        - *(dict) --*

          An object representing a port mapping.

          - **jobPort** *(integer) --*

            The port number on the simulation job instance to use as a remote connection
            point.

          - **applicationPort** *(integer) --*

            The port number on the application.

          - **enableOnPublicIp** *(boolean) --*

            A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientCreateSimulationJobResponsesimulationApplicationsTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsesimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobResponsesimulationApplicationsTypeDef(
    _ClientCreateSimulationJobResponsesimulationApplicationsTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobResponse` `simulationApplications`

    Information about a simulation application configuration.

    - **application** *(string) --*

      The application information for the simulation application.

    - **applicationVersion** *(string) --*

      The version of the simulation application.

    - **launchConfig** *(dict) --*

      The launch configuration for the simulation application.

      - **packageName** *(string) --*

        The package name.

      - **launchFile** *(string) --*

        The launch file name.

      - **environmentVariables** *(dict) --*

        The environment variables for the application launch.

        - *(string) --*

          - *(string) --*

      - **portForwardingConfig** *(dict) --*

        The port forwarding configuration.

        - **portMappings** *(list) --*

          The port mappings for the configuration.

          - *(dict) --*

            An object representing a port mapping.

            - **jobPort** *(integer) --*

              The port number on the simulation job instance to use as a remote connection
              point.

            - **applicationPort** *(integer) --*

              The port number on the application.

            - **enableOnPublicIp** *(boolean) --*

              A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientCreateSimulationJobResponsevpcConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsevpcConfigTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "vpcId": str,
        "assignPublicIp": bool,
    },
    total=False,
)


class ClientCreateSimulationJobResponsevpcConfigTypeDef(
    _ClientCreateSimulationJobResponsevpcConfigTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobResponse` `vpcConfig`

    Information about the vpc configuration.

    - **subnets** *(list) --*

      A list of subnet IDs associated with the simulation job.

      - *(string) --*

    - **securityGroups** *(list) --*

      A list of security group IDs associated with the simulation job.

      - *(string) --*

    - **vpcId** *(string) --*

      The VPC ID associated with your simulation job.

    - **assignPublicIp** *(boolean) --*

      A boolean indicating if a public IP was assigned.
    """


_ClientCreateSimulationJobResponseTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponseTypeDef",
    {
        "arn": str,
        "status": str,
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": str,
        "failureCode": str,
        "clientRequestToken": str,
        "outputLocation": ClientCreateSimulationJobResponseoutputLocationTypeDef,
        "loggingConfig": ClientCreateSimulationJobResponseloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[
            ClientCreateSimulationJobResponserobotApplicationsTypeDef
        ],
        "simulationApplications": List[
            ClientCreateSimulationJobResponsesimulationApplicationsTypeDef
        ],
        "dataSources": List[ClientCreateSimulationJobResponsedataSourcesTypeDef],
        "tags": Dict[str, str],
        "vpcConfig": ClientCreateSimulationJobResponsevpcConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobResponseTypeDef(
    _ClientCreateSimulationJobResponseTypeDef
):
    """
    Type definition for `ClientCreateSimulationJob` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the simulation job.

    - **status** *(string) --*

      The status of the simulation job.

    - **lastStartedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation job was last started.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation job was last updated.

    - **failureBehavior** *(string) --*

      the failure behavior for the simulation job.

    - **failureCode** *(string) --*

      The failure code of the simulation job if it failed:

        InternalServiceError

      Internal service error.

        RobotApplicationCrash

      Robot application exited abnormally.

        SimulationApplicationCrash

      Simulation application exited abnormally.

        BadPermissionsRobotApplication

      Robot application bundle could not be downloaded.

        BadPermissionsSimulationApplication

      Simulation application bundle could not be downloaded.

        BadPermissionsS3Output

      Unable to publish outputs to customer-provided S3 bucket.

        BadPermissionsCloudwatchLogs

      Unable to publish logs to customer-provided CloudWatch Logs resource.

        SubnetIpLimitExceeded

      Subnet IP limit exceeded.

        ENILimitExceeded

      ENI limit exceeded.

        BadPermissionsUserCredentials

      Unable to use the Role provided.

        InvalidBundleRobotApplication

      Robot bundle cannot be extracted (invalid format, bundling error, or other issue).

        InvalidBundleSimulationApplication

      Simulation bundle cannot be extracted (invalid format, bundling error, or other issue).

        RobotApplicationVersionMismatchedEtag

      Etag for RobotApplication does not match value during version creation.

        SimulationApplicationVersionMismatchedEtag

      Etag for SimulationApplication does not match value during version creation.

    - **clientRequestToken** *(string) --*

      Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    - **outputLocation** *(dict) --*

      Simulation job output files location.

      - **s3Bucket** *(string) --*

        The S3 bucket for output.

      - **s3Prefix** *(string) --*

        The S3 folder in the ``s3Bucket`` where output files will be placed.

    - **loggingConfig** *(dict) --*

      The logging configuration.

      - **recordAllRosTopics** *(boolean) --*

        A boolean indicating whether to record all ROS topics.

    - **maxJobDurationInSeconds** *(integer) --*

      The maximum simulation job duration in seconds.

    - **simulationTimeMillis** *(integer) --*

      The simulation job execution duration in milliseconds.

    - **iamRole** *(string) --*

      The IAM role that allows the simulation job to call the AWS APIs that are specified in its
      associated policies on your behalf.

    - **robotApplications** *(list) --*

      The robot application used by the simulation job.

      - *(dict) --*

        Application configuration information for a robot.

        - **application** *(string) --*

          The application information for the robot application.

        - **applicationVersion** *(string) --*

          The version of the robot application.

        - **launchConfig** *(dict) --*

          The launch configuration for the robot application.

          - **packageName** *(string) --*

            The package name.

          - **launchFile** *(string) --*

            The launch file name.

          - **environmentVariables** *(dict) --*

            The environment variables for the application launch.

            - *(string) --*

              - *(string) --*

          - **portForwardingConfig** *(dict) --*

            The port forwarding configuration.

            - **portMappings** *(list) --*

              The port mappings for the configuration.

              - *(dict) --*

                An object representing a port mapping.

                - **jobPort** *(integer) --*

                  The port number on the simulation job instance to use as a remote connection
                  point.

                - **applicationPort** *(integer) --*

                  The port number on the application.

                - **enableOnPublicIp** *(boolean) --*

                  A Boolean indicating whether to enable this port mapping on public IP.

    - **simulationApplications** *(list) --*

      The simulation application used by the simulation job.

      - *(dict) --*

        Information about a simulation application configuration.

        - **application** *(string) --*

          The application information for the simulation application.

        - **applicationVersion** *(string) --*

          The version of the simulation application.

        - **launchConfig** *(dict) --*

          The launch configuration for the simulation application.

          - **packageName** *(string) --*

            The package name.

          - **launchFile** *(string) --*

            The launch file name.

          - **environmentVariables** *(dict) --*

            The environment variables for the application launch.

            - *(string) --*

              - *(string) --*

          - **portForwardingConfig** *(dict) --*

            The port forwarding configuration.

            - **portMappings** *(list) --*

              The port mappings for the configuration.

              - *(dict) --*

                An object representing a port mapping.

                - **jobPort** *(integer) --*

                  The port number on the simulation job instance to use as a remote connection
                  point.

                - **applicationPort** *(integer) --*

                  The port number on the application.

                - **enableOnPublicIp** *(boolean) --*

                  A Boolean indicating whether to enable this port mapping on public IP.

    - **dataSources** *(list) --*

      The data sources for the simulation job.

      - *(dict) --*

        Information about a data source.

        - **name** *(string) --*

          The name of the data source.

        - **s3Bucket** *(string) --*

          The S3 bucket where the data files are located.

        - **s3Keys** *(list) --*

          The list of S3 keys identifying the data source files.

          - *(dict) --*

            Information about S3 keys.

            - **s3Key** *(string) --*

              The S3 key.

            - **etag** *(string) --*

              The etag for the object.

    - **tags** *(dict) --*

      The list of all tags added to the simulation job.

      - *(string) --*

        - *(string) --*

    - **vpcConfig** *(dict) --*

      Information about the vpc configuration.

      - **subnets** *(list) --*

        A list of subnet IDs associated with the simulation job.

        - *(string) --*

      - **securityGroups** *(list) --*

        A list of security group IDs associated with the simulation job.

        - *(string) --*

      - **vpcId** *(string) --*

        The VPC ID associated with your simulation job.

      - **assignPublicIp** *(boolean) --*

        A boolean indicating if a public IP was assigned.
    """


_ClientCreateSimulationJobdataSourcesTypeDef = TypedDict(
    "_ClientCreateSimulationJobdataSourcesTypeDef",
    {"name": str, "s3Bucket": str, "s3Keys": List[str]},
)


class ClientCreateSimulationJobdataSourcesTypeDef(
    _ClientCreateSimulationJobdataSourcesTypeDef
):
    """
    Type definition for `ClientCreateSimulationJob` `dataSources`

    Information about a data source.

    - **name** *(string) --* **[REQUIRED]**

      The name of the data source.

    - **s3Bucket** *(string) --* **[REQUIRED]**

      The S3 bucket where the data files are located.

    - **s3Keys** *(list) --* **[REQUIRED]**

      The list of S3 keys identifying the data source files.

      - *(string) --*
    """


_ClientCreateSimulationJobloggingConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobloggingConfigTypeDef", {"recordAllRosTopics": bool}
)


class ClientCreateSimulationJobloggingConfigTypeDef(
    _ClientCreateSimulationJobloggingConfigTypeDef
):
    """
    Type definition for `ClientCreateSimulationJob` `loggingConfig`

    The logging configuration.

    - **recordAllRosTopics** *(boolean) --* **[REQUIRED]**

      A boolean indicating whether to record all ROS topics.
    """


_ClientCreateSimulationJoboutputLocationTypeDef = TypedDict(
    "_ClientCreateSimulationJoboutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)


class ClientCreateSimulationJoboutputLocationTypeDef(
    _ClientCreateSimulationJoboutputLocationTypeDef
):
    """
    Type definition for `ClientCreateSimulationJob` `outputLocation`

    Location for output files generated by the simulation job.

    - **s3Bucket** *(string) --*

      The S3 bucket for output.

    - **s3Prefix** *(string) --*

      The S3 folder in the ``s3Bucket`` where output files will be placed.
    """


_RequiredClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_RequiredClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int},
)
_OptionalClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_OptionalClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"enableOnPublicIp": bool},
    total=False,
)


class ClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _RequiredClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef,
    _OptionalClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef,
):
    """
    Type definition for `ClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfig` `portMappings`

    An object representing a port mapping.

    - **jobPort** *(integer) --* **[REQUIRED]**

      The port number on the simulation job instance to use as a remote connection point.

    - **applicationPort** *(integer) --* **[REQUIRED]**

      The port number on the application.

    - **enableOnPublicIp** *(boolean) --*

      A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobrobotApplicationslaunchConfig` `portForwardingConfig`

    The port forwarding configuration.

    - **portMappings** *(list) --*

      The port mappings for the configuration.

      - *(dict) --*

        An object representing a port mapping.

        - **jobPort** *(integer) --* **[REQUIRED]**

          The port number on the simulation job instance to use as a remote connection point.

        - **applicationPort** *(integer) --* **[REQUIRED]**

          The port number on the application.

        - **enableOnPublicIp** *(boolean) --*

          A Boolean indicating whether to enable this port mapping on public IP.
    """


_RequiredClientCreateSimulationJobrobotApplicationslaunchConfigTypeDef = TypedDict(
    "_RequiredClientCreateSimulationJobrobotApplicationslaunchConfigTypeDef",
    {"packageName": str, "launchFile": str},
)
_OptionalClientCreateSimulationJobrobotApplicationslaunchConfigTypeDef = TypedDict(
    "_OptionalClientCreateSimulationJobrobotApplicationslaunchConfigTypeDef",
    {
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientCreateSimulationJobrobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobrobotApplicationslaunchConfigTypeDef(
    _RequiredClientCreateSimulationJobrobotApplicationslaunchConfigTypeDef,
    _OptionalClientCreateSimulationJobrobotApplicationslaunchConfigTypeDef,
):
    """
    Type definition for `ClientCreateSimulationJobrobotApplications` `launchConfig`

    The launch configuration for the robot application.

    - **packageName** *(string) --* **[REQUIRED]**

      The package name.

    - **launchFile** *(string) --* **[REQUIRED]**

      The launch file name.

    - **environmentVariables** *(dict) --*

      The environment variables for the application launch.

      - *(string) --*

        - *(string) --*

    - **portForwardingConfig** *(dict) --*

      The port forwarding configuration.

      - **portMappings** *(list) --*

        The port mappings for the configuration.

        - *(dict) --*

          An object representing a port mapping.

          - **jobPort** *(integer) --* **[REQUIRED]**

            The port number on the simulation job instance to use as a remote connection point.

          - **applicationPort** *(integer) --* **[REQUIRED]**

            The port number on the application.

          - **enableOnPublicIp** *(boolean) --*

            A Boolean indicating whether to enable this port mapping on public IP.
    """


_RequiredClientCreateSimulationJobrobotApplicationsTypeDef = TypedDict(
    "_RequiredClientCreateSimulationJobrobotApplicationsTypeDef",
    {
        "application": str,
        "launchConfig": ClientCreateSimulationJobrobotApplicationslaunchConfigTypeDef,
    },
)
_OptionalClientCreateSimulationJobrobotApplicationsTypeDef = TypedDict(
    "_OptionalClientCreateSimulationJobrobotApplicationsTypeDef",
    {"applicationVersion": str},
    total=False,
)


class ClientCreateSimulationJobrobotApplicationsTypeDef(
    _RequiredClientCreateSimulationJobrobotApplicationsTypeDef,
    _OptionalClientCreateSimulationJobrobotApplicationsTypeDef,
):
    """
    Type definition for `ClientCreateSimulationJob` `robotApplications`

    Application configuration information for a robot.

    - **application** *(string) --* **[REQUIRED]**

      The application information for the robot application.

    - **applicationVersion** *(string) --*

      The version of the robot application.

    - **launchConfig** *(dict) --* **[REQUIRED]**

      The launch configuration for the robot application.

      - **packageName** *(string) --* **[REQUIRED]**

        The package name.

      - **launchFile** *(string) --* **[REQUIRED]**

        The launch file name.

      - **environmentVariables** *(dict) --*

        The environment variables for the application launch.

        - *(string) --*

          - *(string) --*

      - **portForwardingConfig** *(dict) --*

        The port forwarding configuration.

        - **portMappings** *(list) --*

          The port mappings for the configuration.

          - *(dict) --*

            An object representing a port mapping.

            - **jobPort** *(integer) --* **[REQUIRED]**

              The port number on the simulation job instance to use as a remote connection point.

            - **applicationPort** *(integer) --* **[REQUIRED]**

              The port number on the application.

            - **enableOnPublicIp** *(boolean) --*

              A Boolean indicating whether to enable this port mapping on public IP.
    """


_RequiredClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_RequiredClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int},
)
_OptionalClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_OptionalClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"enableOnPublicIp": bool},
    total=False,
)


class ClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _RequiredClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef,
    _OptionalClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef,
):
    """
    Type definition for `ClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfig` `portMappings`

    An object representing a port mapping.

    - **jobPort** *(integer) --* **[REQUIRED]**

      The port number on the simulation job instance to use as a remote connection point.

    - **applicationPort** *(integer) --* **[REQUIRED]**

      The port number on the application.

    - **enableOnPublicIp** *(boolean) --*

      A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigTypeDef
):
    """
    Type definition for `ClientCreateSimulationJobsimulationApplicationslaunchConfig` `portForwardingConfig`

    The port forwarding configuration.

    - **portMappings** *(list) --*

      The port mappings for the configuration.

      - *(dict) --*

        An object representing a port mapping.

        - **jobPort** *(integer) --* **[REQUIRED]**

          The port number on the simulation job instance to use as a remote connection point.

        - **applicationPort** *(integer) --* **[REQUIRED]**

          The port number on the application.

        - **enableOnPublicIp** *(boolean) --*

          A Boolean indicating whether to enable this port mapping on public IP.
    """


_RequiredClientCreateSimulationJobsimulationApplicationslaunchConfigTypeDef = TypedDict(
    "_RequiredClientCreateSimulationJobsimulationApplicationslaunchConfigTypeDef",
    {"packageName": str, "launchFile": str},
)
_OptionalClientCreateSimulationJobsimulationApplicationslaunchConfigTypeDef = TypedDict(
    "_OptionalClientCreateSimulationJobsimulationApplicationslaunchConfigTypeDef",
    {
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientCreateSimulationJobsimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobsimulationApplicationslaunchConfigTypeDef(
    _RequiredClientCreateSimulationJobsimulationApplicationslaunchConfigTypeDef,
    _OptionalClientCreateSimulationJobsimulationApplicationslaunchConfigTypeDef,
):
    """
    Type definition for `ClientCreateSimulationJobsimulationApplications` `launchConfig`

    The launch configuration for the simulation application.

    - **packageName** *(string) --* **[REQUIRED]**

      The package name.

    - **launchFile** *(string) --* **[REQUIRED]**

      The launch file name.

    - **environmentVariables** *(dict) --*

      The environment variables for the application launch.

      - *(string) --*

        - *(string) --*

    - **portForwardingConfig** *(dict) --*

      The port forwarding configuration.

      - **portMappings** *(list) --*

        The port mappings for the configuration.

        - *(dict) --*

          An object representing a port mapping.

          - **jobPort** *(integer) --* **[REQUIRED]**

            The port number on the simulation job instance to use as a remote connection point.

          - **applicationPort** *(integer) --* **[REQUIRED]**

            The port number on the application.

          - **enableOnPublicIp** *(boolean) --*

            A Boolean indicating whether to enable this port mapping on public IP.
    """


_RequiredClientCreateSimulationJobsimulationApplicationsTypeDef = TypedDict(
    "_RequiredClientCreateSimulationJobsimulationApplicationsTypeDef",
    {
        "application": str,
        "launchConfig": ClientCreateSimulationJobsimulationApplicationslaunchConfigTypeDef,
    },
)
_OptionalClientCreateSimulationJobsimulationApplicationsTypeDef = TypedDict(
    "_OptionalClientCreateSimulationJobsimulationApplicationsTypeDef",
    {"applicationVersion": str},
    total=False,
)


class ClientCreateSimulationJobsimulationApplicationsTypeDef(
    _RequiredClientCreateSimulationJobsimulationApplicationsTypeDef,
    _OptionalClientCreateSimulationJobsimulationApplicationsTypeDef,
):
    """
    Type definition for `ClientCreateSimulationJob` `simulationApplications`

    Information about a simulation application configuration.

    - **application** *(string) --* **[REQUIRED]**

      The application information for the simulation application.

    - **applicationVersion** *(string) --*

      The version of the simulation application.

    - **launchConfig** *(dict) --* **[REQUIRED]**

      The launch configuration for the simulation application.

      - **packageName** *(string) --* **[REQUIRED]**

        The package name.

      - **launchFile** *(string) --* **[REQUIRED]**

        The launch file name.

      - **environmentVariables** *(dict) --*

        The environment variables for the application launch.

        - *(string) --*

          - *(string) --*

      - **portForwardingConfig** *(dict) --*

        The port forwarding configuration.

        - **portMappings** *(list) --*

          The port mappings for the configuration.

          - *(dict) --*

            An object representing a port mapping.

            - **jobPort** *(integer) --* **[REQUIRED]**

              The port number on the simulation job instance to use as a remote connection point.

            - **applicationPort** *(integer) --* **[REQUIRED]**

              The port number on the application.

            - **enableOnPublicIp** *(boolean) --*

              A Boolean indicating whether to enable this port mapping on public IP.
    """


_RequiredClientCreateSimulationJobvpcConfigTypeDef = TypedDict(
    "_RequiredClientCreateSimulationJobvpcConfigTypeDef", {"subnets": List[str]}
)
_OptionalClientCreateSimulationJobvpcConfigTypeDef = TypedDict(
    "_OptionalClientCreateSimulationJobvpcConfigTypeDef",
    {"securityGroups": List[str], "assignPublicIp": bool},
    total=False,
)


class ClientCreateSimulationJobvpcConfigTypeDef(
    _RequiredClientCreateSimulationJobvpcConfigTypeDef,
    _OptionalClientCreateSimulationJobvpcConfigTypeDef,
):
    """
    Type definition for `ClientCreateSimulationJob` `vpcConfig`

    If your simulation job accesses resources in a VPC, you provide this parameter identifying the
    list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at
    least one security group and one subnet ID.

    - **subnets** *(list) --* **[REQUIRED]**

      A list of one or more subnet IDs in your VPC.

      - *(string) --*

    - **securityGroups** *(list) --*

      A list of one or more security groups IDs in your VPC.

      - *(string) --*

    - **assignPublicIp** *(boolean) --*

      A boolean indicating whether to assign a public IP address.
    """


_ClientDeregisterRobotResponseTypeDef = TypedDict(
    "_ClientDeregisterRobotResponseTypeDef", {"fleet": str, "robot": str}, total=False
)


class ClientDeregisterRobotResponseTypeDef(_ClientDeregisterRobotResponseTypeDef):
    """
    Type definition for `ClientDeregisterRobot` `Response`

    - **fleet** *(string) --*

      The Amazon Resource Name (ARN) of the fleet.

    - **robot** *(string) --*

      The Amazon Resource Name (ARN) of the robot.
    """


_ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)


class ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef(
    _ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef
):
    """
    Type definition for `ClientDescribeDeploymentJobResponsedeploymentApplicationConfigs` `launchConfig`

    The launch configuration.

    - **packageName** *(string) --*

      The package name.

    - **preLaunchFile** *(string) --*

      The deployment pre-launch file. This file will be executed prior to the launch file.

    - **launchFile** *(string) --*

      The launch file name.

    - **postLaunchFile** *(string) --*

      The deployment post-launch file. This file will be executed after the launch file.

    - **environmentVariables** *(dict) --*

      An array of key/value pairs specifying environment variables for the robot application

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef(
    _ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef
):
    """
    Type definition for `ClientDescribeDeploymentJobResponse` `deploymentApplicationConfigs`

    Information about a deployment application configuration.

    - **application** *(string) --*

      The Amazon Resource Name (ARN) of the robot application.

    - **applicationVersion** *(string) --*

      The version of the application.

    - **launchConfig** *(dict) --*

      The launch configuration.

      - **packageName** *(string) --*

        The package name.

      - **preLaunchFile** *(string) --*

        The deployment pre-launch file. This file will be executed prior to the launch file.

      - **launchFile** *(string) --*

        The launch file name.

      - **postLaunchFile** *(string) --*

        The deployment post-launch file. This file will be executed after the launch file.

      - **environmentVariables** *(dict) --*

        An array of key/value pairs specifying environment variables for the robot application

        - *(string) --*

          - *(string) --*
    """


_ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)


class ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef(
    _ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef
):
    """
    Type definition for `ClientDescribeDeploymentJobResponsedeploymentConfig` `downloadConditionFile`

    The download condition file.

    - **bucket** *(string) --*

      The bucket containing the object.

    - **key** *(string) --*

      The key of the object.

    - **etag** *(string) --*

      The etag of the object.
    """


_ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)


class ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef(
    _ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef
):
    """
    Type definition for `ClientDescribeDeploymentJobResponse` `deploymentConfig`

    The deployment configuration.

    - **concurrentDeploymentPercentage** *(integer) --*

      The percentage of robots receiving the deployment at the same time.

    - **failureThresholdPercentage** *(integer) --*

      The percentage of deployments that need to fail before stopping deployment.

    - **robotDeploymentTimeoutInSeconds** *(integer) --*

      The amount of time, in seconds, to wait for deployment to a single robot to complete.
      Choose a time between 1 minute and 7 days. The default is 5 hours.

    - **downloadConditionFile** *(dict) --*

      The download condition file.

      - **bucket** *(string) --*

        The bucket containing the object.

      - **key** *(string) --*

        The key of the object.

      - **etag** *(string) --*

        The etag of the object.
    """


_ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef",
    {
        "currentProgress": str,
        "percentDone": float,
        "estimatedTimeRemainingSeconds": int,
        "targetResource": str,
    },
    total=False,
)


class ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef(
    _ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef
):
    """
    Type definition for `ClientDescribeDeploymentJobResponserobotDeploymentSummary` `progressDetail`

    Information about how the deployment is progressing.

    - **currentProgress** *(string) --*

      The current progress status.

        Validating

      Validating the deployment.

        DownloadingExtracting

      Downloading and extracting the bundle on the robot.

        ExecutingPreLaunch

      Executing pre-launch script(s) if provided.

        Launching

      Launching the robot application.

        ExecutingPostLaunch

      Executing post-launch script(s) if provided.

        Finished

      Deployment is complete.

    - **percentDone** *(float) --*

      Precentage of the step that is done. This currently only applies to the
      ``Downloading/Extracting`` step of the deployment. It is empty for other steps.

    - **estimatedTimeRemainingSeconds** *(integer) --*

      Estimated amount of time in seconds remaining in the step. This currently only applies
      to the ``Downloading/Extracting`` step of the deployment. It is empty for other steps.

    - **targetResource** *(string) --*

      The Amazon Resource Name (ARN) of the deployment job.
    """


_ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef",
    {
        "arn": str,
        "deploymentStartTime": datetime,
        "deploymentFinishTime": datetime,
        "status": str,
        "progressDetail": ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef,
        "failureReason": str,
        "failureCode": str,
    },
    total=False,
)


class ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef(
    _ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef
):
    """
    Type definition for `ClientDescribeDeploymentJobResponse` `robotDeploymentSummary`

    Information about a robot deployment.

    - **arn** *(string) --*

      The robot deployment Amazon Resource Name (ARN).

    - **deploymentStartTime** *(datetime) --*

      The time, in milliseconds since the epoch, when the deployment was started.

    - **deploymentFinishTime** *(datetime) --*

      The time, in milliseconds since the epoch, when the deployment finished.

    - **status** *(string) --*

      The status of the robot deployment.

    - **progressDetail** *(dict) --*

      Information about how the deployment is progressing.

      - **currentProgress** *(string) --*

        The current progress status.

          Validating

        Validating the deployment.

          DownloadingExtracting

        Downloading and extracting the bundle on the robot.

          ExecutingPreLaunch

        Executing pre-launch script(s) if provided.

          Launching

        Launching the robot application.

          ExecutingPostLaunch

        Executing post-launch script(s) if provided.

          Finished

        Deployment is complete.

      - **percentDone** *(float) --*

        Precentage of the step that is done. This currently only applies to the
        ``Downloading/Extracting`` step of the deployment. It is empty for other steps.

      - **estimatedTimeRemainingSeconds** *(integer) --*

        Estimated amount of time in seconds remaining in the step. This currently only applies
        to the ``Downloading/Extracting`` step of the deployment. It is empty for other steps.

      - **targetResource** *(string) --*

        The Amazon Resource Name (ARN) of the deployment job.

    - **failureReason** *(string) --*

      A short description of the reason why the robot deployment failed.

    - **failureCode** *(string) --*

      The robot deployment failure code.
    """


_ClientDescribeDeploymentJobResponseTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": str,
        "deploymentConfig": ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef,
        "deploymentApplicationConfigs": List[
            ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef
        ],
        "failureReason": str,
        "failureCode": str,
        "createdAt": datetime,
        "robotDeploymentSummary": List[
            ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef
        ],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeDeploymentJobResponseTypeDef(
    _ClientDescribeDeploymentJobResponseTypeDef
):
    """
    Type definition for `ClientDescribeDeploymentJob` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the deployment job.

    - **fleet** *(string) --*

      The Amazon Resource Name (ARN) of the fleet.

    - **status** *(string) --*

      The status of the deployment job.

    - **deploymentConfig** *(dict) --*

      The deployment configuration.

      - **concurrentDeploymentPercentage** *(integer) --*

        The percentage of robots receiving the deployment at the same time.

      - **failureThresholdPercentage** *(integer) --*

        The percentage of deployments that need to fail before stopping deployment.

      - **robotDeploymentTimeoutInSeconds** *(integer) --*

        The amount of time, in seconds, to wait for deployment to a single robot to complete.
        Choose a time between 1 minute and 7 days. The default is 5 hours.

      - **downloadConditionFile** *(dict) --*

        The download condition file.

        - **bucket** *(string) --*

          The bucket containing the object.

        - **key** *(string) --*

          The key of the object.

        - **etag** *(string) --*

          The etag of the object.

    - **deploymentApplicationConfigs** *(list) --*

      The deployment application configuration.

      - *(dict) --*

        Information about a deployment application configuration.

        - **application** *(string) --*

          The Amazon Resource Name (ARN) of the robot application.

        - **applicationVersion** *(string) --*

          The version of the application.

        - **launchConfig** *(dict) --*

          The launch configuration.

          - **packageName** *(string) --*

            The package name.

          - **preLaunchFile** *(string) --*

            The deployment pre-launch file. This file will be executed prior to the launch file.

          - **launchFile** *(string) --*

            The launch file name.

          - **postLaunchFile** *(string) --*

            The deployment post-launch file. This file will be executed after the launch file.

          - **environmentVariables** *(dict) --*

            An array of key/value pairs specifying environment variables for the robot application

            - *(string) --*

              - *(string) --*

    - **failureReason** *(string) --*

      A short description of the reason why the deployment job failed.

    - **failureCode** *(string) --*

      The deployment job failure code.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the deployment job was created.

    - **robotDeploymentSummary** *(list) --*

      A list of robot deployment summaries.

      - *(dict) --*

        Information about a robot deployment.

        - **arn** *(string) --*

          The robot deployment Amazon Resource Name (ARN).

        - **deploymentStartTime** *(datetime) --*

          The time, in milliseconds since the epoch, when the deployment was started.

        - **deploymentFinishTime** *(datetime) --*

          The time, in milliseconds since the epoch, when the deployment finished.

        - **status** *(string) --*

          The status of the robot deployment.

        - **progressDetail** *(dict) --*

          Information about how the deployment is progressing.

          - **currentProgress** *(string) --*

            The current progress status.

              Validating

            Validating the deployment.

              DownloadingExtracting

            Downloading and extracting the bundle on the robot.

              ExecutingPreLaunch

            Executing pre-launch script(s) if provided.

              Launching

            Launching the robot application.

              ExecutingPostLaunch

            Executing post-launch script(s) if provided.

              Finished

            Deployment is complete.

          - **percentDone** *(float) --*

            Precentage of the step that is done. This currently only applies to the
            ``Downloading/Extracting`` step of the deployment. It is empty for other steps.

          - **estimatedTimeRemainingSeconds** *(integer) --*

            Estimated amount of time in seconds remaining in the step. This currently only applies
            to the ``Downloading/Extracting`` step of the deployment. It is empty for other steps.

          - **targetResource** *(string) --*

            The Amazon Resource Name (ARN) of the deployment job.

        - **failureReason** *(string) --*

          A short description of the reason why the robot deployment failed.

        - **failureCode** *(string) --*

          The robot deployment failure code.

    - **tags** *(dict) --*

      The list of all tags added to the specified deployment job.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeFleetResponserobotsTypeDef = TypedDict(
    "_ClientDescribeFleetResponserobotsTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": str,
        "greenGrassGroupId": str,
        "createdAt": datetime,
        "architecture": str,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)


class ClientDescribeFleetResponserobotsTypeDef(
    _ClientDescribeFleetResponserobotsTypeDef
):
    """
    Type definition for `ClientDescribeFleetResponse` `robots`

    Information about a robot.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the robot.

    - **name** *(string) --*

      The name of the robot.

    - **fleetArn** *(string) --*

      The Amazon Resource Name (ARN) of the fleet.

    - **status** *(string) --*

      The status of the robot.

    - **greenGrassGroupId** *(string) --*

      The Greengrass group associated with the robot.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the robot was created.

    - **architecture** *(string) --*

      The architecture of the robot.

    - **lastDeploymentJob** *(string) --*

      The Amazon Resource Name (ARN) of the last deployment job.

    - **lastDeploymentTime** *(datetime) --*

      The time of the last deployment.
    """


_ClientDescribeFleetResponseTypeDef = TypedDict(
    "_ClientDescribeFleetResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "robots": List[ClientDescribeFleetResponserobotsTypeDef],
        "createdAt": datetime,
        "lastDeploymentStatus": str,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeFleetResponseTypeDef(_ClientDescribeFleetResponseTypeDef):
    """
    Type definition for `ClientDescribeFleet` `Response`

    - **name** *(string) --*

      The name of the fleet.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the fleet.

    - **robots** *(list) --*

      A list of robots.

      - *(dict) --*

        Information about a robot.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the robot.

        - **name** *(string) --*

          The name of the robot.

        - **fleetArn** *(string) --*

          The Amazon Resource Name (ARN) of the fleet.

        - **status** *(string) --*

          The status of the robot.

        - **greenGrassGroupId** *(string) --*

          The Greengrass group associated with the robot.

        - **createdAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the robot was created.

        - **architecture** *(string) --*

          The architecture of the robot.

        - **lastDeploymentJob** *(string) --*

          The Amazon Resource Name (ARN) of the last deployment job.

        - **lastDeploymentTime** *(datetime) --*

          The time of the last deployment.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the fleet was created.

    - **lastDeploymentStatus** *(string) --*

      The status of the last deployment.

    - **lastDeploymentJob** *(string) --*

      The Amazon Resource Name (ARN) of the last deployment job.

    - **lastDeploymentTime** *(datetime) --*

      The time of the last deployment.

    - **tags** *(dict) --*

      The list of all tags added to the specified fleet.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef(
    _ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientDescribeRobotApplicationResponse` `robotSoftwareSuite`

    The robot software suite used by the robot application.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientDescribeRobotApplicationResponsesourcesTypeDef = TypedDict(
    "_ClientDescribeRobotApplicationResponsesourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "etag": str, "architecture": str},
    total=False,
)


class ClientDescribeRobotApplicationResponsesourcesTypeDef(
    _ClientDescribeRobotApplicationResponsesourcesTypeDef
):
    """
    Type definition for `ClientDescribeRobotApplicationResponse` `sources`

    Information about a source.

    - **s3Bucket** *(string) --*

      The s3 bucket name.

    - **s3Key** *(string) --*

      The s3 object key.

    - **etag** *(string) --*

      A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

    - **architecture** *(string) --*

      The taget processor architecture for the application.
    """


_ClientDescribeRobotApplicationResponseTypeDef = TypedDict(
    "_ClientDescribeRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientDescribeRobotApplicationResponsesourcesTypeDef],
        "robotSoftwareSuite": ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef,
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeRobotApplicationResponseTypeDef(
    _ClientDescribeRobotApplicationResponseTypeDef
):
    """
    Type definition for `ClientDescribeRobotApplication` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the robot application.

    - **name** *(string) --*

      The name of the robot application.

    - **version** *(string) --*

      The version of the robot application.

    - **sources** *(list) --*

      The sources of the robot application.

      - *(dict) --*

        Information about a source.

        - **s3Bucket** *(string) --*

          The s3 bucket name.

        - **s3Key** *(string) --*

          The s3 object key.

        - **etag** *(string) --*

          A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

        - **architecture** *(string) --*

          The taget processor architecture for the application.

    - **robotSoftwareSuite** *(dict) --*

      The robot software suite used by the robot application.

      - **name** *(string) --*

        The name of the robot software suite.

      - **version** *(string) --*

        The version of the robot software suite.

    - **revisionId** *(string) --*

      The revision id of the robot application.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the robot application was last updated.

    - **tags** *(dict) --*

      The list of all tags added to the specified robot application.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeRobotResponseTypeDef = TypedDict(
    "_ClientDescribeRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": str,
        "greengrassGroupId": str,
        "createdAt": datetime,
        "architecture": str,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeRobotResponseTypeDef(_ClientDescribeRobotResponseTypeDef):
    """
    Type definition for `ClientDescribeRobot` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the robot.

    - **name** *(string) --*

      The name of the robot.

    - **fleetArn** *(string) --*

      The Amazon Resource Name (ARN) of the fleet.

    - **status** *(string) --*

      The status of the fleet.

    - **greengrassGroupId** *(string) --*

      The Greengrass group id.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the robot was created.

    - **architecture** *(string) --*

      The target architecture of the robot application.

    - **lastDeploymentJob** *(string) --*

      The Amazon Resource Name (ARN) of the last deployment job.

    - **lastDeploymentTime** *(datetime) --*

      The time of the last deployment job.

    - **tags** *(dict) --*

      The list of all tags added to the specified robot.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeSimulationApplicationResponserenderingEngineTypeDef = TypedDict(
    "_ClientDescribeSimulationApplicationResponserenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientDescribeSimulationApplicationResponserenderingEngineTypeDef(
    _ClientDescribeSimulationApplicationResponserenderingEngineTypeDef
):
    """
    Type definition for `ClientDescribeSimulationApplicationResponse` `renderingEngine`

    The rendering engine for the simulation application.

    - **name** *(string) --*

      The name of the rendering engine.

    - **version** *(string) --*

      The version of the rendering engine.
    """


_ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef(
    _ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientDescribeSimulationApplicationResponse` `robotSoftwareSuite`

    Information about the robot software suite.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef(
    _ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientDescribeSimulationApplicationResponse` `simulationSoftwareSuite`

    The simulation software suite used by the simulation application.

    - **name** *(string) --*

      The name of the simulation software suite.

    - **version** *(string) --*

      The version of the simulation software suite.
    """


_ClientDescribeSimulationApplicationResponsesourcesTypeDef = TypedDict(
    "_ClientDescribeSimulationApplicationResponsesourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "etag": str, "architecture": str},
    total=False,
)


class ClientDescribeSimulationApplicationResponsesourcesTypeDef(
    _ClientDescribeSimulationApplicationResponsesourcesTypeDef
):
    """
    Type definition for `ClientDescribeSimulationApplicationResponse` `sources`

    Information about a source.

    - **s3Bucket** *(string) --*

      The s3 bucket name.

    - **s3Key** *(string) --*

      The s3 object key.

    - **etag** *(string) --*

      A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

    - **architecture** *(string) --*

      The taget processor architecture for the application.
    """


_ClientDescribeSimulationApplicationResponseTypeDef = TypedDict(
    "_ClientDescribeSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientDescribeSimulationApplicationResponsesourcesTypeDef],
        "simulationSoftwareSuite": ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef,
        "renderingEngine": ClientDescribeSimulationApplicationResponserenderingEngineTypeDef,
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeSimulationApplicationResponseTypeDef(
    _ClientDescribeSimulationApplicationResponseTypeDef
):
    """
    Type definition for `ClientDescribeSimulationApplication` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the robot simulation application.

    - **name** *(string) --*

      The name of the simulation application.

    - **version** *(string) --*

      The version of the simulation application.

    - **sources** *(list) --*

      The sources of the simulation application.

      - *(dict) --*

        Information about a source.

        - **s3Bucket** *(string) --*

          The s3 bucket name.

        - **s3Key** *(string) --*

          The s3 object key.

        - **etag** *(string) --*

          A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

        - **architecture** *(string) --*

          The taget processor architecture for the application.

    - **simulationSoftwareSuite** *(dict) --*

      The simulation software suite used by the simulation application.

      - **name** *(string) --*

        The name of the simulation software suite.

      - **version** *(string) --*

        The version of the simulation software suite.

    - **robotSoftwareSuite** *(dict) --*

      Information about the robot software suite.

      - **name** *(string) --*

        The name of the robot software suite.

      - **version** *(string) --*

        The version of the robot software suite.

    - **renderingEngine** *(dict) --*

      The rendering engine for the simulation application.

      - **name** *(string) --*

        The name of the rendering engine.

      - **version** *(string) --*

        The version of the rendering engine.

    - **revisionId** *(string) --*

      The revision id of the simulation application.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation application was last updated.

    - **tags** *(dict) --*

      The list of all tags added to the specified simulation application.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef",
    {"s3Key": str, "etag": str},
    total=False,
)


class ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef(
    _ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponsedataSources` `s3Keys`

    Information about S3 keys.

    - **s3Key** *(string) --*

      The S3 key.

    - **etag** *(string) --*

      The etag for the object.
    """


_ClientDescribeSimulationJobResponsedataSourcesTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsedataSourcesTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List[ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef],
    },
    total=False,
)


class ClientDescribeSimulationJobResponsedataSourcesTypeDef(
    _ClientDescribeSimulationJobResponsedataSourcesTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponse` `dataSources`

    Information about a data source.

    - **name** *(string) --*

      The name of the data source.

    - **s3Bucket** *(string) --*

      The S3 bucket where the data files are located.

    - **s3Keys** *(list) --*

      The list of S3 keys identifying the data source files.

      - *(dict) --*

        Information about S3 keys.

        - **s3Key** *(string) --*

          The S3 key.

        - **etag** *(string) --*

          The etag for the object.
    """


_ClientDescribeSimulationJobResponseloggingConfigTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponseloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)


class ClientDescribeSimulationJobResponseloggingConfigTypeDef(
    _ClientDescribeSimulationJobResponseloggingConfigTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponse` `loggingConfig`

    The logging configuration.

    - **recordAllRosTopics** *(boolean) --*

      A boolean indicating whether to record all ROS topics.
    """


_ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef",
    {"networkInterfaceId": str, "privateIpAddress": str, "publicIpAddress": str},
    total=False,
)


class ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef(
    _ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponse` `networkInterface`

    The network interface information for the simulation job.

    - **networkInterfaceId** *(string) --*

      The ID of the network interface.

    - **privateIpAddress** *(string) --*

      The IPv4 address of the network interface within the subnet.

    - **publicIpAddress** *(string) --*

      The IPv4 public address of the network interface.
    """


_ClientDescribeSimulationJobResponseoutputLocationTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponseoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)


class ClientDescribeSimulationJobResponseoutputLocationTypeDef(
    _ClientDescribeSimulationJobResponseoutputLocationTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponse` `outputLocation`

    Location for output files generated by the simulation job.

    - **s3Bucket** *(string) --*

      The S3 bucket for output.

    - **s3Prefix** *(string) --*

      The S3 folder in the ``s3Bucket`` where output files will be placed.
    """


_ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfig` `portMappings`

    An object representing a port mapping.

    - **jobPort** *(integer) --*

      The port number on the simulation job instance to use as a remote connection
      point.

    - **applicationPort** *(integer) --*

      The port number on the application.

    - **enableOnPublicIp** *(boolean) --*

      A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponserobotApplicationslaunchConfig` `portForwardingConfig`

    The port forwarding configuration.

    - **portMappings** *(list) --*

      The port mappings for the configuration.

      - *(dict) --*

        An object representing a port mapping.

        - **jobPort** *(integer) --*

          The port number on the simulation job instance to use as a remote connection
          point.

        - **applicationPort** *(integer) --*

          The port number on the application.

        - **enableOnPublicIp** *(boolean) --*

          A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef(
    _ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponserobotApplications` `launchConfig`

    The launch configuration for the robot application.

    - **packageName** *(string) --*

      The package name.

    - **launchFile** *(string) --*

      The launch file name.

    - **environmentVariables** *(dict) --*

      The environment variables for the application launch.

      - *(string) --*

        - *(string) --*

    - **portForwardingConfig** *(dict) --*

      The port forwarding configuration.

      - **portMappings** *(list) --*

        The port mappings for the configuration.

        - *(dict) --*

          An object representing a port mapping.

          - **jobPort** *(integer) --*

            The port number on the simulation job instance to use as a remote connection
            point.

          - **applicationPort** *(integer) --*

            The port number on the application.

          - **enableOnPublicIp** *(boolean) --*

            A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientDescribeSimulationJobResponserobotApplicationsTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponserobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSimulationJobResponserobotApplicationsTypeDef(
    _ClientDescribeSimulationJobResponserobotApplicationsTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponse` `robotApplications`

    Application configuration information for a robot.

    - **application** *(string) --*

      The application information for the robot application.

    - **applicationVersion** *(string) --*

      The version of the robot application.

    - **launchConfig** *(dict) --*

      The launch configuration for the robot application.

      - **packageName** *(string) --*

        The package name.

      - **launchFile** *(string) --*

        The launch file name.

      - **environmentVariables** *(dict) --*

        The environment variables for the application launch.

        - *(string) --*

          - *(string) --*

      - **portForwardingConfig** *(dict) --*

        The port forwarding configuration.

        - **portMappings** *(list) --*

          The port mappings for the configuration.

          - *(dict) --*

            An object representing a port mapping.

            - **jobPort** *(integer) --*

              The port number on the simulation job instance to use as a remote connection
              point.

            - **applicationPort** *(integer) --*

              The port number on the application.

            - **enableOnPublicIp** *(boolean) --*

              A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfig` `portMappings`

    An object representing a port mapping.

    - **jobPort** *(integer) --*

      The port number on the simulation job instance to use as a remote connection
      point.

    - **applicationPort** *(integer) --*

      The port number on the application.

    - **enableOnPublicIp** *(boolean) --*

      A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfig` `portForwardingConfig`

    The port forwarding configuration.

    - **portMappings** *(list) --*

      The port mappings for the configuration.

      - *(dict) --*

        An object representing a port mapping.

        - **jobPort** *(integer) --*

          The port number on the simulation job instance to use as a remote connection
          point.

        - **applicationPort** *(integer) --*

          The port number on the application.

        - **enableOnPublicIp** *(boolean) --*

          A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef(
    _ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponsesimulationApplications` `launchConfig`

    The launch configuration for the simulation application.

    - **packageName** *(string) --*

      The package name.

    - **launchFile** *(string) --*

      The launch file name.

    - **environmentVariables** *(dict) --*

      The environment variables for the application launch.

      - *(string) --*

        - *(string) --*

    - **portForwardingConfig** *(dict) --*

      The port forwarding configuration.

      - **portMappings** *(list) --*

        The port mappings for the configuration.

        - *(dict) --*

          An object representing a port mapping.

          - **jobPort** *(integer) --*

            The port number on the simulation job instance to use as a remote connection
            point.

          - **applicationPort** *(integer) --*

            The port number on the application.

          - **enableOnPublicIp** *(boolean) --*

            A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef(
    _ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponse` `simulationApplications`

    Information about a simulation application configuration.

    - **application** *(string) --*

      The application information for the simulation application.

    - **applicationVersion** *(string) --*

      The version of the simulation application.

    - **launchConfig** *(dict) --*

      The launch configuration for the simulation application.

      - **packageName** *(string) --*

        The package name.

      - **launchFile** *(string) --*

        The launch file name.

      - **environmentVariables** *(dict) --*

        The environment variables for the application launch.

        - *(string) --*

          - *(string) --*

      - **portForwardingConfig** *(dict) --*

        The port forwarding configuration.

        - **portMappings** *(list) --*

          The port mappings for the configuration.

          - *(dict) --*

            An object representing a port mapping.

            - **jobPort** *(integer) --*

              The port number on the simulation job instance to use as a remote connection
              point.

            - **applicationPort** *(integer) --*

              The port number on the application.

            - **enableOnPublicIp** *(boolean) --*

              A Boolean indicating whether to enable this port mapping on public IP.
    """


_ClientDescribeSimulationJobResponsevpcConfigTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsevpcConfigTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "vpcId": str,
        "assignPublicIp": bool,
    },
    total=False,
)


class ClientDescribeSimulationJobResponsevpcConfigTypeDef(
    _ClientDescribeSimulationJobResponsevpcConfigTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJobResponse` `vpcConfig`

    The VPC configuration.

    - **subnets** *(list) --*

      A list of subnet IDs associated with the simulation job.

      - *(string) --*

    - **securityGroups** *(list) --*

      A list of security group IDs associated with the simulation job.

      - *(string) --*

    - **vpcId** *(string) --*

      The VPC ID associated with your simulation job.

    - **assignPublicIp** *(boolean) --*

      A boolean indicating if a public IP was assigned.
    """


_ClientDescribeSimulationJobResponseTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": str,
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": str,
        "failureCode": str,
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": ClientDescribeSimulationJobResponseoutputLocationTypeDef,
        "loggingConfig": ClientDescribeSimulationJobResponseloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[
            ClientDescribeSimulationJobResponserobotApplicationsTypeDef
        ],
        "simulationApplications": List[
            ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef
        ],
        "dataSources": List[ClientDescribeSimulationJobResponsedataSourcesTypeDef],
        "tags": Dict[str, str],
        "vpcConfig": ClientDescribeSimulationJobResponsevpcConfigTypeDef,
        "networkInterface": ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef,
    },
    total=False,
)


class ClientDescribeSimulationJobResponseTypeDef(
    _ClientDescribeSimulationJobResponseTypeDef
):
    """
    Type definition for `ClientDescribeSimulationJob` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the simulation job.

    - **name** *(string) --*

      The name of the simulation job.

    - **status** *(string) --*

      The status of the simulation job.

    - **lastStartedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation job was last started.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation job was last updated.

    - **failureBehavior** *(string) --*

      The failure behavior for the simulation job.

    - **failureCode** *(string) --*

      The failure code of the simulation job if it failed:

        InternalServiceError

      Internal service error.

        RobotApplicationCrash

      Robot application exited abnormally.

        SimulationApplicationCrash

      Simulation application exited abnormally.

        BadPermissionsRobotApplication

      Robot application bundle could not be downloaded.

        BadPermissionsSimulationApplication

      Simulation application bundle could not be downloaded.

        BadPermissionsS3Output

      Unable to publish outputs to customer-provided S3 bucket.

        BadPermissionsCloudwatchLogs

      Unable to publish logs to customer-provided CloudWatch Logs resource.

        SubnetIpLimitExceeded

      Subnet IP limit exceeded.

        ENILimitExceeded

      ENI limit exceeded.

        BadPermissionsUserCredentials

      Unable to use the Role provided.

        InvalidBundleRobotApplication

      Robot bundle cannot be extracted (invalid format, bundling error, or other issue).

        InvalidBundleSimulationApplication

      Simulation bundle cannot be extracted (invalid format, bundling error, or other issue).

        RobotApplicationVersionMismatchedEtag

      Etag for RobotApplication does not match value during version creation.

        SimulationApplicationVersionMismatchedEtag

      Etag for SimulationApplication does not match value during version creation.

    - **failureReason** *(string) --*

      Details about why the simulation job failed. For more information about troubleshooting, see
      `Troubleshooting <https://docs.aws.amazon.com/robomaker/latest/dg/troubleshooting.html>`__ .

    - **clientRequestToken** *(string) --*

      Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    - **outputLocation** *(dict) --*

      Location for output files generated by the simulation job.

      - **s3Bucket** *(string) --*

        The S3 bucket for output.

      - **s3Prefix** *(string) --*

        The S3 folder in the ``s3Bucket`` where output files will be placed.

    - **loggingConfig** *(dict) --*

      The logging configuration.

      - **recordAllRosTopics** *(boolean) --*

        A boolean indicating whether to record all ROS topics.

    - **maxJobDurationInSeconds** *(integer) --*

      The maximum job duration in seconds. The value must be 8 days (691,200 seconds) or less.

    - **simulationTimeMillis** *(integer) --*

      The simulation job execution duration in milliseconds.

    - **iamRole** *(string) --*

      The IAM role that allows the simulation instance to call the AWS APIs that are specified in
      its associated policies on your behalf.

    - **robotApplications** *(list) --*

      A list of robot applications.

      - *(dict) --*

        Application configuration information for a robot.

        - **application** *(string) --*

          The application information for the robot application.

        - **applicationVersion** *(string) --*

          The version of the robot application.

        - **launchConfig** *(dict) --*

          The launch configuration for the robot application.

          - **packageName** *(string) --*

            The package name.

          - **launchFile** *(string) --*

            The launch file name.

          - **environmentVariables** *(dict) --*

            The environment variables for the application launch.

            - *(string) --*

              - *(string) --*

          - **portForwardingConfig** *(dict) --*

            The port forwarding configuration.

            - **portMappings** *(list) --*

              The port mappings for the configuration.

              - *(dict) --*

                An object representing a port mapping.

                - **jobPort** *(integer) --*

                  The port number on the simulation job instance to use as a remote connection
                  point.

                - **applicationPort** *(integer) --*

                  The port number on the application.

                - **enableOnPublicIp** *(boolean) --*

                  A Boolean indicating whether to enable this port mapping on public IP.

    - **simulationApplications** *(list) --*

      A list of simulation applications.

      - *(dict) --*

        Information about a simulation application configuration.

        - **application** *(string) --*

          The application information for the simulation application.

        - **applicationVersion** *(string) --*

          The version of the simulation application.

        - **launchConfig** *(dict) --*

          The launch configuration for the simulation application.

          - **packageName** *(string) --*

            The package name.

          - **launchFile** *(string) --*

            The launch file name.

          - **environmentVariables** *(dict) --*

            The environment variables for the application launch.

            - *(string) --*

              - *(string) --*

          - **portForwardingConfig** *(dict) --*

            The port forwarding configuration.

            - **portMappings** *(list) --*

              The port mappings for the configuration.

              - *(dict) --*

                An object representing a port mapping.

                - **jobPort** *(integer) --*

                  The port number on the simulation job instance to use as a remote connection
                  point.

                - **applicationPort** *(integer) --*

                  The port number on the application.

                - **enableOnPublicIp** *(boolean) --*

                  A Boolean indicating whether to enable this port mapping on public IP.

    - **dataSources** *(list) --*

      The data sources for the simulation job.

      - *(dict) --*

        Information about a data source.

        - **name** *(string) --*

          The name of the data source.

        - **s3Bucket** *(string) --*

          The S3 bucket where the data files are located.

        - **s3Keys** *(list) --*

          The list of S3 keys identifying the data source files.

          - *(dict) --*

            Information about S3 keys.

            - **s3Key** *(string) --*

              The S3 key.

            - **etag** *(string) --*

              The etag for the object.

    - **tags** *(dict) --*

      The list of all tags added to the specified simulation job.

      - *(string) --*

        - *(string) --*

    - **vpcConfig** *(dict) --*

      The VPC configuration.

      - **subnets** *(list) --*

        A list of subnet IDs associated with the simulation job.

        - *(string) --*

      - **securityGroups** *(list) --*

        A list of security group IDs associated with the simulation job.

        - *(string) --*

      - **vpcId** *(string) --*

        The VPC ID associated with your simulation job.

      - **assignPublicIp** *(boolean) --*

        A boolean indicating if a public IP was assigned.

    - **networkInterface** *(dict) --*

      The network interface information for the simulation job.

      - **networkInterfaceId** *(string) --*

        The ID of the network interface.

      - **privateIpAddress** *(string) --*

        The IPv4 address of the network interface within the subnet.

      - **publicIpAddress** *(string) --*

        The IPv4 public address of the network interface.
    """


_ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "_ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)


class ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef(
    _ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef
):
    """
    Type definition for `ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigs` `launchConfig`

    The launch configuration.

    - **packageName** *(string) --*

      The package name.

    - **preLaunchFile** *(string) --*

      The deployment pre-launch file. This file will be executed prior to the launch file.

    - **launchFile** *(string) --*

      The launch file name.

    - **postLaunchFile** *(string) --*

      The deployment post-launch file. This file will be executed after the launch file.

    - **environmentVariables** *(dict) --*

      An array of key/value pairs specifying environment variables for the robot
      application

      - *(string) --*

        - *(string) --*
    """


_ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef = TypedDict(
    "_ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)


class ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef(
    _ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef
):
    """
    Type definition for `ClientListDeploymentJobsResponsedeploymentJobs` `deploymentApplicationConfigs`

    Information about a deployment application configuration.

    - **application** *(string) --*

      The Amazon Resource Name (ARN) of the robot application.

    - **applicationVersion** *(string) --*

      The version of the application.

    - **launchConfig** *(dict) --*

      The launch configuration.

      - **packageName** *(string) --*

        The package name.

      - **preLaunchFile** *(string) --*

        The deployment pre-launch file. This file will be executed prior to the launch file.

      - **launchFile** *(string) --*

        The launch file name.

      - **postLaunchFile** *(string) --*

        The deployment post-launch file. This file will be executed after the launch file.

      - **environmentVariables** *(dict) --*

        An array of key/value pairs specifying environment variables for the robot
        application

        - *(string) --*

          - *(string) --*
    """


_ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "_ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)


class ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef(
    _ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef
):
    """
    Type definition for `ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfig` `downloadConditionFile`

    The download condition file.

    - **bucket** *(string) --*

      The bucket containing the object.

    - **key** *(string) --*

      The key of the object.

    - **etag** *(string) --*

      The etag of the object.
    """


_ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef = TypedDict(
    "_ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)


class ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef(
    _ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef
):
    """
    Type definition for `ClientListDeploymentJobsResponsedeploymentJobs` `deploymentConfig`

    The deployment configuration.

    - **concurrentDeploymentPercentage** *(integer) --*

      The percentage of robots receiving the deployment at the same time.

    - **failureThresholdPercentage** *(integer) --*

      The percentage of deployments that need to fail before stopping deployment.

    - **robotDeploymentTimeoutInSeconds** *(integer) --*

      The amount of time, in seconds, to wait for deployment to a single robot to complete.
      Choose a time between 1 minute and 7 days. The default is 5 hours.

    - **downloadConditionFile** *(dict) --*

      The download condition file.

      - **bucket** *(string) --*

        The bucket containing the object.

      - **key** *(string) --*

        The key of the object.

      - **etag** *(string) --*

        The etag of the object.
    """


_ClientListDeploymentJobsResponsedeploymentJobsTypeDef = TypedDict(
    "_ClientListDeploymentJobsResponsedeploymentJobsTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": str,
        "deploymentApplicationConfigs": List[
            ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef
        ],
        "deploymentConfig": ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef,
        "failureReason": str,
        "failureCode": str,
        "createdAt": datetime,
    },
    total=False,
)


class ClientListDeploymentJobsResponsedeploymentJobsTypeDef(
    _ClientListDeploymentJobsResponsedeploymentJobsTypeDef
):
    """
    Type definition for `ClientListDeploymentJobsResponse` `deploymentJobs`

    Information about a deployment job.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the deployment job.

    - **fleet** *(string) --*

      The Amazon Resource Name (ARN) of the fleet.

    - **status** *(string) --*

      The status of the deployment job.

    - **deploymentApplicationConfigs** *(list) --*

      The deployment application configuration.

      - *(dict) --*

        Information about a deployment application configuration.

        - **application** *(string) --*

          The Amazon Resource Name (ARN) of the robot application.

        - **applicationVersion** *(string) --*

          The version of the application.

        - **launchConfig** *(dict) --*

          The launch configuration.

          - **packageName** *(string) --*

            The package name.

          - **preLaunchFile** *(string) --*

            The deployment pre-launch file. This file will be executed prior to the launch file.

          - **launchFile** *(string) --*

            The launch file name.

          - **postLaunchFile** *(string) --*

            The deployment post-launch file. This file will be executed after the launch file.

          - **environmentVariables** *(dict) --*

            An array of key/value pairs specifying environment variables for the robot
            application

            - *(string) --*

              - *(string) --*

    - **deploymentConfig** *(dict) --*

      The deployment configuration.

      - **concurrentDeploymentPercentage** *(integer) --*

        The percentage of robots receiving the deployment at the same time.

      - **failureThresholdPercentage** *(integer) --*

        The percentage of deployments that need to fail before stopping deployment.

      - **robotDeploymentTimeoutInSeconds** *(integer) --*

        The amount of time, in seconds, to wait for deployment to a single robot to complete.
        Choose a time between 1 minute and 7 days. The default is 5 hours.

      - **downloadConditionFile** *(dict) --*

        The download condition file.

        - **bucket** *(string) --*

          The bucket containing the object.

        - **key** *(string) --*

          The key of the object.

        - **etag** *(string) --*

          The etag of the object.

    - **failureReason** *(string) --*

      A short description of the reason why the deployment job failed.

    - **failureCode** *(string) --*

      The deployment job failure code.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the deployment job was created.
    """


_ClientListDeploymentJobsResponseTypeDef = TypedDict(
    "_ClientListDeploymentJobsResponseTypeDef",
    {
        "deploymentJobs": List[ClientListDeploymentJobsResponsedeploymentJobsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListDeploymentJobsResponseTypeDef(_ClientListDeploymentJobsResponseTypeDef):
    """
    Type definition for `ClientListDeploymentJobs` `Response`

    - **deploymentJobs** *(list) --*

      A list of deployment jobs that meet the criteria of the request.

      - *(dict) --*

        Information about a deployment job.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the deployment job.

        - **fleet** *(string) --*

          The Amazon Resource Name (ARN) of the fleet.

        - **status** *(string) --*

          The status of the deployment job.

        - **deploymentApplicationConfigs** *(list) --*

          The deployment application configuration.

          - *(dict) --*

            Information about a deployment application configuration.

            - **application** *(string) --*

              The Amazon Resource Name (ARN) of the robot application.

            - **applicationVersion** *(string) --*

              The version of the application.

            - **launchConfig** *(dict) --*

              The launch configuration.

              - **packageName** *(string) --*

                The package name.

              - **preLaunchFile** *(string) --*

                The deployment pre-launch file. This file will be executed prior to the launch file.

              - **launchFile** *(string) --*

                The launch file name.

              - **postLaunchFile** *(string) --*

                The deployment post-launch file. This file will be executed after the launch file.

              - **environmentVariables** *(dict) --*

                An array of key/value pairs specifying environment variables for the robot
                application

                - *(string) --*

                  - *(string) --*

        - **deploymentConfig** *(dict) --*

          The deployment configuration.

          - **concurrentDeploymentPercentage** *(integer) --*

            The percentage of robots receiving the deployment at the same time.

          - **failureThresholdPercentage** *(integer) --*

            The percentage of deployments that need to fail before stopping deployment.

          - **robotDeploymentTimeoutInSeconds** *(integer) --*

            The amount of time, in seconds, to wait for deployment to a single robot to complete.
            Choose a time between 1 minute and 7 days. The default is 5 hours.

          - **downloadConditionFile** *(dict) --*

            The download condition file.

            - **bucket** *(string) --*

              The bucket containing the object.

            - **key** *(string) --*

              The key of the object.

            - **etag** *(string) --*

              The etag of the object.

        - **failureReason** *(string) --*

          A short description of the reason why the deployment job failed.

        - **failureCode** *(string) --*

          The deployment job failure code.

        - **createdAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the deployment job was created.

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListDeploymentJobs`` request. When the
      results of a ``ListDeploymentJobs`` request exceed ``maxResults`` , this value can be used to
      retrieve the next page of results. This value is ``null`` when there are no more results to
      return.
    """


_ClientListDeploymentJobsfiltersTypeDef = TypedDict(
    "_ClientListDeploymentJobsfiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientListDeploymentJobsfiltersTypeDef(_ClientListDeploymentJobsfiltersTypeDef):
    """
    Type definition for `ClientListDeploymentJobs` `filters`

    Information about a filter.

    - **name** *(string) --*

      The name of the filter.

    - **values** *(list) --*

      A list of values.

      - *(string) --*
    """


_ClientListFleetsResponsefleetDetailsTypeDef = TypedDict(
    "_ClientListFleetsResponsefleetDetailsTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "lastDeploymentStatus": str,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)


class ClientListFleetsResponsefleetDetailsTypeDef(
    _ClientListFleetsResponsefleetDetailsTypeDef
):
    """
    Type definition for `ClientListFleetsResponse` `fleetDetails`

    Information about a fleet.

    - **name** *(string) --*

      The name of the fleet.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the fleet.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the fleet was created.

    - **lastDeploymentStatus** *(string) --*

      The status of the last fleet deployment.

    - **lastDeploymentJob** *(string) --*

      The Amazon Resource Name (ARN) of the last deployment job.

    - **lastDeploymentTime** *(datetime) --*

      The time of the last deployment.
    """


_ClientListFleetsResponseTypeDef = TypedDict(
    "_ClientListFleetsResponseTypeDef",
    {
        "fleetDetails": List[ClientListFleetsResponsefleetDetailsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListFleetsResponseTypeDef(_ClientListFleetsResponseTypeDef):
    """
    Type definition for `ClientListFleets` `Response`

    - **fleetDetails** *(list) --*

      A list of fleet details meeting the request criteria.

      - *(dict) --*

        Information about a fleet.

        - **name** *(string) --*

          The name of the fleet.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the fleet.

        - **createdAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the fleet was created.

        - **lastDeploymentStatus** *(string) --*

          The status of the last fleet deployment.

        - **lastDeploymentJob** *(string) --*

          The Amazon Resource Name (ARN) of the last deployment job.

        - **lastDeploymentTime** *(datetime) --*

          The time of the last deployment.

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListDeploymentJobs`` request. When the
      results of a ``ListFleets`` request exceed ``maxResults`` , this value can be used to
      retrieve the next page of results. This value is ``null`` when there are no more results to
      return.
    """


_ClientListFleetsfiltersTypeDef = TypedDict(
    "_ClientListFleetsfiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ClientListFleetsfiltersTypeDef(_ClientListFleetsfiltersTypeDef):
    """
    Type definition for `ClientListFleets` `filters`

    Information about a filter.

    - **name** *(string) --*

      The name of the filter.

    - **values** *(list) --*

      A list of values.

      - *(string) --*
    """


_ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef(
    _ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientListRobotApplicationsResponserobotApplicationSummaries` `robotSoftwareSuite`

    Information about a robot software suite.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef = TypedDict(
    "_ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef,
    },
    total=False,
)


class ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef(
    _ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef
):
    """
    Type definition for `ClientListRobotApplicationsResponse` `robotApplicationSummaries`

    Summary information for a robot application.

    - **name** *(string) --*

      The name of the robot application.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the robot.

    - **version** *(string) --*

      The version of the robot application.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the robot application was last updated.

    - **robotSoftwareSuite** *(dict) --*

      Information about a robot software suite.

      - **name** *(string) --*

        The name of the robot software suite.

      - **version** *(string) --*

        The version of the robot software suite.
    """


_ClientListRobotApplicationsResponseTypeDef = TypedDict(
    "_ClientListRobotApplicationsResponseTypeDef",
    {
        "robotApplicationSummaries": List[
            ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListRobotApplicationsResponseTypeDef(
    _ClientListRobotApplicationsResponseTypeDef
):
    """
    Type definition for `ClientListRobotApplications` `Response`

    - **robotApplicationSummaries** *(list) --*

      A list of robot application summaries that meet the criteria of the request.

      - *(dict) --*

        Summary information for a robot application.

        - **name** *(string) --*

          The name of the robot application.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the robot.

        - **version** *(string) --*

          The version of the robot application.

        - **lastUpdatedAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the robot application was last updated.

        - **robotSoftwareSuite** *(dict) --*

          Information about a robot software suite.

          - **name** *(string) --*

            The name of the robot software suite.

          - **version** *(string) --*

            The version of the robot software suite.

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListRobotApplications`` request. When the
      results of a ``ListRobotApplications`` request exceed ``maxResults`` , this value can be used
      to retrieve the next page of results. This value is ``null`` when there are no more results
      to return.
    """


_ClientListRobotApplicationsfiltersTypeDef = TypedDict(
    "_ClientListRobotApplicationsfiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientListRobotApplicationsfiltersTypeDef(
    _ClientListRobotApplicationsfiltersTypeDef
):
    """
    Type definition for `ClientListRobotApplications` `filters`

    Information about a filter.

    - **name** *(string) --*

      The name of the filter.

    - **values** *(list) --*

      A list of values.

      - *(string) --*
    """


_ClientListRobotsResponserobotsTypeDef = TypedDict(
    "_ClientListRobotsResponserobotsTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": str,
        "greenGrassGroupId": str,
        "createdAt": datetime,
        "architecture": str,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)


class ClientListRobotsResponserobotsTypeDef(_ClientListRobotsResponserobotsTypeDef):
    """
    Type definition for `ClientListRobotsResponse` `robots`

    Information about a robot.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the robot.

    - **name** *(string) --*

      The name of the robot.

    - **fleetArn** *(string) --*

      The Amazon Resource Name (ARN) of the fleet.

    - **status** *(string) --*

      The status of the robot.

    - **greenGrassGroupId** *(string) --*

      The Greengrass group associated with the robot.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the robot was created.

    - **architecture** *(string) --*

      The architecture of the robot.

    - **lastDeploymentJob** *(string) --*

      The Amazon Resource Name (ARN) of the last deployment job.

    - **lastDeploymentTime** *(datetime) --*

      The time of the last deployment.
    """


_ClientListRobotsResponseTypeDef = TypedDict(
    "_ClientListRobotsResponseTypeDef",
    {"robots": List[ClientListRobotsResponserobotsTypeDef], "nextToken": str},
    total=False,
)


class ClientListRobotsResponseTypeDef(_ClientListRobotsResponseTypeDef):
    """
    Type definition for `ClientListRobots` `Response`

    - **robots** *(list) --*

      A list of robots that meet the criteria of the request.

      - *(dict) --*

        Information about a robot.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the robot.

        - **name** *(string) --*

          The name of the robot.

        - **fleetArn** *(string) --*

          The Amazon Resource Name (ARN) of the fleet.

        - **status** *(string) --*

          The status of the robot.

        - **greenGrassGroupId** *(string) --*

          The Greengrass group associated with the robot.

        - **createdAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the robot was created.

        - **architecture** *(string) --*

          The architecture of the robot.

        - **lastDeploymentJob** *(string) --*

          The Amazon Resource Name (ARN) of the last deployment job.

        - **lastDeploymentTime** *(datetime) --*

          The time of the last deployment.

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListRobots`` request. When the results of a
      ``ListRobot`` request exceed ``maxResults`` , this value can be used to retrieve the next
      page of results. This value is ``null`` when there are no more results to return.
    """


_ClientListRobotsfiltersTypeDef = TypedDict(
    "_ClientListRobotsfiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ClientListRobotsfiltersTypeDef(_ClientListRobotsfiltersTypeDef):
    """
    Type definition for `ClientListRobots` `filters`

    Information about a filter.

    - **name** *(string) --*

      The name of the filter.

    - **values** *(list) --*

      A list of values.

      - *(string) --*
    """


_ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef(
    _ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientListSimulationApplicationsResponsesimulationApplicationSummaries` `robotSoftwareSuite`

    Information about a robot software suite.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef(
    _ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientListSimulationApplicationsResponsesimulationApplicationSummaries` `simulationSoftwareSuite`

    Information about a simulation software suite.

    - **name** *(string) --*

      The name of the simulation software suite.

    - **version** *(string) --*

      The version of the simulation software suite.
    """


_ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef = TypedDict(
    "_ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef,
        "simulationSoftwareSuite": ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef,
    },
    total=False,
)


class ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef(
    _ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef
):
    """
    Type definition for `ClientListSimulationApplicationsResponse` `simulationApplicationSummaries`

    Summary information for a simulation application.

    - **name** *(string) --*

      The name of the simulation application.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the simulation application.

    - **version** *(string) --*

      The version of the simulation application.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation application was last
      updated.

    - **robotSoftwareSuite** *(dict) --*

      Information about a robot software suite.

      - **name** *(string) --*

        The name of the robot software suite.

      - **version** *(string) --*

        The version of the robot software suite.

    - **simulationSoftwareSuite** *(dict) --*

      Information about a simulation software suite.

      - **name** *(string) --*

        The name of the simulation software suite.

      - **version** *(string) --*

        The version of the simulation software suite.
    """


_ClientListSimulationApplicationsResponseTypeDef = TypedDict(
    "_ClientListSimulationApplicationsResponseTypeDef",
    {
        "simulationApplicationSummaries": List[
            ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListSimulationApplicationsResponseTypeDef(
    _ClientListSimulationApplicationsResponseTypeDef
):
    """
    Type definition for `ClientListSimulationApplications` `Response`

    - **simulationApplicationSummaries** *(list) --*

      A list of simulation application summaries that meet the criteria of the request.

      - *(dict) --*

        Summary information for a simulation application.

        - **name** *(string) --*

          The name of the simulation application.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the simulation application.

        - **version** *(string) --*

          The version of the simulation application.

        - **lastUpdatedAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the simulation application was last
          updated.

        - **robotSoftwareSuite** *(dict) --*

          Information about a robot software suite.

          - **name** *(string) --*

            The name of the robot software suite.

          - **version** *(string) --*

            The version of the robot software suite.

        - **simulationSoftwareSuite** *(dict) --*

          Information about a simulation software suite.

          - **name** *(string) --*

            The name of the simulation software suite.

          - **version** *(string) --*

            The version of the simulation software suite.

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListSimulationApplications`` request. When
      the results of a ``ListRobot`` request exceed ``maxResults`` , this value can be used to
      retrieve the next page of results. This value is ``null`` when there are no more results to
      return.
    """


_ClientListSimulationApplicationsfiltersTypeDef = TypedDict(
    "_ClientListSimulationApplicationsfiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientListSimulationApplicationsfiltersTypeDef(
    _ClientListSimulationApplicationsfiltersTypeDef
):
    """
    Type definition for `ClientListSimulationApplications` `filters`

    Information about a filter.

    - **name** *(string) --*

      The name of the filter.

    - **values** *(list) --*

      A list of values.

      - *(string) --*
    """


_ClientListSimulationJobsResponsesimulationJobSummariesTypeDef = TypedDict(
    "_ClientListSimulationJobsResponsesimulationJobSummariesTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": str,
        "simulationApplicationNames": List[str],
        "robotApplicationNames": List[str],
        "dataSourceNames": List[str],
    },
    total=False,
)


class ClientListSimulationJobsResponsesimulationJobSummariesTypeDef(
    _ClientListSimulationJobsResponsesimulationJobSummariesTypeDef
):
    """
    Type definition for `ClientListSimulationJobsResponse` `simulationJobSummaries`

    Summary information for a simulation job.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the simulation job.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation job was last updated.

    - **name** *(string) --*

      The name of the simulation job.

    - **status** *(string) --*

      The status of the simulation job.

    - **simulationApplicationNames** *(list) --*

      A list of simulation job simulation application names.

      - *(string) --*

    - **robotApplicationNames** *(list) --*

      A list of simulation job robot application names.

      - *(string) --*

    - **dataSourceNames** *(list) --*

      The names of the data sources.

      - *(string) --*
    """


_ClientListSimulationJobsResponseTypeDef = TypedDict(
    "_ClientListSimulationJobsResponseTypeDef",
    {
        "simulationJobSummaries": List[
            ClientListSimulationJobsResponsesimulationJobSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListSimulationJobsResponseTypeDef(_ClientListSimulationJobsResponseTypeDef):
    """
    Type definition for `ClientListSimulationJobs` `Response`

    - **simulationJobSummaries** *(list) --*

      A list of simulation job summaries that meet the criteria of the request.

      - *(dict) --*

        Summary information for a simulation job.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the simulation job.

        - **lastUpdatedAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the simulation job was last updated.

        - **name** *(string) --*

          The name of the simulation job.

        - **status** *(string) --*

          The status of the simulation job.

        - **simulationApplicationNames** *(list) --*

          A list of simulation job simulation application names.

          - *(string) --*

        - **robotApplicationNames** *(list) --*

          A list of simulation job robot application names.

          - *(string) --*

        - **dataSourceNames** *(list) --*

          The names of the data sources.

          - *(string) --*

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListSimulationJobs`` request. When the
      results of a ``ListRobot`` request exceed ``maxResults`` , this value can be used to retrieve
      the next page of results. This value is ``null`` when there are no more results to return.
    """


_ClientListSimulationJobsfiltersTypeDef = TypedDict(
    "_ClientListSimulationJobsfiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientListSimulationJobsfiltersTypeDef(_ClientListSimulationJobsfiltersTypeDef):
    """
    Type definition for `ClientListSimulationJobs` `filters`

    Information about a filter.

    - **name** *(string) --*

      The name of the filter.

    - **values** *(list) --*

      A list of values.

      - *(string) --*
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(dict) --*

      The list of all tags added to the specified resource.

      - *(string) --*

        - *(string) --*
    """


_ClientRegisterRobotResponseTypeDef = TypedDict(
    "_ClientRegisterRobotResponseTypeDef", {"fleet": str, "robot": str}, total=False
)


class ClientRegisterRobotResponseTypeDef(_ClientRegisterRobotResponseTypeDef):
    """
    Type definition for `ClientRegisterRobot` `Response`

    - **fleet** *(string) --*

      The Amazon Resource Name (ARN) of the fleet that the robot will join.

    - **robot** *(string) --*

      Information about the robot registration.
    """


_ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "_ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)


class ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef(
    _ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef
):
    """
    Type definition for `ClientSyncDeploymentJobResponsedeploymentApplicationConfigs` `launchConfig`

    The launch configuration.

    - **packageName** *(string) --*

      The package name.

    - **preLaunchFile** *(string) --*

      The deployment pre-launch file. This file will be executed prior to the launch file.

    - **launchFile** *(string) --*

      The launch file name.

    - **postLaunchFile** *(string) --*

      The deployment post-launch file. This file will be executed after the launch file.

    - **environmentVariables** *(dict) --*

      An array of key/value pairs specifying environment variables for the robot application

      - *(string) --*

        - *(string) --*
    """


_ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef = TypedDict(
    "_ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)


class ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef(
    _ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef
):
    """
    Type definition for `ClientSyncDeploymentJobResponse` `deploymentApplicationConfigs`

    Information about a deployment application configuration.

    - **application** *(string) --*

      The Amazon Resource Name (ARN) of the robot application.

    - **applicationVersion** *(string) --*

      The version of the application.

    - **launchConfig** *(dict) --*

      The launch configuration.

      - **packageName** *(string) --*

        The package name.

      - **preLaunchFile** *(string) --*

        The deployment pre-launch file. This file will be executed prior to the launch file.

      - **launchFile** *(string) --*

        The launch file name.

      - **postLaunchFile** *(string) --*

        The deployment post-launch file. This file will be executed after the launch file.

      - **environmentVariables** *(dict) --*

        An array of key/value pairs specifying environment variables for the robot application

        - *(string) --*

          - *(string) --*
    """


_ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "_ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)


class ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef(
    _ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef
):
    """
    Type definition for `ClientSyncDeploymentJobResponsedeploymentConfig` `downloadConditionFile`

    The download condition file.

    - **bucket** *(string) --*

      The bucket containing the object.

    - **key** *(string) --*

      The key of the object.

    - **etag** *(string) --*

      The etag of the object.
    """


_ClientSyncDeploymentJobResponsedeploymentConfigTypeDef = TypedDict(
    "_ClientSyncDeploymentJobResponsedeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)


class ClientSyncDeploymentJobResponsedeploymentConfigTypeDef(
    _ClientSyncDeploymentJobResponsedeploymentConfigTypeDef
):
    """
    Type definition for `ClientSyncDeploymentJobResponse` `deploymentConfig`

    Information about the deployment configuration.

    - **concurrentDeploymentPercentage** *(integer) --*

      The percentage of robots receiving the deployment at the same time.

    - **failureThresholdPercentage** *(integer) --*

      The percentage of deployments that need to fail before stopping deployment.

    - **robotDeploymentTimeoutInSeconds** *(integer) --*

      The amount of time, in seconds, to wait for deployment to a single robot to complete.
      Choose a time between 1 minute and 7 days. The default is 5 hours.

    - **downloadConditionFile** *(dict) --*

      The download condition file.

      - **bucket** *(string) --*

        The bucket containing the object.

      - **key** *(string) --*

        The key of the object.

      - **etag** *(string) --*

        The etag of the object.
    """


_ClientSyncDeploymentJobResponseTypeDef = TypedDict(
    "_ClientSyncDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": str,
        "deploymentConfig": ClientSyncDeploymentJobResponsedeploymentConfigTypeDef,
        "deploymentApplicationConfigs": List[
            ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef
        ],
        "failureReason": str,
        "failureCode": str,
        "createdAt": datetime,
    },
    total=False,
)


class ClientSyncDeploymentJobResponseTypeDef(_ClientSyncDeploymentJobResponseTypeDef):
    """
    Type definition for `ClientSyncDeploymentJob` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the synchronization request.

    - **fleet** *(string) --*

      The Amazon Resource Name (ARN) of the fleet.

    - **status** *(string) --*

      The status of the synchronization job.

    - **deploymentConfig** *(dict) --*

      Information about the deployment configuration.

      - **concurrentDeploymentPercentage** *(integer) --*

        The percentage of robots receiving the deployment at the same time.

      - **failureThresholdPercentage** *(integer) --*

        The percentage of deployments that need to fail before stopping deployment.

      - **robotDeploymentTimeoutInSeconds** *(integer) --*

        The amount of time, in seconds, to wait for deployment to a single robot to complete.
        Choose a time between 1 minute and 7 days. The default is 5 hours.

      - **downloadConditionFile** *(dict) --*

        The download condition file.

        - **bucket** *(string) --*

          The bucket containing the object.

        - **key** *(string) --*

          The key of the object.

        - **etag** *(string) --*

          The etag of the object.

    - **deploymentApplicationConfigs** *(list) --*

      Information about the deployment application configurations.

      - *(dict) --*

        Information about a deployment application configuration.

        - **application** *(string) --*

          The Amazon Resource Name (ARN) of the robot application.

        - **applicationVersion** *(string) --*

          The version of the application.

        - **launchConfig** *(dict) --*

          The launch configuration.

          - **packageName** *(string) --*

            The package name.

          - **preLaunchFile** *(string) --*

            The deployment pre-launch file. This file will be executed prior to the launch file.

          - **launchFile** *(string) --*

            The launch file name.

          - **postLaunchFile** *(string) --*

            The deployment post-launch file. This file will be executed after the launch file.

          - **environmentVariables** *(dict) --*

            An array of key/value pairs specifying environment variables for the robot application

            - *(string) --*

              - *(string) --*

    - **failureReason** *(string) --*

      The failure reason if the job fails.

    - **failureCode** *(string) --*

      The failure code if the job fails:

        InternalServiceError

      Internal service error.

        RobotApplicationCrash

      Robot application exited abnormally.

        SimulationApplicationCrash

      Simulation application exited abnormally.

        BadPermissionsRobotApplication

      Robot application bundle could not be downloaded.

        BadPermissionsSimulationApplication

      Simulation application bundle could not be downloaded.

        BadPermissionsS3Output

      Unable to publish outputs to customer-provided S3 bucket.

        BadPermissionsCloudwatchLogs

      Unable to publish logs to customer-provided CloudWatch Logs resource.

        SubnetIpLimitExceeded

      Subnet IP limit exceeded.

        ENILimitExceeded

      ENI limit exceeded.

        BadPermissionsUserCredentials

      Unable to use the Role provided.

        InvalidBundleRobotApplication

      Robot bundle cannot be extracted (invalid format, bundling error, or other issue).

        InvalidBundleSimulationApplication

      Simulation bundle cannot be extracted (invalid format, bundling error, or other issue).

        RobotApplicationVersionMismatchedEtag

      Etag for RobotApplication does not match value during version creation.

        SimulationApplicationVersionMismatchedEtag

      Etag for SimulationApplication does not match value during version creation.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the fleet was created.
    """


_ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef(
    _ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientUpdateRobotApplicationResponse` `robotSoftwareSuite`

    The robot software suite used by the robot application.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientUpdateRobotApplicationResponsesourcesTypeDef = TypedDict(
    "_ClientUpdateRobotApplicationResponsesourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "etag": str, "architecture": str},
    total=False,
)


class ClientUpdateRobotApplicationResponsesourcesTypeDef(
    _ClientUpdateRobotApplicationResponsesourcesTypeDef
):
    """
    Type definition for `ClientUpdateRobotApplicationResponse` `sources`

    Information about a source.

    - **s3Bucket** *(string) --*

      The s3 bucket name.

    - **s3Key** *(string) --*

      The s3 object key.

    - **etag** *(string) --*

      A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

    - **architecture** *(string) --*

      The taget processor architecture for the application.
    """


_ClientUpdateRobotApplicationResponseTypeDef = TypedDict(
    "_ClientUpdateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientUpdateRobotApplicationResponsesourcesTypeDef],
        "robotSoftwareSuite": ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)


class ClientUpdateRobotApplicationResponseTypeDef(
    _ClientUpdateRobotApplicationResponseTypeDef
):
    """
    Type definition for `ClientUpdateRobotApplication` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the updated robot application.

    - **name** *(string) --*

      The name of the robot application.

    - **version** *(string) --*

      The version of the robot application.

    - **sources** *(list) --*

      The sources of the robot application.

      - *(dict) --*

        Information about a source.

        - **s3Bucket** *(string) --*

          The s3 bucket name.

        - **s3Key** *(string) --*

          The s3 object key.

        - **etag** *(string) --*

          A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

        - **architecture** *(string) --*

          The taget processor architecture for the application.

    - **robotSoftwareSuite** *(dict) --*

      The robot software suite used by the robot application.

      - **name** *(string) --*

        The name of the robot software suite.

      - **version** *(string) --*

        The version of the robot software suite.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the robot application was last updated.

    - **revisionId** *(string) --*

      The revision id of the robot application.
    """


_ClientUpdateRobotApplicationrobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientUpdateRobotApplicationrobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientUpdateRobotApplicationrobotSoftwareSuiteTypeDef(
    _ClientUpdateRobotApplicationrobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientUpdateRobotApplication` `robotSoftwareSuite`

    The robot software suite used by the robot application.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientUpdateRobotApplicationsourcesTypeDef = TypedDict(
    "_ClientUpdateRobotApplicationsourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": str},
    total=False,
)


class ClientUpdateRobotApplicationsourcesTypeDef(
    _ClientUpdateRobotApplicationsourcesTypeDef
):
    """
    Type definition for `ClientUpdateRobotApplication` `sources`

    Information about a source configuration.

    - **s3Bucket** *(string) --*

      The Amazon S3 bucket name.

    - **s3Key** *(string) --*

      The s3 object key.

    - **architecture** *(string) --*

      The target processor architecture for the application.
    """


_ClientUpdateSimulationApplicationResponserenderingEngineTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationResponserenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientUpdateSimulationApplicationResponserenderingEngineTypeDef(
    _ClientUpdateSimulationApplicationResponserenderingEngineTypeDef
):
    """
    Type definition for `ClientUpdateSimulationApplicationResponse` `renderingEngine`

    The rendering engine for the simulation application.

    - **name** *(string) --*

      The name of the rendering engine.

    - **version** *(string) --*

      The version of the rendering engine.
    """


_ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef(
    _ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientUpdateSimulationApplicationResponse` `robotSoftwareSuite`

    Information about the robot software suite.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef(
    _ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientUpdateSimulationApplicationResponse` `simulationSoftwareSuite`

    The simulation software suite used by the simulation application.

    - **name** *(string) --*

      The name of the simulation software suite.

    - **version** *(string) --*

      The version of the simulation software suite.
    """


_ClientUpdateSimulationApplicationResponsesourcesTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationResponsesourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "etag": str, "architecture": str},
    total=False,
)


class ClientUpdateSimulationApplicationResponsesourcesTypeDef(
    _ClientUpdateSimulationApplicationResponsesourcesTypeDef
):
    """
    Type definition for `ClientUpdateSimulationApplicationResponse` `sources`

    Information about a source.

    - **s3Bucket** *(string) --*

      The s3 bucket name.

    - **s3Key** *(string) --*

      The s3 object key.

    - **etag** *(string) --*

      A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

    - **architecture** *(string) --*

      The taget processor architecture for the application.
    """


_ClientUpdateSimulationApplicationResponseTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientUpdateSimulationApplicationResponsesourcesTypeDef],
        "simulationSoftwareSuite": ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef,
        "renderingEngine": ClientUpdateSimulationApplicationResponserenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)


class ClientUpdateSimulationApplicationResponseTypeDef(
    _ClientUpdateSimulationApplicationResponseTypeDef
):
    """
    Type definition for `ClientUpdateSimulationApplication` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the updated simulation application.

    - **name** *(string) --*

      The name of the simulation application.

    - **version** *(string) --*

      The version of the robot application.

    - **sources** *(list) --*

      The sources of the simulation application.

      - *(dict) --*

        Information about a source.

        - **s3Bucket** *(string) --*

          The s3 bucket name.

        - **s3Key** *(string) --*

          The s3 object key.

        - **etag** *(string) --*

          A hash of the object specified by ``s3Bucket`` and ``s3Key`` .

        - **architecture** *(string) --*

          The taget processor architecture for the application.

    - **simulationSoftwareSuite** *(dict) --*

      The simulation software suite used by the simulation application.

      - **name** *(string) --*

        The name of the simulation software suite.

      - **version** *(string) --*

        The version of the simulation software suite.

    - **robotSoftwareSuite** *(dict) --*

      Information about the robot software suite.

      - **name** *(string) --*

        The name of the robot software suite.

      - **version** *(string) --*

        The version of the robot software suite.

    - **renderingEngine** *(dict) --*

      The rendering engine for the simulation application.

      - **name** *(string) --*

        The name of the rendering engine.

      - **version** *(string) --*

        The version of the rendering engine.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation application was last updated.

    - **revisionId** *(string) --*

      The revision id of the simulation application.
    """


_ClientUpdateSimulationApplicationrenderingEngineTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationrenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientUpdateSimulationApplicationrenderingEngineTypeDef(
    _ClientUpdateSimulationApplicationrenderingEngineTypeDef
):
    """
    Type definition for `ClientUpdateSimulationApplication` `renderingEngine`

    The rendering engine for the simulation application.

    - **name** *(string) --*

      The name of the rendering engine.

    - **version** *(string) --*

      The version of the rendering engine.
    """


_ClientUpdateSimulationApplicationrobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationrobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientUpdateSimulationApplicationrobotSoftwareSuiteTypeDef(
    _ClientUpdateSimulationApplicationrobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientUpdateSimulationApplication` `robotSoftwareSuite`

    Information about the robot software suite.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ClientUpdateSimulationApplicationsimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationsimulationSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientUpdateSimulationApplicationsimulationSoftwareSuiteTypeDef(
    _ClientUpdateSimulationApplicationsimulationSoftwareSuiteTypeDef
):
    """
    Type definition for `ClientUpdateSimulationApplication` `simulationSoftwareSuite`

    The simulation software suite used by the simulation application.

    - **name** *(string) --*

      The name of the simulation software suite.

    - **version** *(string) --*

      The version of the simulation software suite.
    """


_ClientUpdateSimulationApplicationsourcesTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationsourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": str},
    total=False,
)


class ClientUpdateSimulationApplicationsourcesTypeDef(
    _ClientUpdateSimulationApplicationsourcesTypeDef
):
    """
    Type definition for `ClientUpdateSimulationApplication` `sources`

    Information about a source configuration.

    - **s3Bucket** *(string) --*

      The Amazon S3 bucket name.

    - **s3Key** *(string) --*

      The s3 object key.

    - **architecture** *(string) --*

      The target processor architecture for the application.
    """


_ListDeploymentJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeploymentJobsPaginatePaginationConfigTypeDef(
    _ListDeploymentJobsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDeploymentJobsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)


class ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef(
    _ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef
):
    """
    Type definition for `ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigs` `launchConfig`

    The launch configuration.

    - **packageName** *(string) --*

      The package name.

    - **preLaunchFile** *(string) --*

      The deployment pre-launch file. This file will be executed prior to the launch file.

    - **launchFile** *(string) --*

      The launch file name.

    - **postLaunchFile** *(string) --*

      The deployment post-launch file. This file will be executed after the launch file.

    - **environmentVariables** *(dict) --*

      An array of key/value pairs specifying environment variables for the robot
      application

      - *(string) --*

        - *(string) --*
    """


_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigsTypeDef = TypedDict(
    "_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)


class ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigsTypeDef(
    _ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigsTypeDef
):
    """
    Type definition for `ListDeploymentJobsPaginateResponsedeploymentJobs` `deploymentApplicationConfigs`

    Information about a deployment application configuration.

    - **application** *(string) --*

      The Amazon Resource Name (ARN) of the robot application.

    - **applicationVersion** *(string) --*

      The version of the application.

    - **launchConfig** *(dict) --*

      The launch configuration.

      - **packageName** *(string) --*

        The package name.

      - **preLaunchFile** *(string) --*

        The deployment pre-launch file. This file will be executed prior to the launch file.

      - **launchFile** *(string) --*

        The launch file name.

      - **postLaunchFile** *(string) --*

        The deployment post-launch file. This file will be executed after the launch file.

      - **environmentVariables** *(dict) --*

        An array of key/value pairs specifying environment variables for the robot
        application

        - *(string) --*

          - *(string) --*
    """


_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)


class ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef(
    _ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef
):
    """
    Type definition for `ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfig` `downloadConditionFile`

    The download condition file.

    - **bucket** *(string) --*

      The bucket containing the object.

    - **key** *(string) --*

      The key of the object.

    - **etag** *(string) --*

      The etag of the object.
    """


_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigTypeDef = TypedDict(
    "_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)


class ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigTypeDef(
    _ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigTypeDef
):
    """
    Type definition for `ListDeploymentJobsPaginateResponsedeploymentJobs` `deploymentConfig`

    The deployment configuration.

    - **concurrentDeploymentPercentage** *(integer) --*

      The percentage of robots receiving the deployment at the same time.

    - **failureThresholdPercentage** *(integer) --*

      The percentage of deployments that need to fail before stopping deployment.

    - **robotDeploymentTimeoutInSeconds** *(integer) --*

      The amount of time, in seconds, to wait for deployment to a single robot to complete.
      Choose a time between 1 minute and 7 days. The default is 5 hours.

    - **downloadConditionFile** *(dict) --*

      The download condition file.

      - **bucket** *(string) --*

        The bucket containing the object.

      - **key** *(string) --*

        The key of the object.

      - **etag** *(string) --*

        The etag of the object.
    """


_ListDeploymentJobsPaginateResponsedeploymentJobsTypeDef = TypedDict(
    "_ListDeploymentJobsPaginateResponsedeploymentJobsTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": str,
        "deploymentApplicationConfigs": List[
            ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigsTypeDef
        ],
        "deploymentConfig": ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigTypeDef,
        "failureReason": str,
        "failureCode": str,
        "createdAt": datetime,
    },
    total=False,
)


class ListDeploymentJobsPaginateResponsedeploymentJobsTypeDef(
    _ListDeploymentJobsPaginateResponsedeploymentJobsTypeDef
):
    """
    Type definition for `ListDeploymentJobsPaginateResponse` `deploymentJobs`

    Information about a deployment job.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the deployment job.

    - **fleet** *(string) --*

      The Amazon Resource Name (ARN) of the fleet.

    - **status** *(string) --*

      The status of the deployment job.

    - **deploymentApplicationConfigs** *(list) --*

      The deployment application configuration.

      - *(dict) --*

        Information about a deployment application configuration.

        - **application** *(string) --*

          The Amazon Resource Name (ARN) of the robot application.

        - **applicationVersion** *(string) --*

          The version of the application.

        - **launchConfig** *(dict) --*

          The launch configuration.

          - **packageName** *(string) --*

            The package name.

          - **preLaunchFile** *(string) --*

            The deployment pre-launch file. This file will be executed prior to the launch file.

          - **launchFile** *(string) --*

            The launch file name.

          - **postLaunchFile** *(string) --*

            The deployment post-launch file. This file will be executed after the launch file.

          - **environmentVariables** *(dict) --*

            An array of key/value pairs specifying environment variables for the robot
            application

            - *(string) --*

              - *(string) --*

    - **deploymentConfig** *(dict) --*

      The deployment configuration.

      - **concurrentDeploymentPercentage** *(integer) --*

        The percentage of robots receiving the deployment at the same time.

      - **failureThresholdPercentage** *(integer) --*

        The percentage of deployments that need to fail before stopping deployment.

      - **robotDeploymentTimeoutInSeconds** *(integer) --*

        The amount of time, in seconds, to wait for deployment to a single robot to complete.
        Choose a time between 1 minute and 7 days. The default is 5 hours.

      - **downloadConditionFile** *(dict) --*

        The download condition file.

        - **bucket** *(string) --*

          The bucket containing the object.

        - **key** *(string) --*

          The key of the object.

        - **etag** *(string) --*

          The etag of the object.

    - **failureReason** *(string) --*

      A short description of the reason why the deployment job failed.

    - **failureCode** *(string) --*

      The deployment job failure code.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the deployment job was created.
    """


_ListDeploymentJobsPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentJobsPaginateResponseTypeDef",
    {
        "deploymentJobs": List[ListDeploymentJobsPaginateResponsedeploymentJobsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListDeploymentJobsPaginateResponseTypeDef(
    _ListDeploymentJobsPaginateResponseTypeDef
):
    """
    Type definition for `ListDeploymentJobsPaginate` `Response`

    - **deploymentJobs** *(list) --*

      A list of deployment jobs that meet the criteria of the request.

      - *(dict) --*

        Information about a deployment job.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the deployment job.

        - **fleet** *(string) --*

          The Amazon Resource Name (ARN) of the fleet.

        - **status** *(string) --*

          The status of the deployment job.

        - **deploymentApplicationConfigs** *(list) --*

          The deployment application configuration.

          - *(dict) --*

            Information about a deployment application configuration.

            - **application** *(string) --*

              The Amazon Resource Name (ARN) of the robot application.

            - **applicationVersion** *(string) --*

              The version of the application.

            - **launchConfig** *(dict) --*

              The launch configuration.

              - **packageName** *(string) --*

                The package name.

              - **preLaunchFile** *(string) --*

                The deployment pre-launch file. This file will be executed prior to the launch file.

              - **launchFile** *(string) --*

                The launch file name.

              - **postLaunchFile** *(string) --*

                The deployment post-launch file. This file will be executed after the launch file.

              - **environmentVariables** *(dict) --*

                An array of key/value pairs specifying environment variables for the robot
                application

                - *(string) --*

                  - *(string) --*

        - **deploymentConfig** *(dict) --*

          The deployment configuration.

          - **concurrentDeploymentPercentage** *(integer) --*

            The percentage of robots receiving the deployment at the same time.

          - **failureThresholdPercentage** *(integer) --*

            The percentage of deployments that need to fail before stopping deployment.

          - **robotDeploymentTimeoutInSeconds** *(integer) --*

            The amount of time, in seconds, to wait for deployment to a single robot to complete.
            Choose a time between 1 minute and 7 days. The default is 5 hours.

          - **downloadConditionFile** *(dict) --*

            The download condition file.

            - **bucket** *(string) --*

              The bucket containing the object.

            - **key** *(string) --*

              The key of the object.

            - **etag** *(string) --*

              The etag of the object.

        - **failureReason** *(string) --*

          A short description of the reason why the deployment job failed.

        - **failureCode** *(string) --*

          The deployment job failure code.

        - **createdAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the deployment job was created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDeploymentJobsPaginatefiltersTypeDef = TypedDict(
    "_ListDeploymentJobsPaginatefiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ListDeploymentJobsPaginatefiltersTypeDef(
    _ListDeploymentJobsPaginatefiltersTypeDef
):
    """
    Type definition for `ListDeploymentJobsPaginate` `filters`

    Information about a filter.

    - **name** *(string) --*

      The name of the filter.

    - **values** *(list) --*

      A list of values.

      - *(string) --*
    """


_ListFleetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFleetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFleetsPaginatePaginationConfigTypeDef(
    _ListFleetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFleetsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListFleetsPaginateResponsefleetDetailsTypeDef = TypedDict(
    "_ListFleetsPaginateResponsefleetDetailsTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "lastDeploymentStatus": str,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)


class ListFleetsPaginateResponsefleetDetailsTypeDef(
    _ListFleetsPaginateResponsefleetDetailsTypeDef
):
    """
    Type definition for `ListFleetsPaginateResponse` `fleetDetails`

    Information about a fleet.

    - **name** *(string) --*

      The name of the fleet.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the fleet.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the fleet was created.

    - **lastDeploymentStatus** *(string) --*

      The status of the last fleet deployment.

    - **lastDeploymentJob** *(string) --*

      The Amazon Resource Name (ARN) of the last deployment job.

    - **lastDeploymentTime** *(datetime) --*

      The time of the last deployment.
    """


_ListFleetsPaginateResponseTypeDef = TypedDict(
    "_ListFleetsPaginateResponseTypeDef",
    {
        "fleetDetails": List[ListFleetsPaginateResponsefleetDetailsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListFleetsPaginateResponseTypeDef(_ListFleetsPaginateResponseTypeDef):
    """
    Type definition for `ListFleetsPaginate` `Response`

    - **fleetDetails** *(list) --*

      A list of fleet details meeting the request criteria.

      - *(dict) --*

        Information about a fleet.

        - **name** *(string) --*

          The name of the fleet.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the fleet.

        - **createdAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the fleet was created.

        - **lastDeploymentStatus** *(string) --*

          The status of the last fleet deployment.

        - **lastDeploymentJob** *(string) --*

          The Amazon Resource Name (ARN) of the last deployment job.

        - **lastDeploymentTime** *(datetime) --*

          The time of the last deployment.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListFleetsPaginatefiltersTypeDef = TypedDict(
    "_ListFleetsPaginatefiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ListFleetsPaginatefiltersTypeDef(_ListFleetsPaginatefiltersTypeDef):
    """
    Type definition for `ListFleetsPaginate` `filters`

    Information about a filter.

    - **name** *(string) --*

      The name of the filter.

    - **values** *(list) --*

      A list of values.

      - *(string) --*
    """


_ListRobotApplicationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRobotApplicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRobotApplicationsPaginatePaginationConfigTypeDef(
    _ListRobotApplicationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRobotApplicationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListRobotApplicationsPaginateResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef = TypedDict(
    "_ListRobotApplicationsPaginateResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ListRobotApplicationsPaginateResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef(
    _ListRobotApplicationsPaginateResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ListRobotApplicationsPaginateResponserobotApplicationSummaries` `robotSoftwareSuite`

    Information about a robot software suite.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ListRobotApplicationsPaginateResponserobotApplicationSummariesTypeDef = TypedDict(
    "_ListRobotApplicationsPaginateResponserobotApplicationSummariesTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": ListRobotApplicationsPaginateResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef,
    },
    total=False,
)


class ListRobotApplicationsPaginateResponserobotApplicationSummariesTypeDef(
    _ListRobotApplicationsPaginateResponserobotApplicationSummariesTypeDef
):
    """
    Type definition for `ListRobotApplicationsPaginateResponse` `robotApplicationSummaries`

    Summary information for a robot application.

    - **name** *(string) --*

      The name of the robot application.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the robot.

    - **version** *(string) --*

      The version of the robot application.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the robot application was last updated.

    - **robotSoftwareSuite** *(dict) --*

      Information about a robot software suite.

      - **name** *(string) --*

        The name of the robot software suite.

      - **version** *(string) --*

        The version of the robot software suite.
    """


_ListRobotApplicationsPaginateResponseTypeDef = TypedDict(
    "_ListRobotApplicationsPaginateResponseTypeDef",
    {
        "robotApplicationSummaries": List[
            ListRobotApplicationsPaginateResponserobotApplicationSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListRobotApplicationsPaginateResponseTypeDef(
    _ListRobotApplicationsPaginateResponseTypeDef
):
    """
    Type definition for `ListRobotApplicationsPaginate` `Response`

    - **robotApplicationSummaries** *(list) --*

      A list of robot application summaries that meet the criteria of the request.

      - *(dict) --*

        Summary information for a robot application.

        - **name** *(string) --*

          The name of the robot application.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the robot.

        - **version** *(string) --*

          The version of the robot application.

        - **lastUpdatedAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the robot application was last updated.

        - **robotSoftwareSuite** *(dict) --*

          Information about a robot software suite.

          - **name** *(string) --*

            The name of the robot software suite.

          - **version** *(string) --*

            The version of the robot software suite.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRobotApplicationsPaginatefiltersTypeDef = TypedDict(
    "_ListRobotApplicationsPaginatefiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ListRobotApplicationsPaginatefiltersTypeDef(
    _ListRobotApplicationsPaginatefiltersTypeDef
):
    """
    Type definition for `ListRobotApplicationsPaginate` `filters`

    Information about a filter.

    - **name** *(string) --*

      The name of the filter.

    - **values** *(list) --*

      A list of values.

      - *(string) --*
    """


_ListRobotsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRobotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRobotsPaginatePaginationConfigTypeDef(
    _ListRobotsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRobotsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListRobotsPaginateResponserobotsTypeDef = TypedDict(
    "_ListRobotsPaginateResponserobotsTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": str,
        "greenGrassGroupId": str,
        "createdAt": datetime,
        "architecture": str,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)


class ListRobotsPaginateResponserobotsTypeDef(_ListRobotsPaginateResponserobotsTypeDef):
    """
    Type definition for `ListRobotsPaginateResponse` `robots`

    Information about a robot.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the robot.

    - **name** *(string) --*

      The name of the robot.

    - **fleetArn** *(string) --*

      The Amazon Resource Name (ARN) of the fleet.

    - **status** *(string) --*

      The status of the robot.

    - **greenGrassGroupId** *(string) --*

      The Greengrass group associated with the robot.

    - **createdAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the robot was created.

    - **architecture** *(string) --*

      The architecture of the robot.

    - **lastDeploymentJob** *(string) --*

      The Amazon Resource Name (ARN) of the last deployment job.

    - **lastDeploymentTime** *(datetime) --*

      The time of the last deployment.
    """


_ListRobotsPaginateResponseTypeDef = TypedDict(
    "_ListRobotsPaginateResponseTypeDef",
    {"robots": List[ListRobotsPaginateResponserobotsTypeDef], "NextToken": str},
    total=False,
)


class ListRobotsPaginateResponseTypeDef(_ListRobotsPaginateResponseTypeDef):
    """
    Type definition for `ListRobotsPaginate` `Response`

    - **robots** *(list) --*

      A list of robots that meet the criteria of the request.

      - *(dict) --*

        Information about a robot.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the robot.

        - **name** *(string) --*

          The name of the robot.

        - **fleetArn** *(string) --*

          The Amazon Resource Name (ARN) of the fleet.

        - **status** *(string) --*

          The status of the robot.

        - **greenGrassGroupId** *(string) --*

          The Greengrass group associated with the robot.

        - **createdAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the robot was created.

        - **architecture** *(string) --*

          The architecture of the robot.

        - **lastDeploymentJob** *(string) --*

          The Amazon Resource Name (ARN) of the last deployment job.

        - **lastDeploymentTime** *(datetime) --*

          The time of the last deployment.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRobotsPaginatefiltersTypeDef = TypedDict(
    "_ListRobotsPaginatefiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ListRobotsPaginatefiltersTypeDef(_ListRobotsPaginatefiltersTypeDef):
    """
    Type definition for `ListRobotsPaginate` `filters`

    Information about a filter.

    - **name** *(string) --*

      The name of the filter.

    - **values** *(list) --*

      A list of values.

      - *(string) --*
    """


_ListSimulationApplicationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSimulationApplicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSimulationApplicationsPaginatePaginationConfigTypeDef(
    _ListSimulationApplicationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSimulationApplicationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef = TypedDict(
    "_ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef(
    _ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef
):
    """
    Type definition for `ListSimulationApplicationsPaginateResponsesimulationApplicationSummaries` `robotSoftwareSuite`

    Information about a robot software suite.

    - **name** *(string) --*

      The name of the robot software suite.

    - **version** *(string) --*

      The version of the robot software suite.
    """


_ListSimulationApplicationsPaginateResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef = TypedDict(
    "_ListSimulationApplicationsPaginateResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ListSimulationApplicationsPaginateResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef(
    _ListSimulationApplicationsPaginateResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef
):
    """
    Type definition for `ListSimulationApplicationsPaginateResponsesimulationApplicationSummaries` `simulationSoftwareSuite`

    Information about a simulation software suite.

    - **name** *(string) --*

      The name of the simulation software suite.

    - **version** *(string) --*

      The version of the simulation software suite.
    """


_ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesTypeDef = TypedDict(
    "_ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef,
        "simulationSoftwareSuite": ListSimulationApplicationsPaginateResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef,
    },
    total=False,
)


class ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesTypeDef(
    _ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesTypeDef
):
    """
    Type definition for `ListSimulationApplicationsPaginateResponse` `simulationApplicationSummaries`

    Summary information for a simulation application.

    - **name** *(string) --*

      The name of the simulation application.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the simulation application.

    - **version** *(string) --*

      The version of the simulation application.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation application was last
      updated.

    - **robotSoftwareSuite** *(dict) --*

      Information about a robot software suite.

      - **name** *(string) --*

        The name of the robot software suite.

      - **version** *(string) --*

        The version of the robot software suite.

    - **simulationSoftwareSuite** *(dict) --*

      Information about a simulation software suite.

      - **name** *(string) --*

        The name of the simulation software suite.

      - **version** *(string) --*

        The version of the simulation software suite.
    """


_ListSimulationApplicationsPaginateResponseTypeDef = TypedDict(
    "_ListSimulationApplicationsPaginateResponseTypeDef",
    {
        "simulationApplicationSummaries": List[
            ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListSimulationApplicationsPaginateResponseTypeDef(
    _ListSimulationApplicationsPaginateResponseTypeDef
):
    """
    Type definition for `ListSimulationApplicationsPaginate` `Response`

    - **simulationApplicationSummaries** *(list) --*

      A list of simulation application summaries that meet the criteria of the request.

      - *(dict) --*

        Summary information for a simulation application.

        - **name** *(string) --*

          The name of the simulation application.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the simulation application.

        - **version** *(string) --*

          The version of the simulation application.

        - **lastUpdatedAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the simulation application was last
          updated.

        - **robotSoftwareSuite** *(dict) --*

          Information about a robot software suite.

          - **name** *(string) --*

            The name of the robot software suite.

          - **version** *(string) --*

            The version of the robot software suite.

        - **simulationSoftwareSuite** *(dict) --*

          Information about a simulation software suite.

          - **name** *(string) --*

            The name of the simulation software suite.

          - **version** *(string) --*

            The version of the simulation software suite.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSimulationApplicationsPaginatefiltersTypeDef = TypedDict(
    "_ListSimulationApplicationsPaginatefiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ListSimulationApplicationsPaginatefiltersTypeDef(
    _ListSimulationApplicationsPaginatefiltersTypeDef
):
    """
    Type definition for `ListSimulationApplicationsPaginate` `filters`

    Information about a filter.

    - **name** *(string) --*

      The name of the filter.

    - **values** *(list) --*

      A list of values.

      - *(string) --*
    """


_ListSimulationJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSimulationJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSimulationJobsPaginatePaginationConfigTypeDef(
    _ListSimulationJobsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSimulationJobsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListSimulationJobsPaginateResponsesimulationJobSummariesTypeDef = TypedDict(
    "_ListSimulationJobsPaginateResponsesimulationJobSummariesTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": str,
        "simulationApplicationNames": List[str],
        "robotApplicationNames": List[str],
        "dataSourceNames": List[str],
    },
    total=False,
)


class ListSimulationJobsPaginateResponsesimulationJobSummariesTypeDef(
    _ListSimulationJobsPaginateResponsesimulationJobSummariesTypeDef
):
    """
    Type definition for `ListSimulationJobsPaginateResponse` `simulationJobSummaries`

    Summary information for a simulation job.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the simulation job.

    - **lastUpdatedAt** *(datetime) --*

      The time, in milliseconds since the epoch, when the simulation job was last updated.

    - **name** *(string) --*

      The name of the simulation job.

    - **status** *(string) --*

      The status of the simulation job.

    - **simulationApplicationNames** *(list) --*

      A list of simulation job simulation application names.

      - *(string) --*

    - **robotApplicationNames** *(list) --*

      A list of simulation job robot application names.

      - *(string) --*

    - **dataSourceNames** *(list) --*

      The names of the data sources.

      - *(string) --*
    """


_ListSimulationJobsPaginateResponseTypeDef = TypedDict(
    "_ListSimulationJobsPaginateResponseTypeDef",
    {
        "simulationJobSummaries": List[
            ListSimulationJobsPaginateResponsesimulationJobSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListSimulationJobsPaginateResponseTypeDef(
    _ListSimulationJobsPaginateResponseTypeDef
):
    """
    Type definition for `ListSimulationJobsPaginate` `Response`

    - **simulationJobSummaries** *(list) --*

      A list of simulation job summaries that meet the criteria of the request.

      - *(dict) --*

        Summary information for a simulation job.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the simulation job.

        - **lastUpdatedAt** *(datetime) --*

          The time, in milliseconds since the epoch, when the simulation job was last updated.

        - **name** *(string) --*

          The name of the simulation job.

        - **status** *(string) --*

          The status of the simulation job.

        - **simulationApplicationNames** *(list) --*

          A list of simulation job simulation application names.

          - *(string) --*

        - **robotApplicationNames** *(list) --*

          A list of simulation job robot application names.

          - *(string) --*

        - **dataSourceNames** *(list) --*

          The names of the data sources.

          - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSimulationJobsPaginatefiltersTypeDef = TypedDict(
    "_ListSimulationJobsPaginatefiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ListSimulationJobsPaginatefiltersTypeDef(
    _ListSimulationJobsPaginatefiltersTypeDef
):
    """
    Type definition for `ListSimulationJobsPaginate` `filters`

    Information about a filter.

    - **name** *(string) --*

      The name of the filter.

    - **values** *(list) --*

      A list of values.

      - *(string) --*
    """
