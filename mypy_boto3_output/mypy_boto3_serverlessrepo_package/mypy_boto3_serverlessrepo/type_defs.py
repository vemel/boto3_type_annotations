"Main interface for serverlessrepo type defs"
from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef",
    "ClientCreateApplicationResponseVersionTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef",
    "ClientCreateApplicationVersionResponseTypeDef",
    "ClientCreateCloudFormationChangeSetParameterOverridesTypeDef",
    "ClientCreateCloudFormationChangeSetResponseTypeDef",
    "ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef",
    "ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef",
    "ClientCreateCloudFormationChangeSetTagsTypeDef",
    "ClientCreateCloudFormationTemplateResponseTypeDef",
    "ClientGetApplicationPolicyResponseStatementsTypeDef",
    "ClientGetApplicationPolicyResponseTypeDef",
    "ClientGetApplicationResponseVersionParameterDefinitionsTypeDef",
    "ClientGetApplicationResponseVersionTypeDef",
    "ClientGetApplicationResponseTypeDef",
    "ClientGetCloudFormationTemplateResponseTypeDef",
    "ClientListApplicationDependenciesResponseDependenciesTypeDef",
    "ClientListApplicationDependenciesResponseTypeDef",
    "ClientListApplicationVersionsResponseVersionsTypeDef",
    "ClientListApplicationVersionsResponseTypeDef",
    "ClientListApplicationsResponseApplicationsTypeDef",
    "ClientListApplicationsResponseTypeDef",
    "ClientPutApplicationPolicyResponseStatementsTypeDef",
    "ClientPutApplicationPolicyResponseTypeDef",
    "ClientPutApplicationPolicyStatementsTypeDef",
    "ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef",
    "ClientUpdateApplicationResponseVersionTypeDef",
    "ClientUpdateApplicationResponseTypeDef",
    "ListApplicationDependenciesPaginatePaginationConfigTypeDef",
    "ListApplicationDependenciesPaginateResponseDependenciesTypeDef",
    "ListApplicationDependenciesPaginateResponseTypeDef",
    "ListApplicationVersionsPaginatePaginationConfigTypeDef",
    "ListApplicationVersionsPaginateResponseVersionsTypeDef",
    "ListApplicationVersionsPaginateResponseTypeDef",
    "ListApplicationsPaginatePaginationConfigTypeDef",
    "ListApplicationsPaginateResponseApplicationsTypeDef",
    "ListApplicationsPaginateResponseTypeDef",
)


_ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef = TypedDict(
    "_ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef",
    {
        "AllowedPattern": str,
        "AllowedValues": List[str],
        "ConstraintDescription": str,
        "DefaultValue": str,
        "Description": str,
        "MaxLength": int,
        "MaxValue": int,
        "MinLength": int,
        "MinValue": int,
        "Name": str,
        "NoEcho": bool,
        "ReferencedByResources": List[str],
        "Type": str,
    },
    total=False,
)


class ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef(
    _ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseVersion` `ParameterDefinitions`

    Parameters supported by the application.

    - **AllowedPattern** *(string) --*

      A regular expression that represents the patterns to allow for String types.

    - **AllowedValues** *(list) --*

      An array containing the list of values allowed for the parameter.

      - *(string) --*

    - **ConstraintDescription** *(string) --*

      A string that explains a constraint when the constraint is violated. For example,
      without a constraint description, a parameter that has an allowed pattern of
      [A-Za-z0-9]+ displays the following error message when the user specifies an invalid
      value:

      Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+

      By adding a constraint description, such as "must contain only uppercase and lowercase
      letters and numbers," you can display the following customized error message:

      Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters
      and numbers.

    - **DefaultValue** *(string) --*

      A value of the appropriate type for the template to use if no value is specified when a
      stack is created. If you define constraints for the parameter, you must specify a value
      that adheres to those constraints.

    - **Description** *(string) --*

      A string of up to 4,000 characters that describes the parameter.

    - **MaxLength** *(integer) --*

      An integer value that determines the largest number of characters that you want to
      allow for String types.

    - **MaxValue** *(integer) --*

      A numeric value that determines the largest numeric value that you want to allow for
      Number types.

    - **MinLength** *(integer) --*

      An integer value that determines the smallest number of characters that you want to
      allow for String types.

    - **MinValue** *(integer) --*

      A numeric value that determines the smallest numeric value that you want to allow for
      Number types.

    - **Name** *(string) --*

      The name of the parameter.

    - **NoEcho** *(boolean) --*

      Whether to mask the parameter value whenever anyone makes a call that describes the
      stack. If you set the value to true, the parameter value is masked with asterisks
      (*****).

    - **ReferencedByResources** *(list) --*

      A list of AWS SAM resources that use this parameter.

      - *(string) --*

    - **Type** *(string) --*

      The type of the parameter.

      Valid values: String | Number | List<Number> | CommaDelimitedList

      String: A literal string.

      For example, users can specify "MyUserName".

      Number: An integer or float. AWS CloudFormation validates the parameter value as a
      number. However, when you use the parameter elsewhere in your template (for example, by
      using the Ref intrinsic function), the parameter value becomes a string.

      For example, users might specify "8888".

      List<Number>: An array of integers or floats that are separated by commas. AWS
      CloudFormation validates the parameter value as numbers. However, when you use the
      parameter elsewhere in your template (for example, by using the Ref intrinsic
      function), the parameter value becomes a list of strings.

      For example, users might specify "80,20", and then Ref results in ["80","20"].

      CommaDelimitedList: An array of literal strings that are separated by commas. The total
      number of strings should be one more than the total number of commas. Also, each member
      string is space-trimmed.

      For example, users might specify "test,dev,prod", and then Ref results in
      ["test","dev","prod"].
    """


_ClientCreateApplicationResponseVersionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseVersionTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List[
            ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef
        ],
        "RequiredCapabilities": List[str],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateUrl": str,
    },
    total=False,
)


class ClientCreateApplicationResponseVersionTypeDef(
    _ClientCreateApplicationResponseVersionTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponse` `Version`

    Version information about the application.

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **CreationTime** *(string) --*

      The date and time this resource was created.

    - **ParameterDefinitions** *(list) --*

      An array of parameter types supported by the application.

      - *(dict) --*

        Parameters supported by the application.

        - **AllowedPattern** *(string) --*

          A regular expression that represents the patterns to allow for String types.

        - **AllowedValues** *(list) --*

          An array containing the list of values allowed for the parameter.

          - *(string) --*

        - **ConstraintDescription** *(string) --*

          A string that explains a constraint when the constraint is violated. For example,
          without a constraint description, a parameter that has an allowed pattern of
          [A-Za-z0-9]+ displays the following error message when the user specifies an invalid
          value:

          Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+

          By adding a constraint description, such as "must contain only uppercase and lowercase
          letters and numbers," you can display the following customized error message:

          Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters
          and numbers.

        - **DefaultValue** *(string) --*

          A value of the appropriate type for the template to use if no value is specified when a
          stack is created. If you define constraints for the parameter, you must specify a value
          that adheres to those constraints.

        - **Description** *(string) --*

          A string of up to 4,000 characters that describes the parameter.

        - **MaxLength** *(integer) --*

          An integer value that determines the largest number of characters that you want to
          allow for String types.

        - **MaxValue** *(integer) --*

          A numeric value that determines the largest numeric value that you want to allow for
          Number types.

        - **MinLength** *(integer) --*

          An integer value that determines the smallest number of characters that you want to
          allow for String types.

        - **MinValue** *(integer) --*

          A numeric value that determines the smallest numeric value that you want to allow for
          Number types.

        - **Name** *(string) --*

          The name of the parameter.

        - **NoEcho** *(boolean) --*

          Whether to mask the parameter value whenever anyone makes a call that describes the
          stack. If you set the value to true, the parameter value is masked with asterisks
          (*****).

        - **ReferencedByResources** *(list) --*

          A list of AWS SAM resources that use this parameter.

          - *(string) --*

        - **Type** *(string) --*

          The type of the parameter.

          Valid values: String | Number | List<Number> | CommaDelimitedList

          String: A literal string.

          For example, users can specify "MyUserName".

          Number: An integer or float. AWS CloudFormation validates the parameter value as a
          number. However, when you use the parameter elsewhere in your template (for example, by
          using the Ref intrinsic function), the parameter value becomes a string.

          For example, users might specify "8888".

          List<Number>: An array of integers or floats that are separated by commas. AWS
          CloudFormation validates the parameter value as numbers. However, when you use the
          parameter elsewhere in your template (for example, by using the Ref intrinsic
          function), the parameter value becomes a list of strings.

          For example, users might specify "80,20", and then Ref results in ["80","20"].

          CommaDelimitedList: An array of literal strings that are separated by commas. The total
          number of strings should be one more than the total number of commas. Also, each member
          string is space-trimmed.

          For example, users might specify "test,dev,prod", and then Ref results in
          ["test","dev","prod"].

    - **RequiredCapabilities** *(list) --*

      A list of values that you must specify before you can deploy certain applications. Some
      applications might include resources that can affect permissions in your AWS account, for
      example, by creating new AWS Identity and Access Management (IAM) users. For those
      applications, you must explicitly acknowledge their capabilities by specifying this
      parameter.

      The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY,
      and CAPABILITY_AUTO_EXPAND.

      The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM:
      `AWS\\:\\:IAM\\:\\:Group
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__
      , `AWS\\:\\:IAM\\:\\:InstanceProfile
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__
      , `AWS\\:\\:IAM\\:\\:Policy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
      , and `AWS\\:\\:IAM\\:\\:Role
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__
      . If the application contains IAM resources, you can specify either CAPABILITY_IAM or
      CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must
      specify CAPABILITY_NAMED_IAM.

      The following resources require you to specify CAPABILITY_RESOURCE_POLICY:
      `AWS\\:\\:Lambda\\:\\:Permission
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html>`__
      , `AWS\\:\\:IAM\\:Policy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
      , `AWS\\:\\:ApplicationAutoScaling\\:\\:ScalingPolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`__
      , `AWS\\:\\:S3\\:\\:BucketPolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html>`__
      , `AWS\\:\\:SQS\\:\\:QueuePolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html>`__
      , and `AWS\\:\\:SNS\\:\\:TopicPolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html>`__
      .

      Applications that contain one or more nested applications require you to specify
      CAPABILITY_AUTO_EXPAND.

      If your application template contains any of the above resources, we recommend that you
      review all permissions associated with the application before deploying. If you don't
      specify this parameter for an application that requires capabilities, the call will fail.

      - *(string) --*

        Values that must be specified in order to deploy some applications.

    - **ResourcesSupported** *(boolean) --*

      Whether all of the AWS resources contained in this application are supported in the region
      in which it is being retrieved.

    - **SemanticVersion** *(string) --*

      The semantic version of the application:

       `https\\://semver.org/ <https://semver.org/>`__

    - **SourceCodeArchiveUrl** *(string) --*

      A link to the S3 object that contains the ZIP archive of the source code for this version
      of your application.

      Maximum size 50 MB

    - **SourceCodeUrl** *(string) --*

      A link to a public repository for the source code of your application, for example the URL
      of a specific GitHub commit.

    - **TemplateUrl** *(string) --*

      A link to the packaged AWS SAM template of your application.
    """


_ClientCreateApplicationResponseTypeDef = TypedDict(
    "_ClientCreateApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "Version": ClientCreateApplicationResponseVersionTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseTypeDef(_ClientCreateApplicationResponseTypeDef):
    """
    Type definition for `ClientCreateApplication` `Response`

    Success

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **Author** *(string) --*

      The name of the author publishing the app.

      Minimum length=1. Maximum length=127.

      Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";

    - **CreationTime** *(string) --*

      The date and time this resource was created.

    - **Description** *(string) --*

      The description of the application.

      Minimum length=1. Maximum length=256

    - **HomePageUrl** *(string) --*

      A URL with more information about the application, for example the location of your GitHub
      repository for the application.

    - **Labels** *(list) --*

      Labels to improve discovery of apps in search results.

      Minimum length=1. Maximum length=127. Maximum number of labels: 10

      Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";

      - *(string) --*

    - **LicenseUrl** *(string) --*

      A link to a license file of the app that matches the spdxLicenseID value of your application.

      Maximum size 5 MB

    - **Name** *(string) --*

      The name of the application.

      Minimum length=1. Maximum length=140

      Pattern: "[a-zA-Z0-9\\-]+";

    - **ReadmeUrl** *(string) --*

      A link to the readme file in Markdown language that contains a more detailed description of
      the application and how it works.

      Maximum size 5 MB

    - **SpdxLicenseId** *(string) --*

      A valid identifier from https://spdx.org/licenses/.

    - **Version** *(dict) --*

      Version information about the application.

      - **ApplicationId** *(string) --*

        The application Amazon Resource Name (ARN).

      - **CreationTime** *(string) --*

        The date and time this resource was created.

      - **ParameterDefinitions** *(list) --*

        An array of parameter types supported by the application.

        - *(dict) --*

          Parameters supported by the application.

          - **AllowedPattern** *(string) --*

            A regular expression that represents the patterns to allow for String types.

          - **AllowedValues** *(list) --*

            An array containing the list of values allowed for the parameter.

            - *(string) --*

          - **ConstraintDescription** *(string) --*

            A string that explains a constraint when the constraint is violated. For example,
            without a constraint description, a parameter that has an allowed pattern of
            [A-Za-z0-9]+ displays the following error message when the user specifies an invalid
            value:

            Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+

            By adding a constraint description, such as "must contain only uppercase and lowercase
            letters and numbers," you can display the following customized error message:

            Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters
            and numbers.

          - **DefaultValue** *(string) --*

            A value of the appropriate type for the template to use if no value is specified when a
            stack is created. If you define constraints for the parameter, you must specify a value
            that adheres to those constraints.

          - **Description** *(string) --*

            A string of up to 4,000 characters that describes the parameter.

          - **MaxLength** *(integer) --*

            An integer value that determines the largest number of characters that you want to
            allow for String types.

          - **MaxValue** *(integer) --*

            A numeric value that determines the largest numeric value that you want to allow for
            Number types.

          - **MinLength** *(integer) --*

            An integer value that determines the smallest number of characters that you want to
            allow for String types.

          - **MinValue** *(integer) --*

            A numeric value that determines the smallest numeric value that you want to allow for
            Number types.

          - **Name** *(string) --*

            The name of the parameter.

          - **NoEcho** *(boolean) --*

            Whether to mask the parameter value whenever anyone makes a call that describes the
            stack. If you set the value to true, the parameter value is masked with asterisks
            (*****).

          - **ReferencedByResources** *(list) --*

            A list of AWS SAM resources that use this parameter.

            - *(string) --*

          - **Type** *(string) --*

            The type of the parameter.

            Valid values: String | Number | List<Number> | CommaDelimitedList

            String: A literal string.

            For example, users can specify "MyUserName".

            Number: An integer or float. AWS CloudFormation validates the parameter value as a
            number. However, when you use the parameter elsewhere in your template (for example, by
            using the Ref intrinsic function), the parameter value becomes a string.

            For example, users might specify "8888".

            List<Number>: An array of integers or floats that are separated by commas. AWS
            CloudFormation validates the parameter value as numbers. However, when you use the
            parameter elsewhere in your template (for example, by using the Ref intrinsic
            function), the parameter value becomes a list of strings.

            For example, users might specify "80,20", and then Ref results in ["80","20"].

            CommaDelimitedList: An array of literal strings that are separated by commas. The total
            number of strings should be one more than the total number of commas. Also, each member
            string is space-trimmed.

            For example, users might specify "test,dev,prod", and then Ref results in
            ["test","dev","prod"].

      - **RequiredCapabilities** *(list) --*

        A list of values that you must specify before you can deploy certain applications. Some
        applications might include resources that can affect permissions in your AWS account, for
        example, by creating new AWS Identity and Access Management (IAM) users. For those
        applications, you must explicitly acknowledge their capabilities by specifying this
        parameter.

        The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY,
        and CAPABILITY_AUTO_EXPAND.

        The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM:
        `AWS\\:\\:IAM\\:\\:Group
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__
        , `AWS\\:\\:IAM\\:\\:InstanceProfile
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__
        , `AWS\\:\\:IAM\\:\\:Policy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
        , and `AWS\\:\\:IAM\\:\\:Role
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__
        . If the application contains IAM resources, you can specify either CAPABILITY_IAM or
        CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must
        specify CAPABILITY_NAMED_IAM.

        The following resources require you to specify CAPABILITY_RESOURCE_POLICY:
        `AWS\\:\\:Lambda\\:\\:Permission
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html>`__
        , `AWS\\:\\:IAM\\:Policy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
        , `AWS\\:\\:ApplicationAutoScaling\\:\\:ScalingPolicy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`__
        , `AWS\\:\\:S3\\:\\:BucketPolicy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html>`__
        , `AWS\\:\\:SQS\\:\\:QueuePolicy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html>`__
        , and `AWS\\:\\:SNS\\:\\:TopicPolicy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html>`__
        .

        Applications that contain one or more nested applications require you to specify
        CAPABILITY_AUTO_EXPAND.

        If your application template contains any of the above resources, we recommend that you
        review all permissions associated with the application before deploying. If you don't
        specify this parameter for an application that requires capabilities, the call will fail.

        - *(string) --*

          Values that must be specified in order to deploy some applications.

      - **ResourcesSupported** *(boolean) --*

        Whether all of the AWS resources contained in this application are supported in the region
        in which it is being retrieved.

      - **SemanticVersion** *(string) --*

        The semantic version of the application:

         `https\\://semver.org/ <https://semver.org/>`__

      - **SourceCodeArchiveUrl** *(string) --*

        A link to the S3 object that contains the ZIP archive of the source code for this version
        of your application.

        Maximum size 50 MB

      - **SourceCodeUrl** *(string) --*

        A link to a public repository for the source code of your application, for example the URL
        of a specific GitHub commit.

      - **TemplateUrl** *(string) --*

        A link to the packaged AWS SAM template of your application.
    """


_ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef = TypedDict(
    "_ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef",
    {
        "AllowedPattern": str,
        "AllowedValues": List[str],
        "ConstraintDescription": str,
        "DefaultValue": str,
        "Description": str,
        "MaxLength": int,
        "MaxValue": int,
        "MinLength": int,
        "MinValue": int,
        "Name": str,
        "NoEcho": bool,
        "ReferencedByResources": List[str],
        "Type": str,
    },
    total=False,
)


class ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef(
    _ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef
):
    """
    Type definition for `ClientCreateApplicationVersionResponse` `ParameterDefinitions`

    Parameters supported by the application.

    - **AllowedPattern** *(string) --*

      A regular expression that represents the patterns to allow for String types.

    - **AllowedValues** *(list) --*

      An array containing the list of values allowed for the parameter.

      - *(string) --*

    - **ConstraintDescription** *(string) --*

      A string that explains a constraint when the constraint is violated. For example, without
      a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+
      displays the following error message when the user specifies an invalid value:

      Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+

      By adding a constraint description, such as "must contain only uppercase and lowercase
      letters and numbers," you can display the following customized error message:

      Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters
      and numbers.

    - **DefaultValue** *(string) --*

      A value of the appropriate type for the template to use if no value is specified when a
      stack is created. If you define constraints for the parameter, you must specify a value
      that adheres to those constraints.

    - **Description** *(string) --*

      A string of up to 4,000 characters that describes the parameter.

    - **MaxLength** *(integer) --*

      An integer value that determines the largest number of characters that you want to allow
      for String types.

    - **MaxValue** *(integer) --*

      A numeric value that determines the largest numeric value that you want to allow for
      Number types.

    - **MinLength** *(integer) --*

      An integer value that determines the smallest number of characters that you want to allow
      for String types.

    - **MinValue** *(integer) --*

      A numeric value that determines the smallest numeric value that you want to allow for
      Number types.

    - **Name** *(string) --*

      The name of the parameter.

    - **NoEcho** *(boolean) --*

      Whether to mask the parameter value whenever anyone makes a call that describes the
      stack. If you set the value to true, the parameter value is masked with asterisks (*****).

    - **ReferencedByResources** *(list) --*

      A list of AWS SAM resources that use this parameter.

      - *(string) --*

    - **Type** *(string) --*

      The type of the parameter.

      Valid values: String | Number | List<Number> | CommaDelimitedList

      String: A literal string.

      For example, users can specify "MyUserName".

      Number: An integer or float. AWS CloudFormation validates the parameter value as a
      number. However, when you use the parameter elsewhere in your template (for example, by
      using the Ref intrinsic function), the parameter value becomes a string.

      For example, users might specify "8888".

      List<Number>: An array of integers or floats that are separated by commas. AWS
      CloudFormation validates the parameter value as numbers. However, when you use the
      parameter elsewhere in your template (for example, by using the Ref intrinsic function),
      the parameter value becomes a list of strings.

      For example, users might specify "80,20", and then Ref results in ["80","20"].

      CommaDelimitedList: An array of literal strings that are separated by commas. The total
      number of strings should be one more than the total number of commas. Also, each member
      string is space-trimmed.

      For example, users might specify "test,dev,prod", and then Ref results in
      ["test","dev","prod"].
    """


_ClientCreateApplicationVersionResponseTypeDef = TypedDict(
    "_ClientCreateApplicationVersionResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List[
            ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef
        ],
        "RequiredCapabilities": List[str],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateUrl": str,
    },
    total=False,
)


class ClientCreateApplicationVersionResponseTypeDef(
    _ClientCreateApplicationVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateApplicationVersion` `Response`

    Success

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **CreationTime** *(string) --*

      The date and time this resource was created.

    - **ParameterDefinitions** *(list) --*

      An array of parameter types supported by the application.

      - *(dict) --*

        Parameters supported by the application.

        - **AllowedPattern** *(string) --*

          A regular expression that represents the patterns to allow for String types.

        - **AllowedValues** *(list) --*

          An array containing the list of values allowed for the parameter.

          - *(string) --*

        - **ConstraintDescription** *(string) --*

          A string that explains a constraint when the constraint is violated. For example, without
          a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+
          displays the following error message when the user specifies an invalid value:

          Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+

          By adding a constraint description, such as "must contain only uppercase and lowercase
          letters and numbers," you can display the following customized error message:

          Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters
          and numbers.

        - **DefaultValue** *(string) --*

          A value of the appropriate type for the template to use if no value is specified when a
          stack is created. If you define constraints for the parameter, you must specify a value
          that adheres to those constraints.

        - **Description** *(string) --*

          A string of up to 4,000 characters that describes the parameter.

        - **MaxLength** *(integer) --*

          An integer value that determines the largest number of characters that you want to allow
          for String types.

        - **MaxValue** *(integer) --*

          A numeric value that determines the largest numeric value that you want to allow for
          Number types.

        - **MinLength** *(integer) --*

          An integer value that determines the smallest number of characters that you want to allow
          for String types.

        - **MinValue** *(integer) --*

          A numeric value that determines the smallest numeric value that you want to allow for
          Number types.

        - **Name** *(string) --*

          The name of the parameter.

        - **NoEcho** *(boolean) --*

          Whether to mask the parameter value whenever anyone makes a call that describes the
          stack. If you set the value to true, the parameter value is masked with asterisks (*****).

        - **ReferencedByResources** *(list) --*

          A list of AWS SAM resources that use this parameter.

          - *(string) --*

        - **Type** *(string) --*

          The type of the parameter.

          Valid values: String | Number | List<Number> | CommaDelimitedList

          String: A literal string.

          For example, users can specify "MyUserName".

          Number: An integer or float. AWS CloudFormation validates the parameter value as a
          number. However, when you use the parameter elsewhere in your template (for example, by
          using the Ref intrinsic function), the parameter value becomes a string.

          For example, users might specify "8888".

          List<Number>: An array of integers or floats that are separated by commas. AWS
          CloudFormation validates the parameter value as numbers. However, when you use the
          parameter elsewhere in your template (for example, by using the Ref intrinsic function),
          the parameter value becomes a list of strings.

          For example, users might specify "80,20", and then Ref results in ["80","20"].

          CommaDelimitedList: An array of literal strings that are separated by commas. The total
          number of strings should be one more than the total number of commas. Also, each member
          string is space-trimmed.

          For example, users might specify "test,dev,prod", and then Ref results in
          ["test","dev","prod"].

    - **RequiredCapabilities** *(list) --*

      A list of values that you must specify before you can deploy certain applications. Some
      applications might include resources that can affect permissions in your AWS account, for
      example, by creating new AWS Identity and Access Management (IAM) users. For those
      applications, you must explicitly acknowledge their capabilities by specifying this parameter.

      The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY,
      and CAPABILITY_AUTO_EXPAND.

      The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM:
      `AWS\\:\\:IAM\\:\\:Group
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__
      , `AWS\\:\\:IAM\\:\\:InstanceProfile
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__
      , `AWS\\:\\:IAM\\:\\:Policy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
      , and `AWS\\:\\:IAM\\:\\:Role
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__
      . If the application contains IAM resources, you can specify either CAPABILITY_IAM or
      CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must
      specify CAPABILITY_NAMED_IAM.

      The following resources require you to specify CAPABILITY_RESOURCE_POLICY:
      `AWS\\:\\:Lambda\\:\\:Permission
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html>`__
      , `AWS\\:\\:IAM\\:Policy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
      , `AWS\\:\\:ApplicationAutoScaling\\:\\:ScalingPolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`__
      , `AWS\\:\\:S3\\:\\:BucketPolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html>`__
      , `AWS\\:\\:SQS\\:\\:QueuePolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html>`__
      , and `AWS\\:\\:SNS\\:\\:TopicPolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html>`__
      .

      Applications that contain one or more nested applications require you to specify
      CAPABILITY_AUTO_EXPAND.

      If your application template contains any of the above resources, we recommend that you
      review all permissions associated with the application before deploying. If you don't specify
      this parameter for an application that requires capabilities, the call will fail.

      - *(string) --*

        Values that must be specified in order to deploy some applications.

    - **ResourcesSupported** *(boolean) --*

      Whether all of the AWS resources contained in this application are supported in the region in
      which it is being retrieved.

    - **SemanticVersion** *(string) --*

      The semantic version of the application:

       `https\\://semver.org/ <https://semver.org/>`__

    - **SourceCodeArchiveUrl** *(string) --*

      A link to the S3 object that contains the ZIP archive of the source code for this version of
      your application.

      Maximum size 50 MB

    - **SourceCodeUrl** *(string) --*

      A link to a public repository for the source code of your application, for example the URL of
      a specific GitHub commit.

    - **TemplateUrl** *(string) --*

      A link to the packaged AWS SAM template of your application.
    """


_ClientCreateCloudFormationChangeSetParameterOverridesTypeDef = TypedDict(
    "_ClientCreateCloudFormationChangeSetParameterOverridesTypeDef",
    {"Name": str, "Value": str},
)


class ClientCreateCloudFormationChangeSetParameterOverridesTypeDef(
    _ClientCreateCloudFormationChangeSetParameterOverridesTypeDef
):
    """
    Type definition for `ClientCreateCloudFormationChangeSet` `ParameterOverrides`

    Parameter value of the application.

    - **Name** *(string) --* **[REQUIRED]**

      The key associated with the parameter. If you don't specify a key and value for a particular
      parameter, AWS CloudFormation uses the default value that is specified in your template.

    - **Value** *(string) --* **[REQUIRED]**

      The input value associated with the parameter.
    """


_ClientCreateCloudFormationChangeSetResponseTypeDef = TypedDict(
    "_ClientCreateCloudFormationChangeSetResponseTypeDef",
    {"ApplicationId": str, "ChangeSetId": str, "SemanticVersion": str, "StackId": str},
    total=False,
)


class ClientCreateCloudFormationChangeSetResponseTypeDef(
    _ClientCreateCloudFormationChangeSetResponseTypeDef
):
    """
    Type definition for `ClientCreateCloudFormationChangeSet` `Response`

    Success

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **ChangeSetId** *(string) --*

      The Amazon Resource Name (ARN) of the change set.

      Length constraints: Minimum length of 1.

      Pattern: ARN:[-a-zA-Z0-9:/]*

    - **SemanticVersion** *(string) --*

      The semantic version of the application:

       `https\\://semver.org/ <https://semver.org/>`__

    - **StackId** *(string) --*

      The unique ID of the stack.
    """


_ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
)


class ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef(
    _ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef
):
    """
    Type definition for `ClientCreateCloudFormationChangeSetRollbackConfiguration` `RollbackTriggers`

    This property corresponds to the *AWS CloudFormation `RollbackTrigger
    <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger>`__ * Data
    Type.

    - **Arn** *(string) --* **[REQUIRED]**

      This property corresponds to the content of the same name for the *AWS CloudFormation
      `RollbackTrigger
      <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger>`__ *
      Data Type.

    - **Type** *(string) --* **[REQUIRED]**

      This property corresponds to the content of the same name for the *AWS CloudFormation
      `RollbackTrigger
      <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger>`__ *
      Data Type.
    """


_ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef = TypedDict(
    "_ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef",
    {
        "MonitoringTimeInMinutes": int,
        "RollbackTriggers": List[
            ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef
        ],
    },
    total=False,
)


class ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef(
    _ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef
):
    """
    Type definition for `ClientCreateCloudFormationChangeSet` `RollbackConfiguration`

    This property corresponds to the parameter of the same name for the *AWS CloudFormation
    `CreateChangeSet
    <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__ * API.

    - **MonitoringTimeInMinutes** *(integer) --*

      This property corresponds to the content of the same name for the *AWS CloudFormation
      `RollbackConfiguration
      <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackConfiguration>`__ *
      Data Type.

    - **RollbackTriggers** *(list) --*

      This property corresponds to the content of the same name for the *AWS CloudFormation
      `RollbackConfiguration
      <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackConfiguration>`__ *
      Data Type.

      - *(dict) --*

        This property corresponds to the *AWS CloudFormation `RollbackTrigger
        <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger>`__ * Data
        Type.

        - **Arn** *(string) --* **[REQUIRED]**

          This property corresponds to the content of the same name for the *AWS CloudFormation
          `RollbackTrigger
          <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger>`__ *
          Data Type.

        - **Type** *(string) --* **[REQUIRED]**

          This property corresponds to the content of the same name for the *AWS CloudFormation
          `RollbackTrigger
          <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger>`__ *
          Data Type.
    """


_ClientCreateCloudFormationChangeSetTagsTypeDef = TypedDict(
    "_ClientCreateCloudFormationChangeSetTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateCloudFormationChangeSetTagsTypeDef(
    _ClientCreateCloudFormationChangeSetTagsTypeDef
):
    """
    Type definition for `ClientCreateCloudFormationChangeSet` `Tags`

    This property corresponds to the *AWS CloudFormation `Tag
    <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag>`__ * Data Type.

    - **Key** *(string) --* **[REQUIRED]**

      This property corresponds to the content of the same name for the *AWS CloudFormation `Tag
      <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag>`__ * Data Type.

    - **Value** *(string) --* **[REQUIRED]**

      This property corresponds to the content of the same name for the *AWS CloudFormation `Tag
      <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag>`__ * Data Type.
    """


