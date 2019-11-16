"Main interface for mturk type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef",
    "ClientCreateHitAssignmentReviewPolicyParametersTypeDef",
    "ClientCreateHitAssignmentReviewPolicyTypeDef",
    "ClientCreateHitHITLayoutParametersTypeDef",
    "ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef",
    "ClientCreateHitHITReviewPolicyParametersTypeDef",
    "ClientCreateHitHITReviewPolicyTypeDef",
    "ClientCreateHitQualificationRequirementsLocaleValuesTypeDef",
    "ClientCreateHitQualificationRequirementsTypeDef",
    "ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef",
    "ClientCreateHitResponseHITQualificationRequirementsTypeDef",
    "ClientCreateHitResponseHITTypeDef",
    "ClientCreateHitResponseTypeDef",
    "ClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef",
    "ClientCreateHitTypeQualificationRequirementsTypeDef",
    "ClientCreateHitTypeResponseTypeDef",
    "ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef",
    "ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef",
    "ClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef",
    "ClientCreateHitWithHitTypeHITLayoutParametersTypeDef",
    "ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef",
    "ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef",
    "ClientCreateHitWithHitTypeHITReviewPolicyTypeDef",
    "ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef",
    "ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef",
    "ClientCreateHitWithHitTypeResponseHITTypeDef",
    "ClientCreateHitWithHitTypeResponseTypeDef",
    "ClientCreateQualificationTypeResponseQualificationTypeTypeDef",
    "ClientCreateQualificationTypeResponseTypeDef",
    "ClientGetAccountBalanceResponseTypeDef",
    "ClientGetAssignmentResponseAssignmentTypeDef",
    "ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef",
    "ClientGetAssignmentResponseHITQualificationRequirementsTypeDef",
    "ClientGetAssignmentResponseHITTypeDef",
    "ClientGetAssignmentResponseTypeDef",
    "ClientGetFileUploadUrlResponseTypeDef",
    "ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef",
    "ClientGetHitResponseHITQualificationRequirementsTypeDef",
    "ClientGetHitResponseHITTypeDef",
    "ClientGetHitResponseTypeDef",
    "ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef",
    "ClientGetQualificationScoreResponseQualificationTypeDef",
    "ClientGetQualificationScoreResponseTypeDef",
    "ClientGetQualificationTypeResponseQualificationTypeTypeDef",
    "ClientGetQualificationTypeResponseTypeDef",
    "ClientListAssignmentsForHitResponseAssignmentsTypeDef",
    "ClientListAssignmentsForHitResponseTypeDef",
    "ClientListBonusPaymentsResponseBonusPaymentsTypeDef",
    "ClientListBonusPaymentsResponseTypeDef",
    "ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef",
    "ClientListHitsForQualificationTypeResponseHITsTypeDef",
    "ClientListHitsForQualificationTypeResponseTypeDef",
    "ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ClientListHitsResponseHITsQualificationRequirementsTypeDef",
    "ClientListHitsResponseHITsTypeDef",
    "ClientListHitsResponseTypeDef",
    "ClientListQualificationRequestsResponseQualificationRequestsTypeDef",
    "ClientListQualificationRequestsResponseTypeDef",
    "ClientListQualificationTypesResponseQualificationTypesTypeDef",
    "ClientListQualificationTypesResponseTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef",
    "ClientListReviewPolicyResultsForHitResponseTypeDef",
    "ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef",
    "ClientListReviewableHitsResponseHITsTypeDef",
    "ClientListReviewableHitsResponseTypeDef",
    "ClientListWorkerBlocksResponseWorkerBlocksTypeDef",
    "ClientListWorkerBlocksResponseTypeDef",
    "ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef",
    "ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef",
    "ClientListWorkersWithQualificationTypeResponseTypeDef",
    "ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef",
    "ClientNotifyWorkersResponseTypeDef",
    "ClientSendTestEventNotificationNotificationTypeDef",
    "ClientUpdateNotificationSettingsNotificationTypeDef",
    "ClientUpdateQualificationTypeResponseQualificationTypeTypeDef",
    "ClientUpdateQualificationTypeResponseTypeDef",
    "ListAssignmentsForHITPaginatePaginationConfigTypeDef",
    "ListAssignmentsForHITPaginateResponseAssignmentsTypeDef",
    "ListAssignmentsForHITPaginateResponseTypeDef",
    "ListBonusPaymentsPaginatePaginationConfigTypeDef",
    "ListBonusPaymentsPaginateResponseBonusPaymentsTypeDef",
    "ListBonusPaymentsPaginateResponseTypeDef",
    "ListHITsForQualificationTypePaginatePaginationConfigTypeDef",
    "ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsTypeDef",
    "ListHITsForQualificationTypePaginateResponseHITsTypeDef",
    "ListHITsForQualificationTypePaginateResponseTypeDef",
    "ListHITsPaginatePaginationConfigTypeDef",
    "ListHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ListHITsPaginateResponseHITsQualificationRequirementsTypeDef",
    "ListHITsPaginateResponseHITsTypeDef",
    "ListHITsPaginateResponseTypeDef",
    "ListQualificationRequestsPaginatePaginationConfigTypeDef",
    "ListQualificationRequestsPaginateResponseQualificationRequestsTypeDef",
    "ListQualificationRequestsPaginateResponseTypeDef",
    "ListQualificationTypesPaginatePaginationConfigTypeDef",
    "ListQualificationTypesPaginateResponseQualificationTypesTypeDef",
    "ListQualificationTypesPaginateResponseTypeDef",
    "ListReviewableHITsPaginatePaginationConfigTypeDef",
    "ListReviewableHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ListReviewableHITsPaginateResponseHITsQualificationRequirementsTypeDef",
    "ListReviewableHITsPaginateResponseHITsTypeDef",
    "ListReviewableHITsPaginateResponseTypeDef",
    "ListWorkerBlocksPaginatePaginationConfigTypeDef",
    "ListWorkerBlocksPaginateResponseWorkerBlocksTypeDef",
    "ListWorkerBlocksPaginateResponseTypeDef",
    "ListWorkersWithQualificationTypePaginatePaginationConfigTypeDef",
    "ListWorkersWithQualificationTypePaginateResponseQualificationsLocaleValueTypeDef",
    "ListWorkersWithQualificationTypePaginateResponseQualificationsTypeDef",
    "ListWorkersWithQualificationTypePaginateResponseTypeDef",
)


_ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "_ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef(
    _ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef
):
    """
    Type definition for `ClientCreateHitAssignmentReviewPolicyParameters` `MapEntries`

    This data structure is the data type for the AnswerKey parameter of the
    ScoreMyKnownAnswers/2011-09-01 Review Policy.

    - **Key** *(string) --*

      The QuestionID from the HIT that is used to identify which question requires Mechanical
      Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

    - **Values** *(list) --*

      The list of answers to the question specified in the MapEntry Key element. The Worker
      must match all values in order for the answer to be scored correctly.

      - *(string) --*
    """


_ClientCreateHitAssignmentReviewPolicyParametersTypeDef = TypedDict(
    "_ClientCreateHitAssignmentReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[
            ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef
        ],
    },
    total=False,
)


class ClientCreateHitAssignmentReviewPolicyParametersTypeDef(
    _ClientCreateHitAssignmentReviewPolicyParametersTypeDef
):
    """
    Type definition for `ClientCreateHitAssignmentReviewPolicy` `Parameters`

    Name of the parameter from the Review policy.

    - **Key** *(string) --*

      Name of the parameter from the list of Review Polices.

    - **Values** *(list) --*

      The list of values of the Parameter

      - *(string) --*

    - **MapEntries** *(list) --*

      List of ParameterMapEntry objects.

      - *(dict) --*

        This data structure is the data type for the AnswerKey parameter of the
        ScoreMyKnownAnswers/2011-09-01 Review Policy.

        - **Key** *(string) --*

          The QuestionID from the HIT that is used to identify which question requires Mechanical
          Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

        - **Values** *(list) --*

          The list of answers to the question specified in the MapEntry Key element. The Worker
          must match all values in order for the answer to be scored correctly.

          - *(string) --*
    """


_RequiredClientCreateHitAssignmentReviewPolicyTypeDef = TypedDict(
    "_RequiredClientCreateHitAssignmentReviewPolicyTypeDef", {"PolicyName": str}
)
_OptionalClientCreateHitAssignmentReviewPolicyTypeDef = TypedDict(
    "_OptionalClientCreateHitAssignmentReviewPolicyTypeDef",
    {"Parameters": List[ClientCreateHitAssignmentReviewPolicyParametersTypeDef]},
    total=False,
)


class ClientCreateHitAssignmentReviewPolicyTypeDef(
    _RequiredClientCreateHitAssignmentReviewPolicyTypeDef,
    _OptionalClientCreateHitAssignmentReviewPolicyTypeDef,
):
    """
    Type definition for `ClientCreateHit` `AssignmentReviewPolicy`

    The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for
    Mechanical Turk to take various actions based on the policy.

    - **PolicyName** *(string) --* **[REQUIRED]**

      Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01

    - **Parameters** *(list) --*

      Name of the parameter from the Review policy.

      - *(dict) --*

        Name of the parameter from the Review policy.

        - **Key** *(string) --*

          Name of the parameter from the list of Review Polices.

        - **Values** *(list) --*

          The list of values of the Parameter

          - *(string) --*

        - **MapEntries** *(list) --*

          List of ParameterMapEntry objects.

          - *(dict) --*

            This data structure is the data type for the AnswerKey parameter of the
            ScoreMyKnownAnswers/2011-09-01 Review Policy.

            - **Key** *(string) --*

              The QuestionID from the HIT that is used to identify which question requires Mechanical
              Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

            - **Values** *(list) --*

              The list of answers to the question specified in the MapEntry Key element. The Worker
              must match all values in order for the answer to be scored correctly.

              - *(string) --*
    """


_ClientCreateHitHITLayoutParametersTypeDef = TypedDict(
    "_ClientCreateHitHITLayoutParametersTypeDef", {"Name": str, "Value": str}
)


class ClientCreateHitHITLayoutParametersTypeDef(
    _ClientCreateHitHITLayoutParametersTypeDef
):
    """
    Type definition for `ClientCreateHit` `HITLayoutParameters`

    The HITLayoutParameter data structure defines parameter values used with a HITLayout. A
    HITLayout is a reusable Amazon Mechanical Turk project template used to provide Human
    Intelligence Task (HIT) question data for CreateHIT.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the parameter in the HITLayout.

    - **Value** *(string) --* **[REQUIRED]**

      The value substituted for the parameter referenced in the HITLayout.
    """


_ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "_ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef(
    _ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef
):
    """
    Type definition for `ClientCreateHitHITReviewPolicyParameters` `MapEntries`

    This data structure is the data type for the AnswerKey parameter of the
    ScoreMyKnownAnswers/2011-09-01 Review Policy.

    - **Key** *(string) --*

      The QuestionID from the HIT that is used to identify which question requires Mechanical
      Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

    - **Values** *(list) --*

      The list of answers to the question specified in the MapEntry Key element. The Worker
      must match all values in order for the answer to be scored correctly.

      - *(string) --*
    """


_ClientCreateHitHITReviewPolicyParametersTypeDef = TypedDict(
    "_ClientCreateHitHITReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef],
    },
    total=False,
)


class ClientCreateHitHITReviewPolicyParametersTypeDef(
    _ClientCreateHitHITReviewPolicyParametersTypeDef
):
    """
    Type definition for `ClientCreateHitHITReviewPolicy` `Parameters`

    Name of the parameter from the Review policy.

    - **Key** *(string) --*

      Name of the parameter from the list of Review Polices.

    - **Values** *(list) --*

      The list of values of the Parameter

      - *(string) --*

    - **MapEntries** *(list) --*

      List of ParameterMapEntry objects.

      - *(dict) --*

        This data structure is the data type for the AnswerKey parameter of the
        ScoreMyKnownAnswers/2011-09-01 Review Policy.

        - **Key** *(string) --*

          The QuestionID from the HIT that is used to identify which question requires Mechanical
          Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

        - **Values** *(list) --*

          The list of answers to the question specified in the MapEntry Key element. The Worker
          must match all values in order for the answer to be scored correctly.

          - *(string) --*
    """


_RequiredClientCreateHitHITReviewPolicyTypeDef = TypedDict(
    "_RequiredClientCreateHitHITReviewPolicyTypeDef", {"PolicyName": str}
)
_OptionalClientCreateHitHITReviewPolicyTypeDef = TypedDict(
    "_OptionalClientCreateHitHITReviewPolicyTypeDef",
    {"Parameters": List[ClientCreateHitHITReviewPolicyParametersTypeDef]},
    total=False,
)


class ClientCreateHitHITReviewPolicyTypeDef(
    _RequiredClientCreateHitHITReviewPolicyTypeDef,
    _OptionalClientCreateHitHITReviewPolicyTypeDef,
):
    """
    Type definition for `ClientCreateHit` `HITReviewPolicy`

    The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take
    various actions based on the policy.

    - **PolicyName** *(string) --* **[REQUIRED]**

      Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01

    - **Parameters** *(list) --*

      Name of the parameter from the Review policy.

      - *(dict) --*

        Name of the parameter from the Review policy.

        - **Key** *(string) --*

          Name of the parameter from the list of Review Polices.

        - **Values** *(list) --*

          The list of values of the Parameter

          - *(string) --*

        - **MapEntries** *(list) --*

          List of ParameterMapEntry objects.

          - *(dict) --*

            This data structure is the data type for the AnswerKey parameter of the
            ScoreMyKnownAnswers/2011-09-01 Review Policy.

            - **Key** *(string) --*

              The QuestionID from the HIT that is used to identify which question requires Mechanical
              Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

            - **Values** *(list) --*

              The list of answers to the question specified in the MapEntry Key element. The Worker
              must match all values in order for the answer to be scored correctly.

              - *(string) --*
    """


_RequiredClientCreateHitQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_RequiredClientCreateHitQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str},
)
_OptionalClientCreateHitQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_OptionalClientCreateHitQualificationRequirementsLocaleValuesTypeDef",
    {"Subdivision": str},
    total=False,
)


class ClientCreateHitQualificationRequirementsLocaleValuesTypeDef(
    _RequiredClientCreateHitQualificationRequirementsLocaleValuesTypeDef,
    _OptionalClientCreateHitQualificationRequirementsLocaleValuesTypeDef,
):
    """
    Type definition for `ClientCreateHitQualificationRequirements` `LocaleValues`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --* **[REQUIRED]**

      The country of the locale. Must be a valid ISO 3166 country code. For example, the code
      US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example,
      the code WA refers to the state of Washington.
    """


_RequiredClientCreateHitQualificationRequirementsTypeDef = TypedDict(
    "_RequiredClientCreateHitQualificationRequirementsTypeDef",
    {"QualificationTypeId": str, "Comparator": str},
)
_OptionalClientCreateHitQualificationRequirementsTypeDef = TypedDict(
    "_OptionalClientCreateHitQualificationRequirementsTypeDef",
    {
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientCreateHitQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": str,
    },
    total=False,
)


class ClientCreateHitQualificationRequirementsTypeDef(
    _RequiredClientCreateHitQualificationRequirementsTypeDef,
    _OptionalClientCreateHitQualificationRequirementsTypeDef,
):
    """
    Type definition for `ClientCreateHit` `QualificationRequirements`

    The QualificationRequirement data structure describes a Qualification that a Worker must have
    before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker
    must have the Qualification in order to preview the HIT, or see the HIT in search results.

    - **QualificationTypeId** *(string) --* **[REQUIRED]**

      The ID of the Qualification type for the requirement.

    - **Comparator** *(string) --* **[REQUIRED]**

      The kind of comparison to make against a Qualification's value. You can compare a
      Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
      GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare
      it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to
      see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a
      Qualification requirement can also test if a Qualification Exists or DoesNotExist in the
      user's profile, regardless of its value.

    - **IntegerValues** *(list) --*

      The integer value to compare against the Qualification's value. IntegerValue must not be
      present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the
      Qualification type has an integer value; it cannot be used with the Worker_Locale
      QualificationType ID. When performing a set comparison by using the In or the NotIn
      comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data
      structure.

      - *(integer) --*

    - **LocaleValues** *(list) --*

      The locale value to compare against the Qualification's value. The local value must be a
      valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used
      with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo,
      NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when
      using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In
      or the NotIn comparator, you can use up to 30 LocaleValue elements in a
      QualificationRequirement data structure.

      - *(dict) --*

        The Locale data structure represents a geographical region or location.

        - **Country** *(string) --* **[REQUIRED]**

          The country of the locale. Must be a valid ISO 3166 country code. For example, the code
          US refers to the United States of America.

        - **Subdivision** *(string) --*

          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example,
          the code WA refers to the state of Washington.

    - **RequiredToPreview** *(boolean) --*

      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
      question data for the HIT will not be shown when a Worker whose Qualifications do not meet
      this requirement tries to preview the HIT. That is, a Worker's Qualifications must meet all
      of the requirements for which RequiredToPreview is true in order to preview the HIT. If a
      Worker meets all of the requirements where RequiredToPreview is true (or if there are no such
      requirements), but does not meet all of the requirements for the HIT, the Worker will be
      allowed to preview the HIT's question data, but will not be allowed to accept and complete
      the HIT. The default is false. This should not be used in combination with the
      ``ActionsGuarded`` field.

    - **ActionsGuarded** *(string) --*

      Setting this attribute prevents Workers whose Qualifications do not meet this
      QualificationRequirement from taking the specified action. Valid arguments include "Accept"
      (Worker cannot accept the HIT, but can preview the HIT and see it in their search results),
      "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can see the HIT in their
      search results), and "DiscoverPreviewAndAccept" (Worker cannot accept, preview, or see the
      HIT in their search results). It's possible for you to create a HIT with multiple
      QualificationRequirements (which can have different values for the ActionGuarded attribute).
      In this case, the Worker is only permitted to perform an action when they have met all
      QualificationRequirements guarding the action. The actions in the order of least restrictive
      to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all
      QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all
      requirements that are set with PreviewAndAccept, then the Worker will be able to Discover,
      i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT.
      ActionsGuarded should not be used in combination with the ``RequiredToPreview`` field.
    """


_ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef(
    _ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef
):
    """
    Type definition for `ClientCreateHitResponseHITQualificationRequirements` `LocaleValues`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --*

      The country of the locale. Must be a valid ISO 3166 country code. For example, the
      code US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
      example, the code WA refers to the state of Washington.
    """


_ClientCreateHitResponseHITQualificationRequirementsTypeDef = TypedDict(
    "_ClientCreateHitResponseHITQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": str,
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": str,
    },
    total=False,
)


class ClientCreateHitResponseHITQualificationRequirementsTypeDef(
    _ClientCreateHitResponseHITQualificationRequirementsTypeDef
):
    """
    Type definition for `ClientCreateHitResponseHIT` `QualificationRequirements`

    The QualificationRequirement data structure describes a Qualification that a Worker must
    have before the Worker is allowed to accept a HIT. A requirement may optionally state
    that a Worker must have the Qualification in order to preview the HIT, or see the HIT in
    search results.

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type for the requirement.

    - **Comparator** *(string) --*

      The kind of comparison to make against a Qualification's value. You can compare a
      Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
      GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
      compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You
      can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
      values. Lastly, a Qualification requirement can also test if a Qualification Exists or
      DoesNotExist in the user's profile, regardless of its value.

    - **IntegerValues** *(list) --*

      The integer value to compare against the Qualification's value. IntegerValue must not
      be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
      the Qualification type has an integer value; it cannot be used with the Worker_Locale
      QualificationType ID. When performing a set comparison by using the In or the NotIn
      comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
      data structure.

      - *(integer) --*

    - **LocaleValues** *(list) --*

      The locale value to compare against the Qualification's value. The local value must be
      a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only
      be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with
      the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
      LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a
      set comparison by using the In or the NotIn comparator, you can use up to 30
      LocaleValue elements in a QualificationRequirement data structure.

      - *(dict) --*

        The Locale data structure represents a geographical region or location.

        - **Country** *(string) --*

          The country of the locale. Must be a valid ISO 3166 country code. For example, the
          code US refers to the United States of America.

        - **Subdivision** *(string) --*

          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
          example, the code WA refers to the state of Washington.

    - **RequiredToPreview** *(boolean) --*

      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
      question data for the HIT will not be shown when a Worker whose Qualifications do not
      meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must
      meet all of the requirements for which RequiredToPreview is true in order to preview
      the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or
      if there are no such requirements), but does not meet all of the requirements for the
      HIT, the Worker will be allowed to preview the HIT's question data, but will not be
      allowed to accept and complete the HIT. The default is false. This should not be used
      in combination with the ``ActionsGuarded`` field.

    - **ActionsGuarded** *(string) --*

      Setting this attribute prevents Workers whose Qualifications do not meet this
      QualificationRequirement from taking the specified action. Valid arguments include
      "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
      search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
      see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
      accept, preview, or see the HIT in their search results). It's possible for you to
      create a HIT with multiple QualificationRequirements (which can have different values
      for the ActionGuarded attribute). In this case, the Worker is only permitted to perform
      an action when they have met all QualificationRequirements guarding the action. The
      actions in the order of least restrictive to most restrictive are Discover, Preview and
      Accept. For example, if a Worker meets all QualificationRequirements that are set to
      DiscoverPreviewAndAccept, but do not meet all requirements that are set with
      PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their
      search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should
      not be used in combination with the ``RequiredToPreview`` field.
    """


_ClientCreateHitResponseHITTypeDef = TypedDict(
    "_ClientCreateHitResponseHITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": str,
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientCreateHitResponseHITQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": str,
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientCreateHitResponseHITTypeDef(_ClientCreateHitResponseHITTypeDef):
    """
    Type definition for `ClientCreateHitResponse` `HIT`

    Contains the newly created HIT data. For a description of the HIT data structure as it
    appears in responses, see the HIT Data Structure documentation.

    - **HITId** *(string) --*

      A unique identifier for the HIT.

    - **HITTypeId** *(string) --*

      The ID of the HIT type of this HIT

    - **HITGroupId** *(string) --*

      The ID of the HIT Group of this HIT.

    - **HITLayoutId** *(string) --*

      The ID of the HIT Layout of this HIT.

    - **CreationTime** *(datetime) --*

      The date and time the HIT was created.

    - **Title** *(string) --*

      The title of the HIT.

    - **Description** *(string) --*

      A general description of the HIT.

    - **Question** *(string) --*

      The data the Worker completing the HIT uses produce the results. This is either either a
      QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

    - **Keywords** *(string) --*

      One or more words or phrases that describe the HIT, separated by commas. Search terms
      similar to the keywords of a HIT are more likely to have the HIT in the search results.

    - **HITStatus** *(string) --*

      The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
      Reviewable | Reviewing | Disposed.

    - **MaxAssignments** *(integer) --*

      The number of times the HIT can be accepted and completed before the HIT becomes
      unavailable.

    - **Reward** *(string) --*

      A string representing a currency amount.

    - **AutoApprovalDelayInSeconds** *(integer) --*

      The amount of time, in seconds, after the Worker submits an assignment for the HIT that the
      results are automatically approved by Amazon Mechanical Turk. This is the amount of time
      the Requester has to reject an assignment submitted by a Worker before the assignment is
      auto-approved and the Worker is paid.

    - **Expiration** *(datetime) --*

      The date and time the HIT expires.

    - **AssignmentDurationInSeconds** *(integer) --*

      The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

    - **RequesterAnnotation** *(string) --*

      An arbitrary data field the Requester who created the HIT can use. This field is visible
      only to the creator of the HIT.

    - **QualificationRequirements** *(list) --*

      Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
      have between zero and ten Qualification requirements. All requirements must be met in order
      for a Worker to accept the HIT. Additionally, other actions can be restricted using the
      ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

      - *(dict) --*

        The QualificationRequirement data structure describes a Qualification that a Worker must
        have before the Worker is allowed to accept a HIT. A requirement may optionally state
        that a Worker must have the Qualification in order to preview the HIT, or see the HIT in
        search results.

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type for the requirement.

        - **Comparator** *(string) --*

          The kind of comparison to make against a Qualification's value. You can compare a
          Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
          GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
          compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You
          can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
          values. Lastly, a Qualification requirement can also test if a Qualification Exists or
          DoesNotExist in the user's profile, regardless of its value.

        - **IntegerValues** *(list) --*

          The integer value to compare against the Qualification's value. IntegerValue must not
          be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
          the Qualification type has an integer value; it cannot be used with the Worker_Locale
          QualificationType ID. When performing a set comparison by using the In or the NotIn
          comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
          data structure.

          - *(integer) --*

        - **LocaleValues** *(list) --*

          The locale value to compare against the Qualification's value. The local value must be
          a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only
          be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with
          the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
          LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a
          set comparison by using the In or the NotIn comparator, you can use up to 30
          LocaleValue elements in a QualificationRequirement data structure.

          - *(dict) --*

            The Locale data structure represents a geographical region or location.

            - **Country** *(string) --*

              The country of the locale. Must be a valid ISO 3166 country code. For example, the
              code US refers to the United States of America.

            - **Subdivision** *(string) --*

              The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
              example, the code WA refers to the state of Washington.

        - **RequiredToPreview** *(boolean) --*

          DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
          question data for the HIT will not be shown when a Worker whose Qualifications do not
          meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must
          meet all of the requirements for which RequiredToPreview is true in order to preview
          the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or
          if there are no such requirements), but does not meet all of the requirements for the
          HIT, the Worker will be allowed to preview the HIT's question data, but will not be
          allowed to accept and complete the HIT. The default is false. This should not be used
          in combination with the ``ActionsGuarded`` field.

        - **ActionsGuarded** *(string) --*

          Setting this attribute prevents Workers whose Qualifications do not meet this
          QualificationRequirement from taking the specified action. Valid arguments include
          "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
          search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
          see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
          accept, preview, or see the HIT in their search results). It's possible for you to
          create a HIT with multiple QualificationRequirements (which can have different values
          for the ActionGuarded attribute). In this case, the Worker is only permitted to perform
          an action when they have met all QualificationRequirements guarding the action. The
          actions in the order of least restrictive to most restrictive are Discover, Preview and
          Accept. For example, if a Worker meets all QualificationRequirements that are set to
          DiscoverPreviewAndAccept, but do not meet all requirements that are set with
          PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their
          search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should
          not be used in combination with the ``RequiredToPreview`` field.

    - **HITReviewStatus** *(string) --*

      Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
      ReviewedAppropriate | ReviewedInappropriate.

    - **NumberOfAssignmentsPending** *(integer) --*

      The number of assignments for this HIT that are being previewed or have been accepted by
      Workers, but have not yet been submitted, returned, or abandoned.

    - **NumberOfAssignmentsAvailable** *(integer) --*

      The number of assignments for this HIT that are available for Workers to accept.

    - **NumberOfAssignmentsCompleted** *(integer) --*

      The number of assignments for this HIT that have been approved or rejected.
    """


_ClientCreateHitResponseTypeDef = TypedDict(
    "_ClientCreateHitResponseTypeDef",
    {"HIT": ClientCreateHitResponseHITTypeDef},
    total=False,
)


class ClientCreateHitResponseTypeDef(_ClientCreateHitResponseTypeDef):
    """
    Type definition for `ClientCreateHit` `Response`

    - **HIT** *(dict) --*

      Contains the newly created HIT data. For a description of the HIT data structure as it
      appears in responses, see the HIT Data Structure documentation.

      - **HITId** *(string) --*

        A unique identifier for the HIT.

      - **HITTypeId** *(string) --*

        The ID of the HIT type of this HIT

      - **HITGroupId** *(string) --*

        The ID of the HIT Group of this HIT.

      - **HITLayoutId** *(string) --*

        The ID of the HIT Layout of this HIT.

      - **CreationTime** *(datetime) --*

        The date and time the HIT was created.

      - **Title** *(string) --*

        The title of the HIT.

      - **Description** *(string) --*

        A general description of the HIT.

      - **Question** *(string) --*

        The data the Worker completing the HIT uses produce the results. This is either either a
        QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

      - **Keywords** *(string) --*

        One or more words or phrases that describe the HIT, separated by commas. Search terms
        similar to the keywords of a HIT are more likely to have the HIT in the search results.

      - **HITStatus** *(string) --*

        The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
        Reviewable | Reviewing | Disposed.

      - **MaxAssignments** *(integer) --*

        The number of times the HIT can be accepted and completed before the HIT becomes
        unavailable.

      - **Reward** *(string) --*

        A string representing a currency amount.

      - **AutoApprovalDelayInSeconds** *(integer) --*

        The amount of time, in seconds, after the Worker submits an assignment for the HIT that the
        results are automatically approved by Amazon Mechanical Turk. This is the amount of time
        the Requester has to reject an assignment submitted by a Worker before the assignment is
        auto-approved and the Worker is paid.

      - **Expiration** *(datetime) --*

        The date and time the HIT expires.

      - **AssignmentDurationInSeconds** *(integer) --*

        The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

      - **RequesterAnnotation** *(string) --*

        An arbitrary data field the Requester who created the HIT can use. This field is visible
        only to the creator of the HIT.

      - **QualificationRequirements** *(list) --*

        Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
        have between zero and ten Qualification requirements. All requirements must be met in order
        for a Worker to accept the HIT. Additionally, other actions can be restricted using the
        ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

        - *(dict) --*

          The QualificationRequirement data structure describes a Qualification that a Worker must
          have before the Worker is allowed to accept a HIT. A requirement may optionally state
          that a Worker must have the Qualification in order to preview the HIT, or see the HIT in
          search results.

          - **QualificationTypeId** *(string) --*

            The ID of the Qualification type for the requirement.

          - **Comparator** *(string) --*

            The kind of comparison to make against a Qualification's value. You can compare a
            Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
            GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
            compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You
            can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
            values. Lastly, a Qualification requirement can also test if a Qualification Exists or
            DoesNotExist in the user's profile, regardless of its value.

          - **IntegerValues** *(list) --*

            The integer value to compare against the Qualification's value. IntegerValue must not
            be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
            the Qualification type has an integer value; it cannot be used with the Worker_Locale
            QualificationType ID. When performing a set comparison by using the In or the NotIn
            comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
            data structure.

            - *(integer) --*

          - **LocaleValues** *(list) --*

            The locale value to compare against the Qualification's value. The local value must be
            a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only
            be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with
            the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
            LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a
            set comparison by using the In or the NotIn comparator, you can use up to 30
            LocaleValue elements in a QualificationRequirement data structure.

            - *(dict) --*

              The Locale data structure represents a geographical region or location.

              - **Country** *(string) --*

                The country of the locale. Must be a valid ISO 3166 country code. For example, the
                code US refers to the United States of America.

              - **Subdivision** *(string) --*

                The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
                example, the code WA refers to the state of Washington.

          - **RequiredToPreview** *(boolean) --*

            DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
            question data for the HIT will not be shown when a Worker whose Qualifications do not
            meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must
            meet all of the requirements for which RequiredToPreview is true in order to preview
            the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or
            if there are no such requirements), but does not meet all of the requirements for the
            HIT, the Worker will be allowed to preview the HIT's question data, but will not be
            allowed to accept and complete the HIT. The default is false. This should not be used
            in combination with the ``ActionsGuarded`` field.

          - **ActionsGuarded** *(string) --*

            Setting this attribute prevents Workers whose Qualifications do not meet this
            QualificationRequirement from taking the specified action. Valid arguments include
            "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
            search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
            see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
            accept, preview, or see the HIT in their search results). It's possible for you to
            create a HIT with multiple QualificationRequirements (which can have different values
            for the ActionGuarded attribute). In this case, the Worker is only permitted to perform
            an action when they have met all QualificationRequirements guarding the action. The
            actions in the order of least restrictive to most restrictive are Discover, Preview and
            Accept. For example, if a Worker meets all QualificationRequirements that are set to
            DiscoverPreviewAndAccept, but do not meet all requirements that are set with
            PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their
            search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should
            not be used in combination with the ``RequiredToPreview`` field.

      - **HITReviewStatus** *(string) --*

        Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
        ReviewedAppropriate | ReviewedInappropriate.

      - **NumberOfAssignmentsPending** *(integer) --*

        The number of assignments for this HIT that are being previewed or have been accepted by
        Workers, but have not yet been submitted, returned, or abandoned.

      - **NumberOfAssignmentsAvailable** *(integer) --*

        The number of assignments for this HIT that are available for Workers to accept.

      - **NumberOfAssignmentsCompleted** *(integer) --*

        The number of assignments for this HIT that have been approved or rejected.
    """


_RequiredClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_RequiredClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str},
)
_OptionalClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_OptionalClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef",
    {"Subdivision": str},
    total=False,
)


class ClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef(
    _RequiredClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef,
    _OptionalClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef,
):
    """
    Type definition for `ClientCreateHitTypeQualificationRequirements` `LocaleValues`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --* **[REQUIRED]**

      The country of the locale. Must be a valid ISO 3166 country code. For example, the code
      US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example,
      the code WA refers to the state of Washington.
    """


_RequiredClientCreateHitTypeQualificationRequirementsTypeDef = TypedDict(
    "_RequiredClientCreateHitTypeQualificationRequirementsTypeDef",
    {"QualificationTypeId": str, "Comparator": str},
)
_OptionalClientCreateHitTypeQualificationRequirementsTypeDef = TypedDict(
    "_OptionalClientCreateHitTypeQualificationRequirementsTypeDef",
    {
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": str,
    },
    total=False,
)


class ClientCreateHitTypeQualificationRequirementsTypeDef(
    _RequiredClientCreateHitTypeQualificationRequirementsTypeDef,
    _OptionalClientCreateHitTypeQualificationRequirementsTypeDef,
):
    """
    Type definition for `ClientCreateHitType` `QualificationRequirements`

    The QualificationRequirement data structure describes a Qualification that a Worker must have
    before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker
    must have the Qualification in order to preview the HIT, or see the HIT in search results.

    - **QualificationTypeId** *(string) --* **[REQUIRED]**

      The ID of the Qualification type for the requirement.

    - **Comparator** *(string) --* **[REQUIRED]**

      The kind of comparison to make against a Qualification's value. You can compare a
      Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
      GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare
      it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to
      see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a
      Qualification requirement can also test if a Qualification Exists or DoesNotExist in the
      user's profile, regardless of its value.

    - **IntegerValues** *(list) --*

      The integer value to compare against the Qualification's value. IntegerValue must not be
      present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the
      Qualification type has an integer value; it cannot be used with the Worker_Locale
      QualificationType ID. When performing a set comparison by using the In or the NotIn
      comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data
      structure.

      - *(integer) --*

    - **LocaleValues** *(list) --*

      The locale value to compare against the Qualification's value. The local value must be a
      valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used
      with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo,
      NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when
      using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In
      or the NotIn comparator, you can use up to 30 LocaleValue elements in a
      QualificationRequirement data structure.

      - *(dict) --*

        The Locale data structure represents a geographical region or location.

        - **Country** *(string) --* **[REQUIRED]**

          The country of the locale. Must be a valid ISO 3166 country code. For example, the code
          US refers to the United States of America.

        - **Subdivision** *(string) --*

          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example,
          the code WA refers to the state of Washington.

    - **RequiredToPreview** *(boolean) --*

      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
      question data for the HIT will not be shown when a Worker whose Qualifications do not meet
      this requirement tries to preview the HIT. That is, a Worker's Qualifications must meet all
      of the requirements for which RequiredToPreview is true in order to preview the HIT. If a
      Worker meets all of the requirements where RequiredToPreview is true (or if there are no such
      requirements), but does not meet all of the requirements for the HIT, the Worker will be
      allowed to preview the HIT's question data, but will not be allowed to accept and complete
      the HIT. The default is false. This should not be used in combination with the
      ``ActionsGuarded`` field.

    - **ActionsGuarded** *(string) --*

      Setting this attribute prevents Workers whose Qualifications do not meet this
      QualificationRequirement from taking the specified action. Valid arguments include "Accept"
      (Worker cannot accept the HIT, but can preview the HIT and see it in their search results),
      "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can see the HIT in their
      search results), and "DiscoverPreviewAndAccept" (Worker cannot accept, preview, or see the
      HIT in their search results). It's possible for you to create a HIT with multiple
      QualificationRequirements (which can have different values for the ActionGuarded attribute).
      In this case, the Worker is only permitted to perform an action when they have met all
      QualificationRequirements guarding the action. The actions in the order of least restrictive
      to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all
      QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all
      requirements that are set with PreviewAndAccept, then the Worker will be able to Discover,
      i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT.
      ActionsGuarded should not be used in combination with the ``RequiredToPreview`` field.
    """