_ClientCreateCloudFormationTemplateResponseTypeDef = TypedDict(
    "_ClientCreateCloudFormationTemplateResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ExpirationTime": str,
        "SemanticVersion": str,
        "Status": str,
        "TemplateId": str,
        "TemplateUrl": str,
    },
    total=False,
)


class ClientCreateCloudFormationTemplateResponseTypeDef(
    _ClientCreateCloudFormationTemplateResponseTypeDef
):
    """
    Type definition for `ClientCreateCloudFormationTemplate` `Response`

    Success

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **CreationTime** *(string) --*

      The date and time this resource was created.

    - **ExpirationTime** *(string) --*

      The date and time this template expires. Templates expire 1 hour after creation.

    - **SemanticVersion** *(string) --*

      The semantic version of the application:

       `https\\://semver.org/ <https://semver.org/>`__

    - **Status** *(string) --*

      Status of the template creation workflow.

      Possible values: PREPARING | ACTIVE | EXPIRED

    - **TemplateId** *(string) --*

      The UUID returned by CreateCloudFormationTemplate.

      Pattern: [0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12}

    - **TemplateUrl** *(string) --*

      A link to the template that can be used to deploy the application using AWS CloudFormation.
    """


_ClientGetApplicationPolicyResponseStatementsTypeDef = TypedDict(
    "_ClientGetApplicationPolicyResponseStatementsTypeDef",
    {"Actions": List[str], "Principals": List[str], "StatementId": str},
    total=False,
)


class ClientGetApplicationPolicyResponseStatementsTypeDef(
    _ClientGetApplicationPolicyResponseStatementsTypeDef
):
    """
    Type definition for `ClientGetApplicationPolicyResponse` `Statements`

    Policy statement applied to the application.

    - **Actions** *(list) --*

      For the list of actions supported for this operation, see `Application Permissions
      <https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions>`__
      .

      - *(string) --*

    - **Principals** *(list) --*

      An array of AWS account IDs, or * to make the application public.

      - *(string) --*

    - **StatementId** *(string) --*

      A unique ID for the statement.
    """


_ClientGetApplicationPolicyResponseTypeDef = TypedDict(
    "_ClientGetApplicationPolicyResponseTypeDef",
    {"Statements": List[ClientGetApplicationPolicyResponseStatementsTypeDef]},
    total=False,
)


class ClientGetApplicationPolicyResponseTypeDef(
    _ClientGetApplicationPolicyResponseTypeDef
):
    """
    Type definition for `ClientGetApplicationPolicy` `Response`

    Success

    - **Statements** *(list) --*

      An array of policy statements applied to the application.

      - *(dict) --*

        Policy statement applied to the application.

        - **Actions** *(list) --*

          For the list of actions supported for this operation, see `Application Permissions
          <https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions>`__
          .

          - *(string) --*

        - **Principals** *(list) --*

          An array of AWS account IDs, or * to make the application public.

          - *(string) --*

        - **StatementId** *(string) --*

          A unique ID for the statement.
    """


_ClientGetApplicationResponseVersionParameterDefinitionsTypeDef = TypedDict(
    "_ClientGetApplicationResponseVersionParameterDefinitionsTypeDef",
    {
        "AllowedPattern": str,
        "AllowedValues": List[str],
        "ConstraintDescription": str,
        "DefaultValue": str,
        "Description": str,
        "MaxLength": int,
        "MaxValue": int,
        "MinLength": int,
        "MinValue": int,
        "Name": str,
        "NoEcho": bool,
        "ReferencedByResources": List[str],
        "Type": str,
    },
    total=False,
)


class ClientGetApplicationResponseVersionParameterDefinitionsTypeDef(
    _ClientGetApplicationResponseVersionParameterDefinitionsTypeDef
):
    """
    Type definition for `ClientGetApplicationResponseVersion` `ParameterDefinitions`

    Parameters supported by the application.

    - **AllowedPattern** *(string) --*

      A regular expression that represents the patterns to allow for String types.

    - **AllowedValues** *(list) --*

      An array containing the list of values allowed for the parameter.

      - *(string) --*

    - **ConstraintDescription** *(string) --*

      A string that explains a constraint when the constraint is violated. For example,
      without a constraint description, a parameter that has an allowed pattern of
      [A-Za-z0-9]+ displays the following error message when the user specifies an invalid
      value:

      Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+

      By adding a constraint description, such as "must contain only uppercase and lowercase
      letters and numbers," you can display the following customized error message:

      Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters
      and numbers.

    - **DefaultValue** *(string) --*

      A value of the appropriate type for the template to use if no value is specified when a
      stack is created. If you define constraints for the parameter, you must specify a value
      that adheres to those constraints.

    - **Description** *(string) --*

      A string of up to 4,000 characters that describes the parameter.

    - **MaxLength** *(integer) --*

      An integer value that determines the largest number of characters that you want to
      allow for String types.

    - **MaxValue** *(integer) --*

      A numeric value that determines the largest numeric value that you want to allow for
      Number types.

    - **MinLength** *(integer) --*

      An integer value that determines the smallest number of characters that you want to
      allow for String types.

    - **MinValue** *(integer) --*

      A numeric value that determines the smallest numeric value that you want to allow for
      Number types.

    - **Name** *(string) --*

      The name of the parameter.

    - **NoEcho** *(boolean) --*

      Whether to mask the parameter value whenever anyone makes a call that describes the
      stack. If you set the value to true, the parameter value is masked with asterisks
      (*****).

    - **ReferencedByResources** *(list) --*

      A list of AWS SAM resources that use this parameter.

      - *(string) --*

    - **Type** *(string) --*

      The type of the parameter.

      Valid values: String | Number | List<Number> | CommaDelimitedList

      String: A literal string.

      For example, users can specify "MyUserName".

      Number: An integer or float. AWS CloudFormation validates the parameter value as a
      number. However, when you use the parameter elsewhere in your template (for example, by
      using the Ref intrinsic function), the parameter value becomes a string.

      For example, users might specify "8888".

      List<Number>: An array of integers or floats that are separated by commas. AWS
      CloudFormation validates the parameter value as numbers. However, when you use the
      parameter elsewhere in your template (for example, by using the Ref intrinsic
      function), the parameter value becomes a list of strings.

      For example, users might specify "80,20", and then Ref results in ["80","20"].

      CommaDelimitedList: An array of literal strings that are separated by commas. The total
      number of strings should be one more than the total number of commas. Also, each member
      string is space-trimmed.

      For example, users might specify "test,dev,prod", and then Ref results in
      ["test","dev","prod"].
    """


_ClientGetApplicationResponseVersionTypeDef = TypedDict(
    "_ClientGetApplicationResponseVersionTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List[
            ClientGetApplicationResponseVersionParameterDefinitionsTypeDef
        ],
        "RequiredCapabilities": List[str],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateUrl": str,
    },
    total=False,
)


class ClientGetApplicationResponseVersionTypeDef(
    _ClientGetApplicationResponseVersionTypeDef
):
    """
    Type definition for `ClientGetApplicationResponse` `Version`

    Version information about the application.

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **CreationTime** *(string) --*

      The date and time this resource was created.

    - **ParameterDefinitions** *(list) --*

      An array of parameter types supported by the application.

      - *(dict) --*

        Parameters supported by the application.

        - **AllowedPattern** *(string) --*

          A regular expression that represents the patterns to allow for String types.

        - **AllowedValues** *(list) --*

          An array containing the list of values allowed for the parameter.

          - *(string) --*

        - **ConstraintDescription** *(string) --*

          A string that explains a constraint when the constraint is violated. For example,
          without a constraint description, a parameter that has an allowed pattern of
          [A-Za-z0-9]+ displays the following error message when the user specifies an invalid
          value:

          Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+

          By adding a constraint description, such as "must contain only uppercase and lowercase
          letters and numbers," you can display the following customized error message:

          Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters
          and numbers.

        - **DefaultValue** *(string) --*

          A value of the appropriate type for the template to use if no value is specified when a
          stack is created. If you define constraints for the parameter, you must specify a value
          that adheres to those constraints.

        - **Description** *(string) --*

          A string of up to 4,000 characters that describes the parameter.

        - **MaxLength** *(integer) --*

          An integer value that determines the largest number of characters that you want to
          allow for String types.

        - **MaxValue** *(integer) --*

          A numeric value that determines the largest numeric value that you want to allow for
          Number types.

        - **MinLength** *(integer) --*

          An integer value that determines the smallest number of characters that you want to
          allow for String types.

        - **MinValue** *(integer) --*

          A numeric value that determines the smallest numeric value that you want to allow for
          Number types.

        - **Name** *(string) --*

          The name of the parameter.

        - **NoEcho** *(boolean) --*

          Whether to mask the parameter value whenever anyone makes a call that describes the
          stack. If you set the value to true, the parameter value is masked with asterisks
          (*****).

        - **ReferencedByResources** *(list) --*

          A list of AWS SAM resources that use this parameter.

          - *(string) --*

        - **Type** *(string) --*

          The type of the parameter.

          Valid values: String | Number | List<Number> | CommaDelimitedList

          String: A literal string.

          For example, users can specify "MyUserName".

          Number: An integer or float. AWS CloudFormation validates the parameter value as a
          number. However, when you use the parameter elsewhere in your template (for example, by
          using the Ref intrinsic function), the parameter value becomes a string.

          For example, users might specify "8888".

          List<Number>: An array of integers or floats that are separated by commas. AWS
          CloudFormation validates the parameter value as numbers. However, when you use the
          parameter elsewhere in your template (for example, by using the Ref intrinsic
          function), the parameter value becomes a list of strings.

          For example, users might specify "80,20", and then Ref results in ["80","20"].

          CommaDelimitedList: An array of literal strings that are separated by commas. The total
          number of strings should be one more than the total number of commas. Also, each member
          string is space-trimmed.

          For example, users might specify "test,dev,prod", and then Ref results in
          ["test","dev","prod"].

    - **RequiredCapabilities** *(list) --*

      A list of values that you must specify before you can deploy certain applications. Some
      applications might include resources that can affect permissions in your AWS account, for
      example, by creating new AWS Identity and Access Management (IAM) users. For those
      applications, you must explicitly acknowledge their capabilities by specifying this
      parameter.

      The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY,
      and CAPABILITY_AUTO_EXPAND.

      The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM:
      `AWS\\:\\:IAM\\:\\:Group
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__
      , `AWS\\:\\:IAM\\:\\:InstanceProfile
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__
      , `AWS\\:\\:IAM\\:\\:Policy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
      , and `AWS\\:\\:IAM\\:\\:Role
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__
      . If the application contains IAM resources, you can specify either CAPABILITY_IAM or
      CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must
      specify CAPABILITY_NAMED_IAM.

      The following resources require you to specify CAPABILITY_RESOURCE_POLICY:
      `AWS\\:\\:Lambda\\:\\:Permission
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html>`__
      , `AWS\\:\\:IAM\\:Policy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
      , `AWS\\:\\:ApplicationAutoScaling\\:\\:ScalingPolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`__
      , `AWS\\:\\:S3\\:\\:BucketPolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html>`__
      , `AWS\\:\\:SQS\\:\\:QueuePolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html>`__
      , and `AWS\\:\\:SNS\\:\\:TopicPolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html>`__
      .

      Applications that contain one or more nested applications require you to specify
      CAPABILITY_AUTO_EXPAND.

      If your application template contains any of the above resources, we recommend that you
      review all permissions associated with the application before deploying. If you don't
      specify this parameter for an application that requires capabilities, the call will fail.

      - *(string) --*

        Values that must be specified in order to deploy some applications.

    - **ResourcesSupported** *(boolean) --*

      Whether all of the AWS resources contained in this application are supported in the region
      in which it is being retrieved.

    - **SemanticVersion** *(string) --*

      The semantic version of the application:

       `https\\://semver.org/ <https://semver.org/>`__

    - **SourceCodeArchiveUrl** *(string) --*

      A link to the S3 object that contains the ZIP archive of the source code for this version
      of your application.

      Maximum size 50 MB

    - **SourceCodeUrl** *(string) --*

      A link to a public repository for the source code of your application, for example the URL
      of a specific GitHub commit.

    - **TemplateUrl** *(string) --*

      A link to the packaged AWS SAM template of your application.
    """


_ClientGetApplicationResponseTypeDef = TypedDict(
    "_ClientGetApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "Version": ClientGetApplicationResponseVersionTypeDef,
    },
    total=False,
)


class ClientGetApplicationResponseTypeDef(_ClientGetApplicationResponseTypeDef):
    """
    Type definition for `ClientGetApplication` `Response`

    Success

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **Author** *(string) --*

      The name of the author publishing the app.

      Minimum length=1. Maximum length=127.

      Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";

    - **CreationTime** *(string) --*

      The date and time this resource was created.

    - **Description** *(string) --*

      The description of the application.

      Minimum length=1. Maximum length=256

    - **HomePageUrl** *(string) --*

      A URL with more information about the application, for example the location of your GitHub
      repository for the application.

    - **Labels** *(list) --*

      Labels to improve discovery of apps in search results.

      Minimum length=1. Maximum length=127. Maximum number of labels: 10

      Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";

      - *(string) --*

    - **LicenseUrl** *(string) --*

      A link to a license file of the app that matches the spdxLicenseID value of your application.

      Maximum size 5 MB

    - **Name** *(string) --*

      The name of the application.

      Minimum length=1. Maximum length=140

      Pattern: "[a-zA-Z0-9\\-]+";

    - **ReadmeUrl** *(string) --*

      A link to the readme file in Markdown language that contains a more detailed description of
      the application and how it works.

      Maximum size 5 MB

    - **SpdxLicenseId** *(string) --*

      A valid identifier from https://spdx.org/licenses/.

    - **Version** *(dict) --*

      Version information about the application.

      - **ApplicationId** *(string) --*

        The application Amazon Resource Name (ARN).

      - **CreationTime** *(string) --*

        The date and time this resource was created.

      - **ParameterDefinitions** *(list) --*

        An array of parameter types supported by the application.

        - *(dict) --*

          Parameters supported by the application.

          - **AllowedPattern** *(string) --*

            A regular expression that represents the patterns to allow for String types.

          - **AllowedValues** *(list) --*

            An array containing the list of values allowed for the parameter.

            - *(string) --*

          - **ConstraintDescription** *(string) --*

            A string that explains a constraint when the constraint is violated. For example,
            without a constraint description, a parameter that has an allowed pattern of
            [A-Za-z0-9]+ displays the following error message when the user specifies an invalid
            value:

            Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+

            By adding a constraint description, such as "must contain only uppercase and lowercase
            letters and numbers," you can display the following customized error message:

            Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters
            and numbers.

          - **DefaultValue** *(string) --*

            A value of the appropriate type for the template to use if no value is specified when a
            stack is created. If you define constraints for the parameter, you must specify a value
            that adheres to those constraints.

          - **Description** *(string) --*

            A string of up to 4,000 characters that describes the parameter.

          - **MaxLength** *(integer) --*

            An integer value that determines the largest number of characters that you want to
            allow for String types.

          - **MaxValue** *(integer) --*

            A numeric value that determines the largest numeric value that you want to allow for
            Number types.

          - **MinLength** *(integer) --*

            An integer value that determines the smallest number of characters that you want to
            allow for String types.

          - **MinValue** *(integer) --*

            A numeric value that determines the smallest numeric value that you want to allow for
            Number types.

          - **Name** *(string) --*

            The name of the parameter.

          - **NoEcho** *(boolean) --*

            Whether to mask the parameter value whenever anyone makes a call that describes the
            stack. If you set the value to true, the parameter value is masked with asterisks
            (*****).

          - **ReferencedByResources** *(list) --*

            A list of AWS SAM resources that use this parameter.

            - *(string) --*

          - **Type** *(string) --*

            The type of the parameter.

            Valid values: String | Number | List<Number> | CommaDelimitedList

            String: A literal string.

            For example, users can specify "MyUserName".

            Number: An integer or float. AWS CloudFormation validates the parameter value as a
            number. However, when you use the parameter elsewhere in your template (for example, by
            using the Ref intrinsic function), the parameter value becomes a string.

            For example, users might specify "8888".

            List<Number>: An array of integers or floats that are separated by commas. AWS
            CloudFormation validates the parameter value as numbers. However, when you use the
            parameter elsewhere in your template (for example, by using the Ref intrinsic
            function), the parameter value becomes a list of strings.

            For example, users might specify "80,20", and then Ref results in ["80","20"].

            CommaDelimitedList: An array of literal strings that are separated by commas. The total
            number of strings should be one more than the total number of commas. Also, each member
            string is space-trimmed.

            For example, users might specify "test,dev,prod", and then Ref results in
            ["test","dev","prod"].

      - **RequiredCapabilities** *(list) --*

        A list of values that you must specify before you can deploy certain applications. Some
        applications might include resources that can affect permissions in your AWS account, for
        example, by creating new AWS Identity and Access Management (IAM) users. For those
        applications, you must explicitly acknowledge their capabilities by specifying this
        parameter.

        The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY,
        and CAPABILITY_AUTO_EXPAND.

        The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM:
        `AWS\\:\\:IAM\\:\\:Group
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__
        , `AWS\\:\\:IAM\\:\\:InstanceProfile
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__
        , `AWS\\:\\:IAM\\:\\:Policy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
        , and `AWS\\:\\:IAM\\:\\:Role
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__
        . If the application contains IAM resources, you can specify either CAPABILITY_IAM or
        CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must
        specify CAPABILITY_NAMED_IAM.

        The following resources require you to specify CAPABILITY_RESOURCE_POLICY:
        `AWS\\:\\:Lambda\\:\\:Permission
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html>`__
        , `AWS\\:\\:IAM\\:Policy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
        , `AWS\\:\\:ApplicationAutoScaling\\:\\:ScalingPolicy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`__
        , `AWS\\:\\:S3\\:\\:BucketPolicy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html>`__
        , `AWS\\:\\:SQS\\:\\:QueuePolicy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html>`__
        , and `AWS\\:\\:SNS\\:\\:TopicPolicy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html>`__
        .

        Applications that contain one or more nested applications require you to specify
        CAPABILITY_AUTO_EXPAND.

        If your application template contains any of the above resources, we recommend that you
        review all permissions associated with the application before deploying. If you don't
        specify this parameter for an application that requires capabilities, the call will fail.

        - *(string) --*

          Values that must be specified in order to deploy some applications.

      - **ResourcesSupported** *(boolean) --*

        Whether all of the AWS resources contained in this application are supported in the region
        in which it is being retrieved.

      - **SemanticVersion** *(string) --*

        The semantic version of the application:

         `https\\://semver.org/ <https://semver.org/>`__

      - **SourceCodeArchiveUrl** *(string) --*

        A link to the S3 object that contains the ZIP archive of the source code for this version
        of your application.

        Maximum size 50 MB

      - **SourceCodeUrl** *(string) --*

        A link to a public repository for the source code of your application, for example the URL
        of a specific GitHub commit.

      - **TemplateUrl** *(string) --*

        A link to the packaged AWS SAM template of your application.
    """


_ClientGetCloudFormationTemplateResponseTypeDef = TypedDict(
    "_ClientGetCloudFormationTemplateResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ExpirationTime": str,
        "SemanticVersion": str,
        "Status": str,
        "TemplateId": str,
        "TemplateUrl": str,
    },
    total=False,
)


class ClientGetCloudFormationTemplateResponseTypeDef(
    _ClientGetCloudFormationTemplateResponseTypeDef
):
    """
    Type definition for `ClientGetCloudFormationTemplate` `Response`

    Success

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **CreationTime** *(string) --*

      The date and time this resource was created.

    - **ExpirationTime** *(string) --*

      The date and time this template expires. Templates expire 1 hour after creation.

    - **SemanticVersion** *(string) --*

      The semantic version of the application:

       `https\\://semver.org/ <https://semver.org/>`__

    - **Status** *(string) --*

      Status of the template creation workflow.

      Possible values: PREPARING | ACTIVE | EXPIRED

    - **TemplateId** *(string) --*

      The UUID returned by CreateCloudFormationTemplate.

      Pattern: [0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12}

    - **TemplateUrl** *(string) --*

      A link to the template that can be used to deploy the application using AWS CloudFormation.
    """


_ClientListApplicationDependenciesResponseDependenciesTypeDef = TypedDict(
    "_ClientListApplicationDependenciesResponseDependenciesTypeDef",
    {"ApplicationId": str, "SemanticVersion": str},
    total=False,
)