_ClientCreateHitTypeResponseTypeDef = TypedDict(
    "_ClientCreateHitTypeResponseTypeDef", {"HITTypeId": str}, total=False
)


class ClientCreateHitTypeResponseTypeDef(_ClientCreateHitTypeResponseTypeDef):
    """
    Type definition for `ClientCreateHitType` `Response`

    - **HITTypeId** *(string) --*

      The ID of the newly registered HIT type.
    """


_ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef(
    _ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef
):
    """
    Type definition for `ClientCreateHitWithHitTypeAssignmentReviewPolicyParameters` `MapEntries`

    This data structure is the data type for the AnswerKey parameter of the
    ScoreMyKnownAnswers/2011-09-01 Review Policy.

    - **Key** *(string) --*

      The QuestionID from the HIT that is used to identify which question requires Mechanical
      Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

    - **Values** *(list) --*

      The list of answers to the question specified in the MapEntry Key element. The Worker
      must match all values in order for the answer to be scored correctly.

      - *(string) --*
    """


_ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[
            ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef
        ],
    },
    total=False,
)


class ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef(
    _ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef
):
    """
    Type definition for `ClientCreateHitWithHitTypeAssignmentReviewPolicy` `Parameters`

    Name of the parameter from the Review policy.

    - **Key** *(string) --*

      Name of the parameter from the list of Review Polices.

    - **Values** *(list) --*

      The list of values of the Parameter

      - *(string) --*

    - **MapEntries** *(list) --*

      List of ParameterMapEntry objects.

      - *(dict) --*

        This data structure is the data type for the AnswerKey parameter of the
        ScoreMyKnownAnswers/2011-09-01 Review Policy.

        - **Key** *(string) --*

          The QuestionID from the HIT that is used to identify which question requires Mechanical
          Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

        - **Values** *(list) --*

          The list of answers to the question specified in the MapEntry Key element. The Worker
          must match all values in order for the answer to be scored correctly.

          - *(string) --*
    """


_RequiredClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef = TypedDict(
    "_RequiredClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef",
    {"PolicyName": str},
)
_OptionalClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef = TypedDict(
    "_OptionalClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef",
    {
        "Parameters": List[
            ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef
        ]
    },
    total=False,
)


class ClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef(
    _RequiredClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef,
    _OptionalClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef,
):
    """
    Type definition for `ClientCreateHitWithHitType` `AssignmentReviewPolicy`

    The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for
    Mechanical Turk to take various actions based on the policy.

    - **PolicyName** *(string) --* **[REQUIRED]**

      Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01

    - **Parameters** *(list) --*

      Name of the parameter from the Review policy.

      - *(dict) --*

        Name of the parameter from the Review policy.

        - **Key** *(string) --*

          Name of the parameter from the list of Review Polices.

        - **Values** *(list) --*

          The list of values of the Parameter

          - *(string) --*

        - **MapEntries** *(list) --*

          List of ParameterMapEntry objects.

          - *(dict) --*

            This data structure is the data type for the AnswerKey parameter of the
            ScoreMyKnownAnswers/2011-09-01 Review Policy.

            - **Key** *(string) --*

              The QuestionID from the HIT that is used to identify which question requires Mechanical
              Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

            - **Values** *(list) --*

              The list of answers to the question specified in the MapEntry Key element. The Worker
              must match all values in order for the answer to be scored correctly.

              - *(string) --*
    """


_ClientCreateHitWithHitTypeHITLayoutParametersTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeHITLayoutParametersTypeDef", {"Name": str, "Value": str}
)


class ClientCreateHitWithHitTypeHITLayoutParametersTypeDef(
    _ClientCreateHitWithHitTypeHITLayoutParametersTypeDef
):
    """
    Type definition for `ClientCreateHitWithHitType` `HITLayoutParameters`

    The HITLayoutParameter data structure defines parameter values used with a HITLayout. A
    HITLayout is a reusable Amazon Mechanical Turk project template used to provide Human
    Intelligence Task (HIT) question data for CreateHIT.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the parameter in the HITLayout.

    - **Value** *(string) --* **[REQUIRED]**

      The value substituted for the parameter referenced in the HITLayout.
    """


_ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef(
    _ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef
):
    """
    Type definition for `ClientCreateHitWithHitTypeHITReviewPolicyParameters` `MapEntries`

    This data structure is the data type for the AnswerKey parameter of the
    ScoreMyKnownAnswers/2011-09-01 Review Policy.

    - **Key** *(string) --*

      The QuestionID from the HIT that is used to identify which question requires Mechanical
      Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

    - **Values** *(list) --*

      The list of answers to the question specified in the MapEntry Key element. The Worker
      must match all values in order for the answer to be scored correctly.

      - *(string) --*
    """


_ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[
            ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef
        ],
    },
    total=False,
)


class ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef(
    _ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef
):
    """
    Type definition for `ClientCreateHitWithHitTypeHITReviewPolicy` `Parameters`

    Name of the parameter from the Review policy.

    - **Key** *(string) --*

      Name of the parameter from the list of Review Polices.

    - **Values** *(list) --*

      The list of values of the Parameter

      - *(string) --*

    - **MapEntries** *(list) --*

      List of ParameterMapEntry objects.

      - *(dict) --*

        This data structure is the data type for the AnswerKey parameter of the
        ScoreMyKnownAnswers/2011-09-01 Review Policy.

        - **Key** *(string) --*

          The QuestionID from the HIT that is used to identify which question requires Mechanical
          Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

        - **Values** *(list) --*

          The list of answers to the question specified in the MapEntry Key element. The Worker
          must match all values in order for the answer to be scored correctly.

          - *(string) --*
    """


_RequiredClientCreateHitWithHitTypeHITReviewPolicyTypeDef = TypedDict(
    "_RequiredClientCreateHitWithHitTypeHITReviewPolicyTypeDef", {"PolicyName": str}
)
_OptionalClientCreateHitWithHitTypeHITReviewPolicyTypeDef = TypedDict(
    "_OptionalClientCreateHitWithHitTypeHITReviewPolicyTypeDef",
    {"Parameters": List[ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef]},
    total=False,
)


class ClientCreateHitWithHitTypeHITReviewPolicyTypeDef(
    _RequiredClientCreateHitWithHitTypeHITReviewPolicyTypeDef,
    _OptionalClientCreateHitWithHitTypeHITReviewPolicyTypeDef,
):
    """
    Type definition for `ClientCreateHitWithHitType` `HITReviewPolicy`

    The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take
    various actions based on the policy.

    - **PolicyName** *(string) --* **[REQUIRED]**

      Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01

    - **Parameters** *(list) --*

      Name of the parameter from the Review policy.

      - *(dict) --*

        Name of the parameter from the Review policy.

        - **Key** *(string) --*

          Name of the parameter from the list of Review Polices.

        - **Values** *(list) --*

          The list of values of the Parameter

          - *(string) --*

        - **MapEntries** *(list) --*

          List of ParameterMapEntry objects.

          - *(dict) --*

            This data structure is the data type for the AnswerKey parameter of the
            ScoreMyKnownAnswers/2011-09-01 Review Policy.

            - **Key** *(string) --*

              The QuestionID from the HIT that is used to identify which question requires Mechanical
              Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

            - **Values** *(list) --*

              The list of answers to the question specified in the MapEntry Key element. The Worker
              must match all values in order for the answer to be scored correctly.

              - *(string) --*
    """


_ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef(
    _ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef
):
    """
    Type definition for `ClientCreateHitWithHitTypeResponseHITQualificationRequirements` `LocaleValues`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --*

      The country of the locale. Must be a valid ISO 3166 country code. For example, the
      code US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
      example, the code WA refers to the state of Washington.
    """


_ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": str,
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": str,
    },
    total=False,
)


class ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef(
    _ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef
):
    """
    Type definition for `ClientCreateHitWithHitTypeResponseHIT` `QualificationRequirements`

    The QualificationRequirement data structure describes a Qualification that a Worker must
    have before the Worker is allowed to accept a HIT. A requirement may optionally state
    that a Worker must have the Qualification in order to preview the HIT, or see the HIT in
    search results.

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type for the requirement.

    - **Comparator** *(string) --*

      The kind of comparison to make against a Qualification's value. You can compare a
      Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
      GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
      compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You
      can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
      values. Lastly, a Qualification requirement can also test if a Qualification Exists or
      DoesNotExist in the user's profile, regardless of its value.

    - **IntegerValues** *(list) --*

      The integer value to compare against the Qualification's value. IntegerValue must not
      be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
      the Qualification type has an integer value; it cannot be used with the Worker_Locale
      QualificationType ID. When performing a set comparison by using the In or the NotIn
      comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
      data structure.

      - *(integer) --*

    - **LocaleValues** *(list) --*

      The locale value to compare against the Qualification's value. The local value must be
      a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only
      be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with
      the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
      LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a
      set comparison by using the In or the NotIn comparator, you can use up to 30
      LocaleValue elements in a QualificationRequirement data structure.

      - *(dict) --*

        The Locale data structure represents a geographical region or location.

        - **Country** *(string) --*

          The country of the locale. Must be a valid ISO 3166 country code. For example, the
          code US refers to the United States of America.

        - **Subdivision** *(string) --*

          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
          example, the code WA refers to the state of Washington.

    - **RequiredToPreview** *(boolean) --*

      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
      question data for the HIT will not be shown when a Worker whose Qualifications do not
      meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must
      meet all of the requirements for which RequiredToPreview is true in order to preview
      the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or
      if there are no such requirements), but does not meet all of the requirements for the
      HIT, the Worker will be allowed to preview the HIT's question data, but will not be
      allowed to accept and complete the HIT. The default is false. This should not be used
      in combination with the ``ActionsGuarded`` field.

    - **ActionsGuarded** *(string) --*

      Setting this attribute prevents Workers whose Qualifications do not meet this
      QualificationRequirement from taking the specified action. Valid arguments include
      "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
      search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
      see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
      accept, preview, or see the HIT in their search results). It's possible for you to
      create a HIT with multiple QualificationRequirements (which can have different values
      for the ActionGuarded attribute). In this case, the Worker is only permitted to perform
      an action when they have met all QualificationRequirements guarding the action. The
      actions in the order of least restrictive to most restrictive are Discover, Preview and
      Accept. For example, if a Worker meets all QualificationRequirements that are set to
      DiscoverPreviewAndAccept, but do not meet all requirements that are set with
      PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their
      search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should
      not be used in combination with the ``RequiredToPreview`` field.
    """


_ClientCreateHitWithHitTypeResponseHITTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeResponseHITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": str,
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": str,
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientCreateHitWithHitTypeResponseHITTypeDef(
    _ClientCreateHitWithHitTypeResponseHITTypeDef
):
    """
    Type definition for `ClientCreateHitWithHitTypeResponse` `HIT`

    Contains the newly created HIT data. For a description of the HIT data structure as it
    appears in responses, see the HIT Data Structure documentation.

    - **HITId** *(string) --*

      A unique identifier for the HIT.

    - **HITTypeId** *(string) --*

      The ID of the HIT type of this HIT

    - **HITGroupId** *(string) --*

      The ID of the HIT Group of this HIT.

    - **HITLayoutId** *(string) --*

      The ID of the HIT Layout of this HIT.

    - **CreationTime** *(datetime) --*

      The date and time the HIT was created.

    - **Title** *(string) --*

      The title of the HIT.

    - **Description** *(string) --*

      A general description of the HIT.

    - **Question** *(string) --*

      The data the Worker completing the HIT uses produce the results. This is either either a
      QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

    - **Keywords** *(string) --*

      One or more words or phrases that describe the HIT, separated by commas. Search terms
      similar to the keywords of a HIT are more likely to have the HIT in the search results.

    - **HITStatus** *(string) --*

      The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
      Reviewable | Reviewing | Disposed.

    - **MaxAssignments** *(integer) --*

      The number of times the HIT can be accepted and completed before the HIT becomes
      unavailable.

    - **Reward** *(string) --*

      A string representing a currency amount.

    - **AutoApprovalDelayInSeconds** *(integer) --*

      The amount of time, in seconds, after the Worker submits an assignment for the HIT that the
      results are automatically approved by Amazon Mechanical Turk. This is the amount of time
      the Requester has to reject an assignment submitted by a Worker before the assignment is
      auto-approved and the Worker is paid.

    - **Expiration** *(datetime) --*

      The date and time the HIT expires.

    - **AssignmentDurationInSeconds** *(integer) --*

      The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

    - **RequesterAnnotation** *(string) --*

      An arbitrary data field the Requester who created the HIT can use. This field is visible
      only to the creator of the HIT.

    - **QualificationRequirements** *(list) --*

      Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
      have between zero and ten Qualification requirements. All requirements must be met in order
      for a Worker to accept the HIT. Additionally, other actions can be restricted using the
      ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

      - *(dict) --*

        The QualificationRequirement data structure describes a Qualification that a Worker must
        have before the Worker is allowed to accept a HIT. A requirement may optionally state
        that a Worker must have the Qualification in order to preview the HIT, or see the HIT in
        search results.

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type for the requirement.

        - **Comparator** *(string) --*

          The kind of comparison to make against a Qualification's value. You can compare a
          Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
          GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
          compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You
          can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
          values. Lastly, a Qualification requirement can also test if a Qualification Exists or
          DoesNotExist in the user's profile, regardless of its value.

        - **IntegerValues** *(list) --*

          The integer value to compare against the Qualification's value. IntegerValue must not
          be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
          the Qualification type has an integer value; it cannot be used with the Worker_Locale
          QualificationType ID. When performing a set comparison by using the In or the NotIn
          comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
          data structure.

          - *(integer) --*

        - **LocaleValues** *(list) --*

          The locale value to compare against the Qualification's value. The local value must be
          a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only
          be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with
          the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
          LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a
          set comparison by using the In or the NotIn comparator, you can use up to 30
          LocaleValue elements in a QualificationRequirement data structure.

          - *(dict) --*

            The Locale data structure represents a geographical region or location.

            - **Country** *(string) --*

              The country of the locale. Must be a valid ISO 3166 country code. For example, the
              code US refers to the United States of America.

            - **Subdivision** *(string) --*

              The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
              example, the code WA refers to the state of Washington.

        - **RequiredToPreview** *(boolean) --*

          DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
          question data for the HIT will not be shown when a Worker whose Qualifications do not
          meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must
          meet all of the requirements for which RequiredToPreview is true in order to preview
          the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or
          if there are no such requirements), but does not meet all of the requirements for the
          HIT, the Worker will be allowed to preview the HIT's question data, but will not be
          allowed to accept and complete the HIT. The default is false. This should not be used
          in combination with the ``ActionsGuarded`` field.

        - **ActionsGuarded** *(string) --*

          Setting this attribute prevents Workers whose Qualifications do not meet this
          QualificationRequirement from taking the specified action. Valid arguments include
          "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
          search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
          see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
          accept, preview, or see the HIT in their search results). It's possible for you to
          create a HIT with multiple QualificationRequirements (which can have different values
          for the ActionGuarded attribute). In this case, the Worker is only permitted to perform
          an action when they have met all QualificationRequirements guarding the action. The
          actions in the order of least restrictive to most restrictive are Discover, Preview and
          Accept. For example, if a Worker meets all QualificationRequirements that are set to
          DiscoverPreviewAndAccept, but do not meet all requirements that are set with
          PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their
          search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should
          not be used in combination with the ``RequiredToPreview`` field.

    - **HITReviewStatus** *(string) --*

      Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
      ReviewedAppropriate | ReviewedInappropriate.

    - **NumberOfAssignmentsPending** *(integer) --*

      The number of assignments for this HIT that are being previewed or have been accepted by
      Workers, but have not yet been submitted, returned, or abandoned.

    - **NumberOfAssignmentsAvailable** *(integer) --*

      The number of assignments for this HIT that are available for Workers to accept.

    - **NumberOfAssignmentsCompleted** *(integer) --*

      The number of assignments for this HIT that have been approved or rejected.
    """


_ClientCreateHitWithHitTypeResponseTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeResponseTypeDef",
    {"HIT": ClientCreateHitWithHitTypeResponseHITTypeDef},
    total=False,
)


class ClientCreateHitWithHitTypeResponseTypeDef(
    _ClientCreateHitWithHitTypeResponseTypeDef
):
    """
    Type definition for `ClientCreateHitWithHitType` `Response`

    - **HIT** *(dict) --*

      Contains the newly created HIT data. For a description of the HIT data structure as it
      appears in responses, see the HIT Data Structure documentation.

      - **HITId** *(string) --*

        A unique identifier for the HIT.

      - **HITTypeId** *(string) --*

        The ID of the HIT type of this HIT

      - **HITGroupId** *(string) --*

        The ID of the HIT Group of this HIT.

      - **HITLayoutId** *(string) --*

        The ID of the HIT Layout of this HIT.

      - **CreationTime** *(datetime) --*

        The date and time the HIT was created.

      - **Title** *(string) --*

        The title of the HIT.

      - **Description** *(string) --*

        A general description of the HIT.

      - **Question** *(string) --*

        The data the Worker completing the HIT uses produce the results. This is either either a
        QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

      - **Keywords** *(string) --*

        One or more words or phrases that describe the HIT, separated by commas. Search terms
        similar to the keywords of a HIT are more likely to have the HIT in the search results.

      - **HITStatus** *(string) --*

        The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
        Reviewable | Reviewing | Disposed.

      - **MaxAssignments** *(integer) --*

        The number of times the HIT can be accepted and completed before the HIT becomes
        unavailable.

      - **Reward** *(string) --*

        A string representing a currency amount.

      - **AutoApprovalDelayInSeconds** *(integer) --*

        The amount of time, in seconds, after the Worker submits an assignment for the HIT that the
        results are automatically approved by Amazon Mechanical Turk. This is the amount of time
        the Requester has to reject an assignment submitted by a Worker before the assignment is
        auto-approved and the Worker is paid.

      - **Expiration** *(datetime) --*

        The date and time the HIT expires.

      - **AssignmentDurationInSeconds** *(integer) --*

        The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

      - **RequesterAnnotation** *(string) --*

        An arbitrary data field the Requester who created the HIT can use. This field is visible
        only to the creator of the HIT.

      - **QualificationRequirements** *(list) --*

        Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
        have between zero and ten Qualification requirements. All requirements must be met in order
        for a Worker to accept the HIT. Additionally, other actions can be restricted using the
        ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

        - *(dict) --*

          The QualificationRequirement data structure describes a Qualification that a Worker must
          have before the Worker is allowed to accept a HIT. A requirement may optionally state
          that a Worker must have the Qualification in order to preview the HIT, or see the HIT in
          search results.

          - **QualificationTypeId** *(string) --*

            The ID of the Qualification type for the requirement.

          - **Comparator** *(string) --*

            The kind of comparison to make against a Qualification's value. You can compare a
            Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
            GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
            compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You
            can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
            values. Lastly, a Qualification requirement can also test if a Qualification Exists or
            DoesNotExist in the user's profile, regardless of its value.

          - **IntegerValues** *(list) --*

            The integer value to compare against the Qualification's value. IntegerValue must not
            be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
            the Qualification type has an integer value; it cannot be used with the Worker_Locale
            QualificationType ID. When performing a set comparison by using the In or the NotIn
            comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
            data structure.

            - *(integer) --*

          - **LocaleValues** *(list) --*

            The locale value to compare against the Qualification's value. The local value must be
            a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only
            be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with
            the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
            LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a
            set comparison by using the In or the NotIn comparator, you can use up to 30
            LocaleValue elements in a QualificationRequirement data structure.

            - *(dict) --*

              The Locale data structure represents a geographical region or location.

              - **Country** *(string) --*

                The country of the locale. Must be a valid ISO 3166 country code. For example, the
                code US refers to the United States of America.

              - **Subdivision** *(string) --*

                The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
                example, the code WA refers to the state of Washington.

          - **RequiredToPreview** *(boolean) --*

            DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
            question data for the HIT will not be shown when a Worker whose Qualifications do not
            meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must
            meet all of the requirements for which RequiredToPreview is true in order to preview
            the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or
            if there are no such requirements), but does not meet all of the requirements for the
            HIT, the Worker will be allowed to preview the HIT's question data, but will not be
            allowed to accept and complete the HIT. The default is false. This should not be used
            in combination with the ``ActionsGuarded`` field.

          - **ActionsGuarded** *(string) --*

            Setting this attribute prevents Workers whose Qualifications do not meet this
            QualificationRequirement from taking the specified action. Valid arguments include
            "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
            search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
            see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
            accept, preview, or see the HIT in their search results). It's possible for you to
            create a HIT with multiple QualificationRequirements (which can have different values
            for the ActionGuarded attribute). In this case, the Worker is only permitted to perform
            an action when they have met all QualificationRequirements guarding the action. The
            actions in the order of least restrictive to most restrictive are Discover, Preview and
            Accept. For example, if a Worker meets all QualificationRequirements that are set to
            DiscoverPreviewAndAccept, but do not meet all requirements that are set with
            PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their
            search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should
            not be used in combination with the ``RequiredToPreview`` field.

      - **HITReviewStatus** *(string) --*

        Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
        ReviewedAppropriate | ReviewedInappropriate.

      - **NumberOfAssignmentsPending** *(integer) --*

        The number of assignments for this HIT that are being previewed or have been accepted by
        Workers, but have not yet been submitted, returned, or abandoned.

      - **NumberOfAssignmentsAvailable** *(integer) --*

        The number of assignments for this HIT that are available for Workers to accept.

      - **NumberOfAssignmentsCompleted** *(integer) --*

        The number of assignments for this HIT that have been approved or rejected.
    """


_ClientCreateQualificationTypeResponseQualificationTypeTypeDef = TypedDict(
    "_ClientCreateQualificationTypeResponseQualificationTypeTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": str,
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)


class ClientCreateQualificationTypeResponseQualificationTypeTypeDef(
    _ClientCreateQualificationTypeResponseQualificationTypeTypeDef
):
    """
    Type definition for `ClientCreateQualificationTypeResponse` `QualificationType`

    The created Qualification type, returned as a QualificationType data structure.

    - **QualificationTypeId** *(string) --*

      A unique identifier for the Qualification type. A Qualification type is given a
      Qualification type ID when you call the CreateQualificationType operation.

    - **CreationTime** *(datetime) --*

      The date and time the Qualification type was created.

    - **Name** *(string) --*

      The name of the Qualification type. The type name is used to identify the type, and to find
      the type using a Qualification type search.

    - **Description** *(string) --*

      A long description for the Qualification type.

    - **Keywords** *(string) --*

      One or more words or phrases that describe theQualification type, separated by commas. The
      Keywords make the type easier to find using a search.

    - **QualificationTypeStatus** *(string) --*

      The status of the Qualification type. A Qualification type's status determines if users can
      apply to receive a Qualification of this type, and if HITs can be created with requirements
      based on this type. Valid values are Active | Inactive.

    - **Test** *(string) --*

      The questions for a Qualification test associated with this Qualification type that a user
      can take to obtain a Qualification of this type. This parameter must be specified if
      AnswerKey is present. A Qualification type cannot have both a specified Test parameter and
      an AutoGranted value of true.

    - **TestDurationInSeconds** *(integer) --*

      The amount of time, in seconds, given to a Worker to complete the Qualification test,
      beginning from the time the Worker requests the Qualification.

    - **AnswerKey** *(string) --*

      The answers to the Qualification test specified in the Test parameter.

    - **RetryDelayInSeconds** *(integer) --*

      The amount of time, in seconds, Workers must wait after taking the Qualification test
      before they can take it again. Workers can take a Qualification test multiple times if they
      were not granted the Qualification from a previous attempt, or if the test offers a
      gradient score and they want a better score. If not specified, retries are disabled and
      Workers can request a Qualification only once.

    - **IsRequestable** *(boolean) --*

      Specifies whether the Qualification type is one that a user can request through the Amazon
      Mechanical Turk web site, such as by taking a Qualification test. This value is False for
      Qualifications assigned automatically by the system. Valid values are True | False.

    - **AutoGranted** *(boolean) --*

      Specifies that requests for the Qualification type are granted immediately, without
      prompting the Worker with a Qualification test. Valid values are True | False.

    - **AutoGrantedValue** *(integer) --*

      The Qualification integer value to use for automatically granted Qualifications, if
      AutoGranted is true. This is 1 by default.
    """


_ClientCreateQualificationTypeResponseTypeDef = TypedDict(
    "_ClientCreateQualificationTypeResponseTypeDef",
    {
        "QualificationType": ClientCreateQualificationTypeResponseQualificationTypeTypeDef
    },
    total=False,
)


class ClientCreateQualificationTypeResponseTypeDef(
    _ClientCreateQualificationTypeResponseTypeDef
):
    """
    Type definition for `ClientCreateQualificationType` `Response`

    - **QualificationType** *(dict) --*

      The created Qualification type, returned as a QualificationType data structure.

      - **QualificationTypeId** *(string) --*

        A unique identifier for the Qualification type. A Qualification type is given a
        Qualification type ID when you call the CreateQualificationType operation.

      - **CreationTime** *(datetime) --*

        The date and time the Qualification type was created.

      - **Name** *(string) --*

        The name of the Qualification type. The type name is used to identify the type, and to find
        the type using a Qualification type search.

      - **Description** *(string) --*

        A long description for the Qualification type.

      - **Keywords** *(string) --*

        One or more words or phrases that describe theQualification type, separated by commas. The
        Keywords make the type easier to find using a search.

      - **QualificationTypeStatus** *(string) --*

        The status of the Qualification type. A Qualification type's status determines if users can
        apply to receive a Qualification of this type, and if HITs can be created with requirements
        based on this type. Valid values are Active | Inactive.

      - **Test** *(string) --*

        The questions for a Qualification test associated with this Qualification type that a user
        can take to obtain a Qualification of this type. This parameter must be specified if
        AnswerKey is present. A Qualification type cannot have both a specified Test parameter and
        an AutoGranted value of true.

      - **TestDurationInSeconds** *(integer) --*

        The amount of time, in seconds, given to a Worker to complete the Qualification test,
        beginning from the time the Worker requests the Qualification.

      - **AnswerKey** *(string) --*

        The answers to the Qualification test specified in the Test parameter.

      - **RetryDelayInSeconds** *(integer) --*

        The amount of time, in seconds, Workers must wait after taking the Qualification test
        before they can take it again. Workers can take a Qualification test multiple times if they
        were not granted the Qualification from a previous attempt, or if the test offers a
        gradient score and they want a better score. If not specified, retries are disabled and
        Workers can request a Qualification only once.

      - **IsRequestable** *(boolean) --*

        Specifies whether the Qualification type is one that a user can request through the Amazon
        Mechanical Turk web site, such as by taking a Qualification test. This value is False for
        Qualifications assigned automatically by the system. Valid values are True | False.

      - **AutoGranted** *(boolean) --*

        Specifies that requests for the Qualification type are granted immediately, without
        prompting the Worker with a Qualification test. Valid values are True | False.

      - **AutoGrantedValue** *(integer) --*

        The Qualification integer value to use for automatically granted Qualifications, if
        AutoGranted is true. This is 1 by default.
    """


_ClientGetAccountBalanceResponseTypeDef = TypedDict(
    "_ClientGetAccountBalanceResponseTypeDef",
    {"AvailableBalance": str, "OnHoldBalance": str},
    total=False,
)


class ClientGetAccountBalanceResponseTypeDef(_ClientGetAccountBalanceResponseTypeDef):
    """
    Type definition for `ClientGetAccountBalance` `Response`

    - **AvailableBalance** *(string) --*

      A string representing a currency amount.

    - **OnHoldBalance** *(string) --*

      A string representing a currency amount.
    """


_ClientGetAssignmentResponseAssignmentTypeDef = TypedDict(
    "_ClientGetAssignmentResponseAssignmentTypeDef",
    {
        "AssignmentId": str,
        "WorkerId": str,
        "HITId": str,
        "AssignmentStatus": str,
        "AutoApprovalTime": datetime,
        "AcceptTime": datetime,
        "SubmitTime": datetime,
        "ApprovalTime": datetime,
        "RejectionTime": datetime,
        "Deadline": datetime,
        "Answer": str,
        "RequesterFeedback": str,
    },
    total=False,
)


class ClientGetAssignmentResponseAssignmentTypeDef(
    _ClientGetAssignmentResponseAssignmentTypeDef
):
    """
    Type definition for `ClientGetAssignmentResponse` `Assignment`

    The assignment. The response includes one Assignment element.

    - **AssignmentId** *(string) --*

      A unique identifier for the assignment.

    - **WorkerId** *(string) --*

      The ID of the Worker who accepted the HIT.

    - **HITId** *(string) --*

      The ID of the HIT.

    - **AssignmentStatus** *(string) --*

      The status of the assignment.

    - **AutoApprovalTime** *(datetime) --*

      If results have been submitted, AutoApprovalTime is the date and time the results of the
      assignment results are considered Approved automatically if they have not already been
      explicitly approved or rejected by the Requester. This value is derived from the
      auto-approval delay specified by the Requester in the HIT. This value is omitted from the
      assignment if the Worker has not yet submitted results.

    - **AcceptTime** *(datetime) --*

      The date and time the Worker accepted the assignment.

    - **SubmitTime** *(datetime) --*

      If the Worker has submitted results, SubmitTime is the date and time the assignment was
      submitted. This value is omitted from the assignment if the Worker has not yet submitted
      results.

    - **ApprovalTime** *(datetime) --*

      If the Worker has submitted results and the Requester has approved the results,
      ApprovalTime is the date and time the Requester approved the results. This value is omitted
      from the assignment if the Requester has not yet approved the results.

    - **RejectionTime** *(datetime) --*

      If the Worker has submitted results and the Requester has rejected the results,
      RejectionTime is the date and time the Requester rejected the results.

    - **Deadline** *(datetime) --*

      The date and time of the deadline for the assignment. This value is derived from the
      deadline specification for the HIT and the date and time the Worker accepted the HIT.

    - **Answer** *(string) --*

      The Worker's answers submitted for the HIT contained in a QuestionFormAnswers document, if
      the Worker provides an answer. If the Worker does not provide any answers, Answer may
      contain a QuestionFormAnswers document, or Answer may be empty.

    - **RequesterFeedback** *(string) --*

      The feedback string included with the call to the ApproveAssignment operation or the
      RejectAssignment operation, if the Requester approved or rejected the assignment and
      specified feedback.
    """


_ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef(
    _ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef
):
    """
    Type definition for `ClientGetAssignmentResponseHITQualificationRequirements` `LocaleValues`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --*

      The country of the locale. Must be a valid ISO 3166 country code. For example, the
      code US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
      example, the code WA refers to the state of Washington.
    """


_ClientGetAssignmentResponseHITQualificationRequirementsTypeDef = TypedDict(
    "_ClientGetAssignmentResponseHITQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": str,
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": str,
    },
    total=False,
)


class ClientGetAssignmentResponseHITQualificationRequirementsTypeDef(
    _ClientGetAssignmentResponseHITQualificationRequirementsTypeDef
):
    """
    Type definition for `ClientGetAssignmentResponseHIT` `QualificationRequirements`

    The QualificationRequirement data structure describes a Qualification that a Worker must
    have before the Worker is allowed to accept a HIT. A requirement may optionally state
    that a Worker must have the Qualification in order to preview the HIT, or see the HIT in
    search results.

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type for the requirement.

    - **Comparator** *(string) --*

      The kind of comparison to make against a Qualification's value. You can compare a
      Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
      GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
      compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You
      can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
      values. Lastly, a Qualification requirement can also test if a Qualification Exists or
      DoesNotExist in the user's profile, regardless of its value.

    - **IntegerValues** *(list) --*

      The integer value to compare against the Qualification's value. IntegerValue must not
      be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
      the Qualification type has an integer value; it cannot be used with the Worker_Locale
      QualificationType ID. When performing a set comparison by using the In or the NotIn
      comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
      data structure.

      - *(integer) --*

    - **LocaleValues** *(list) --*

      The locale value to compare against the Qualification's value. The local value must be
      a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only
      be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with
      the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
      LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a
      set comparison by using the In or the NotIn comparator, you can use up to 30
      LocaleValue elements in a QualificationRequirement data structure.

      - *(dict) --*

        The Locale data structure represents a geographical region or location.

        - **Country** *(string) --*

          The country of the locale. Must be a valid ISO 3166 country code. For example, the
          code US refers to the United States of America.

        - **Subdivision** *(string) --*

          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
          example, the code WA refers to the state of Washington.

    - **RequiredToPreview** *(boolean) --*

      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
      question data for the HIT will not be shown when a Worker whose Qualifications do not
      meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must
      meet all of the requirements for which RequiredToPreview is true in order to preview
      the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or
      if there are no such requirements), but does not meet all of the requirements for the
      HIT, the Worker will be allowed to preview the HIT's question data, but will not be
      allowed to accept and complete the HIT. The default is false. This should not be used
      in combination with the ``ActionsGuarded`` field.

    - **ActionsGuarded** *(string) --*

      Setting this attribute prevents Workers whose Qualifications do not meet this
      QualificationRequirement from taking the specified action. Valid arguments include
      "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
      search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
      see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
      accept, preview, or see the HIT in their search results). It's possible for you to
      create a HIT with multiple QualificationRequirements (which can have different values
      for the ActionGuarded attribute). In this case, the Worker is only permitted to perform
      an action when they have met all QualificationRequirements guarding the action. The
      actions in the order of least restrictive to most restrictive are Discover, Preview and
      Accept. For example, if a Worker meets all QualificationRequirements that are set to
      DiscoverPreviewAndAccept, but do not meet all requirements that are set with
      PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their
      search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should
      not be used in combination with the ``RequiredToPreview`` field.
    """