class ClientListApplicationDependenciesResponseDependenciesTypeDef(
    _ClientListApplicationDependenciesResponseDependenciesTypeDef
):
    """
    Type definition for `ClientListApplicationDependenciesResponse` `Dependencies`

    A nested application summary.

    - **ApplicationId** *(string) --*

      The Amazon Resource Name (ARN) of the nested application.

    - **SemanticVersion** *(string) --*

      The semantic version of the nested application.
    """


_ClientListApplicationDependenciesResponseTypeDef = TypedDict(
    "_ClientListApplicationDependenciesResponseTypeDef",
    {
        "Dependencies": List[
            ClientListApplicationDependenciesResponseDependenciesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListApplicationDependenciesResponseTypeDef(
    _ClientListApplicationDependenciesResponseTypeDef
):
    """
    Type definition for `ClientListApplicationDependencies` `Response`

    Success

    - **Dependencies** *(list) --*

      An array of application summaries nested in the application.

      - *(dict) --*

        A nested application summary.

        - **ApplicationId** *(string) --*

          The Amazon Resource Name (ARN) of the nested application.

        - **SemanticVersion** *(string) --*

          The semantic version of the nested application.

    - **NextToken** *(string) --*

      The token to request the next page of results.
    """


_ClientListApplicationVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListApplicationVersionsResponseVersionsTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "SemanticVersion": str,
        "SourceCodeUrl": str,
    },
    total=False,
)


class ClientListApplicationVersionsResponseVersionsTypeDef(
    _ClientListApplicationVersionsResponseVersionsTypeDef
):
    """
    Type definition for `ClientListApplicationVersionsResponse` `Versions`

    An application version summary.

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **CreationTime** *(string) --*

      The date and time this resource was created.

    - **SemanticVersion** *(string) --*

      The semantic version of the application:

       `https\\://semver.org/ <https://semver.org/>`__

    - **SourceCodeUrl** *(string) --*

      A link to a public repository for the source code of your application, for example the
      URL of a specific GitHub commit.
    """


_ClientListApplicationVersionsResponseTypeDef = TypedDict(
    "_ClientListApplicationVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListApplicationVersionsResponseVersionsTypeDef],
    },
    total=False,
)


class ClientListApplicationVersionsResponseTypeDef(
    _ClientListApplicationVersionsResponseTypeDef
):
    """
    Type definition for `ClientListApplicationVersions` `Response`

    Success

    - **NextToken** *(string) --*

      The token to request the next page of results.

    - **Versions** *(list) --*

      An array of version summaries for the application.

      - *(dict) --*

        An application version summary.

        - **ApplicationId** *(string) --*

          The application Amazon Resource Name (ARN).

        - **CreationTime** *(string) --*

          The date and time this resource was created.

        - **SemanticVersion** *(string) --*

          The semantic version of the application:

           `https\\://semver.org/ <https://semver.org/>`__

        - **SourceCodeUrl** *(string) --*

          A link to a public repository for the source code of your application, for example the
          URL of a specific GitHub commit.
    """


_ClientListApplicationsResponseApplicationsTypeDef = TypedDict(
    "_ClientListApplicationsResponseApplicationsTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "Labels": List[str],
        "Name": str,
        "SpdxLicenseId": str,
    },
    total=False,
)


class ClientListApplicationsResponseApplicationsTypeDef(
    _ClientListApplicationsResponseApplicationsTypeDef
):
    """
    Type definition for `ClientListApplicationsResponse` `Applications`

    Summary of details about the application.

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **Author** *(string) --*

      The name of the author publishing the app.

      Minimum length=1. Maximum length=127.

      Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";

    - **CreationTime** *(string) --*

      The date and time this resource was created.

    - **Description** *(string) --*

      The description of the application.

      Minimum length=1. Maximum length=256

    - **HomePageUrl** *(string) --*

      A URL with more information about the application, for example the location of your
      GitHub repository for the application.

    - **Labels** *(list) --*

      Labels to improve discovery of apps in search results.

      Minimum length=1. Maximum length=127. Maximum number of labels: 10

      Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";

      - *(string) --*

    - **Name** *(string) --*

      The name of the application.

      Minimum length=1. Maximum length=140

      Pattern: "[a-zA-Z0-9\\-]+";

    - **SpdxLicenseId** *(string) --*

      A valid identifier from `https\\://spdx.org/licenses/ <https://spdx.org/licenses/>`__ .
    """


_ClientListApplicationsResponseTypeDef = TypedDict(
    "_ClientListApplicationsResponseTypeDef",
    {
        "Applications": List[ClientListApplicationsResponseApplicationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListApplicationsResponseTypeDef(_ClientListApplicationsResponseTypeDef):
    """
    Type definition for `ClientListApplications` `Response`

    Success

    - **Applications** *(list) --*

      An array of application summaries.

      - *(dict) --*

        Summary of details about the application.

        - **ApplicationId** *(string) --*

          The application Amazon Resource Name (ARN).

        - **Author** *(string) --*

          The name of the author publishing the app.

          Minimum length=1. Maximum length=127.

          Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";

        - **CreationTime** *(string) --*

          The date and time this resource was created.

        - **Description** *(string) --*

          The description of the application.

          Minimum length=1. Maximum length=256

        - **HomePageUrl** *(string) --*

          A URL with more information about the application, for example the location of your
          GitHub repository for the application.

        - **Labels** *(list) --*

          Labels to improve discovery of apps in search results.

          Minimum length=1. Maximum length=127. Maximum number of labels: 10

          Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";

          - *(string) --*

        - **Name** *(string) --*

          The name of the application.

          Minimum length=1. Maximum length=140

          Pattern: "[a-zA-Z0-9\\-]+";

        - **SpdxLicenseId** *(string) --*

          A valid identifier from `https\\://spdx.org/licenses/ <https://spdx.org/licenses/>`__ .

    - **NextToken** *(string) --*

      The token to request the next page of results.
    """


_ClientPutApplicationPolicyResponseStatementsTypeDef = TypedDict(
    "_ClientPutApplicationPolicyResponseStatementsTypeDef",
    {"Actions": List[str], "Principals": List[str], "StatementId": str},
    total=False,
)


class ClientPutApplicationPolicyResponseStatementsTypeDef(
    _ClientPutApplicationPolicyResponseStatementsTypeDef
):
    """
    Type definition for `ClientPutApplicationPolicyResponse` `Statements`

    Policy statement applied to the application.

    - **Actions** *(list) --*

      For the list of actions supported for this operation, see `Application Permissions
      <https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions>`__
      .

      - *(string) --*

    - **Principals** *(list) --*

      An array of AWS account IDs, or * to make the application public.

      - *(string) --*

    - **StatementId** *(string) --*

      A unique ID for the statement.
    """


_ClientPutApplicationPolicyResponseTypeDef = TypedDict(
    "_ClientPutApplicationPolicyResponseTypeDef",
    {"Statements": List[ClientPutApplicationPolicyResponseStatementsTypeDef]},
    total=False,
)


class ClientPutApplicationPolicyResponseTypeDef(
    _ClientPutApplicationPolicyResponseTypeDef
):
    """
    Type definition for `ClientPutApplicationPolicy` `Response`

    Success

    - **Statements** *(list) --*

      An array of policy statements applied to the application.

      - *(dict) --*

        Policy statement applied to the application.

        - **Actions** *(list) --*

          For the list of actions supported for this operation, see `Application Permissions
          <https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions>`__
          .

          - *(string) --*

        - **Principals** *(list) --*

          An array of AWS account IDs, or * to make the application public.

          - *(string) --*

        - **StatementId** *(string) --*

          A unique ID for the statement.
    """


_RequiredClientPutApplicationPolicyStatementsTypeDef = TypedDict(
    "_RequiredClientPutApplicationPolicyStatementsTypeDef",
    {"Actions": List[str], "Principals": List[str]},
)
_OptionalClientPutApplicationPolicyStatementsTypeDef = TypedDict(
    "_OptionalClientPutApplicationPolicyStatementsTypeDef",
    {"StatementId": str},
    total=False,
)


class ClientPutApplicationPolicyStatementsTypeDef(
    _RequiredClientPutApplicationPolicyStatementsTypeDef,
    _OptionalClientPutApplicationPolicyStatementsTypeDef,
):
    """
    Type definition for `ClientPutApplicationPolicy` `Statements`

    Policy statement applied to the application.

    - **Actions** *(list) --* **[REQUIRED]**

      For the list of actions supported for this operation, see `Application Permissions
      <https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions>`__
      .

      - *(string) --*

    - **Principals** *(list) --* **[REQUIRED]**

      An array of AWS account IDs, or * to make the application public.

      - *(string) --*

    - **StatementId** *(string) --*

      A unique ID for the statement.
    """


_ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef",
    {
        "AllowedPattern": str,
        "AllowedValues": List[str],
        "ConstraintDescription": str,
        "DefaultValue": str,
        "Description": str,
        "MaxLength": int,
        "MaxValue": int,
        "MinLength": int,
        "MinValue": int,
        "Name": str,
        "NoEcho": bool,
        "ReferencedByResources": List[str],
        "Type": str,
    },
    total=False,
)


class ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef(
    _ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseVersion` `ParameterDefinitions`

    Parameters supported by the application.

    - **AllowedPattern** *(string) --*

      A regular expression that represents the patterns to allow for String types.

    - **AllowedValues** *(list) --*

      An array containing the list of values allowed for the parameter.

      - *(string) --*

    - **ConstraintDescription** *(string) --*

      A string that explains a constraint when the constraint is violated. For example,
      without a constraint description, a parameter that has an allowed pattern of
      [A-Za-z0-9]+ displays the following error message when the user specifies an invalid
      value:

      Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+

      By adding a constraint description, such as "must contain only uppercase and lowercase
      letters and numbers," you can display the following customized error message:

      Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters
      and numbers.

    - **DefaultValue** *(string) --*

      A value of the appropriate type for the template to use if no value is specified when a
      stack is created. If you define constraints for the parameter, you must specify a value
      that adheres to those constraints.

    - **Description** *(string) --*

      A string of up to 4,000 characters that describes the parameter.

    - **MaxLength** *(integer) --*

      An integer value that determines the largest number of characters that you want to
      allow for String types.

    - **MaxValue** *(integer) --*

      A numeric value that determines the largest numeric value that you want to allow for
      Number types.

    - **MinLength** *(integer) --*

      An integer value that determines the smallest number of characters that you want to
      allow for String types.

    - **MinValue** *(integer) --*

      A numeric value that determines the smallest numeric value that you want to allow for
      Number types.

    - **Name** *(string) --*

      The name of the parameter.

    - **NoEcho** *(boolean) --*

      Whether to mask the parameter value whenever anyone makes a call that describes the
      stack. If you set the value to true, the parameter value is masked with asterisks
      (*****).

    - **ReferencedByResources** *(list) --*

      A list of AWS SAM resources that use this parameter.

      - *(string) --*

    - **Type** *(string) --*

      The type of the parameter.

      Valid values: String | Number | List<Number> | CommaDelimitedList

      String: A literal string.

      For example, users can specify "MyUserName".

      Number: An integer or float. AWS CloudFormation validates the parameter value as a
      number. However, when you use the parameter elsewhere in your template (for example, by
      using the Ref intrinsic function), the parameter value becomes a string.

      For example, users might specify "8888".

      List<Number>: An array of integers or floats that are separated by commas. AWS
      CloudFormation validates the parameter value as numbers. However, when you use the
      parameter elsewhere in your template (for example, by using the Ref intrinsic
      function), the parameter value becomes a list of strings.

      For example, users might specify "80,20", and then Ref results in ["80","20"].

      CommaDelimitedList: An array of literal strings that are separated by commas. The total
      number of strings should be one more than the total number of commas. Also, each member
      string is space-trimmed.

      For example, users might specify "test,dev,prod", and then Ref results in
      ["test","dev","prod"].
    """


_ClientUpdateApplicationResponseVersionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseVersionTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List[
            ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef
        ],
        "RequiredCapabilities": List[str],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateUrl": str,
    },
    total=False,
)


class ClientUpdateApplicationResponseVersionTypeDef(
    _ClientUpdateApplicationResponseVersionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponse` `Version`

    Version information about the application.

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **CreationTime** *(string) --*

      The date and time this resource was created.

    - **ParameterDefinitions** *(list) --*

      An array of parameter types supported by the application.

      - *(dict) --*

        Parameters supported by the application.

        - **AllowedPattern** *(string) --*

          A regular expression that represents the patterns to allow for String types.

        - **AllowedValues** *(list) --*

          An array containing the list of values allowed for the parameter.

          - *(string) --*

        - **ConstraintDescription** *(string) --*

          A string that explains a constraint when the constraint is violated. For example,
          without a constraint description, a parameter that has an allowed pattern of
          [A-Za-z0-9]+ displays the following error message when the user specifies an invalid
          value:

          Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+

          By adding a constraint description, such as "must contain only uppercase and lowercase
          letters and numbers," you can display the following customized error message:

          Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters
          and numbers.

        - **DefaultValue** *(string) --*

          A value of the appropriate type for the template to use if no value is specified when a
          stack is created. If you define constraints for the parameter, you must specify a value
          that adheres to those constraints.

        - **Description** *(string) --*

          A string of up to 4,000 characters that describes the parameter.

        - **MaxLength** *(integer) --*

          An integer value that determines the largest number of characters that you want to
          allow for String types.

        - **MaxValue** *(integer) --*

          A numeric value that determines the largest numeric value that you want to allow for
          Number types.

        - **MinLength** *(integer) --*

          An integer value that determines the smallest number of characters that you want to
          allow for String types.

        - **MinValue** *(integer) --*

          A numeric value that determines the smallest numeric value that you want to allow for
          Number types.

        - **Name** *(string) --*

          The name of the parameter.

        - **NoEcho** *(boolean) --*

          Whether to mask the parameter value whenever anyone makes a call that describes the
          stack. If you set the value to true, the parameter value is masked with asterisks
          (*****).

        - **ReferencedByResources** *(list) --*

          A list of AWS SAM resources that use this parameter.

          - *(string) --*

        - **Type** *(string) --*

          The type of the parameter.

          Valid values: String | Number | List<Number> | CommaDelimitedList

          String: A literal string.

          For example, users can specify "MyUserName".

          Number: An integer or float. AWS CloudFormation validates the parameter value as a
          number. However, when you use the parameter elsewhere in your template (for example, by
          using the Ref intrinsic function), the parameter value becomes a string.

          For example, users might specify "8888".

          List<Number>: An array of integers or floats that are separated by commas. AWS
          CloudFormation validates the parameter value as numbers. However, when you use the
          parameter elsewhere in your template (for example, by using the Ref intrinsic
          function), the parameter value becomes a list of strings.

          For example, users might specify "80,20", and then Ref results in ["80","20"].

          CommaDelimitedList: An array of literal strings that are separated by commas. The total
          number of strings should be one more than the total number of commas. Also, each member
          string is space-trimmed.

          For example, users might specify "test,dev,prod", and then Ref results in
          ["test","dev","prod"].

    - **RequiredCapabilities** *(list) --*

      A list of values that you must specify before you can deploy certain applications. Some
      applications might include resources that can affect permissions in your AWS account, for
      example, by creating new AWS Identity and Access Management (IAM) users. For those
      applications, you must explicitly acknowledge their capabilities by specifying this
      parameter.

      The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY,
      and CAPABILITY_AUTO_EXPAND.

      The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM:
      `AWS\\:\\:IAM\\:\\:Group
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__
      , `AWS\\:\\:IAM\\:\\:InstanceProfile
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__
      , `AWS\\:\\:IAM\\:\\:Policy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
      , and `AWS\\:\\:IAM\\:\\:Role
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__
      . If the application contains IAM resources, you can specify either CAPABILITY_IAM or
      CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must
      specify CAPABILITY_NAMED_IAM.

      The following resources require you to specify CAPABILITY_RESOURCE_POLICY:
      `AWS\\:\\:Lambda\\:\\:Permission
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html>`__
      , `AWS\\:\\:IAM\\:Policy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
      , `AWS\\:\\:ApplicationAutoScaling\\:\\:ScalingPolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`__
      , `AWS\\:\\:S3\\:\\:BucketPolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html>`__
      , `AWS\\:\\:SQS\\:\\:QueuePolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html>`__
      , and `AWS\\:\\:SNS\\:\\:TopicPolicy
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html>`__
      .

      Applications that contain one or more nested applications require you to specify
      CAPABILITY_AUTO_EXPAND.

      If your application template contains any of the above resources, we recommend that you
      review all permissions associated with the application before deploying. If you don't
      specify this parameter for an application that requires capabilities, the call will fail.

      - *(string) --*

        Values that must be specified in order to deploy some applications.

    - **ResourcesSupported** *(boolean) --*

      Whether all of the AWS resources contained in this application are supported in the region
      in which it is being retrieved.

    - **SemanticVersion** *(string) --*

      The semantic version of the application:

       `https\\://semver.org/ <https://semver.org/>`__

    - **SourceCodeArchiveUrl** *(string) --*

      A link to the S3 object that contains the ZIP archive of the source code for this version
      of your application.

      Maximum size 50 MB

    - **SourceCodeUrl** *(string) --*

      A link to a public repository for the source code of your application, for example the URL
      of a specific GitHub commit.

    - **TemplateUrl** *(string) --*

      A link to the packaged AWS SAM template of your application.
    """


_ClientUpdateApplicationResponseTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "Version": ClientUpdateApplicationResponseVersionTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseTypeDef(_ClientUpdateApplicationResponseTypeDef):
    """
    Type definition for `ClientUpdateApplication` `Response`

    Success

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **Author** *(string) --*

      The name of the author publishing the app.

      Minimum length=1. Maximum length=127.

      Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";

    - **CreationTime** *(string) --*

      The date and time this resource was created.

    - **Description** *(string) --*

      The description of the application.

      Minimum length=1. Maximum length=256

    - **HomePageUrl** *(string) --*

      A URL with more information about the application, for example the location of your GitHub
      repository for the application.

    - **Labels** *(list) --*

      Labels to improve discovery of apps in search results.

      Minimum length=1. Maximum length=127. Maximum number of labels: 10

      Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";

      - *(string) --*

    - **LicenseUrl** *(string) --*

      A link to a license file of the app that matches the spdxLicenseID value of your application.

      Maximum size 5 MB

    - **Name** *(string) --*

      The name of the application.

      Minimum length=1. Maximum length=140

      Pattern: "[a-zA-Z0-9\\-]+";

    - **ReadmeUrl** *(string) --*

      A link to the readme file in Markdown language that contains a more detailed description of
      the application and how it works.

      Maximum size 5 MB

    - **SpdxLicenseId** *(string) --*

      A valid identifier from https://spdx.org/licenses/.

    - **Version** *(dict) --*

      Version information about the application.

      - **ApplicationId** *(string) --*

        The application Amazon Resource Name (ARN).

      - **CreationTime** *(string) --*

        The date and time this resource was created.

      - **ParameterDefinitions** *(list) --*

        An array of parameter types supported by the application.

        - *(dict) --*

          Parameters supported by the application.

          - **AllowedPattern** *(string) --*

            A regular expression that represents the patterns to allow for String types.

          - **AllowedValues** *(list) --*

            An array containing the list of values allowed for the parameter.

            - *(string) --*

          - **ConstraintDescription** *(string) --*

            A string that explains a constraint when the constraint is violated. For example,
            without a constraint description, a parameter that has an allowed pattern of
            [A-Za-z0-9]+ displays the following error message when the user specifies an invalid
            value:

            Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+

            By adding a constraint description, such as "must contain only uppercase and lowercase
            letters and numbers," you can display the following customized error message:

            Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters
            and numbers.

          - **DefaultValue** *(string) --*

            A value of the appropriate type for the template to use if no value is specified when a
            stack is created. If you define constraints for the parameter, you must specify a value
            that adheres to those constraints.

          - **Description** *(string) --*

            A string of up to 4,000 characters that describes the parameter.

          - **MaxLength** *(integer) --*

            An integer value that determines the largest number of characters that you want to
            allow for String types.

          - **MaxValue** *(integer) --*

            A numeric value that determines the largest numeric value that you want to allow for
            Number types.

          - **MinLength** *(integer) --*

            An integer value that determines the smallest number of characters that you want to
            allow for String types.

          - **MinValue** *(integer) --*

            A numeric value that determines the smallest numeric value that you want to allow for
            Number types.

          - **Name** *(string) --*

            The name of the parameter.

          - **NoEcho** *(boolean) --*

            Whether to mask the parameter value whenever anyone makes a call that describes the
            stack. If you set the value to true, the parameter value is masked with asterisks
            (*****).

          - **ReferencedByResources** *(list) --*

            A list of AWS SAM resources that use this parameter.

            - *(string) --*

          - **Type** *(string) --*

            The type of the parameter.

            Valid values: String | Number | List<Number> | CommaDelimitedList

            String: A literal string.

            For example, users can specify "MyUserName".

            Number: An integer or float. AWS CloudFormation validates the parameter value as a
            number. However, when you use the parameter elsewhere in your template (for example, by
            using the Ref intrinsic function), the parameter value becomes a string.

            For example, users might specify "8888".

            List<Number>: An array of integers or floats that are separated by commas. AWS
            CloudFormation validates the parameter value as numbers. However, when you use the
            parameter elsewhere in your template (for example, by using the Ref intrinsic
            function), the parameter value becomes a list of strings.

            For example, users might specify "80,20", and then Ref results in ["80","20"].

            CommaDelimitedList: An array of literal strings that are separated by commas. The total
            number of strings should be one more than the total number of commas. Also, each member
            string is space-trimmed.

            For example, users might specify "test,dev,prod", and then Ref results in
            ["test","dev","prod"].

      - **RequiredCapabilities** *(list) --*

        A list of values that you must specify before you can deploy certain applications. Some
        applications might include resources that can affect permissions in your AWS account, for
        example, by creating new AWS Identity and Access Management (IAM) users. For those
        applications, you must explicitly acknowledge their capabilities by specifying this
        parameter.

        The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY,
        and CAPABILITY_AUTO_EXPAND.

        The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM:
        `AWS\\:\\:IAM\\:\\:Group
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__
        , `AWS\\:\\:IAM\\:\\:InstanceProfile
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__
        , `AWS\\:\\:IAM\\:\\:Policy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
        , and `AWS\\:\\:IAM\\:\\:Role
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__
        . If the application contains IAM resources, you can specify either CAPABILITY_IAM or
        CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must
        specify CAPABILITY_NAMED_IAM.

        The following resources require you to specify CAPABILITY_RESOURCE_POLICY:
        `AWS\\:\\:Lambda\\:\\:Permission
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html>`__
        , `AWS\\:\\:IAM\\:Policy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>`__
        , `AWS\\:\\:ApplicationAutoScaling\\:\\:ScalingPolicy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`__
        , `AWS\\:\\:S3\\:\\:BucketPolicy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html>`__
        , `AWS\\:\\:SQS\\:\\:QueuePolicy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html>`__
        , and `AWS\\:\\:SNS\\:\\:TopicPolicy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html>`__
        .

        Applications that contain one or more nested applications require you to specify
        CAPABILITY_AUTO_EXPAND.

        If your application template contains any of the above resources, we recommend that you
        review all permissions associated with the application before deploying. If you don't
        specify this parameter for an application that requires capabilities, the call will fail.

        - *(string) --*

          Values that must be specified in order to deploy some applications.

      - **ResourcesSupported** *(boolean) --*

        Whether all of the AWS resources contained in this application are supported in the region
        in which it is being retrieved.

      - **SemanticVersion** *(string) --*

        The semantic version of the application:

         `https\\://semver.org/ <https://semver.org/>`__

      - **SourceCodeArchiveUrl** *(string) --*

        A link to the S3 object that contains the ZIP archive of the source code for this version
        of your application.

        Maximum size 50 MB

      - **SourceCodeUrl** *(string) --*

        A link to a public repository for the source code of your application, for example the URL
        of a specific GitHub commit.

      - **TemplateUrl** *(string) --*

        A link to the packaged AWS SAM template of your application.
    """


_ListApplicationDependenciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListApplicationDependenciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListApplicationDependenciesPaginatePaginationConfigTypeDef(
    _ListApplicationDependenciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListApplicationDependenciesPaginate` `PaginationConfig`

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


_ListApplicationDependenciesPaginateResponseDependenciesTypeDef = TypedDict(
    "_ListApplicationDependenciesPaginateResponseDependenciesTypeDef",
    {"ApplicationId": str, "SemanticVersion": str},
    total=False,
)


class ListApplicationDependenciesPaginateResponseDependenciesTypeDef(
    _ListApplicationDependenciesPaginateResponseDependenciesTypeDef
):
    """
    Type definition for `ListApplicationDependenciesPaginateResponse` `Dependencies`

    A nested application summary.

    - **ApplicationId** *(string) --*

      The Amazon Resource Name (ARN) of the nested application.

    - **SemanticVersion** *(string) --*

      The semantic version of the nested application.
    """


_ListApplicationDependenciesPaginateResponseTypeDef = TypedDict(
    "_ListApplicationDependenciesPaginateResponseTypeDef",
    {
        "Dependencies": List[
            ListApplicationDependenciesPaginateResponseDependenciesTypeDef
        ]
    },
    total=False,
)


class ListApplicationDependenciesPaginateResponseTypeDef(
    _ListApplicationDependenciesPaginateResponseTypeDef
):
    """
    Type definition for `ListApplicationDependenciesPaginate` `Response`

    Success

    - **Dependencies** *(list) --*

      An array of application summaries nested in the application.

      - *(dict) --*

        A nested application summary.

        - **ApplicationId** *(string) --*

          The Amazon Resource Name (ARN) of the nested application.

        - **SemanticVersion** *(string) --*

          The semantic version of the nested application.
    """


_ListApplicationVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListApplicationVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListApplicationVersionsPaginatePaginationConfigTypeDef(
    _ListApplicationVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListApplicationVersionsPaginate` `PaginationConfig`

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


_ListApplicationVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListApplicationVersionsPaginateResponseVersionsTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "SemanticVersion": str,
        "SourceCodeUrl": str,
    },
    total=False,
)


class ListApplicationVersionsPaginateResponseVersionsTypeDef(
    _ListApplicationVersionsPaginateResponseVersionsTypeDef
):
    """
    Type definition for `ListApplicationVersionsPaginateResponse` `Versions`

    An application version summary.

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **CreationTime** *(string) --*

      The date and time this resource was created.

    - **SemanticVersion** *(string) --*

      The semantic version of the application:

       `https\\://semver.org/ <https://semver.org/>`__

    - **SourceCodeUrl** *(string) --*

      A link to a public repository for the source code of your application, for example the
      URL of a specific GitHub commit.
    """


_ListApplicationVersionsPaginateResponseTypeDef = TypedDict(
    "_ListApplicationVersionsPaginateResponseTypeDef",
    {"Versions": List[ListApplicationVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListApplicationVersionsPaginateResponseTypeDef(
    _ListApplicationVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListApplicationVersionsPaginate` `Response`

    Success

    - **Versions** *(list) --*

      An array of version summaries for the application.

      - *(dict) --*

        An application version summary.

        - **ApplicationId** *(string) --*

          The application Amazon Resource Name (ARN).

        - **CreationTime** *(string) --*

          The date and time this resource was created.

        - **SemanticVersion** *(string) --*

          The semantic version of the application:

           `https\\://semver.org/ <https://semver.org/>`__

        - **SourceCodeUrl** *(string) --*

          A link to a public repository for the source code of your application, for example the
          URL of a specific GitHub commit.
    """


_ListApplicationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListApplicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListApplicationsPaginatePaginationConfigTypeDef(
    _ListApplicationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListApplicationsPaginate` `PaginationConfig`

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


_ListApplicationsPaginateResponseApplicationsTypeDef = TypedDict(
    "_ListApplicationsPaginateResponseApplicationsTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "Labels": List[str],
        "Name": str,
        "SpdxLicenseId": str,
    },
    total=False,
)


class ListApplicationsPaginateResponseApplicationsTypeDef(
    _ListApplicationsPaginateResponseApplicationsTypeDef
):
    """
    Type definition for `ListApplicationsPaginateResponse` `Applications`

    Summary of details about the application.

    - **ApplicationId** *(string) --*

      The application Amazon Resource Name (ARN).

    - **Author** *(string) --*

      The name of the author publishing the app.

      Minimum length=1. Maximum length=127.

      Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";

    - **CreationTime** *(string) --*

      The date and time this resource was created.

    - **Description** *(string) --*

      The description of the application.

      Minimum length=1. Maximum length=256

    - **HomePageUrl** *(string) --*

      A URL with more information about the application, for example the location of your
      GitHub repository for the application.

    - **Labels** *(list) --*

      Labels to improve discovery of apps in search results.

      Minimum length=1. Maximum length=127. Maximum number of labels: 10

      Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";

      - *(string) --*

    - **Name** *(string) --*

      The name of the application.

      Minimum length=1. Maximum length=140

      Pattern: "[a-zA-Z0-9\\-]+";

    - **SpdxLicenseId** *(string) --*

      A valid identifier from `https\\://spdx.org/licenses/ <https://spdx.org/licenses/>`__ .
    """


_ListApplicationsPaginateResponseTypeDef = TypedDict(
    "_ListApplicationsPaginateResponseTypeDef",
    {"Applications": List[ListApplicationsPaginateResponseApplicationsTypeDef]},
    total=False,
)


class ListApplicationsPaginateResponseTypeDef(_ListApplicationsPaginateResponseTypeDef):
    """
    Type definition for `ListApplicationsPaginate` `Response`

    Success

    - **Applications** *(list) --*

      An array of application summaries.

      - *(dict) --*

        Summary of details about the application.

        - **ApplicationId** *(string) --*

          The application Amazon Resource Name (ARN).

        - **Author** *(string) --*

          The name of the author publishing the app.

          Minimum length=1. Maximum length=127.

          Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";

        - **CreationTime** *(string) --*

          The date and time this resource was created.

        - **Description** *(string) --*

          The description of the application.

          Minimum length=1. Maximum length=256

        - **HomePageUrl** *(string) --*

          A URL with more information about the application, for example the location of your
          GitHub repository for the application.

        - **Labels** *(list) --*

          Labels to improve discovery of apps in search results.

          Minimum length=1. Maximum length=127. Maximum number of labels: 10

          Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";

          - *(string) --*

        - **Name** *(string) --*

          The name of the application.

          Minimum length=1. Maximum length=140

          Pattern: "[a-zA-Z0-9\\-]+";

        - **SpdxLicenseId** *(string) --*

          A valid identifier from `https\\://spdx.org/licenses/ <https://spdx.org/licenses/>`__ .
    """