_ClientGetAssignmentResponseHITTypeDef = TypedDict(
    "_ClientGetAssignmentResponseHITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": str,
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientGetAssignmentResponseHITQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": str,
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientGetAssignmentResponseHITTypeDef(_ClientGetAssignmentResponseHITTypeDef):
    """
    Type definition for `ClientGetAssignmentResponse` `HIT`

    The HIT associated with this assignment. The response includes one HIT element.

    - **HITId** *(string) --*

      A unique identifier for the HIT.

    - **HITTypeId** *(string) --*

      The ID of the HIT type of this HIT

    - **HITGroupId** *(string) --*

      The ID of the HIT Group of this HIT.

    - **HITLayoutId** *(string) --*

      The ID of the HIT Layout of this HIT.

    - **CreationTime** *(datetime) --*

      The date and time the HIT was created.

    - **Title** *(string) --*

      The title of the HIT.

    - **Description** *(string) --*

      A general description of the HIT.

    - **Question** *(string) --*

      The data the Worker completing the HIT uses produce the results. This is either either a
      QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

    - **Keywords** *(string) --*

      One or more words or phrases that describe the HIT, separated by commas. Search terms
      similar to the keywords of a HIT are more likely to have the HIT in the search results.

    - **HITStatus** *(string) --*

      The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
      Reviewable | Reviewing | Disposed.

    - **MaxAssignments** *(integer) --*

      The number of times the HIT can be accepted and completed before the HIT becomes
      unavailable.

    - **Reward** *(string) --*

      A string representing a currency amount.

    - **AutoApprovalDelayInSeconds** *(integer) --*

      The amount of time, in seconds, after the Worker submits an assignment for the HIT that the
      results are automatically approved by Amazon Mechanical Turk. This is the amount of time
      the Requester has to reject an assignment submitted by a Worker before the assignment is
      auto-approved and the Worker is paid.

    - **Expiration** *(datetime) --*

      The date and time the HIT expires.

    - **AssignmentDurationInSeconds** *(integer) --*

      The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

    - **RequesterAnnotation** *(string) --*

      An arbitrary data field the Requester who created the HIT can use. This field is visible
      only to the creator of the HIT.

    - **QualificationRequirements** *(list) --*

      Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
      have between zero and ten Qualification requirements. All requirements must be met in order
      for a Worker to accept the HIT. Additionally, other actions can be restricted using the
      ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

      - *(dict) --*

        The QualificationRequirement data structure describes a Qualification that a Worker must
        have before the Worker is allowed to accept a HIT. A requirement may optionally state
        that a Worker must have the Qualification in order to preview the HIT, or see the HIT in
        search results.

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type for the requirement.

        - **Comparator** *(string) --*

          The kind of comparison to make against a Qualification's value. You can compare a
          Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
          GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
          compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You
          can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
          values. Lastly, a Qualification requirement can also test if a Qualification Exists or
          DoesNotExist in the user's profile, regardless of its value.

        - **IntegerValues** *(list) --*

          The integer value to compare against the Qualification's value. IntegerValue must not
          be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
          the Qualification type has an integer value; it cannot be used with the Worker_Locale
          QualificationType ID. When performing a set comparison by using the In or the NotIn
          comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
          data structure.

          - *(integer) --*

        - **LocaleValues** *(list) --*

          The locale value to compare against the Qualification's value. The local value must be
          a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only
          be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with
          the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
          LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a
          set comparison by using the In or the NotIn comparator, you can use up to 30
          LocaleValue elements in a QualificationRequirement data structure.

          - *(dict) --*

            The Locale data structure represents a geographical region or location.

            - **Country** *(string) --*

              The country of the locale. Must be a valid ISO 3166 country code. For example, the
              code US refers to the United States of America.

            - **Subdivision** *(string) --*

              The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
              example, the code WA refers to the state of Washington.

        - **RequiredToPreview** *(boolean) --*

          DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
          question data for the HIT will not be shown when a Worker whose Qualifications do not
          meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must
          meet all of the requirements for which RequiredToPreview is true in order to preview
          the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or
          if there are no such requirements), but does not meet all of the requirements for the
          HIT, the Worker will be allowed to preview the HIT's question data, but will not be
          allowed to accept and complete the HIT. The default is false. This should not be used
          in combination with the ``ActionsGuarded`` field.

        - **ActionsGuarded** *(string) --*

          Setting this attribute prevents Workers whose Qualifications do not meet this
          QualificationRequirement from taking the specified action. Valid arguments include
          "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
          search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
          see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
          accept, preview, or see the HIT in their search results). It's possible for you to
          create a HIT with multiple QualificationRequirements (which can have different values
          for the ActionGuarded attribute). In this case, the Worker is only permitted to perform
          an action when they have met all QualificationRequirements guarding the action. The
          actions in the order of least restrictive to most restrictive are Discover, Preview and
          Accept. For example, if a Worker meets all QualificationRequirements that are set to
          DiscoverPreviewAndAccept, but do not meet all requirements that are set with
          PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their
          search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should
          not be used in combination with the ``RequiredToPreview`` field.

    - **HITReviewStatus** *(string) --*

      Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
      ReviewedAppropriate | ReviewedInappropriate.

    - **NumberOfAssignmentsPending** *(integer) --*

      The number of assignments for this HIT that are being previewed or have been accepted by
      Workers, but have not yet been submitted, returned, or abandoned.

    - **NumberOfAssignmentsAvailable** *(integer) --*

      The number of assignments for this HIT that are available for Workers to accept.

    - **NumberOfAssignmentsCompleted** *(integer) --*

      The number of assignments for this HIT that have been approved or rejected.
    """


_ClientGetAssignmentResponseTypeDef = TypedDict(
    "_ClientGetAssignmentResponseTypeDef",
    {
        "Assignment": ClientGetAssignmentResponseAssignmentTypeDef,
        "HIT": ClientGetAssignmentResponseHITTypeDef,
    },
    total=False,
)


class ClientGetAssignmentResponseTypeDef(_ClientGetAssignmentResponseTypeDef):
    """
    Type definition for `ClientGetAssignment` `Response`

    - **Assignment** *(dict) --*

      The assignment. The response includes one Assignment element.

      - **AssignmentId** *(string) --*

        A unique identifier for the assignment.

      - **WorkerId** *(string) --*

        The ID of the Worker who accepted the HIT.

      - **HITId** *(string) --*

        The ID of the HIT.

      - **AssignmentStatus** *(string) --*

        The status of the assignment.

      - **AutoApprovalTime** *(datetime) --*

        If results have been submitted, AutoApprovalTime is the date and time the results of the
        assignment results are considered Approved automatically if they have not already been
        explicitly approved or rejected by the Requester. This value is derived from the
        auto-approval delay specified by the Requester in the HIT. This value is omitted from the
        assignment if the Worker has not yet submitted results.

      - **AcceptTime** *(datetime) --*

        The date and time the Worker accepted the assignment.

      - **SubmitTime** *(datetime) --*

        If the Worker has submitted results, SubmitTime is the date and time the assignment was
        submitted. This value is omitted from the assignment if the Worker has not yet submitted
        results.

      - **ApprovalTime** *(datetime) --*

        If the Worker has submitted results and the Requester has approved the results,
        ApprovalTime is the date and time the Requester approved the results. This value is omitted
        from the assignment if the Requester has not yet approved the results.

      - **RejectionTime** *(datetime) --*

        If the Worker has submitted results and the Requester has rejected the results,
        RejectionTime is the date and time the Requester rejected the results.

      - **Deadline** *(datetime) --*

        The date and time of the deadline for the assignment. This value is derived from the
        deadline specification for the HIT and the date and time the Worker accepted the HIT.

      - **Answer** *(string) --*

        The Worker's answers submitted for the HIT contained in a QuestionFormAnswers document, if
        the Worker provides an answer. If the Worker does not provide any answers, Answer may
        contain a QuestionFormAnswers document, or Answer may be empty.

      - **RequesterFeedback** *(string) --*

        The feedback string included with the call to the ApproveAssignment operation or the
        RejectAssignment operation, if the Requester approved or rejected the assignment and
        specified feedback.

    - **HIT** *(dict) --*

      The HIT associated with this assignment. The response includes one HIT element.

      - **HITId** *(string) --*

        A unique identifier for the HIT.

      - **HITTypeId** *(string) --*

        The ID of the HIT type of this HIT

      - **HITGroupId** *(string) --*

        The ID of the HIT Group of this HIT.

      - **HITLayoutId** *(string) --*

        The ID of the HIT Layout of this HIT.

      - **CreationTime** *(datetime) --*

        The date and time the HIT was created.

      - **Title** *(string) --*

        The title of the HIT.

      - **Description** *(string) --*

        A general description of the HIT.

      - **Question** *(string) --*

        The data the Worker completing the HIT uses produce the results. This is either either a
        QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

      - **Keywords** *(string) --*

        One or more words or phrases that describe the HIT, separated by commas. Search terms
        similar to the keywords of a HIT are more likely to have the HIT in the search results.

      - **HITStatus** *(string) --*

        The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
        Reviewable | Reviewing | Disposed.

      - **MaxAssignments** *(integer) --*

        The number of times the HIT can be accepted and completed before the HIT becomes
        unavailable.

      - **Reward** *(string) --*

        A string representing a currency amount.

      - **AutoApprovalDelayInSeconds** *(integer) --*

        The amount of time, in seconds, after the Worker submits an assignment for the HIT that the
        results are automatically approved by Amazon Mechanical Turk. This is the amount of time
        the Requester has to reject an assignment submitted by a Worker before the assignment is
        auto-approved and the Worker is paid.

      - **Expiration** *(datetime) --*

        The date and time the HIT expires.

      - **AssignmentDurationInSeconds** *(integer) --*

        The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

      - **RequesterAnnotation** *(string) --*

        An arbitrary data field the Requester who created the HIT can use. This field is visible
        only to the creator of the HIT.

      - **QualificationRequirements** *(list) --*

        Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
        have between zero and ten Qualification requirements. All requirements must be met in order
        for a Worker to accept the HIT. Additionally, other actions can be restricted using the
        ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

        - *(dict) --*

          The QualificationRequirement data structure describes a Qualification that a Worker must
          have before the Worker is allowed to accept a HIT. A requirement may optionally state
          that a Worker must have the Qualification in order to preview the HIT, or see the HIT in
          search results.

          - **QualificationTypeId** *(string) --*

            The ID of the Qualification type for the requirement.

          - **Comparator** *(string) --*

            The kind of comparison to make against a Qualification's value. You can compare a
            Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
            GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
            compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You
            can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
            values. Lastly, a Qualification requirement can also test if a Qualification Exists or
            DoesNotExist in the user's profile, regardless of its value.

          - **IntegerValues** *(list) --*

            The integer value to compare against the Qualification's value. IntegerValue must not
            be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
            the Qualification type has an integer value; it cannot be used with the Worker_Locale
            QualificationType ID. When performing a set comparison by using the In or the NotIn
            comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
            data structure.

            - *(integer) --*

          - **LocaleValues** *(list) --*

            The locale value to compare against the Qualification's value. The local value must be
            a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only
            be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with
            the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
            LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a
            set comparison by using the In or the NotIn comparator, you can use up to 30
            LocaleValue elements in a QualificationRequirement data structure.

            - *(dict) --*

              The Locale data structure represents a geographical region or location.

              - **Country** *(string) --*

                The country of the locale. Must be a valid ISO 3166 country code. For example, the
                code US refers to the United States of America.

              - **Subdivision** *(string) --*

                The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
                example, the code WA refers to the state of Washington.

          - **RequiredToPreview** *(boolean) --*

            DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
            question data for the HIT will not be shown when a Worker whose Qualifications do not
            meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must
            meet all of the requirements for which RequiredToPreview is true in order to preview
            the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or
            if there are no such requirements), but does not meet all of the requirements for the
            HIT, the Worker will be allowed to preview the HIT's question data, but will not be
            allowed to accept and complete the HIT. The default is false. This should not be used
            in combination with the ``ActionsGuarded`` field.

          - **ActionsGuarded** *(string) --*

            Setting this attribute prevents Workers whose Qualifications do not meet this
            QualificationRequirement from taking the specified action. Valid arguments include
            "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
            search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
            see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
            accept, preview, or see the HIT in their search results). It's possible for you to
            create a HIT with multiple QualificationRequirements (which can have different values
            for the ActionGuarded attribute). In this case, the Worker is only permitted to perform
            an action when they have met all QualificationRequirements guarding the action. The
            actions in the order of least restrictive to most restrictive are Discover, Preview and
            Accept. For example, if a Worker meets all QualificationRequirements that are set to
            DiscoverPreviewAndAccept, but do not meet all requirements that are set with
            PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their
            search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should
            not be used in combination with the ``RequiredToPreview`` field.

      - **HITReviewStatus** *(string) --*

        Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
        ReviewedAppropriate | ReviewedInappropriate.

      - **NumberOfAssignmentsPending** *(integer) --*

        The number of assignments for this HIT that are being previewed or have been accepted by
        Workers, but have not yet been submitted, returned, or abandoned.

      - **NumberOfAssignmentsAvailable** *(integer) --*

        The number of assignments for this HIT that are available for Workers to accept.

      - **NumberOfAssignmentsCompleted** *(integer) --*

        The number of assignments for this HIT that have been approved or rejected.
    """


_ClientGetFileUploadUrlResponseTypeDef = TypedDict(
    "_ClientGetFileUploadUrlResponseTypeDef", {"FileUploadURL": str}, total=False
)


class ClientGetFileUploadUrlResponseTypeDef(_ClientGetFileUploadUrlResponseTypeDef):
    """
    Type definition for `ClientGetFileUploadUrl` `Response`

    - **FileUploadURL** *(string) --*

      A temporary URL for the file that the Worker uploaded for the answer.
    """


_ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef(
    _ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef
):
    """
    Type definition for `ClientGetHitResponseHITQualificationRequirements` `LocaleValues`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --*

      The country of the locale. Must be a valid ISO 3166 country code. For example, the
      code US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
      example, the code WA refers to the state of Washington.
    """


_ClientGetHitResponseHITQualificationRequirementsTypeDef = TypedDict(
    "_ClientGetHitResponseHITQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": str,
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": str,
    },
    total=False,
)


class ClientGetHitResponseHITQualificationRequirementsTypeDef(
    _ClientGetHitResponseHITQualificationRequirementsTypeDef
):
    """
    Type definition for `ClientGetHitResponseHIT` `QualificationRequirements`

    The QualificationRequirement data structure describes a Qualification that a Worker must
    have before the Worker is allowed to accept a HIT. A requirement may optionally state
    that a Worker must have the Qualification in order to preview the HIT, or see the HIT in
    search results.

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type for the requirement.

    - **Comparator** *(string) --*

      The kind of comparison to make against a Qualification's value. You can compare a
      Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
      GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
      compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You
      can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
      values. Lastly, a Qualification requirement can also test if a Qualification Exists or
      DoesNotExist in the user's profile, regardless of its value.

    - **IntegerValues** *(list) --*

      The integer value to compare against the Qualification's value. IntegerValue must not
      be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
      the Qualification type has an integer value; it cannot be used with the Worker_Locale
      QualificationType ID. When performing a set comparison by using the In or the NotIn
      comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
      data structure.

      - *(integer) --*

    - **LocaleValues** *(list) --*

      The locale value to compare against the Qualification's value. The local value must be
      a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only
      be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with
      the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
      LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a
      set comparison by using the In or the NotIn comparator, you can use up to 30
      LocaleValue elements in a QualificationRequirement data structure.

      - *(dict) --*

        The Locale data structure represents a geographical region or location.

        - **Country** *(string) --*

          The country of the locale. Must be a valid ISO 3166 country code. For example, the
          code US refers to the United States of America.

        - **Subdivision** *(string) --*

          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
          example, the code WA refers to the state of Washington.

    - **RequiredToPreview** *(boolean) --*

      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
      question data for the HIT will not be shown when a Worker whose Qualifications do not
      meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must
      meet all of the requirements for which RequiredToPreview is true in order to preview
      the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or
      if there are no such requirements), but does not meet all of the requirements for the
      HIT, the Worker will be allowed to preview the HIT's question data, but will not be
      allowed to accept and complete the HIT. The default is false. This should not be used
      in combination with the ``ActionsGuarded`` field.

    - **ActionsGuarded** *(string) --*

      Setting this attribute prevents Workers whose Qualifications do not meet this
      QualificationRequirement from taking the specified action. Valid arguments include
      "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
      search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
      see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
      accept, preview, or see the HIT in their search results). It's possible for you to
      create a HIT with multiple QualificationRequirements (which can have different values
      for the ActionGuarded attribute). In this case, the Worker is only permitted to perform
      an action when they have met all QualificationRequirements guarding the action. The
      actions in the order of least restrictive to most restrictive are Discover, Preview and
      Accept. For example, if a Worker meets all QualificationRequirements that are set to
      DiscoverPreviewAndAccept, but do not meet all requirements that are set with
      PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their
      search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should
      not be used in combination with the ``RequiredToPreview`` field.
    """


_ClientGetHitResponseHITTypeDef = TypedDict(
    "_ClientGetHitResponseHITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": str,
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientGetHitResponseHITQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": str,
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientGetHitResponseHITTypeDef(_ClientGetHitResponseHITTypeDef):
    """
    Type definition for `ClientGetHitResponse` `HIT`

    Contains the requested HIT data.

    - **HITId** *(string) --*

      A unique identifier for the HIT.

    - **HITTypeId** *(string) --*

      The ID of the HIT type of this HIT

    - **HITGroupId** *(string) --*

      The ID of the HIT Group of this HIT.

    - **HITLayoutId** *(string) --*

      The ID of the HIT Layout of this HIT.

    - **CreationTime** *(datetime) --*

      The date and time the HIT was created.

    - **Title** *(string) --*

      The title of the HIT.

    - **Description** *(string) --*

      A general description of the HIT.

    - **Question** *(string) --*

      The data the Worker completing the HIT uses produce the results. This is either either a
      QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

    - **Keywords** *(string) --*

      One or more words or phrases that describe the HIT, separated by commas. Search terms
      similar to the keywords of a HIT are more likely to have the HIT in the search results.

    - **HITStatus** *(string) --*

      The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
      Reviewable | Reviewing | Disposed.

    - **MaxAssignments** *(integer) --*

      The number of times the HIT can be accepted and completed before the HIT becomes
      unavailable.

    - **Reward** *(string) --*

      A string representing a currency amount.

    - **AutoApprovalDelayInSeconds** *(integer) --*

      The amount of time, in seconds, after the Worker submits an assignment for the HIT that the
      results are automatically approved by Amazon Mechanical Turk. This is the amount of time
      the Requester has to reject an assignment submitted by a Worker before the assignment is
      auto-approved and the Worker is paid.

    - **Expiration** *(datetime) --*

      The date and time the HIT expires.

    - **AssignmentDurationInSeconds** *(integer) --*

      The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

    - **RequesterAnnotation** *(string) --*

      An arbitrary data field the Requester who created the HIT can use. This field is visible
      only to the creator of the HIT.

    - **QualificationRequirements** *(list) --*

      Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
      have between zero and ten Qualification requirements. All requirements must be met in order
      for a Worker to accept the HIT. Additionally, other actions can be restricted using the
      ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

      - *(dict) --*

        The QualificationRequirement data structure describes a Qualification that a Worker must
        have before the Worker is allowed to accept a HIT. A requirement may optionally state
        that a Worker must have the Qualification in order to preview the HIT, or see the HIT in
        search results.

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type for the requirement.

        - **Comparator** *(string) --*

          The kind of comparison to make against a Qualification's value. You can compare a
          Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
          GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
          compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You
          can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
          values. Lastly, a Qualification requirement can also test if a Qualification Exists or
          DoesNotExist in the user's profile, regardless of its value.

        - **IntegerValues** *(list) --*

          The integer value to compare against the Qualification's value. IntegerValue must not
          be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
          the Qualification type has an integer value; it cannot be used with the Worker_Locale
          QualificationType ID. When performing a set comparison by using the In or the NotIn
          comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
          data structure.

          - *(integer) --*

        - **LocaleValues** *(list) --*

          The locale value to compare against the Qualification's value. The local value must be
          a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only
          be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with
          the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
          LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a
          set comparison by using the In or the NotIn comparator, you can use up to 30
          LocaleValue elements in a QualificationRequirement data structure.

          - *(dict) --*

            The Locale data structure represents a geographical region or location.

            - **Country** *(string) --*

              The country of the locale. Must be a valid ISO 3166 country code. For example, the
              code US refers to the United States of America.

            - **Subdivision** *(string) --*

              The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
              example, the code WA refers to the state of Washington.

        - **RequiredToPreview** *(boolean) --*

          DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
          question data for the HIT will not be shown when a Worker whose Qualifications do not
          meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must
          meet all of the requirements for which RequiredToPreview is true in order to preview
          the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or
          if there are no such requirements), but does not meet all of the requirements for the
          HIT, the Worker will be allowed to preview the HIT's question data, but will not be
          allowed to accept and complete the HIT. The default is false. This should not be used
          in combination with the ``ActionsGuarded`` field.

        - **ActionsGuarded** *(string) --*

          Setting this attribute prevents Workers whose Qualifications do not meet this
          QualificationRequirement from taking the specified action. Valid arguments include
          "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
          search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
          see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
          accept, preview, or see the HIT in their search results). It's possible for you to
          create a HIT with multiple QualificationRequirements (which can have different values
          for the ActionGuarded attribute). In this case, the Worker is only permitted to perform
          an action when they have met all QualificationRequirements guarding the action. The
          actions in the order of least restrictive to most restrictive are Discover, Preview and
          Accept. For example, if a Worker meets all QualificationRequirements that are set to
          DiscoverPreviewAndAccept, but do not meet all requirements that are set with
          PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their
          search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should
          not be used in combination with the ``RequiredToPreview`` field.

    - **HITReviewStatus** *(string) --*

      Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
      ReviewedAppropriate | ReviewedInappropriate.

    - **NumberOfAssignmentsPending** *(integer) --*

      The number of assignments for this HIT that are being previewed or have been accepted by
      Workers, but have not yet been submitted, returned, or abandoned.

    - **NumberOfAssignmentsAvailable** *(integer) --*

      The number of assignments for this HIT that are available for Workers to accept.

    - **NumberOfAssignmentsCompleted** *(integer) --*

      The number of assignments for this HIT that have been approved or rejected.
    """


_ClientGetHitResponseTypeDef = TypedDict(
    "_ClientGetHitResponseTypeDef", {"HIT": ClientGetHitResponseHITTypeDef}, total=False
)


class ClientGetHitResponseTypeDef(_ClientGetHitResponseTypeDef):
    """
    Type definition for `ClientGetHit` `Response`

    - **HIT** *(dict) --*

      Contains the requested HIT data.

      - **HITId** *(string) --*

        A unique identifier for the HIT.

      - **HITTypeId** *(string) --*

        The ID of the HIT type of this HIT

      - **HITGroupId** *(string) --*

        The ID of the HIT Group of this HIT.

      - **HITLayoutId** *(string) --*

        The ID of the HIT Layout of this HIT.

      - **CreationTime** *(datetime) --*

        The date and time the HIT was created.

      - **Title** *(string) --*

        The title of the HIT.

      - **Description** *(string) --*

        A general description of the HIT.

      - **Question** *(string) --*

        The data the Worker completing the HIT uses produce the results. This is either either a
        QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

      - **Keywords** *(string) --*

        One or more words or phrases that describe the HIT, separated by commas. Search terms
        similar to the keywords of a HIT are more likely to have the HIT in the search results.

      - **HITStatus** *(string) --*

        The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
        Reviewable | Reviewing | Disposed.

      - **MaxAssignments** *(integer) --*

        The number of times the HIT can be accepted and completed before the HIT becomes
        unavailable.

      - **Reward** *(string) --*

        A string representing a currency amount.

      - **AutoApprovalDelayInSeconds** *(integer) --*

        The amount of time, in seconds, after the Worker submits an assignment for the HIT that the
        results are automatically approved by Amazon Mechanical Turk. This is the amount of time
        the Requester has to reject an assignment submitted by a Worker before the assignment is
        auto-approved and the Worker is paid.

      - **Expiration** *(datetime) --*

        The date and time the HIT expires.

      - **AssignmentDurationInSeconds** *(integer) --*

        The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

      - **RequesterAnnotation** *(string) --*

        An arbitrary data field the Requester who created the HIT can use. This field is visible
        only to the creator of the HIT.

      - **QualificationRequirements** *(list) --*

        Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
        have between zero and ten Qualification requirements. All requirements must be met in order
        for a Worker to accept the HIT. Additionally, other actions can be restricted using the
        ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

        - *(dict) --*

          The QualificationRequirement data structure describes a Qualification that a Worker must
          have before the Worker is allowed to accept a HIT. A requirement may optionally state
          that a Worker must have the Qualification in order to preview the HIT, or see the HIT in
          search results.

          - **QualificationTypeId** *(string) --*

            The ID of the Qualification type for the requirement.

          - **Comparator** *(string) --*

            The kind of comparison to make against a Qualification's value. You can compare a
            Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
            GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
            compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You
            can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
            values. Lastly, a Qualification requirement can also test if a Qualification Exists or
            DoesNotExist in the user's profile, regardless of its value.

          - **IntegerValues** *(list) --*

            The integer value to compare against the Qualification's value. IntegerValue must not
            be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
            the Qualification type has an integer value; it cannot be used with the Worker_Locale
            QualificationType ID. When performing a set comparison by using the In or the NotIn
            comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
            data structure.

            - *(integer) --*

          - **LocaleValues** *(list) --*

            The locale value to compare against the Qualification's value. The local value must be
            a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only
            be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with
            the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
            LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a
            set comparison by using the In or the NotIn comparator, you can use up to 30
            LocaleValue elements in a QualificationRequirement data structure.

            - *(dict) --*

              The Locale data structure represents a geographical region or location.

              - **Country** *(string) --*

                The country of the locale. Must be a valid ISO 3166 country code. For example, the
                code US refers to the United States of America.

              - **Subdivision** *(string) --*

                The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
                example, the code WA refers to the state of Washington.

          - **RequiredToPreview** *(boolean) --*

            DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the
            question data for the HIT will not be shown when a Worker whose Qualifications do not
            meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must
            meet all of the requirements for which RequiredToPreview is true in order to preview
            the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or
            if there are no such requirements), but does not meet all of the requirements for the
            HIT, the Worker will be allowed to preview the HIT's question data, but will not be
            allowed to accept and complete the HIT. The default is false. This should not be used
            in combination with the ``ActionsGuarded`` field.

          - **ActionsGuarded** *(string) --*

            Setting this attribute prevents Workers whose Qualifications do not meet this
            QualificationRequirement from taking the specified action. Valid arguments include
            "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
            search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
            see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
            accept, preview, or see the HIT in their search results). It's possible for you to
            create a HIT with multiple QualificationRequirements (which can have different values
            for the ActionGuarded attribute). In this case, the Worker is only permitted to perform
            an action when they have met all QualificationRequirements guarding the action. The
            actions in the order of least restrictive to most restrictive are Discover, Preview and
            Accept. For example, if a Worker meets all QualificationRequirements that are set to
            DiscoverPreviewAndAccept, but do not meet all requirements that are set with
            PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their
            search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should
            not be used in combination with the ``RequiredToPreview`` field.

      - **HITReviewStatus** *(string) --*

        Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
        ReviewedAppropriate | ReviewedInappropriate.

      - **NumberOfAssignmentsPending** *(integer) --*

        The number of assignments for this HIT that are being previewed or have been accepted by
        Workers, but have not yet been submitted, returned, or abandoned.

      - **NumberOfAssignmentsAvailable** *(integer) --*

        The number of assignments for this HIT that are available for Workers to accept.

      - **NumberOfAssignmentsCompleted** *(integer) --*

        The number of assignments for this HIT that have been approved or rejected.
    """


_ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef = TypedDict(
    "_ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef(
    _ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef
):
    """
    Type definition for `ClientGetQualificationScoreResponseQualification` `LocaleValue`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --*

      The country of the locale. Must be a valid ISO 3166 country code. For example, the code
      US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example,
      the code WA refers to the state of Washington.
    """


_ClientGetQualificationScoreResponseQualificationTypeDef = TypedDict(
    "_ClientGetQualificationScoreResponseQualificationTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "GrantTime": datetime,
        "IntegerValue": int,
        "LocaleValue": ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef,
        "Status": str,
    },
    total=False,
)


class ClientGetQualificationScoreResponseQualificationTypeDef(
    _ClientGetQualificationScoreResponseQualificationTypeDef
):
    """
    Type definition for `ClientGetQualificationScoreResponse` `Qualification`

    The Qualification data structure of the Qualification assigned to a user, including the
    Qualification type and the value (score).

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type for the Qualification.

    - **WorkerId** *(string) --*

      The ID of the Worker who possesses the Qualification.

    - **GrantTime** *(datetime) --*

      The date and time the Qualification was granted to the Worker. If the Worker's
      Qualification was revoked, and then re-granted based on a new Qualification request,
      GrantTime is the date and time of the last call to the AcceptQualificationRequest operation.

    - **IntegerValue** *(integer) --*

      The value (score) of the Qualification, if the Qualification has an integer value.

    - **LocaleValue** *(dict) --*

      The Locale data structure represents a geographical region or location.

      - **Country** *(string) --*

        The country of the locale. Must be a valid ISO 3166 country code. For example, the code
        US refers to the United States of America.

      - **Subdivision** *(string) --*

        The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example,
        the code WA refers to the state of Washington.

    - **Status** *(string) --*

      The status of the Qualification. Valid values are Granted | Revoked.
    """


_ClientGetQualificationScoreResponseTypeDef = TypedDict(
    "_ClientGetQualificationScoreResponseTypeDef",
    {"Qualification": ClientGetQualificationScoreResponseQualificationTypeDef},
    total=False,
)


class ClientGetQualificationScoreResponseTypeDef(
    _ClientGetQualificationScoreResponseTypeDef
):
    """
    Type definition for `ClientGetQualificationScore` `Response`

    - **Qualification** *(dict) --*

      The Qualification data structure of the Qualification assigned to a user, including the
      Qualification type and the value (score).

      - **QualificationTypeId** *(string) --*

        The ID of the Qualification type for the Qualification.

      - **WorkerId** *(string) --*

        The ID of the Worker who possesses the Qualification.

      - **GrantTime** *(datetime) --*

        The date and time the Qualification was granted to the Worker. If the Worker's
        Qualification was revoked, and then re-granted based on a new Qualification request,
        GrantTime is the date and time of the last call to the AcceptQualificationRequest operation.

      - **IntegerValue** *(integer) --*

        The value (score) of the Qualification, if the Qualification has an integer value.

      - **LocaleValue** *(dict) --*

        The Locale data structure represents a geographical region or location.

        - **Country** *(string) --*

          The country of the locale. Must be a valid ISO 3166 country code. For example, the code
          US refers to the United States of America.

        - **Subdivision** *(string) --*

          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example,
          the code WA refers to the state of Washington.

      - **Status** *(string) --*

        The status of the Qualification. Valid values are Granted | Revoked.
    """


_ClientGetQualificationTypeResponseQualificationTypeTypeDef = TypedDict(
    "_ClientGetQualificationTypeResponseQualificationTypeTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": str,
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)


class ClientGetQualificationTypeResponseQualificationTypeTypeDef(
    _ClientGetQualificationTypeResponseQualificationTypeTypeDef
):
    """
    Type definition for `ClientGetQualificationTypeResponse` `QualificationType`

    The returned Qualification Type

    - **QualificationTypeId** *(string) --*

      A unique identifier for the Qualification type. A Qualification type is given a
      Qualification type ID when you call the CreateQualificationType operation.

    - **CreationTime** *(datetime) --*

      The date and time the Qualification type was created.

    - **Name** *(string) --*

      The name of the Qualification type. The type name is used to identify the type, and to find
      the type using a Qualification type search.

    - **Description** *(string) --*

      A long description for the Qualification type.

    - **Keywords** *(string) --*

      One or more words or phrases that describe theQualification type, separated by commas. The
      Keywords make the type easier to find using a search.

    - **QualificationTypeStatus** *(string) --*

      The status of the Qualification type. A Qualification type's status determines if users can
      apply to receive a Qualification of this type, and if HITs can be created with requirements
      based on this type. Valid values are Active | Inactive.

    - **Test** *(string) --*

      The questions for a Qualification test associated with this Qualification type that a user
      can take to obtain a Qualification of this type. This parameter must be specified if
      AnswerKey is present. A Qualification type cannot have both a specified Test parameter and
      an AutoGranted value of true.

    - **TestDurationInSeconds** *(integer) --*

      The amount of time, in seconds, given to a Worker to complete the Qualification test,
      beginning from the time the Worker requests the Qualification.

    - **AnswerKey** *(string) --*

      The answers to the Qualification test specified in the Test parameter.

    - **RetryDelayInSeconds** *(integer) --*

      The amount of time, in seconds, Workers must wait after taking the Qualification test
      before they can take it again. Workers can take a Qualification test multiple times if they
      were not granted the Qualification from a previous attempt, or if the test offers a
      gradient score and they want a better score. If not specified, retries are disabled and
      Workers can request a Qualification only once.

    - **IsRequestable** *(boolean) --*

      Specifies whether the Qualification type is one that a user can request through the Amazon
      Mechanical Turk web site, such as by taking a Qualification test. This value is False for
      Qualifications assigned automatically by the system. Valid values are True | False.

    - **AutoGranted** *(boolean) --*

      Specifies that requests for the Qualification type are granted immediately, without
      prompting the Worker with a Qualification test. Valid values are True | False.

    - **AutoGrantedValue** *(integer) --*

      The Qualification integer value to use for automatically granted Qualifications, if
      AutoGranted is true. This is 1 by default.
    """


_ClientGetQualificationTypeResponseTypeDef = TypedDict(
    "_ClientGetQualificationTypeResponseTypeDef",
    {"QualificationType": ClientGetQualificationTypeResponseQualificationTypeTypeDef},
    total=False,
)


class ClientGetQualificationTypeResponseTypeDef(
    _ClientGetQualificationTypeResponseTypeDef
):
    """
    Type definition for `ClientGetQualificationType` `Response`

    - **QualificationType** *(dict) --*

      The returned Qualification Type

      - **QualificationTypeId** *(string) --*

        A unique identifier for the Qualification type. A Qualification type is given a
        Qualification type ID when you call the CreateQualificationType operation.

      - **CreationTime** *(datetime) --*

        The date and time the Qualification type was created.

      - **Name** *(string) --*

        The name of the Qualification type. The type name is used to identify the type, and to find
        the type using a Qualification type search.

      - **Description** *(string) --*

        A long description for the Qualification type.

      - **Keywords** *(string) --*

        One or more words or phrases that describe theQualification type, separated by commas. The
        Keywords make the type easier to find using a search.

      - **QualificationTypeStatus** *(string) --*

        The status of the Qualification type. A Qualification type's status determines if users can
        apply to receive a Qualification of this type, and if HITs can be created with requirements
        based on this type. Valid values are Active | Inactive.

      - **Test** *(string) --*

        The questions for a Qualification test associated with this Qualification type that a user
        can take to obtain a Qualification of this type. This parameter must be specified if
        AnswerKey is present. A Qualification type cannot have both a specified Test parameter and
        an AutoGranted value of true.

      - **TestDurationInSeconds** *(integer) --*

        The amount of time, in seconds, given to a Worker to complete the Qualification test,
        beginning from the time the Worker requests the Qualification.

      - **AnswerKey** *(string) --*

        The answers to the Qualification test specified in the Test parameter.

      - **RetryDelayInSeconds** *(integer) --*

        The amount of time, in seconds, Workers must wait after taking the Qualification test
        before they can take it again. Workers can take a Qualification test multiple times if they
        were not granted the Qualification from a previous attempt, or if the test offers a
        gradient score and they want a better score. If not specified, retries are disabled and
        Workers can request a Qualification only once.

      - **IsRequestable** *(boolean) --*

        Specifies whether the Qualification type is one that a user can request through the Amazon
        Mechanical Turk web site, such as by taking a Qualification test. This value is False for
        Qualifications assigned automatically by the system. Valid values are True | False.

      - **AutoGranted** *(boolean) --*

        Specifies that requests for the Qualification type are granted immediately, without
        prompting the Worker with a Qualification test. Valid values are True | False.

      - **AutoGrantedValue** *(integer) --*

        The Qualification integer value to use for automatically granted Qualifications, if
        AutoGranted is true. This is 1 by default.
    """


_ClientListAssignmentsForHitResponseAssignmentsTypeDef = TypedDict(
    "_ClientListAssignmentsForHitResponseAssignmentsTypeDef",
    {
        "AssignmentId": str,
        "WorkerId": str,
        "HITId": str,
        "AssignmentStatus": str,
        "AutoApprovalTime": datetime,
        "AcceptTime": datetime,
        "SubmitTime": datetime,
        "ApprovalTime": datetime,
        "RejectionTime": datetime,
        "Deadline": datetime,
        "Answer": str,
        "RequesterFeedback": str,
    },
    total=False,
)


class ClientListAssignmentsForHitResponseAssignmentsTypeDef(
    _ClientListAssignmentsForHitResponseAssignmentsTypeDef
):
    """
    Type definition for `ClientListAssignmentsForHitResponse` `Assignments`

    The Assignment data structure represents a single assignment of a HIT to a Worker. The
    assignment tracks the Worker's efforts to complete the HIT, and contains the results for
    later retrieval.

    - **AssignmentId** *(string) --*

      A unique identifier for the assignment.

    - **WorkerId** *(string) --*

      The ID of the Worker who accepted the HIT.

    - **HITId** *(string) --*

      The ID of the HIT.

    - **AssignmentStatus** *(string) --*

      The status of the assignment.

    - **AutoApprovalTime** *(datetime) --*

      If results have been submitted, AutoApprovalTime is the date and time the results of the
      assignment results are considered Approved automatically if they have not already been
      explicitly approved or rejected by the Requester. This value is derived from the
      auto-approval delay specified by the Requester in the HIT. This value is omitted from the
      assignment if the Worker has not yet submitted results.

    - **AcceptTime** *(datetime) --*

      The date and time the Worker accepted the assignment.

    - **SubmitTime** *(datetime) --*

      If the Worker has submitted results, SubmitTime is the date and time the assignment was
      submitted. This value is omitted from the assignment if the Worker has not yet submitted
      results.

    - **ApprovalTime** *(datetime) --*

      If the Worker has submitted results and the Requester has approved the results,
      ApprovalTime is the date and time the Requester approved the results. This value is
      omitted from the assignment if the Requester has not yet approved the results.

    - **RejectionTime** *(datetime) --*

      If the Worker has submitted results and the Requester has rejected the results,
      RejectionTime is the date and time the Requester rejected the results.

    - **Deadline** *(datetime) --*

      The date and time of the deadline for the assignment. This value is derived from the
      deadline specification for the HIT and the date and time the Worker accepted the HIT.

    - **Answer** *(string) --*

      The Worker's answers submitted for the HIT contained in a QuestionFormAnswers document,
      if the Worker provides an answer. If the Worker does not provide any answers, Answer may
      contain a QuestionFormAnswers document, or Answer may be empty.

    - **RequesterFeedback** *(string) --*

      The feedback string included with the call to the ApproveAssignment operation or the
      RejectAssignment operation, if the Requester approved or rejected the assignment and
      specified feedback.
    """


_ClientListAssignmentsForHitResponseTypeDef = TypedDict(
    "_ClientListAssignmentsForHitResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Assignments": List[ClientListAssignmentsForHitResponseAssignmentsTypeDef],
    },
    total=False,
)


class ClientListAssignmentsForHitResponseTypeDef(
    _ClientListAssignmentsForHitResponseTypeDef
):
    """
    Type definition for `ClientListAssignmentsForHit` `Response`

    - **NextToken** *(string) --*

      If the previous response was incomplete (because there is more data to retrieve), Amazon
      Mechanical Turk returns a pagination token in the response. You can use this pagination token
      to retrieve the next set of results.

    - **NumResults** *(integer) --*

      The number of assignments on the page in the filtered results list, equivalent to the number
      of assignments returned by this call.

    - **Assignments** *(list) --*

      The collection of Assignment data structures returned by this call.

      - *(dict) --*

        The Assignment data structure represents a single assignment of a HIT to a Worker. The
        assignment tracks the Worker's efforts to complete the HIT, and contains the results for
        later retrieval.

        - **AssignmentId** *(string) --*

          A unique identifier for the assignment.

        - **WorkerId** *(string) --*

          The ID of the Worker who accepted the HIT.

        - **HITId** *(string) --*

          The ID of the HIT.

        - **AssignmentStatus** *(string) --*

          The status of the assignment.

        - **AutoApprovalTime** *(datetime) --*

          If results have been submitted, AutoApprovalTime is the date and time the results of the
          assignment results are considered Approved automatically if they have not already been
          explicitly approved or rejected by the Requester. This value is derived from the
          auto-approval delay specified by the Requester in the HIT. This value is omitted from the
          assignment if the Worker has not yet submitted results.

        - **AcceptTime** *(datetime) --*

          The date and time the Worker accepted the assignment.

        - **SubmitTime** *(datetime) --*

          If the Worker has submitted results, SubmitTime is the date and time the assignment was
          submitted. This value is omitted from the assignment if the Worker has not yet submitted
          results.

        - **ApprovalTime** *(datetime) --*

          If the Worker has submitted results and the Requester has approved the results,
          ApprovalTime is the date and time the Requester approved the results. This value is
          omitted from the assignment if the Requester has not yet approved the results.

        - **RejectionTime** *(datetime) --*

          If the Worker has submitted results and the Requester has rejected the results,
          RejectionTime is the date and time the Requester rejected the results.

        - **Deadline** *(datetime) --*

          The date and time of the deadline for the assignment. This value is derived from the
          deadline specification for the HIT and the date and time the Worker accepted the HIT.

        - **Answer** *(string) --*

          The Worker's answers submitted for the HIT contained in a QuestionFormAnswers document,
          if the Worker provides an answer. If the Worker does not provide any answers, Answer may
          contain a QuestionFormAnswers document, or Answer may be empty.

        - **RequesterFeedback** *(string) --*

          The feedback string included with the call to the ApproveAssignment operation or the
          RejectAssignment operation, if the Requester approved or rejected the assignment and
          specified feedback.
    """


_ClientListBonusPaymentsResponseBonusPaymentsTypeDef = TypedDict(
    "_ClientListBonusPaymentsResponseBonusPaymentsTypeDef",
    {
        "WorkerId": str,
        "BonusAmount": str,
        "AssignmentId": str,
        "Reason": str,
        "GrantTime": datetime,
    },
    total=False,
)


class ClientListBonusPaymentsResponseBonusPaymentsTypeDef(
    _ClientListBonusPaymentsResponseBonusPaymentsTypeDef
):
    """
    Type definition for `ClientListBonusPaymentsResponse` `BonusPayments`

    An object representing a Bonus payment paid to a Worker.

    - **WorkerId** *(string) --*

      The ID of the Worker to whom the bonus was paid.

    - **BonusAmount** *(string) --*

      A string representing a currency amount.

    - **AssignmentId** *(string) --*

      The ID of the assignment associated with this bonus payment.

    - **Reason** *(string) --*

      The Reason text given when the bonus was granted, if any.

    - **GrantTime** *(datetime) --*

      The date and time of when the bonus was granted.
    """


_ClientListBonusPaymentsResponseTypeDef = TypedDict(
    "_ClientListBonusPaymentsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "BonusPayments": List[ClientListBonusPaymentsResponseBonusPaymentsTypeDef],
    },
    total=False,
)


class ClientListBonusPaymentsResponseTypeDef(_ClientListBonusPaymentsResponseTypeDef):
    """
    Type definition for `ClientListBonusPayments` `Response`

    - **NumResults** *(integer) --*

      The number of bonus payments on this page in the filtered results list, equivalent to the
      number of bonus payments being returned by this call.

    - **NextToken** *(string) --*

      If the previous response was incomplete (because there is more data to retrieve), Amazon
      Mechanical Turk returns a pagination token in the response. You can use this pagination token
      to retrieve the next set of results.

    - **BonusPayments** *(list) --*

      A successful request to the ListBonusPayments operation returns a list of BonusPayment
      objects.

      - *(dict) --*

        An object representing a Bonus payment paid to a Worker.

        - **WorkerId** *(string) --*

          The ID of the Worker to whom the bonus was paid.

        - **BonusAmount** *(string) --*

          A string representing a currency amount.

        - **AssignmentId** *(string) --*

          The ID of the assignment associated with this bonus payment.

        - **Reason** *(string) --*

          The Reason text given when the bonus was granted, if any.

        - **GrantTime** *(datetime) --*

          The date and time of when the bonus was granted.
    """


_ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef(
    _ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef
):
    """
    Type definition for `ClientListHitsForQualificationTypeResponseHITsQualificationRequirements` `LocaleValues`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --*

      The country of the locale. Must be a valid ISO 3166 country code. For example,
      the code US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
      example, the code WA refers to the state of Washington.
    """


_ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "_ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": str,
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": str,
    },
    total=False,
)


class ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef(
    _ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef
):
    """
    Type definition for `ClientListHitsForQualificationTypeResponseHITs` `QualificationRequirements`

    The QualificationRequirement data structure describes a Qualification that a Worker
    must have before the Worker is allowed to accept a HIT. A requirement may optionally
    state that a Worker must have the Qualification in order to preview the HIT, or see the
    HIT in search results.

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type for the requirement.

    - **Comparator** *(string) --*

      The kind of comparison to make against a Qualification's value. You can compare a
      Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
      GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
      compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
      You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
      values. Lastly, a Qualification requirement can also test if a Qualification Exists
      or DoesNotExist in the user's profile, regardless of its value.

    - **IntegerValues** *(list) --*

      The integer value to compare against the Qualification's value. IntegerValue must not
      be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
      the Qualification type has an integer value; it cannot be used with the Worker_Locale
      QualificationType ID. When performing a set comparison by using the In or the NotIn
      comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
      data structure.

      - *(integer) --*

    - **LocaleValues** *(list) --*

      The locale value to compare against the Qualification's value. The local value must
      be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
      only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
      with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
      LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
      a set comparison by using the In or the NotIn comparator, you can use up to 30
      LocaleValue elements in a QualificationRequirement data structure.

      - *(dict) --*

        The Locale data structure represents a geographical region or location.

        - **Country** *(string) --*

          The country of the locale. Must be a valid ISO 3166 country code. For example,
          the code US refers to the United States of America.

        - **Subdivision** *(string) --*

          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
          example, the code WA refers to the state of Washington.

    - **RequiredToPreview** *(boolean) --*

      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
      the question data for the HIT will not be shown when a Worker whose Qualifications do
      not meet this requirement tries to preview the HIT. That is, a Worker's
      Qualifications must meet all of the requirements for which RequiredToPreview is true
      in order to preview the HIT. If a Worker meets all of the requirements where
      RequiredToPreview is true (or if there are no such requirements), but does not meet
      all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
      question data, but will not be allowed to accept and complete the HIT. The default is
      false. This should not be used in combination with the ``ActionsGuarded`` field.

    - **ActionsGuarded** *(string) --*

      Setting this attribute prevents Workers whose Qualifications do not meet this
      QualificationRequirement from taking the specified action. Valid arguments include
      "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
      search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
      see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
      accept, preview, or see the HIT in their search results). It's possible for you to
      create a HIT with multiple QualificationRequirements (which can have different values
      for the ActionGuarded attribute). In this case, the Worker is only permitted to
      perform an action when they have met all QualificationRequirements guarding the
      action. The actions in the order of least restrictive to most restrictive are
      Discover, Preview and Accept. For example, if a Worker meets all
      QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
      all requirements that are set with PreviewAndAccept, then the Worker will be able to
      Discover, i.e. see the HIT in their search result, but will not be able to Preview or
      Accept the HIT. ActionsGuarded should not be used in combination with the
      ``RequiredToPreview`` field.
    """


_ClientListHitsForQualificationTypeResponseHITsTypeDef = TypedDict(
    "_ClientListHitsForQualificationTypeResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": str,
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": str,
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientListHitsForQualificationTypeResponseHITsTypeDef(
    _ClientListHitsForQualificationTypeResponseHITsTypeDef
):
    """
    Type definition for `ClientListHitsForQualificationTypeResponse` `HITs`

    The HIT data structure represents a single HIT, including all the information necessary for
    a Worker to accept and complete the HIT.

    - **HITId** *(string) --*

      A unique identifier for the HIT.

    - **HITTypeId** *(string) --*

      The ID of the HIT type of this HIT

    - **HITGroupId** *(string) --*

      The ID of the HIT Group of this HIT.

    - **HITLayoutId** *(string) --*

      The ID of the HIT Layout of this HIT.

    - **CreationTime** *(datetime) --*

      The date and time the HIT was created.

    - **Title** *(string) --*

      The title of the HIT.

    - **Description** *(string) --*

      A general description of the HIT.

    - **Question** *(string) --*

      The data the Worker completing the HIT uses produce the results. This is either either a
      QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

    - **Keywords** *(string) --*

      One or more words or phrases that describe the HIT, separated by commas. Search terms
      similar to the keywords of a HIT are more likely to have the HIT in the search results.

    - **HITStatus** *(string) --*

      The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
      Reviewable | Reviewing | Disposed.

    - **MaxAssignments** *(integer) --*

      The number of times the HIT can be accepted and completed before the HIT becomes
      unavailable.

    - **Reward** *(string) --*

      A string representing a currency amount.

    - **AutoApprovalDelayInSeconds** *(integer) --*

      The amount of time, in seconds, after the Worker submits an assignment for the HIT that
      the results are automatically approved by Amazon Mechanical Turk. This is the amount of
      time the Requester has to reject an assignment submitted by a Worker before the
      assignment is auto-approved and the Worker is paid.

    - **Expiration** *(datetime) --*

      The date and time the HIT expires.

    - **AssignmentDurationInSeconds** *(integer) --*

      The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

    - **RequesterAnnotation** *(string) --*

      An arbitrary data field the Requester who created the HIT can use. This field is visible
      only to the creator of the HIT.

    - **QualificationRequirements** *(list) --*

      Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
      have between zero and ten Qualification requirements. All requirements must be met in
      order for a Worker to accept the HIT. Additionally, other actions can be restricted using
      the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

      - *(dict) --*

        The QualificationRequirement data structure describes a Qualification that a Worker
        must have before the Worker is allowed to accept a HIT. A requirement may optionally
        state that a Worker must have the Qualification in order to preview the HIT, or see the
        HIT in search results.

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type for the requirement.

        - **Comparator** *(string) --*

          The kind of comparison to make against a Qualification's value. You can compare a
          Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
          GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
          compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
          You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
          values. Lastly, a Qualification requirement can also test if a Qualification Exists
          or DoesNotExist in the user's profile, regardless of its value.

        - **IntegerValues** *(list) --*

          The integer value to compare against the Qualification's value. IntegerValue must not
          be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
          the Qualification type has an integer value; it cannot be used with the Worker_Locale
          QualificationType ID. When performing a set comparison by using the In or the NotIn
          comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
          data structure.

          - *(integer) --*

        - **LocaleValues** *(list) --*

          The locale value to compare against the Qualification's value. The local value must
          be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
          only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
          with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
          LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
          a set comparison by using the In or the NotIn comparator, you can use up to 30
          LocaleValue elements in a QualificationRequirement data structure.

          - *(dict) --*

            The Locale data structure represents a geographical region or location.

            - **Country** *(string) --*

              The country of the locale. Must be a valid ISO 3166 country code. For example,
              the code US refers to the United States of America.

            - **Subdivision** *(string) --*

              The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
              example, the code WA refers to the state of Washington.

        - **RequiredToPreview** *(boolean) --*

          DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
          the question data for the HIT will not be shown when a Worker whose Qualifications do
          not meet this requirement tries to preview the HIT. That is, a Worker's
          Qualifications must meet all of the requirements for which RequiredToPreview is true
          in order to preview the HIT. If a Worker meets all of the requirements where
          RequiredToPreview is true (or if there are no such requirements), but does not meet
          all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
          question data, but will not be allowed to accept and complete the HIT. The default is
          false. This should not be used in combination with the ``ActionsGuarded`` field.

        - **ActionsGuarded** *(string) --*

          Setting this attribute prevents Workers whose Qualifications do not meet this
          QualificationRequirement from taking the specified action. Valid arguments include
          "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
          search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
          see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
          accept, preview, or see the HIT in their search results). It's possible for you to
          create a HIT with multiple QualificationRequirements (which can have different values
          for the ActionGuarded attribute). In this case, the Worker is only permitted to
          perform an action when they have met all QualificationRequirements guarding the
          action. The actions in the order of least restrictive to most restrictive are
          Discover, Preview and Accept. For example, if a Worker meets all
          QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
          all requirements that are set with PreviewAndAccept, then the Worker will be able to
          Discover, i.e. see the HIT in their search result, but will not be able to Preview or
          Accept the HIT. ActionsGuarded should not be used in combination with the
          ``RequiredToPreview`` field.

    - **HITReviewStatus** *(string) --*

      Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
      ReviewedAppropriate | ReviewedInappropriate.

    - **NumberOfAssignmentsPending** *(integer) --*

      The number of assignments for this HIT that are being previewed or have been accepted by
      Workers, but have not yet been submitted, returned, or abandoned.

    - **NumberOfAssignmentsAvailable** *(integer) --*

      The number of assignments for this HIT that are available for Workers to accept.

    - **NumberOfAssignmentsCompleted** *(integer) --*

      The number of assignments for this HIT that have been approved or rejected.
    """


_ClientListHitsForQualificationTypeResponseTypeDef = TypedDict(
    "_ClientListHitsForQualificationTypeResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List[ClientListHitsForQualificationTypeResponseHITsTypeDef],
    },
    total=False,
)


class ClientListHitsForQualificationTypeResponseTypeDef(
    _ClientListHitsForQualificationTypeResponseTypeDef
):
    """
    Type definition for `ClientListHitsForQualificationType` `Response`

    - **NextToken** *(string) --*

      If the previous response was incomplete (because there is more data to retrieve), Amazon
      Mechanical Turk returns a pagination token in the response. You can use this pagination token
      to retrieve the next set of results.

    - **NumResults** *(integer) --*

      The number of HITs on this page in the filtered results list, equivalent to the number of
      HITs being returned by this call.

    - **HITs** *(list) --*

      The list of HIT elements returned by the query.

      - *(dict) --*

        The HIT data structure represents a single HIT, including all the information necessary for
        a Worker to accept and complete the HIT.

        - **HITId** *(string) --*

          A unique identifier for the HIT.

        - **HITTypeId** *(string) --*

          The ID of the HIT type of this HIT

        - **HITGroupId** *(string) --*

          The ID of the HIT Group of this HIT.

        - **HITLayoutId** *(string) --*

          The ID of the HIT Layout of this HIT.

        - **CreationTime** *(datetime) --*

          The date and time the HIT was created.

        - **Title** *(string) --*

          The title of the HIT.

        - **Description** *(string) --*

          A general description of the HIT.

        - **Question** *(string) --*

          The data the Worker completing the HIT uses produce the results. This is either either a
          QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

        - **Keywords** *(string) --*

          One or more words or phrases that describe the HIT, separated by commas. Search terms
          similar to the keywords of a HIT are more likely to have the HIT in the search results.

        - **HITStatus** *(string) --*

          The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
          Reviewable | Reviewing | Disposed.

        - **MaxAssignments** *(integer) --*

          The number of times the HIT can be accepted and completed before the HIT becomes
          unavailable.

        - **Reward** *(string) --*

          A string representing a currency amount.

        - **AutoApprovalDelayInSeconds** *(integer) --*

          The amount of time, in seconds, after the Worker submits an assignment for the HIT that
          the results are automatically approved by Amazon Mechanical Turk. This is the amount of
          time the Requester has to reject an assignment submitted by a Worker before the
          assignment is auto-approved and the Worker is paid.

        - **Expiration** *(datetime) --*

          The date and time the HIT expires.

        - **AssignmentDurationInSeconds** *(integer) --*

          The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

        - **RequesterAnnotation** *(string) --*

          An arbitrary data field the Requester who created the HIT can use. This field is visible
          only to the creator of the HIT.

        - **QualificationRequirements** *(list) --*

          Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
          have between zero and ten Qualification requirements. All requirements must be met in
          order for a Worker to accept the HIT. Additionally, other actions can be restricted using
          the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

          - *(dict) --*

            The QualificationRequirement data structure describes a Qualification that a Worker
            must have before the Worker is allowed to accept a HIT. A requirement may optionally
            state that a Worker must have the Qualification in order to preview the HIT, or see the
            HIT in search results.

            - **QualificationTypeId** *(string) --*

              The ID of the Qualification type for the requirement.

            - **Comparator** *(string) --*

              The kind of comparison to make against a Qualification's value. You can compare a
              Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
              GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
              compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
              You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
              values. Lastly, a Qualification requirement can also test if a Qualification Exists
              or DoesNotExist in the user's profile, regardless of its value.

            - **IntegerValues** *(list) --*

              The integer value to compare against the Qualification's value. IntegerValue must not
              be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
              the Qualification type has an integer value; it cannot be used with the Worker_Locale
              QualificationType ID. When performing a set comparison by using the In or the NotIn
              comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
              data structure.

              - *(integer) --*

            - **LocaleValues** *(list) --*

              The locale value to compare against the Qualification's value. The local value must
              be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
              only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
              with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
              LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
              a set comparison by using the In or the NotIn comparator, you can use up to 30
              LocaleValue elements in a QualificationRequirement data structure.

              - *(dict) --*

                The Locale data structure represents a geographical region or location.

                - **Country** *(string) --*

                  The country of the locale. Must be a valid ISO 3166 country code. For example,
                  the code US refers to the United States of America.

                - **Subdivision** *(string) --*

                  The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
                  example, the code WA refers to the state of Washington.

            - **RequiredToPreview** *(boolean) --*

              DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
              the question data for the HIT will not be shown when a Worker whose Qualifications do
              not meet this requirement tries to preview the HIT. That is, a Worker's
              Qualifications must meet all of the requirements for which RequiredToPreview is true
              in order to preview the HIT. If a Worker meets all of the requirements where
              RequiredToPreview is true (or if there are no such requirements), but does not meet
              all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
              question data, but will not be allowed to accept and complete the HIT. The default is
              false. This should not be used in combination with the ``ActionsGuarded`` field.

            - **ActionsGuarded** *(string) --*

              Setting this attribute prevents Workers whose Qualifications do not meet this
              QualificationRequirement from taking the specified action. Valid arguments include
              "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
              search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
              see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
              accept, preview, or see the HIT in their search results). It's possible for you to
              create a HIT with multiple QualificationRequirements (which can have different values
              for the ActionGuarded attribute). In this case, the Worker is only permitted to
              perform an action when they have met all QualificationRequirements guarding the
              action. The actions in the order of least restrictive to most restrictive are
              Discover, Preview and Accept. For example, if a Worker meets all
              QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
              all requirements that are set with PreviewAndAccept, then the Worker will be able to
              Discover, i.e. see the HIT in their search result, but will not be able to Preview or
              Accept the HIT. ActionsGuarded should not be used in combination with the
              ``RequiredToPreview`` field.

        - **HITReviewStatus** *(string) --*

          Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
          ReviewedAppropriate | ReviewedInappropriate.

        - **NumberOfAssignmentsPending** *(integer) --*

          The number of assignments for this HIT that are being previewed or have been accepted by
          Workers, but have not yet been submitted, returned, or abandoned.

        - **NumberOfAssignmentsAvailable** *(integer) --*

          The number of assignments for this HIT that are available for Workers to accept.

        - **NumberOfAssignmentsCompleted** *(integer) --*

          The number of assignments for this HIT that have been approved or rejected.
    """


_ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef(
    _ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef
):
    """
    Type definition for `ClientListHitsResponseHITsQualificationRequirements` `LocaleValues`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --*

      The country of the locale. Must be a valid ISO 3166 country code. For example,
      the code US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
      example, the code WA refers to the state of Washington.
    """


_ClientListHitsResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "_ClientListHitsResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": str,
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": str,
    },
    total=False,
)


class ClientListHitsResponseHITsQualificationRequirementsTypeDef(
    _ClientListHitsResponseHITsQualificationRequirementsTypeDef
):
    """
    Type definition for `ClientListHitsResponseHITs` `QualificationRequirements`

    The QualificationRequirement data structure describes a Qualification that a Worker
    must have before the Worker is allowed to accept a HIT. A requirement may optionally
    state that a Worker must have the Qualification in order to preview the HIT, or see the
    HIT in search results.

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type for the requirement.

    - **Comparator** *(string) --*

      The kind of comparison to make against a Qualification's value. You can compare a
      Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
      GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
      compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
      You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
      values. Lastly, a Qualification requirement can also test if a Qualification Exists
      or DoesNotExist in the user's profile, regardless of its value.

    - **IntegerValues** *(list) --*

      The integer value to compare against the Qualification's value. IntegerValue must not
      be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
      the Qualification type has an integer value; it cannot be used with the Worker_Locale
      QualificationType ID. When performing a set comparison by using the In or the NotIn
      comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
      data structure.

      - *(integer) --*

    - **LocaleValues** *(list) --*

      The locale value to compare against the Qualification's value. The local value must
      be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
      only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
      with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
      LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
      a set comparison by using the In or the NotIn comparator, you can use up to 30
      LocaleValue elements in a QualificationRequirement data structure.

      - *(dict) --*

        The Locale data structure represents a geographical region or location.

        - **Country** *(string) --*

          The country of the locale. Must be a valid ISO 3166 country code. For example,
          the code US refers to the United States of America.

        - **Subdivision** *(string) --*

          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
          example, the code WA refers to the state of Washington.

    - **RequiredToPreview** *(boolean) --*

      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
      the question data for the HIT will not be shown when a Worker whose Qualifications do
      not meet this requirement tries to preview the HIT. That is, a Worker's
      Qualifications must meet all of the requirements for which RequiredToPreview is true
      in order to preview the HIT. If a Worker meets all of the requirements where
      RequiredToPreview is true (or if there are no such requirements), but does not meet
      all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
      question data, but will not be allowed to accept and complete the HIT. The default is
      false. This should not be used in combination with the ``ActionsGuarded`` field.

    - **ActionsGuarded** *(string) --*

      Setting this attribute prevents Workers whose Qualifications do not meet this
      QualificationRequirement from taking the specified action. Valid arguments include
      "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
      search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
      see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
      accept, preview, or see the HIT in their search results). It's possible for you to
      create a HIT with multiple QualificationRequirements (which can have different values
      for the ActionGuarded attribute). In this case, the Worker is only permitted to
      perform an action when they have met all QualificationRequirements guarding the
      action. The actions in the order of least restrictive to most restrictive are
      Discover, Preview and Accept. For example, if a Worker meets all
      QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
      all requirements that are set with PreviewAndAccept, then the Worker will be able to
      Discover, i.e. see the HIT in their search result, but will not be able to Preview or
      Accept the HIT. ActionsGuarded should not be used in combination with the
      ``RequiredToPreview`` field.
    """


_ClientListHitsResponseHITsTypeDef = TypedDict(
    "_ClientListHitsResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": str,
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientListHitsResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": str,
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientListHitsResponseHITsTypeDef(_ClientListHitsResponseHITsTypeDef):
    """
    Type definition for `ClientListHitsResponse` `HITs`

    The HIT data structure represents a single HIT, including all the information necessary for
    a Worker to accept and complete the HIT.

    - **HITId** *(string) --*

      A unique identifier for the HIT.

    - **HITTypeId** *(string) --*

      The ID of the HIT type of this HIT

    - **HITGroupId** *(string) --*

      The ID of the HIT Group of this HIT.

    - **HITLayoutId** *(string) --*

      The ID of the HIT Layout of this HIT.

    - **CreationTime** *(datetime) --*

      The date and time the HIT was created.

    - **Title** *(string) --*

      The title of the HIT.

    - **Description** *(string) --*

      A general description of the HIT.

    - **Question** *(string) --*

      The data the Worker completing the HIT uses produce the results. This is either either a
      QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

    - **Keywords** *(string) --*

      One or more words or phrases that describe the HIT, separated by commas. Search terms
      similar to the keywords of a HIT are more likely to have the HIT in the search results.

    - **HITStatus** *(string) --*

      The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
      Reviewable | Reviewing | Disposed.

    - **MaxAssignments** *(integer) --*

      The number of times the HIT can be accepted and completed before the HIT becomes
      unavailable.

    - **Reward** *(string) --*

      A string representing a currency amount.

    - **AutoApprovalDelayInSeconds** *(integer) --*

      The amount of time, in seconds, after the Worker submits an assignment for the HIT that
      the results are automatically approved by Amazon Mechanical Turk. This is the amount of
      time the Requester has to reject an assignment submitted by a Worker before the
      assignment is auto-approved and the Worker is paid.

    - **Expiration** *(datetime) --*

      The date and time the HIT expires.

    - **AssignmentDurationInSeconds** *(integer) --*

      The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

    - **RequesterAnnotation** *(string) --*

      An arbitrary data field the Requester who created the HIT can use. This field is visible
      only to the creator of the HIT.

    - **QualificationRequirements** *(list) --*

      Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
      have between zero and ten Qualification requirements. All requirements must be met in
      order for a Worker to accept the HIT. Additionally, other actions can be restricted using
      the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

      - *(dict) --*

        The QualificationRequirement data structure describes a Qualification that a Worker
        must have before the Worker is allowed to accept a HIT. A requirement may optionally
        state that a Worker must have the Qualification in order to preview the HIT, or see the
        HIT in search results.

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type for the requirement.

        - **Comparator** *(string) --*

          The kind of comparison to make against a Qualification's value. You can compare a
          Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
          GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
          compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
          You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
          values. Lastly, a Qualification requirement can also test if a Qualification Exists
          or DoesNotExist in the user's profile, regardless of its value.

        - **IntegerValues** *(list) --*

          The integer value to compare against the Qualification's value. IntegerValue must not
          be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
          the Qualification type has an integer value; it cannot be used with the Worker_Locale
          QualificationType ID. When performing a set comparison by using the In or the NotIn
          comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
          data structure.

          - *(integer) --*

        - **LocaleValues** *(list) --*

          The locale value to compare against the Qualification's value. The local value must
          be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
          only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
          with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
          LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
          a set comparison by using the In or the NotIn comparator, you can use up to 30
          LocaleValue elements in a QualificationRequirement data structure.

          - *(dict) --*

            The Locale data structure represents a geographical region or location.

            - **Country** *(string) --*

              The country of the locale. Must be a valid ISO 3166 country code. For example,
              the code US refers to the United States of America.

            - **Subdivision** *(string) --*

              The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
              example, the code WA refers to the state of Washington.

        - **RequiredToPreview** *(boolean) --*

          DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
          the question data for the HIT will not be shown when a Worker whose Qualifications do
          not meet this requirement tries to preview the HIT. That is, a Worker's
          Qualifications must meet all of the requirements for which RequiredToPreview is true
          in order to preview the HIT. If a Worker meets all of the requirements where
          RequiredToPreview is true (or if there are no such requirements), but does not meet
          all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
          question data, but will not be allowed to accept and complete the HIT. The default is
          false. This should not be used in combination with the ``ActionsGuarded`` field.

        - **ActionsGuarded** *(string) --*

          Setting this attribute prevents Workers whose Qualifications do not meet this
          QualificationRequirement from taking the specified action. Valid arguments include
          "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
          search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
          see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
          accept, preview, or see the HIT in their search results). It's possible for you to
          create a HIT with multiple QualificationRequirements (which can have different values
          for the ActionGuarded attribute). In this case, the Worker is only permitted to
          perform an action when they have met all QualificationRequirements guarding the
          action. The actions in the order of least restrictive to most restrictive are
          Discover, Preview and Accept. For example, if a Worker meets all
          QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
          all requirements that are set with PreviewAndAccept, then the Worker will be able to
          Discover, i.e. see the HIT in their search result, but will not be able to Preview or
          Accept the HIT. ActionsGuarded should not be used in combination with the
          ``RequiredToPreview`` field.

    - **HITReviewStatus** *(string) --*

      Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
      ReviewedAppropriate | ReviewedInappropriate.

    - **NumberOfAssignmentsPending** *(integer) --*

      The number of assignments for this HIT that are being previewed or have been accepted by
      Workers, but have not yet been submitted, returned, or abandoned.

    - **NumberOfAssignmentsAvailable** *(integer) --*

      The number of assignments for this HIT that are available for Workers to accept.

    - **NumberOfAssignmentsCompleted** *(integer) --*

      The number of assignments for this HIT that have been approved or rejected.
    """


_ClientListHitsResponseTypeDef = TypedDict(
    "_ClientListHitsResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List[ClientListHitsResponseHITsTypeDef],
    },
    total=False,
)


class ClientListHitsResponseTypeDef(_ClientListHitsResponseTypeDef):
    """
    Type definition for `ClientListHits` `Response`

    - **NextToken** *(string) --*

      If the previous response was incomplete (because there is more data to retrieve), Amazon
      Mechanical Turk returns a pagination token in the response. You can use this pagination token
      to retrieve the next set of results.

    - **NumResults** *(integer) --*

      The number of HITs on this page in the filtered results list, equivalent to the number of
      HITs being returned by this call.

    - **HITs** *(list) --*

      The list of HIT elements returned by the query.

      - *(dict) --*

        The HIT data structure represents a single HIT, including all the information necessary for
        a Worker to accept and complete the HIT.

        - **HITId** *(string) --*

          A unique identifier for the HIT.

        - **HITTypeId** *(string) --*

          The ID of the HIT type of this HIT

        - **HITGroupId** *(string) --*

          The ID of the HIT Group of this HIT.

        - **HITLayoutId** *(string) --*

          The ID of the HIT Layout of this HIT.

        - **CreationTime** *(datetime) --*

          The date and time the HIT was created.

        - **Title** *(string) --*

          The title of the HIT.

        - **Description** *(string) --*

          A general description of the HIT.

        - **Question** *(string) --*

          The data the Worker completing the HIT uses produce the results. This is either either a
          QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

        - **Keywords** *(string) --*

          One or more words or phrases that describe the HIT, separated by commas. Search terms
          similar to the keywords of a HIT are more likely to have the HIT in the search results.

        - **HITStatus** *(string) --*

          The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
          Reviewable | Reviewing | Disposed.

        - **MaxAssignments** *(integer) --*

          The number of times the HIT can be accepted and completed before the HIT becomes
          unavailable.

        - **Reward** *(string) --*

          A string representing a currency amount.

        - **AutoApprovalDelayInSeconds** *(integer) --*

          The amount of time, in seconds, after the Worker submits an assignment for the HIT that
          the results are automatically approved by Amazon Mechanical Turk. This is the amount of
          time the Requester has to reject an assignment submitted by a Worker before the
          assignment is auto-approved and the Worker is paid.

        - **Expiration** *(datetime) --*

          The date and time the HIT expires.

        - **AssignmentDurationInSeconds** *(integer) --*

          The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

        - **RequesterAnnotation** *(string) --*

          An arbitrary data field the Requester who created the HIT can use. This field is visible
          only to the creator of the HIT.

        - **QualificationRequirements** *(list) --*

          Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
          have between zero and ten Qualification requirements. All requirements must be met in
          order for a Worker to accept the HIT. Additionally, other actions can be restricted using
          the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

          - *(dict) --*

            The QualificationRequirement data structure describes a Qualification that a Worker
            must have before the Worker is allowed to accept a HIT. A requirement may optionally
            state that a Worker must have the Qualification in order to preview the HIT, or see the
            HIT in search results.

            - **QualificationTypeId** *(string) --*

              The ID of the Qualification type for the requirement.

            - **Comparator** *(string) --*

              The kind of comparison to make against a Qualification's value. You can compare a
              Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
              GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
              compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
              You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
              values. Lastly, a Qualification requirement can also test if a Qualification Exists
              or DoesNotExist in the user's profile, regardless of its value.

            - **IntegerValues** *(list) --*

              The integer value to compare against the Qualification's value. IntegerValue must not
              be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
              the Qualification type has an integer value; it cannot be used with the Worker_Locale
              QualificationType ID. When performing a set comparison by using the In or the NotIn
              comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
              data structure.

              - *(integer) --*

            - **LocaleValues** *(list) --*

              The locale value to compare against the Qualification's value. The local value must
              be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
              only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
              with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
              LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
              a set comparison by using the In or the NotIn comparator, you can use up to 30
              LocaleValue elements in a QualificationRequirement data structure.

              - *(dict) --*

                The Locale data structure represents a geographical region or location.

                - **Country** *(string) --*

                  The country of the locale. Must be a valid ISO 3166 country code. For example,
                  the code US refers to the United States of America.

                - **Subdivision** *(string) --*

                  The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
                  example, the code WA refers to the state of Washington.

            - **RequiredToPreview** *(boolean) --*

              DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
              the question data for the HIT will not be shown when a Worker whose Qualifications do
              not meet this requirement tries to preview the HIT. That is, a Worker's
              Qualifications must meet all of the requirements for which RequiredToPreview is true
              in order to preview the HIT. If a Worker meets all of the requirements where
              RequiredToPreview is true (or if there are no such requirements), but does not meet
              all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
              question data, but will not be allowed to accept and complete the HIT. The default is
              false. This should not be used in combination with the ``ActionsGuarded`` field.

            - **ActionsGuarded** *(string) --*

              Setting this attribute prevents Workers whose Qualifications do not meet this
              QualificationRequirement from taking the specified action. Valid arguments include
              "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
              search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
              see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
              accept, preview, or see the HIT in their search results). It's possible for you to
              create a HIT with multiple QualificationRequirements (which can have different values
              for the ActionGuarded attribute). In this case, the Worker is only permitted to
              perform an action when they have met all QualificationRequirements guarding the
              action. The actions in the order of least restrictive to most restrictive are
              Discover, Preview and Accept. For example, if a Worker meets all
              QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
              all requirements that are set with PreviewAndAccept, then the Worker will be able to
              Discover, i.e. see the HIT in their search result, but will not be able to Preview or
              Accept the HIT. ActionsGuarded should not be used in combination with the
              ``RequiredToPreview`` field.

        - **HITReviewStatus** *(string) --*

          Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
          ReviewedAppropriate | ReviewedInappropriate.

        - **NumberOfAssignmentsPending** *(integer) --*

          The number of assignments for this HIT that are being previewed or have been accepted by
          Workers, but have not yet been submitted, returned, or abandoned.

        - **NumberOfAssignmentsAvailable** *(integer) --*

          The number of assignments for this HIT that are available for Workers to accept.

        - **NumberOfAssignmentsCompleted** *(integer) --*

          The number of assignments for this HIT that have been approved or rejected.
    """


_ClientListQualificationRequestsResponseQualificationRequestsTypeDef = TypedDict(
    "_ClientListQualificationRequestsResponseQualificationRequestsTypeDef",
    {
        "QualificationRequestId": str,
        "QualificationTypeId": str,
        "WorkerId": str,
        "Test": str,
        "Answer": str,
        "SubmitTime": datetime,
    },
    total=False,
)


class ClientListQualificationRequestsResponseQualificationRequestsTypeDef(
    _ClientListQualificationRequestsResponseQualificationRequestsTypeDef
):
    """
    Type definition for `ClientListQualificationRequestsResponse` `QualificationRequests`

    The QualificationRequest data structure represents a request a Worker has made for a
    Qualification.

    - **QualificationRequestId** *(string) --*

      The ID of the Qualification request, a unique identifier generated when the request was
      submitted.

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type the Worker is requesting, as returned by the
      CreateQualificationType operation.

    - **WorkerId** *(string) --*

      The ID of the Worker requesting the Qualification.

    - **Test** *(string) --*

      The contents of the Qualification test that was presented to the Worker, if the type has
      a test and the Worker has submitted answers. This value is identical to the QuestionForm
      associated with the Qualification type at the time the Worker requests the Qualification.

    - **Answer** *(string) --*

      The Worker's answers for the Qualification type's test contained in a QuestionFormAnswers
      document, if the type has a test and the Worker has submitted answers. If the Worker does
      not provide any answers, Answer may be empty.

    - **SubmitTime** *(datetime) --*

      The date and time the Qualification request had a status of Submitted. This is either the
      time the Worker submitted answers for a Qualification test, or the time the Worker
      requested the Qualification if the Qualification type does not have a test.
    """


_ClientListQualificationRequestsResponseTypeDef = TypedDict(
    "_ClientListQualificationRequestsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationRequests": List[
            ClientListQualificationRequestsResponseQualificationRequestsTypeDef
        ],
    },
    total=False,
)


class ClientListQualificationRequestsResponseTypeDef(
    _ClientListQualificationRequestsResponseTypeDef
):
    """
    Type definition for `ClientListQualificationRequests` `Response`

    - **NumResults** *(integer) --*

      The number of Qualification requests on this page in the filtered results list, equivalent to
      the number of Qualification requests being returned by this call.

    - **NextToken** *(string) --*

      If the previous response was incomplete (because there is more data to retrieve), Amazon
      Mechanical Turk returns a pagination token in the response. You can use this pagination token
      to retrieve the next set of results.

    - **QualificationRequests** *(list) --*

      The Qualification request. The response includes one QualificationRequest element for each
      Qualification request returned by the query.

      - *(dict) --*

        The QualificationRequest data structure represents a request a Worker has made for a
        Qualification.

        - **QualificationRequestId** *(string) --*

          The ID of the Qualification request, a unique identifier generated when the request was
          submitted.

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type the Worker is requesting, as returned by the
          CreateQualificationType operation.

        - **WorkerId** *(string) --*

          The ID of the Worker requesting the Qualification.

        - **Test** *(string) --*

          The contents of the Qualification test that was presented to the Worker, if the type has
          a test and the Worker has submitted answers. This value is identical to the QuestionForm
          associated with the Qualification type at the time the Worker requests the Qualification.

        - **Answer** *(string) --*

          The Worker's answers for the Qualification type's test contained in a QuestionFormAnswers
          document, if the type has a test and the Worker has submitted answers. If the Worker does
          not provide any answers, Answer may be empty.

        - **SubmitTime** *(datetime) --*

          The date and time the Qualification request had a status of Submitted. This is either the
          time the Worker submitted answers for a Qualification test, or the time the Worker
          requested the Qualification if the Qualification type does not have a test.
    """


_ClientListQualificationTypesResponseQualificationTypesTypeDef = TypedDict(
    "_ClientListQualificationTypesResponseQualificationTypesTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": str,
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)


class ClientListQualificationTypesResponseQualificationTypesTypeDef(
    _ClientListQualificationTypesResponseQualificationTypesTypeDef
):
    """
    Type definition for `ClientListQualificationTypesResponse` `QualificationTypes`

    The QualificationType data structure represents a Qualification type, a description of a
    property of a Worker that must match the requirements of a HIT for the Worker to be able to
    accept the HIT. The type also describes how a Worker can obtain a Qualification of that
    type, such as through a Qualification test.

    - **QualificationTypeId** *(string) --*

      A unique identifier for the Qualification type. A Qualification type is given a
      Qualification type ID when you call the CreateQualificationType operation.

    - **CreationTime** *(datetime) --*

      The date and time the Qualification type was created.

    - **Name** *(string) --*

      The name of the Qualification type. The type name is used to identify the type, and to
      find the type using a Qualification type search.

    - **Description** *(string) --*

      A long description for the Qualification type.

    - **Keywords** *(string) --*

      One or more words or phrases that describe theQualification type, separated by commas.
      The Keywords make the type easier to find using a search.

    - **QualificationTypeStatus** *(string) --*

      The status of the Qualification type. A Qualification type's status determines if users
      can apply to receive a Qualification of this type, and if HITs can be created with
      requirements based on this type. Valid values are Active | Inactive.

    - **Test** *(string) --*

      The questions for a Qualification test associated with this Qualification type that a
      user can take to obtain a Qualification of this type. This parameter must be specified if
      AnswerKey is present. A Qualification type cannot have both a specified Test parameter
      and an AutoGranted value of true.

    - **TestDurationInSeconds** *(integer) --*

      The amount of time, in seconds, given to a Worker to complete the Qualification test,
      beginning from the time the Worker requests the Qualification.

    - **AnswerKey** *(string) --*

      The answers to the Qualification test specified in the Test parameter.

    - **RetryDelayInSeconds** *(integer) --*

      The amount of time, in seconds, Workers must wait after taking the Qualification test
      before they can take it again. Workers can take a Qualification test multiple times if
      they were not granted the Qualification from a previous attempt, or if the test offers a
      gradient score and they want a better score. If not specified, retries are disabled and
      Workers can request a Qualification only once.

    - **IsRequestable** *(boolean) --*

      Specifies whether the Qualification type is one that a user can request through the
      Amazon Mechanical Turk web site, such as by taking a Qualification test. This value is
      False for Qualifications assigned automatically by the system. Valid values are True |
      False.

    - **AutoGranted** *(boolean) --*

      Specifies that requests for the Qualification type are granted immediately, without
      prompting the Worker with a Qualification test. Valid values are True | False.

    - **AutoGrantedValue** *(integer) --*

      The Qualification integer value to use for automatically granted Qualifications, if
      AutoGranted is true. This is 1 by default.
    """


_ClientListQualificationTypesResponseTypeDef = TypedDict(
    "_ClientListQualificationTypesResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationTypes": List[
            ClientListQualificationTypesResponseQualificationTypesTypeDef
        ],
    },
    total=False,
)


class ClientListQualificationTypesResponseTypeDef(
    _ClientListQualificationTypesResponseTypeDef
):
    """
    Type definition for `ClientListQualificationTypes` `Response`

    - **NumResults** *(integer) --*

      The number of Qualification types on this page in the filtered results list, equivalent to
      the number of types this operation returns.

    - **NextToken** *(string) --*

      If the previous response was incomplete (because there is more data to retrieve), Amazon
      Mechanical Turk returns a pagination token in the response. You can use this pagination token
      to retrieve the next set of results.

    - **QualificationTypes** *(list) --*

      The list of QualificationType elements returned by the query.

      - *(dict) --*

        The QualificationType data structure represents a Qualification type, a description of a
        property of a Worker that must match the requirements of a HIT for the Worker to be able to
        accept the HIT. The type also describes how a Worker can obtain a Qualification of that
        type, such as through a Qualification test.

        - **QualificationTypeId** *(string) --*

          A unique identifier for the Qualification type. A Qualification type is given a
          Qualification type ID when you call the CreateQualificationType operation.

        - **CreationTime** *(datetime) --*

          The date and time the Qualification type was created.

        - **Name** *(string) --*

          The name of the Qualification type. The type name is used to identify the type, and to
          find the type using a Qualification type search.

        - **Description** *(string) --*

          A long description for the Qualification type.

        - **Keywords** *(string) --*

          One or more words or phrases that describe theQualification type, separated by commas.
          The Keywords make the type easier to find using a search.

        - **QualificationTypeStatus** *(string) --*

          The status of the Qualification type. A Qualification type's status determines if users
          can apply to receive a Qualification of this type, and if HITs can be created with
          requirements based on this type. Valid values are Active | Inactive.

        - **Test** *(string) --*

          The questions for a Qualification test associated with this Qualification type that a
          user can take to obtain a Qualification of this type. This parameter must be specified if
          AnswerKey is present. A Qualification type cannot have both a specified Test parameter
          and an AutoGranted value of true.

        - **TestDurationInSeconds** *(integer) --*

          The amount of time, in seconds, given to a Worker to complete the Qualification test,
          beginning from the time the Worker requests the Qualification.

        - **AnswerKey** *(string) --*

          The answers to the Qualification test specified in the Test parameter.

        - **RetryDelayInSeconds** *(integer) --*

          The amount of time, in seconds, Workers must wait after taking the Qualification test
          before they can take it again. Workers can take a Qualification test multiple times if
          they were not granted the Qualification from a previous attempt, or if the test offers a
          gradient score and they want a better score. If not specified, retries are disabled and
          Workers can request a Qualification only once.

        - **IsRequestable** *(boolean) --*

          Specifies whether the Qualification type is one that a user can request through the
          Amazon Mechanical Turk web site, such as by taking a Qualification test. This value is
          False for Qualifications assigned automatically by the system. Valid values are True |
          False.

        - **AutoGranted** *(boolean) --*

          Specifies that requests for the Qualification type are granted immediately, without
          prompting the Worker with a Qualification test. Valid values are True | False.

        - **AutoGrantedValue** *(integer) --*

          The Qualification integer value to use for automatically granted Qualifications, if
          AutoGranted is true. This is 1 by default.
    """


_ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef(
    _ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef
):
    """
    Type definition for `ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParameters` `MapEntries`

    This data structure is the data type for the AnswerKey parameter of the
    ScoreMyKnownAnswers/2011-09-01 Review Policy.

    - **Key** *(string) --*

      The QuestionID from the HIT that is used to identify which question requires
      Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review
      Policy.

    - **Values** *(list) --*

      The list of answers to the question specified in the MapEntry Key element. The
      Worker must match all values in order for the answer to be scored correctly.

      - *(string) --*
    """


_ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[
            ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef
        ],
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef(
    _ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef
):
    """
    Type definition for `ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicy` `Parameters`

    Name of the parameter from the Review policy.

    - **Key** *(string) --*

      Name of the parameter from the list of Review Polices.

    - **Values** *(list) --*

      The list of values of the Parameter

      - *(string) --*

    - **MapEntries** *(list) --*

      List of ParameterMapEntry objects.

      - *(dict) --*

        This data structure is the data type for the AnswerKey parameter of the
        ScoreMyKnownAnswers/2011-09-01 Review Policy.

        - **Key** *(string) --*

          The QuestionID from the HIT that is used to identify which question requires
          Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review
          Policy.

        - **Values** *(list) --*

          The list of answers to the question specified in the MapEntry Key element. The
          Worker must match all values in order for the answer to be scored correctly.

          - *(string) --*
    """


_ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef",
    {
        "PolicyName": str,
        "Parameters": List[
            ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef
        ],
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef(
    _ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef
):
    """
    Type definition for `ClientListReviewPolicyResultsForHitResponse` `AssignmentReviewPolicy`

    The name of the Assignment-level Review Policy. This contains only the PolicyName element.

    - **PolicyName** *(string) --*

      Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01

    - **Parameters** *(list) --*

      Name of the parameter from the Review policy.

      - *(dict) --*

        Name of the parameter from the Review policy.

        - **Key** *(string) --*

          Name of the parameter from the list of Review Polices.

        - **Values** *(list) --*

          The list of values of the Parameter

          - *(string) --*

        - **MapEntries** *(list) --*

          List of ParameterMapEntry objects.

          - *(dict) --*

            This data structure is the data type for the AnswerKey parameter of the
            ScoreMyKnownAnswers/2011-09-01 Review Policy.

            - **Key** *(string) --*

              The QuestionID from the HIT that is used to identify which question requires
              Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review
              Policy.

            - **Values** *(list) --*

              The list of answers to the question specified in the MapEntry Key element. The
              Worker must match all values in order for the answer to be scored correctly.

              - *(string) --*
    """


_ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef",
    {
        "ActionId": str,
        "ActionName": str,
        "TargetId": str,
        "TargetType": str,
        "Status": str,
        "CompleteTime": datetime,
        "Result": str,
        "ErrorCode": str,
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef(
    _ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef
):
    """
    Type definition for `ClientListReviewPolicyResultsForHitResponseAssignmentReviewReport` `ReviewActions`

    Both the AssignmentReviewReport and the HITReviewReport elements contains the
    ReviewActionDetail data structure. This structure is returned multiple times for each
    action specified in the Review Policy.

    - **ActionId** *(string) --*

      The unique identifier for the action.

    - **ActionName** *(string) --*

      The nature of the action itself. The Review Policy is responsible for examining the HIT
      and Assignments, emitting results, and deciding which other actions will be necessary.

    - **TargetId** *(string) --*

      The specific HITId or AssignmentID targeted by the action.

    - **TargetType** *(string) --*

      The type of object in TargetId.

    - **Status** *(string) --*

      The current disposition of the action: INTENDED, SUCCEEDED, FAILED, or CANCELLED.

    - **CompleteTime** *(datetime) --*

      The date when the action was completed.

    - **Result** *(string) --*

      A description of the outcome of the review.

    - **ErrorCode** *(string) --*

      Present only when the Results have a FAILED Status.
    """


_ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef",
    {
        "ActionId": str,
        "SubjectId": str,
        "SubjectType": str,
        "QuestionId": str,
        "Key": str,
        "Value": str,
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef(
    _ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef
):
    """
    Type definition for `ClientListReviewPolicyResultsForHitResponseAssignmentReviewReport` `ReviewResults`

    This data structure is returned multiple times for each result specified in the Review
    Policy.

    - **ActionId** *(string) --*

      A unique identifier of the Review action result.

    - **SubjectId** *(string) --*

      The HITID or AssignmentId about which this result was taken. Note that HIT-level Review
      Policies will often emit results about both the HIT itself and its Assignments, while
      Assignment-level review policies generally only emit results about the Assignment
      itself.

    - **SubjectType** *(string) --*

      The type of the object from the SubjectId field.

    - **QuestionId** *(string) --*

      Specifies the QuestionId the result is describing. Depending on whether the TargetType
      is a HIT or Assignment this results could specify multiple values. If TargetType is HIT
      and QuestionId is absent, then the result describes results of the HIT, including the
      HIT agreement score. If ObjectType is Assignment and QuestionId is absent, then the
      result describes the Worker's performance on the HIT.

    - **Key** *(string) --*

      Key identifies the particular piece of reviewed information.

    - **Value** *(string) --*

      The values of Key provided by the review policies you have selected.
    """


_ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef",
    {
        "ReviewResults": List[
            ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef
        ],
        "ReviewActions": List[
            ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef
        ],
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef(
    _ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef
):
    """
    Type definition for `ClientListReviewPolicyResultsForHitResponse` `AssignmentReviewReport`

    Contains both ReviewResult and ReviewAction elements for an Assignment.

    - **ReviewResults** *(list) --*

      A list of ReviewResults objects for each action specified in the Review Policy.

      - *(dict) --*

        This data structure is returned multiple times for each result specified in the Review
        Policy.

        - **ActionId** *(string) --*

          A unique identifier of the Review action result.

        - **SubjectId** *(string) --*

          The HITID or AssignmentId about which this result was taken. Note that HIT-level Review
          Policies will often emit results about both the HIT itself and its Assignments, while
          Assignment-level review policies generally only emit results about the Assignment
          itself.

        - **SubjectType** *(string) --*

          The type of the object from the SubjectId field.

        - **QuestionId** *(string) --*

          Specifies the QuestionId the result is describing. Depending on whether the TargetType
          is a HIT or Assignment this results could specify multiple values. If TargetType is HIT
          and QuestionId is absent, then the result describes results of the HIT, including the
          HIT agreement score. If ObjectType is Assignment and QuestionId is absent, then the
          result describes the Worker's performance on the HIT.

        - **Key** *(string) --*

          Key identifies the particular piece of reviewed information.

        - **Value** *(string) --*

          The values of Key provided by the review policies you have selected.

    - **ReviewActions** *(list) --*

      A list of ReviewAction objects for each action specified in the Review Policy.

      - *(dict) --*

        Both the AssignmentReviewReport and the HITReviewReport elements contains the
        ReviewActionDetail data structure. This structure is returned multiple times for each
        action specified in the Review Policy.

        - **ActionId** *(string) --*

          The unique identifier for the action.

        - **ActionName** *(string) --*

          The nature of the action itself. The Review Policy is responsible for examining the HIT
          and Assignments, emitting results, and deciding which other actions will be necessary.

        - **TargetId** *(string) --*

          The specific HITId or AssignmentID targeted by the action.

        - **TargetType** *(string) --*

          The type of object in TargetId.

        - **Status** *(string) --*

          The current disposition of the action: INTENDED, SUCCEEDED, FAILED, or CANCELLED.

        - **CompleteTime** *(datetime) --*

          The date when the action was completed.

        - **Result** *(string) --*

          A description of the outcome of the review.

        - **ErrorCode** *(string) --*

          Present only when the Results have a FAILED Status.
    """


_ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef(
    _ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef
):
    """
    Type definition for `ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParameters` `MapEntries`

    This data structure is the data type for the AnswerKey parameter of the
    ScoreMyKnownAnswers/2011-09-01 Review Policy.

    - **Key** *(string) --*

      The QuestionID from the HIT that is used to identify which question requires
      Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review
      Policy.

    - **Values** *(list) --*

      The list of answers to the question specified in the MapEntry Key element. The
      Worker must match all values in order for the answer to be scored correctly.

      - *(string) --*
    """


_ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[
            ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef
        ],
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef(
    _ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef
):
    """
    Type definition for `ClientListReviewPolicyResultsForHitResponseHITReviewPolicy` `Parameters`

    Name of the parameter from the Review policy.

    - **Key** *(string) --*

      Name of the parameter from the list of Review Polices.

    - **Values** *(list) --*

      The list of values of the Parameter

      - *(string) --*

    - **MapEntries** *(list) --*

      List of ParameterMapEntry objects.

      - *(dict) --*

        This data structure is the data type for the AnswerKey parameter of the
        ScoreMyKnownAnswers/2011-09-01 Review Policy.

        - **Key** *(string) --*

          The QuestionID from the HIT that is used to identify which question requires
          Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review
          Policy.

        - **Values** *(list) --*

          The list of answers to the question specified in the MapEntry Key element. The
          Worker must match all values in order for the answer to be scored correctly.

          - *(string) --*
    """


_ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef",
    {
        "PolicyName": str,
        "Parameters": List[
            ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef
        ],
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef(
    _ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef
):
    """
    Type definition for `ClientListReviewPolicyResultsForHitResponse` `HITReviewPolicy`

    The name of the HIT-level Review Policy. This contains only the PolicyName element.

    - **PolicyName** *(string) --*

      Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01

    - **Parameters** *(list) --*

      Name of the parameter from the Review policy.

      - *(dict) --*

        Name of the parameter from the Review policy.

        - **Key** *(string) --*

          Name of the parameter from the list of Review Polices.

        - **Values** *(list) --*

          The list of values of the Parameter

          - *(string) --*

        - **MapEntries** *(list) --*

          List of ParameterMapEntry objects.

          - *(dict) --*

            This data structure is the data type for the AnswerKey parameter of the
            ScoreMyKnownAnswers/2011-09-01 Review Policy.

            - **Key** *(string) --*

              The QuestionID from the HIT that is used to identify which question requires
              Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review
              Policy.

            - **Values** *(list) --*

              The list of answers to the question specified in the MapEntry Key element. The
              Worker must match all values in order for the answer to be scored correctly.

              - *(string) --*
    """


_ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef",
    {
        "ActionId": str,
        "ActionName": str,
        "TargetId": str,
        "TargetType": str,
        "Status": str,
        "CompleteTime": datetime,
        "Result": str,
        "ErrorCode": str,
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef(
    _ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef
):
    """
    Type definition for `ClientListReviewPolicyResultsForHitResponseHITReviewReport` `ReviewActions`

    Both the AssignmentReviewReport and the HITReviewReport elements contains the
    ReviewActionDetail data structure. This structure is returned multiple times for each
    action specified in the Review Policy.

    - **ActionId** *(string) --*

      The unique identifier for the action.

    - **ActionName** *(string) --*

      The nature of the action itself. The Review Policy is responsible for examining the HIT
      and Assignments, emitting results, and deciding which other actions will be necessary.

    - **TargetId** *(string) --*

      The specific HITId or AssignmentID targeted by the action.

    - **TargetType** *(string) --*

      The type of object in TargetId.

    - **Status** *(string) --*

      The current disposition of the action: INTENDED, SUCCEEDED, FAILED, or CANCELLED.

    - **CompleteTime** *(datetime) --*

      The date when the action was completed.

    - **Result** *(string) --*

      A description of the outcome of the review.

    - **ErrorCode** *(string) --*

      Present only when the Results have a FAILED Status.
    """


_ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef",
    {
        "ActionId": str,
        "SubjectId": str,
        "SubjectType": str,
        "QuestionId": str,
        "Key": str,
        "Value": str,
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef(
    _ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef
):
    """
    Type definition for `ClientListReviewPolicyResultsForHitResponseHITReviewReport` `ReviewResults`

    This data structure is returned multiple times for each result specified in the Review
    Policy.

    - **ActionId** *(string) --*

      A unique identifier of the Review action result.

    - **SubjectId** *(string) --*

      The HITID or AssignmentId about which this result was taken. Note that HIT-level Review
      Policies will often emit results about both the HIT itself and its Assignments, while
      Assignment-level review policies generally only emit results about the Assignment
      itself.

    - **SubjectType** *(string) --*

      The type of the object from the SubjectId field.

    - **QuestionId** *(string) --*

      Specifies the QuestionId the result is describing. Depending on whether the TargetType
      is a HIT or Assignment this results could specify multiple values. If TargetType is HIT
      and QuestionId is absent, then the result describes results of the HIT, including the
      HIT agreement score. If ObjectType is Assignment and QuestionId is absent, then the
      result describes the Worker's performance on the HIT.

    - **Key** *(string) --*

      Key identifies the particular piece of reviewed information.

    - **Value** *(string) --*

      The values of Key provided by the review policies you have selected.
    """


_ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef",
    {
        "ReviewResults": List[
            ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef
        ],
        "ReviewActions": List[
            ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef
        ],
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef(
    _ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef
):
    """
    Type definition for `ClientListReviewPolicyResultsForHitResponse` `HITReviewReport`

    Contains both ReviewResult and ReviewAction elements for a particular HIT.

    - **ReviewResults** *(list) --*

      A list of ReviewResults objects for each action specified in the Review Policy.

      - *(dict) --*

        This data structure is returned multiple times for each result specified in the Review
        Policy.

        - **ActionId** *(string) --*

          A unique identifier of the Review action result.

        - **SubjectId** *(string) --*

          The HITID or AssignmentId about which this result was taken. Note that HIT-level Review
          Policies will often emit results about both the HIT itself and its Assignments, while
          Assignment-level review policies generally only emit results about the Assignment
          itself.

        - **SubjectType** *(string) --*

          The type of the object from the SubjectId field.

        - **QuestionId** *(string) --*

          Specifies the QuestionId the result is describing. Depending on whether the TargetType
          is a HIT or Assignment this results could specify multiple values. If TargetType is HIT
          and QuestionId is absent, then the result describes results of the HIT, including the
          HIT agreement score. If ObjectType is Assignment and QuestionId is absent, then the
          result describes the Worker's performance on the HIT.

        - **Key** *(string) --*

          Key identifies the particular piece of reviewed information.

        - **Value** *(string) --*

          The values of Key provided by the review policies you have selected.

    - **ReviewActions** *(list) --*

      A list of ReviewAction objects for each action specified in the Review Policy.

      - *(dict) --*

        Both the AssignmentReviewReport and the HITReviewReport elements contains the
        ReviewActionDetail data structure. This structure is returned multiple times for each
        action specified in the Review Policy.

        - **ActionId** *(string) --*

          The unique identifier for the action.

        - **ActionName** *(string) --*

          The nature of the action itself. The Review Policy is responsible for examining the HIT
          and Assignments, emitting results, and deciding which other actions will be necessary.

        - **TargetId** *(string) --*

          The specific HITId or AssignmentID targeted by the action.

        - **TargetType** *(string) --*

          The type of object in TargetId.

        - **Status** *(string) --*

          The current disposition of the action: INTENDED, SUCCEEDED, FAILED, or CANCELLED.

        - **CompleteTime** *(datetime) --*

          The date when the action was completed.

        - **Result** *(string) --*

          A description of the outcome of the review.

        - **ErrorCode** *(string) --*

          Present only when the Results have a FAILED Status.
    """


_ClientListReviewPolicyResultsForHitResponseTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseTypeDef",
    {
        "HITId": str,
        "AssignmentReviewPolicy": ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef,
        "HITReviewPolicy": ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef,
        "AssignmentReviewReport": ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef,
        "HITReviewReport": ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef,
        "NextToken": str,
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseTypeDef(
    _ClientListReviewPolicyResultsForHitResponseTypeDef
):
    """
    Type definition for `ClientListReviewPolicyResultsForHit` `Response`

    - **HITId** *(string) --*

      The HITId of the HIT for which results have been returned.

    - **AssignmentReviewPolicy** *(dict) --*

      The name of the Assignment-level Review Policy. This contains only the PolicyName element.

      - **PolicyName** *(string) --*

        Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01

      - **Parameters** *(list) --*

        Name of the parameter from the Review policy.

        - *(dict) --*

          Name of the parameter from the Review policy.

          - **Key** *(string) --*

            Name of the parameter from the list of Review Polices.

          - **Values** *(list) --*

            The list of values of the Parameter

            - *(string) --*

          - **MapEntries** *(list) --*

            List of ParameterMapEntry objects.

            - *(dict) --*

              This data structure is the data type for the AnswerKey parameter of the
              ScoreMyKnownAnswers/2011-09-01 Review Policy.

              - **Key** *(string) --*

                The QuestionID from the HIT that is used to identify which question requires
                Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review
                Policy.

              - **Values** *(list) --*

                The list of answers to the question specified in the MapEntry Key element. The
                Worker must match all values in order for the answer to be scored correctly.

                - *(string) --*

    - **HITReviewPolicy** *(dict) --*

      The name of the HIT-level Review Policy. This contains only the PolicyName element.

      - **PolicyName** *(string) --*

        Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01

      - **Parameters** *(list) --*

        Name of the parameter from the Review policy.

        - *(dict) --*

          Name of the parameter from the Review policy.

          - **Key** *(string) --*

            Name of the parameter from the list of Review Polices.

          - **Values** *(list) --*

            The list of values of the Parameter

            - *(string) --*

          - **MapEntries** *(list) --*

            List of ParameterMapEntry objects.

            - *(dict) --*

              This data structure is the data type for the AnswerKey parameter of the
              ScoreMyKnownAnswers/2011-09-01 Review Policy.

              - **Key** *(string) --*

                The QuestionID from the HIT that is used to identify which question requires
                Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review
                Policy.

              - **Values** *(list) --*

                The list of answers to the question specified in the MapEntry Key element. The
                Worker must match all values in order for the answer to be scored correctly.

                - *(string) --*

    - **AssignmentReviewReport** *(dict) --*

      Contains both ReviewResult and ReviewAction elements for an Assignment.

      - **ReviewResults** *(list) --*

        A list of ReviewResults objects for each action specified in the Review Policy.

        - *(dict) --*

          This data structure is returned multiple times for each result specified in the Review
          Policy.

          - **ActionId** *(string) --*

            A unique identifier of the Review action result.

          - **SubjectId** *(string) --*

            The HITID or AssignmentId about which this result was taken. Note that HIT-level Review
            Policies will often emit results about both the HIT itself and its Assignments, while
            Assignment-level review policies generally only emit results about the Assignment
            itself.

          - **SubjectType** *(string) --*

            The type of the object from the SubjectId field.

          - **QuestionId** *(string) --*

            Specifies the QuestionId the result is describing. Depending on whether the TargetType
            is a HIT or Assignment this results could specify multiple values. If TargetType is HIT
            and QuestionId is absent, then the result describes results of the HIT, including the
            HIT agreement score. If ObjectType is Assignment and QuestionId is absent, then the
            result describes the Worker's performance on the HIT.

          - **Key** *(string) --*

            Key identifies the particular piece of reviewed information.

          - **Value** *(string) --*

            The values of Key provided by the review policies you have selected.

      - **ReviewActions** *(list) --*

        A list of ReviewAction objects for each action specified in the Review Policy.

        - *(dict) --*

          Both the AssignmentReviewReport and the HITReviewReport elements contains the
          ReviewActionDetail data structure. This structure is returned multiple times for each
          action specified in the Review Policy.

          - **ActionId** *(string) --*

            The unique identifier for the action.

          - **ActionName** *(string) --*

            The nature of the action itself. The Review Policy is responsible for examining the HIT
            and Assignments, emitting results, and deciding which other actions will be necessary.

          - **TargetId** *(string) --*

            The specific HITId or AssignmentID targeted by the action.

          - **TargetType** *(string) --*

            The type of object in TargetId.

          - **Status** *(string) --*

            The current disposition of the action: INTENDED, SUCCEEDED, FAILED, or CANCELLED.

          - **CompleteTime** *(datetime) --*

            The date when the action was completed.

          - **Result** *(string) --*

            A description of the outcome of the review.

          - **ErrorCode** *(string) --*

            Present only when the Results have a FAILED Status.

    - **HITReviewReport** *(dict) --*

      Contains both ReviewResult and ReviewAction elements for a particular HIT.

      - **ReviewResults** *(list) --*

        A list of ReviewResults objects for each action specified in the Review Policy.

        - *(dict) --*

          This data structure is returned multiple times for each result specified in the Review
          Policy.

          - **ActionId** *(string) --*

            A unique identifier of the Review action result.

          - **SubjectId** *(string) --*

            The HITID or AssignmentId about which this result was taken. Note that HIT-level Review
            Policies will often emit results about both the HIT itself and its Assignments, while
            Assignment-level review policies generally only emit results about the Assignment
            itself.

          - **SubjectType** *(string) --*

            The type of the object from the SubjectId field.

          - **QuestionId** *(string) --*

            Specifies the QuestionId the result is describing. Depending on whether the TargetType
            is a HIT or Assignment this results could specify multiple values. If TargetType is HIT
            and QuestionId is absent, then the result describes results of the HIT, including the
            HIT agreement score. If ObjectType is Assignment and QuestionId is absent, then the
            result describes the Worker's performance on the HIT.

          - **Key** *(string) --*

            Key identifies the particular piece of reviewed information.

          - **Value** *(string) --*

            The values of Key provided by the review policies you have selected.

      - **ReviewActions** *(list) --*

        A list of ReviewAction objects for each action specified in the Review Policy.

        - *(dict) --*

          Both the AssignmentReviewReport and the HITReviewReport elements contains the
          ReviewActionDetail data structure. This structure is returned multiple times for each
          action specified in the Review Policy.

          - **ActionId** *(string) --*

            The unique identifier for the action.

          - **ActionName** *(string) --*

            The nature of the action itself. The Review Policy is responsible for examining the HIT
            and Assignments, emitting results, and deciding which other actions will be necessary.

          - **TargetId** *(string) --*

            The specific HITId or AssignmentID targeted by the action.

          - **TargetType** *(string) --*

            The type of object in TargetId.

          - **Status** *(string) --*

            The current disposition of the action: INTENDED, SUCCEEDED, FAILED, or CANCELLED.

          - **CompleteTime** *(datetime) --*

            The date when the action was completed.

          - **Result** *(string) --*

            A description of the outcome of the review.

          - **ErrorCode** *(string) --*

            Present only when the Results have a FAILED Status.

    - **NextToken** *(string) --*

      If the previous response was incomplete (because there is more data to retrieve), Amazon
      Mechanical Turk returns a pagination token in the response. You can use this pagination token
      to retrieve the next set of results.
    """


_ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef(
    _ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef
):
    """
    Type definition for `ClientListReviewableHitsResponseHITsQualificationRequirements` `LocaleValues`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --*

      The country of the locale. Must be a valid ISO 3166 country code. For example,
      the code US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
      example, the code WA refers to the state of Washington.
    """


_ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "_ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": str,
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": str,
    },
    total=False,
)


class ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef(
    _ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef
):
    """
    Type definition for `ClientListReviewableHitsResponseHITs` `QualificationRequirements`

    The QualificationRequirement data structure describes a Qualification that a Worker
    must have before the Worker is allowed to accept a HIT. A requirement may optionally
    state that a Worker must have the Qualification in order to preview the HIT, or see the
    HIT in search results.

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type for the requirement.

    - **Comparator** *(string) --*

      The kind of comparison to make against a Qualification's value. You can compare a
      Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
      GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
      compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
      You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
      values. Lastly, a Qualification requirement can also test if a Qualification Exists
      or DoesNotExist in the user's profile, regardless of its value.

    - **IntegerValues** *(list) --*

      The integer value to compare against the Qualification's value. IntegerValue must not
      be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
      the Qualification type has an integer value; it cannot be used with the Worker_Locale
      QualificationType ID. When performing a set comparison by using the In or the NotIn
      comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
      data structure.

      - *(integer) --*

    - **LocaleValues** *(list) --*

      The locale value to compare against the Qualification's value. The local value must
      be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
      only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
      with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
      LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
      a set comparison by using the In or the NotIn comparator, you can use up to 30
      LocaleValue elements in a QualificationRequirement data structure.

      - *(dict) --*

        The Locale data structure represents a geographical region or location.

        - **Country** *(string) --*

          The country of the locale. Must be a valid ISO 3166 country code. For example,
          the code US refers to the United States of America.

        - **Subdivision** *(string) --*

          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
          example, the code WA refers to the state of Washington.

    - **RequiredToPreview** *(boolean) --*

      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
      the question data for the HIT will not be shown when a Worker whose Qualifications do
      not meet this requirement tries to preview the HIT. That is, a Worker's
      Qualifications must meet all of the requirements for which RequiredToPreview is true
      in order to preview the HIT. If a Worker meets all of the requirements where
      RequiredToPreview is true (or if there are no such requirements), but does not meet
      all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
      question data, but will not be allowed to accept and complete the HIT. The default is
      false. This should not be used in combination with the ``ActionsGuarded`` field.

    - **ActionsGuarded** *(string) --*

      Setting this attribute prevents Workers whose Qualifications do not meet this
      QualificationRequirement from taking the specified action. Valid arguments include
      "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
      search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
      see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
      accept, preview, or see the HIT in their search results). It's possible for you to
      create a HIT with multiple QualificationRequirements (which can have different values
      for the ActionGuarded attribute). In this case, the Worker is only permitted to
      perform an action when they have met all QualificationRequirements guarding the
      action. The actions in the order of least restrictive to most restrictive are
      Discover, Preview and Accept. For example, if a Worker meets all
      QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
      all requirements that are set with PreviewAndAccept, then the Worker will be able to
      Discover, i.e. see the HIT in their search result, but will not be able to Preview or
      Accept the HIT. ActionsGuarded should not be used in combination with the
      ``RequiredToPreview`` field.
    """


_ClientListReviewableHitsResponseHITsTypeDef = TypedDict(
    "_ClientListReviewableHitsResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": str,
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": str,
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientListReviewableHitsResponseHITsTypeDef(
    _ClientListReviewableHitsResponseHITsTypeDef
):
    """
    Type definition for `ClientListReviewableHitsResponse` `HITs`

    The HIT data structure represents a single HIT, including all the information necessary for
    a Worker to accept and complete the HIT.

    - **HITId** *(string) --*

      A unique identifier for the HIT.

    - **HITTypeId** *(string) --*

      The ID of the HIT type of this HIT

    - **HITGroupId** *(string) --*

      The ID of the HIT Group of this HIT.

    - **HITLayoutId** *(string) --*

      The ID of the HIT Layout of this HIT.

    - **CreationTime** *(datetime) --*

      The date and time the HIT was created.

    - **Title** *(string) --*

      The title of the HIT.

    - **Description** *(string) --*

      A general description of the HIT.

    - **Question** *(string) --*

      The data the Worker completing the HIT uses produce the results. This is either either a
      QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

    - **Keywords** *(string) --*

      One or more words or phrases that describe the HIT, separated by commas. Search terms
      similar to the keywords of a HIT are more likely to have the HIT in the search results.

    - **HITStatus** *(string) --*

      The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
      Reviewable | Reviewing | Disposed.

    - **MaxAssignments** *(integer) --*

      The number of times the HIT can be accepted and completed before the HIT becomes
      unavailable.

    - **Reward** *(string) --*

      A string representing a currency amount.

    - **AutoApprovalDelayInSeconds** *(integer) --*

      The amount of time, in seconds, after the Worker submits an assignment for the HIT that
      the results are automatically approved by Amazon Mechanical Turk. This is the amount of
      time the Requester has to reject an assignment submitted by a Worker before the
      assignment is auto-approved and the Worker is paid.

    - **Expiration** *(datetime) --*

      The date and time the HIT expires.

    - **AssignmentDurationInSeconds** *(integer) --*

      The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

    - **RequesterAnnotation** *(string) --*

      An arbitrary data field the Requester who created the HIT can use. This field is visible
      only to the creator of the HIT.

    - **QualificationRequirements** *(list) --*

      Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
      have between zero and ten Qualification requirements. All requirements must be met in
      order for a Worker to accept the HIT. Additionally, other actions can be restricted using
      the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

      - *(dict) --*

        The QualificationRequirement data structure describes a Qualification that a Worker
        must have before the Worker is allowed to accept a HIT. A requirement may optionally
        state that a Worker must have the Qualification in order to preview the HIT, or see the
        HIT in search results.

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type for the requirement.

        - **Comparator** *(string) --*

          The kind of comparison to make against a Qualification's value. You can compare a
          Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
          GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
          compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
          You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
          values. Lastly, a Qualification requirement can also test if a Qualification Exists
          or DoesNotExist in the user's profile, regardless of its value.

        - **IntegerValues** *(list) --*

          The integer value to compare against the Qualification's value. IntegerValue must not
          be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
          the Qualification type has an integer value; it cannot be used with the Worker_Locale
          QualificationType ID. When performing a set comparison by using the In or the NotIn
          comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
          data structure.

          - *(integer) --*

        - **LocaleValues** *(list) --*

          The locale value to compare against the Qualification's value. The local value must
          be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
          only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
          with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
          LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
          a set comparison by using the In or the NotIn comparator, you can use up to 30
          LocaleValue elements in a QualificationRequirement data structure.

          - *(dict) --*

            The Locale data structure represents a geographical region or location.

            - **Country** *(string) --*

              The country of the locale. Must be a valid ISO 3166 country code. For example,
              the code US refers to the United States of America.

            - **Subdivision** *(string) --*

              The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
              example, the code WA refers to the state of Washington.

        - **RequiredToPreview** *(boolean) --*

          DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
          the question data for the HIT will not be shown when a Worker whose Qualifications do
          not meet this requirement tries to preview the HIT. That is, a Worker's
          Qualifications must meet all of the requirements for which RequiredToPreview is true
          in order to preview the HIT. If a Worker meets all of the requirements where
          RequiredToPreview is true (or if there are no such requirements), but does not meet
          all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
          question data, but will not be allowed to accept and complete the HIT. The default is
          false. This should not be used in combination with the ``ActionsGuarded`` field.

        - **ActionsGuarded** *(string) --*

          Setting this attribute prevents Workers whose Qualifications do not meet this
          QualificationRequirement from taking the specified action. Valid arguments include
          "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
          search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
          see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
          accept, preview, or see the HIT in their search results). It's possible for you to
          create a HIT with multiple QualificationRequirements (which can have different values
          for the ActionGuarded attribute). In this case, the Worker is only permitted to
          perform an action when they have met all QualificationRequirements guarding the
          action. The actions in the order of least restrictive to most restrictive are
          Discover, Preview and Accept. For example, if a Worker meets all
          QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
          all requirements that are set with PreviewAndAccept, then the Worker will be able to
          Discover, i.e. see the HIT in their search result, but will not be able to Preview or
          Accept the HIT. ActionsGuarded should not be used in combination with the
          ``RequiredToPreview`` field.

    - **HITReviewStatus** *(string) --*

      Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
      ReviewedAppropriate | ReviewedInappropriate.

    - **NumberOfAssignmentsPending** *(integer) --*

      The number of assignments for this HIT that are being previewed or have been accepted by
      Workers, but have not yet been submitted, returned, or abandoned.

    - **NumberOfAssignmentsAvailable** *(integer) --*

      The number of assignments for this HIT that are available for Workers to accept.

    - **NumberOfAssignmentsCompleted** *(integer) --*

      The number of assignments for this HIT that have been approved or rejected.
    """


_ClientListReviewableHitsResponseTypeDef = TypedDict(
    "_ClientListReviewableHitsResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List[ClientListReviewableHitsResponseHITsTypeDef],
    },
    total=False,
)


class ClientListReviewableHitsResponseTypeDef(_ClientListReviewableHitsResponseTypeDef):
    """
    Type definition for `ClientListReviewableHits` `Response`

    - **NextToken** *(string) --*

      If the previous response was incomplete (because there is more data to retrieve), Amazon
      Mechanical Turk returns a pagination token in the response. You can use this pagination token
      to retrieve the next set of results.

    - **NumResults** *(integer) --*

      The number of HITs on this page in the filtered results list, equivalent to the number of
      HITs being returned by this call.

    - **HITs** *(list) --*

      The list of HIT elements returned by the query.

      - *(dict) --*

        The HIT data structure represents a single HIT, including all the information necessary for
        a Worker to accept and complete the HIT.

        - **HITId** *(string) --*

          A unique identifier for the HIT.

        - **HITTypeId** *(string) --*

          The ID of the HIT type of this HIT

        - **HITGroupId** *(string) --*

          The ID of the HIT Group of this HIT.

        - **HITLayoutId** *(string) --*

          The ID of the HIT Layout of this HIT.

        - **CreationTime** *(datetime) --*

          The date and time the HIT was created.

        - **Title** *(string) --*

          The title of the HIT.

        - **Description** *(string) --*

          A general description of the HIT.

        - **Question** *(string) --*

          The data the Worker completing the HIT uses produce the results. This is either either a
          QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

        - **Keywords** *(string) --*

          One or more words or phrases that describe the HIT, separated by commas. Search terms
          similar to the keywords of a HIT are more likely to have the HIT in the search results.

        - **HITStatus** *(string) --*

          The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
          Reviewable | Reviewing | Disposed.

        - **MaxAssignments** *(integer) --*

          The number of times the HIT can be accepted and completed before the HIT becomes
          unavailable.

        - **Reward** *(string) --*

          A string representing a currency amount.

        - **AutoApprovalDelayInSeconds** *(integer) --*

          The amount of time, in seconds, after the Worker submits an assignment for the HIT that
          the results are automatically approved by Amazon Mechanical Turk. This is the amount of
          time the Requester has to reject an assignment submitted by a Worker before the
          assignment is auto-approved and the Worker is paid.

        - **Expiration** *(datetime) --*

          The date and time the HIT expires.

        - **AssignmentDurationInSeconds** *(integer) --*

          The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

        - **RequesterAnnotation** *(string) --*

          An arbitrary data field the Requester who created the HIT can use. This field is visible
          only to the creator of the HIT.

        - **QualificationRequirements** *(list) --*

          Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
          have between zero and ten Qualification requirements. All requirements must be met in
          order for a Worker to accept the HIT. Additionally, other actions can be restricted using
          the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

          - *(dict) --*

            The QualificationRequirement data structure describes a Qualification that a Worker
            must have before the Worker is allowed to accept a HIT. A requirement may optionally
            state that a Worker must have the Qualification in order to preview the HIT, or see the
            HIT in search results.

            - **QualificationTypeId** *(string) --*

              The ID of the Qualification type for the requirement.

            - **Comparator** *(string) --*

              The kind of comparison to make against a Qualification's value. You can compare a
              Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
              GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
              compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
              You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
              values. Lastly, a Qualification requirement can also test if a Qualification Exists
              or DoesNotExist in the user's profile, regardless of its value.

            - **IntegerValues** *(list) --*

              The integer value to compare against the Qualification's value. IntegerValue must not
              be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
              the Qualification type has an integer value; it cannot be used with the Worker_Locale
              QualificationType ID. When performing a set comparison by using the In or the NotIn
              comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
              data structure.

              - *(integer) --*

            - **LocaleValues** *(list) --*

              The locale value to compare against the Qualification's value. The local value must
              be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
              only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
              with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
              LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
              a set comparison by using the In or the NotIn comparator, you can use up to 30
              LocaleValue elements in a QualificationRequirement data structure.

              - *(dict) --*

                The Locale data structure represents a geographical region or location.

                - **Country** *(string) --*

                  The country of the locale. Must be a valid ISO 3166 country code. For example,
                  the code US refers to the United States of America.

                - **Subdivision** *(string) --*

                  The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
                  example, the code WA refers to the state of Washington.

            - **RequiredToPreview** *(boolean) --*

              DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
              the question data for the HIT will not be shown when a Worker whose Qualifications do
              not meet this requirement tries to preview the HIT. That is, a Worker's
              Qualifications must meet all of the requirements for which RequiredToPreview is true
              in order to preview the HIT. If a Worker meets all of the requirements where
              RequiredToPreview is true (or if there are no such requirements), but does not meet
              all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
              question data, but will not be allowed to accept and complete the HIT. The default is
              false. This should not be used in combination with the ``ActionsGuarded`` field.

            - **ActionsGuarded** *(string) --*

              Setting this attribute prevents Workers whose Qualifications do not meet this
              QualificationRequirement from taking the specified action. Valid arguments include
              "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
              search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
              see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
              accept, preview, or see the HIT in their search results). It's possible for you to
              create a HIT with multiple QualificationRequirements (which can have different values
              for the ActionGuarded attribute). In this case, the Worker is only permitted to
              perform an action when they have met all QualificationRequirements guarding the
              action. The actions in the order of least restrictive to most restrictive are
              Discover, Preview and Accept. For example, if a Worker meets all
              QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
              all requirements that are set with PreviewAndAccept, then the Worker will be able to
              Discover, i.e. see the HIT in their search result, but will not be able to Preview or
              Accept the HIT. ActionsGuarded should not be used in combination with the
              ``RequiredToPreview`` field.

        - **HITReviewStatus** *(string) --*

          Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
          ReviewedAppropriate | ReviewedInappropriate.

        - **NumberOfAssignmentsPending** *(integer) --*

          The number of assignments for this HIT that are being previewed or have been accepted by
          Workers, but have not yet been submitted, returned, or abandoned.

        - **NumberOfAssignmentsAvailable** *(integer) --*

          The number of assignments for this HIT that are available for Workers to accept.

        - **NumberOfAssignmentsCompleted** *(integer) --*

          The number of assignments for this HIT that have been approved or rejected.
    """


_ClientListWorkerBlocksResponseWorkerBlocksTypeDef = TypedDict(
    "_ClientListWorkerBlocksResponseWorkerBlocksTypeDef",
    {"WorkerId": str, "Reason": str},
    total=False,
)


class ClientListWorkerBlocksResponseWorkerBlocksTypeDef(
    _ClientListWorkerBlocksResponseWorkerBlocksTypeDef
):
    """
    Type definition for `ClientListWorkerBlocksResponse` `WorkerBlocks`

    The WorkerBlock data structure represents a Worker who has been blocked. It has two
    elements: the WorkerId and the Reason for the block.

    - **WorkerId** *(string) --*

      The ID of the Worker who accepted the HIT.

    - **Reason** *(string) --*

      A message explaining the reason the Worker was blocked.
    """


_ClientListWorkerBlocksResponseTypeDef = TypedDict(
    "_ClientListWorkerBlocksResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "WorkerBlocks": List[ClientListWorkerBlocksResponseWorkerBlocksTypeDef],
    },
    total=False,
)


class ClientListWorkerBlocksResponseTypeDef(_ClientListWorkerBlocksResponseTypeDef):
    """
    Type definition for `ClientListWorkerBlocks` `Response`

    - **NextToken** *(string) --*

      If the previous response was incomplete (because there is more data to retrieve), Amazon
      Mechanical Turk returns a pagination token in the response. You can use this pagination token
      to retrieve the next set of results.

    - **NumResults** *(integer) --*

      The number of assignments on the page in the filtered results list, equivalent to the number
      of assignments returned by this call.

    - **WorkerBlocks** *(list) --*

      The list of WorkerBlocks, containing the collection of Worker IDs and reasons for blocking.

      - *(dict) --*

        The WorkerBlock data structure represents a Worker who has been blocked. It has two
        elements: the WorkerId and the Reason for the block.

        - **WorkerId** *(string) --*

          The ID of the Worker who accepted the HIT.

        - **Reason** *(string) --*

          A message explaining the reason the Worker was blocked.
    """


_ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef = TypedDict(
    "_ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef(
    _ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef
):
    """
    Type definition for `ClientListWorkersWithQualificationTypeResponseQualifications` `LocaleValue`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --*

      The country of the locale. Must be a valid ISO 3166 country code. For example, the code
      US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
      example, the code WA refers to the state of Washington.
    """


_ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef = TypedDict(
    "_ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "GrantTime": datetime,
        "IntegerValue": int,
        "LocaleValue": ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef,
        "Status": str,
    },
    total=False,
)


class ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef(
    _ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef
):
    """
    Type definition for `ClientListWorkersWithQualificationTypeResponse` `Qualifications`

    The Qualification data structure represents a Qualification assigned to a user, including
    the Qualification type and the value (score).

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type for the Qualification.

    - **WorkerId** *(string) --*

      The ID of the Worker who possesses the Qualification.

    - **GrantTime** *(datetime) --*

      The date and time the Qualification was granted to the Worker. If the Worker's
      Qualification was revoked, and then re-granted based on a new Qualification request,
      GrantTime is the date and time of the last call to the AcceptQualificationRequest
      operation.

    - **IntegerValue** *(integer) --*

      The value (score) of the Qualification, if the Qualification has an integer value.

    - **LocaleValue** *(dict) --*

      The Locale data structure represents a geographical region or location.

      - **Country** *(string) --*

        The country of the locale. Must be a valid ISO 3166 country code. For example, the code
        US refers to the United States of America.

      - **Subdivision** *(string) --*

        The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
        example, the code WA refers to the state of Washington.

    - **Status** *(string) --*

      The status of the Qualification. Valid values are Granted | Revoked.
    """


_ClientListWorkersWithQualificationTypeResponseTypeDef = TypedDict(
    "_ClientListWorkersWithQualificationTypeResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Qualifications": List[
            ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef
        ],
    },
    total=False,
)


class ClientListWorkersWithQualificationTypeResponseTypeDef(
    _ClientListWorkersWithQualificationTypeResponseTypeDef
):
    """
    Type definition for `ClientListWorkersWithQualificationType` `Response`

    - **NextToken** *(string) --*

      If the previous response was incomplete (because there is more data to retrieve), Amazon
      Mechanical Turk returns a pagination token in the response. You can use this pagination token
      to retrieve the next set of results.

    - **NumResults** *(integer) --*

      The number of Qualifications on this page in the filtered results list, equivalent to the
      number of Qualifications being returned by this call.

    - **Qualifications** *(list) --*

      The list of Qualification elements returned by this call.

      - *(dict) --*

        The Qualification data structure represents a Qualification assigned to a user, including
        the Qualification type and the value (score).

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type for the Qualification.

        - **WorkerId** *(string) --*

          The ID of the Worker who possesses the Qualification.

        - **GrantTime** *(datetime) --*

          The date and time the Qualification was granted to the Worker. If the Worker's
          Qualification was revoked, and then re-granted based on a new Qualification request,
          GrantTime is the date and time of the last call to the AcceptQualificationRequest
          operation.

        - **IntegerValue** *(integer) --*

          The value (score) of the Qualification, if the Qualification has an integer value.

        - **LocaleValue** *(dict) --*

          The Locale data structure represents a geographical region or location.

          - **Country** *(string) --*

            The country of the locale. Must be a valid ISO 3166 country code. For example, the code
            US refers to the United States of America.

          - **Subdivision** *(string) --*

            The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
            example, the code WA refers to the state of Washington.

        - **Status** *(string) --*

          The status of the Qualification. Valid values are Granted | Revoked.
    """


_ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef = TypedDict(
    "_ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef",
    {
        "NotifyWorkersFailureCode": str,
        "NotifyWorkersFailureMessage": str,
        "WorkerId": str,
    },
    total=False,
)


class ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef(
    _ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef
):
    """
    Type definition for `ClientNotifyWorkersResponse` `NotifyWorkersFailureStatuses`

    When MTurk encounters an issue with notifying the Workers you specified, it returns back
    this object with failure details.

    - **NotifyWorkersFailureCode** *(string) --*

      Encoded value for the failure type.

    - **NotifyWorkersFailureMessage** *(string) --*

      A message detailing the reason the Worker could not be notified.

    - **WorkerId** *(string) --*

      The ID of the Worker.
    """


_ClientNotifyWorkersResponseTypeDef = TypedDict(
    "_ClientNotifyWorkersResponseTypeDef",
    {
        "NotifyWorkersFailureStatuses": List[
            ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef
        ]
    },
    total=False,
)


class ClientNotifyWorkersResponseTypeDef(_ClientNotifyWorkersResponseTypeDef):
    """
    Type definition for `ClientNotifyWorkers` `Response`

    - **NotifyWorkersFailureStatuses** *(list) --*

      When MTurk sends notifications to the list of Workers, it returns back any failures it
      encounters in this list of NotifyWorkersFailureStatus objects.

      - *(dict) --*

        When MTurk encounters an issue with notifying the Workers you specified, it returns back
        this object with failure details.

        - **NotifyWorkersFailureCode** *(string) --*

          Encoded value for the failure type.

        - **NotifyWorkersFailureMessage** *(string) --*

          A message detailing the reason the Worker could not be notified.

        - **WorkerId** *(string) --*

          The ID of the Worker.
    """


_ClientSendTestEventNotificationNotificationTypeDef = TypedDict(
    "_ClientSendTestEventNotificationNotificationTypeDef",
    {"Destination": str, "Transport": str, "Version": str, "EventTypes": List[str]},
)


class ClientSendTestEventNotificationNotificationTypeDef(
    _ClientSendTestEventNotificationNotificationTypeDef
):
    """
    Type definition for `ClientSendTestEventNotification` `Notification`

    The notification specification to test. This value is identical to the value you would provide to
    the UpdateNotificationSettings operation when you establish the notification specification for a
    HIT type.

    - **Destination** *(string) --* **[REQUIRED]**

      The target for notification messages. The Destination’s format is determined by the specified
      Transport:

      * When Transport is Email, the Destination is your email address.

      * When Transport is SQS, the Destination is your queue URL.

      * When Transport is SNS, the Destination is the ARN of your topic.

    - **Transport** *(string) --* **[REQUIRED]**

      The method Amazon Mechanical Turk uses to send the notification. Valid Values: Email | SQS |
      SNS.

    - **Version** *(string) --* **[REQUIRED]**

      The version of the Notification API to use. Valid value is 2006-05-05.

    - **EventTypes** *(list) --* **[REQUIRED]**

      The list of events that should cause notifications to be sent. Valid Values: AssignmentAccepted
      | AssignmentAbandoned | AssignmentReturned | AssignmentSubmitted | AssignmentRejected |
      AssignmentApproved | HITCreated | HITExtended | HITDisposed | HITReviewable | HITExpired |
      Ping. The Ping event is only valid for the SendTestEventNotification operation.

      - *(string) --*
    """


_ClientUpdateNotificationSettingsNotificationTypeDef = TypedDict(
    "_ClientUpdateNotificationSettingsNotificationTypeDef",
    {"Destination": str, "Transport": str, "Version": str, "EventTypes": List[str]},
)


class ClientUpdateNotificationSettingsNotificationTypeDef(
    _ClientUpdateNotificationSettingsNotificationTypeDef
):
    """
    Type definition for `ClientUpdateNotificationSettings` `Notification`

    The notification specification for the HIT type.

    - **Destination** *(string) --* **[REQUIRED]**

      The target for notification messages. The Destination’s format is determined by the specified
      Transport:

      * When Transport is Email, the Destination is your email address.

      * When Transport is SQS, the Destination is your queue URL.

      * When Transport is SNS, the Destination is the ARN of your topic.

    - **Transport** *(string) --* **[REQUIRED]**

      The method Amazon Mechanical Turk uses to send the notification. Valid Values: Email | SQS |
      SNS.

    - **Version** *(string) --* **[REQUIRED]**

      The version of the Notification API to use. Valid value is 2006-05-05.

    - **EventTypes** *(list) --* **[REQUIRED]**

      The list of events that should cause notifications to be sent. Valid Values: AssignmentAccepted
      | AssignmentAbandoned | AssignmentReturned | AssignmentSubmitted | AssignmentRejected |
      AssignmentApproved | HITCreated | HITExtended | HITDisposed | HITReviewable | HITExpired |
      Ping. The Ping event is only valid for the SendTestEventNotification operation.

      - *(string) --*
    """


_ClientUpdateQualificationTypeResponseQualificationTypeTypeDef = TypedDict(
    "_ClientUpdateQualificationTypeResponseQualificationTypeTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": str,
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)


class ClientUpdateQualificationTypeResponseQualificationTypeTypeDef(
    _ClientUpdateQualificationTypeResponseQualificationTypeTypeDef
):
    """
    Type definition for `ClientUpdateQualificationTypeResponse` `QualificationType`

    Contains a QualificationType data structure.

    - **QualificationTypeId** *(string) --*

      A unique identifier for the Qualification type. A Qualification type is given a
      Qualification type ID when you call the CreateQualificationType operation.

    - **CreationTime** *(datetime) --*

      The date and time the Qualification type was created.

    - **Name** *(string) --*

      The name of the Qualification type. The type name is used to identify the type, and to find
      the type using a Qualification type search.

    - **Description** *(string) --*

      A long description for the Qualification type.

    - **Keywords** *(string) --*

      One or more words or phrases that describe theQualification type, separated by commas. The
      Keywords make the type easier to find using a search.

    - **QualificationTypeStatus** *(string) --*

      The status of the Qualification type. A Qualification type's status determines if users can
      apply to receive a Qualification of this type, and if HITs can be created with requirements
      based on this type. Valid values are Active | Inactive.

    - **Test** *(string) --*

      The questions for a Qualification test associated with this Qualification type that a user
      can take to obtain a Qualification of this type. This parameter must be specified if
      AnswerKey is present. A Qualification type cannot have both a specified Test parameter and
      an AutoGranted value of true.

    - **TestDurationInSeconds** *(integer) --*

      The amount of time, in seconds, given to a Worker to complete the Qualification test,
      beginning from the time the Worker requests the Qualification.

    - **AnswerKey** *(string) --*

      The answers to the Qualification test specified in the Test parameter.

    - **RetryDelayInSeconds** *(integer) --*

      The amount of time, in seconds, Workers must wait after taking the Qualification test
      before they can take it again. Workers can take a Qualification test multiple times if they
      were not granted the Qualification from a previous attempt, or if the test offers a
      gradient score and they want a better score. If not specified, retries are disabled and
      Workers can request a Qualification only once.

    - **IsRequestable** *(boolean) --*

      Specifies whether the Qualification type is one that a user can request through the Amazon
      Mechanical Turk web site, such as by taking a Qualification test. This value is False for
      Qualifications assigned automatically by the system. Valid values are True | False.

    - **AutoGranted** *(boolean) --*

      Specifies that requests for the Qualification type are granted immediately, without
      prompting the Worker with a Qualification test. Valid values are True | False.

    - **AutoGrantedValue** *(integer) --*

      The Qualification integer value to use for automatically granted Qualifications, if
      AutoGranted is true. This is 1 by default.
    """


_ClientUpdateQualificationTypeResponseTypeDef = TypedDict(
    "_ClientUpdateQualificationTypeResponseTypeDef",
    {
        "QualificationType": ClientUpdateQualificationTypeResponseQualificationTypeTypeDef
    },
    total=False,
)


class ClientUpdateQualificationTypeResponseTypeDef(
    _ClientUpdateQualificationTypeResponseTypeDef
):
    """
    Type definition for `ClientUpdateQualificationType` `Response`

    - **QualificationType** *(dict) --*

      Contains a QualificationType data structure.

      - **QualificationTypeId** *(string) --*

        A unique identifier for the Qualification type. A Qualification type is given a
        Qualification type ID when you call the CreateQualificationType operation.

      - **CreationTime** *(datetime) --*

        The date and time the Qualification type was created.

      - **Name** *(string) --*

        The name of the Qualification type. The type name is used to identify the type, and to find
        the type using a Qualification type search.

      - **Description** *(string) --*

        A long description for the Qualification type.

      - **Keywords** *(string) --*

        One or more words or phrases that describe theQualification type, separated by commas. The
        Keywords make the type easier to find using a search.

      - **QualificationTypeStatus** *(string) --*

        The status of the Qualification type. A Qualification type's status determines if users can
        apply to receive a Qualification of this type, and if HITs can be created with requirements
        based on this type. Valid values are Active | Inactive.

      - **Test** *(string) --*

        The questions for a Qualification test associated with this Qualification type that a user
        can take to obtain a Qualification of this type. This parameter must be specified if
        AnswerKey is present. A Qualification type cannot have both a specified Test parameter and
        an AutoGranted value of true.

      - **TestDurationInSeconds** *(integer) --*

        The amount of time, in seconds, given to a Worker to complete the Qualification test,
        beginning from the time the Worker requests the Qualification.

      - **AnswerKey** *(string) --*

        The answers to the Qualification test specified in the Test parameter.

      - **RetryDelayInSeconds** *(integer) --*

        The amount of time, in seconds, Workers must wait after taking the Qualification test
        before they can take it again. Workers can take a Qualification test multiple times if they
        were not granted the Qualification from a previous attempt, or if the test offers a
        gradient score and they want a better score. If not specified, retries are disabled and
        Workers can request a Qualification only once.

      - **IsRequestable** *(boolean) --*

        Specifies whether the Qualification type is one that a user can request through the Amazon
        Mechanical Turk web site, such as by taking a Qualification test. This value is False for
        Qualifications assigned automatically by the system. Valid values are True | False.

      - **AutoGranted** *(boolean) --*

        Specifies that requests for the Qualification type are granted immediately, without
        prompting the Worker with a Qualification test. Valid values are True | False.

      - **AutoGrantedValue** *(integer) --*

        The Qualification integer value to use for automatically granted Qualifications, if
        AutoGranted is true. This is 1 by default.
    """


_ListAssignmentsForHITPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssignmentsForHITPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssignmentsForHITPaginatePaginationConfigTypeDef(
    _ListAssignmentsForHITPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAssignmentsForHITPaginate` `PaginationConfig`

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


_ListAssignmentsForHITPaginateResponseAssignmentsTypeDef = TypedDict(
    "_ListAssignmentsForHITPaginateResponseAssignmentsTypeDef",
    {
        "AssignmentId": str,
        "WorkerId": str,
        "HITId": str,
        "AssignmentStatus": str,
        "AutoApprovalTime": datetime,
        "AcceptTime": datetime,
        "SubmitTime": datetime,
        "ApprovalTime": datetime,
        "RejectionTime": datetime,
        "Deadline": datetime,
        "Answer": str,
        "RequesterFeedback": str,
    },
    total=False,
)


class ListAssignmentsForHITPaginateResponseAssignmentsTypeDef(
    _ListAssignmentsForHITPaginateResponseAssignmentsTypeDef
):
    """
    Type definition for `ListAssignmentsForHITPaginateResponse` `Assignments`

    The Assignment data structure represents a single assignment of a HIT to a Worker. The
    assignment tracks the Worker's efforts to complete the HIT, and contains the results for
    later retrieval.

    - **AssignmentId** *(string) --*

      A unique identifier for the assignment.

    - **WorkerId** *(string) --*

      The ID of the Worker who accepted the HIT.

    - **HITId** *(string) --*

      The ID of the HIT.

    - **AssignmentStatus** *(string) --*

      The status of the assignment.

    - **AutoApprovalTime** *(datetime) --*

      If results have been submitted, AutoApprovalTime is the date and time the results of the
      assignment results are considered Approved automatically if they have not already been
      explicitly approved or rejected by the Requester. This value is derived from the
      auto-approval delay specified by the Requester in the HIT. This value is omitted from the
      assignment if the Worker has not yet submitted results.

    - **AcceptTime** *(datetime) --*

      The date and time the Worker accepted the assignment.

    - **SubmitTime** *(datetime) --*

      If the Worker has submitted results, SubmitTime is the date and time the assignment was
      submitted. This value is omitted from the assignment if the Worker has not yet submitted
      results.

    - **ApprovalTime** *(datetime) --*

      If the Worker has submitted results and the Requester has approved the results,
      ApprovalTime is the date and time the Requester approved the results. This value is
      omitted from the assignment if the Requester has not yet approved the results.

    - **RejectionTime** *(datetime) --*

      If the Worker has submitted results and the Requester has rejected the results,
      RejectionTime is the date and time the Requester rejected the results.

    - **Deadline** *(datetime) --*

      The date and time of the deadline for the assignment. This value is derived from the
      deadline specification for the HIT and the date and time the Worker accepted the HIT.

    - **Answer** *(string) --*

      The Worker's answers submitted for the HIT contained in a QuestionFormAnswers document,
      if the Worker provides an answer. If the Worker does not provide any answers, Answer may
      contain a QuestionFormAnswers document, or Answer may be empty.

    - **RequesterFeedback** *(string) --*

      The feedback string included with the call to the ApproveAssignment operation or the
      RejectAssignment operation, if the Requester approved or rejected the assignment and
      specified feedback.
    """


_ListAssignmentsForHITPaginateResponseTypeDef = TypedDict(
    "_ListAssignmentsForHITPaginateResponseTypeDef",
    {
        "NumResults": int,
        "Assignments": List[ListAssignmentsForHITPaginateResponseAssignmentsTypeDef],
    },
    total=False,
)


class ListAssignmentsForHITPaginateResponseTypeDef(
    _ListAssignmentsForHITPaginateResponseTypeDef
):
    """
    Type definition for `ListAssignmentsForHITPaginate` `Response`

    - **NumResults** *(integer) --*

      The number of assignments on the page in the filtered results list, equivalent to the number
      of assignments returned by this call.

    - **Assignments** *(list) --*

      The collection of Assignment data structures returned by this call.

      - *(dict) --*

        The Assignment data structure represents a single assignment of a HIT to a Worker. The
        assignment tracks the Worker's efforts to complete the HIT, and contains the results for
        later retrieval.

        - **AssignmentId** *(string) --*

          A unique identifier for the assignment.

        - **WorkerId** *(string) --*

          The ID of the Worker who accepted the HIT.

        - **HITId** *(string) --*

          The ID of the HIT.

        - **AssignmentStatus** *(string) --*

          The status of the assignment.

        - **AutoApprovalTime** *(datetime) --*

          If results have been submitted, AutoApprovalTime is the date and time the results of the
          assignment results are considered Approved automatically if they have not already been
          explicitly approved or rejected by the Requester. This value is derived from the
          auto-approval delay specified by the Requester in the HIT. This value is omitted from the
          assignment if the Worker has not yet submitted results.

        - **AcceptTime** *(datetime) --*

          The date and time the Worker accepted the assignment.

        - **SubmitTime** *(datetime) --*

          If the Worker has submitted results, SubmitTime is the date and time the assignment was
          submitted. This value is omitted from the assignment if the Worker has not yet submitted
          results.

        - **ApprovalTime** *(datetime) --*

          If the Worker has submitted results and the Requester has approved the results,
          ApprovalTime is the date and time the Requester approved the results. This value is
          omitted from the assignment if the Requester has not yet approved the results.

        - **RejectionTime** *(datetime) --*

          If the Worker has submitted results and the Requester has rejected the results,
          RejectionTime is the date and time the Requester rejected the results.

        - **Deadline** *(datetime) --*

          The date and time of the deadline for the assignment. This value is derived from the
          deadline specification for the HIT and the date and time the Worker accepted the HIT.

        - **Answer** *(string) --*

          The Worker's answers submitted for the HIT contained in a QuestionFormAnswers document,
          if the Worker provides an answer. If the Worker does not provide any answers, Answer may
          contain a QuestionFormAnswers document, or Answer may be empty.

        - **RequesterFeedback** *(string) --*

          The feedback string included with the call to the ApproveAssignment operation or the
          RejectAssignment operation, if the Requester approved or rejected the assignment and
          specified feedback.
    """


_ListBonusPaymentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBonusPaymentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBonusPaymentsPaginatePaginationConfigTypeDef(
    _ListBonusPaymentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBonusPaymentsPaginate` `PaginationConfig`

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


_ListBonusPaymentsPaginateResponseBonusPaymentsTypeDef = TypedDict(
    "_ListBonusPaymentsPaginateResponseBonusPaymentsTypeDef",
    {
        "WorkerId": str,
        "BonusAmount": str,
        "AssignmentId": str,
        "Reason": str,
        "GrantTime": datetime,
    },
    total=False,
)


class ListBonusPaymentsPaginateResponseBonusPaymentsTypeDef(
    _ListBonusPaymentsPaginateResponseBonusPaymentsTypeDef
):
    """
    Type definition for `ListBonusPaymentsPaginateResponse` `BonusPayments`

    An object representing a Bonus payment paid to a Worker.

    - **WorkerId** *(string) --*

      The ID of the Worker to whom the bonus was paid.

    - **BonusAmount** *(string) --*

      A string representing a currency amount.

    - **AssignmentId** *(string) --*

      The ID of the assignment associated with this bonus payment.

    - **Reason** *(string) --*

      The Reason text given when the bonus was granted, if any.

    - **GrantTime** *(datetime) --*

      The date and time of when the bonus was granted.
    """


_ListBonusPaymentsPaginateResponseTypeDef = TypedDict(
    "_ListBonusPaymentsPaginateResponseTypeDef",
    {
        "NumResults": int,
        "BonusPayments": List[ListBonusPaymentsPaginateResponseBonusPaymentsTypeDef],
    },
    total=False,
)


class ListBonusPaymentsPaginateResponseTypeDef(
    _ListBonusPaymentsPaginateResponseTypeDef
):
    """
    Type definition for `ListBonusPaymentsPaginate` `Response`

    - **NumResults** *(integer) --*

      The number of bonus payments on this page in the filtered results list, equivalent to the
      number of bonus payments being returned by this call.

    - **BonusPayments** *(list) --*

      A successful request to the ListBonusPayments operation returns a list of BonusPayment
      objects.

      - *(dict) --*

        An object representing a Bonus payment paid to a Worker.

        - **WorkerId** *(string) --*

          The ID of the Worker to whom the bonus was paid.

        - **BonusAmount** *(string) --*

          A string representing a currency amount.

        - **AssignmentId** *(string) --*

          The ID of the assignment associated with this bonus payment.

        - **Reason** *(string) --*

          The Reason text given when the bonus was granted, if any.

        - **GrantTime** *(datetime) --*

          The date and time of when the bonus was granted.
    """


_ListHITsForQualificationTypePaginatePaginationConfigTypeDef = TypedDict(
    "_ListHITsForQualificationTypePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHITsForQualificationTypePaginatePaginationConfigTypeDef(
    _ListHITsForQualificationTypePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListHITsForQualificationTypePaginate` `PaginationConfig`

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


_ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef(
    _ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef
):
    """
    Type definition for `ListHITsForQualificationTypePaginateResponseHITsQualificationRequirements` `LocaleValues`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --*

      The country of the locale. Must be a valid ISO 3166 country code. For example,
      the code US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
      example, the code WA refers to the state of Washington.
    """


_ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "_ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": str,
        "IntegerValues": List[int],
        "LocaleValues": List[
            ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": str,
    },
    total=False,
)


class ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsTypeDef(
    _ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsTypeDef
):
    """
    Type definition for `ListHITsForQualificationTypePaginateResponseHITs` `QualificationRequirements`

    The QualificationRequirement data structure describes a Qualification that a Worker
    must have before the Worker is allowed to accept a HIT. A requirement may optionally
    state that a Worker must have the Qualification in order to preview the HIT, or see the
    HIT in search results.

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type for the requirement.

    - **Comparator** *(string) --*

      The kind of comparison to make against a Qualification's value. You can compare a
      Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
      GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
      compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
      You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
      values. Lastly, a Qualification requirement can also test if a Qualification Exists
      or DoesNotExist in the user's profile, regardless of its value.

    - **IntegerValues** *(list) --*

      The integer value to compare against the Qualification's value. IntegerValue must not
      be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
      the Qualification type has an integer value; it cannot be used with the Worker_Locale
      QualificationType ID. When performing a set comparison by using the In or the NotIn
      comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
      data structure.

      - *(integer) --*

    - **LocaleValues** *(list) --*

      The locale value to compare against the Qualification's value. The local value must
      be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
      only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
      with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
      LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
      a set comparison by using the In or the NotIn comparator, you can use up to 30
      LocaleValue elements in a QualificationRequirement data structure.

      - *(dict) --*

        The Locale data structure represents a geographical region or location.

        - **Country** *(string) --*

          The country of the locale. Must be a valid ISO 3166 country code. For example,
          the code US refers to the United States of America.

        - **Subdivision** *(string) --*

          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
          example, the code WA refers to the state of Washington.

    - **RequiredToPreview** *(boolean) --*

      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
      the question data for the HIT will not be shown when a Worker whose Qualifications do
      not meet this requirement tries to preview the HIT. That is, a Worker's
      Qualifications must meet all of the requirements for which RequiredToPreview is true
      in order to preview the HIT. If a Worker meets all of the requirements where
      RequiredToPreview is true (or if there are no such requirements), but does not meet
      all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
      question data, but will not be allowed to accept and complete the HIT. The default is
      false. This should not be used in combination with the ``ActionsGuarded`` field.

    - **ActionsGuarded** *(string) --*

      Setting this attribute prevents Workers whose Qualifications do not meet this
      QualificationRequirement from taking the specified action. Valid arguments include
      "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
      search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
      see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
      accept, preview, or see the HIT in their search results). It's possible for you to
      create a HIT with multiple QualificationRequirements (which can have different values
      for the ActionGuarded attribute). In this case, the Worker is only permitted to
      perform an action when they have met all QualificationRequirements guarding the
      action. The actions in the order of least restrictive to most restrictive are
      Discover, Preview and Accept. For example, if a Worker meets all
      QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
      all requirements that are set with PreviewAndAccept, then the Worker will be able to
      Discover, i.e. see the HIT in their search result, but will not be able to Preview or
      Accept the HIT. ActionsGuarded should not be used in combination with the
      ``RequiredToPreview`` field.
    """


_ListHITsForQualificationTypePaginateResponseHITsTypeDef = TypedDict(
    "_ListHITsForQualificationTypePaginateResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": str,
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": str,
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ListHITsForQualificationTypePaginateResponseHITsTypeDef(
    _ListHITsForQualificationTypePaginateResponseHITsTypeDef
):
    """
    Type definition for `ListHITsForQualificationTypePaginateResponse` `HITs`

    The HIT data structure represents a single HIT, including all the information necessary for
    a Worker to accept and complete the HIT.

    - **HITId** *(string) --*

      A unique identifier for the HIT.

    - **HITTypeId** *(string) --*

      The ID of the HIT type of this HIT

    - **HITGroupId** *(string) --*

      The ID of the HIT Group of this HIT.

    - **HITLayoutId** *(string) --*

      The ID of the HIT Layout of this HIT.

    - **CreationTime** *(datetime) --*

      The date and time the HIT was created.

    - **Title** *(string) --*

      The title of the HIT.

    - **Description** *(string) --*

      A general description of the HIT.

    - **Question** *(string) --*

      The data the Worker completing the HIT uses produce the results. This is either either a
      QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

    - **Keywords** *(string) --*

      One or more words or phrases that describe the HIT, separated by commas. Search terms
      similar to the keywords of a HIT are more likely to have the HIT in the search results.

    - **HITStatus** *(string) --*

      The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
      Reviewable | Reviewing | Disposed.

    - **MaxAssignments** *(integer) --*

      The number of times the HIT can be accepted and completed before the HIT becomes
      unavailable.

    - **Reward** *(string) --*

      A string representing a currency amount.

    - **AutoApprovalDelayInSeconds** *(integer) --*

      The amount of time, in seconds, after the Worker submits an assignment for the HIT that
      the results are automatically approved by Amazon Mechanical Turk. This is the amount of
      time the Requester has to reject an assignment submitted by a Worker before the
      assignment is auto-approved and the Worker is paid.

    - **Expiration** *(datetime) --*

      The date and time the HIT expires.

    - **AssignmentDurationInSeconds** *(integer) --*

      The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

    - **RequesterAnnotation** *(string) --*

      An arbitrary data field the Requester who created the HIT can use. This field is visible
      only to the creator of the HIT.

    - **QualificationRequirements** *(list) --*

      Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
      have between zero and ten Qualification requirements. All requirements must be met in
      order for a Worker to accept the HIT. Additionally, other actions can be restricted using
      the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

      - *(dict) --*

        The QualificationRequirement data structure describes a Qualification that a Worker
        must have before the Worker is allowed to accept a HIT. A requirement may optionally
        state that a Worker must have the Qualification in order to preview the HIT, or see the
        HIT in search results.

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type for the requirement.

        - **Comparator** *(string) --*

          The kind of comparison to make against a Qualification's value. You can compare a
          Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
          GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
          compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
          You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
          values. Lastly, a Qualification requirement can also test if a Qualification Exists
          or DoesNotExist in the user's profile, regardless of its value.

        - **IntegerValues** *(list) --*

          The integer value to compare against the Qualification's value. IntegerValue must not
          be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
          the Qualification type has an integer value; it cannot be used with the Worker_Locale
          QualificationType ID. When performing a set comparison by using the In or the NotIn
          comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
          data structure.

          - *(integer) --*

        - **LocaleValues** *(list) --*

          The locale value to compare against the Qualification's value. The local value must
          be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
          only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
          with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
          LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
          a set comparison by using the In or the NotIn comparator, you can use up to 30
          LocaleValue elements in a QualificationRequirement data structure.

          - *(dict) --*

            The Locale data structure represents a geographical region or location.

            - **Country** *(string) --*

              The country of the locale. Must be a valid ISO 3166 country code. For example,
              the code US refers to the United States of America.

            - **Subdivision** *(string) --*

              The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
              example, the code WA refers to the state of Washington.

        - **RequiredToPreview** *(boolean) --*

          DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
          the question data for the HIT will not be shown when a Worker whose Qualifications do
          not meet this requirement tries to preview the HIT. That is, a Worker's
          Qualifications must meet all of the requirements for which RequiredToPreview is true
          in order to preview the HIT. If a Worker meets all of the requirements where
          RequiredToPreview is true (or if there are no such requirements), but does not meet
          all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
          question data, but will not be allowed to accept and complete the HIT. The default is
          false. This should not be used in combination with the ``ActionsGuarded`` field.

        - **ActionsGuarded** *(string) --*

          Setting this attribute prevents Workers whose Qualifications do not meet this
          QualificationRequirement from taking the specified action. Valid arguments include
          "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
          search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
          see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
          accept, preview, or see the HIT in their search results). It's possible for you to
          create a HIT with multiple QualificationRequirements (which can have different values
          for the ActionGuarded attribute). In this case, the Worker is only permitted to
          perform an action when they have met all QualificationRequirements guarding the
          action. The actions in the order of least restrictive to most restrictive are
          Discover, Preview and Accept. For example, if a Worker meets all
          QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
          all requirements that are set with PreviewAndAccept, then the Worker will be able to
          Discover, i.e. see the HIT in their search result, but will not be able to Preview or
          Accept the HIT. ActionsGuarded should not be used in combination with the
          ``RequiredToPreview`` field.

    - **HITReviewStatus** *(string) --*

      Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
      ReviewedAppropriate | ReviewedInappropriate.

    - **NumberOfAssignmentsPending** *(integer) --*

      The number of assignments for this HIT that are being previewed or have been accepted by
      Workers, but have not yet been submitted, returned, or abandoned.

    - **NumberOfAssignmentsAvailable** *(integer) --*

      The number of assignments for this HIT that are available for Workers to accept.

    - **NumberOfAssignmentsCompleted** *(integer) --*

      The number of assignments for this HIT that have been approved or rejected.
    """


_ListHITsForQualificationTypePaginateResponseTypeDef = TypedDict(
    "_ListHITsForQualificationTypePaginateResponseTypeDef",
    {
        "NumResults": int,
        "HITs": List[ListHITsForQualificationTypePaginateResponseHITsTypeDef],
    },
    total=False,
)


class ListHITsForQualificationTypePaginateResponseTypeDef(
    _ListHITsForQualificationTypePaginateResponseTypeDef
):
    """
    Type definition for `ListHITsForQualificationTypePaginate` `Response`

    - **NumResults** *(integer) --*

      The number of HITs on this page in the filtered results list, equivalent to the number of
      HITs being returned by this call.

    - **HITs** *(list) --*

      The list of HIT elements returned by the query.

      - *(dict) --*

        The HIT data structure represents a single HIT, including all the information necessary for
        a Worker to accept and complete the HIT.

        - **HITId** *(string) --*

          A unique identifier for the HIT.

        - **HITTypeId** *(string) --*

          The ID of the HIT type of this HIT

        - **HITGroupId** *(string) --*

          The ID of the HIT Group of this HIT.

        - **HITLayoutId** *(string) --*

          The ID of the HIT Layout of this HIT.

        - **CreationTime** *(datetime) --*

          The date and time the HIT was created.

        - **Title** *(string) --*

          The title of the HIT.

        - **Description** *(string) --*

          A general description of the HIT.

        - **Question** *(string) --*

          The data the Worker completing the HIT uses produce the results. This is either either a
          QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

        - **Keywords** *(string) --*

          One or more words or phrases that describe the HIT, separated by commas. Search terms
          similar to the keywords of a HIT are more likely to have the HIT in the search results.

        - **HITStatus** *(string) --*

          The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
          Reviewable | Reviewing | Disposed.

        - **MaxAssignments** *(integer) --*

          The number of times the HIT can be accepted and completed before the HIT becomes
          unavailable.

        - **Reward** *(string) --*

          A string representing a currency amount.

        - **AutoApprovalDelayInSeconds** *(integer) --*

          The amount of time, in seconds, after the Worker submits an assignment for the HIT that
          the results are automatically approved by Amazon Mechanical Turk. This is the amount of
          time the Requester has to reject an assignment submitted by a Worker before the
          assignment is auto-approved and the Worker is paid.

        - **Expiration** *(datetime) --*

          The date and time the HIT expires.

        - **AssignmentDurationInSeconds** *(integer) --*

          The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

        - **RequesterAnnotation** *(string) --*

          An arbitrary data field the Requester who created the HIT can use. This field is visible
          only to the creator of the HIT.

        - **QualificationRequirements** *(list) --*

          Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
          have between zero and ten Qualification requirements. All requirements must be met in
          order for a Worker to accept the HIT. Additionally, other actions can be restricted using
          the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

          - *(dict) --*

            The QualificationRequirement data structure describes a Qualification that a Worker
            must have before the Worker is allowed to accept a HIT. A requirement may optionally
            state that a Worker must have the Qualification in order to preview the HIT, or see the
            HIT in search results.

            - **QualificationTypeId** *(string) --*

              The ID of the Qualification type for the requirement.

            - **Comparator** *(string) --*

              The kind of comparison to make against a Qualification's value. You can compare a
              Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
              GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
              compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
              You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
              values. Lastly, a Qualification requirement can also test if a Qualification Exists
              or DoesNotExist in the user's profile, regardless of its value.

            - **IntegerValues** *(list) --*

              The integer value to compare against the Qualification's value. IntegerValue must not
              be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
              the Qualification type has an integer value; it cannot be used with the Worker_Locale
              QualificationType ID. When performing a set comparison by using the In or the NotIn
              comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
              data structure.

              - *(integer) --*

            - **LocaleValues** *(list) --*

              The locale value to compare against the Qualification's value. The local value must
              be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
              only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
              with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
              LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
              a set comparison by using the In or the NotIn comparator, you can use up to 30
              LocaleValue elements in a QualificationRequirement data structure.

              - *(dict) --*

                The Locale data structure represents a geographical region or location.

                - **Country** *(string) --*

                  The country of the locale. Must be a valid ISO 3166 country code. For example,
                  the code US refers to the United States of America.

                - **Subdivision** *(string) --*

                  The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
                  example, the code WA refers to the state of Washington.

            - **RequiredToPreview** *(boolean) --*

              DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
              the question data for the HIT will not be shown when a Worker whose Qualifications do
              not meet this requirement tries to preview the HIT. That is, a Worker's
              Qualifications must meet all of the requirements for which RequiredToPreview is true
              in order to preview the HIT. If a Worker meets all of the requirements where
              RequiredToPreview is true (or if there are no such requirements), but does not meet
              all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
              question data, but will not be allowed to accept and complete the HIT. The default is
              false. This should not be used in combination with the ``ActionsGuarded`` field.

            - **ActionsGuarded** *(string) --*

              Setting this attribute prevents Workers whose Qualifications do not meet this
              QualificationRequirement from taking the specified action. Valid arguments include
              "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
              search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
              see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
              accept, preview, or see the HIT in their search results). It's possible for you to
              create a HIT with multiple QualificationRequirements (which can have different values
              for the ActionGuarded attribute). In this case, the Worker is only permitted to
              perform an action when they have met all QualificationRequirements guarding the
              action. The actions in the order of least restrictive to most restrictive are
              Discover, Preview and Accept. For example, if a Worker meets all
              QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
              all requirements that are set with PreviewAndAccept, then the Worker will be able to
              Discover, i.e. see the HIT in their search result, but will not be able to Preview or
              Accept the HIT. ActionsGuarded should not be used in combination with the
              ``RequiredToPreview`` field.

        - **HITReviewStatus** *(string) --*

          Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
          ReviewedAppropriate | ReviewedInappropriate.

        - **NumberOfAssignmentsPending** *(integer) --*

          The number of assignments for this HIT that are being previewed or have been accepted by
          Workers, but have not yet been submitted, returned, or abandoned.

        - **NumberOfAssignmentsAvailable** *(integer) --*

          The number of assignments for this HIT that are available for Workers to accept.

        - **NumberOfAssignmentsCompleted** *(integer) --*

          The number of assignments for this HIT that have been approved or rejected.
    """


_ListHITsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHITsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHITsPaginatePaginationConfigTypeDef(_ListHITsPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListHITsPaginate` `PaginationConfig`

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


_ListHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ListHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ListHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef(
    _ListHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef
):
    """
    Type definition for `ListHITsPaginateResponseHITsQualificationRequirements` `LocaleValues`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --*

      The country of the locale. Must be a valid ISO 3166 country code. For example,
      the code US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
      example, the code WA refers to the state of Washington.
    """


_ListHITsPaginateResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "_ListHITsPaginateResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": str,
        "IntegerValues": List[int],
        "LocaleValues": List[
            ListHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": str,
    },
    total=False,
)


class ListHITsPaginateResponseHITsQualificationRequirementsTypeDef(
    _ListHITsPaginateResponseHITsQualificationRequirementsTypeDef
):
    """
    Type definition for `ListHITsPaginateResponseHITs` `QualificationRequirements`

    The QualificationRequirement data structure describes a Qualification that a Worker
    must have before the Worker is allowed to accept a HIT. A requirement may optionally
    state that a Worker must have the Qualification in order to preview the HIT, or see the
    HIT in search results.

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type for the requirement.

    - **Comparator** *(string) --*

      The kind of comparison to make against a Qualification's value. You can compare a
      Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
      GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
      compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
      You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
      values. Lastly, a Qualification requirement can also test if a Qualification Exists
      or DoesNotExist in the user's profile, regardless of its value.

    - **IntegerValues** *(list) --*

      The integer value to compare against the Qualification's value. IntegerValue must not
      be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
      the Qualification type has an integer value; it cannot be used with the Worker_Locale
      QualificationType ID. When performing a set comparison by using the In or the NotIn
      comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
      data structure.

      - *(integer) --*

    - **LocaleValues** *(list) --*

      The locale value to compare against the Qualification's value. The local value must
      be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
      only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
      with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
      LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
      a set comparison by using the In or the NotIn comparator, you can use up to 30
      LocaleValue elements in a QualificationRequirement data structure.

      - *(dict) --*

        The Locale data structure represents a geographical region or location.

        - **Country** *(string) --*

          The country of the locale. Must be a valid ISO 3166 country code. For example,
          the code US refers to the United States of America.

        - **Subdivision** *(string) --*

          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
          example, the code WA refers to the state of Washington.

    - **RequiredToPreview** *(boolean) --*

      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
      the question data for the HIT will not be shown when a Worker whose Qualifications do
      not meet this requirement tries to preview the HIT. That is, a Worker's
      Qualifications must meet all of the requirements for which RequiredToPreview is true
      in order to preview the HIT. If a Worker meets all of the requirements where
      RequiredToPreview is true (or if there are no such requirements), but does not meet
      all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
      question data, but will not be allowed to accept and complete the HIT. The default is
      false. This should not be used in combination with the ``ActionsGuarded`` field.

    - **ActionsGuarded** *(string) --*

      Setting this attribute prevents Workers whose Qualifications do not meet this
      QualificationRequirement from taking the specified action. Valid arguments include
      "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
      search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
      see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
      accept, preview, or see the HIT in their search results). It's possible for you to
      create a HIT with multiple QualificationRequirements (which can have different values
      for the ActionGuarded attribute). In this case, the Worker is only permitted to
      perform an action when they have met all QualificationRequirements guarding the
      action. The actions in the order of least restrictive to most restrictive are
      Discover, Preview and Accept. For example, if a Worker meets all
      QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
      all requirements that are set with PreviewAndAccept, then the Worker will be able to
      Discover, i.e. see the HIT in their search result, but will not be able to Preview or
      Accept the HIT. ActionsGuarded should not be used in combination with the
      ``RequiredToPreview`` field.
    """


_ListHITsPaginateResponseHITsTypeDef = TypedDict(
    "_ListHITsPaginateResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": str,
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ListHITsPaginateResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": str,
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ListHITsPaginateResponseHITsTypeDef(_ListHITsPaginateResponseHITsTypeDef):
    """
    Type definition for `ListHITsPaginateResponse` `HITs`

    The HIT data structure represents a single HIT, including all the information necessary for
    a Worker to accept and complete the HIT.

    - **HITId** *(string) --*

      A unique identifier for the HIT.

    - **HITTypeId** *(string) --*

      The ID of the HIT type of this HIT

    - **HITGroupId** *(string) --*

      The ID of the HIT Group of this HIT.

    - **HITLayoutId** *(string) --*

      The ID of the HIT Layout of this HIT.

    - **CreationTime** *(datetime) --*

      The date and time the HIT was created.

    - **Title** *(string) --*

      The title of the HIT.

    - **Description** *(string) --*

      A general description of the HIT.

    - **Question** *(string) --*

      The data the Worker completing the HIT uses produce the results. This is either either a
      QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

    - **Keywords** *(string) --*

      One or more words or phrases that describe the HIT, separated by commas. Search terms
      similar to the keywords of a HIT are more likely to have the HIT in the search results.

    - **HITStatus** *(string) --*

      The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
      Reviewable | Reviewing | Disposed.

    - **MaxAssignments** *(integer) --*

      The number of times the HIT can be accepted and completed before the HIT becomes
      unavailable.

    - **Reward** *(string) --*

      A string representing a currency amount.

    - **AutoApprovalDelayInSeconds** *(integer) --*

      The amount of time, in seconds, after the Worker submits an assignment for the HIT that
      the results are automatically approved by Amazon Mechanical Turk. This is the amount of
      time the Requester has to reject an assignment submitted by a Worker before the
      assignment is auto-approved and the Worker is paid.

    - **Expiration** *(datetime) --*

      The date and time the HIT expires.

    - **AssignmentDurationInSeconds** *(integer) --*

      The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

    - **RequesterAnnotation** *(string) --*

      An arbitrary data field the Requester who created the HIT can use. This field is visible
      only to the creator of the HIT.

    - **QualificationRequirements** *(list) --*

      Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
      have between zero and ten Qualification requirements. All requirements must be met in
      order for a Worker to accept the HIT. Additionally, other actions can be restricted using
      the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

      - *(dict) --*

        The QualificationRequirement data structure describes a Qualification that a Worker
        must have before the Worker is allowed to accept a HIT. A requirement may optionally
        state that a Worker must have the Qualification in order to preview the HIT, or see the
        HIT in search results.

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type for the requirement.

        - **Comparator** *(string) --*

          The kind of comparison to make against a Qualification's value. You can compare a
          Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
          GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
          compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
          You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
          values. Lastly, a Qualification requirement can also test if a Qualification Exists
          or DoesNotExist in the user's profile, regardless of its value.

        - **IntegerValues** *(list) --*

          The integer value to compare against the Qualification's value. IntegerValue must not
          be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
          the Qualification type has an integer value; it cannot be used with the Worker_Locale
          QualificationType ID. When performing a set comparison by using the In or the NotIn
          comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
          data structure.

          - *(integer) --*

        - **LocaleValues** *(list) --*

          The locale value to compare against the Qualification's value. The local value must
          be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
          only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
          with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
          LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
          a set comparison by using the In or the NotIn comparator, you can use up to 30
          LocaleValue elements in a QualificationRequirement data structure.

          - *(dict) --*

            The Locale data structure represents a geographical region or location.

            - **Country** *(string) --*

              The country of the locale. Must be a valid ISO 3166 country code. For example,
              the code US refers to the United States of America.

            - **Subdivision** *(string) --*

              The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
              example, the code WA refers to the state of Washington.

        - **RequiredToPreview** *(boolean) --*

          DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
          the question data for the HIT will not be shown when a Worker whose Qualifications do
          not meet this requirement tries to preview the HIT. That is, a Worker's
          Qualifications must meet all of the requirements for which RequiredToPreview is true
          in order to preview the HIT. If a Worker meets all of the requirements where
          RequiredToPreview is true (or if there are no such requirements), but does not meet
          all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
          question data, but will not be allowed to accept and complete the HIT. The default is
          false. This should not be used in combination with the ``ActionsGuarded`` field.

        - **ActionsGuarded** *(string) --*

          Setting this attribute prevents Workers whose Qualifications do not meet this
          QualificationRequirement from taking the specified action. Valid arguments include
          "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
          search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
          see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
          accept, preview, or see the HIT in their search results). It's possible for you to
          create a HIT with multiple QualificationRequirements (which can have different values
          for the ActionGuarded attribute). In this case, the Worker is only permitted to
          perform an action when they have met all QualificationRequirements guarding the
          action. The actions in the order of least restrictive to most restrictive are
          Discover, Preview and Accept. For example, if a Worker meets all
          QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
          all requirements that are set with PreviewAndAccept, then the Worker will be able to
          Discover, i.e. see the HIT in their search result, but will not be able to Preview or
          Accept the HIT. ActionsGuarded should not be used in combination with the
          ``RequiredToPreview`` field.

    - **HITReviewStatus** *(string) --*

      Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
      ReviewedAppropriate | ReviewedInappropriate.

    - **NumberOfAssignmentsPending** *(integer) --*

      The number of assignments for this HIT that are being previewed or have been accepted by
      Workers, but have not yet been submitted, returned, or abandoned.

    - **NumberOfAssignmentsAvailable** *(integer) --*

      The number of assignments for this HIT that are available for Workers to accept.

    - **NumberOfAssignmentsCompleted** *(integer) --*

      The number of assignments for this HIT that have been approved or rejected.
    """


_ListHITsPaginateResponseTypeDef = TypedDict(
    "_ListHITsPaginateResponseTypeDef",
    {"NumResults": int, "HITs": List[ListHITsPaginateResponseHITsTypeDef]},
    total=False,
)


class ListHITsPaginateResponseTypeDef(_ListHITsPaginateResponseTypeDef):
    """
    Type definition for `ListHITsPaginate` `Response`

    - **NumResults** *(integer) --*

      The number of HITs on this page in the filtered results list, equivalent to the number of
      HITs being returned by this call.

    - **HITs** *(list) --*

      The list of HIT elements returned by the query.

      - *(dict) --*

        The HIT data structure represents a single HIT, including all the information necessary for
        a Worker to accept and complete the HIT.

        - **HITId** *(string) --*

          A unique identifier for the HIT.

        - **HITTypeId** *(string) --*

          The ID of the HIT type of this HIT

        - **HITGroupId** *(string) --*

          The ID of the HIT Group of this HIT.

        - **HITLayoutId** *(string) --*

          The ID of the HIT Layout of this HIT.

        - **CreationTime** *(datetime) --*

          The date and time the HIT was created.

        - **Title** *(string) --*

          The title of the HIT.

        - **Description** *(string) --*

          A general description of the HIT.

        - **Question** *(string) --*

          The data the Worker completing the HIT uses produce the results. This is either either a
          QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

        - **Keywords** *(string) --*

          One or more words or phrases that describe the HIT, separated by commas. Search terms
          similar to the keywords of a HIT are more likely to have the HIT in the search results.

        - **HITStatus** *(string) --*

          The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
          Reviewable | Reviewing | Disposed.

        - **MaxAssignments** *(integer) --*

          The number of times the HIT can be accepted and completed before the HIT becomes
          unavailable.

        - **Reward** *(string) --*

          A string representing a currency amount.

        - **AutoApprovalDelayInSeconds** *(integer) --*

          The amount of time, in seconds, after the Worker submits an assignment for the HIT that
          the results are automatically approved by Amazon Mechanical Turk. This is the amount of
          time the Requester has to reject an assignment submitted by a Worker before the
          assignment is auto-approved and the Worker is paid.

        - **Expiration** *(datetime) --*

          The date and time the HIT expires.

        - **AssignmentDurationInSeconds** *(integer) --*

          The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

        - **RequesterAnnotation** *(string) --*

          An arbitrary data field the Requester who created the HIT can use. This field is visible
          only to the creator of the HIT.

        - **QualificationRequirements** *(list) --*

          Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
          have between zero and ten Qualification requirements. All requirements must be met in
          order for a Worker to accept the HIT. Additionally, other actions can be restricted using
          the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

          - *(dict) --*

            The QualificationRequirement data structure describes a Qualification that a Worker
            must have before the Worker is allowed to accept a HIT. A requirement may optionally
            state that a Worker must have the Qualification in order to preview the HIT, or see the
            HIT in search results.

            - **QualificationTypeId** *(string) --*

              The ID of the Qualification type for the requirement.

            - **Comparator** *(string) --*

              The kind of comparison to make against a Qualification's value. You can compare a
              Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
              GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
              compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
              You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
              values. Lastly, a Qualification requirement can also test if a Qualification Exists
              or DoesNotExist in the user's profile, regardless of its value.

            - **IntegerValues** *(list) --*

              The integer value to compare against the Qualification's value. IntegerValue must not
              be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
              the Qualification type has an integer value; it cannot be used with the Worker_Locale
              QualificationType ID. When performing a set comparison by using the In or the NotIn
              comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
              data structure.

              - *(integer) --*

            - **LocaleValues** *(list) --*

              The locale value to compare against the Qualification's value. The local value must
              be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
              only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
              with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
              LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
              a set comparison by using the In or the NotIn comparator, you can use up to 30
              LocaleValue elements in a QualificationRequirement data structure.

              - *(dict) --*

                The Locale data structure represents a geographical region or location.

                - **Country** *(string) --*

                  The country of the locale. Must be a valid ISO 3166 country code. For example,
                  the code US refers to the United States of America.

                - **Subdivision** *(string) --*

                  The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
                  example, the code WA refers to the state of Washington.

            - **RequiredToPreview** *(boolean) --*

              DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
              the question data for the HIT will not be shown when a Worker whose Qualifications do
              not meet this requirement tries to preview the HIT. That is, a Worker's
              Qualifications must meet all of the requirements for which RequiredToPreview is true
              in order to preview the HIT. If a Worker meets all of the requirements where
              RequiredToPreview is true (or if there are no such requirements), but does not meet
              all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
              question data, but will not be allowed to accept and complete the HIT. The default is
              false. This should not be used in combination with the ``ActionsGuarded`` field.

            - **ActionsGuarded** *(string) --*

              Setting this attribute prevents Workers whose Qualifications do not meet this
              QualificationRequirement from taking the specified action. Valid arguments include
              "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
              search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
              see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
              accept, preview, or see the HIT in their search results). It's possible for you to
              create a HIT with multiple QualificationRequirements (which can have different values
              for the ActionGuarded attribute). In this case, the Worker is only permitted to
              perform an action when they have met all QualificationRequirements guarding the
              action. The actions in the order of least restrictive to most restrictive are
              Discover, Preview and Accept. For example, if a Worker meets all
              QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
              all requirements that are set with PreviewAndAccept, then the Worker will be able to
              Discover, i.e. see the HIT in their search result, but will not be able to Preview or
              Accept the HIT. ActionsGuarded should not be used in combination with the
              ``RequiredToPreview`` field.

        - **HITReviewStatus** *(string) --*

          Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
          ReviewedAppropriate | ReviewedInappropriate.

        - **NumberOfAssignmentsPending** *(integer) --*

          The number of assignments for this HIT that are being previewed or have been accepted by
          Workers, but have not yet been submitted, returned, or abandoned.

        - **NumberOfAssignmentsAvailable** *(integer) --*

          The number of assignments for this HIT that are available for Workers to accept.

        - **NumberOfAssignmentsCompleted** *(integer) --*

          The number of assignments for this HIT that have been approved or rejected.
    """


_ListQualificationRequestsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListQualificationRequestsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListQualificationRequestsPaginatePaginationConfigTypeDef(
    _ListQualificationRequestsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListQualificationRequestsPaginate` `PaginationConfig`

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


_ListQualificationRequestsPaginateResponseQualificationRequestsTypeDef = TypedDict(
    "_ListQualificationRequestsPaginateResponseQualificationRequestsTypeDef",
    {
        "QualificationRequestId": str,
        "QualificationTypeId": str,
        "WorkerId": str,
        "Test": str,
        "Answer": str,
        "SubmitTime": datetime,
    },
    total=False,
)


class ListQualificationRequestsPaginateResponseQualificationRequestsTypeDef(
    _ListQualificationRequestsPaginateResponseQualificationRequestsTypeDef
):
    """
    Type definition for `ListQualificationRequestsPaginateResponse` `QualificationRequests`

    The QualificationRequest data structure represents a request a Worker has made for a
    Qualification.

    - **QualificationRequestId** *(string) --*

      The ID of the Qualification request, a unique identifier generated when the request was
      submitted.

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type the Worker is requesting, as returned by the
      CreateQualificationType operation.

    - **WorkerId** *(string) --*

      The ID of the Worker requesting the Qualification.

    - **Test** *(string) --*

      The contents of the Qualification test that was presented to the Worker, if the type has
      a test and the Worker has submitted answers. This value is identical to the QuestionForm
      associated with the Qualification type at the time the Worker requests the Qualification.

    - **Answer** *(string) --*

      The Worker's answers for the Qualification type's test contained in a QuestionFormAnswers
      document, if the type has a test and the Worker has submitted answers. If the Worker does
      not provide any answers, Answer may be empty.

    - **SubmitTime** *(datetime) --*

      The date and time the Qualification request had a status of Submitted. This is either the
      time the Worker submitted answers for a Qualification test, or the time the Worker
      requested the Qualification if the Qualification type does not have a test.
    """


_ListQualificationRequestsPaginateResponseTypeDef = TypedDict(
    "_ListQualificationRequestsPaginateResponseTypeDef",
    {
        "NumResults": int,
        "QualificationRequests": List[
            ListQualificationRequestsPaginateResponseQualificationRequestsTypeDef
        ],
    },
    total=False,
)


class ListQualificationRequestsPaginateResponseTypeDef(
    _ListQualificationRequestsPaginateResponseTypeDef
):
    """
    Type definition for `ListQualificationRequestsPaginate` `Response`

    - **NumResults** *(integer) --*

      The number of Qualification requests on this page in the filtered results list, equivalent to
      the number of Qualification requests being returned by this call.

    - **QualificationRequests** *(list) --*

      The Qualification request. The response includes one QualificationRequest element for each
      Qualification request returned by the query.

      - *(dict) --*

        The QualificationRequest data structure represents a request a Worker has made for a
        Qualification.

        - **QualificationRequestId** *(string) --*

          The ID of the Qualification request, a unique identifier generated when the request was
          submitted.

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type the Worker is requesting, as returned by the
          CreateQualificationType operation.

        - **WorkerId** *(string) --*

          The ID of the Worker requesting the Qualification.

        - **Test** *(string) --*

          The contents of the Qualification test that was presented to the Worker, if the type has
          a test and the Worker has submitted answers. This value is identical to the QuestionForm
          associated with the Qualification type at the time the Worker requests the Qualification.

        - **Answer** *(string) --*

          The Worker's answers for the Qualification type's test contained in a QuestionFormAnswers
          document, if the type has a test and the Worker has submitted answers. If the Worker does
          not provide any answers, Answer may be empty.

        - **SubmitTime** *(datetime) --*

          The date and time the Qualification request had a status of Submitted. This is either the
          time the Worker submitted answers for a Qualification test, or the time the Worker
          requested the Qualification if the Qualification type does not have a test.
    """


_ListQualificationTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListQualificationTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListQualificationTypesPaginatePaginationConfigTypeDef(
    _ListQualificationTypesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListQualificationTypesPaginate` `PaginationConfig`

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


_ListQualificationTypesPaginateResponseQualificationTypesTypeDef = TypedDict(
    "_ListQualificationTypesPaginateResponseQualificationTypesTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": str,
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)


class ListQualificationTypesPaginateResponseQualificationTypesTypeDef(
    _ListQualificationTypesPaginateResponseQualificationTypesTypeDef
):
    """
    Type definition for `ListQualificationTypesPaginateResponse` `QualificationTypes`

    The QualificationType data structure represents a Qualification type, a description of a
    property of a Worker that must match the requirements of a HIT for the Worker to be able to
    accept the HIT. The type also describes how a Worker can obtain a Qualification of that
    type, such as through a Qualification test.

    - **QualificationTypeId** *(string) --*

      A unique identifier for the Qualification type. A Qualification type is given a
      Qualification type ID when you call the CreateQualificationType operation.

    - **CreationTime** *(datetime) --*

      The date and time the Qualification type was created.

    - **Name** *(string) --*

      The name of the Qualification type. The type name is used to identify the type, and to
      find the type using a Qualification type search.

    - **Description** *(string) --*

      A long description for the Qualification type.

    - **Keywords** *(string) --*

      One or more words or phrases that describe theQualification type, separated by commas.
      The Keywords make the type easier to find using a search.

    - **QualificationTypeStatus** *(string) --*

      The status of the Qualification type. A Qualification type's status determines if users
      can apply to receive a Qualification of this type, and if HITs can be created with
      requirements based on this type. Valid values are Active | Inactive.

    - **Test** *(string) --*

      The questions for a Qualification test associated with this Qualification type that a
      user can take to obtain a Qualification of this type. This parameter must be specified if
      AnswerKey is present. A Qualification type cannot have both a specified Test parameter
      and an AutoGranted value of true.

    - **TestDurationInSeconds** *(integer) --*

      The amount of time, in seconds, given to a Worker to complete the Qualification test,
      beginning from the time the Worker requests the Qualification.

    - **AnswerKey** *(string) --*

      The answers to the Qualification test specified in the Test parameter.

    - **RetryDelayInSeconds** *(integer) --*

      The amount of time, in seconds, Workers must wait after taking the Qualification test
      before they can take it again. Workers can take a Qualification test multiple times if
      they were not granted the Qualification from a previous attempt, or if the test offers a
      gradient score and they want a better score. If not specified, retries are disabled and
      Workers can request a Qualification only once.

    - **IsRequestable** *(boolean) --*

      Specifies whether the Qualification type is one that a user can request through the
      Amazon Mechanical Turk web site, such as by taking a Qualification test. This value is
      False for Qualifications assigned automatically by the system. Valid values are True |
      False.

    - **AutoGranted** *(boolean) --*

      Specifies that requests for the Qualification type are granted immediately, without
      prompting the Worker with a Qualification test. Valid values are True | False.

    - **AutoGrantedValue** *(integer) --*

      The Qualification integer value to use for automatically granted Qualifications, if
      AutoGranted is true. This is 1 by default.
    """


_ListQualificationTypesPaginateResponseTypeDef = TypedDict(
    "_ListQualificationTypesPaginateResponseTypeDef",
    {
        "NumResults": int,
        "QualificationTypes": List[
            ListQualificationTypesPaginateResponseQualificationTypesTypeDef
        ],
    },
    total=False,
)


class ListQualificationTypesPaginateResponseTypeDef(
    _ListQualificationTypesPaginateResponseTypeDef
):
    """
    Type definition for `ListQualificationTypesPaginate` `Response`

    - **NumResults** *(integer) --*

      The number of Qualification types on this page in the filtered results list, equivalent to
      the number of types this operation returns.

    - **QualificationTypes** *(list) --*

      The list of QualificationType elements returned by the query.

      - *(dict) --*

        The QualificationType data structure represents a Qualification type, a description of a
        property of a Worker that must match the requirements of a HIT for the Worker to be able to
        accept the HIT. The type also describes how a Worker can obtain a Qualification of that
        type, such as through a Qualification test.

        - **QualificationTypeId** *(string) --*

          A unique identifier for the Qualification type. A Qualification type is given a
          Qualification type ID when you call the CreateQualificationType operation.

        - **CreationTime** *(datetime) --*

          The date and time the Qualification type was created.

        - **Name** *(string) --*

          The name of the Qualification type. The type name is used to identify the type, and to
          find the type using a Qualification type search.

        - **Description** *(string) --*

          A long description for the Qualification type.

        - **Keywords** *(string) --*

          One or more words or phrases that describe theQualification type, separated by commas.
          The Keywords make the type easier to find using a search.

        - **QualificationTypeStatus** *(string) --*

          The status of the Qualification type. A Qualification type's status determines if users
          can apply to receive a Qualification of this type, and if HITs can be created with
          requirements based on this type. Valid values are Active | Inactive.

        - **Test** *(string) --*

          The questions for a Qualification test associated with this Qualification type that a
          user can take to obtain a Qualification of this type. This parameter must be specified if
          AnswerKey is present. A Qualification type cannot have both a specified Test parameter
          and an AutoGranted value of true.

        - **TestDurationInSeconds** *(integer) --*

          The amount of time, in seconds, given to a Worker to complete the Qualification test,
          beginning from the time the Worker requests the Qualification.

        - **AnswerKey** *(string) --*

          The answers to the Qualification test specified in the Test parameter.

        - **RetryDelayInSeconds** *(integer) --*

          The amount of time, in seconds, Workers must wait after taking the Qualification test
          before they can take it again. Workers can take a Qualification test multiple times if
          they were not granted the Qualification from a previous attempt, or if the test offers a
          gradient score and they want a better score. If not specified, retries are disabled and
          Workers can request a Qualification only once.

        - **IsRequestable** *(boolean) --*

          Specifies whether the Qualification type is one that a user can request through the
          Amazon Mechanical Turk web site, such as by taking a Qualification test. This value is
          False for Qualifications assigned automatically by the system. Valid values are True |
          False.

        - **AutoGranted** *(boolean) --*

          Specifies that requests for the Qualification type are granted immediately, without
          prompting the Worker with a Qualification test. Valid values are True | False.

        - **AutoGrantedValue** *(integer) --*

          The Qualification integer value to use for automatically granted Qualifications, if
          AutoGranted is true. This is 1 by default.
    """


_ListReviewableHITsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListReviewableHITsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListReviewableHITsPaginatePaginationConfigTypeDef(
    _ListReviewableHITsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListReviewableHITsPaginate` `PaginationConfig`

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


_ListReviewableHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ListReviewableHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ListReviewableHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef(
    _ListReviewableHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef
):
    """
    Type definition for `ListReviewableHITsPaginateResponseHITsQualificationRequirements` `LocaleValues`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --*

      The country of the locale. Must be a valid ISO 3166 country code. For example,
      the code US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
      example, the code WA refers to the state of Washington.
    """


_ListReviewableHITsPaginateResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "_ListReviewableHITsPaginateResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": str,
        "IntegerValues": List[int],
        "LocaleValues": List[
            ListReviewableHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": str,
    },
    total=False,
)


class ListReviewableHITsPaginateResponseHITsQualificationRequirementsTypeDef(
    _ListReviewableHITsPaginateResponseHITsQualificationRequirementsTypeDef
):
    """
    Type definition for `ListReviewableHITsPaginateResponseHITs` `QualificationRequirements`

    The QualificationRequirement data structure describes a Qualification that a Worker
    must have before the Worker is allowed to accept a HIT. A requirement may optionally
    state that a Worker must have the Qualification in order to preview the HIT, or see the
    HIT in search results.

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type for the requirement.

    - **Comparator** *(string) --*

      The kind of comparison to make against a Qualification's value. You can compare a
      Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
      GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
      compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
      You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
      values. Lastly, a Qualification requirement can also test if a Qualification Exists
      or DoesNotExist in the user's profile, regardless of its value.

    - **IntegerValues** *(list) --*

      The integer value to compare against the Qualification's value. IntegerValue must not
      be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
      the Qualification type has an integer value; it cannot be used with the Worker_Locale
      QualificationType ID. When performing a set comparison by using the In or the NotIn
      comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
      data structure.

      - *(integer) --*

    - **LocaleValues** *(list) --*

      The locale value to compare against the Qualification's value. The local value must
      be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
      only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
      with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
      LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
      a set comparison by using the In or the NotIn comparator, you can use up to 30
      LocaleValue elements in a QualificationRequirement data structure.

      - *(dict) --*

        The Locale data structure represents a geographical region or location.

        - **Country** *(string) --*

          The country of the locale. Must be a valid ISO 3166 country code. For example,
          the code US refers to the United States of America.

        - **Subdivision** *(string) --*

          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
          example, the code WA refers to the state of Washington.

    - **RequiredToPreview** *(boolean) --*

      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
      the question data for the HIT will not be shown when a Worker whose Qualifications do
      not meet this requirement tries to preview the HIT. That is, a Worker's
      Qualifications must meet all of the requirements for which RequiredToPreview is true
      in order to preview the HIT. If a Worker meets all of the requirements where
      RequiredToPreview is true (or if there are no such requirements), but does not meet
      all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
      question data, but will not be allowed to accept and complete the HIT. The default is
      false. This should not be used in combination with the ``ActionsGuarded`` field.

    - **ActionsGuarded** *(string) --*

      Setting this attribute prevents Workers whose Qualifications do not meet this
      QualificationRequirement from taking the specified action. Valid arguments include
      "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
      search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
      see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
      accept, preview, or see the HIT in their search results). It's possible for you to
      create a HIT with multiple QualificationRequirements (which can have different values
      for the ActionGuarded attribute). In this case, the Worker is only permitted to
      perform an action when they have met all QualificationRequirements guarding the
      action. The actions in the order of least restrictive to most restrictive are
      Discover, Preview and Accept. For example, if a Worker meets all
      QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
      all requirements that are set with PreviewAndAccept, then the Worker will be able to
      Discover, i.e. see the HIT in their search result, but will not be able to Preview or
      Accept the HIT. ActionsGuarded should not be used in combination with the
      ``RequiredToPreview`` field.
    """


_ListReviewableHITsPaginateResponseHITsTypeDef = TypedDict(
    "_ListReviewableHITsPaginateResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": str,
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ListReviewableHITsPaginateResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": str,
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ListReviewableHITsPaginateResponseHITsTypeDef(
    _ListReviewableHITsPaginateResponseHITsTypeDef
):
    """
    Type definition for `ListReviewableHITsPaginateResponse` `HITs`

    The HIT data structure represents a single HIT, including all the information necessary for
    a Worker to accept and complete the HIT.

    - **HITId** *(string) --*

      A unique identifier for the HIT.

    - **HITTypeId** *(string) --*

      The ID of the HIT type of this HIT

    - **HITGroupId** *(string) --*

      The ID of the HIT Group of this HIT.

    - **HITLayoutId** *(string) --*

      The ID of the HIT Layout of this HIT.

    - **CreationTime** *(datetime) --*

      The date and time the HIT was created.

    - **Title** *(string) --*

      The title of the HIT.

    - **Description** *(string) --*

      A general description of the HIT.

    - **Question** *(string) --*

      The data the Worker completing the HIT uses produce the results. This is either either a
      QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

    - **Keywords** *(string) --*

      One or more words or phrases that describe the HIT, separated by commas. Search terms
      similar to the keywords of a HIT are more likely to have the HIT in the search results.

    - **HITStatus** *(string) --*

      The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
      Reviewable | Reviewing | Disposed.

    - **MaxAssignments** *(integer) --*

      The number of times the HIT can be accepted and completed before the HIT becomes
      unavailable.

    - **Reward** *(string) --*

      A string representing a currency amount.

    - **AutoApprovalDelayInSeconds** *(integer) --*

      The amount of time, in seconds, after the Worker submits an assignment for the HIT that
      the results are automatically approved by Amazon Mechanical Turk. This is the amount of
      time the Requester has to reject an assignment submitted by a Worker before the
      assignment is auto-approved and the Worker is paid.

    - **Expiration** *(datetime) --*

      The date and time the HIT expires.

    - **AssignmentDurationInSeconds** *(integer) --*

      The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

    - **RequesterAnnotation** *(string) --*

      An arbitrary data field the Requester who created the HIT can use. This field is visible
      only to the creator of the HIT.

    - **QualificationRequirements** *(list) --*

      Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
      have between zero and ten Qualification requirements. All requirements must be met in
      order for a Worker to accept the HIT. Additionally, other actions can be restricted using
      the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

      - *(dict) --*

        The QualificationRequirement data structure describes a Qualification that a Worker
        must have before the Worker is allowed to accept a HIT. A requirement may optionally
        state that a Worker must have the Qualification in order to preview the HIT, or see the
        HIT in search results.

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type for the requirement.

        - **Comparator** *(string) --*

          The kind of comparison to make against a Qualification's value. You can compare a
          Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
          GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
          compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
          You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
          values. Lastly, a Qualification requirement can also test if a Qualification Exists
          or DoesNotExist in the user's profile, regardless of its value.

        - **IntegerValues** *(list) --*

          The integer value to compare against the Qualification's value. IntegerValue must not
          be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
          the Qualification type has an integer value; it cannot be used with the Worker_Locale
          QualificationType ID. When performing a set comparison by using the In or the NotIn
          comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
          data structure.

          - *(integer) --*

        - **LocaleValues** *(list) --*

          The locale value to compare against the Qualification's value. The local value must
          be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
          only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
          with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
          LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
          a set comparison by using the In or the NotIn comparator, you can use up to 30
          LocaleValue elements in a QualificationRequirement data structure.

          - *(dict) --*

            The Locale data structure represents a geographical region or location.

            - **Country** *(string) --*

              The country of the locale. Must be a valid ISO 3166 country code. For example,
              the code US refers to the United States of America.

            - **Subdivision** *(string) --*

              The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
              example, the code WA refers to the state of Washington.

        - **RequiredToPreview** *(boolean) --*

          DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
          the question data for the HIT will not be shown when a Worker whose Qualifications do
          not meet this requirement tries to preview the HIT. That is, a Worker's
          Qualifications must meet all of the requirements for which RequiredToPreview is true
          in order to preview the HIT. If a Worker meets all of the requirements where
          RequiredToPreview is true (or if there are no such requirements), but does not meet
          all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
          question data, but will not be allowed to accept and complete the HIT. The default is
          false. This should not be used in combination with the ``ActionsGuarded`` field.

        - **ActionsGuarded** *(string) --*

          Setting this attribute prevents Workers whose Qualifications do not meet this
          QualificationRequirement from taking the specified action. Valid arguments include
          "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
          search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
          see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
          accept, preview, or see the HIT in their search results). It's possible for you to
          create a HIT with multiple QualificationRequirements (which can have different values
          for the ActionGuarded attribute). In this case, the Worker is only permitted to
          perform an action when they have met all QualificationRequirements guarding the
          action. The actions in the order of least restrictive to most restrictive are
          Discover, Preview and Accept. For example, if a Worker meets all
          QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
          all requirements that are set with PreviewAndAccept, then the Worker will be able to
          Discover, i.e. see the HIT in their search result, but will not be able to Preview or
          Accept the HIT. ActionsGuarded should not be used in combination with the
          ``RequiredToPreview`` field.

    - **HITReviewStatus** *(string) --*

      Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
      ReviewedAppropriate | ReviewedInappropriate.

    - **NumberOfAssignmentsPending** *(integer) --*

      The number of assignments for this HIT that are being previewed or have been accepted by
      Workers, but have not yet been submitted, returned, or abandoned.

    - **NumberOfAssignmentsAvailable** *(integer) --*

      The number of assignments for this HIT that are available for Workers to accept.

    - **NumberOfAssignmentsCompleted** *(integer) --*

      The number of assignments for this HIT that have been approved or rejected.
    """


_ListReviewableHITsPaginateResponseTypeDef = TypedDict(
    "_ListReviewableHITsPaginateResponseTypeDef",
    {"NumResults": int, "HITs": List[ListReviewableHITsPaginateResponseHITsTypeDef]},
    total=False,
)


class ListReviewableHITsPaginateResponseTypeDef(
    _ListReviewableHITsPaginateResponseTypeDef
):
    """
    Type definition for `ListReviewableHITsPaginate` `Response`

    - **NumResults** *(integer) --*

      The number of HITs on this page in the filtered results list, equivalent to the number of
      HITs being returned by this call.

    - **HITs** *(list) --*

      The list of HIT elements returned by the query.

      - *(dict) --*

        The HIT data structure represents a single HIT, including all the information necessary for
        a Worker to accept and complete the HIT.

        - **HITId** *(string) --*

          A unique identifier for the HIT.

        - **HITTypeId** *(string) --*

          The ID of the HIT type of this HIT

        - **HITGroupId** *(string) --*

          The ID of the HIT Group of this HIT.

        - **HITLayoutId** *(string) --*

          The ID of the HIT Layout of this HIT.

        - **CreationTime** *(datetime) --*

          The date and time the HIT was created.

        - **Title** *(string) --*

          The title of the HIT.

        - **Description** *(string) --*

          A general description of the HIT.

        - **Question** *(string) --*

          The data the Worker completing the HIT uses produce the results. This is either either a
          QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

        - **Keywords** *(string) --*

          One or more words or phrases that describe the HIT, separated by commas. Search terms
          similar to the keywords of a HIT are more likely to have the HIT in the search results.

        - **HITStatus** *(string) --*

          The status of the HIT and its assignments. Valid Values are Assignable | Unassignable |
          Reviewable | Reviewing | Disposed.

        - **MaxAssignments** *(integer) --*

          The number of times the HIT can be accepted and completed before the HIT becomes
          unavailable.

        - **Reward** *(string) --*

          A string representing a currency amount.

        - **AutoApprovalDelayInSeconds** *(integer) --*

          The amount of time, in seconds, after the Worker submits an assignment for the HIT that
          the results are automatically approved by Amazon Mechanical Turk. This is the amount of
          time the Requester has to reject an assignment submitted by a Worker before the
          assignment is auto-approved and the Worker is paid.

        - **Expiration** *(datetime) --*

          The date and time the HIT expires.

        - **AssignmentDurationInSeconds** *(integer) --*

          The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

        - **RequesterAnnotation** *(string) --*

          An arbitrary data field the Requester who created the HIT can use. This field is visible
          only to the creator of the HIT.

        - **QualificationRequirements** *(list) --*

          Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can
          have between zero and ten Qualification requirements. All requirements must be met in
          order for a Worker to accept the HIT. Additionally, other actions can be restricted using
          the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure.

          - *(dict) --*

            The QualificationRequirement data structure describes a Qualification that a Worker
            must have before the Worker is allowed to accept a HIT. A requirement may optionally
            state that a Worker must have the Qualification in order to preview the HIT, or see the
            HIT in search results.

            - **QualificationTypeId** *(string) --*

              The ID of the Qualification type for the requirement.

            - **Comparator** *(string) --*

              The kind of comparison to make against a Qualification's value. You can compare a
              Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo,
              GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can
              compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue.
              You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue
              values. Lastly, a Qualification requirement can also test if a Qualification Exists
              or DoesNotExist in the user's profile, regardless of its value.

            - **IntegerValues** *(list) --*

              The integer value to compare against the Qualification's value. IntegerValue must not
              be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if
              the Qualification type has an integer value; it cannot be used with the Worker_Locale
              QualificationType ID. When performing a set comparison by using the In or the NotIn
              comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement
              data structure.

              - *(integer) --*

            - **LocaleValues** *(list) --*

              The locale value to compare against the Qualification's value. The local value must
              be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can
              only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used
              with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single
              LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing
              a set comparison by using the In or the NotIn comparator, you can use up to 30
              LocaleValue elements in a QualificationRequirement data structure.

              - *(dict) --*

                The Locale data structure represents a geographical region or location.

                - **Country** *(string) --*

                  The country of the locale. Must be a valid ISO 3166 country code. For example,
                  the code US refers to the United States of America.

                - **Subdivision** *(string) --*

                  The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
                  example, the code WA refers to the state of Washington.

            - **RequiredToPreview** *(boolean) --*

              DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true,
              the question data for the HIT will not be shown when a Worker whose Qualifications do
              not meet this requirement tries to preview the HIT. That is, a Worker's
              Qualifications must meet all of the requirements for which RequiredToPreview is true
              in order to preview the HIT. If a Worker meets all of the requirements where
              RequiredToPreview is true (or if there are no such requirements), but does not meet
              all of the requirements for the HIT, the Worker will be allowed to preview the HIT's
              question data, but will not be allowed to accept and complete the HIT. The default is
              false. This should not be used in combination with the ``ActionsGuarded`` field.

            - **ActionsGuarded** *(string) --*

              Setting this attribute prevents Workers whose Qualifications do not meet this
              QualificationRequirement from taking the specified action. Valid arguments include
              "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their
              search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can
              see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot
              accept, preview, or see the HIT in their search results). It's possible for you to
              create a HIT with multiple QualificationRequirements (which can have different values
              for the ActionGuarded attribute). In this case, the Worker is only permitted to
              perform an action when they have met all QualificationRequirements guarding the
              action. The actions in the order of least restrictive to most restrictive are
              Discover, Preview and Accept. For example, if a Worker meets all
              QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet
              all requirements that are set with PreviewAndAccept, then the Worker will be able to
              Discover, i.e. see the HIT in their search result, but will not be able to Preview or
              Accept the HIT. ActionsGuarded should not be used in combination with the
              ``RequiredToPreview`` field.

        - **HITReviewStatus** *(string) --*

          Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview |
          ReviewedAppropriate | ReviewedInappropriate.

        - **NumberOfAssignmentsPending** *(integer) --*

          The number of assignments for this HIT that are being previewed or have been accepted by
          Workers, but have not yet been submitted, returned, or abandoned.

        - **NumberOfAssignmentsAvailable** *(integer) --*

          The number of assignments for this HIT that are available for Workers to accept.

        - **NumberOfAssignmentsCompleted** *(integer) --*

          The number of assignments for this HIT that have been approved or rejected.
    """


_ListWorkerBlocksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListWorkerBlocksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListWorkerBlocksPaginatePaginationConfigTypeDef(
    _ListWorkerBlocksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListWorkerBlocksPaginate` `PaginationConfig`

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


_ListWorkerBlocksPaginateResponseWorkerBlocksTypeDef = TypedDict(
    "_ListWorkerBlocksPaginateResponseWorkerBlocksTypeDef",
    {"WorkerId": str, "Reason": str},
    total=False,
)


class ListWorkerBlocksPaginateResponseWorkerBlocksTypeDef(
    _ListWorkerBlocksPaginateResponseWorkerBlocksTypeDef
):
    """
    Type definition for `ListWorkerBlocksPaginateResponse` `WorkerBlocks`

    The WorkerBlock data structure represents a Worker who has been blocked. It has two
    elements: the WorkerId and the Reason for the block.

    - **WorkerId** *(string) --*

      The ID of the Worker who accepted the HIT.

    - **Reason** *(string) --*

      A message explaining the reason the Worker was blocked.
    """


_ListWorkerBlocksPaginateResponseTypeDef = TypedDict(
    "_ListWorkerBlocksPaginateResponseTypeDef",
    {
        "NumResults": int,
        "WorkerBlocks": List[ListWorkerBlocksPaginateResponseWorkerBlocksTypeDef],
    },
    total=False,
)


class ListWorkerBlocksPaginateResponseTypeDef(_ListWorkerBlocksPaginateResponseTypeDef):
    """
    Type definition for `ListWorkerBlocksPaginate` `Response`

    - **NumResults** *(integer) --*

      The number of assignments on the page in the filtered results list, equivalent to the number
      of assignments returned by this call.

    - **WorkerBlocks** *(list) --*

      The list of WorkerBlocks, containing the collection of Worker IDs and reasons for blocking.

      - *(dict) --*

        The WorkerBlock data structure represents a Worker who has been blocked. It has two
        elements: the WorkerId and the Reason for the block.

        - **WorkerId** *(string) --*

          The ID of the Worker who accepted the HIT.

        - **Reason** *(string) --*

          A message explaining the reason the Worker was blocked.
    """


_ListWorkersWithQualificationTypePaginatePaginationConfigTypeDef = TypedDict(
    "_ListWorkersWithQualificationTypePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListWorkersWithQualificationTypePaginatePaginationConfigTypeDef(
    _ListWorkersWithQualificationTypePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListWorkersWithQualificationTypePaginate` `PaginationConfig`

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


_ListWorkersWithQualificationTypePaginateResponseQualificationsLocaleValueTypeDef = TypedDict(
    "_ListWorkersWithQualificationTypePaginateResponseQualificationsLocaleValueTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ListWorkersWithQualificationTypePaginateResponseQualificationsLocaleValueTypeDef(
    _ListWorkersWithQualificationTypePaginateResponseQualificationsLocaleValueTypeDef
):
    """
    Type definition for `ListWorkersWithQualificationTypePaginateResponseQualifications` `LocaleValue`

    The Locale data structure represents a geographical region or location.

    - **Country** *(string) --*

      The country of the locale. Must be a valid ISO 3166 country code. For example, the code
      US refers to the United States of America.

    - **Subdivision** *(string) --*

      The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
      example, the code WA refers to the state of Washington.
    """


_ListWorkersWithQualificationTypePaginateResponseQualificationsTypeDef = TypedDict(
    "_ListWorkersWithQualificationTypePaginateResponseQualificationsTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "GrantTime": datetime,
        "IntegerValue": int,
        "LocaleValue": ListWorkersWithQualificationTypePaginateResponseQualificationsLocaleValueTypeDef,
        "Status": str,
    },
    total=False,
)


class ListWorkersWithQualificationTypePaginateResponseQualificationsTypeDef(
    _ListWorkersWithQualificationTypePaginateResponseQualificationsTypeDef
):
    """
    Type definition for `ListWorkersWithQualificationTypePaginateResponse` `Qualifications`

    The Qualification data structure represents a Qualification assigned to a user, including
    the Qualification type and the value (score).

    - **QualificationTypeId** *(string) --*

      The ID of the Qualification type for the Qualification.

    - **WorkerId** *(string) --*

      The ID of the Worker who possesses the Qualification.

    - **GrantTime** *(datetime) --*

      The date and time the Qualification was granted to the Worker. If the Worker's
      Qualification was revoked, and then re-granted based on a new Qualification request,
      GrantTime is the date and time of the last call to the AcceptQualificationRequest
      operation.

    - **IntegerValue** *(integer) --*

      The value (score) of the Qualification, if the Qualification has an integer value.

    - **LocaleValue** *(dict) --*

      The Locale data structure represents a geographical region or location.

      - **Country** *(string) --*

        The country of the locale. Must be a valid ISO 3166 country code. For example, the code
        US refers to the United States of America.

      - **Subdivision** *(string) --*

        The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
        example, the code WA refers to the state of Washington.

    - **Status** *(string) --*

      The status of the Qualification. Valid values are Granted | Revoked.
    """


_ListWorkersWithQualificationTypePaginateResponseTypeDef = TypedDict(
    "_ListWorkersWithQualificationTypePaginateResponseTypeDef",
    {
        "NumResults": int,
        "Qualifications": List[
            ListWorkersWithQualificationTypePaginateResponseQualificationsTypeDef
        ],
    },
    total=False,
)


class ListWorkersWithQualificationTypePaginateResponseTypeDef(
    _ListWorkersWithQualificationTypePaginateResponseTypeDef
):
    """
    Type definition for `ListWorkersWithQualificationTypePaginate` `Response`

    - **NumResults** *(integer) --*

      The number of Qualifications on this page in the filtered results list, equivalent to the
      number of Qualifications being returned by this call.

    - **Qualifications** *(list) --*

      The list of Qualification elements returned by this call.

      - *(dict) --*

        The Qualification data structure represents a Qualification assigned to a user, including
        the Qualification type and the value (score).

        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type for the Qualification.

        - **WorkerId** *(string) --*

          The ID of the Worker who possesses the Qualification.

        - **GrantTime** *(datetime) --*

          The date and time the Qualification was granted to the Worker. If the Worker's
          Qualification was revoked, and then re-granted based on a new Qualification request,
          GrantTime is the date and time of the last call to the AcceptQualificationRequest
          operation.

        - **IntegerValue** *(integer) --*

          The value (score) of the Qualification, if the Qualification has an integer value.

        - **LocaleValue** *(dict) --*

          The Locale data structure represents a geographical region or location.

          - **Country** *(string) --*

            The country of the locale. Must be a valid ISO 3166 country code. For example, the code
            US refers to the United States of America.

          - **Subdivision** *(string) --*

            The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For
            example, the code WA refers to the state of Washington.

        - **Status** *(string) --*

          The status of the Qualification. Valid values are Granted | Revoked.
    """
