"Main interface for codecommit type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsTypeDef",
    "ClientBatchDescribeMergeConflictsResponseerrorsTypeDef",
    "ClientBatchDescribeMergeConflictsResponseTypeDef",
    "ClientBatchGetCommitsResponsecommitsauthorTypeDef",
    "ClientBatchGetCommitsResponsecommitscommitterTypeDef",
    "ClientBatchGetCommitsResponsecommitsTypeDef",
    "ClientBatchGetCommitsResponseerrorsTypeDef",
    "ClientBatchGetCommitsResponseTypeDef",
    "ClientBatchGetRepositoriesResponserepositoriesTypeDef",
    "ClientBatchGetRepositoriesResponseTypeDef",
    "ClientCreateCommitResponsefilesAddedTypeDef",
    "ClientCreateCommitResponsefilesDeletedTypeDef",
    "ClientCreateCommitResponsefilesUpdatedTypeDef",
    "ClientCreateCommitResponseTypeDef",
    "ClientCreateCommitdeleteFilesTypeDef",
    "ClientCreateCommitputFilessourceFileTypeDef",
    "ClientCreateCommitputFilesTypeDef",
    "ClientCreateCommitsetFileModesTypeDef",
    "ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef",
    "ClientCreatePullRequestResponsepullRequestTypeDef",
    "ClientCreatePullRequestResponseTypeDef",
    "ClientCreatePullRequesttargetsTypeDef",
    "ClientCreateRepositoryResponserepositoryMetadataTypeDef",
    "ClientCreateRepositoryResponseTypeDef",
    "ClientCreateUnreferencedMergeCommitResponseTypeDef",
    "ClientCreateUnreferencedMergeCommitconflictResolutiondeleteFilesTypeDef",
    "ClientCreateUnreferencedMergeCommitconflictResolutionreplaceContentsTypeDef",
    "ClientCreateUnreferencedMergeCommitconflictResolutionsetFileModesTypeDef",
    "ClientCreateUnreferencedMergeCommitconflictResolutionTypeDef",
    "ClientDeleteBranchResponsedeletedBranchTypeDef",
    "ClientDeleteBranchResponseTypeDef",
    "ClientDeleteCommentContentResponsecommentTypeDef",
    "ClientDeleteCommentContentResponseTypeDef",
    "ClientDeleteFileResponseTypeDef",
    "ClientDeleteRepositoryResponseTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadataTypeDef",
    "ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef",
    "ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef",
    "ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef",
    "ClientDescribeMergeConflictsResponsemergeHunksTypeDef",
    "ClientDescribeMergeConflictsResponseTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef",
    "ClientDescribePullRequestEventsResponseTypeDef",
    "ClientGetBlobResponseTypeDef",
    "ClientGetBranchResponsebranchTypeDef",
    "ClientGetBranchResponseTypeDef",
    "ClientGetCommentResponsecommentTypeDef",
    "ClientGetCommentResponseTypeDef",
    "ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef",
    "ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef",
    "ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef",
    "ClientGetCommentsForComparedCommitResponseTypeDef",
    "ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef",
    "ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef",
    "ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef",
    "ClientGetCommentsForPullRequestResponseTypeDef",
    "ClientGetCommitResponsecommitauthorTypeDef",
    "ClientGetCommitResponsecommitcommitterTypeDef",
    "ClientGetCommitResponsecommitTypeDef",
    "ClientGetCommitResponseTypeDef",
    "ClientGetDifferencesResponsedifferencesafterBlobTypeDef",
    "ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef",
    "ClientGetDifferencesResponsedifferencesTypeDef",
    "ClientGetDifferencesResponseTypeDef",
    "ClientGetFileResponseTypeDef",
    "ClientGetFolderResponsefilesTypeDef",
    "ClientGetFolderResponsesubFoldersTypeDef",
    "ClientGetFolderResponsesubModulesTypeDef",
    "ClientGetFolderResponsesymbolicLinksTypeDef",
    "ClientGetFolderResponseTypeDef",
    "ClientGetMergeCommitResponseTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListTypeDef",
    "ClientGetMergeConflictsResponseTypeDef",
    "ClientGetMergeOptionsResponseTypeDef",
    "ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef",
    "ClientGetPullRequestResponsepullRequestTypeDef",
    "ClientGetPullRequestResponseTypeDef",
    "ClientGetRepositoryResponserepositoryMetadataTypeDef",
    "ClientGetRepositoryResponseTypeDef",
    "ClientGetRepositoryTriggersResponsetriggersTypeDef",
    "ClientGetRepositoryTriggersResponseTypeDef",
    "ClientListBranchesResponseTypeDef",
    "ClientListPullRequestsResponseTypeDef",
    "ClientListRepositoriesResponserepositoriesTypeDef",
    "ClientListRepositoriesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientMergeBranchesByFastForwardResponseTypeDef",
    "ClientMergeBranchesBySquashResponseTypeDef",
    "ClientMergeBranchesBySquashconflictResolutiondeleteFilesTypeDef",
    "ClientMergeBranchesBySquashconflictResolutionreplaceContentsTypeDef",
    "ClientMergeBranchesBySquashconflictResolutionsetFileModesTypeDef",
    "ClientMergeBranchesBySquashconflictResolutionTypeDef",
    "ClientMergeBranchesByThreeWayResponseTypeDef",
    "ClientMergeBranchesByThreeWayconflictResolutiondeleteFilesTypeDef",
    "ClientMergeBranchesByThreeWayconflictResolutionreplaceContentsTypeDef",
    "ClientMergeBranchesByThreeWayconflictResolutionsetFileModesTypeDef",
    "ClientMergeBranchesByThreeWayconflictResolutionTypeDef",
    "ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef",
    "ClientMergePullRequestByFastForwardResponsepullRequestTypeDef",
    "ClientMergePullRequestByFastForwardResponseTypeDef",
    "ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef",
    "ClientMergePullRequestBySquashResponsepullRequestTypeDef",
    "ClientMergePullRequestBySquashResponseTypeDef",
    "ClientMergePullRequestBySquashconflictResolutiondeleteFilesTypeDef",
    "ClientMergePullRequestBySquashconflictResolutionreplaceContentsTypeDef",
    "ClientMergePullRequestBySquashconflictResolutionsetFileModesTypeDef",
    "ClientMergePullRequestBySquashconflictResolutionTypeDef",
    "ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef",
    "ClientMergePullRequestByThreeWayResponsepullRequestTypeDef",
    "ClientMergePullRequestByThreeWayResponseTypeDef",
    "ClientMergePullRequestByThreeWayconflictResolutiondeleteFilesTypeDef",
    "ClientMergePullRequestByThreeWayconflictResolutionreplaceContentsTypeDef",
    "ClientMergePullRequestByThreeWayconflictResolutionsetFileModesTypeDef",
    "ClientMergePullRequestByThreeWayconflictResolutionTypeDef",
    "ClientPostCommentForComparedCommitResponsecommentTypeDef",
    "ClientPostCommentForComparedCommitResponselocationTypeDef",
    "ClientPostCommentForComparedCommitResponseTypeDef",
    "ClientPostCommentForComparedCommitlocationTypeDef",
    "ClientPostCommentForPullRequestResponsecommentTypeDef",
    "ClientPostCommentForPullRequestResponselocationTypeDef",
    "ClientPostCommentForPullRequestResponseTypeDef",
    "ClientPostCommentForPullRequestlocationTypeDef",
    "ClientPostCommentReplyResponsecommentTypeDef",
    "ClientPostCommentReplyResponseTypeDef",
    "ClientPutFileResponseTypeDef",
    "ClientPutRepositoryTriggersResponseTypeDef",
    "ClientPutRepositoryTriggerstriggersTypeDef",
    "ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef",
    "ClientTestRepositoryTriggersResponseTypeDef",
    "ClientTestRepositoryTriggerstriggersTypeDef",
    "ClientUpdateCommentResponsecommentTypeDef",
    "ClientUpdateCommentResponseTypeDef",
    "ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef",
    "ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef",
    "ClientUpdatePullRequestDescriptionResponseTypeDef",
    "ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef",
    "ClientUpdatePullRequestStatusResponsepullRequestTypeDef",
    "ClientUpdatePullRequestStatusResponseTypeDef",
    "ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef",
    "ClientUpdatePullRequestTitleResponsepullRequestTypeDef",
    "ClientUpdatePullRequestTitleResponseTypeDef",
    "DescribePullRequestEventsPaginatePaginationConfigTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventsTypeDef",
    "DescribePullRequestEventsPaginateResponseTypeDef",
    "GetCommentsForComparedCommitPaginatePaginationConfigTypeDef",
    "GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatacommentsTypeDef",
    "GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatalocationTypeDef",
    "GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDataTypeDef",
    "GetCommentsForComparedCommitPaginateResponseTypeDef",
    "GetCommentsForPullRequestPaginatePaginationConfigTypeDef",
    "GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatacommentsTypeDef",
    "GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatalocationTypeDef",
    "GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDataTypeDef",
    "GetCommentsForPullRequestPaginateResponseTypeDef",
    "GetDifferencesPaginatePaginationConfigTypeDef",
    "GetDifferencesPaginateResponsedifferencesafterBlobTypeDef",
    "GetDifferencesPaginateResponsedifferencesbeforeBlobTypeDef",
    "GetDifferencesPaginateResponsedifferencesTypeDef",
    "GetDifferencesPaginateResponseTypeDef",
    "ListBranchesPaginatePaginationConfigTypeDef",
    "ListBranchesPaginateResponseTypeDef",
    "ListPullRequestsPaginatePaginationConfigTypeDef",
    "ListPullRequestsPaginateResponseTypeDef",
    "ListRepositoriesPaginatePaginationConfigTypeDef",
    "ListRepositoriesPaginateResponserepositoriesTypeDef",
    "ListRepositoriesPaginateResponseTypeDef",
)


_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef",
    {"source": str, "destination": str, "base": str},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef
):
    """
    Type definition for `ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadata` `fileModes`

    The file modes of the file in the source, destination, and base of the merge.

    - **source** *(string) --*

      The file mode of a file in the source of a merge or pull request.

    - **destination** *(string) --*

      The file mode of a file in the destination of a merge or pull request.

    - **base** *(string) --*

      The file mode of a file in the base of a merge or pull request.
    """


_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef",
    {"source": int, "destination": int, "base": int},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef
):
    """
    Type definition for `ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadata` `fileSizes`

    The file sizes of the file in the source, destination, and base of the merge.

    - **source** *(integer) --*

      The size of a file in the source of a merge or pull request.

    - **destination** *(integer) --*

      The size of a file in the destination of a merge or pull request.

    - **base** *(integer) --*

      The size of a file in the base of a merge or pull request.
    """


_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef",
    {"source": bool, "destination": bool, "base": bool},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef
):
    """
    Type definition for `ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadata` `isBinaryFile`

    A boolean value (true or false) indicating whether the file is binary or textual in the
    source, destination, and base of the merge.

    - **source** *(boolean) --*

      The binary or non-binary status of file in the source of a merge or pull request.

    - **destination** *(boolean) --*

      The binary or non-binary status of a file in the destination of a merge or pull
      request.

    - **base** *(boolean) --*

      The binary or non-binary status of a file in the base of a merge or pull request.
    """


_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef",
    {"source": str, "destination": str},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef
):
    """
    Type definition for `ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadata` `mergeOperations`

    Whether an add, modify, or delete operation caused the conflict between the source and
    destination of the merge.

    - **source** *(string) --*

      The operation on a file (add, modify, or delete) of a file in the source of a merge
      or pull request.

    - **destination** *(string) --*

      The operation on a file in the destination of a merge or pull request.
    """


_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef",
    {"source": str, "destination": str, "base": str},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef
):
    """
    Type definition for `ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadata` `objectTypes`

    Information about any object type conflicts in a merge operation.

    - **source** *(string) --*

      The type of the object in the source branch.

    - **destination** *(string) --*

      The type of the object in the destination branch.

    - **base** *(string) --*

      The type of the object in the base commit of the merge.
    """


_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef",
    {
        "filePath": str,
        "fileSizes": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef,
        "fileModes": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef,
        "objectTypes": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef,
        "numberOfConflicts": int,
        "isBinaryFile": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef,
        "contentConflict": bool,
        "fileModeConflict": bool,
        "objectTypeConflict": bool,
        "mergeOperations": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef,
    },
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef
):
    """
    Type definition for `ClientBatchDescribeMergeConflictsResponseconflicts` `conflictMetadata`

    Metadata about a conflict in a merge operation.

    - **filePath** *(string) --*

      The path of the file that contains conflicts.

    - **fileSizes** *(dict) --*

      The file sizes of the file in the source, destination, and base of the merge.

      - **source** *(integer) --*

        The size of a file in the source of a merge or pull request.

      - **destination** *(integer) --*

        The size of a file in the destination of a merge or pull request.

      - **base** *(integer) --*

        The size of a file in the base of a merge or pull request.

    - **fileModes** *(dict) --*

      The file modes of the file in the source, destination, and base of the merge.

      - **source** *(string) --*

        The file mode of a file in the source of a merge or pull request.

      - **destination** *(string) --*

        The file mode of a file in the destination of a merge or pull request.

      - **base** *(string) --*

        The file mode of a file in the base of a merge or pull request.

    - **objectTypes** *(dict) --*

      Information about any object type conflicts in a merge operation.

      - **source** *(string) --*

        The type of the object in the source branch.

      - **destination** *(string) --*

        The type of the object in the destination branch.

      - **base** *(string) --*

        The type of the object in the base commit of the merge.

    - **numberOfConflicts** *(integer) --*

      The number of conflicts, including both hunk conflicts and metadata conflicts.

    - **isBinaryFile** *(dict) --*

      A boolean value (true or false) indicating whether the file is binary or textual in the
      source, destination, and base of the merge.

      - **source** *(boolean) --*

        The binary or non-binary status of file in the source of a merge or pull request.

      - **destination** *(boolean) --*

        The binary or non-binary status of a file in the destination of a merge or pull
        request.

      - **base** *(boolean) --*

        The binary or non-binary status of a file in the base of a merge or pull request.

    - **contentConflict** *(boolean) --*

      A boolean value indicating whether there are conflicts in the content of a file.

    - **fileModeConflict** *(boolean) --*

      A boolean value indicating whether there are conflicts in the file mode of a file.

    - **objectTypeConflict** *(boolean) --*

      A boolean value (true or false) indicating whether there are conflicts between the
      branches in the object type of a file, folder, or submodule.

    - **mergeOperations** *(dict) --*

      Whether an add, modify, or delete operation caused the conflict between the source and
      destination of the merge.

      - **source** *(string) --*

        The operation on a file (add, modify, or delete) of a file in the source of a merge
        or pull request.

      - **destination** *(string) --*

        The operation on a file in the destination of a merge or pull request.
    """


_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef
):
    """
    Type definition for `ClientBatchDescribeMergeConflictsResponseconflictsmergeHunks` `base`

    Information about the merge hunk in the base of a merge or pull request.

    - **startLine** *(integer) --*

      The start position of the hunk in the merge result.

    - **endLine** *(integer) --*

      The end position of the hunk in the merge result.

    - **hunkContent** *(string) --*

      The base-64 encoded content of the hunk merged region that might or might not
      contain a conflict.
    """


_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef
):
    """
    Type definition for `ClientBatchDescribeMergeConflictsResponseconflictsmergeHunks` `destination`

    Information about the merge hunk in the destination of a merge or pull request.

    - **startLine** *(integer) --*

      The start position of the hunk in the merge result.

    - **endLine** *(integer) --*

      The end position of the hunk in the merge result.

    - **hunkContent** *(string) --*

      The base-64 encoded content of the hunk merged region that might or might not
      contain a conflict.
    """


_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef
):
    """
    Type definition for `ClientBatchDescribeMergeConflictsResponseconflictsmergeHunks` `source`

    Information about the merge hunk in the source of a merge or pull request.

    - **startLine** *(integer) --*

      The start position of the hunk in the merge result.

    - **endLine** *(integer) --*

      The end position of the hunk in the merge result.

    - **hunkContent** *(string) --*

      The base-64 encoded content of the hunk merged region that might or might not
      contain a conflict.
    """


_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef",
    {
        "isConflict": bool,
        "source": ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef,
        "destination": ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef,
        "base": ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef,
    },
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef
):
    """
    Type definition for `ClientBatchDescribeMergeConflictsResponseconflicts` `mergeHunks`

    Information about merge hunks in a merge or pull request operation.

    - **isConflict** *(boolean) --*

      A Boolean value indicating whether a combination of hunks contains a conflict.
      Conflicts occur when the same file or the same lines in a file were modified in both
      the source and destination of a merge or pull request. Valid values include true,
      false, and null. This will be true when the hunk represents a conflict and one or
      more files contains a line conflict. File mode conflicts in a merge will not set this
      to be true.

    - **source** *(dict) --*

      Information about the merge hunk in the source of a merge or pull request.

      - **startLine** *(integer) --*

        The start position of the hunk in the merge result.

      - **endLine** *(integer) --*

        The end position of the hunk in the merge result.

      - **hunkContent** *(string) --*

        The base-64 encoded content of the hunk merged region that might or might not
        contain a conflict.

    - **destination** *(dict) --*

      Information about the merge hunk in the destination of a merge or pull request.

      - **startLine** *(integer) --*

        The start position of the hunk in the merge result.

      - **endLine** *(integer) --*

        The end position of the hunk in the merge result.

      - **hunkContent** *(string) --*

        The base-64 encoded content of the hunk merged region that might or might not
        contain a conflict.

    - **base** *(dict) --*

      Information about the merge hunk in the base of a merge or pull request.

      - **startLine** *(integer) --*

        The start position of the hunk in the merge result.

      - **endLine** *(integer) --*

        The end position of the hunk in the merge result.

      - **hunkContent** *(string) --*

        The base-64 encoded content of the hunk merged region that might or might not
        contain a conflict.
    """


_ClientBatchDescribeMergeConflictsResponseconflictsTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsTypeDef",
    {
        "conflictMetadata": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef,
        "mergeHunks": List[
            ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef
        ],
    },
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsTypeDef
):
    """
    Type definition for `ClientBatchDescribeMergeConflictsResponse` `conflicts`

    Information about conflicts in a merge operation.

    - **conflictMetadata** *(dict) --*

      Metadata about a conflict in a merge operation.

      - **filePath** *(string) --*

        The path of the file that contains conflicts.

      - **fileSizes** *(dict) --*

        The file sizes of the file in the source, destination, and base of the merge.

        - **source** *(integer) --*

          The size of a file in the source of a merge or pull request.

        - **destination** *(integer) --*

          The size of a file in the destination of a merge or pull request.

        - **base** *(integer) --*

          The size of a file in the base of a merge or pull request.

      - **fileModes** *(dict) --*

        The file modes of the file in the source, destination, and base of the merge.

        - **source** *(string) --*

          The file mode of a file in the source of a merge or pull request.

        - **destination** *(string) --*

          The file mode of a file in the destination of a merge or pull request.

        - **base** *(string) --*

          The file mode of a file in the base of a merge or pull request.

      - **objectTypes** *(dict) --*

        Information about any object type conflicts in a merge operation.

        - **source** *(string) --*

          The type of the object in the source branch.

        - **destination** *(string) --*

          The type of the object in the destination branch.

        - **base** *(string) --*

          The type of the object in the base commit of the merge.

      - **numberOfConflicts** *(integer) --*

        The number of conflicts, including both hunk conflicts and metadata conflicts.

      - **isBinaryFile** *(dict) --*

        A boolean value (true or false) indicating whether the file is binary or textual in the
        source, destination, and base of the merge.

        - **source** *(boolean) --*

          The binary or non-binary status of file in the source of a merge or pull request.

        - **destination** *(boolean) --*

          The binary or non-binary status of a file in the destination of a merge or pull
          request.

        - **base** *(boolean) --*

          The binary or non-binary status of a file in the base of a merge or pull request.

      - **contentConflict** *(boolean) --*

        A boolean value indicating whether there are conflicts in the content of a file.

      - **fileModeConflict** *(boolean) --*

        A boolean value indicating whether there are conflicts in the file mode of a file.

      - **objectTypeConflict** *(boolean) --*

        A boolean value (true or false) indicating whether there are conflicts between the
        branches in the object type of a file, folder, or submodule.

      - **mergeOperations** *(dict) --*

        Whether an add, modify, or delete operation caused the conflict between the source and
        destination of the merge.

        - **source** *(string) --*

          The operation on a file (add, modify, or delete) of a file in the source of a merge
          or pull request.

        - **destination** *(string) --*

          The operation on a file in the destination of a merge or pull request.

    - **mergeHunks** *(list) --*

      A list of hunks that contain the differences between files or lines causing the conflict.

      - *(dict) --*

        Information about merge hunks in a merge or pull request operation.

        - **isConflict** *(boolean) --*

          A Boolean value indicating whether a combination of hunks contains a conflict.
          Conflicts occur when the same file or the same lines in a file were modified in both
          the source and destination of a merge or pull request. Valid values include true,
          false, and null. This will be true when the hunk represents a conflict and one or
          more files contains a line conflict. File mode conflicts in a merge will not set this
          to be true.

        - **source** *(dict) --*

          Information about the merge hunk in the source of a merge or pull request.

          - **startLine** *(integer) --*

            The start position of the hunk in the merge result.

          - **endLine** *(integer) --*

            The end position of the hunk in the merge result.

          - **hunkContent** *(string) --*

            The base-64 encoded content of the hunk merged region that might or might not
            contain a conflict.

        - **destination** *(dict) --*

          Information about the merge hunk in the destination of a merge or pull request.

          - **startLine** *(integer) --*

            The start position of the hunk in the merge result.

          - **endLine** *(integer) --*

            The end position of the hunk in the merge result.

          - **hunkContent** *(string) --*

            The base-64 encoded content of the hunk merged region that might or might not
            contain a conflict.

        - **base** *(dict) --*

          Information about the merge hunk in the base of a merge or pull request.

          - **startLine** *(integer) --*

            The start position of the hunk in the merge result.

          - **endLine** *(integer) --*

            The end position of the hunk in the merge result.

          - **hunkContent** *(string) --*

            The base-64 encoded content of the hunk merged region that might or might not
            contain a conflict.
    """


_ClientBatchDescribeMergeConflictsResponseerrorsTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseerrorsTypeDef",
    {"filePath": str, "exceptionName": str, "message": str},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseerrorsTypeDef(
    _ClientBatchDescribeMergeConflictsResponseerrorsTypeDef
):
    """
    Type definition for `ClientBatchDescribeMergeConflictsResponse` `errors`

    Information about errors in a BatchDescribeMergeConflicts operation.

    - **filePath** *(string) --*

      The path to the file.

    - **exceptionName** *(string) --*

      The name of the exception.

    - **message** *(string) --*

      The message provided by the exception.
    """


_ClientBatchDescribeMergeConflictsResponseTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseTypeDef",
    {
        "conflicts": List[ClientBatchDescribeMergeConflictsResponseconflictsTypeDef],
        "nextToken": str,
        "errors": List[ClientBatchDescribeMergeConflictsResponseerrorsTypeDef],
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
    },
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseTypeDef(
    _ClientBatchDescribeMergeConflictsResponseTypeDef
):
    """
    Type definition for `ClientBatchDescribeMergeConflicts` `Response`

    - **conflicts** *(list) --*

      A list of conflicts for each file, including the conflict metadata and the hunks of the
      differences between the files.

      - *(dict) --*

        Information about conflicts in a merge operation.

        - **conflictMetadata** *(dict) --*

          Metadata about a conflict in a merge operation.

          - **filePath** *(string) --*

            The path of the file that contains conflicts.

          - **fileSizes** *(dict) --*

            The file sizes of the file in the source, destination, and base of the merge.

            - **source** *(integer) --*

              The size of a file in the source of a merge or pull request.

            - **destination** *(integer) --*

              The size of a file in the destination of a merge or pull request.

            - **base** *(integer) --*

              The size of a file in the base of a merge or pull request.

          - **fileModes** *(dict) --*

            The file modes of the file in the source, destination, and base of the merge.

            - **source** *(string) --*

              The file mode of a file in the source of a merge or pull request.

            - **destination** *(string) --*

              The file mode of a file in the destination of a merge or pull request.

            - **base** *(string) --*

              The file mode of a file in the base of a merge or pull request.

          - **objectTypes** *(dict) --*

            Information about any object type conflicts in a merge operation.

            - **source** *(string) --*

              The type of the object in the source branch.

            - **destination** *(string) --*

              The type of the object in the destination branch.

            - **base** *(string) --*

              The type of the object in the base commit of the merge.

          - **numberOfConflicts** *(integer) --*

            The number of conflicts, including both hunk conflicts and metadata conflicts.

          - **isBinaryFile** *(dict) --*

            A boolean value (true or false) indicating whether the file is binary or textual in the
            source, destination, and base of the merge.

            - **source** *(boolean) --*

              The binary or non-binary status of file in the source of a merge or pull request.

            - **destination** *(boolean) --*

              The binary or non-binary status of a file in the destination of a merge or pull
              request.

            - **base** *(boolean) --*

              The binary or non-binary status of a file in the base of a merge or pull request.

          - **contentConflict** *(boolean) --*

            A boolean value indicating whether there are conflicts in the content of a file.

          - **fileModeConflict** *(boolean) --*

            A boolean value indicating whether there are conflicts in the file mode of a file.

          - **objectTypeConflict** *(boolean) --*

            A boolean value (true or false) indicating whether there are conflicts between the
            branches in the object type of a file, folder, or submodule.

          - **mergeOperations** *(dict) --*

            Whether an add, modify, or delete operation caused the conflict between the source and
            destination of the merge.

            - **source** *(string) --*

              The operation on a file (add, modify, or delete) of a file in the source of a merge
              or pull request.

            - **destination** *(string) --*

              The operation on a file in the destination of a merge or pull request.

        - **mergeHunks** *(list) --*

          A list of hunks that contain the differences between files or lines causing the conflict.

          - *(dict) --*

            Information about merge hunks in a merge or pull request operation.

            - **isConflict** *(boolean) --*

              A Boolean value indicating whether a combination of hunks contains a conflict.
              Conflicts occur when the same file or the same lines in a file were modified in both
              the source and destination of a merge or pull request. Valid values include true,
              false, and null. This will be true when the hunk represents a conflict and one or
              more files contains a line conflict. File mode conflicts in a merge will not set this
              to be true.

            - **source** *(dict) --*

              Information about the merge hunk in the source of a merge or pull request.

              - **startLine** *(integer) --*

                The start position of the hunk in the merge result.

              - **endLine** *(integer) --*

                The end position of the hunk in the merge result.

              - **hunkContent** *(string) --*

                The base-64 encoded content of the hunk merged region that might or might not
                contain a conflict.

            - **destination** *(dict) --*

              Information about the merge hunk in the destination of a merge or pull request.

              - **startLine** *(integer) --*

                The start position of the hunk in the merge result.

              - **endLine** *(integer) --*

                The end position of the hunk in the merge result.

              - **hunkContent** *(string) --*

                The base-64 encoded content of the hunk merged region that might or might not
                contain a conflict.

            - **base** *(dict) --*

              Information about the merge hunk in the base of a merge or pull request.

              - **startLine** *(integer) --*

                The start position of the hunk in the merge result.

              - **endLine** *(integer) --*

                The end position of the hunk in the merge result.

              - **hunkContent** *(string) --*

                The base-64 encoded content of the hunk merged region that might or might not
                contain a conflict.

    - **nextToken** *(string) --*

      An enumeration token that can be used in a request to return the next batch of the results.

    - **errors** *(list) --*

      A list of any errors returned while describing the merge conflicts for each file.

      - *(dict) --*

        Information about errors in a BatchDescribeMergeConflicts operation.

        - **filePath** *(string) --*

          The path to the file.

        - **exceptionName** *(string) --*

          The name of the exception.

        - **message** *(string) --*

          The message provided by the exception.

    - **destinationCommitId** *(string) --*

      The commit ID of the destination commit specifier that was used in the merge evaluation.

    - **sourceCommitId** *(string) --*

      The commit ID of the source commit specifier that was used in the merge evaluation.

    - **baseCommitId** *(string) --*

      The commit ID of the merge base.
    """


_ClientBatchGetCommitsResponsecommitsauthorTypeDef = TypedDict(
    "_ClientBatchGetCommitsResponsecommitsauthorTypeDef",
    {"name": str, "email": str, "date": str},
    total=False,
)


class ClientBatchGetCommitsResponsecommitsauthorTypeDef(
    _ClientBatchGetCommitsResponsecommitsauthorTypeDef
):
    """
    Type definition for `ClientBatchGetCommitsResponsecommits` `author`

    Information about the author of the specified commit. Information includes the date in
    timestamp format with GMT offset, the name of the author, and the email address for the
    author, as configured in Git.

    - **name** *(string) --*

      The name of the user who made the specified commit.

    - **email** *(string) --*

      The email address associated with the user who made the commit, if any.

    - **date** *(string) --*

      The date when the specified commit was commited, in timestamp format with GMT offset.
    """


_ClientBatchGetCommitsResponsecommitscommitterTypeDef = TypedDict(
    "_ClientBatchGetCommitsResponsecommitscommitterTypeDef",
    {"name": str, "email": str, "date": str},
    total=False,
)


class ClientBatchGetCommitsResponsecommitscommitterTypeDef(
    _ClientBatchGetCommitsResponsecommitscommitterTypeDef
):
    """
    Type definition for `ClientBatchGetCommitsResponsecommits` `committer`

    Information about the person who committed the specified commit, also known as the
    committer. Information includes the date in timestamp format with GMT offset, the name of
    the committer, and the email address for the committer, as configured in Git.

    For more information about the difference between an author and a committer in Git, see
    `Viewing the Commit History <http://git-scm.com/book/ch2-3.html>`__ in Pro Git by Scott
    Chacon and Ben Straub.

    - **name** *(string) --*

      The name of the user who made the specified commit.

    - **email** *(string) --*

      The email address associated with the user who made the commit, if any.

    - **date** *(string) --*

      The date when the specified commit was commited, in timestamp format with GMT offset.
    """


_ClientBatchGetCommitsResponsecommitsTypeDef = TypedDict(
    "_ClientBatchGetCommitsResponsecommitsTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "parents": List[str],
        "message": str,
        "author": ClientBatchGetCommitsResponsecommitsauthorTypeDef,
        "committer": ClientBatchGetCommitsResponsecommitscommitterTypeDef,
        "additionalData": str,
    },
    total=False,
)


class ClientBatchGetCommitsResponsecommitsTypeDef(
    _ClientBatchGetCommitsResponsecommitsTypeDef
):
    """
    Type definition for `ClientBatchGetCommitsResponse` `commits`

    Returns information about a specific commit.

    - **commitId** *(string) --*

      The full SHA of the specified commit.

    - **treeId** *(string) --*

      Tree information for the specified commit.

    - **parents** *(list) --*

      A list of parent commits for the specified commit. Each parent commit ID is the full
      commit ID.

      - *(string) --*

    - **message** *(string) --*

      The commit message associated with the specified commit.

    - **author** *(dict) --*

      Information about the author of the specified commit. Information includes the date in
      timestamp format with GMT offset, the name of the author, and the email address for the
      author, as configured in Git.

      - **name** *(string) --*

        The name of the user who made the specified commit.

      - **email** *(string) --*

        The email address associated with the user who made the commit, if any.

      - **date** *(string) --*

        The date when the specified commit was commited, in timestamp format with GMT offset.

    - **committer** *(dict) --*

      Information about the person who committed the specified commit, also known as the
      committer. Information includes the date in timestamp format with GMT offset, the name of
      the committer, and the email address for the committer, as configured in Git.

      For more information about the difference between an author and a committer in Git, see
      `Viewing the Commit History <http://git-scm.com/book/ch2-3.html>`__ in Pro Git by Scott
      Chacon and Ben Straub.

      - **name** *(string) --*

        The name of the user who made the specified commit.

      - **email** *(string) --*

        The email address associated with the user who made the commit, if any.

      - **date** *(string) --*

        The date when the specified commit was commited, in timestamp format with GMT offset.

    - **additionalData** *(string) --*

      Any additional data associated with the specified commit.
    """


_ClientBatchGetCommitsResponseerrorsTypeDef = TypedDict(
    "_ClientBatchGetCommitsResponseerrorsTypeDef",
    {"commitId": str, "errorCode": str, "errorMessage": str},
    total=False,
)


class ClientBatchGetCommitsResponseerrorsTypeDef(
    _ClientBatchGetCommitsResponseerrorsTypeDef
):
    """
    Type definition for `ClientBatchGetCommitsResponse` `errors`

    Returns information about errors in a BatchGetCommits operation.

    - **commitId** *(string) --*

      A commit ID that either could not be found or was not in a valid format.

    - **errorCode** *(string) --*

      An error code that specifies whether the commit ID was not valid or not found.

    - **errorMessage** *(string) --*

      An error message that provides detail about why the commit ID either was not found or was
      not valid.
    """


_ClientBatchGetCommitsResponseTypeDef = TypedDict(
    "_ClientBatchGetCommitsResponseTypeDef",
    {
        "commits": List[ClientBatchGetCommitsResponsecommitsTypeDef],
        "errors": List[ClientBatchGetCommitsResponseerrorsTypeDef],
    },
    total=False,
)


class ClientBatchGetCommitsResponseTypeDef(_ClientBatchGetCommitsResponseTypeDef):
    """
    Type definition for `ClientBatchGetCommits` `Response`

    - **commits** *(list) --*

      An array of commit data type objects, each of which contains information about a specified
      commit.

      - *(dict) --*

        Returns information about a specific commit.

        - **commitId** *(string) --*

          The full SHA of the specified commit.

        - **treeId** *(string) --*

          Tree information for the specified commit.

        - **parents** *(list) --*

          A list of parent commits for the specified commit. Each parent commit ID is the full
          commit ID.

          - *(string) --*

        - **message** *(string) --*

          The commit message associated with the specified commit.

        - **author** *(dict) --*

          Information about the author of the specified commit. Information includes the date in
          timestamp format with GMT offset, the name of the author, and the email address for the
          author, as configured in Git.

          - **name** *(string) --*

            The name of the user who made the specified commit.

          - **email** *(string) --*

            The email address associated with the user who made the commit, if any.

          - **date** *(string) --*

            The date when the specified commit was commited, in timestamp format with GMT offset.

        - **committer** *(dict) --*

          Information about the person who committed the specified commit, also known as the
          committer. Information includes the date in timestamp format with GMT offset, the name of
          the committer, and the email address for the committer, as configured in Git.

          For more information about the difference between an author and a committer in Git, see
          `Viewing the Commit History <http://git-scm.com/book/ch2-3.html>`__ in Pro Git by Scott
          Chacon and Ben Straub.

          - **name** *(string) --*

            The name of the user who made the specified commit.

          - **email** *(string) --*

            The email address associated with the user who made the commit, if any.

          - **date** *(string) --*

            The date when the specified commit was commited, in timestamp format with GMT offset.

        - **additionalData** *(string) --*

          Any additional data associated with the specified commit.

    - **errors** *(list) --*

      Returns any commit IDs for which information could not be found. For example, if one of the
      commit IDs was a shortened SHA or that commit was not found in the specified repository, the
      ID will return an error object with additional information.

      - *(dict) --*

        Returns information about errors in a BatchGetCommits operation.

        - **commitId** *(string) --*

          A commit ID that either could not be found or was not in a valid format.

        - **errorCode** *(string) --*

          An error code that specifies whether the commit ID was not valid or not found.

        - **errorMessage** *(string) --*

          An error message that provides detail about why the commit ID either was not found or was
          not valid.
    """


_ClientBatchGetRepositoriesResponserepositoriesTypeDef = TypedDict(
    "_ClientBatchGetRepositoriesResponserepositoriesTypeDef",
    {
        "accountId": str,
        "repositoryId": str,
        "repositoryName": str,
        "repositoryDescription": str,
        "defaultBranch": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "cloneUrlHttp": str,
        "cloneUrlSsh": str,
        "Arn": str,
    },
    total=False,
)


class ClientBatchGetRepositoriesResponserepositoriesTypeDef(
    _ClientBatchGetRepositoriesResponserepositoriesTypeDef
):
    """
    Type definition for `ClientBatchGetRepositoriesResponse` `repositories`

    Information about a repository.

    - **accountId** *(string) --*

      The ID of the AWS account associated with the repository.

    - **repositoryId** *(string) --*

      The ID of the repository.

    - **repositoryName** *(string) --*

      The repository's name.

    - **repositoryDescription** *(string) --*

      A comment or description about the repository.

    - **defaultBranch** *(string) --*

      The repository's default branch name.

    - **lastModifiedDate** *(datetime) --*

      The date and time the repository was last modified, in timestamp format.

    - **creationDate** *(datetime) --*

      The date and time the repository was created, in timestamp format.

    - **cloneUrlHttp** *(string) --*

      The URL to use for cloning the repository over HTTPS.

    - **cloneUrlSsh** *(string) --*

      The URL to use for cloning the repository over SSH.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the repository.
    """


_ClientBatchGetRepositoriesResponseTypeDef = TypedDict(
    "_ClientBatchGetRepositoriesResponseTypeDef",
    {
        "repositories": List[ClientBatchGetRepositoriesResponserepositoriesTypeDef],
        "repositoriesNotFound": List[str],
    },
    total=False,
)


class ClientBatchGetRepositoriesResponseTypeDef(
    _ClientBatchGetRepositoriesResponseTypeDef
):
    """
    Type definition for `ClientBatchGetRepositories` `Response`

    Represents the output of a batch get repositories operation.

    - **repositories** *(list) --*

      A list of repositories returned by the batch get repositories operation.

      - *(dict) --*

        Information about a repository.

        - **accountId** *(string) --*

          The ID of the AWS account associated with the repository.

        - **repositoryId** *(string) --*

          The ID of the repository.

        - **repositoryName** *(string) --*

          The repository's name.

        - **repositoryDescription** *(string) --*

          A comment or description about the repository.

        - **defaultBranch** *(string) --*

          The repository's default branch name.

        - **lastModifiedDate** *(datetime) --*

          The date and time the repository was last modified, in timestamp format.

        - **creationDate** *(datetime) --*

          The date and time the repository was created, in timestamp format.

        - **cloneUrlHttp** *(string) --*

          The URL to use for cloning the repository over HTTPS.

        - **cloneUrlSsh** *(string) --*

          The URL to use for cloning the repository over SSH.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the repository.

    - **repositoriesNotFound** *(list) --*

      Returns a list of repository names for which information could not be found.

      - *(string) --*
    """


_ClientCreateCommitResponsefilesAddedTypeDef = TypedDict(
    "_ClientCreateCommitResponsefilesAddedTypeDef",
    {"absolutePath": str, "blobId": str, "fileMode": str},
    total=False,
)


class ClientCreateCommitResponsefilesAddedTypeDef(
    _ClientCreateCommitResponsefilesAddedTypeDef
):
    """
    Type definition for `ClientCreateCommitResponse` `filesAdded`

    A file that will be added, updated, or deleted as part of a commit.

    - **absolutePath** *(string) --*

      The full path to the file that will be added or updated, including the name of the file.

    - **blobId** *(string) --*

      The blob ID that contains the file information.

    - **fileMode** *(string) --*

      The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and
      NORMAL.
    """


_ClientCreateCommitResponsefilesDeletedTypeDef = TypedDict(
    "_ClientCreateCommitResponsefilesDeletedTypeDef",
    {"absolutePath": str, "blobId": str, "fileMode": str},
    total=False,
)


class ClientCreateCommitResponsefilesDeletedTypeDef(
    _ClientCreateCommitResponsefilesDeletedTypeDef
):
    """
    Type definition for `ClientCreateCommitResponse` `filesDeleted`

    A file that will be added, updated, or deleted as part of a commit.

    - **absolutePath** *(string) --*

      The full path to the file that will be added or updated, including the name of the file.

    - **blobId** *(string) --*

      The blob ID that contains the file information.

    - **fileMode** *(string) --*

      The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and
      NORMAL.
    """


_ClientCreateCommitResponsefilesUpdatedTypeDef = TypedDict(
    "_ClientCreateCommitResponsefilesUpdatedTypeDef",
    {"absolutePath": str, "blobId": str, "fileMode": str},
    total=False,
)


class ClientCreateCommitResponsefilesUpdatedTypeDef(
    _ClientCreateCommitResponsefilesUpdatedTypeDef
):
    """
    Type definition for `ClientCreateCommitResponse` `filesUpdated`

    A file that will be added, updated, or deleted as part of a commit.

    - **absolutePath** *(string) --*

      The full path to the file that will be added or updated, including the name of the file.

    - **blobId** *(string) --*

      The blob ID that contains the file information.

    - **fileMode** *(string) --*

      The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and
      NORMAL.
    """


_ClientCreateCommitResponseTypeDef = TypedDict(
    "_ClientCreateCommitResponseTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "filesAdded": List[ClientCreateCommitResponsefilesAddedTypeDef],
        "filesUpdated": List[ClientCreateCommitResponsefilesUpdatedTypeDef],
        "filesDeleted": List[ClientCreateCommitResponsefilesDeletedTypeDef],
    },
    total=False,
)


class ClientCreateCommitResponseTypeDef(_ClientCreateCommitResponseTypeDef):
    """
    Type definition for `ClientCreateCommit` `Response`

    - **commitId** *(string) --*

      The full commit ID of the commit that contains your committed file changes.

    - **treeId** *(string) --*

      The full SHA-1 pointer of the tree information for the commit that contains the commited file
      changes.

    - **filesAdded** *(list) --*

      The files added as part of the committed file changes.

      - *(dict) --*

        A file that will be added, updated, or deleted as part of a commit.

        - **absolutePath** *(string) --*

          The full path to the file that will be added or updated, including the name of the file.

        - **blobId** *(string) --*

          The blob ID that contains the file information.

        - **fileMode** *(string) --*

          The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and
          NORMAL.

    - **filesUpdated** *(list) --*

      The files updated as part of the commited file changes.

      - *(dict) --*

        A file that will be added, updated, or deleted as part of a commit.

        - **absolutePath** *(string) --*

          The full path to the file that will be added or updated, including the name of the file.

        - **blobId** *(string) --*

          The blob ID that contains the file information.

        - **fileMode** *(string) --*

          The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and
          NORMAL.

    - **filesDeleted** *(list) --*

      The files deleted as part of the committed file changes.

      - *(dict) --*

        A file that will be added, updated, or deleted as part of a commit.

        - **absolutePath** *(string) --*

          The full path to the file that will be added or updated, including the name of the file.

        - **blobId** *(string) --*

          The blob ID that contains the file information.

        - **fileMode** *(string) --*

          The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and
          NORMAL.
    """


_ClientCreateCommitdeleteFilesTypeDef = TypedDict(
    "_ClientCreateCommitdeleteFilesTypeDef", {"filePath": str}
)


class ClientCreateCommitdeleteFilesTypeDef(_ClientCreateCommitdeleteFilesTypeDef):
    """
    Type definition for `ClientCreateCommit` `deleteFiles`

    A file that will be deleted as part of a commit.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path of the file that will be deleted, including the name of the file.
    """


_RequiredClientCreateCommitputFilessourceFileTypeDef = TypedDict(
    "_RequiredClientCreateCommitputFilessourceFileTypeDef", {"filePath": str}
)
_OptionalClientCreateCommitputFilessourceFileTypeDef = TypedDict(
    "_OptionalClientCreateCommitputFilessourceFileTypeDef",
    {"isMove": bool},
    total=False,
)


class ClientCreateCommitputFilessourceFileTypeDef(
    _RequiredClientCreateCommitputFilessourceFileTypeDef,
    _OptionalClientCreateCommitputFilessourceFileTypeDef,
):
    """
    Type definition for `ClientCreateCommitputFiles` `sourceFile`

    The name and full path of the file that contains the changes you want to make as part of the
    commit, if you are not providing the file content directly.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path to the file, including the name of the file.

    - **isMove** *(boolean) --*

      Whether to remove the source file from the parent commit.
    """


_RequiredClientCreateCommitputFilesTypeDef = TypedDict(
    "_RequiredClientCreateCommitputFilesTypeDef", {"filePath": str}
)
_OptionalClientCreateCommitputFilesTypeDef = TypedDict(
    "_OptionalClientCreateCommitputFilesTypeDef",
    {
        "fileMode": str,
        "fileContent": bytes,
        "sourceFile": ClientCreateCommitputFilessourceFileTypeDef,
    },
    total=False,
)


class ClientCreateCommitputFilesTypeDef(
    _RequiredClientCreateCommitputFilesTypeDef,
    _OptionalClientCreateCommitputFilesTypeDef,
):
    """
    Type definition for `ClientCreateCommit` `putFiles`

    Information about a file that will be added or updated as part of a commit.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path to the file in the repository, including the name of the file.

    - **fileMode** *(string) --*

      The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and
      NORMAL.

    - **fileContent** *(bytes) --*

      The content of the file, if a source file is not specified.

    - **sourceFile** *(dict) --*

      The name and full path of the file that contains the changes you want to make as part of the
      commit, if you are not providing the file content directly.

      - **filePath** *(string) --* **[REQUIRED]**

        The full path to the file, including the name of the file.

      - **isMove** *(boolean) --*

        Whether to remove the source file from the parent commit.
    """


_ClientCreateCommitsetFileModesTypeDef = TypedDict(
    "_ClientCreateCommitsetFileModesTypeDef", {"filePath": str, "fileMode": str}
)


class ClientCreateCommitsetFileModesTypeDef(_ClientCreateCommitsetFileModesTypeDef):
    """
    Type definition for `ClientCreateCommit` `setFileModes`

    Information about the file mode changes.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path to the file, including the name of the file.

    - **fileMode** *(string) --* **[REQUIRED]**

      The file mode for the file.
    """


_ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {"isMerged": bool, "mergedBy": str, "mergeCommitId": str, "mergeOption": str},
    total=False,
)


class ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    """
    Type definition for `ClientCreatePullRequestResponsepullRequestpullRequestTargets` `mergeMetadata`

    Returns metadata about the state of the merge, including whether the merge has been
    made.

    - **isMerged** *(boolean) --*

      A Boolean value indicating whether the merge has been made.

    - **mergedBy** *(string) --*

      The Amazon Resource Name (ARN) of the user who merged the branches.

    - **mergeCommitId** *(string) --*

      The commit ID for the merge commit, if any.

    - **mergeOption** *(string) --*

      The merge strategy used in the merge.
    """


_ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef(
    _ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef
):
    """
    Type definition for `ClientCreatePullRequestResponsepullRequest` `pullRequestTargets`

    Returns information about a pull request target.

    - **repositoryName** *(string) --*

      The name of the repository that contains the pull request source and destination
      branches.

    - **sourceReference** *(string) --*

      The branch of the repository that contains the changes for the pull request. Also known
      as the source branch.

    - **destinationReference** *(string) --*

      The branch of the repository where the pull request changes will be merged into. Also
      known as the destination branch.

    - **destinationCommit** *(string) --*

      The full commit ID that is the tip of the destination branch. This is the commit where
      the pull request was or will be merged.

    - **sourceCommit** *(string) --*

      The full commit ID of the tip of the source branch used to create the pull request. If
      the pull request branch is updated by a push while the pull request is open, the commit
      ID will change to reflect the new tip of the branch.

    - **mergeBase** *(string) --*

      The commit ID of the most recent commit that the source branch and the destination
      branch have in common.

    - **mergeMetadata** *(dict) --*

      Returns metadata about the state of the merge, including whether the merge has been
      made.

      - **isMerged** *(boolean) --*

        A Boolean value indicating whether the merge has been made.

      - **mergedBy** *(string) --*

        The Amazon Resource Name (ARN) of the user who merged the branches.

      - **mergeCommitId** *(string) --*

        The commit ID for the merge commit, if any.

      - **mergeOption** *(string) --*

        The merge strategy used in the merge.
    """


_ClientCreatePullRequestResponsepullRequestTypeDef = TypedDict(
    "_ClientCreatePullRequestResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": str,
        "authorArn": str,
        "pullRequestTargets": List[
            ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
    },
    total=False,
)


class ClientCreatePullRequestResponsepullRequestTypeDef(
    _ClientCreatePullRequestResponsepullRequestTypeDef
):
    """
    Type definition for `ClientCreatePullRequestResponse` `pullRequest`

    Information about the newly created pull request.

    - **pullRequestId** *(string) --*

      The system-generated ID of the pull request.

    - **title** *(string) --*

      The user-defined title of the pull request. This title is displayed in the list of pull
      requests to other users of the repository.

    - **description** *(string) --*

      The user-defined description of the pull request. This description can be used to clarify
      what should be reviewed and other details of the request.

    - **lastActivityDate** *(datetime) --*

      The day and time of the last user or system activity on the pull request, in timestamp
      format.

    - **creationDate** *(datetime) --*

      The date and time the pull request was originally created, in timestamp format.

    - **pullRequestStatus** *(string) --*

      The status of the pull request. Pull request status can only change from ``OPEN`` to
      ``CLOSED`` .

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the user who created the pull request.

    - **pullRequestTargets** *(list) --*

      The targets of the pull request, including the source branch and destination branch for the
      pull request.

      - *(dict) --*

        Returns information about a pull request target.

        - **repositoryName** *(string) --*

          The name of the repository that contains the pull request source and destination
          branches.

        - **sourceReference** *(string) --*

          The branch of the repository that contains the changes for the pull request. Also known
          as the source branch.

        - **destinationReference** *(string) --*

          The branch of the repository where the pull request changes will be merged into. Also
          known as the destination branch.

        - **destinationCommit** *(string) --*

          The full commit ID that is the tip of the destination branch. This is the commit where
          the pull request was or will be merged.

        - **sourceCommit** *(string) --*

          The full commit ID of the tip of the source branch used to create the pull request. If
          the pull request branch is updated by a push while the pull request is open, the commit
          ID will change to reflect the new tip of the branch.

        - **mergeBase** *(string) --*

          The commit ID of the most recent commit that the source branch and the destination
          branch have in common.

        - **mergeMetadata** *(dict) --*

          Returns metadata about the state of the merge, including whether the merge has been
          made.

          - **isMerged** *(boolean) --*

            A Boolean value indicating whether the merge has been made.

          - **mergedBy** *(string) --*

            The Amazon Resource Name (ARN) of the user who merged the branches.

          - **mergeCommitId** *(string) --*

            The commit ID for the merge commit, if any.

          - **mergeOption** *(string) --*

            The merge strategy used in the merge.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientCreatePullRequestResponseTypeDef = TypedDict(
    "_ClientCreatePullRequestResponseTypeDef",
    {"pullRequest": ClientCreatePullRequestResponsepullRequestTypeDef},
    total=False,
)


class ClientCreatePullRequestResponseTypeDef(_ClientCreatePullRequestResponseTypeDef):
    """
    Type definition for `ClientCreatePullRequest` `Response`

    - **pullRequest** *(dict) --*

      Information about the newly created pull request.

      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.

      - **title** *(string) --*

        The user-defined title of the pull request. This title is displayed in the list of pull
        requests to other users of the repository.

      - **description** *(string) --*

        The user-defined description of the pull request. This description can be used to clarify
        what should be reviewed and other details of the request.

      - **lastActivityDate** *(datetime) --*

        The day and time of the last user or system activity on the pull request, in timestamp
        format.

      - **creationDate** *(datetime) --*

        The date and time the pull request was originally created, in timestamp format.

      - **pullRequestStatus** *(string) --*

        The status of the pull request. Pull request status can only change from ``OPEN`` to
        ``CLOSED`` .

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the user who created the pull request.

      - **pullRequestTargets** *(list) --*

        The targets of the pull request, including the source branch and destination branch for the
        pull request.

        - *(dict) --*

          Returns information about a pull request target.

          - **repositoryName** *(string) --*

            The name of the repository that contains the pull request source and destination
            branches.

          - **sourceReference** *(string) --*

            The branch of the repository that contains the changes for the pull request. Also known
            as the source branch.

          - **destinationReference** *(string) --*

            The branch of the repository where the pull request changes will be merged into. Also
            known as the destination branch.

          - **destinationCommit** *(string) --*

            The full commit ID that is the tip of the destination branch. This is the commit where
            the pull request was or will be merged.

          - **sourceCommit** *(string) --*

            The full commit ID of the tip of the source branch used to create the pull request. If
            the pull request branch is updated by a push while the pull request is open, the commit
            ID will change to reflect the new tip of the branch.

          - **mergeBase** *(string) --*

            The commit ID of the most recent commit that the source branch and the destination
            branch have in common.

          - **mergeMetadata** *(dict) --*

            Returns metadata about the state of the merge, including whether the merge has been
            made.

            - **isMerged** *(boolean) --*

              A Boolean value indicating whether the merge has been made.

            - **mergedBy** *(string) --*

              The Amazon Resource Name (ARN) of the user who merged the branches.

            - **mergeCommitId** *(string) --*

              The commit ID for the merge commit, if any.

            - **mergeOption** *(string) --*

              The merge strategy used in the merge.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_RequiredClientCreatePullRequesttargetsTypeDef = TypedDict(
    "_RequiredClientCreatePullRequesttargetsTypeDef",
    {"repositoryName": str, "sourceReference": str},
)
_OptionalClientCreatePullRequesttargetsTypeDef = TypedDict(
    "_OptionalClientCreatePullRequesttargetsTypeDef",
    {"destinationReference": str},
    total=False,
)


class ClientCreatePullRequesttargetsTypeDef(
    _RequiredClientCreatePullRequesttargetsTypeDef,
    _OptionalClientCreatePullRequesttargetsTypeDef,
):
    """
    Type definition for `ClientCreatePullRequest` `targets`

    Returns information about a target for a pull request.

    - **repositoryName** *(string) --* **[REQUIRED]**

      The name of the repository that contains the pull request.

    - **sourceReference** *(string) --* **[REQUIRED]**

      The branch of the repository that contains the changes for the pull request. Also known as
      the source branch.

    - **destinationReference** *(string) --*

      The branch of the repository where the pull request changes will be merged into. Also known
      as the destination branch.
    """


_ClientCreateRepositoryResponserepositoryMetadataTypeDef = TypedDict(
    "_ClientCreateRepositoryResponserepositoryMetadataTypeDef",
    {
        "accountId": str,
        "repositoryId": str,
        "repositoryName": str,
        "repositoryDescription": str,
        "defaultBranch": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "cloneUrlHttp": str,
        "cloneUrlSsh": str,
        "Arn": str,
    },
    total=False,
)


class ClientCreateRepositoryResponserepositoryMetadataTypeDef(
    _ClientCreateRepositoryResponserepositoryMetadataTypeDef
):
    """
    Type definition for `ClientCreateRepositoryResponse` `repositoryMetadata`

    Information about the newly created repository.

    - **accountId** *(string) --*

      The ID of the AWS account associated with the repository.

    - **repositoryId** *(string) --*

      The ID of the repository.

    - **repositoryName** *(string) --*

      The repository's name.

    - **repositoryDescription** *(string) --*

      A comment or description about the repository.

    - **defaultBranch** *(string) --*

      The repository's default branch name.

    - **lastModifiedDate** *(datetime) --*

      The date and time the repository was last modified, in timestamp format.

    - **creationDate** *(datetime) --*

      The date and time the repository was created, in timestamp format.

    - **cloneUrlHttp** *(string) --*

      The URL to use for cloning the repository over HTTPS.

    - **cloneUrlSsh** *(string) --*

      The URL to use for cloning the repository over SSH.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the repository.
    """


_ClientCreateRepositoryResponseTypeDef = TypedDict(
    "_ClientCreateRepositoryResponseTypeDef",
    {"repositoryMetadata": ClientCreateRepositoryResponserepositoryMetadataTypeDef},
    total=False,
)


class ClientCreateRepositoryResponseTypeDef(_ClientCreateRepositoryResponseTypeDef):
    """
    Type definition for `ClientCreateRepository` `Response`

    Represents the output of a create repository operation.

    - **repositoryMetadata** *(dict) --*

      Information about the newly created repository.

      - **accountId** *(string) --*

        The ID of the AWS account associated with the repository.

      - **repositoryId** *(string) --*

        The ID of the repository.

      - **repositoryName** *(string) --*

        The repository's name.

      - **repositoryDescription** *(string) --*

        A comment or description about the repository.

      - **defaultBranch** *(string) --*

        The repository's default branch name.

      - **lastModifiedDate** *(datetime) --*

        The date and time the repository was last modified, in timestamp format.

      - **creationDate** *(datetime) --*

        The date and time the repository was created, in timestamp format.

      - **cloneUrlHttp** *(string) --*

        The URL to use for cloning the repository over HTTPS.

      - **cloneUrlSsh** *(string) --*

        The URL to use for cloning the repository over SSH.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the repository.
    """


_ClientCreateUnreferencedMergeCommitResponseTypeDef = TypedDict(
    "_ClientCreateUnreferencedMergeCommitResponseTypeDef",
    {"commitId": str, "treeId": str},
    total=False,
)


class ClientCreateUnreferencedMergeCommitResponseTypeDef(
    _ClientCreateUnreferencedMergeCommitResponseTypeDef
):
    """
    Type definition for `ClientCreateUnreferencedMergeCommit` `Response`

    - **commitId** *(string) --*

      The full commit ID of the commit that contains your merge results.

    - **treeId** *(string) --*

      The full SHA-1 pointer of the tree information for the commit that contains the merge results.
    """


_ClientCreateUnreferencedMergeCommitconflictResolutiondeleteFilesTypeDef = TypedDict(
    "_ClientCreateUnreferencedMergeCommitconflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
)


class ClientCreateUnreferencedMergeCommitconflictResolutiondeleteFilesTypeDef(
    _ClientCreateUnreferencedMergeCommitconflictResolutiondeleteFilesTypeDef
):
    """
    Type definition for `ClientCreateUnreferencedMergeCommitconflictResolution` `deleteFiles`

    A file that will be deleted as part of a commit.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path of the file that will be deleted, including the name of the file.
    """


_RequiredClientCreateUnreferencedMergeCommitconflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientCreateUnreferencedMergeCommitconflictResolutionreplaceContentsTypeDef",
    {"filePath": str, "replacementType": str},
)
_OptionalClientCreateUnreferencedMergeCommitconflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientCreateUnreferencedMergeCommitconflictResolutionreplaceContentsTypeDef",
    {"content": bytes, "fileMode": str},
    total=False,
)


class ClientCreateUnreferencedMergeCommitconflictResolutionreplaceContentsTypeDef(
    _RequiredClientCreateUnreferencedMergeCommitconflictResolutionreplaceContentsTypeDef,
    _OptionalClientCreateUnreferencedMergeCommitconflictResolutionreplaceContentsTypeDef,
):
    """
    Type definition for `ClientCreateUnreferencedMergeCommitconflictResolution` `replaceContents`

    Information about a replacement content entry in the conflict of a merge or pull request
    operation.

    - **filePath** *(string) --* **[REQUIRED]**

      The path of the conflicting file.

    - **replacementType** *(string) --* **[REQUIRED]**

      The replacement type to use when determining how to resolve the conflict.

    - **content** *(bytes) --*

      The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

    - **fileMode** *(string) --*

      The file mode to apply during conflict resoltion.
    """


_ClientCreateUnreferencedMergeCommitconflictResolutionsetFileModesTypeDef = TypedDict(
    "_ClientCreateUnreferencedMergeCommitconflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": str},
)


class ClientCreateUnreferencedMergeCommitconflictResolutionsetFileModesTypeDef(
    _ClientCreateUnreferencedMergeCommitconflictResolutionsetFileModesTypeDef
):
    """
    Type definition for `ClientCreateUnreferencedMergeCommitconflictResolution` `setFileModes`

    Information about the file mode changes.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path to the file, including the name of the file.

    - **fileMode** *(string) --* **[REQUIRED]**

      The file mode for the file.
    """


_ClientCreateUnreferencedMergeCommitconflictResolutionTypeDef = TypedDict(
    "_ClientCreateUnreferencedMergeCommitconflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientCreateUnreferencedMergeCommitconflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[
            ClientCreateUnreferencedMergeCommitconflictResolutiondeleteFilesTypeDef
        ],
        "setFileModes": List[
            ClientCreateUnreferencedMergeCommitconflictResolutionsetFileModesTypeDef
        ],
    },
    total=False,
)


class ClientCreateUnreferencedMergeCommitconflictResolutionTypeDef(
    _ClientCreateUnreferencedMergeCommitconflictResolutionTypeDef
):
    """
    Type definition for `ClientCreateUnreferencedMergeCommit` `conflictResolution`

    A list of inputs to use when resolving conflicts during a merge if AUTOMERGE is chosen as the
    conflict resolution strategy.

    - **replaceContents** *(list) --*

      Files that will have content replaced as part of the merge conflict resolution.

      - *(dict) --*

        Information about a replacement content entry in the conflict of a merge or pull request
        operation.

        - **filePath** *(string) --* **[REQUIRED]**

          The path of the conflicting file.

        - **replacementType** *(string) --* **[REQUIRED]**

          The replacement type to use when determining how to resolve the conflict.

        - **content** *(bytes) --*

          The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

        - **fileMode** *(string) --*

          The file mode to apply during conflict resoltion.

    - **deleteFiles** *(list) --*

      Files that will be deleted as part of the merge conflict resolution.

      - *(dict) --*

        A file that will be deleted as part of a commit.

        - **filePath** *(string) --* **[REQUIRED]**

          The full path of the file that will be deleted, including the name of the file.

    - **setFileModes** *(list) --*

      File modes that will be set as part of the merge conflict resolution.

      - *(dict) --*

        Information about the file mode changes.

        - **filePath** *(string) --* **[REQUIRED]**

          The full path to the file, including the name of the file.

        - **fileMode** *(string) --* **[REQUIRED]**

          The file mode for the file.
    """


_ClientDeleteBranchResponsedeletedBranchTypeDef = TypedDict(
    "_ClientDeleteBranchResponsedeletedBranchTypeDef",
    {"branchName": str, "commitId": str},
    total=False,
)


class ClientDeleteBranchResponsedeletedBranchTypeDef(
    _ClientDeleteBranchResponsedeletedBranchTypeDef
):
    """
    Type definition for `ClientDeleteBranchResponse` `deletedBranch`

    Information about the branch deleted by the operation, including the branch name and the
    commit ID that was the tip of the branch.

    - **branchName** *(string) --*

      The name of the branch.

    - **commitId** *(string) --*

      The ID of the last commit made to the branch.
    """


_ClientDeleteBranchResponseTypeDef = TypedDict(
    "_ClientDeleteBranchResponseTypeDef",
    {"deletedBranch": ClientDeleteBranchResponsedeletedBranchTypeDef},
    total=False,
)


class ClientDeleteBranchResponseTypeDef(_ClientDeleteBranchResponseTypeDef):
    """
    Type definition for `ClientDeleteBranch` `Response`

    Represents the output of a delete branch operation.

    - **deletedBranch** *(dict) --*

      Information about the branch deleted by the operation, including the branch name and the
      commit ID that was the tip of the branch.

      - **branchName** *(string) --*

        The name of the branch.

      - **commitId** *(string) --*

        The ID of the last commit made to the branch.
    """


_ClientDeleteCommentContentResponsecommentTypeDef = TypedDict(
    "_ClientDeleteCommentContentResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientDeleteCommentContentResponsecommentTypeDef(
    _ClientDeleteCommentContentResponsecommentTypeDef
):
    """
    Type definition for `ClientDeleteCommentContentResponse` `comment`

    Information about the comment you just deleted.

    - **commentId** *(string) --*

      The system-generated comment ID.

    - **content** *(string) --*

      The content of the comment.

    - **inReplyTo** *(string) --*

      The ID of the comment for which this comment is a reply, if any.

    - **creationDate** *(datetime) --*

      The date and time the comment was created, in timestamp format.

    - **lastModifiedDate** *(datetime) --*

      The date and time the comment was most recently modified, in timestamp format.

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the person who posted the comment.

    - **deleted** *(boolean) --*

      A Boolean value indicating whether the comment has been deleted.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientDeleteCommentContentResponseTypeDef = TypedDict(
    "_ClientDeleteCommentContentResponseTypeDef",
    {"comment": ClientDeleteCommentContentResponsecommentTypeDef},
    total=False,
)


class ClientDeleteCommentContentResponseTypeDef(
    _ClientDeleteCommentContentResponseTypeDef
):
    """
    Type definition for `ClientDeleteCommentContent` `Response`

    - **comment** *(dict) --*

      Information about the comment you just deleted.

      - **commentId** *(string) --*

        The system-generated comment ID.

      - **content** *(string) --*

        The content of the comment.

      - **inReplyTo** *(string) --*

        The ID of the comment for which this comment is a reply, if any.

      - **creationDate** *(datetime) --*

        The date and time the comment was created, in timestamp format.

      - **lastModifiedDate** *(datetime) --*

        The date and time the comment was most recently modified, in timestamp format.

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the person who posted the comment.

      - **deleted** *(boolean) --*

        A Boolean value indicating whether the comment has been deleted.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_ClientDeleteFileResponseTypeDef = TypedDict(
    "_ClientDeleteFileResponseTypeDef",
    {"commitId": str, "blobId": str, "treeId": str, "filePath": str},
    total=False,
)


class ClientDeleteFileResponseTypeDef(_ClientDeleteFileResponseTypeDef):
    """
    Type definition for `ClientDeleteFile` `Response`

    - **commitId** *(string) --*

      The full commit ID of the commit that contains the change that deletes the file.

    - **blobId** *(string) --*

      The blob ID removed from the tree as part of deleting the file.

    - **treeId** *(string) --*

      The full SHA-1 pointer of the tree information for the commit that contains the delete file
      change.

    - **filePath** *(string) --*

      The fully-qualified path to the file that will be deleted, including the full name and
      extension of that file.
    """


_ClientDeleteRepositoryResponseTypeDef = TypedDict(
    "_ClientDeleteRepositoryResponseTypeDef", {"repositoryId": str}, total=False
)


class ClientDeleteRepositoryResponseTypeDef(_ClientDeleteRepositoryResponseTypeDef):
    """
    Type definition for `ClientDeleteRepository` `Response`

    Represents the output of a delete repository operation.

    - **repositoryId** *(string) --*

      The ID of the repository that was deleted.
    """


_ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef",
    {"source": str, "destination": str, "base": str},
    total=False,
)


class ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef(
    _ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef
):
    """
    Type definition for `ClientDescribeMergeConflictsResponseconflictMetadata` `fileModes`

    The file modes of the file in the source, destination, and base of the merge.

    - **source** *(string) --*

      The file mode of a file in the source of a merge or pull request.

    - **destination** *(string) --*

      The file mode of a file in the destination of a merge or pull request.

    - **base** *(string) --*

      The file mode of a file in the base of a merge or pull request.
    """


_ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef",
    {"source": int, "destination": int, "base": int},
    total=False,
)


class ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef(
    _ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef
):
    """
    Type definition for `ClientDescribeMergeConflictsResponseconflictMetadata` `fileSizes`

    The file sizes of the file in the source, destination, and base of the merge.

    - **source** *(integer) --*

      The size of a file in the source of a merge or pull request.

    - **destination** *(integer) --*

      The size of a file in the destination of a merge or pull request.

    - **base** *(integer) --*

      The size of a file in the base of a merge or pull request.
    """


_ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef",
    {"source": bool, "destination": bool, "base": bool},
    total=False,
)


class ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef(
    _ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef
):
    """
    Type definition for `ClientDescribeMergeConflictsResponseconflictMetadata` `isBinaryFile`

    A boolean value (true or false) indicating whether the file is binary or textual in the
    source, destination, and base of the merge.

    - **source** *(boolean) --*

      The binary or non-binary status of file in the source of a merge or pull request.

    - **destination** *(boolean) --*

      The binary or non-binary status of a file in the destination of a merge or pull request.

    - **base** *(boolean) --*

      The binary or non-binary status of a file in the base of a merge or pull request.
    """


_ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef",
    {"source": str, "destination": str},
    total=False,
)


class ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef(
    _ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef
):
    """
    Type definition for `ClientDescribeMergeConflictsResponseconflictMetadata` `mergeOperations`

    Whether an add, modify, or delete operation caused the conflict between the source and
    destination of the merge.

    - **source** *(string) --*

      The operation on a file (add, modify, or delete) of a file in the source of a merge or
      pull request.

    - **destination** *(string) --*

      The operation on a file in the destination of a merge or pull request.
    """


_ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef",
    {"source": str, "destination": str, "base": str},
    total=False,
)


class ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef(
    _ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef
):
    """
    Type definition for `ClientDescribeMergeConflictsResponseconflictMetadata` `objectTypes`

    Information about any object type conflicts in a merge operation.

    - **source** *(string) --*

      The type of the object in the source branch.

    - **destination** *(string) --*

      The type of the object in the destination branch.

    - **base** *(string) --*

      The type of the object in the base commit of the merge.
    """


_ClientDescribeMergeConflictsResponseconflictMetadataTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseconflictMetadataTypeDef",
    {
        "filePath": str,
        "fileSizes": ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef,
        "fileModes": ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef,
        "objectTypes": ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef,
        "numberOfConflicts": int,
        "isBinaryFile": ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef,
        "contentConflict": bool,
        "fileModeConflict": bool,
        "objectTypeConflict": bool,
        "mergeOperations": ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef,
    },
    total=False,
)


class ClientDescribeMergeConflictsResponseconflictMetadataTypeDef(
    _ClientDescribeMergeConflictsResponseconflictMetadataTypeDef
):
    """
    Type definition for `ClientDescribeMergeConflictsResponse` `conflictMetadata`

    Contains metadata about the conflicts found in the merge.

    - **filePath** *(string) --*

      The path of the file that contains conflicts.

    - **fileSizes** *(dict) --*

      The file sizes of the file in the source, destination, and base of the merge.

      - **source** *(integer) --*

        The size of a file in the source of a merge or pull request.

      - **destination** *(integer) --*

        The size of a file in the destination of a merge or pull request.

      - **base** *(integer) --*

        The size of a file in the base of a merge or pull request.

    - **fileModes** *(dict) --*

      The file modes of the file in the source, destination, and base of the merge.

      - **source** *(string) --*

        The file mode of a file in the source of a merge or pull request.

      - **destination** *(string) --*

        The file mode of a file in the destination of a merge or pull request.

      - **base** *(string) --*

        The file mode of a file in the base of a merge or pull request.

    - **objectTypes** *(dict) --*

      Information about any object type conflicts in a merge operation.

      - **source** *(string) --*

        The type of the object in the source branch.

      - **destination** *(string) --*

        The type of the object in the destination branch.

      - **base** *(string) --*

        The type of the object in the base commit of the merge.

    - **numberOfConflicts** *(integer) --*

      The number of conflicts, including both hunk conflicts and metadata conflicts.

    - **isBinaryFile** *(dict) --*

      A boolean value (true or false) indicating whether the file is binary or textual in the
      source, destination, and base of the merge.

      - **source** *(boolean) --*

        The binary or non-binary status of file in the source of a merge or pull request.

      - **destination** *(boolean) --*

        The binary or non-binary status of a file in the destination of a merge or pull request.

      - **base** *(boolean) --*

        The binary or non-binary status of a file in the base of a merge or pull request.

    - **contentConflict** *(boolean) --*

      A boolean value indicating whether there are conflicts in the content of a file.

    - **fileModeConflict** *(boolean) --*

      A boolean value indicating whether there are conflicts in the file mode of a file.

    - **objectTypeConflict** *(boolean) --*

      A boolean value (true or false) indicating whether there are conflicts between the branches
      in the object type of a file, folder, or submodule.

    - **mergeOperations** *(dict) --*

      Whether an add, modify, or delete operation caused the conflict between the source and
      destination of the merge.

      - **source** *(string) --*

        The operation on a file (add, modify, or delete) of a file in the source of a merge or
        pull request.

      - **destination** *(string) --*

        The operation on a file in the destination of a merge or pull request.
    """


_ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)


class ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef(
    _ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef
):
    """
    Type definition for `ClientDescribeMergeConflictsResponsemergeHunks` `base`

    Information about the merge hunk in the base of a merge or pull request.

    - **startLine** *(integer) --*

      The start position of the hunk in the merge result.

    - **endLine** *(integer) --*

      The end position of the hunk in the merge result.

    - **hunkContent** *(string) --*

      The base-64 encoded content of the hunk merged region that might or might not contain a
      conflict.
    """


_ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)


class ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef(
    _ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef
):
    """
    Type definition for `ClientDescribeMergeConflictsResponsemergeHunks` `destination`

    Information about the merge hunk in the destination of a merge or pull request.

    - **startLine** *(integer) --*

      The start position of the hunk in the merge result.

    - **endLine** *(integer) --*

      The end position of the hunk in the merge result.

    - **hunkContent** *(string) --*

      The base-64 encoded content of the hunk merged region that might or might not contain a
      conflict.
    """


_ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)


class ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef(
    _ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef
):
    """
    Type definition for `ClientDescribeMergeConflictsResponsemergeHunks` `source`

    Information about the merge hunk in the source of a merge or pull request.

    - **startLine** *(integer) --*

      The start position of the hunk in the merge result.

    - **endLine** *(integer) --*

      The end position of the hunk in the merge result.

    - **hunkContent** *(string) --*

      The base-64 encoded content of the hunk merged region that might or might not contain a
      conflict.
    """


_ClientDescribeMergeConflictsResponsemergeHunksTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponsemergeHunksTypeDef",
    {
        "isConflict": bool,
        "source": ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef,
        "destination": ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef,
        "base": ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef,
    },
    total=False,
)


class ClientDescribeMergeConflictsResponsemergeHunksTypeDef(
    _ClientDescribeMergeConflictsResponsemergeHunksTypeDef
):
    """
    Type definition for `ClientDescribeMergeConflictsResponse` `mergeHunks`

    Information about merge hunks in a merge or pull request operation.

    - **isConflict** *(boolean) --*

      A Boolean value indicating whether a combination of hunks contains a conflict. Conflicts
      occur when the same file or the same lines in a file were modified in both the source and
      destination of a merge or pull request. Valid values include true, false, and null. This
      will be true when the hunk represents a conflict and one or more files contains a line
      conflict. File mode conflicts in a merge will not set this to be true.

    - **source** *(dict) --*

      Information about the merge hunk in the source of a merge or pull request.

      - **startLine** *(integer) --*

        The start position of the hunk in the merge result.

      - **endLine** *(integer) --*

        The end position of the hunk in the merge result.

      - **hunkContent** *(string) --*

        The base-64 encoded content of the hunk merged region that might or might not contain a
        conflict.

    - **destination** *(dict) --*

      Information about the merge hunk in the destination of a merge or pull request.

      - **startLine** *(integer) --*

        The start position of the hunk in the merge result.

      - **endLine** *(integer) --*

        The end position of the hunk in the merge result.

      - **hunkContent** *(string) --*

        The base-64 encoded content of the hunk merged region that might or might not contain a
        conflict.

    - **base** *(dict) --*

      Information about the merge hunk in the base of a merge or pull request.

      - **startLine** *(integer) --*

        The start position of the hunk in the merge result.

      - **endLine** *(integer) --*

        The end position of the hunk in the merge result.

      - **hunkContent** *(string) --*

        The base-64 encoded content of the hunk merged region that might or might not contain a
        conflict.
    """


_ClientDescribeMergeConflictsResponseTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseTypeDef",
    {
        "conflictMetadata": ClientDescribeMergeConflictsResponseconflictMetadataTypeDef,
        "mergeHunks": List[ClientDescribeMergeConflictsResponsemergeHunksTypeDef],
        "nextToken": str,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
    },
    total=False,
)


class ClientDescribeMergeConflictsResponseTypeDef(
    _ClientDescribeMergeConflictsResponseTypeDef
):
    """
    Type definition for `ClientDescribeMergeConflicts` `Response`

    - **conflictMetadata** *(dict) --*

      Contains metadata about the conflicts found in the merge.

      - **filePath** *(string) --*

        The path of the file that contains conflicts.

      - **fileSizes** *(dict) --*

        The file sizes of the file in the source, destination, and base of the merge.

        - **source** *(integer) --*

          The size of a file in the source of a merge or pull request.

        - **destination** *(integer) --*

          The size of a file in the destination of a merge or pull request.

        - **base** *(integer) --*

          The size of a file in the base of a merge or pull request.

      - **fileModes** *(dict) --*

        The file modes of the file in the source, destination, and base of the merge.

        - **source** *(string) --*

          The file mode of a file in the source of a merge or pull request.

        - **destination** *(string) --*

          The file mode of a file in the destination of a merge or pull request.

        - **base** *(string) --*

          The file mode of a file in the base of a merge or pull request.

      - **objectTypes** *(dict) --*

        Information about any object type conflicts in a merge operation.

        - **source** *(string) --*

          The type of the object in the source branch.

        - **destination** *(string) --*

          The type of the object in the destination branch.

        - **base** *(string) --*

          The type of the object in the base commit of the merge.

      - **numberOfConflicts** *(integer) --*

        The number of conflicts, including both hunk conflicts and metadata conflicts.

      - **isBinaryFile** *(dict) --*

        A boolean value (true or false) indicating whether the file is binary or textual in the
        source, destination, and base of the merge.

        - **source** *(boolean) --*

          The binary or non-binary status of file in the source of a merge or pull request.

        - **destination** *(boolean) --*

          The binary or non-binary status of a file in the destination of a merge or pull request.

        - **base** *(boolean) --*

          The binary or non-binary status of a file in the base of a merge or pull request.

      - **contentConflict** *(boolean) --*

        A boolean value indicating whether there are conflicts in the content of a file.

      - **fileModeConflict** *(boolean) --*

        A boolean value indicating whether there are conflicts in the file mode of a file.

      - **objectTypeConflict** *(boolean) --*

        A boolean value (true or false) indicating whether there are conflicts between the branches
        in the object type of a file, folder, or submodule.

      - **mergeOperations** *(dict) --*

        Whether an add, modify, or delete operation caused the conflict between the source and
        destination of the merge.

        - **source** *(string) --*

          The operation on a file (add, modify, or delete) of a file in the source of a merge or
          pull request.

        - **destination** *(string) --*

          The operation on a file in the destination of a merge or pull request.

    - **mergeHunks** *(list) --*

      A list of merge hunks of the differences between the files or lines.

      - *(dict) --*

        Information about merge hunks in a merge or pull request operation.

        - **isConflict** *(boolean) --*

          A Boolean value indicating whether a combination of hunks contains a conflict. Conflicts
          occur when the same file or the same lines in a file were modified in both the source and
          destination of a merge or pull request. Valid values include true, false, and null. This
          will be true when the hunk represents a conflict and one or more files contains a line
          conflict. File mode conflicts in a merge will not set this to be true.

        - **source** *(dict) --*

          Information about the merge hunk in the source of a merge or pull request.

          - **startLine** *(integer) --*

            The start position of the hunk in the merge result.

          - **endLine** *(integer) --*

            The end position of the hunk in the merge result.

          - **hunkContent** *(string) --*

            The base-64 encoded content of the hunk merged region that might or might not contain a
            conflict.

        - **destination** *(dict) --*

          Information about the merge hunk in the destination of a merge or pull request.

          - **startLine** *(integer) --*

            The start position of the hunk in the merge result.

          - **endLine** *(integer) --*

            The end position of the hunk in the merge result.

          - **hunkContent** *(string) --*

            The base-64 encoded content of the hunk merged region that might or might not contain a
            conflict.

        - **base** *(dict) --*

          Information about the merge hunk in the base of a merge or pull request.

          - **startLine** *(integer) --*

            The start position of the hunk in the merge result.

          - **endLine** *(integer) --*

            The end position of the hunk in the merge result.

          - **hunkContent** *(string) --*

            The base-64 encoded content of the hunk merged region that might or might not contain a
            conflict.

    - **nextToken** *(string) --*

      An enumeration token that can be used in a request to return the next batch of the results.

    - **destinationCommitId** *(string) --*

      The commit ID of the destination commit specifier that was used in the merge evaluation.

    - **sourceCommitId** *(string) --*

      The commit ID of the source commit specifier that was used in the merge evaluation.

    - **baseCommitId** *(string) --*

      The commit ID of the merge base.
    """


_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "sourceCommitId": str,
        "destinationCommitId": str,
        "mergeBase": str,
    },
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef
):
    """
    Type definition for `ClientDescribePullRequestEventsResponsepullRequestEvents` `pullRequestCreatedEventMetadata`

    Information about the source and destination branches for the pull request.

    - **repositoryName** *(string) --*

      The name of the repository where the pull request was created.

    - **sourceCommitId** *(string) --*

      The commit ID on the source branch used when the pull request was created.

    - **destinationCommitId** *(string) --*

      The commit ID of the tip of the branch specified as the destination branch when the
      pull request was created.

    - **mergeBase** *(string) --*

      The commit ID of the most recent commit that the source branch and the destination
      branch have in common.
    """


_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef",
    {"isMerged": bool, "mergedBy": str, "mergeCommitId": str, "mergeOption": str},
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef
):
    """
    Type definition for `ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadata` `mergeMetadata`

    Information about the merge state change event.

    - **isMerged** *(boolean) --*

      A Boolean value indicating whether the merge has been made.

    - **mergedBy** *(string) --*

      The Amazon Resource Name (ARN) of the user who merged the branches.

    - **mergeCommitId** *(string) --*

      The commit ID for the merge commit, if any.

    - **mergeOption** *(string) --*

      The merge strategy used in the merge.
    """


_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "destinationReference": str,
        "mergeMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef,
    },
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef
):
    """
    Type definition for `ClientDescribePullRequestEventsResponsepullRequestEvents` `pullRequestMergedStateChangedEventMetadata`

    Information about the change in mergability state for the pull request event.

    - **repositoryName** *(string) --*

      The name of the repository where the pull request was created.

    - **destinationReference** *(string) --*

      The name of the branch that the pull request will be merged into.

    - **mergeMetadata** *(dict) --*

      Information about the merge state change event.

      - **isMerged** *(boolean) --*

        A Boolean value indicating whether the merge has been made.

      - **mergedBy** *(string) --*

        The Amazon Resource Name (ARN) of the user who merged the branches.

      - **mergeCommitId** *(string) --*

        The commit ID for the merge commit, if any.

      - **mergeOption** *(string) --*

        The merge strategy used in the merge.
    """


_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "mergeBase": str,
    },
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef
):
    """
    Type definition for `ClientDescribePullRequestEventsResponsepullRequestEvents` `pullRequestSourceReferenceUpdatedEventMetadata`

    Information about the updated source branch for the pull request event.

    - **repositoryName** *(string) --*

      The name of the repository where the pull request was updated.

    - **beforeCommitId** *(string) --*

      The full commit ID of the commit in the destination branch that was the tip of the
      branch at the time the pull request was updated.

    - **afterCommitId** *(string) --*

      The full commit ID of the commit in the source branch that was the tip of the branch at
      the time the pull request was updated.

    - **mergeBase** *(string) --*

      The commit ID of the most recent commit that the source branch and the destination
      branch have in common.
    """


_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef",
    {"pullRequestStatus": str},
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef
):
    """
    Type definition for `ClientDescribePullRequestEventsResponsepullRequestEvents` `pullRequestStatusChangedEventMetadata`

    Information about the change in status for the pull request event.

    - **pullRequestStatus** *(string) --*

      The changed status of the pull request.
    """


_ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef",
    {
        "pullRequestId": str,
        "eventDate": datetime,
        "pullRequestEventType": str,
        "actorArn": str,
        "pullRequestCreatedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef,
        "pullRequestStatusChangedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef,
        "pullRequestSourceReferenceUpdatedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef,
        "pullRequestMergedStateChangedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef,
    },
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef
):
    """
    Type definition for `ClientDescribePullRequestEventsResponse` `pullRequestEvents`

    Returns information about a pull request event.

    - **pullRequestId** *(string) --*

      The system-generated ID of the pull request.

    - **eventDate** *(datetime) --*

      The day and time of the pull request event, in timestamp format.

    - **pullRequestEventType** *(string) --*

      The type of the pull request event, for example a status change event
      (PULL_REQUEST_STATUS_CHANGED) or update event (PULL_REQUEST_SOURCE_REFERENCE_UPDATED).

    - **actorArn** *(string) --*

      The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples
      include updating the pull request with additional commits or changing the status of a
      pull request.

    - **pullRequestCreatedEventMetadata** *(dict) --*

      Information about the source and destination branches for the pull request.

      - **repositoryName** *(string) --*

        The name of the repository where the pull request was created.

      - **sourceCommitId** *(string) --*

        The commit ID on the source branch used when the pull request was created.

      - **destinationCommitId** *(string) --*

        The commit ID of the tip of the branch specified as the destination branch when the
        pull request was created.

      - **mergeBase** *(string) --*

        The commit ID of the most recent commit that the source branch and the destination
        branch have in common.

    - **pullRequestStatusChangedEventMetadata** *(dict) --*

      Information about the change in status for the pull request event.

      - **pullRequestStatus** *(string) --*

        The changed status of the pull request.

    - **pullRequestSourceReferenceUpdatedEventMetadata** *(dict) --*

      Information about the updated source branch for the pull request event.

      - **repositoryName** *(string) --*

        The name of the repository where the pull request was updated.

      - **beforeCommitId** *(string) --*

        The full commit ID of the commit in the destination branch that was the tip of the
        branch at the time the pull request was updated.

      - **afterCommitId** *(string) --*

        The full commit ID of the commit in the source branch that was the tip of the branch at
        the time the pull request was updated.

      - **mergeBase** *(string) --*

        The commit ID of the most recent commit that the source branch and the destination
        branch have in common.

    - **pullRequestMergedStateChangedEventMetadata** *(dict) --*

      Information about the change in mergability state for the pull request event.

      - **repositoryName** *(string) --*

        The name of the repository where the pull request was created.

      - **destinationReference** *(string) --*

        The name of the branch that the pull request will be merged into.

      - **mergeMetadata** *(dict) --*

        Information about the merge state change event.

        - **isMerged** *(boolean) --*

          A Boolean value indicating whether the merge has been made.

        - **mergedBy** *(string) --*

          The Amazon Resource Name (ARN) of the user who merged the branches.

        - **mergeCommitId** *(string) --*

          The commit ID for the merge commit, if any.

        - **mergeOption** *(string) --*

          The merge strategy used in the merge.
    """


_ClientDescribePullRequestEventsResponseTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponseTypeDef",
    {
        "pullRequestEvents": List[
            ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribePullRequestEventsResponseTypeDef(
    _ClientDescribePullRequestEventsResponseTypeDef
):
    """
    Type definition for `ClientDescribePullRequestEvents` `Response`

    - **pullRequestEvents** *(list) --*

      Information about the pull request events.

      - *(dict) --*

        Returns information about a pull request event.

        - **pullRequestId** *(string) --*

          The system-generated ID of the pull request.

        - **eventDate** *(datetime) --*

          The day and time of the pull request event, in timestamp format.

        - **pullRequestEventType** *(string) --*

          The type of the pull request event, for example a status change event
          (PULL_REQUEST_STATUS_CHANGED) or update event (PULL_REQUEST_SOURCE_REFERENCE_UPDATED).

        - **actorArn** *(string) --*

          The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples
          include updating the pull request with additional commits or changing the status of a
          pull request.

        - **pullRequestCreatedEventMetadata** *(dict) --*

          Information about the source and destination branches for the pull request.

          - **repositoryName** *(string) --*

            The name of the repository where the pull request was created.

          - **sourceCommitId** *(string) --*

            The commit ID on the source branch used when the pull request was created.

          - **destinationCommitId** *(string) --*

            The commit ID of the tip of the branch specified as the destination branch when the
            pull request was created.

          - **mergeBase** *(string) --*

            The commit ID of the most recent commit that the source branch and the destination
            branch have in common.

        - **pullRequestStatusChangedEventMetadata** *(dict) --*

          Information about the change in status for the pull request event.

          - **pullRequestStatus** *(string) --*

            The changed status of the pull request.

        - **pullRequestSourceReferenceUpdatedEventMetadata** *(dict) --*

          Information about the updated source branch for the pull request event.

          - **repositoryName** *(string) --*

            The name of the repository where the pull request was updated.

          - **beforeCommitId** *(string) --*

            The full commit ID of the commit in the destination branch that was the tip of the
            branch at the time the pull request was updated.

          - **afterCommitId** *(string) --*

            The full commit ID of the commit in the source branch that was the tip of the branch at
            the time the pull request was updated.

          - **mergeBase** *(string) --*

            The commit ID of the most recent commit that the source branch and the destination
            branch have in common.

        - **pullRequestMergedStateChangedEventMetadata** *(dict) --*

          Information about the change in mergability state for the pull request event.

          - **repositoryName** *(string) --*

            The name of the repository where the pull request was created.

          - **destinationReference** *(string) --*

            The name of the branch that the pull request will be merged into.

          - **mergeMetadata** *(dict) --*

            Information about the merge state change event.

            - **isMerged** *(boolean) --*

              A Boolean value indicating whether the merge has been made.

            - **mergedBy** *(string) --*

              The Amazon Resource Name (ARN) of the user who merged the branches.

            - **mergeCommitId** *(string) --*

              The commit ID for the merge commit, if any.

            - **mergeOption** *(string) --*

              The merge strategy used in the merge.

    - **nextToken** *(string) --*

      An enumeration token that can be used in a request to return the next batch of the results.
    """


_ClientGetBlobResponseTypeDef = TypedDict(
    "_ClientGetBlobResponseTypeDef", {"content": bytes}, total=False
)


class ClientGetBlobResponseTypeDef(_ClientGetBlobResponseTypeDef):
    """
    Type definition for `ClientGetBlob` `Response`

    Represents the output of a get blob operation.

    - **content** *(bytes) --*

      The content of the blob, usually a file.
    """


_ClientGetBranchResponsebranchTypeDef = TypedDict(
    "_ClientGetBranchResponsebranchTypeDef",
    {"branchName": str, "commitId": str},
    total=False,
)


class ClientGetBranchResponsebranchTypeDef(_ClientGetBranchResponsebranchTypeDef):
    """
    Type definition for `ClientGetBranchResponse` `branch`

    The name of the branch.

    - **branchName** *(string) --*

      The name of the branch.

    - **commitId** *(string) --*

      The ID of the last commit made to the branch.
    """


_ClientGetBranchResponseTypeDef = TypedDict(
    "_ClientGetBranchResponseTypeDef",
    {"branch": ClientGetBranchResponsebranchTypeDef},
    total=False,
)


class ClientGetBranchResponseTypeDef(_ClientGetBranchResponseTypeDef):
    """
    Type definition for `ClientGetBranch` `Response`

    Represents the output of a get branch operation.

    - **branch** *(dict) --*

      The name of the branch.

      - **branchName** *(string) --*

        The name of the branch.

      - **commitId** *(string) --*

        The ID of the last commit made to the branch.
    """


_ClientGetCommentResponsecommentTypeDef = TypedDict(
    "_ClientGetCommentResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientGetCommentResponsecommentTypeDef(_ClientGetCommentResponsecommentTypeDef):
    """
    Type definition for `ClientGetCommentResponse` `comment`

    The contents of the comment.

    - **commentId** *(string) --*

      The system-generated comment ID.

    - **content** *(string) --*

      The content of the comment.

    - **inReplyTo** *(string) --*

      The ID of the comment for which this comment is a reply, if any.

    - **creationDate** *(datetime) --*

      The date and time the comment was created, in timestamp format.

    - **lastModifiedDate** *(datetime) --*

      The date and time the comment was most recently modified, in timestamp format.

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the person who posted the comment.

    - **deleted** *(boolean) --*

      A Boolean value indicating whether the comment has been deleted.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientGetCommentResponseTypeDef = TypedDict(
    "_ClientGetCommentResponseTypeDef",
    {"comment": ClientGetCommentResponsecommentTypeDef},
    total=False,
)


class ClientGetCommentResponseTypeDef(_ClientGetCommentResponseTypeDef):
    """
    Type definition for `ClientGetComment` `Response`

    - **comment** *(dict) --*

      The contents of the comment.

      - **commentId** *(string) --*

        The system-generated comment ID.

      - **content** *(string) --*

        The content of the comment.

      - **inReplyTo** *(string) --*

        The ID of the comment for which this comment is a reply, if any.

      - **creationDate** *(datetime) --*

        The date and time the comment was created, in timestamp format.

      - **lastModifiedDate** *(datetime) --*

        The date and time the comment was most recently modified, in timestamp format.

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the person who posted the comment.

      - **deleted** *(boolean) --*

        A Boolean value indicating whether the comment has been deleted.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef = TypedDict(
    "_ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef(
    _ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef
):
    """
    Type definition for `ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitData` `comments`

    Returns information about a specific comment.

    - **commentId** *(string) --*

      The system-generated comment ID.

    - **content** *(string) --*

      The content of the comment.

    - **inReplyTo** *(string) --*

      The ID of the comment for which this comment is a reply, if any.

    - **creationDate** *(datetime) --*

      The date and time the comment was created, in timestamp format.

    - **lastModifiedDate** *(datetime) --*

      The date and time the comment was most recently modified, in timestamp format.

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the person who posted the comment.

    - **deleted** *(boolean) --*

      A Boolean value indicating whether the comment has been deleted.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures
      the request cannot be repeated with a changed parameter. If a request is received
      with the same parameters and a token is included, the request will return information
      about the initial request that used that token.
    """


_ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef = TypedDict(
    "_ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": str},
    total=False,
)


class ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef(
    _ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef
):
    """
    Type definition for `ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitData` `location`

    Location information about the comment on the comparison, including the file name, line
    number, and whether the version of the file where the comment was made is 'BEFORE' or
    'AFTER'.

    - **filePath** *(string) --*

      The name of the file being compared, including its extension and subdirectory, if any.

    - **filePosition** *(integer) --*

      The position of a change within a compared file, in line number format.

    - **relativeFileVersion** *(string) --*

      In a comparison of commits or a pull request, whether the change is in the 'before' or
      'after' of that comparison.
    """


_ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef = TypedDict(
    "_ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef,
        "comments": List[
            ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef
        ],
    },
    total=False,
)


class ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef(
    _ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef
):
    """
    Type definition for `ClientGetCommentsForComparedCommitResponse` `commentsForComparedCommitData`

    Returns information about comments on the comparison between two commits.

    - **repositoryName** *(string) --*

      The name of the repository that contains the compared commits.

    - **beforeCommitId** *(string) --*

      The full commit ID of the commit used to establish the 'before' of the comparison.

    - **afterCommitId** *(string) --*

      The full commit ID of the commit used to establish the 'after' of the comparison.

    - **beforeBlobId** *(string) --*

      The full blob ID of the commit used to establish the 'before' of the comparison.

    - **afterBlobId** *(string) --*

      The full blob ID of the commit used to establish the 'after' of the comparison.

    - **location** *(dict) --*

      Location information about the comment on the comparison, including the file name, line
      number, and whether the version of the file where the comment was made is 'BEFORE' or
      'AFTER'.

      - **filePath** *(string) --*

        The name of the file being compared, including its extension and subdirectory, if any.

      - **filePosition** *(integer) --*

        The position of a change within a compared file, in line number format.

      - **relativeFileVersion** *(string) --*

        In a comparison of commits or a pull request, whether the change is in the 'before' or
        'after' of that comparison.

    - **comments** *(list) --*

      An array of comment objects. Each comment object contains information about a comment on
      the comparison between commits.

      - *(dict) --*

        Returns information about a specific comment.

        - **commentId** *(string) --*

          The system-generated comment ID.

        - **content** *(string) --*

          The content of the comment.

        - **inReplyTo** *(string) --*

          The ID of the comment for which this comment is a reply, if any.

        - **creationDate** *(datetime) --*

          The date and time the comment was created, in timestamp format.

        - **lastModifiedDate** *(datetime) --*

          The date and time the comment was most recently modified, in timestamp format.

        - **authorArn** *(string) --*

          The Amazon Resource Name (ARN) of the person who posted the comment.

        - **deleted** *(boolean) --*

          A Boolean value indicating whether the comment has been deleted.

        - **clientRequestToken** *(string) --*

          A unique, client-generated idempotency token that when provided in a request, ensures
          the request cannot be repeated with a changed parameter. If a request is received
          with the same parameters and a token is included, the request will return information
          about the initial request that used that token.
    """


_ClientGetCommentsForComparedCommitResponseTypeDef = TypedDict(
    "_ClientGetCommentsForComparedCommitResponseTypeDef",
    {
        "commentsForComparedCommitData": List[
            ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetCommentsForComparedCommitResponseTypeDef(
    _ClientGetCommentsForComparedCommitResponseTypeDef
):
    """
    Type definition for `ClientGetCommentsForComparedCommit` `Response`

    - **commentsForComparedCommitData** *(list) --*

      A list of comment objects on the compared commit.

      - *(dict) --*

        Returns information about comments on the comparison between two commits.

        - **repositoryName** *(string) --*

          The name of the repository that contains the compared commits.

        - **beforeCommitId** *(string) --*

          The full commit ID of the commit used to establish the 'before' of the comparison.

        - **afterCommitId** *(string) --*

          The full commit ID of the commit used to establish the 'after' of the comparison.

        - **beforeBlobId** *(string) --*

          The full blob ID of the commit used to establish the 'before' of the comparison.

        - **afterBlobId** *(string) --*

          The full blob ID of the commit used to establish the 'after' of the comparison.

        - **location** *(dict) --*

          Location information about the comment on the comparison, including the file name, line
          number, and whether the version of the file where the comment was made is 'BEFORE' or
          'AFTER'.

          - **filePath** *(string) --*

            The name of the file being compared, including its extension and subdirectory, if any.

          - **filePosition** *(integer) --*

            The position of a change within a compared file, in line number format.

          - **relativeFileVersion** *(string) --*

            In a comparison of commits or a pull request, whether the change is in the 'before' or
            'after' of that comparison.

        - **comments** *(list) --*

          An array of comment objects. Each comment object contains information about a comment on
          the comparison between commits.

          - *(dict) --*

            Returns information about a specific comment.

            - **commentId** *(string) --*

              The system-generated comment ID.

            - **content** *(string) --*

              The content of the comment.

            - **inReplyTo** *(string) --*

              The ID of the comment for which this comment is a reply, if any.

            - **creationDate** *(datetime) --*

              The date and time the comment was created, in timestamp format.

            - **lastModifiedDate** *(datetime) --*

              The date and time the comment was most recently modified, in timestamp format.

            - **authorArn** *(string) --*

              The Amazon Resource Name (ARN) of the person who posted the comment.

            - **deleted** *(boolean) --*

              A Boolean value indicating whether the comment has been deleted.

            - **clientRequestToken** *(string) --*

              A unique, client-generated idempotency token that when provided in a request, ensures
              the request cannot be repeated with a changed parameter. If a request is received
              with the same parameters and a token is included, the request will return information
              about the initial request that used that token.

    - **nextToken** *(string) --*

      An enumeration token that can be used in a request to return the next batch of the results.
    """


_ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef = TypedDict(
    "_ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef(
    _ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef
):
    """
    Type definition for `ClientGetCommentsForPullRequestResponsecommentsForPullRequestData` `comments`

    Returns information about a specific comment.

    - **commentId** *(string) --*

      The system-generated comment ID.

    - **content** *(string) --*

      The content of the comment.

    - **inReplyTo** *(string) --*

      The ID of the comment for which this comment is a reply, if any.

    - **creationDate** *(datetime) --*

      The date and time the comment was created, in timestamp format.

    - **lastModifiedDate** *(datetime) --*

      The date and time the comment was most recently modified, in timestamp format.

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the person who posted the comment.

    - **deleted** *(boolean) --*

      A Boolean value indicating whether the comment has been deleted.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures
      the request cannot be repeated with a changed parameter. If a request is received
      with the same parameters and a token is included, the request will return information
      about the initial request that used that token.
    """


_ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef = TypedDict(
    "_ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": str},
    total=False,
)


class ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef(
    _ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef
):
    """
    Type definition for `ClientGetCommentsForPullRequestResponsecommentsForPullRequestData` `location`

    Location information about the comment on the pull request, including the file name, line
    number, and whether the version of the file where the comment was made is 'BEFORE'
    (destination branch) or 'AFTER' (source branch).

    - **filePath** *(string) --*

      The name of the file being compared, including its extension and subdirectory, if any.

    - **filePosition** *(integer) --*

      The position of a change within a compared file, in line number format.

    - **relativeFileVersion** *(string) --*

      In a comparison of commits or a pull request, whether the change is in the 'before' or
      'after' of that comparison.
    """


_ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef = TypedDict(
    "_ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef,
        "comments": List[
            ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef
        ],
    },
    total=False,
)


class ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef(
    _ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef
):
    """
    Type definition for `ClientGetCommentsForPullRequestResponse` `commentsForPullRequestData`

    Returns information about comments on a pull request.

    - **pullRequestId** *(string) --*

      The system-generated ID of the pull request.

    - **repositoryName** *(string) --*

      The name of the repository that contains the pull request.

    - **beforeCommitId** *(string) --*

      The full commit ID of the commit that was the tip of the destination branch when the pull
      request was created. This commit will be superceded by the after commit in the source
      branch when and if you merge the source branch into the destination branch.

    - **afterCommitId** *(string) --*

      he full commit ID of the commit that was the tip of the source branch at the time the
      comment was made.

    - **beforeBlobId** *(string) --*

      The full blob ID of the file on which you want to comment on the destination commit.

    - **afterBlobId** *(string) --*

      The full blob ID of the file on which you want to comment on the source commit.

    - **location** *(dict) --*

      Location information about the comment on the pull request, including the file name, line
      number, and whether the version of the file where the comment was made is 'BEFORE'
      (destination branch) or 'AFTER' (source branch).

      - **filePath** *(string) --*

        The name of the file being compared, including its extension and subdirectory, if any.

      - **filePosition** *(integer) --*

        The position of a change within a compared file, in line number format.

      - **relativeFileVersion** *(string) --*

        In a comparison of commits or a pull request, whether the change is in the 'before' or
        'after' of that comparison.

    - **comments** *(list) --*

      An array of comment objects. Each comment object contains information about a comment on
      the pull request.

      - *(dict) --*

        Returns information about a specific comment.

        - **commentId** *(string) --*

          The system-generated comment ID.

        - **content** *(string) --*

          The content of the comment.

        - **inReplyTo** *(string) --*

          The ID of the comment for which this comment is a reply, if any.

        - **creationDate** *(datetime) --*

          The date and time the comment was created, in timestamp format.

        - **lastModifiedDate** *(datetime) --*

          The date and time the comment was most recently modified, in timestamp format.

        - **authorArn** *(string) --*

          The Amazon Resource Name (ARN) of the person who posted the comment.

        - **deleted** *(boolean) --*

          A Boolean value indicating whether the comment has been deleted.

        - **clientRequestToken** *(string) --*

          A unique, client-generated idempotency token that when provided in a request, ensures
          the request cannot be repeated with a changed parameter. If a request is received
          with the same parameters and a token is included, the request will return information
          about the initial request that used that token.
    """


_ClientGetCommentsForPullRequestResponseTypeDef = TypedDict(
    "_ClientGetCommentsForPullRequestResponseTypeDef",
    {
        "commentsForPullRequestData": List[
            ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetCommentsForPullRequestResponseTypeDef(
    _ClientGetCommentsForPullRequestResponseTypeDef
):
    """
    Type definition for `ClientGetCommentsForPullRequest` `Response`

    - **commentsForPullRequestData** *(list) --*

      An array of comment objects on the pull request.

      - *(dict) --*

        Returns information about comments on a pull request.

        - **pullRequestId** *(string) --*

          The system-generated ID of the pull request.

        - **repositoryName** *(string) --*

          The name of the repository that contains the pull request.

        - **beforeCommitId** *(string) --*

          The full commit ID of the commit that was the tip of the destination branch when the pull
          request was created. This commit will be superceded by the after commit in the source
          branch when and if you merge the source branch into the destination branch.

        - **afterCommitId** *(string) --*

          he full commit ID of the commit that was the tip of the source branch at the time the
          comment was made.

        - **beforeBlobId** *(string) --*

          The full blob ID of the file on which you want to comment on the destination commit.

        - **afterBlobId** *(string) --*

          The full blob ID of the file on which you want to comment on the source commit.

        - **location** *(dict) --*

          Location information about the comment on the pull request, including the file name, line
          number, and whether the version of the file where the comment was made is 'BEFORE'
          (destination branch) or 'AFTER' (source branch).

          - **filePath** *(string) --*

            The name of the file being compared, including its extension and subdirectory, if any.

          - **filePosition** *(integer) --*

            The position of a change within a compared file, in line number format.

          - **relativeFileVersion** *(string) --*

            In a comparison of commits or a pull request, whether the change is in the 'before' or
            'after' of that comparison.

        - **comments** *(list) --*

          An array of comment objects. Each comment object contains information about a comment on
          the pull request.

          - *(dict) --*

            Returns information about a specific comment.

            - **commentId** *(string) --*

              The system-generated comment ID.

            - **content** *(string) --*

              The content of the comment.

            - **inReplyTo** *(string) --*

              The ID of the comment for which this comment is a reply, if any.

            - **creationDate** *(datetime) --*

              The date and time the comment was created, in timestamp format.

            - **lastModifiedDate** *(datetime) --*

              The date and time the comment was most recently modified, in timestamp format.

            - **authorArn** *(string) --*

              The Amazon Resource Name (ARN) of the person who posted the comment.

            - **deleted** *(boolean) --*

              A Boolean value indicating whether the comment has been deleted.

            - **clientRequestToken** *(string) --*

              A unique, client-generated idempotency token that when provided in a request, ensures
              the request cannot be repeated with a changed parameter. If a request is received
              with the same parameters and a token is included, the request will return information
              about the initial request that used that token.

    - **nextToken** *(string) --*

      An enumeration token that can be used in a request to return the next batch of the results.
    """


_ClientGetCommitResponsecommitauthorTypeDef = TypedDict(
    "_ClientGetCommitResponsecommitauthorTypeDef",
    {"name": str, "email": str, "date": str},
    total=False,
)


class ClientGetCommitResponsecommitauthorTypeDef(
    _ClientGetCommitResponsecommitauthorTypeDef
):
    """
    Type definition for `ClientGetCommitResponsecommit` `author`

    Information about the author of the specified commit. Information includes the date in
    timestamp format with GMT offset, the name of the author, and the email address for the
    author, as configured in Git.

    - **name** *(string) --*

      The name of the user who made the specified commit.

    - **email** *(string) --*

      The email address associated with the user who made the commit, if any.

    - **date** *(string) --*

      The date when the specified commit was commited, in timestamp format with GMT offset.
    """


_ClientGetCommitResponsecommitcommitterTypeDef = TypedDict(
    "_ClientGetCommitResponsecommitcommitterTypeDef",
    {"name": str, "email": str, "date": str},
    total=False,
)


class ClientGetCommitResponsecommitcommitterTypeDef(
    _ClientGetCommitResponsecommitcommitterTypeDef
):
    """
    Type definition for `ClientGetCommitResponsecommit` `committer`

    Information about the person who committed the specified commit, also known as the
    committer. Information includes the date in timestamp format with GMT offset, the name of
    the committer, and the email address for the committer, as configured in Git.

    For more information about the difference between an author and a committer in Git, see
    `Viewing the Commit History <http://git-scm.com/book/ch2-3.html>`__ in Pro Git by Scott
    Chacon and Ben Straub.

    - **name** *(string) --*

      The name of the user who made the specified commit.

    - **email** *(string) --*

      The email address associated with the user who made the commit, if any.

    - **date** *(string) --*

      The date when the specified commit was commited, in timestamp format with GMT offset.
    """


_ClientGetCommitResponsecommitTypeDef = TypedDict(
    "_ClientGetCommitResponsecommitTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "parents": List[str],
        "message": str,
        "author": ClientGetCommitResponsecommitauthorTypeDef,
        "committer": ClientGetCommitResponsecommitcommitterTypeDef,
        "additionalData": str,
    },
    total=False,
)


class ClientGetCommitResponsecommitTypeDef(_ClientGetCommitResponsecommitTypeDef):
    """
    Type definition for `ClientGetCommitResponse` `commit`

    A commit data type object that contains information about the specified commit.

    - **commitId** *(string) --*

      The full SHA of the specified commit.

    - **treeId** *(string) --*

      Tree information for the specified commit.

    - **parents** *(list) --*

      A list of parent commits for the specified commit. Each parent commit ID is the full commit
      ID.

      - *(string) --*

    - **message** *(string) --*

      The commit message associated with the specified commit.

    - **author** *(dict) --*

      Information about the author of the specified commit. Information includes the date in
      timestamp format with GMT offset, the name of the author, and the email address for the
      author, as configured in Git.

      - **name** *(string) --*

        The name of the user who made the specified commit.

      - **email** *(string) --*

        The email address associated with the user who made the commit, if any.

      - **date** *(string) --*

        The date when the specified commit was commited, in timestamp format with GMT offset.

    - **committer** *(dict) --*

      Information about the person who committed the specified commit, also known as the
      committer. Information includes the date in timestamp format with GMT offset, the name of
      the committer, and the email address for the committer, as configured in Git.

      For more information about the difference between an author and a committer in Git, see
      `Viewing the Commit History <http://git-scm.com/book/ch2-3.html>`__ in Pro Git by Scott
      Chacon and Ben Straub.

      - **name** *(string) --*

        The name of the user who made the specified commit.

      - **email** *(string) --*

        The email address associated with the user who made the commit, if any.

      - **date** *(string) --*

        The date when the specified commit was commited, in timestamp format with GMT offset.

    - **additionalData** *(string) --*

      Any additional data associated with the specified commit.
    """


_ClientGetCommitResponseTypeDef = TypedDict(
    "_ClientGetCommitResponseTypeDef",
    {"commit": ClientGetCommitResponsecommitTypeDef},
    total=False,
)


class ClientGetCommitResponseTypeDef(_ClientGetCommitResponseTypeDef):
    """
    Type definition for `ClientGetCommit` `Response`

    Represents the output of a get commit operation.

    - **commit** *(dict) --*

      A commit data type object that contains information about the specified commit.

      - **commitId** *(string) --*

        The full SHA of the specified commit.

      - **treeId** *(string) --*

        Tree information for the specified commit.

      - **parents** *(list) --*

        A list of parent commits for the specified commit. Each parent commit ID is the full commit
        ID.

        - *(string) --*

      - **message** *(string) --*

        The commit message associated with the specified commit.

      - **author** *(dict) --*

        Information about the author of the specified commit. Information includes the date in
        timestamp format with GMT offset, the name of the author, and the email address for the
        author, as configured in Git.

        - **name** *(string) --*

          The name of the user who made the specified commit.

        - **email** *(string) --*

          The email address associated with the user who made the commit, if any.

        - **date** *(string) --*

          The date when the specified commit was commited, in timestamp format with GMT offset.

      - **committer** *(dict) --*

        Information about the person who committed the specified commit, also known as the
        committer. Information includes the date in timestamp format with GMT offset, the name of
        the committer, and the email address for the committer, as configured in Git.

        For more information about the difference between an author and a committer in Git, see
        `Viewing the Commit History <http://git-scm.com/book/ch2-3.html>`__ in Pro Git by Scott
        Chacon and Ben Straub.

        - **name** *(string) --*

          The name of the user who made the specified commit.

        - **email** *(string) --*

          The email address associated with the user who made the commit, if any.

        - **date** *(string) --*

          The date when the specified commit was commited, in timestamp format with GMT offset.

      - **additionalData** *(string) --*

        Any additional data associated with the specified commit.
    """


_ClientGetDifferencesResponsedifferencesafterBlobTypeDef = TypedDict(
    "_ClientGetDifferencesResponsedifferencesafterBlobTypeDef",
    {"blobId": str, "path": str, "mode": str},
    total=False,
)


class ClientGetDifferencesResponsedifferencesafterBlobTypeDef(
    _ClientGetDifferencesResponsedifferencesafterBlobTypeDef
):
    """
    Type definition for `ClientGetDifferencesResponsedifferences` `afterBlob`

    Information about an ``afterBlob`` data type object, including the ID, the file mode
    permission code, and the path.

    - **blobId** *(string) --*

      The full ID of the blob.

    - **path** *(string) --*

      The path to the blob and any associated file name, if any.

    - **mode** *(string) --*

      The file mode permissions of the blob. File mode permission codes include:

      * ``100644`` indicates read/write

      * ``100755`` indicates read/write/execute

      * ``160000`` indicates a submodule

      * ``120000`` indicates a symlink
    """


_ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef = TypedDict(
    "_ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef",
    {"blobId": str, "path": str, "mode": str},
    total=False,
)


class ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef(
    _ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef
):
    """
    Type definition for `ClientGetDifferencesResponsedifferences` `beforeBlob`

    Information about a ``beforeBlob`` data type object, including the ID, the file mode
    permission code, and the path.

    - **blobId** *(string) --*

      The full ID of the blob.

    - **path** *(string) --*

      The path to the blob and any associated file name, if any.

    - **mode** *(string) --*

      The file mode permissions of the blob. File mode permission codes include:

      * ``100644`` indicates read/write

      * ``100755`` indicates read/write/execute

      * ``160000`` indicates a submodule

      * ``120000`` indicates a symlink
    """


_ClientGetDifferencesResponsedifferencesTypeDef = TypedDict(
    "_ClientGetDifferencesResponsedifferencesTypeDef",
    {
        "beforeBlob": ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef,
        "afterBlob": ClientGetDifferencesResponsedifferencesafterBlobTypeDef,
        "changeType": str,
    },
    total=False,
)


class ClientGetDifferencesResponsedifferencesTypeDef(
    _ClientGetDifferencesResponsedifferencesTypeDef
):
    """
    Type definition for `ClientGetDifferencesResponse` `differences`

    Returns information about a set of differences for a commit specifier.

    - **beforeBlob** *(dict) --*

      Information about a ``beforeBlob`` data type object, including the ID, the file mode
      permission code, and the path.

      - **blobId** *(string) --*

        The full ID of the blob.

      - **path** *(string) --*

        The path to the blob and any associated file name, if any.

      - **mode** *(string) --*

        The file mode permissions of the blob. File mode permission codes include:

        * ``100644`` indicates read/write

        * ``100755`` indicates read/write/execute

        * ``160000`` indicates a submodule

        * ``120000`` indicates a symlink

    - **afterBlob** *(dict) --*

      Information about an ``afterBlob`` data type object, including the ID, the file mode
      permission code, and the path.

      - **blobId** *(string) --*

        The full ID of the blob.

      - **path** *(string) --*

        The path to the blob and any associated file name, if any.

      - **mode** *(string) --*

        The file mode permissions of the blob. File mode permission codes include:

        * ``100644`` indicates read/write

        * ``100755`` indicates read/write/execute

        * ``160000`` indicates a submodule

        * ``120000`` indicates a symlink

    - **changeType** *(string) --*

      Whether the change type of the difference is an addition (A), deletion (D), or
      modification (M).
    """


_ClientGetDifferencesResponseTypeDef = TypedDict(
    "_ClientGetDifferencesResponseTypeDef",
    {
        "differences": List[ClientGetDifferencesResponsedifferencesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientGetDifferencesResponseTypeDef(_ClientGetDifferencesResponseTypeDef):
    """
    Type definition for `ClientGetDifferences` `Response`

    - **differences** *(list) --*

      A differences data type object that contains information about the differences, including
      whether the difference is added, modified, or deleted (A, D, M).

      - *(dict) --*

        Returns information about a set of differences for a commit specifier.

        - **beforeBlob** *(dict) --*

          Information about a ``beforeBlob`` data type object, including the ID, the file mode
          permission code, and the path.

          - **blobId** *(string) --*

            The full ID of the blob.

          - **path** *(string) --*

            The path to the blob and any associated file name, if any.

          - **mode** *(string) --*

            The file mode permissions of the blob. File mode permission codes include:

            * ``100644`` indicates read/write

            * ``100755`` indicates read/write/execute

            * ``160000`` indicates a submodule

            * ``120000`` indicates a symlink

        - **afterBlob** *(dict) --*

          Information about an ``afterBlob`` data type object, including the ID, the file mode
          permission code, and the path.

          - **blobId** *(string) --*

            The full ID of the blob.

          - **path** *(string) --*

            The path to the blob and any associated file name, if any.

          - **mode** *(string) --*

            The file mode permissions of the blob. File mode permission codes include:

            * ``100644`` indicates read/write

            * ``100755`` indicates read/write/execute

            * ``160000`` indicates a submodule

            * ``120000`` indicates a symlink

        - **changeType** *(string) --*

          Whether the change type of the difference is an addition (A), deletion (D), or
          modification (M).

    - **NextToken** *(string) --*

      An enumeration token that can be used in a request to return the next batch of the results.
    """


_ClientGetFileResponseTypeDef = TypedDict(
    "_ClientGetFileResponseTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "filePath": str,
        "fileMode": str,
        "fileSize": int,
        "fileContent": bytes,
    },
    total=False,
)


class ClientGetFileResponseTypeDef(_ClientGetFileResponseTypeDef):
    """
    Type definition for `ClientGetFile` `Response`

    - **commitId** *(string) --*

      The full commit ID of the commit that contains the content returned by GetFile.

    - **blobId** *(string) --*

      The blob ID of the object that represents the file content.

    - **filePath** *(string) --*

      The fully qualified path to the specified file. This returns the name and extension of the
      file.

    - **fileMode** *(string) --*

      The extrapolated file mode permissions of the blob. Valid values include strings such as
      EXECUTABLE and not numeric values.

      .. note::

        The file mode permissions returned by this API are not the standard file mode permission
        values, such as 100644, but rather extrapolated values. See below for a full list of
        supported return values.

    - **fileSize** *(integer) --*

      The size of the contents of the file, in bytes.

    - **fileContent** *(bytes) --*

      The base-64 encoded binary data object that represents the content of the file.
    """


_ClientGetFolderResponsefilesTypeDef = TypedDict(
    "_ClientGetFolderResponsefilesTypeDef",
    {"blobId": str, "absolutePath": str, "relativePath": str, "fileMode": str},
    total=False,
)


class ClientGetFolderResponsefilesTypeDef(_ClientGetFolderResponsefilesTypeDef):
    """
    Type definition for `ClientGetFolderResponse` `files`

    Returns information about a file in a repository.

    - **blobId** *(string) --*

      The blob ID that contains the file information.

    - **absolutePath** *(string) --*

      The fully-qualified path to the file in the repository.

    - **relativePath** *(string) --*

      The relative path of the file from the folder where the query originated.

    - **fileMode** *(string) --*

      The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and
      NORMAL.
    """


_ClientGetFolderResponsesubFoldersTypeDef = TypedDict(
    "_ClientGetFolderResponsesubFoldersTypeDef",
    {"treeId": str, "absolutePath": str, "relativePath": str},
    total=False,
)


class ClientGetFolderResponsesubFoldersTypeDef(
    _ClientGetFolderResponsesubFoldersTypeDef
):
    """
    Type definition for `ClientGetFolderResponse` `subFolders`

    Returns information about a folder in a repository.

    - **treeId** *(string) --*

      The full SHA-1 pointer of the tree information for the commit that contains the folder.

    - **absolutePath** *(string) --*

      The fully-qualified path of the folder in the repository.

    - **relativePath** *(string) --*

      The relative path of the specified folder from the folder where the query originated.
    """


_ClientGetFolderResponsesubModulesTypeDef = TypedDict(
    "_ClientGetFolderResponsesubModulesTypeDef",
    {"commitId": str, "absolutePath": str, "relativePath": str},
    total=False,
)


class ClientGetFolderResponsesubModulesTypeDef(
    _ClientGetFolderResponsesubModulesTypeDef
):
    """
    Type definition for `ClientGetFolderResponse` `subModules`

    Returns information about a submodule reference in a repository folder.

    - **commitId** *(string) --*

      The commit ID that contains the reference to the submodule.

    - **absolutePath** *(string) --*

      The fully qualified path to the folder that contains the reference to the submodule.

    - **relativePath** *(string) --*

      The relative path of the submodule from the folder where the query originated.
    """


_ClientGetFolderResponsesymbolicLinksTypeDef = TypedDict(
    "_ClientGetFolderResponsesymbolicLinksTypeDef",
    {"blobId": str, "absolutePath": str, "relativePath": str, "fileMode": str},
    total=False,
)


class ClientGetFolderResponsesymbolicLinksTypeDef(
    _ClientGetFolderResponsesymbolicLinksTypeDef
):
    """
    Type definition for `ClientGetFolderResponse` `symbolicLinks`

    Returns information about a symbolic link in a repository folder.

    - **blobId** *(string) --*

      The blob ID that contains the information about the symbolic link.

    - **absolutePath** *(string) --*

      The fully-qualified path to the folder that contains the symbolic link.

    - **relativePath** *(string) --*

      The relative path of the symbolic link from the folder where the query originated.

    - **fileMode** *(string) --*

      The file mode permissions of the blob that cotains information about the symbolic link.
    """


_ClientGetFolderResponseTypeDef = TypedDict(
    "_ClientGetFolderResponseTypeDef",
    {
        "commitId": str,
        "folderPath": str,
        "treeId": str,
        "subFolders": List[ClientGetFolderResponsesubFoldersTypeDef],
        "files": List[ClientGetFolderResponsefilesTypeDef],
        "symbolicLinks": List[ClientGetFolderResponsesymbolicLinksTypeDef],
        "subModules": List[ClientGetFolderResponsesubModulesTypeDef],
    },
    total=False,
)


class ClientGetFolderResponseTypeDef(_ClientGetFolderResponseTypeDef):
    """
    Type definition for `ClientGetFolder` `Response`

    - **commitId** *(string) --*

      The full commit ID used as a reference for which version of the folder content is returned.

    - **folderPath** *(string) --*

      The fully-qualified path of the folder whose contents are returned.

    - **treeId** *(string) --*

      The full SHA-1 pointer of the tree information for the commit that contains the folder.

    - **subFolders** *(list) --*

      The list of folders that exist beneath the specified folder, if any.

      - *(dict) --*

        Returns information about a folder in a repository.

        - **treeId** *(string) --*

          The full SHA-1 pointer of the tree information for the commit that contains the folder.

        - **absolutePath** *(string) --*

          The fully-qualified path of the folder in the repository.

        - **relativePath** *(string) --*

          The relative path of the specified folder from the folder where the query originated.

    - **files** *(list) --*

      The list of files that exist in the specified folder, if any.

      - *(dict) --*

        Returns information about a file in a repository.

        - **blobId** *(string) --*

          The blob ID that contains the file information.

        - **absolutePath** *(string) --*

          The fully-qualified path to the file in the repository.

        - **relativePath** *(string) --*

          The relative path of the file from the folder where the query originated.

        - **fileMode** *(string) --*

          The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and
          NORMAL.

    - **symbolicLinks** *(list) --*

      The list of symbolic links to other files and folders that exist in the specified folder, if
      any.

      - *(dict) --*

        Returns information about a symbolic link in a repository folder.

        - **blobId** *(string) --*

          The blob ID that contains the information about the symbolic link.

        - **absolutePath** *(string) --*

          The fully-qualified path to the folder that contains the symbolic link.

        - **relativePath** *(string) --*

          The relative path of the symbolic link from the folder where the query originated.

        - **fileMode** *(string) --*

          The file mode permissions of the blob that cotains information about the symbolic link.

    - **subModules** *(list) --*

      The list of submodules that exist in the specified folder, if any.

      - *(dict) --*

        Returns information about a submodule reference in a repository folder.

        - **commitId** *(string) --*

          The commit ID that contains the reference to the submodule.

        - **absolutePath** *(string) --*

          The fully qualified path to the folder that contains the reference to the submodule.

        - **relativePath** *(string) --*

          The relative path of the submodule from the folder where the query originated.
    """


_ClientGetMergeCommitResponseTypeDef = TypedDict(
    "_ClientGetMergeCommitResponseTypeDef",
    {
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
        "mergedCommitId": str,
    },
    total=False,
)


class ClientGetMergeCommitResponseTypeDef(_ClientGetMergeCommitResponseTypeDef):
    """
    Type definition for `ClientGetMergeCommit` `Response`

    - **sourceCommitId** *(string) --*

      The commit ID of the source commit specifier that was used in the merge evaluation.

    - **destinationCommitId** *(string) --*

      The commit ID of the destination commit specifier that was used in the merge evaluation.

    - **baseCommitId** *(string) --*

      The commit ID of the merge base.

    - **mergedCommitId** *(string) --*

      The commit ID for the merge commit created when the source branch was merged into the
      destination branch. If the fast-forward merge strategy was used, no merge commit exists.
    """


_ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef",
    {"source": str, "destination": str, "base": str},
    total=False,
)


class ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef(
    _ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef
):
    """
    Type definition for `ClientGetMergeConflictsResponseconflictMetadataList` `fileModes`

    The file modes of the file in the source, destination, and base of the merge.

    - **source** *(string) --*

      The file mode of a file in the source of a merge or pull request.

    - **destination** *(string) --*

      The file mode of a file in the destination of a merge or pull request.

    - **base** *(string) --*

      The file mode of a file in the base of a merge or pull request.
    """


_ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef",
    {"source": int, "destination": int, "base": int},
    total=False,
)


class ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef(
    _ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef
):
    """
    Type definition for `ClientGetMergeConflictsResponseconflictMetadataList` `fileSizes`

    The file sizes of the file in the source, destination, and base of the merge.

    - **source** *(integer) --*

      The size of a file in the source of a merge or pull request.

    - **destination** *(integer) --*

      The size of a file in the destination of a merge or pull request.

    - **base** *(integer) --*

      The size of a file in the base of a merge or pull request.
    """


_ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef",
    {"source": bool, "destination": bool, "base": bool},
    total=False,
)


class ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef(
    _ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef
):
    """
    Type definition for `ClientGetMergeConflictsResponseconflictMetadataList` `isBinaryFile`

    A boolean value (true or false) indicating whether the file is binary or textual in the
    source, destination, and base of the merge.

    - **source** *(boolean) --*

      The binary or non-binary status of file in the source of a merge or pull request.

    - **destination** *(boolean) --*

      The binary or non-binary status of a file in the destination of a merge or pull request.

    - **base** *(boolean) --*

      The binary or non-binary status of a file in the base of a merge or pull request.
    """


_ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef",
    {"source": str, "destination": str},
    total=False,
)


class ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef(
    _ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef
):
    """
    Type definition for `ClientGetMergeConflictsResponseconflictMetadataList` `mergeOperations`

    Whether an add, modify, or delete operation caused the conflict between the source and
    destination of the merge.

    - **source** *(string) --*

      The operation on a file (add, modify, or delete) of a file in the source of a merge or
      pull request.

    - **destination** *(string) --*

      The operation on a file in the destination of a merge or pull request.
    """


_ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef",
    {"source": str, "destination": str, "base": str},
    total=False,
)


class ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef(
    _ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef
):
    """
    Type definition for `ClientGetMergeConflictsResponseconflictMetadataList` `objectTypes`

    Information about any object type conflicts in a merge operation.

    - **source** *(string) --*

      The type of the object in the source branch.

    - **destination** *(string) --*

      The type of the object in the destination branch.

    - **base** *(string) --*

      The type of the object in the base commit of the merge.
    """


_ClientGetMergeConflictsResponseconflictMetadataListTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseconflictMetadataListTypeDef",
    {
        "filePath": str,
        "fileSizes": ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef,
        "fileModes": ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef,
        "objectTypes": ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef,
        "numberOfConflicts": int,
        "isBinaryFile": ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef,
        "contentConflict": bool,
        "fileModeConflict": bool,
        "objectTypeConflict": bool,
        "mergeOperations": ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef,
    },
    total=False,
)


class ClientGetMergeConflictsResponseconflictMetadataListTypeDef(
    _ClientGetMergeConflictsResponseconflictMetadataListTypeDef
):
    """
    Type definition for `ClientGetMergeConflictsResponse` `conflictMetadataList`

    Information about the metadata for a conflict in a merge operation.

    - **filePath** *(string) --*

      The path of the file that contains conflicts.

    - **fileSizes** *(dict) --*

      The file sizes of the file in the source, destination, and base of the merge.

      - **source** *(integer) --*

        The size of a file in the source of a merge or pull request.

      - **destination** *(integer) --*

        The size of a file in the destination of a merge or pull request.

      - **base** *(integer) --*

        The size of a file in the base of a merge or pull request.

    - **fileModes** *(dict) --*

      The file modes of the file in the source, destination, and base of the merge.

      - **source** *(string) --*

        The file mode of a file in the source of a merge or pull request.

      - **destination** *(string) --*

        The file mode of a file in the destination of a merge or pull request.

      - **base** *(string) --*

        The file mode of a file in the base of a merge or pull request.

    - **objectTypes** *(dict) --*

      Information about any object type conflicts in a merge operation.

      - **source** *(string) --*

        The type of the object in the source branch.

      - **destination** *(string) --*

        The type of the object in the destination branch.

      - **base** *(string) --*

        The type of the object in the base commit of the merge.

    - **numberOfConflicts** *(integer) --*

      The number of conflicts, including both hunk conflicts and metadata conflicts.

    - **isBinaryFile** *(dict) --*

      A boolean value (true or false) indicating whether the file is binary or textual in the
      source, destination, and base of the merge.

      - **source** *(boolean) --*

        The binary or non-binary status of file in the source of a merge or pull request.

      - **destination** *(boolean) --*

        The binary or non-binary status of a file in the destination of a merge or pull request.

      - **base** *(boolean) --*

        The binary or non-binary status of a file in the base of a merge or pull request.

    - **contentConflict** *(boolean) --*

      A boolean value indicating whether there are conflicts in the content of a file.

    - **fileModeConflict** *(boolean) --*

      A boolean value indicating whether there are conflicts in the file mode of a file.

    - **objectTypeConflict** *(boolean) --*

      A boolean value (true or false) indicating whether there are conflicts between the
      branches in the object type of a file, folder, or submodule.

    - **mergeOperations** *(dict) --*

      Whether an add, modify, or delete operation caused the conflict between the source and
      destination of the merge.

      - **source** *(string) --*

        The operation on a file (add, modify, or delete) of a file in the source of a merge or
        pull request.

      - **destination** *(string) --*

        The operation on a file in the destination of a merge or pull request.
    """


_ClientGetMergeConflictsResponseTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseTypeDef",
    {
        "mergeable": bool,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "conflictMetadataList": List[
            ClientGetMergeConflictsResponseconflictMetadataListTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetMergeConflictsResponseTypeDef(_ClientGetMergeConflictsResponseTypeDef):
    """
    Type definition for `ClientGetMergeConflicts` `Response`

    - **mergeable** *(boolean) --*

      A Boolean value that indicates whether the code is mergeable by the specified merge option.

    - **destinationCommitId** *(string) --*

      The commit ID of the destination commit specifier that was used in the merge evaluation.

    - **sourceCommitId** *(string) --*

      The commit ID of the source commit specifier that was used in the merge evaluation.

    - **baseCommitId** *(string) --*

      The commit ID of the merge base.

    - **conflictMetadataList** *(list) --*

      A list of metadata for any conflicting files. If the specified merge strategy is
      FAST_FORWARD_MERGE, this list will always be empty.

      - *(dict) --*

        Information about the metadata for a conflict in a merge operation.

        - **filePath** *(string) --*

          The path of the file that contains conflicts.

        - **fileSizes** *(dict) --*

          The file sizes of the file in the source, destination, and base of the merge.

          - **source** *(integer) --*

            The size of a file in the source of a merge or pull request.

          - **destination** *(integer) --*

            The size of a file in the destination of a merge or pull request.

          - **base** *(integer) --*

            The size of a file in the base of a merge or pull request.

        - **fileModes** *(dict) --*

          The file modes of the file in the source, destination, and base of the merge.

          - **source** *(string) --*

            The file mode of a file in the source of a merge or pull request.

          - **destination** *(string) --*

            The file mode of a file in the destination of a merge or pull request.

          - **base** *(string) --*

            The file mode of a file in the base of a merge or pull request.

        - **objectTypes** *(dict) --*

          Information about any object type conflicts in a merge operation.

          - **source** *(string) --*

            The type of the object in the source branch.

          - **destination** *(string) --*

            The type of the object in the destination branch.

          - **base** *(string) --*

            The type of the object in the base commit of the merge.

        - **numberOfConflicts** *(integer) --*

          The number of conflicts, including both hunk conflicts and metadata conflicts.

        - **isBinaryFile** *(dict) --*

          A boolean value (true or false) indicating whether the file is binary or textual in the
          source, destination, and base of the merge.

          - **source** *(boolean) --*

            The binary or non-binary status of file in the source of a merge or pull request.

          - **destination** *(boolean) --*

            The binary or non-binary status of a file in the destination of a merge or pull request.

          - **base** *(boolean) --*

            The binary or non-binary status of a file in the base of a merge or pull request.

        - **contentConflict** *(boolean) --*

          A boolean value indicating whether there are conflicts in the content of a file.

        - **fileModeConflict** *(boolean) --*

          A boolean value indicating whether there are conflicts in the file mode of a file.

        - **objectTypeConflict** *(boolean) --*

          A boolean value (true or false) indicating whether there are conflicts between the
          branches in the object type of a file, folder, or submodule.

        - **mergeOperations** *(dict) --*

          Whether an add, modify, or delete operation caused the conflict between the source and
          destination of the merge.

          - **source** *(string) --*

            The operation on a file (add, modify, or delete) of a file in the source of a merge or
            pull request.

          - **destination** *(string) --*

            The operation on a file in the destination of a merge or pull request.

    - **nextToken** *(string) --*

      An enumeration token that can be used in a request to return the next batch of the results.
    """


_ClientGetMergeOptionsResponseTypeDef = TypedDict(
    "_ClientGetMergeOptionsResponseTypeDef",
    {
        "mergeOptions": List[str],
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
    },
    total=False,
)


class ClientGetMergeOptionsResponseTypeDef(_ClientGetMergeOptionsResponseTypeDef):
    """
    Type definition for `ClientGetMergeOptions` `Response`

    - **mergeOptions** *(list) --*

      The merge option or strategy used to merge the code.

      - *(string) --*

    - **sourceCommitId** *(string) --*

      The commit ID of the source commit specifier that was used in the merge evaluation.

    - **destinationCommitId** *(string) --*

      The commit ID of the destination commit specifier that was used in the merge evaluation.

    - **baseCommitId** *(string) --*

      The commit ID of the merge base.
    """


_ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {"isMerged": bool, "mergedBy": str, "mergeCommitId": str, "mergeOption": str},
    total=False,
)


class ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    """
    Type definition for `ClientGetPullRequestResponsepullRequestpullRequestTargets` `mergeMetadata`

    Returns metadata about the state of the merge, including whether the merge has been
    made.

    - **isMerged** *(boolean) --*

      A Boolean value indicating whether the merge has been made.

    - **mergedBy** *(string) --*

      The Amazon Resource Name (ARN) of the user who merged the branches.

    - **mergeCommitId** *(string) --*

      The commit ID for the merge commit, if any.

    - **mergeOption** *(string) --*

      The merge strategy used in the merge.
    """


_ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef(
    _ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef
):
    """
    Type definition for `ClientGetPullRequestResponsepullRequest` `pullRequestTargets`

    Returns information about a pull request target.

    - **repositoryName** *(string) --*

      The name of the repository that contains the pull request source and destination
      branches.

    - **sourceReference** *(string) --*

      The branch of the repository that contains the changes for the pull request. Also known
      as the source branch.

    - **destinationReference** *(string) --*

      The branch of the repository where the pull request changes will be merged into. Also
      known as the destination branch.

    - **destinationCommit** *(string) --*

      The full commit ID that is the tip of the destination branch. This is the commit where
      the pull request was or will be merged.

    - **sourceCommit** *(string) --*

      The full commit ID of the tip of the source branch used to create the pull request. If
      the pull request branch is updated by a push while the pull request is open, the commit
      ID will change to reflect the new tip of the branch.

    - **mergeBase** *(string) --*

      The commit ID of the most recent commit that the source branch and the destination
      branch have in common.

    - **mergeMetadata** *(dict) --*

      Returns metadata about the state of the merge, including whether the merge has been
      made.

      - **isMerged** *(boolean) --*

        A Boolean value indicating whether the merge has been made.

      - **mergedBy** *(string) --*

        The Amazon Resource Name (ARN) of the user who merged the branches.

      - **mergeCommitId** *(string) --*

        The commit ID for the merge commit, if any.

      - **mergeOption** *(string) --*

        The merge strategy used in the merge.
    """


_ClientGetPullRequestResponsepullRequestTypeDef = TypedDict(
    "_ClientGetPullRequestResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": str,
        "authorArn": str,
        "pullRequestTargets": List[
            ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
    },
    total=False,
)


class ClientGetPullRequestResponsepullRequestTypeDef(
    _ClientGetPullRequestResponsepullRequestTypeDef
):
    """
    Type definition for `ClientGetPullRequestResponse` `pullRequest`

    Information about the specified pull request.

    - **pullRequestId** *(string) --*

      The system-generated ID of the pull request.

    - **title** *(string) --*

      The user-defined title of the pull request. This title is displayed in the list of pull
      requests to other users of the repository.

    - **description** *(string) --*

      The user-defined description of the pull request. This description can be used to clarify
      what should be reviewed and other details of the request.

    - **lastActivityDate** *(datetime) --*

      The day and time of the last user or system activity on the pull request, in timestamp
      format.

    - **creationDate** *(datetime) --*

      The date and time the pull request was originally created, in timestamp format.

    - **pullRequestStatus** *(string) --*

      The status of the pull request. Pull request status can only change from ``OPEN`` to
      ``CLOSED`` .

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the user who created the pull request.

    - **pullRequestTargets** *(list) --*

      The targets of the pull request, including the source branch and destination branch for the
      pull request.

      - *(dict) --*

        Returns information about a pull request target.

        - **repositoryName** *(string) --*

          The name of the repository that contains the pull request source and destination
          branches.

        - **sourceReference** *(string) --*

          The branch of the repository that contains the changes for the pull request. Also known
          as the source branch.

        - **destinationReference** *(string) --*

          The branch of the repository where the pull request changes will be merged into. Also
          known as the destination branch.

        - **destinationCommit** *(string) --*

          The full commit ID that is the tip of the destination branch. This is the commit where
          the pull request was or will be merged.

        - **sourceCommit** *(string) --*

          The full commit ID of the tip of the source branch used to create the pull request. If
          the pull request branch is updated by a push while the pull request is open, the commit
          ID will change to reflect the new tip of the branch.

        - **mergeBase** *(string) --*

          The commit ID of the most recent commit that the source branch and the destination
          branch have in common.

        - **mergeMetadata** *(dict) --*

          Returns metadata about the state of the merge, including whether the merge has been
          made.

          - **isMerged** *(boolean) --*

            A Boolean value indicating whether the merge has been made.

          - **mergedBy** *(string) --*

            The Amazon Resource Name (ARN) of the user who merged the branches.

          - **mergeCommitId** *(string) --*

            The commit ID for the merge commit, if any.

          - **mergeOption** *(string) --*

            The merge strategy used in the merge.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientGetPullRequestResponseTypeDef = TypedDict(
    "_ClientGetPullRequestResponseTypeDef",
    {"pullRequest": ClientGetPullRequestResponsepullRequestTypeDef},
    total=False,
)


class ClientGetPullRequestResponseTypeDef(_ClientGetPullRequestResponseTypeDef):
    """
    Type definition for `ClientGetPullRequest` `Response`

    - **pullRequest** *(dict) --*

      Information about the specified pull request.

      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.

      - **title** *(string) --*

        The user-defined title of the pull request. This title is displayed in the list of pull
        requests to other users of the repository.

      - **description** *(string) --*

        The user-defined description of the pull request. This description can be used to clarify
        what should be reviewed and other details of the request.

      - **lastActivityDate** *(datetime) --*

        The day and time of the last user or system activity on the pull request, in timestamp
        format.

      - **creationDate** *(datetime) --*

        The date and time the pull request was originally created, in timestamp format.

      - **pullRequestStatus** *(string) --*

        The status of the pull request. Pull request status can only change from ``OPEN`` to
        ``CLOSED`` .

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the user who created the pull request.

      - **pullRequestTargets** *(list) --*

        The targets of the pull request, including the source branch and destination branch for the
        pull request.

        - *(dict) --*

          Returns information about a pull request target.

          - **repositoryName** *(string) --*

            The name of the repository that contains the pull request source and destination
            branches.

          - **sourceReference** *(string) --*

            The branch of the repository that contains the changes for the pull request. Also known
            as the source branch.

          - **destinationReference** *(string) --*

            The branch of the repository where the pull request changes will be merged into. Also
            known as the destination branch.

          - **destinationCommit** *(string) --*

            The full commit ID that is the tip of the destination branch. This is the commit where
            the pull request was or will be merged.

          - **sourceCommit** *(string) --*

            The full commit ID of the tip of the source branch used to create the pull request. If
            the pull request branch is updated by a push while the pull request is open, the commit
            ID will change to reflect the new tip of the branch.

          - **mergeBase** *(string) --*

            The commit ID of the most recent commit that the source branch and the destination
            branch have in common.

          - **mergeMetadata** *(dict) --*

            Returns metadata about the state of the merge, including whether the merge has been
            made.

            - **isMerged** *(boolean) --*

              A Boolean value indicating whether the merge has been made.

            - **mergedBy** *(string) --*

              The Amazon Resource Name (ARN) of the user who merged the branches.

            - **mergeCommitId** *(string) --*

              The commit ID for the merge commit, if any.

            - **mergeOption** *(string) --*

              The merge strategy used in the merge.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_ClientGetRepositoryResponserepositoryMetadataTypeDef = TypedDict(
    "_ClientGetRepositoryResponserepositoryMetadataTypeDef",
    {
        "accountId": str,
        "repositoryId": str,
        "repositoryName": str,
        "repositoryDescription": str,
        "defaultBranch": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "cloneUrlHttp": str,
        "cloneUrlSsh": str,
        "Arn": str,
    },
    total=False,
)


class ClientGetRepositoryResponserepositoryMetadataTypeDef(
    _ClientGetRepositoryResponserepositoryMetadataTypeDef
):
    """
    Type definition for `ClientGetRepositoryResponse` `repositoryMetadata`

    Information about the repository.

    - **accountId** *(string) --*

      The ID of the AWS account associated with the repository.

    - **repositoryId** *(string) --*

      The ID of the repository.

    - **repositoryName** *(string) --*

      The repository's name.

    - **repositoryDescription** *(string) --*

      A comment or description about the repository.

    - **defaultBranch** *(string) --*

      The repository's default branch name.

    - **lastModifiedDate** *(datetime) --*

      The date and time the repository was last modified, in timestamp format.

    - **creationDate** *(datetime) --*

      The date and time the repository was created, in timestamp format.

    - **cloneUrlHttp** *(string) --*

      The URL to use for cloning the repository over HTTPS.

    - **cloneUrlSsh** *(string) --*

      The URL to use for cloning the repository over SSH.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the repository.
    """


_ClientGetRepositoryResponseTypeDef = TypedDict(
    "_ClientGetRepositoryResponseTypeDef",
    {"repositoryMetadata": ClientGetRepositoryResponserepositoryMetadataTypeDef},
    total=False,
)


class ClientGetRepositoryResponseTypeDef(_ClientGetRepositoryResponseTypeDef):
    """
    Type definition for `ClientGetRepository` `Response`

    Represents the output of a get repository operation.

    - **repositoryMetadata** *(dict) --*

      Information about the repository.

      - **accountId** *(string) --*

        The ID of the AWS account associated with the repository.

      - **repositoryId** *(string) --*

        The ID of the repository.

      - **repositoryName** *(string) --*

        The repository's name.

      - **repositoryDescription** *(string) --*

        A comment or description about the repository.

      - **defaultBranch** *(string) --*

        The repository's default branch name.

      - **lastModifiedDate** *(datetime) --*

        The date and time the repository was last modified, in timestamp format.

      - **creationDate** *(datetime) --*

        The date and time the repository was created, in timestamp format.

      - **cloneUrlHttp** *(string) --*

        The URL to use for cloning the repository over HTTPS.

      - **cloneUrlSsh** *(string) --*

        The URL to use for cloning the repository over SSH.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the repository.
    """


_ClientGetRepositoryTriggersResponsetriggersTypeDef = TypedDict(
    "_ClientGetRepositoryTriggersResponsetriggersTypeDef",
    {
        "name": str,
        "destinationArn": str,
        "customData": str,
        "branches": List[str],
        "events": List[str],
    },
    total=False,
)


class ClientGetRepositoryTriggersResponsetriggersTypeDef(
    _ClientGetRepositoryTriggersResponsetriggersTypeDef
):
    """
    Type definition for `ClientGetRepositoryTriggersResponse` `triggers`

    Information about a trigger for a repository.

    - **name** *(string) --*

      The name of the trigger.

    - **destinationArn** *(string) --*

      The ARN of the resource that is the target for a trigger. For example, the ARN of a topic
      in Amazon SNS.

    - **customData** *(string) --*

      Any custom data associated with the trigger that will be included in the information sent
      to the target of the trigger.

    - **branches** *(list) --*

      The branches that will be included in the trigger configuration. If you specify an empty
      array, the trigger will apply to all branches.

      .. note::

        Although no content is required in the array, you must include the array itself.

      - *(string) --*

    - **events** *(list) --*

      The repository events that will cause the trigger to run actions in another service, such
      as sending a notification through Amazon SNS.

      .. note::

        The valid value "all" cannot be used with any other values.

      - *(string) --*
    """


_ClientGetRepositoryTriggersResponseTypeDef = TypedDict(
    "_ClientGetRepositoryTriggersResponseTypeDef",
    {
        "configurationId": str,
        "triggers": List[ClientGetRepositoryTriggersResponsetriggersTypeDef],
    },
    total=False,
)


class ClientGetRepositoryTriggersResponseTypeDef(
    _ClientGetRepositoryTriggersResponseTypeDef
):
    """
    Type definition for `ClientGetRepositoryTriggers` `Response`

    Represents the output of a get repository triggers operation.

    - **configurationId** *(string) --*

      The system-generated unique ID for the trigger.

    - **triggers** *(list) --*

      The JSON block of configuration information for each trigger.

      - *(dict) --*

        Information about a trigger for a repository.

        - **name** *(string) --*

          The name of the trigger.

        - **destinationArn** *(string) --*

          The ARN of the resource that is the target for a trigger. For example, the ARN of a topic
          in Amazon SNS.

        - **customData** *(string) --*

          Any custom data associated with the trigger that will be included in the information sent
          to the target of the trigger.

        - **branches** *(list) --*

          The branches that will be included in the trigger configuration. If you specify an empty
          array, the trigger will apply to all branches.

          .. note::

            Although no content is required in the array, you must include the array itself.

          - *(string) --*

        - **events** *(list) --*

          The repository events that will cause the trigger to run actions in another service, such
          as sending a notification through Amazon SNS.

          .. note::

            The valid value "all" cannot be used with any other values.

          - *(string) --*
    """


_ClientListBranchesResponseTypeDef = TypedDict(
    "_ClientListBranchesResponseTypeDef",
    {"branches": List[str], "nextToken": str},
    total=False,
)


class ClientListBranchesResponseTypeDef(_ClientListBranchesResponseTypeDef):
    """
    Type definition for `ClientListBranches` `Response`

    Represents the output of a list branches operation.

    - **branches** *(list) --*

      The list of branch names.

      - *(string) --*

    - **nextToken** *(string) --*

      An enumeration token that returns the batch of the results.
    """


_ClientListPullRequestsResponseTypeDef = TypedDict(
    "_ClientListPullRequestsResponseTypeDef",
    {"pullRequestIds": List[str], "nextToken": str},
    total=False,
)


class ClientListPullRequestsResponseTypeDef(_ClientListPullRequestsResponseTypeDef):
    """
    Type definition for `ClientListPullRequests` `Response`

    - **pullRequestIds** *(list) --*

      The system-generated IDs of the pull requests.

      - *(string) --*

    - **nextToken** *(string) --*

      An enumeration token that when provided in a request, returns the next batch of the results.
    """


_ClientListRepositoriesResponserepositoriesTypeDef = TypedDict(
    "_ClientListRepositoriesResponserepositoriesTypeDef",
    {"repositoryName": str, "repositoryId": str},
    total=False,
)


class ClientListRepositoriesResponserepositoriesTypeDef(
    _ClientListRepositoriesResponserepositoriesTypeDef
):
    """
    Type definition for `ClientListRepositoriesResponse` `repositories`

    Information about a repository name and ID.

    - **repositoryName** *(string) --*

      The name associated with the repository.

    - **repositoryId** *(string) --*

      The ID associated with the repository.
    """


_ClientListRepositoriesResponseTypeDef = TypedDict(
    "_ClientListRepositoriesResponseTypeDef",
    {
        "repositories": List[ClientListRepositoriesResponserepositoriesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListRepositoriesResponseTypeDef(_ClientListRepositoriesResponseTypeDef):
    """
    Type definition for `ClientListRepositories` `Response`

    Represents the output of a list repositories operation.

    - **repositories** *(list) --*

      Lists the repositories called by the list repositories operation.

      - *(dict) --*

        Information about a repository name and ID.

        - **repositoryName** *(string) --*

          The name associated with the repository.

        - **repositoryId** *(string) --*

          The ID associated with the repository.

    - **nextToken** *(string) --*

      An enumeration token that allows the operation to batch the results of the operation. Batch
      sizes are 1,000 for list repository operations. When the client sends the token back to AWS
      CodeCommit, another page of 1,000 records is retrieved.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": Dict[str, str], "nextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(dict) --*

      A list of tag key and value pairs associated with the specified resource.

      - *(string) --*

        - *(string) --*

    - **nextToken** *(string) --*

      An enumeration token that allows the operation to batch the next results of the operation.
    """


_ClientMergeBranchesByFastForwardResponseTypeDef = TypedDict(
    "_ClientMergeBranchesByFastForwardResponseTypeDef",
    {"commitId": str, "treeId": str},
    total=False,
)


class ClientMergeBranchesByFastForwardResponseTypeDef(
    _ClientMergeBranchesByFastForwardResponseTypeDef
):
    """
    Type definition for `ClientMergeBranchesByFastForward` `Response`

    - **commitId** *(string) --*

      The commit ID of the merge in the destination or target branch.

    - **treeId** *(string) --*

      The tree ID of the merge in the destination or target branch.
    """


_ClientMergeBranchesBySquashResponseTypeDef = TypedDict(
    "_ClientMergeBranchesBySquashResponseTypeDef",
    {"commitId": str, "treeId": str},
    total=False,
)


class ClientMergeBranchesBySquashResponseTypeDef(
    _ClientMergeBranchesBySquashResponseTypeDef
):
    """
    Type definition for `ClientMergeBranchesBySquash` `Response`

    - **commitId** *(string) --*

      The commit ID of the merge in the destination or target branch.

    - **treeId** *(string) --*

      The tree ID of the merge in the destination or target branch.
    """


_ClientMergeBranchesBySquashconflictResolutiondeleteFilesTypeDef = TypedDict(
    "_ClientMergeBranchesBySquashconflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
)


class ClientMergeBranchesBySquashconflictResolutiondeleteFilesTypeDef(
    _ClientMergeBranchesBySquashconflictResolutiondeleteFilesTypeDef
):
    """
    Type definition for `ClientMergeBranchesBySquashconflictResolution` `deleteFiles`

    A file that will be deleted as part of a commit.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path of the file that will be deleted, including the name of the file.
    """


_RequiredClientMergeBranchesBySquashconflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientMergeBranchesBySquashconflictResolutionreplaceContentsTypeDef",
    {"filePath": str, "replacementType": str},
)
_OptionalClientMergeBranchesBySquashconflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientMergeBranchesBySquashconflictResolutionreplaceContentsTypeDef",
    {"content": bytes, "fileMode": str},
    total=False,
)


class ClientMergeBranchesBySquashconflictResolutionreplaceContentsTypeDef(
    _RequiredClientMergeBranchesBySquashconflictResolutionreplaceContentsTypeDef,
    _OptionalClientMergeBranchesBySquashconflictResolutionreplaceContentsTypeDef,
):
    """
    Type definition for `ClientMergeBranchesBySquashconflictResolution` `replaceContents`

    Information about a replacement content entry in the conflict of a merge or pull request
    operation.

    - **filePath** *(string) --* **[REQUIRED]**

      The path of the conflicting file.

    - **replacementType** *(string) --* **[REQUIRED]**

      The replacement type to use when determining how to resolve the conflict.

    - **content** *(bytes) --*

      The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

    - **fileMode** *(string) --*

      The file mode to apply during conflict resoltion.
    """


_ClientMergeBranchesBySquashconflictResolutionsetFileModesTypeDef = TypedDict(
    "_ClientMergeBranchesBySquashconflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": str},
)


class ClientMergeBranchesBySquashconflictResolutionsetFileModesTypeDef(
    _ClientMergeBranchesBySquashconflictResolutionsetFileModesTypeDef
):
    """
    Type definition for `ClientMergeBranchesBySquashconflictResolution` `setFileModes`

    Information about the file mode changes.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path to the file, including the name of the file.

    - **fileMode** *(string) --* **[REQUIRED]**

      The file mode for the file.
    """


_ClientMergeBranchesBySquashconflictResolutionTypeDef = TypedDict(
    "_ClientMergeBranchesBySquashconflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientMergeBranchesBySquashconflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[
            ClientMergeBranchesBySquashconflictResolutiondeleteFilesTypeDef
        ],
        "setFileModes": List[
            ClientMergeBranchesBySquashconflictResolutionsetFileModesTypeDef
        ],
    },
    total=False,
)


class ClientMergeBranchesBySquashconflictResolutionTypeDef(
    _ClientMergeBranchesBySquashconflictResolutionTypeDef
):
    """
    Type definition for `ClientMergeBranchesBySquash` `conflictResolution`

    A list of inputs to use when resolving conflicts during a merge if AUTOMERGE is chosen as the
    conflict resolution strategy.

    - **replaceContents** *(list) --*

      Files that will have content replaced as part of the merge conflict resolution.

      - *(dict) --*

        Information about a replacement content entry in the conflict of a merge or pull request
        operation.

        - **filePath** *(string) --* **[REQUIRED]**

          The path of the conflicting file.

        - **replacementType** *(string) --* **[REQUIRED]**

          The replacement type to use when determining how to resolve the conflict.

        - **content** *(bytes) --*

          The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

        - **fileMode** *(string) --*

          The file mode to apply during conflict resoltion.

    - **deleteFiles** *(list) --*

      Files that will be deleted as part of the merge conflict resolution.

      - *(dict) --*

        A file that will be deleted as part of a commit.

        - **filePath** *(string) --* **[REQUIRED]**

          The full path of the file that will be deleted, including the name of the file.

    - **setFileModes** *(list) --*

      File modes that will be set as part of the merge conflict resolution.

      - *(dict) --*

        Information about the file mode changes.

        - **filePath** *(string) --* **[REQUIRED]**

          The full path to the file, including the name of the file.

        - **fileMode** *(string) --* **[REQUIRED]**

          The file mode for the file.
    """


_ClientMergeBranchesByThreeWayResponseTypeDef = TypedDict(
    "_ClientMergeBranchesByThreeWayResponseTypeDef",
    {"commitId": str, "treeId": str},
    total=False,
)


class ClientMergeBranchesByThreeWayResponseTypeDef(
    _ClientMergeBranchesByThreeWayResponseTypeDef
):
    """
    Type definition for `ClientMergeBranchesByThreeWay` `Response`

    - **commitId** *(string) --*

      The commit ID of the merge in the destination or target branch.

    - **treeId** *(string) --*

      The tree ID of the merge in the destination or target branch.
    """


_ClientMergeBranchesByThreeWayconflictResolutiondeleteFilesTypeDef = TypedDict(
    "_ClientMergeBranchesByThreeWayconflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
)


class ClientMergeBranchesByThreeWayconflictResolutiondeleteFilesTypeDef(
    _ClientMergeBranchesByThreeWayconflictResolutiondeleteFilesTypeDef
):
    """
    Type definition for `ClientMergeBranchesByThreeWayconflictResolution` `deleteFiles`

    A file that will be deleted as part of a commit.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path of the file that will be deleted, including the name of the file.
    """


_RequiredClientMergeBranchesByThreeWayconflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientMergeBranchesByThreeWayconflictResolutionreplaceContentsTypeDef",
    {"filePath": str, "replacementType": str},
)
_OptionalClientMergeBranchesByThreeWayconflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientMergeBranchesByThreeWayconflictResolutionreplaceContentsTypeDef",
    {"content": bytes, "fileMode": str},
    total=False,
)


class ClientMergeBranchesByThreeWayconflictResolutionreplaceContentsTypeDef(
    _RequiredClientMergeBranchesByThreeWayconflictResolutionreplaceContentsTypeDef,
    _OptionalClientMergeBranchesByThreeWayconflictResolutionreplaceContentsTypeDef,
):
    """
    Type definition for `ClientMergeBranchesByThreeWayconflictResolution` `replaceContents`

    Information about a replacement content entry in the conflict of a merge or pull request
    operation.

    - **filePath** *(string) --* **[REQUIRED]**

      The path of the conflicting file.

    - **replacementType** *(string) --* **[REQUIRED]**

      The replacement type to use when determining how to resolve the conflict.

    - **content** *(bytes) --*

      The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

    - **fileMode** *(string) --*

      The file mode to apply during conflict resoltion.
    """


_ClientMergeBranchesByThreeWayconflictResolutionsetFileModesTypeDef = TypedDict(
    "_ClientMergeBranchesByThreeWayconflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": str},
)


class ClientMergeBranchesByThreeWayconflictResolutionsetFileModesTypeDef(
    _ClientMergeBranchesByThreeWayconflictResolutionsetFileModesTypeDef
):
    """
    Type definition for `ClientMergeBranchesByThreeWayconflictResolution` `setFileModes`

    Information about the file mode changes.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path to the file, including the name of the file.

    - **fileMode** *(string) --* **[REQUIRED]**

      The file mode for the file.
    """


_ClientMergeBranchesByThreeWayconflictResolutionTypeDef = TypedDict(
    "_ClientMergeBranchesByThreeWayconflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientMergeBranchesByThreeWayconflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[
            ClientMergeBranchesByThreeWayconflictResolutiondeleteFilesTypeDef
        ],
        "setFileModes": List[
            ClientMergeBranchesByThreeWayconflictResolutionsetFileModesTypeDef
        ],
    },
    total=False,
)


class ClientMergeBranchesByThreeWayconflictResolutionTypeDef(
    _ClientMergeBranchesByThreeWayconflictResolutionTypeDef
):
    """
    Type definition for `ClientMergeBranchesByThreeWay` `conflictResolution`

    A list of inputs to use when resolving conflicts during a merge if AUTOMERGE is chosen as the
    conflict resolution strategy.

    - **replaceContents** *(list) --*

      Files that will have content replaced as part of the merge conflict resolution.

      - *(dict) --*

        Information about a replacement content entry in the conflict of a merge or pull request
        operation.

        - **filePath** *(string) --* **[REQUIRED]**

          The path of the conflicting file.

        - **replacementType** *(string) --* **[REQUIRED]**

          The replacement type to use when determining how to resolve the conflict.

        - **content** *(bytes) --*

          The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

        - **fileMode** *(string) --*

          The file mode to apply during conflict resoltion.

    - **deleteFiles** *(list) --*

      Files that will be deleted as part of the merge conflict resolution.

      - *(dict) --*

        A file that will be deleted as part of a commit.

        - **filePath** *(string) --* **[REQUIRED]**

          The full path of the file that will be deleted, including the name of the file.

    - **setFileModes** *(list) --*

      File modes that will be set as part of the merge conflict resolution.

      - *(dict) --*

        Information about the file mode changes.

        - **filePath** *(string) --* **[REQUIRED]**

          The full path to the file, including the name of the file.

        - **fileMode** *(string) --* **[REQUIRED]**

          The file mode for the file.
    """


_ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {"isMerged": bool, "mergedBy": str, "mergeCommitId": str, "mergeOption": str},
    total=False,
)


class ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    """
    Type definition for `ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargets` `mergeMetadata`

    Returns metadata about the state of the merge, including whether the merge has been
    made.

    - **isMerged** *(boolean) --*

      A Boolean value indicating whether the merge has been made.

    - **mergedBy** *(string) --*

      The Amazon Resource Name (ARN) of the user who merged the branches.

    - **mergeCommitId** *(string) --*

      The commit ID for the merge commit, if any.

    - **mergeOption** *(string) --*

      The merge strategy used in the merge.
    """


_ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef(
    _ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef
):
    """
    Type definition for `ClientMergePullRequestByFastForwardResponsepullRequest` `pullRequestTargets`

    Returns information about a pull request target.

    - **repositoryName** *(string) --*

      The name of the repository that contains the pull request source and destination
      branches.

    - **sourceReference** *(string) --*

      The branch of the repository that contains the changes for the pull request. Also known
      as the source branch.

    - **destinationReference** *(string) --*

      The branch of the repository where the pull request changes will be merged into. Also
      known as the destination branch.

    - **destinationCommit** *(string) --*

      The full commit ID that is the tip of the destination branch. This is the commit where
      the pull request was or will be merged.

    - **sourceCommit** *(string) --*

      The full commit ID of the tip of the source branch used to create the pull request. If
      the pull request branch is updated by a push while the pull request is open, the commit
      ID will change to reflect the new tip of the branch.

    - **mergeBase** *(string) --*

      The commit ID of the most recent commit that the source branch and the destination
      branch have in common.

    - **mergeMetadata** *(dict) --*

      Returns metadata about the state of the merge, including whether the merge has been
      made.

      - **isMerged** *(boolean) --*

        A Boolean value indicating whether the merge has been made.

      - **mergedBy** *(string) --*

        The Amazon Resource Name (ARN) of the user who merged the branches.

      - **mergeCommitId** *(string) --*

        The commit ID for the merge commit, if any.

      - **mergeOption** *(string) --*

        The merge strategy used in the merge.
    """


_ClientMergePullRequestByFastForwardResponsepullRequestTypeDef = TypedDict(
    "_ClientMergePullRequestByFastForwardResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": str,
        "authorArn": str,
        "pullRequestTargets": List[
            ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
    },
    total=False,
)


class ClientMergePullRequestByFastForwardResponsepullRequestTypeDef(
    _ClientMergePullRequestByFastForwardResponsepullRequestTypeDef
):
    """
    Type definition for `ClientMergePullRequestByFastForwardResponse` `pullRequest`

    Information about the specified pull request, including information about the merge.

    - **pullRequestId** *(string) --*

      The system-generated ID of the pull request.

    - **title** *(string) --*

      The user-defined title of the pull request. This title is displayed in the list of pull
      requests to other users of the repository.

    - **description** *(string) --*

      The user-defined description of the pull request. This description can be used to clarify
      what should be reviewed and other details of the request.

    - **lastActivityDate** *(datetime) --*

      The day and time of the last user or system activity on the pull request, in timestamp
      format.

    - **creationDate** *(datetime) --*

      The date and time the pull request was originally created, in timestamp format.

    - **pullRequestStatus** *(string) --*

      The status of the pull request. Pull request status can only change from ``OPEN`` to
      ``CLOSED`` .

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the user who created the pull request.

    - **pullRequestTargets** *(list) --*

      The targets of the pull request, including the source branch and destination branch for the
      pull request.

      - *(dict) --*

        Returns information about a pull request target.

        - **repositoryName** *(string) --*

          The name of the repository that contains the pull request source and destination
          branches.

        - **sourceReference** *(string) --*

          The branch of the repository that contains the changes for the pull request. Also known
          as the source branch.

        - **destinationReference** *(string) --*

          The branch of the repository where the pull request changes will be merged into. Also
          known as the destination branch.

        - **destinationCommit** *(string) --*

          The full commit ID that is the tip of the destination branch. This is the commit where
          the pull request was or will be merged.

        - **sourceCommit** *(string) --*

          The full commit ID of the tip of the source branch used to create the pull request. If
          the pull request branch is updated by a push while the pull request is open, the commit
          ID will change to reflect the new tip of the branch.

        - **mergeBase** *(string) --*

          The commit ID of the most recent commit that the source branch and the destination
          branch have in common.

        - **mergeMetadata** *(dict) --*

          Returns metadata about the state of the merge, including whether the merge has been
          made.

          - **isMerged** *(boolean) --*

            A Boolean value indicating whether the merge has been made.

          - **mergedBy** *(string) --*

            The Amazon Resource Name (ARN) of the user who merged the branches.

          - **mergeCommitId** *(string) --*

            The commit ID for the merge commit, if any.

          - **mergeOption** *(string) --*

            The merge strategy used in the merge.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientMergePullRequestByFastForwardResponseTypeDef = TypedDict(
    "_ClientMergePullRequestByFastForwardResponseTypeDef",
    {"pullRequest": ClientMergePullRequestByFastForwardResponsepullRequestTypeDef},
    total=False,
)


class ClientMergePullRequestByFastForwardResponseTypeDef(
    _ClientMergePullRequestByFastForwardResponseTypeDef
):
    """
    Type definition for `ClientMergePullRequestByFastForward` `Response`

    - **pullRequest** *(dict) --*

      Information about the specified pull request, including information about the merge.

      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.

      - **title** *(string) --*

        The user-defined title of the pull request. This title is displayed in the list of pull
        requests to other users of the repository.

      - **description** *(string) --*

        The user-defined description of the pull request. This description can be used to clarify
        what should be reviewed and other details of the request.

      - **lastActivityDate** *(datetime) --*

        The day and time of the last user or system activity on the pull request, in timestamp
        format.

      - **creationDate** *(datetime) --*

        The date and time the pull request was originally created, in timestamp format.

      - **pullRequestStatus** *(string) --*

        The status of the pull request. Pull request status can only change from ``OPEN`` to
        ``CLOSED`` .

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the user who created the pull request.

      - **pullRequestTargets** *(list) --*

        The targets of the pull request, including the source branch and destination branch for the
        pull request.

        - *(dict) --*

          Returns information about a pull request target.

          - **repositoryName** *(string) --*

            The name of the repository that contains the pull request source and destination
            branches.

          - **sourceReference** *(string) --*

            The branch of the repository that contains the changes for the pull request. Also known
            as the source branch.

          - **destinationReference** *(string) --*

            The branch of the repository where the pull request changes will be merged into. Also
            known as the destination branch.

          - **destinationCommit** *(string) --*

            The full commit ID that is the tip of the destination branch. This is the commit where
            the pull request was or will be merged.

          - **sourceCommit** *(string) --*

            The full commit ID of the tip of the source branch used to create the pull request. If
            the pull request branch is updated by a push while the pull request is open, the commit
            ID will change to reflect the new tip of the branch.

          - **mergeBase** *(string) --*

            The commit ID of the most recent commit that the source branch and the destination
            branch have in common.

          - **mergeMetadata** *(dict) --*

            Returns metadata about the state of the merge, including whether the merge has been
            made.

            - **isMerged** *(boolean) --*

              A Boolean value indicating whether the merge has been made.

            - **mergedBy** *(string) --*

              The Amazon Resource Name (ARN) of the user who merged the branches.

            - **mergeCommitId** *(string) --*

              The commit ID for the merge commit, if any.

            - **mergeOption** *(string) --*

              The merge strategy used in the merge.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {"isMerged": bool, "mergedBy": str, "mergeCommitId": str, "mergeOption": str},
    total=False,
)


class ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    """
    Type definition for `ClientMergePullRequestBySquashResponsepullRequestpullRequestTargets` `mergeMetadata`

    Returns metadata about the state of the merge, including whether the merge has been
    made.

    - **isMerged** *(boolean) --*

      A Boolean value indicating whether the merge has been made.

    - **mergedBy** *(string) --*

      The Amazon Resource Name (ARN) of the user who merged the branches.

    - **mergeCommitId** *(string) --*

      The commit ID for the merge commit, if any.

    - **mergeOption** *(string) --*

      The merge strategy used in the merge.
    """


_ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef(
    _ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef
):
    """
    Type definition for `ClientMergePullRequestBySquashResponsepullRequest` `pullRequestTargets`

    Returns information about a pull request target.

    - **repositoryName** *(string) --*

      The name of the repository that contains the pull request source and destination
      branches.

    - **sourceReference** *(string) --*

      The branch of the repository that contains the changes for the pull request. Also known
      as the source branch.

    - **destinationReference** *(string) --*

      The branch of the repository where the pull request changes will be merged into. Also
      known as the destination branch.

    - **destinationCommit** *(string) --*

      The full commit ID that is the tip of the destination branch. This is the commit where
      the pull request was or will be merged.

    - **sourceCommit** *(string) --*

      The full commit ID of the tip of the source branch used to create the pull request. If
      the pull request branch is updated by a push while the pull request is open, the commit
      ID will change to reflect the new tip of the branch.

    - **mergeBase** *(string) --*

      The commit ID of the most recent commit that the source branch and the destination
      branch have in common.

    - **mergeMetadata** *(dict) --*

      Returns metadata about the state of the merge, including whether the merge has been
      made.

      - **isMerged** *(boolean) --*

        A Boolean value indicating whether the merge has been made.

      - **mergedBy** *(string) --*

        The Amazon Resource Name (ARN) of the user who merged the branches.

      - **mergeCommitId** *(string) --*

        The commit ID for the merge commit, if any.

      - **mergeOption** *(string) --*

        The merge strategy used in the merge.
    """


_ClientMergePullRequestBySquashResponsepullRequestTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": str,
        "authorArn": str,
        "pullRequestTargets": List[
            ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
    },
    total=False,
)


class ClientMergePullRequestBySquashResponsepullRequestTypeDef(
    _ClientMergePullRequestBySquashResponsepullRequestTypeDef
):
    """
    Type definition for `ClientMergePullRequestBySquashResponse` `pullRequest`

    Returns information about a pull request.

    - **pullRequestId** *(string) --*

      The system-generated ID of the pull request.

    - **title** *(string) --*

      The user-defined title of the pull request. This title is displayed in the list of pull
      requests to other users of the repository.

    - **description** *(string) --*

      The user-defined description of the pull request. This description can be used to clarify
      what should be reviewed and other details of the request.

    - **lastActivityDate** *(datetime) --*

      The day and time of the last user or system activity on the pull request, in timestamp
      format.

    - **creationDate** *(datetime) --*

      The date and time the pull request was originally created, in timestamp format.

    - **pullRequestStatus** *(string) --*

      The status of the pull request. Pull request status can only change from ``OPEN`` to
      ``CLOSED`` .

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the user who created the pull request.

    - **pullRequestTargets** *(list) --*

      The targets of the pull request, including the source branch and destination branch for the
      pull request.

      - *(dict) --*

        Returns information about a pull request target.

        - **repositoryName** *(string) --*

          The name of the repository that contains the pull request source and destination
          branches.

        - **sourceReference** *(string) --*

          The branch of the repository that contains the changes for the pull request. Also known
          as the source branch.

        - **destinationReference** *(string) --*

          The branch of the repository where the pull request changes will be merged into. Also
          known as the destination branch.

        - **destinationCommit** *(string) --*

          The full commit ID that is the tip of the destination branch. This is the commit where
          the pull request was or will be merged.

        - **sourceCommit** *(string) --*

          The full commit ID of the tip of the source branch used to create the pull request. If
          the pull request branch is updated by a push while the pull request is open, the commit
          ID will change to reflect the new tip of the branch.

        - **mergeBase** *(string) --*

          The commit ID of the most recent commit that the source branch and the destination
          branch have in common.

        - **mergeMetadata** *(dict) --*

          Returns metadata about the state of the merge, including whether the merge has been
          made.

          - **isMerged** *(boolean) --*

            A Boolean value indicating whether the merge has been made.

          - **mergedBy** *(string) --*

            The Amazon Resource Name (ARN) of the user who merged the branches.

          - **mergeCommitId** *(string) --*

            The commit ID for the merge commit, if any.

          - **mergeOption** *(string) --*

            The merge strategy used in the merge.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientMergePullRequestBySquashResponseTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashResponseTypeDef",
    {"pullRequest": ClientMergePullRequestBySquashResponsepullRequestTypeDef},
    total=False,
)


class ClientMergePullRequestBySquashResponseTypeDef(
    _ClientMergePullRequestBySquashResponseTypeDef
):
    """
    Type definition for `ClientMergePullRequestBySquash` `Response`

    - **pullRequest** *(dict) --*

      Returns information about a pull request.

      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.

      - **title** *(string) --*

        The user-defined title of the pull request. This title is displayed in the list of pull
        requests to other users of the repository.

      - **description** *(string) --*

        The user-defined description of the pull request. This description can be used to clarify
        what should be reviewed and other details of the request.

      - **lastActivityDate** *(datetime) --*

        The day and time of the last user or system activity on the pull request, in timestamp
        format.

      - **creationDate** *(datetime) --*

        The date and time the pull request was originally created, in timestamp format.

      - **pullRequestStatus** *(string) --*

        The status of the pull request. Pull request status can only change from ``OPEN`` to
        ``CLOSED`` .

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the user who created the pull request.

      - **pullRequestTargets** *(list) --*

        The targets of the pull request, including the source branch and destination branch for the
        pull request.

        - *(dict) --*

          Returns information about a pull request target.

          - **repositoryName** *(string) --*

            The name of the repository that contains the pull request source and destination
            branches.

          - **sourceReference** *(string) --*

            The branch of the repository that contains the changes for the pull request. Also known
            as the source branch.

          - **destinationReference** *(string) --*

            The branch of the repository where the pull request changes will be merged into. Also
            known as the destination branch.

          - **destinationCommit** *(string) --*

            The full commit ID that is the tip of the destination branch. This is the commit where
            the pull request was or will be merged.

          - **sourceCommit** *(string) --*

            The full commit ID of the tip of the source branch used to create the pull request. If
            the pull request branch is updated by a push while the pull request is open, the commit
            ID will change to reflect the new tip of the branch.

          - **mergeBase** *(string) --*

            The commit ID of the most recent commit that the source branch and the destination
            branch have in common.

          - **mergeMetadata** *(dict) --*

            Returns metadata about the state of the merge, including whether the merge has been
            made.

            - **isMerged** *(boolean) --*

              A Boolean value indicating whether the merge has been made.

            - **mergedBy** *(string) --*

              The Amazon Resource Name (ARN) of the user who merged the branches.

            - **mergeCommitId** *(string) --*

              The commit ID for the merge commit, if any.

            - **mergeOption** *(string) --*

              The merge strategy used in the merge.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_ClientMergePullRequestBySquashconflictResolutiondeleteFilesTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashconflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
)


class ClientMergePullRequestBySquashconflictResolutiondeleteFilesTypeDef(
    _ClientMergePullRequestBySquashconflictResolutiondeleteFilesTypeDef
):
    """
    Type definition for `ClientMergePullRequestBySquashconflictResolution` `deleteFiles`

    A file that will be deleted as part of a commit.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path of the file that will be deleted, including the name of the file.
    """


_RequiredClientMergePullRequestBySquashconflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientMergePullRequestBySquashconflictResolutionreplaceContentsTypeDef",
    {"filePath": str, "replacementType": str},
)
_OptionalClientMergePullRequestBySquashconflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientMergePullRequestBySquashconflictResolutionreplaceContentsTypeDef",
    {"content": bytes, "fileMode": str},
    total=False,
)


class ClientMergePullRequestBySquashconflictResolutionreplaceContentsTypeDef(
    _RequiredClientMergePullRequestBySquashconflictResolutionreplaceContentsTypeDef,
    _OptionalClientMergePullRequestBySquashconflictResolutionreplaceContentsTypeDef,
):
    """
    Type definition for `ClientMergePullRequestBySquashconflictResolution` `replaceContents`

    Information about a replacement content entry in the conflict of a merge or pull request
    operation.

    - **filePath** *(string) --* **[REQUIRED]**

      The path of the conflicting file.

    - **replacementType** *(string) --* **[REQUIRED]**

      The replacement type to use when determining how to resolve the conflict.

    - **content** *(bytes) --*

      The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

    - **fileMode** *(string) --*

      The file mode to apply during conflict resoltion.
    """


_ClientMergePullRequestBySquashconflictResolutionsetFileModesTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashconflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": str},
)


class ClientMergePullRequestBySquashconflictResolutionsetFileModesTypeDef(
    _ClientMergePullRequestBySquashconflictResolutionsetFileModesTypeDef
):
    """
    Type definition for `ClientMergePullRequestBySquashconflictResolution` `setFileModes`

    Information about the file mode changes.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path to the file, including the name of the file.

    - **fileMode** *(string) --* **[REQUIRED]**

      The file mode for the file.
    """


_ClientMergePullRequestBySquashconflictResolutionTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashconflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientMergePullRequestBySquashconflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[
            ClientMergePullRequestBySquashconflictResolutiondeleteFilesTypeDef
        ],
        "setFileModes": List[
            ClientMergePullRequestBySquashconflictResolutionsetFileModesTypeDef
        ],
    },
    total=False,
)


class ClientMergePullRequestBySquashconflictResolutionTypeDef(
    _ClientMergePullRequestBySquashconflictResolutionTypeDef
):
    """
    Type definition for `ClientMergePullRequestBySquash` `conflictResolution`

    A list of inputs to use when resolving conflicts during a merge if AUTOMERGE is chosen as the
    conflict resolution strategy.

    - **replaceContents** *(list) --*

      Files that will have content replaced as part of the merge conflict resolution.

      - *(dict) --*

        Information about a replacement content entry in the conflict of a merge or pull request
        operation.

        - **filePath** *(string) --* **[REQUIRED]**

          The path of the conflicting file.

        - **replacementType** *(string) --* **[REQUIRED]**

          The replacement type to use when determining how to resolve the conflict.

        - **content** *(bytes) --*

          The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

        - **fileMode** *(string) --*

          The file mode to apply during conflict resoltion.

    - **deleteFiles** *(list) --*

      Files that will be deleted as part of the merge conflict resolution.

      - *(dict) --*

        A file that will be deleted as part of a commit.

        - **filePath** *(string) --* **[REQUIRED]**

          The full path of the file that will be deleted, including the name of the file.

    - **setFileModes** *(list) --*

      File modes that will be set as part of the merge conflict resolution.

      - *(dict) --*

        Information about the file mode changes.

        - **filePath** *(string) --* **[REQUIRED]**

          The full path to the file, including the name of the file.

        - **fileMode** *(string) --* **[REQUIRED]**

          The file mode for the file.
    """


_ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {"isMerged": bool, "mergedBy": str, "mergeCommitId": str, "mergeOption": str},
    total=False,
)


class ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    """
    Type definition for `ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargets` `mergeMetadata`

    Returns metadata about the state of the merge, including whether the merge has been
    made.

    - **isMerged** *(boolean) --*

      A Boolean value indicating whether the merge has been made.

    - **mergedBy** *(string) --*

      The Amazon Resource Name (ARN) of the user who merged the branches.

    - **mergeCommitId** *(string) --*

      The commit ID for the merge commit, if any.

    - **mergeOption** *(string) --*

      The merge strategy used in the merge.
    """


_ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef(
    _ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef
):
    """
    Type definition for `ClientMergePullRequestByThreeWayResponsepullRequest` `pullRequestTargets`

    Returns information about a pull request target.

    - **repositoryName** *(string) --*

      The name of the repository that contains the pull request source and destination
      branches.

    - **sourceReference** *(string) --*

      The branch of the repository that contains the changes for the pull request. Also known
      as the source branch.

    - **destinationReference** *(string) --*

      The branch of the repository where the pull request changes will be merged into. Also
      known as the destination branch.

    - **destinationCommit** *(string) --*

      The full commit ID that is the tip of the destination branch. This is the commit where
      the pull request was or will be merged.

    - **sourceCommit** *(string) --*

      The full commit ID of the tip of the source branch used to create the pull request. If
      the pull request branch is updated by a push while the pull request is open, the commit
      ID will change to reflect the new tip of the branch.

    - **mergeBase** *(string) --*

      The commit ID of the most recent commit that the source branch and the destination
      branch have in common.

    - **mergeMetadata** *(dict) --*

      Returns metadata about the state of the merge, including whether the merge has been
      made.

      - **isMerged** *(boolean) --*

        A Boolean value indicating whether the merge has been made.

      - **mergedBy** *(string) --*

        The Amazon Resource Name (ARN) of the user who merged the branches.

      - **mergeCommitId** *(string) --*

        The commit ID for the merge commit, if any.

      - **mergeOption** *(string) --*

        The merge strategy used in the merge.
    """


_ClientMergePullRequestByThreeWayResponsepullRequestTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": str,
        "authorArn": str,
        "pullRequestTargets": List[
            ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
    },
    total=False,
)


class ClientMergePullRequestByThreeWayResponsepullRequestTypeDef(
    _ClientMergePullRequestByThreeWayResponsepullRequestTypeDef
):
    """
    Type definition for `ClientMergePullRequestByThreeWayResponse` `pullRequest`

    Returns information about a pull request.

    - **pullRequestId** *(string) --*

      The system-generated ID of the pull request.

    - **title** *(string) --*

      The user-defined title of the pull request. This title is displayed in the list of pull
      requests to other users of the repository.

    - **description** *(string) --*

      The user-defined description of the pull request. This description can be used to clarify
      what should be reviewed and other details of the request.

    - **lastActivityDate** *(datetime) --*

      The day and time of the last user or system activity on the pull request, in timestamp
      format.

    - **creationDate** *(datetime) --*

      The date and time the pull request was originally created, in timestamp format.

    - **pullRequestStatus** *(string) --*

      The status of the pull request. Pull request status can only change from ``OPEN`` to
      ``CLOSED`` .

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the user who created the pull request.

    - **pullRequestTargets** *(list) --*

      The targets of the pull request, including the source branch and destination branch for the
      pull request.

      - *(dict) --*

        Returns information about a pull request target.

        - **repositoryName** *(string) --*

          The name of the repository that contains the pull request source and destination
          branches.

        - **sourceReference** *(string) --*

          The branch of the repository that contains the changes for the pull request. Also known
          as the source branch.

        - **destinationReference** *(string) --*

          The branch of the repository where the pull request changes will be merged into. Also
          known as the destination branch.

        - **destinationCommit** *(string) --*

          The full commit ID that is the tip of the destination branch. This is the commit where
          the pull request was or will be merged.

        - **sourceCommit** *(string) --*

          The full commit ID of the tip of the source branch used to create the pull request. If
          the pull request branch is updated by a push while the pull request is open, the commit
          ID will change to reflect the new tip of the branch.

        - **mergeBase** *(string) --*

          The commit ID of the most recent commit that the source branch and the destination
          branch have in common.

        - **mergeMetadata** *(dict) --*

          Returns metadata about the state of the merge, including whether the merge has been
          made.

          - **isMerged** *(boolean) --*

            A Boolean value indicating whether the merge has been made.

          - **mergedBy** *(string) --*

            The Amazon Resource Name (ARN) of the user who merged the branches.

          - **mergeCommitId** *(string) --*

            The commit ID for the merge commit, if any.

          - **mergeOption** *(string) --*

            The merge strategy used in the merge.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientMergePullRequestByThreeWayResponseTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayResponseTypeDef",
    {"pullRequest": ClientMergePullRequestByThreeWayResponsepullRequestTypeDef},
    total=False,
)


class ClientMergePullRequestByThreeWayResponseTypeDef(
    _ClientMergePullRequestByThreeWayResponseTypeDef
):
    """
    Type definition for `ClientMergePullRequestByThreeWay` `Response`

    - **pullRequest** *(dict) --*

      Returns information about a pull request.

      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.

      - **title** *(string) --*

        The user-defined title of the pull request. This title is displayed in the list of pull
        requests to other users of the repository.

      - **description** *(string) --*

        The user-defined description of the pull request. This description can be used to clarify
        what should be reviewed and other details of the request.

      - **lastActivityDate** *(datetime) --*

        The day and time of the last user or system activity on the pull request, in timestamp
        format.

      - **creationDate** *(datetime) --*

        The date and time the pull request was originally created, in timestamp format.

      - **pullRequestStatus** *(string) --*

        The status of the pull request. Pull request status can only change from ``OPEN`` to
        ``CLOSED`` .

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the user who created the pull request.

      - **pullRequestTargets** *(list) --*

        The targets of the pull request, including the source branch and destination branch for the
        pull request.

        - *(dict) --*

          Returns information about a pull request target.

          - **repositoryName** *(string) --*

            The name of the repository that contains the pull request source and destination
            branches.

          - **sourceReference** *(string) --*

            The branch of the repository that contains the changes for the pull request. Also known
            as the source branch.

          - **destinationReference** *(string) --*

            The branch of the repository where the pull request changes will be merged into. Also
            known as the destination branch.

          - **destinationCommit** *(string) --*

            The full commit ID that is the tip of the destination branch. This is the commit where
            the pull request was or will be merged.

          - **sourceCommit** *(string) --*

            The full commit ID of the tip of the source branch used to create the pull request. If
            the pull request branch is updated by a push while the pull request is open, the commit
            ID will change to reflect the new tip of the branch.

          - **mergeBase** *(string) --*

            The commit ID of the most recent commit that the source branch and the destination
            branch have in common.

          - **mergeMetadata** *(dict) --*

            Returns metadata about the state of the merge, including whether the merge has been
            made.

            - **isMerged** *(boolean) --*

              A Boolean value indicating whether the merge has been made.

            - **mergedBy** *(string) --*

              The Amazon Resource Name (ARN) of the user who merged the branches.

            - **mergeCommitId** *(string) --*

              The commit ID for the merge commit, if any.

            - **mergeOption** *(string) --*

              The merge strategy used in the merge.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_ClientMergePullRequestByThreeWayconflictResolutiondeleteFilesTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayconflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
)


class ClientMergePullRequestByThreeWayconflictResolutiondeleteFilesTypeDef(
    _ClientMergePullRequestByThreeWayconflictResolutiondeleteFilesTypeDef
):
    """
    Type definition for `ClientMergePullRequestByThreeWayconflictResolution` `deleteFiles`

    A file that will be deleted as part of a commit.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path of the file that will be deleted, including the name of the file.
    """


_RequiredClientMergePullRequestByThreeWayconflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientMergePullRequestByThreeWayconflictResolutionreplaceContentsTypeDef",
    {"filePath": str, "replacementType": str},
)
_OptionalClientMergePullRequestByThreeWayconflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientMergePullRequestByThreeWayconflictResolutionreplaceContentsTypeDef",
    {"content": bytes, "fileMode": str},
    total=False,
)


class ClientMergePullRequestByThreeWayconflictResolutionreplaceContentsTypeDef(
    _RequiredClientMergePullRequestByThreeWayconflictResolutionreplaceContentsTypeDef,
    _OptionalClientMergePullRequestByThreeWayconflictResolutionreplaceContentsTypeDef,
):
    """
    Type definition for `ClientMergePullRequestByThreeWayconflictResolution` `replaceContents`

    Information about a replacement content entry in the conflict of a merge or pull request
    operation.

    - **filePath** *(string) --* **[REQUIRED]**

      The path of the conflicting file.

    - **replacementType** *(string) --* **[REQUIRED]**

      The replacement type to use when determining how to resolve the conflict.

    - **content** *(bytes) --*

      The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

    - **fileMode** *(string) --*

      The file mode to apply during conflict resoltion.
    """


_ClientMergePullRequestByThreeWayconflictResolutionsetFileModesTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayconflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": str},
)


class ClientMergePullRequestByThreeWayconflictResolutionsetFileModesTypeDef(
    _ClientMergePullRequestByThreeWayconflictResolutionsetFileModesTypeDef
):
    """
    Type definition for `ClientMergePullRequestByThreeWayconflictResolution` `setFileModes`

    Information about the file mode changes.

    - **filePath** *(string) --* **[REQUIRED]**

      The full path to the file, including the name of the file.

    - **fileMode** *(string) --* **[REQUIRED]**

      The file mode for the file.
    """


_ClientMergePullRequestByThreeWayconflictResolutionTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayconflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientMergePullRequestByThreeWayconflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[
            ClientMergePullRequestByThreeWayconflictResolutiondeleteFilesTypeDef
        ],
        "setFileModes": List[
            ClientMergePullRequestByThreeWayconflictResolutionsetFileModesTypeDef
        ],
    },
    total=False,
)


class ClientMergePullRequestByThreeWayconflictResolutionTypeDef(
    _ClientMergePullRequestByThreeWayconflictResolutionTypeDef
):
    """
    Type definition for `ClientMergePullRequestByThreeWay` `conflictResolution`

    A list of inputs to use when resolving conflicts during a merge if AUTOMERGE is chosen as the
    conflict resolution strategy.

    - **replaceContents** *(list) --*

      Files that will have content replaced as part of the merge conflict resolution.

      - *(dict) --*

        Information about a replacement content entry in the conflict of a merge or pull request
        operation.

        - **filePath** *(string) --* **[REQUIRED]**

          The path of the conflicting file.

        - **replacementType** *(string) --* **[REQUIRED]**

          The replacement type to use when determining how to resolve the conflict.

        - **content** *(bytes) --*

          The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

        - **fileMode** *(string) --*

          The file mode to apply during conflict resoltion.

    - **deleteFiles** *(list) --*

      Files that will be deleted as part of the merge conflict resolution.

      - *(dict) --*

        A file that will be deleted as part of a commit.

        - **filePath** *(string) --* **[REQUIRED]**

          The full path of the file that will be deleted, including the name of the file.

    - **setFileModes** *(list) --*

      File modes that will be set as part of the merge conflict resolution.

      - *(dict) --*

        Information about the file mode changes.

        - **filePath** *(string) --* **[REQUIRED]**

          The full path to the file, including the name of the file.

        - **fileMode** *(string) --* **[REQUIRED]**

          The file mode for the file.
    """


_ClientPostCommentForComparedCommitResponsecommentTypeDef = TypedDict(
    "_ClientPostCommentForComparedCommitResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientPostCommentForComparedCommitResponsecommentTypeDef(
    _ClientPostCommentForComparedCommitResponsecommentTypeDef
):
    """
    Type definition for `ClientPostCommentForComparedCommitResponse` `comment`

    The content of the comment you posted.

    - **commentId** *(string) --*

      The system-generated comment ID.

    - **content** *(string) --*

      The content of the comment.

    - **inReplyTo** *(string) --*

      The ID of the comment for which this comment is a reply, if any.

    - **creationDate** *(datetime) --*

      The date and time the comment was created, in timestamp format.

    - **lastModifiedDate** *(datetime) --*

      The date and time the comment was most recently modified, in timestamp format.

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the person who posted the comment.

    - **deleted** *(boolean) --*

      A Boolean value indicating whether the comment has been deleted.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientPostCommentForComparedCommitResponselocationTypeDef = TypedDict(
    "_ClientPostCommentForComparedCommitResponselocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": str},
    total=False,
)


class ClientPostCommentForComparedCommitResponselocationTypeDef(
    _ClientPostCommentForComparedCommitResponselocationTypeDef
):
    """
    Type definition for `ClientPostCommentForComparedCommitResponse` `location`

    The location of the comment in the comparison between the two commits.

    - **filePath** *(string) --*

      The name of the file being compared, including its extension and subdirectory, if any.

    - **filePosition** *(integer) --*

      The position of a change within a compared file, in line number format.

    - **relativeFileVersion** *(string) --*

      In a comparison of commits or a pull request, whether the change is in the 'before' or
      'after' of that comparison.
    """


_ClientPostCommentForComparedCommitResponseTypeDef = TypedDict(
    "_ClientPostCommentForComparedCommitResponseTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": ClientPostCommentForComparedCommitResponselocationTypeDef,
        "comment": ClientPostCommentForComparedCommitResponsecommentTypeDef,
    },
    total=False,
)


class ClientPostCommentForComparedCommitResponseTypeDef(
    _ClientPostCommentForComparedCommitResponseTypeDef
):
    """
    Type definition for `ClientPostCommentForComparedCommit` `Response`

    - **repositoryName** *(string) --*

      The name of the repository where you posted a comment on the comparison between commits.

    - **beforeCommitId** *(string) --*

      In the directionality you established, the full commit ID of the 'before' commit.

    - **afterCommitId** *(string) --*

      In the directionality you established, the full commit ID of the 'after' commit.

    - **beforeBlobId** *(string) --*

      In the directionality you established, the blob ID of the 'before' blob.

    - **afterBlobId** *(string) --*

      In the directionality you established, the blob ID of the 'after' blob.

    - **location** *(dict) --*

      The location of the comment in the comparison between the two commits.

      - **filePath** *(string) --*

        The name of the file being compared, including its extension and subdirectory, if any.

      - **filePosition** *(integer) --*

        The position of a change within a compared file, in line number format.

      - **relativeFileVersion** *(string) --*

        In a comparison of commits or a pull request, whether the change is in the 'before' or
        'after' of that comparison.

    - **comment** *(dict) --*

      The content of the comment you posted.

      - **commentId** *(string) --*

        The system-generated comment ID.

      - **content** *(string) --*

        The content of the comment.

      - **inReplyTo** *(string) --*

        The ID of the comment for which this comment is a reply, if any.

      - **creationDate** *(datetime) --*

        The date and time the comment was created, in timestamp format.

      - **lastModifiedDate** *(datetime) --*

        The date and time the comment was most recently modified, in timestamp format.

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the person who posted the comment.

      - **deleted** *(boolean) --*

        A Boolean value indicating whether the comment has been deleted.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_ClientPostCommentForComparedCommitlocationTypeDef = TypedDict(
    "_ClientPostCommentForComparedCommitlocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": str},
    total=False,
)


class ClientPostCommentForComparedCommitlocationTypeDef(
    _ClientPostCommentForComparedCommitlocationTypeDef
):
    """
    Type definition for `ClientPostCommentForComparedCommit` `location`

    The location of the comparison where you want to comment.

    - **filePath** *(string) --*

      The name of the file being compared, including its extension and subdirectory, if any.

    - **filePosition** *(integer) --*

      The position of a change within a compared file, in line number format.

    - **relativeFileVersion** *(string) --*

      In a comparison of commits or a pull request, whether the change is in the 'before' or 'after'
      of that comparison.
    """


_ClientPostCommentForPullRequestResponsecommentTypeDef = TypedDict(
    "_ClientPostCommentForPullRequestResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientPostCommentForPullRequestResponsecommentTypeDef(
    _ClientPostCommentForPullRequestResponsecommentTypeDef
):
    """
    Type definition for `ClientPostCommentForPullRequestResponse` `comment`

    The content of the comment you posted.

    - **commentId** *(string) --*

      The system-generated comment ID.

    - **content** *(string) --*

      The content of the comment.

    - **inReplyTo** *(string) --*

      The ID of the comment for which this comment is a reply, if any.

    - **creationDate** *(datetime) --*

      The date and time the comment was created, in timestamp format.

    - **lastModifiedDate** *(datetime) --*

      The date and time the comment was most recently modified, in timestamp format.

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the person who posted the comment.

    - **deleted** *(boolean) --*

      A Boolean value indicating whether the comment has been deleted.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientPostCommentForPullRequestResponselocationTypeDef = TypedDict(
    "_ClientPostCommentForPullRequestResponselocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": str},
    total=False,
)


class ClientPostCommentForPullRequestResponselocationTypeDef(
    _ClientPostCommentForPullRequestResponselocationTypeDef
):
    """
    Type definition for `ClientPostCommentForPullRequestResponse` `location`

    The location of the change where you posted your comment.

    - **filePath** *(string) --*

      The name of the file being compared, including its extension and subdirectory, if any.

    - **filePosition** *(integer) --*

      The position of a change within a compared file, in line number format.

    - **relativeFileVersion** *(string) --*

      In a comparison of commits or a pull request, whether the change is in the 'before' or
      'after' of that comparison.
    """


_ClientPostCommentForPullRequestResponseTypeDef = TypedDict(
    "_ClientPostCommentForPullRequestResponseTypeDef",
    {
        "repositoryName": str,
        "pullRequestId": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": ClientPostCommentForPullRequestResponselocationTypeDef,
        "comment": ClientPostCommentForPullRequestResponsecommentTypeDef,
    },
    total=False,
)


class ClientPostCommentForPullRequestResponseTypeDef(
    _ClientPostCommentForPullRequestResponseTypeDef
):
    """
    Type definition for `ClientPostCommentForPullRequest` `Response`

    - **repositoryName** *(string) --*

      The name of the repository where you posted a comment on a pull request.

    - **pullRequestId** *(string) --*

      The system-generated ID of the pull request.

    - **beforeCommitId** *(string) --*

      The full commit ID of the commit in the source branch used to create the pull request, or in
      the case of an updated pull request, the full commit ID of the commit used to update the pull
      request.

    - **afterCommitId** *(string) --*

      The full commit ID of the commit in the destination branch where the pull request will be
      merged.

    - **beforeBlobId** *(string) --*

      In the directionality of the pull request, the blob ID of the 'before' blob.

    - **afterBlobId** *(string) --*

      In the directionality of the pull request, the blob ID of the 'after' blob.

    - **location** *(dict) --*

      The location of the change where you posted your comment.

      - **filePath** *(string) --*

        The name of the file being compared, including its extension and subdirectory, if any.

      - **filePosition** *(integer) --*

        The position of a change within a compared file, in line number format.

      - **relativeFileVersion** *(string) --*

        In a comparison of commits or a pull request, whether the change is in the 'before' or
        'after' of that comparison.

    - **comment** *(dict) --*

      The content of the comment you posted.

      - **commentId** *(string) --*

        The system-generated comment ID.

      - **content** *(string) --*

        The content of the comment.

      - **inReplyTo** *(string) --*

        The ID of the comment for which this comment is a reply, if any.

      - **creationDate** *(datetime) --*

        The date and time the comment was created, in timestamp format.

      - **lastModifiedDate** *(datetime) --*

        The date and time the comment was most recently modified, in timestamp format.

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the person who posted the comment.

      - **deleted** *(boolean) --*

        A Boolean value indicating whether the comment has been deleted.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_ClientPostCommentForPullRequestlocationTypeDef = TypedDict(
    "_ClientPostCommentForPullRequestlocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": str},
    total=False,
)


class ClientPostCommentForPullRequestlocationTypeDef(
    _ClientPostCommentForPullRequestlocationTypeDef
):
    """
    Type definition for `ClientPostCommentForPullRequest` `location`

    The location of the change where you want to post your comment. If no location is provided, the
    comment will be posted as a general comment on the pull request difference between the before
    commit ID and the after commit ID.

    - **filePath** *(string) --*

      The name of the file being compared, including its extension and subdirectory, if any.

    - **filePosition** *(integer) --*

      The position of a change within a compared file, in line number format.

    - **relativeFileVersion** *(string) --*

      In a comparison of commits or a pull request, whether the change is in the 'before' or 'after'
      of that comparison.
    """


_ClientPostCommentReplyResponsecommentTypeDef = TypedDict(
    "_ClientPostCommentReplyResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientPostCommentReplyResponsecommentTypeDef(
    _ClientPostCommentReplyResponsecommentTypeDef
):
    """
    Type definition for `ClientPostCommentReplyResponse` `comment`

    Information about the reply to a comment.

    - **commentId** *(string) --*

      The system-generated comment ID.

    - **content** *(string) --*

      The content of the comment.

    - **inReplyTo** *(string) --*

      The ID of the comment for which this comment is a reply, if any.

    - **creationDate** *(datetime) --*

      The date and time the comment was created, in timestamp format.

    - **lastModifiedDate** *(datetime) --*

      The date and time the comment was most recently modified, in timestamp format.

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the person who posted the comment.

    - **deleted** *(boolean) --*

      A Boolean value indicating whether the comment has been deleted.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientPostCommentReplyResponseTypeDef = TypedDict(
    "_ClientPostCommentReplyResponseTypeDef",
    {"comment": ClientPostCommentReplyResponsecommentTypeDef},
    total=False,
)


class ClientPostCommentReplyResponseTypeDef(_ClientPostCommentReplyResponseTypeDef):
    """
    Type definition for `ClientPostCommentReply` `Response`

    - **comment** *(dict) --*

      Information about the reply to a comment.

      - **commentId** *(string) --*

        The system-generated comment ID.

      - **content** *(string) --*

        The content of the comment.

      - **inReplyTo** *(string) --*

        The ID of the comment for which this comment is a reply, if any.

      - **creationDate** *(datetime) --*

        The date and time the comment was created, in timestamp format.

      - **lastModifiedDate** *(datetime) --*

        The date and time the comment was most recently modified, in timestamp format.

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the person who posted the comment.

      - **deleted** *(boolean) --*

        A Boolean value indicating whether the comment has been deleted.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_ClientPutFileResponseTypeDef = TypedDict(
    "_ClientPutFileResponseTypeDef",
    {"commitId": str, "blobId": str, "treeId": str},
    total=False,
)


class ClientPutFileResponseTypeDef(_ClientPutFileResponseTypeDef):
    """
    Type definition for `ClientPutFile` `Response`

    - **commitId** *(string) --*

      The full SHA of the commit that contains this file change.

    - **blobId** *(string) --*

      The ID of the blob, which is its SHA-1 pointer.

    - **treeId** *(string) --*

      The full SHA-1 pointer of the tree information for the commit that contains this file change.
    """


_ClientPutRepositoryTriggersResponseTypeDef = TypedDict(
    "_ClientPutRepositoryTriggersResponseTypeDef", {"configurationId": str}, total=False
)


class ClientPutRepositoryTriggersResponseTypeDef(
    _ClientPutRepositoryTriggersResponseTypeDef
):
    """
    Type definition for `ClientPutRepositoryTriggers` `Response`

    Represents the output of a put repository triggers operation.

    - **configurationId** *(string) --*

      The system-generated unique ID for the create or update operation.
    """


_RequiredClientPutRepositoryTriggerstriggersTypeDef = TypedDict(
    "_RequiredClientPutRepositoryTriggerstriggersTypeDef",
    {"name": str, "destinationArn": str, "events": List[str]},
)
_OptionalClientPutRepositoryTriggerstriggersTypeDef = TypedDict(
    "_OptionalClientPutRepositoryTriggerstriggersTypeDef",
    {"customData": str, "branches": List[str]},
    total=False,
)


class ClientPutRepositoryTriggerstriggersTypeDef(
    _RequiredClientPutRepositoryTriggerstriggersTypeDef,
    _OptionalClientPutRepositoryTriggerstriggersTypeDef,
):
    """
    Type definition for `ClientPutRepositoryTriggers` `triggers`

    Information about a trigger for a repository.

    - **name** *(string) --* **[REQUIRED]**

      The name of the trigger.

    - **destinationArn** *(string) --* **[REQUIRED]**

      The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in
      Amazon SNS.

    - **customData** *(string) --*

      Any custom data associated with the trigger that will be included in the information sent to
      the target of the trigger.

    - **branches** *(list) --*

      The branches that will be included in the trigger configuration. If you specify an empty
      array, the trigger will apply to all branches.

      .. note::

        Although no content is required in the array, you must include the array itself.

      - *(string) --*

    - **events** *(list) --* **[REQUIRED]**

      The repository events that will cause the trigger to run actions in another service, such as
      sending a notification through Amazon SNS.

      .. note::

        The valid value "all" cannot be used with any other values.

      - *(string) --*
    """


_ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef = TypedDict(
    "_ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef",
    {"trigger": str, "failureMessage": str},
    total=False,
)


class ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef(
    _ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef
):
    """
    Type definition for `ClientTestRepositoryTriggersResponse` `failedExecutions`

    A trigger failed to run.

    - **trigger** *(string) --*

      The name of the trigger that did not run.

    - **failureMessage** *(string) --*

      Additional message information about the trigger that did not run.
    """


_ClientTestRepositoryTriggersResponseTypeDef = TypedDict(
    "_ClientTestRepositoryTriggersResponseTypeDef",
    {
        "successfulExecutions": List[str],
        "failedExecutions": List[
            ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef
        ],
    },
    total=False,
)


class ClientTestRepositoryTriggersResponseTypeDef(
    _ClientTestRepositoryTriggersResponseTypeDef
):
    """
    Type definition for `ClientTestRepositoryTriggers` `Response`

    Represents the output of a test repository triggers operation.

    - **successfulExecutions** *(list) --*

      The list of triggers that were successfully tested. This list provides the names of the
      triggers that were successfully tested, separated by commas.

      - *(string) --*

    - **failedExecutions** *(list) --*

      The list of triggers that were not able to be tested. This list provides the names of the
      triggers that could not be tested, separated by commas.

      - *(dict) --*

        A trigger failed to run.

        - **trigger** *(string) --*

          The name of the trigger that did not run.

        - **failureMessage** *(string) --*

          Additional message information about the trigger that did not run.
    """


_RequiredClientTestRepositoryTriggerstriggersTypeDef = TypedDict(
    "_RequiredClientTestRepositoryTriggerstriggersTypeDef",
    {"name": str, "destinationArn": str, "events": List[str]},
)
_OptionalClientTestRepositoryTriggerstriggersTypeDef = TypedDict(
    "_OptionalClientTestRepositoryTriggerstriggersTypeDef",
    {"customData": str, "branches": List[str]},
    total=False,
)


class ClientTestRepositoryTriggerstriggersTypeDef(
    _RequiredClientTestRepositoryTriggerstriggersTypeDef,
    _OptionalClientTestRepositoryTriggerstriggersTypeDef,
):
    """
    Type definition for `ClientTestRepositoryTriggers` `triggers`

    Information about a trigger for a repository.

    - **name** *(string) --* **[REQUIRED]**

      The name of the trigger.

    - **destinationArn** *(string) --* **[REQUIRED]**

      The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in
      Amazon SNS.

    - **customData** *(string) --*

      Any custom data associated with the trigger that will be included in the information sent to
      the target of the trigger.

    - **branches** *(list) --*

      The branches that will be included in the trigger configuration. If you specify an empty
      array, the trigger will apply to all branches.

      .. note::

        Although no content is required in the array, you must include the array itself.

      - *(string) --*

    - **events** *(list) --* **[REQUIRED]**

      The repository events that will cause the trigger to run actions in another service, such as
      sending a notification through Amazon SNS.

      .. note::

        The valid value "all" cannot be used with any other values.

      - *(string) --*
    """


_ClientUpdateCommentResponsecommentTypeDef = TypedDict(
    "_ClientUpdateCommentResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientUpdateCommentResponsecommentTypeDef(
    _ClientUpdateCommentResponsecommentTypeDef
):
    """
    Type definition for `ClientUpdateCommentResponse` `comment`

    Information about the updated comment.

    - **commentId** *(string) --*

      The system-generated comment ID.

    - **content** *(string) --*

      The content of the comment.

    - **inReplyTo** *(string) --*

      The ID of the comment for which this comment is a reply, if any.

    - **creationDate** *(datetime) --*

      The date and time the comment was created, in timestamp format.

    - **lastModifiedDate** *(datetime) --*

      The date and time the comment was most recently modified, in timestamp format.

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the person who posted the comment.

    - **deleted** *(boolean) --*

      A Boolean value indicating whether the comment has been deleted.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientUpdateCommentResponseTypeDef = TypedDict(
    "_ClientUpdateCommentResponseTypeDef",
    {"comment": ClientUpdateCommentResponsecommentTypeDef},
    total=False,
)


class ClientUpdateCommentResponseTypeDef(_ClientUpdateCommentResponseTypeDef):
    """
    Type definition for `ClientUpdateComment` `Response`

    - **comment** *(dict) --*

      Information about the updated comment.

      - **commentId** *(string) --*

        The system-generated comment ID.

      - **content** *(string) --*

        The content of the comment.

      - **inReplyTo** *(string) --*

        The ID of the comment for which this comment is a reply, if any.

      - **creationDate** *(datetime) --*

        The date and time the comment was created, in timestamp format.

      - **lastModifiedDate** *(datetime) --*

        The date and time the comment was most recently modified, in timestamp format.

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the person who posted the comment.

      - **deleted** *(boolean) --*

        A Boolean value indicating whether the comment has been deleted.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {"isMerged": bool, "mergedBy": str, "mergeCommitId": str, "mergeOption": str},
    total=False,
)


class ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    """
    Type definition for `ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargets` `mergeMetadata`

    Returns metadata about the state of the merge, including whether the merge has been
    made.

    - **isMerged** *(boolean) --*

      A Boolean value indicating whether the merge has been made.

    - **mergedBy** *(string) --*

      The Amazon Resource Name (ARN) of the user who merged the branches.

    - **mergeCommitId** *(string) --*

      The commit ID for the merge commit, if any.

    - **mergeOption** *(string) --*

      The merge strategy used in the merge.
    """


_ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef(
    _ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef
):
    """
    Type definition for `ClientUpdatePullRequestDescriptionResponsepullRequest` `pullRequestTargets`

    Returns information about a pull request target.

    - **repositoryName** *(string) --*

      The name of the repository that contains the pull request source and destination
      branches.

    - **sourceReference** *(string) --*

      The branch of the repository that contains the changes for the pull request. Also known
      as the source branch.

    - **destinationReference** *(string) --*

      The branch of the repository where the pull request changes will be merged into. Also
      known as the destination branch.

    - **destinationCommit** *(string) --*

      The full commit ID that is the tip of the destination branch. This is the commit where
      the pull request was or will be merged.

    - **sourceCommit** *(string) --*

      The full commit ID of the tip of the source branch used to create the pull request. If
      the pull request branch is updated by a push while the pull request is open, the commit
      ID will change to reflect the new tip of the branch.

    - **mergeBase** *(string) --*

      The commit ID of the most recent commit that the source branch and the destination
      branch have in common.

    - **mergeMetadata** *(dict) --*

      Returns metadata about the state of the merge, including whether the merge has been
      made.

      - **isMerged** *(boolean) --*

        A Boolean value indicating whether the merge has been made.

      - **mergedBy** *(string) --*

        The Amazon Resource Name (ARN) of the user who merged the branches.

      - **mergeCommitId** *(string) --*

        The commit ID for the merge commit, if any.

      - **mergeOption** *(string) --*

        The merge strategy used in the merge.
    """


_ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef = TypedDict(
    "_ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": str,
        "authorArn": str,
        "pullRequestTargets": List[
            ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
    },
    total=False,
)


class ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef(
    _ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef
):
    """
    Type definition for `ClientUpdatePullRequestDescriptionResponse` `pullRequest`

    Information about the updated pull request.

    - **pullRequestId** *(string) --*

      The system-generated ID of the pull request.

    - **title** *(string) --*

      The user-defined title of the pull request. This title is displayed in the list of pull
      requests to other users of the repository.

    - **description** *(string) --*

      The user-defined description of the pull request. This description can be used to clarify
      what should be reviewed and other details of the request.

    - **lastActivityDate** *(datetime) --*

      The day and time of the last user or system activity on the pull request, in timestamp
      format.

    - **creationDate** *(datetime) --*

      The date and time the pull request was originally created, in timestamp format.

    - **pullRequestStatus** *(string) --*

      The status of the pull request. Pull request status can only change from ``OPEN`` to
      ``CLOSED`` .

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the user who created the pull request.

    - **pullRequestTargets** *(list) --*

      The targets of the pull request, including the source branch and destination branch for the
      pull request.

      - *(dict) --*

        Returns information about a pull request target.

        - **repositoryName** *(string) --*

          The name of the repository that contains the pull request source and destination
          branches.

        - **sourceReference** *(string) --*

          The branch of the repository that contains the changes for the pull request. Also known
          as the source branch.

        - **destinationReference** *(string) --*

          The branch of the repository where the pull request changes will be merged into. Also
          known as the destination branch.

        - **destinationCommit** *(string) --*

          The full commit ID that is the tip of the destination branch. This is the commit where
          the pull request was or will be merged.

        - **sourceCommit** *(string) --*

          The full commit ID of the tip of the source branch used to create the pull request. If
          the pull request branch is updated by a push while the pull request is open, the commit
          ID will change to reflect the new tip of the branch.

        - **mergeBase** *(string) --*

          The commit ID of the most recent commit that the source branch and the destination
          branch have in common.

        - **mergeMetadata** *(dict) --*

          Returns metadata about the state of the merge, including whether the merge has been
          made.

          - **isMerged** *(boolean) --*

            A Boolean value indicating whether the merge has been made.

          - **mergedBy** *(string) --*

            The Amazon Resource Name (ARN) of the user who merged the branches.

          - **mergeCommitId** *(string) --*

            The commit ID for the merge commit, if any.

          - **mergeOption** *(string) --*

            The merge strategy used in the merge.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientUpdatePullRequestDescriptionResponseTypeDef = TypedDict(
    "_ClientUpdatePullRequestDescriptionResponseTypeDef",
    {"pullRequest": ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef},
    total=False,
)


class ClientUpdatePullRequestDescriptionResponseTypeDef(
    _ClientUpdatePullRequestDescriptionResponseTypeDef
):
    """
    Type definition for `ClientUpdatePullRequestDescription` `Response`

    - **pullRequest** *(dict) --*

      Information about the updated pull request.

      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.

      - **title** *(string) --*

        The user-defined title of the pull request. This title is displayed in the list of pull
        requests to other users of the repository.

      - **description** *(string) --*

        The user-defined description of the pull request. This description can be used to clarify
        what should be reviewed and other details of the request.

      - **lastActivityDate** *(datetime) --*

        The day and time of the last user or system activity on the pull request, in timestamp
        format.

      - **creationDate** *(datetime) --*

        The date and time the pull request was originally created, in timestamp format.

      - **pullRequestStatus** *(string) --*

        The status of the pull request. Pull request status can only change from ``OPEN`` to
        ``CLOSED`` .

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the user who created the pull request.

      - **pullRequestTargets** *(list) --*

        The targets of the pull request, including the source branch and destination branch for the
        pull request.

        - *(dict) --*

          Returns information about a pull request target.

          - **repositoryName** *(string) --*

            The name of the repository that contains the pull request source and destination
            branches.

          - **sourceReference** *(string) --*

            The branch of the repository that contains the changes for the pull request. Also known
            as the source branch.

          - **destinationReference** *(string) --*

            The branch of the repository where the pull request changes will be merged into. Also
            known as the destination branch.

          - **destinationCommit** *(string) --*

            The full commit ID that is the tip of the destination branch. This is the commit where
            the pull request was or will be merged.

          - **sourceCommit** *(string) --*

            The full commit ID of the tip of the source branch used to create the pull request. If
            the pull request branch is updated by a push while the pull request is open, the commit
            ID will change to reflect the new tip of the branch.

          - **mergeBase** *(string) --*

            The commit ID of the most recent commit that the source branch and the destination
            branch have in common.

          - **mergeMetadata** *(dict) --*

            Returns metadata about the state of the merge, including whether the merge has been
            made.

            - **isMerged** *(boolean) --*

              A Boolean value indicating whether the merge has been made.

            - **mergedBy** *(string) --*

              The Amazon Resource Name (ARN) of the user who merged the branches.

            - **mergeCommitId** *(string) --*

              The commit ID for the merge commit, if any.

            - **mergeOption** *(string) --*

              The merge strategy used in the merge.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {"isMerged": bool, "mergedBy": str, "mergeCommitId": str, "mergeOption": str},
    total=False,
)


class ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    """
    Type definition for `ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargets` `mergeMetadata`

    Returns metadata about the state of the merge, including whether the merge has been
    made.

    - **isMerged** *(boolean) --*

      A Boolean value indicating whether the merge has been made.

    - **mergedBy** *(string) --*

      The Amazon Resource Name (ARN) of the user who merged the branches.

    - **mergeCommitId** *(string) --*

      The commit ID for the merge commit, if any.

    - **mergeOption** *(string) --*

      The merge strategy used in the merge.
    """


_ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef(
    _ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef
):
    """
    Type definition for `ClientUpdatePullRequestStatusResponsepullRequest` `pullRequestTargets`

    Returns information about a pull request target.

    - **repositoryName** *(string) --*

      The name of the repository that contains the pull request source and destination
      branches.

    - **sourceReference** *(string) --*

      The branch of the repository that contains the changes for the pull request. Also known
      as the source branch.

    - **destinationReference** *(string) --*

      The branch of the repository where the pull request changes will be merged into. Also
      known as the destination branch.

    - **destinationCommit** *(string) --*

      The full commit ID that is the tip of the destination branch. This is the commit where
      the pull request was or will be merged.

    - **sourceCommit** *(string) --*

      The full commit ID of the tip of the source branch used to create the pull request. If
      the pull request branch is updated by a push while the pull request is open, the commit
      ID will change to reflect the new tip of the branch.

    - **mergeBase** *(string) --*

      The commit ID of the most recent commit that the source branch and the destination
      branch have in common.

    - **mergeMetadata** *(dict) --*

      Returns metadata about the state of the merge, including whether the merge has been
      made.

      - **isMerged** *(boolean) --*

        A Boolean value indicating whether the merge has been made.

      - **mergedBy** *(string) --*

        The Amazon Resource Name (ARN) of the user who merged the branches.

      - **mergeCommitId** *(string) --*

        The commit ID for the merge commit, if any.

      - **mergeOption** *(string) --*

        The merge strategy used in the merge.
    """


_ClientUpdatePullRequestStatusResponsepullRequestTypeDef = TypedDict(
    "_ClientUpdatePullRequestStatusResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": str,
        "authorArn": str,
        "pullRequestTargets": List[
            ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
    },
    total=False,
)


class ClientUpdatePullRequestStatusResponsepullRequestTypeDef(
    _ClientUpdatePullRequestStatusResponsepullRequestTypeDef
):
    """
    Type definition for `ClientUpdatePullRequestStatusResponse` `pullRequest`

    Information about the pull request.

    - **pullRequestId** *(string) --*

      The system-generated ID of the pull request.

    - **title** *(string) --*

      The user-defined title of the pull request. This title is displayed in the list of pull
      requests to other users of the repository.

    - **description** *(string) --*

      The user-defined description of the pull request. This description can be used to clarify
      what should be reviewed and other details of the request.

    - **lastActivityDate** *(datetime) --*

      The day and time of the last user or system activity on the pull request, in timestamp
      format.

    - **creationDate** *(datetime) --*

      The date and time the pull request was originally created, in timestamp format.

    - **pullRequestStatus** *(string) --*

      The status of the pull request. Pull request status can only change from ``OPEN`` to
      ``CLOSED`` .

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the user who created the pull request.

    - **pullRequestTargets** *(list) --*

      The targets of the pull request, including the source branch and destination branch for the
      pull request.

      - *(dict) --*

        Returns information about a pull request target.

        - **repositoryName** *(string) --*

          The name of the repository that contains the pull request source and destination
          branches.

        - **sourceReference** *(string) --*

          The branch of the repository that contains the changes for the pull request. Also known
          as the source branch.

        - **destinationReference** *(string) --*

          The branch of the repository where the pull request changes will be merged into. Also
          known as the destination branch.

        - **destinationCommit** *(string) --*

          The full commit ID that is the tip of the destination branch. This is the commit where
          the pull request was or will be merged.

        - **sourceCommit** *(string) --*

          The full commit ID of the tip of the source branch used to create the pull request. If
          the pull request branch is updated by a push while the pull request is open, the commit
          ID will change to reflect the new tip of the branch.

        - **mergeBase** *(string) --*

          The commit ID of the most recent commit that the source branch and the destination
          branch have in common.

        - **mergeMetadata** *(dict) --*

          Returns metadata about the state of the merge, including whether the merge has been
          made.

          - **isMerged** *(boolean) --*

            A Boolean value indicating whether the merge has been made.

          - **mergedBy** *(string) --*

            The Amazon Resource Name (ARN) of the user who merged the branches.

          - **mergeCommitId** *(string) --*

            The commit ID for the merge commit, if any.

          - **mergeOption** *(string) --*

            The merge strategy used in the merge.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientUpdatePullRequestStatusResponseTypeDef = TypedDict(
    "_ClientUpdatePullRequestStatusResponseTypeDef",
    {"pullRequest": ClientUpdatePullRequestStatusResponsepullRequestTypeDef},
    total=False,
)


class ClientUpdatePullRequestStatusResponseTypeDef(
    _ClientUpdatePullRequestStatusResponseTypeDef
):
    """
    Type definition for `ClientUpdatePullRequestStatus` `Response`

    - **pullRequest** *(dict) --*

      Information about the pull request.

      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.

      - **title** *(string) --*

        The user-defined title of the pull request. This title is displayed in the list of pull
        requests to other users of the repository.

      - **description** *(string) --*

        The user-defined description of the pull request. This description can be used to clarify
        what should be reviewed and other details of the request.

      - **lastActivityDate** *(datetime) --*

        The day and time of the last user or system activity on the pull request, in timestamp
        format.

      - **creationDate** *(datetime) --*

        The date and time the pull request was originally created, in timestamp format.

      - **pullRequestStatus** *(string) --*

        The status of the pull request. Pull request status can only change from ``OPEN`` to
        ``CLOSED`` .

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the user who created the pull request.

      - **pullRequestTargets** *(list) --*

        The targets of the pull request, including the source branch and destination branch for the
        pull request.

        - *(dict) --*

          Returns information about a pull request target.

          - **repositoryName** *(string) --*

            The name of the repository that contains the pull request source and destination
            branches.

          - **sourceReference** *(string) --*

            The branch of the repository that contains the changes for the pull request. Also known
            as the source branch.

          - **destinationReference** *(string) --*

            The branch of the repository where the pull request changes will be merged into. Also
            known as the destination branch.

          - **destinationCommit** *(string) --*

            The full commit ID that is the tip of the destination branch. This is the commit where
            the pull request was or will be merged.

          - **sourceCommit** *(string) --*

            The full commit ID of the tip of the source branch used to create the pull request. If
            the pull request branch is updated by a push while the pull request is open, the commit
            ID will change to reflect the new tip of the branch.

          - **mergeBase** *(string) --*

            The commit ID of the most recent commit that the source branch and the destination
            branch have in common.

          - **mergeMetadata** *(dict) --*

            Returns metadata about the state of the merge, including whether the merge has been
            made.

            - **isMerged** *(boolean) --*

              A Boolean value indicating whether the merge has been made.

            - **mergedBy** *(string) --*

              The Amazon Resource Name (ARN) of the user who merged the branches.

            - **mergeCommitId** *(string) --*

              The commit ID for the merge commit, if any.

            - **mergeOption** *(string) --*

              The merge strategy used in the merge.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {"isMerged": bool, "mergedBy": str, "mergeCommitId": str, "mergeOption": str},
    total=False,
)


class ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    """
    Type definition for `ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargets` `mergeMetadata`

    Returns metadata about the state of the merge, including whether the merge has been
    made.

    - **isMerged** *(boolean) --*

      A Boolean value indicating whether the merge has been made.

    - **mergedBy** *(string) --*

      The Amazon Resource Name (ARN) of the user who merged the branches.

    - **mergeCommitId** *(string) --*

      The commit ID for the merge commit, if any.

    - **mergeOption** *(string) --*

      The merge strategy used in the merge.
    """


_ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef(
    _ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef
):
    """
    Type definition for `ClientUpdatePullRequestTitleResponsepullRequest` `pullRequestTargets`

    Returns information about a pull request target.

    - **repositoryName** *(string) --*

      The name of the repository that contains the pull request source and destination
      branches.

    - **sourceReference** *(string) --*

      The branch of the repository that contains the changes for the pull request. Also known
      as the source branch.

    - **destinationReference** *(string) --*

      The branch of the repository where the pull request changes will be merged into. Also
      known as the destination branch.

    - **destinationCommit** *(string) --*

      The full commit ID that is the tip of the destination branch. This is the commit where
      the pull request was or will be merged.

    - **sourceCommit** *(string) --*

      The full commit ID of the tip of the source branch used to create the pull request. If
      the pull request branch is updated by a push while the pull request is open, the commit
      ID will change to reflect the new tip of the branch.

    - **mergeBase** *(string) --*

      The commit ID of the most recent commit that the source branch and the destination
      branch have in common.

    - **mergeMetadata** *(dict) --*

      Returns metadata about the state of the merge, including whether the merge has been
      made.

      - **isMerged** *(boolean) --*

        A Boolean value indicating whether the merge has been made.

      - **mergedBy** *(string) --*

        The Amazon Resource Name (ARN) of the user who merged the branches.

      - **mergeCommitId** *(string) --*

        The commit ID for the merge commit, if any.

      - **mergeOption** *(string) --*

        The merge strategy used in the merge.
    """


_ClientUpdatePullRequestTitleResponsepullRequestTypeDef = TypedDict(
    "_ClientUpdatePullRequestTitleResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": str,
        "authorArn": str,
        "pullRequestTargets": List[
            ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
    },
    total=False,
)


class ClientUpdatePullRequestTitleResponsepullRequestTypeDef(
    _ClientUpdatePullRequestTitleResponsepullRequestTypeDef
):
    """
    Type definition for `ClientUpdatePullRequestTitleResponse` `pullRequest`

    Information about the updated pull request.

    - **pullRequestId** *(string) --*

      The system-generated ID of the pull request.

    - **title** *(string) --*

      The user-defined title of the pull request. This title is displayed in the list of pull
      requests to other users of the repository.

    - **description** *(string) --*

      The user-defined description of the pull request. This description can be used to clarify
      what should be reviewed and other details of the request.

    - **lastActivityDate** *(datetime) --*

      The day and time of the last user or system activity on the pull request, in timestamp
      format.

    - **creationDate** *(datetime) --*

      The date and time the pull request was originally created, in timestamp format.

    - **pullRequestStatus** *(string) --*

      The status of the pull request. Pull request status can only change from ``OPEN`` to
      ``CLOSED`` .

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the user who created the pull request.

    - **pullRequestTargets** *(list) --*

      The targets of the pull request, including the source branch and destination branch for the
      pull request.

      - *(dict) --*

        Returns information about a pull request target.

        - **repositoryName** *(string) --*

          The name of the repository that contains the pull request source and destination
          branches.

        - **sourceReference** *(string) --*

          The branch of the repository that contains the changes for the pull request. Also known
          as the source branch.

        - **destinationReference** *(string) --*

          The branch of the repository where the pull request changes will be merged into. Also
          known as the destination branch.

        - **destinationCommit** *(string) --*

          The full commit ID that is the tip of the destination branch. This is the commit where
          the pull request was or will be merged.

        - **sourceCommit** *(string) --*

          The full commit ID of the tip of the source branch used to create the pull request. If
          the pull request branch is updated by a push while the pull request is open, the commit
          ID will change to reflect the new tip of the branch.

        - **mergeBase** *(string) --*

          The commit ID of the most recent commit that the source branch and the destination
          branch have in common.

        - **mergeMetadata** *(dict) --*

          Returns metadata about the state of the merge, including whether the merge has been
          made.

          - **isMerged** *(boolean) --*

            A Boolean value indicating whether the merge has been made.

          - **mergedBy** *(string) --*

            The Amazon Resource Name (ARN) of the user who merged the branches.

          - **mergeCommitId** *(string) --*

            The commit ID for the merge commit, if any.

          - **mergeOption** *(string) --*

            The merge strategy used in the merge.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures the
      request cannot be repeated with a changed parameter. If a request is received with the same
      parameters and a token is included, the request will return information about the initial
      request that used that token.
    """


_ClientUpdatePullRequestTitleResponseTypeDef = TypedDict(
    "_ClientUpdatePullRequestTitleResponseTypeDef",
    {"pullRequest": ClientUpdatePullRequestTitleResponsepullRequestTypeDef},
    total=False,
)


class ClientUpdatePullRequestTitleResponseTypeDef(
    _ClientUpdatePullRequestTitleResponseTypeDef
):
    """
    Type definition for `ClientUpdatePullRequestTitle` `Response`

    - **pullRequest** *(dict) --*

      Information about the updated pull request.

      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.

      - **title** *(string) --*

        The user-defined title of the pull request. This title is displayed in the list of pull
        requests to other users of the repository.

      - **description** *(string) --*

        The user-defined description of the pull request. This description can be used to clarify
        what should be reviewed and other details of the request.

      - **lastActivityDate** *(datetime) --*

        The day and time of the last user or system activity on the pull request, in timestamp
        format.

      - **creationDate** *(datetime) --*

        The date and time the pull request was originally created, in timestamp format.

      - **pullRequestStatus** *(string) --*

        The status of the pull request. Pull request status can only change from ``OPEN`` to
        ``CLOSED`` .

      - **authorArn** *(string) --*

        The Amazon Resource Name (ARN) of the user who created the pull request.

      - **pullRequestTargets** *(list) --*

        The targets of the pull request, including the source branch and destination branch for the
        pull request.

        - *(dict) --*

          Returns information about a pull request target.

          - **repositoryName** *(string) --*

            The name of the repository that contains the pull request source and destination
            branches.

          - **sourceReference** *(string) --*

            The branch of the repository that contains the changes for the pull request. Also known
            as the source branch.

          - **destinationReference** *(string) --*

            The branch of the repository where the pull request changes will be merged into. Also
            known as the destination branch.

          - **destinationCommit** *(string) --*

            The full commit ID that is the tip of the destination branch. This is the commit where
            the pull request was or will be merged.

          - **sourceCommit** *(string) --*

            The full commit ID of the tip of the source branch used to create the pull request. If
            the pull request branch is updated by a push while the pull request is open, the commit
            ID will change to reflect the new tip of the branch.

          - **mergeBase** *(string) --*

            The commit ID of the most recent commit that the source branch and the destination
            branch have in common.

          - **mergeMetadata** *(dict) --*

            Returns metadata about the state of the merge, including whether the merge has been
            made.

            - **isMerged** *(boolean) --*

              A Boolean value indicating whether the merge has been made.

            - **mergedBy** *(string) --*

              The Amazon Resource Name (ARN) of the user who merged the branches.

            - **mergeCommitId** *(string) --*

              The commit ID for the merge commit, if any.

            - **mergeOption** *(string) --*

              The merge strategy used in the merge.

      - **clientRequestToken** *(string) --*

        A unique, client-generated idempotency token that when provided in a request, ensures the
        request cannot be repeated with a changed parameter. If a request is received with the same
        parameters and a token is included, the request will return information about the initial
        request that used that token.
    """


_DescribePullRequestEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribePullRequestEventsPaginatePaginationConfigTypeDef(
    _DescribePullRequestEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribePullRequestEventsPaginate` `PaginationConfig`

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


_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "sourceCommitId": str,
        "destinationCommitId": str,
        "mergeBase": str,
    },
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef
):
    """
    Type definition for `DescribePullRequestEventsPaginateResponsepullRequestEvents` `pullRequestCreatedEventMetadata`

    Information about the source and destination branches for the pull request.

    - **repositoryName** *(string) --*

      The name of the repository where the pull request was created.

    - **sourceCommitId** *(string) --*

      The commit ID on the source branch used when the pull request was created.

    - **destinationCommitId** *(string) --*

      The commit ID of the tip of the branch specified as the destination branch when the
      pull request was created.

    - **mergeBase** *(string) --*

      The commit ID of the most recent commit that the source branch and the destination
      branch have in common.
    """


_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef",
    {"isMerged": bool, "mergedBy": str, "mergeCommitId": str, "mergeOption": str},
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef
):
    """
    Type definition for `DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadata` `mergeMetadata`

    Information about the merge state change event.

    - **isMerged** *(boolean) --*

      A Boolean value indicating whether the merge has been made.

    - **mergedBy** *(string) --*

      The Amazon Resource Name (ARN) of the user who merged the branches.

    - **mergeCommitId** *(string) --*

      The commit ID for the merge commit, if any.

    - **mergeOption** *(string) --*

      The merge strategy used in the merge.
    """


_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "destinationReference": str,
        "mergeMetadata": DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef,
    },
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef
):
    """
    Type definition for `DescribePullRequestEventsPaginateResponsepullRequestEvents` `pullRequestMergedStateChangedEventMetadata`

    Information about the change in mergability state for the pull request event.

    - **repositoryName** *(string) --*

      The name of the repository where the pull request was created.

    - **destinationReference** *(string) --*

      The name of the branch that the pull request will be merged into.

    - **mergeMetadata** *(dict) --*

      Information about the merge state change event.

      - **isMerged** *(boolean) --*

        A Boolean value indicating whether the merge has been made.

      - **mergedBy** *(string) --*

        The Amazon Resource Name (ARN) of the user who merged the branches.

      - **mergeCommitId** *(string) --*

        The commit ID for the merge commit, if any.

      - **mergeOption** *(string) --*

        The merge strategy used in the merge.
    """


_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "mergeBase": str,
    },
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef
):
    """
    Type definition for `DescribePullRequestEventsPaginateResponsepullRequestEvents` `pullRequestSourceReferenceUpdatedEventMetadata`

    Information about the updated source branch for the pull request event.

    - **repositoryName** *(string) --*

      The name of the repository where the pull request was updated.

    - **beforeCommitId** *(string) --*

      The full commit ID of the commit in the destination branch that was the tip of the
      branch at the time the pull request was updated.

    - **afterCommitId** *(string) --*

      The full commit ID of the commit in the source branch that was the tip of the branch at
      the time the pull request was updated.

    - **mergeBase** *(string) --*

      The commit ID of the most recent commit that the source branch and the destination
      branch have in common.
    """


_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef",
    {"pullRequestStatus": str},
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef
):
    """
    Type definition for `DescribePullRequestEventsPaginateResponsepullRequestEvents` `pullRequestStatusChangedEventMetadata`

    Information about the change in status for the pull request event.

    - **pullRequestStatus** *(string) --*

      The changed status of the pull request.
    """


_DescribePullRequestEventsPaginateResponsepullRequestEventsTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventsTypeDef",
    {
        "pullRequestId": str,
        "eventDate": datetime,
        "pullRequestEventType": str,
        "actorArn": str,
        "pullRequestCreatedEventMetadata": DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef,
        "pullRequestStatusChangedEventMetadata": DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef,
        "pullRequestSourceReferenceUpdatedEventMetadata": DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef,
        "pullRequestMergedStateChangedEventMetadata": DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef,
    },
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventsTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventsTypeDef
):
    """
    Type definition for `DescribePullRequestEventsPaginateResponse` `pullRequestEvents`

    Returns information about a pull request event.

    - **pullRequestId** *(string) --*

      The system-generated ID of the pull request.

    - **eventDate** *(datetime) --*

      The day and time of the pull request event, in timestamp format.

    - **pullRequestEventType** *(string) --*

      The type of the pull request event, for example a status change event
      (PULL_REQUEST_STATUS_CHANGED) or update event (PULL_REQUEST_SOURCE_REFERENCE_UPDATED).

    - **actorArn** *(string) --*

      The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples
      include updating the pull request with additional commits or changing the status of a
      pull request.

    - **pullRequestCreatedEventMetadata** *(dict) --*

      Information about the source and destination branches for the pull request.

      - **repositoryName** *(string) --*

        The name of the repository where the pull request was created.

      - **sourceCommitId** *(string) --*

        The commit ID on the source branch used when the pull request was created.

      - **destinationCommitId** *(string) --*

        The commit ID of the tip of the branch specified as the destination branch when the
        pull request was created.

      - **mergeBase** *(string) --*

        The commit ID of the most recent commit that the source branch and the destination
        branch have in common.

    - **pullRequestStatusChangedEventMetadata** *(dict) --*

      Information about the change in status for the pull request event.

      - **pullRequestStatus** *(string) --*

        The changed status of the pull request.

    - **pullRequestSourceReferenceUpdatedEventMetadata** *(dict) --*

      Information about the updated source branch for the pull request event.

      - **repositoryName** *(string) --*

        The name of the repository where the pull request was updated.

      - **beforeCommitId** *(string) --*

        The full commit ID of the commit in the destination branch that was the tip of the
        branch at the time the pull request was updated.

      - **afterCommitId** *(string) --*

        The full commit ID of the commit in the source branch that was the tip of the branch at
        the time the pull request was updated.

      - **mergeBase** *(string) --*

        The commit ID of the most recent commit that the source branch and the destination
        branch have in common.

    - **pullRequestMergedStateChangedEventMetadata** *(dict) --*

      Information about the change in mergability state for the pull request event.

      - **repositoryName** *(string) --*

        The name of the repository where the pull request was created.

      - **destinationReference** *(string) --*

        The name of the branch that the pull request will be merged into.

      - **mergeMetadata** *(dict) --*

        Information about the merge state change event.

        - **isMerged** *(boolean) --*

          A Boolean value indicating whether the merge has been made.

        - **mergedBy** *(string) --*

          The Amazon Resource Name (ARN) of the user who merged the branches.

        - **mergeCommitId** *(string) --*

          The commit ID for the merge commit, if any.

        - **mergeOption** *(string) --*

          The merge strategy used in the merge.
    """


_DescribePullRequestEventsPaginateResponseTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponseTypeDef",
    {
        "pullRequestEvents": List[
            DescribePullRequestEventsPaginateResponsepullRequestEventsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribePullRequestEventsPaginateResponseTypeDef(
    _DescribePullRequestEventsPaginateResponseTypeDef
):
    """
    Type definition for `DescribePullRequestEventsPaginate` `Response`

    - **pullRequestEvents** *(list) --*

      Information about the pull request events.

      - *(dict) --*

        Returns information about a pull request event.

        - **pullRequestId** *(string) --*

          The system-generated ID of the pull request.

        - **eventDate** *(datetime) --*

          The day and time of the pull request event, in timestamp format.

        - **pullRequestEventType** *(string) --*

          The type of the pull request event, for example a status change event
          (PULL_REQUEST_STATUS_CHANGED) or update event (PULL_REQUEST_SOURCE_REFERENCE_UPDATED).

        - **actorArn** *(string) --*

          The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples
          include updating the pull request with additional commits or changing the status of a
          pull request.

        - **pullRequestCreatedEventMetadata** *(dict) --*

          Information about the source and destination branches for the pull request.

          - **repositoryName** *(string) --*

            The name of the repository where the pull request was created.

          - **sourceCommitId** *(string) --*

            The commit ID on the source branch used when the pull request was created.

          - **destinationCommitId** *(string) --*

            The commit ID of the tip of the branch specified as the destination branch when the
            pull request was created.

          - **mergeBase** *(string) --*

            The commit ID of the most recent commit that the source branch and the destination
            branch have in common.

        - **pullRequestStatusChangedEventMetadata** *(dict) --*

          Information about the change in status for the pull request event.

          - **pullRequestStatus** *(string) --*

            The changed status of the pull request.

        - **pullRequestSourceReferenceUpdatedEventMetadata** *(dict) --*

          Information about the updated source branch for the pull request event.

          - **repositoryName** *(string) --*

            The name of the repository where the pull request was updated.

          - **beforeCommitId** *(string) --*

            The full commit ID of the commit in the destination branch that was the tip of the
            branch at the time the pull request was updated.

          - **afterCommitId** *(string) --*

            The full commit ID of the commit in the source branch that was the tip of the branch at
            the time the pull request was updated.

          - **mergeBase** *(string) --*

            The commit ID of the most recent commit that the source branch and the destination
            branch have in common.

        - **pullRequestMergedStateChangedEventMetadata** *(dict) --*

          Information about the change in mergability state for the pull request event.

          - **repositoryName** *(string) --*

            The name of the repository where the pull request was created.

          - **destinationReference** *(string) --*

            The name of the branch that the pull request will be merged into.

          - **mergeMetadata** *(dict) --*

            Information about the merge state change event.

            - **isMerged** *(boolean) --*

              A Boolean value indicating whether the merge has been made.

            - **mergedBy** *(string) --*

              The Amazon Resource Name (ARN) of the user who merged the branches.

            - **mergeCommitId** *(string) --*

              The commit ID for the merge commit, if any.

            - **mergeOption** *(string) --*

              The merge strategy used in the merge.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetCommentsForComparedCommitPaginatePaginationConfigTypeDef = TypedDict(
    "_GetCommentsForComparedCommitPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetCommentsForComparedCommitPaginatePaginationConfigTypeDef(
    _GetCommentsForComparedCommitPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetCommentsForComparedCommitPaginate` `PaginationConfig`

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


_GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatacommentsTypeDef = TypedDict(
    "_GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatacommentsTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatacommentsTypeDef(
    _GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatacommentsTypeDef
):
    """
    Type definition for `GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitData` `comments`

    Returns information about a specific comment.

    - **commentId** *(string) --*

      The system-generated comment ID.

    - **content** *(string) --*

      The content of the comment.

    - **inReplyTo** *(string) --*

      The ID of the comment for which this comment is a reply, if any.

    - **creationDate** *(datetime) --*

      The date and time the comment was created, in timestamp format.

    - **lastModifiedDate** *(datetime) --*

      The date and time the comment was most recently modified, in timestamp format.

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the person who posted the comment.

    - **deleted** *(boolean) --*

      A Boolean value indicating whether the comment has been deleted.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures
      the request cannot be repeated with a changed parameter. If a request is received
      with the same parameters and a token is included, the request will return information
      about the initial request that used that token.
    """


_GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatalocationTypeDef = TypedDict(
    "_GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatalocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": str},
    total=False,
)


class GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatalocationTypeDef(
    _GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatalocationTypeDef
):
    """
    Type definition for `GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitData` `location`

    Location information about the comment on the comparison, including the file name, line
    number, and whether the version of the file where the comment was made is 'BEFORE' or
    'AFTER'.

    - **filePath** *(string) --*

      The name of the file being compared, including its extension and subdirectory, if any.

    - **filePosition** *(integer) --*

      The position of a change within a compared file, in line number format.

    - **relativeFileVersion** *(string) --*

      In a comparison of commits or a pull request, whether the change is in the 'before' or
      'after' of that comparison.
    """


_GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDataTypeDef = TypedDict(
    "_GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDataTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatalocationTypeDef,
        "comments": List[
            GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatacommentsTypeDef
        ],
    },
    total=False,
)


class GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDataTypeDef(
    _GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDataTypeDef
):
    """
    Type definition for `GetCommentsForComparedCommitPaginateResponse` `commentsForComparedCommitData`

    Returns information about comments on the comparison between two commits.

    - **repositoryName** *(string) --*

      The name of the repository that contains the compared commits.

    - **beforeCommitId** *(string) --*

      The full commit ID of the commit used to establish the 'before' of the comparison.

    - **afterCommitId** *(string) --*

      The full commit ID of the commit used to establish the 'after' of the comparison.

    - **beforeBlobId** *(string) --*

      The full blob ID of the commit used to establish the 'before' of the comparison.

    - **afterBlobId** *(string) --*

      The full blob ID of the commit used to establish the 'after' of the comparison.

    - **location** *(dict) --*

      Location information about the comment on the comparison, including the file name, line
      number, and whether the version of the file where the comment was made is 'BEFORE' or
      'AFTER'.

      - **filePath** *(string) --*

        The name of the file being compared, including its extension and subdirectory, if any.

      - **filePosition** *(integer) --*

        The position of a change within a compared file, in line number format.

      - **relativeFileVersion** *(string) --*

        In a comparison of commits or a pull request, whether the change is in the 'before' or
        'after' of that comparison.

    - **comments** *(list) --*

      An array of comment objects. Each comment object contains information about a comment on
      the comparison between commits.

      - *(dict) --*

        Returns information about a specific comment.

        - **commentId** *(string) --*

          The system-generated comment ID.

        - **content** *(string) --*

          The content of the comment.

        - **inReplyTo** *(string) --*

          The ID of the comment for which this comment is a reply, if any.

        - **creationDate** *(datetime) --*

          The date and time the comment was created, in timestamp format.

        - **lastModifiedDate** *(datetime) --*

          The date and time the comment was most recently modified, in timestamp format.

        - **authorArn** *(string) --*

          The Amazon Resource Name (ARN) of the person who posted the comment.

        - **deleted** *(boolean) --*

          A Boolean value indicating whether the comment has been deleted.

        - **clientRequestToken** *(string) --*

          A unique, client-generated idempotency token that when provided in a request, ensures
          the request cannot be repeated with a changed parameter. If a request is received
          with the same parameters and a token is included, the request will return information
          about the initial request that used that token.
    """


_GetCommentsForComparedCommitPaginateResponseTypeDef = TypedDict(
    "_GetCommentsForComparedCommitPaginateResponseTypeDef",
    {
        "commentsForComparedCommitData": List[
            GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDataTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetCommentsForComparedCommitPaginateResponseTypeDef(
    _GetCommentsForComparedCommitPaginateResponseTypeDef
):
    """
    Type definition for `GetCommentsForComparedCommitPaginate` `Response`

    - **commentsForComparedCommitData** *(list) --*

      A list of comment objects on the compared commit.

      - *(dict) --*

        Returns information about comments on the comparison between two commits.

        - **repositoryName** *(string) --*

          The name of the repository that contains the compared commits.

        - **beforeCommitId** *(string) --*

          The full commit ID of the commit used to establish the 'before' of the comparison.

        - **afterCommitId** *(string) --*

          The full commit ID of the commit used to establish the 'after' of the comparison.

        - **beforeBlobId** *(string) --*

          The full blob ID of the commit used to establish the 'before' of the comparison.

        - **afterBlobId** *(string) --*

          The full blob ID of the commit used to establish the 'after' of the comparison.

        - **location** *(dict) --*

          Location information about the comment on the comparison, including the file name, line
          number, and whether the version of the file where the comment was made is 'BEFORE' or
          'AFTER'.

          - **filePath** *(string) --*

            The name of the file being compared, including its extension and subdirectory, if any.

          - **filePosition** *(integer) --*

            The position of a change within a compared file, in line number format.

          - **relativeFileVersion** *(string) --*

            In a comparison of commits or a pull request, whether the change is in the 'before' or
            'after' of that comparison.

        - **comments** *(list) --*

          An array of comment objects. Each comment object contains information about a comment on
          the comparison between commits.

          - *(dict) --*

            Returns information about a specific comment.

            - **commentId** *(string) --*

              The system-generated comment ID.

            - **content** *(string) --*

              The content of the comment.

            - **inReplyTo** *(string) --*

              The ID of the comment for which this comment is a reply, if any.

            - **creationDate** *(datetime) --*

              The date and time the comment was created, in timestamp format.

            - **lastModifiedDate** *(datetime) --*

              The date and time the comment was most recently modified, in timestamp format.

            - **authorArn** *(string) --*

              The Amazon Resource Name (ARN) of the person who posted the comment.

            - **deleted** *(boolean) --*

              A Boolean value indicating whether the comment has been deleted.

            - **clientRequestToken** *(string) --*

              A unique, client-generated idempotency token that when provided in a request, ensures
              the request cannot be repeated with a changed parameter. If a request is received
              with the same parameters and a token is included, the request will return information
              about the initial request that used that token.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetCommentsForPullRequestPaginatePaginationConfigTypeDef = TypedDict(
    "_GetCommentsForPullRequestPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetCommentsForPullRequestPaginatePaginationConfigTypeDef(
    _GetCommentsForPullRequestPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetCommentsForPullRequestPaginate` `PaginationConfig`

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


_GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatacommentsTypeDef = TypedDict(
    "_GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatacommentsTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatacommentsTypeDef(
    _GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatacommentsTypeDef
):
    """
    Type definition for `GetCommentsForPullRequestPaginateResponsecommentsForPullRequestData` `comments`

    Returns information about a specific comment.

    - **commentId** *(string) --*

      The system-generated comment ID.

    - **content** *(string) --*

      The content of the comment.

    - **inReplyTo** *(string) --*

      The ID of the comment for which this comment is a reply, if any.

    - **creationDate** *(datetime) --*

      The date and time the comment was created, in timestamp format.

    - **lastModifiedDate** *(datetime) --*

      The date and time the comment was most recently modified, in timestamp format.

    - **authorArn** *(string) --*

      The Amazon Resource Name (ARN) of the person who posted the comment.

    - **deleted** *(boolean) --*

      A Boolean value indicating whether the comment has been deleted.

    - **clientRequestToken** *(string) --*

      A unique, client-generated idempotency token that when provided in a request, ensures
      the request cannot be repeated with a changed parameter. If a request is received
      with the same parameters and a token is included, the request will return information
      about the initial request that used that token.
    """


_GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatalocationTypeDef = TypedDict(
    "_GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatalocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": str},
    total=False,
)


class GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatalocationTypeDef(
    _GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatalocationTypeDef
):
    """
    Type definition for `GetCommentsForPullRequestPaginateResponsecommentsForPullRequestData` `location`

    Location information about the comment on the pull request, including the file name, line
    number, and whether the version of the file where the comment was made is 'BEFORE'
    (destination branch) or 'AFTER' (source branch).

    - **filePath** *(string) --*

      The name of the file being compared, including its extension and subdirectory, if any.

    - **filePosition** *(integer) --*

      The position of a change within a compared file, in line number format.

    - **relativeFileVersion** *(string) --*

      In a comparison of commits or a pull request, whether the change is in the 'before' or
      'after' of that comparison.
    """


_GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDataTypeDef = TypedDict(
    "_GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDataTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatalocationTypeDef,
        "comments": List[
            GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatacommentsTypeDef
        ],
    },
    total=False,
)


class GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDataTypeDef(
    _GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDataTypeDef
):
    """
    Type definition for `GetCommentsForPullRequestPaginateResponse` `commentsForPullRequestData`

    Returns information about comments on a pull request.

    - **pullRequestId** *(string) --*

      The system-generated ID of the pull request.

    - **repositoryName** *(string) --*

      The name of the repository that contains the pull request.

    - **beforeCommitId** *(string) --*

      The full commit ID of the commit that was the tip of the destination branch when the pull
      request was created. This commit will be superceded by the after commit in the source
      branch when and if you merge the source branch into the destination branch.

    - **afterCommitId** *(string) --*

      he full commit ID of the commit that was the tip of the source branch at the time the
      comment was made.

    - **beforeBlobId** *(string) --*

      The full blob ID of the file on which you want to comment on the destination commit.

    - **afterBlobId** *(string) --*

      The full blob ID of the file on which you want to comment on the source commit.

    - **location** *(dict) --*

      Location information about the comment on the pull request, including the file name, line
      number, and whether the version of the file where the comment was made is 'BEFORE'
      (destination branch) or 'AFTER' (source branch).

      - **filePath** *(string) --*

        The name of the file being compared, including its extension and subdirectory, if any.

      - **filePosition** *(integer) --*

        The position of a change within a compared file, in line number format.

      - **relativeFileVersion** *(string) --*

        In a comparison of commits or a pull request, whether the change is in the 'before' or
        'after' of that comparison.

    - **comments** *(list) --*

      An array of comment objects. Each comment object contains information about a comment on
      the pull request.

      - *(dict) --*

        Returns information about a specific comment.

        - **commentId** *(string) --*

          The system-generated comment ID.

        - **content** *(string) --*

          The content of the comment.

        - **inReplyTo** *(string) --*

          The ID of the comment for which this comment is a reply, if any.

        - **creationDate** *(datetime) --*

          The date and time the comment was created, in timestamp format.

        - **lastModifiedDate** *(datetime) --*

          The date and time the comment was most recently modified, in timestamp format.

        - **authorArn** *(string) --*

          The Amazon Resource Name (ARN) of the person who posted the comment.

        - **deleted** *(boolean) --*

          A Boolean value indicating whether the comment has been deleted.

        - **clientRequestToken** *(string) --*

          A unique, client-generated idempotency token that when provided in a request, ensures
          the request cannot be repeated with a changed parameter. If a request is received
          with the same parameters and a token is included, the request will return information
          about the initial request that used that token.
    """


_GetCommentsForPullRequestPaginateResponseTypeDef = TypedDict(
    "_GetCommentsForPullRequestPaginateResponseTypeDef",
    {
        "commentsForPullRequestData": List[
            GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDataTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetCommentsForPullRequestPaginateResponseTypeDef(
    _GetCommentsForPullRequestPaginateResponseTypeDef
):
    """
    Type definition for `GetCommentsForPullRequestPaginate` `Response`

    - **commentsForPullRequestData** *(list) --*

      An array of comment objects on the pull request.

      - *(dict) --*

        Returns information about comments on a pull request.

        - **pullRequestId** *(string) --*

          The system-generated ID of the pull request.

        - **repositoryName** *(string) --*

          The name of the repository that contains the pull request.

        - **beforeCommitId** *(string) --*

          The full commit ID of the commit that was the tip of the destination branch when the pull
          request was created. This commit will be superceded by the after commit in the source
          branch when and if you merge the source branch into the destination branch.

        - **afterCommitId** *(string) --*

          he full commit ID of the commit that was the tip of the source branch at the time the
          comment was made.

        - **beforeBlobId** *(string) --*

          The full blob ID of the file on which you want to comment on the destination commit.

        - **afterBlobId** *(string) --*

          The full blob ID of the file on which you want to comment on the source commit.

        - **location** *(dict) --*

          Location information about the comment on the pull request, including the file name, line
          number, and whether the version of the file where the comment was made is 'BEFORE'
          (destination branch) or 'AFTER' (source branch).

          - **filePath** *(string) --*

            The name of the file being compared, including its extension and subdirectory, if any.

          - **filePosition** *(integer) --*

            The position of a change within a compared file, in line number format.

          - **relativeFileVersion** *(string) --*

            In a comparison of commits or a pull request, whether the change is in the 'before' or
            'after' of that comparison.

        - **comments** *(list) --*

          An array of comment objects. Each comment object contains information about a comment on
          the pull request.

          - *(dict) --*

            Returns information about a specific comment.

            - **commentId** *(string) --*

              The system-generated comment ID.

            - **content** *(string) --*

              The content of the comment.

            - **inReplyTo** *(string) --*

              The ID of the comment for which this comment is a reply, if any.

            - **creationDate** *(datetime) --*

              The date and time the comment was created, in timestamp format.

            - **lastModifiedDate** *(datetime) --*

              The date and time the comment was most recently modified, in timestamp format.

            - **authorArn** *(string) --*

              The Amazon Resource Name (ARN) of the person who posted the comment.

            - **deleted** *(boolean) --*

              A Boolean value indicating whether the comment has been deleted.

            - **clientRequestToken** *(string) --*

              A unique, client-generated idempotency token that when provided in a request, ensures
              the request cannot be repeated with a changed parameter. If a request is received
              with the same parameters and a token is included, the request will return information
              about the initial request that used that token.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetDifferencesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDifferencesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDifferencesPaginatePaginationConfigTypeDef(
    _GetDifferencesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetDifferencesPaginate` `PaginationConfig`

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


_GetDifferencesPaginateResponsedifferencesafterBlobTypeDef = TypedDict(
    "_GetDifferencesPaginateResponsedifferencesafterBlobTypeDef",
    {"blobId": str, "path": str, "mode": str},
    total=False,
)


class GetDifferencesPaginateResponsedifferencesafterBlobTypeDef(
    _GetDifferencesPaginateResponsedifferencesafterBlobTypeDef
):
    """
    Type definition for `GetDifferencesPaginateResponsedifferences` `afterBlob`

    Information about an ``afterBlob`` data type object, including the ID, the file mode
    permission code, and the path.

    - **blobId** *(string) --*

      The full ID of the blob.

    - **path** *(string) --*

      The path to the blob and any associated file name, if any.

    - **mode** *(string) --*

      The file mode permissions of the blob. File mode permission codes include:

      * ``100644`` indicates read/write

      * ``100755`` indicates read/write/execute

      * ``160000`` indicates a submodule

      * ``120000`` indicates a symlink
    """


_GetDifferencesPaginateResponsedifferencesbeforeBlobTypeDef = TypedDict(
    "_GetDifferencesPaginateResponsedifferencesbeforeBlobTypeDef",
    {"blobId": str, "path": str, "mode": str},
    total=False,
)


class GetDifferencesPaginateResponsedifferencesbeforeBlobTypeDef(
    _GetDifferencesPaginateResponsedifferencesbeforeBlobTypeDef
):
    """
    Type definition for `GetDifferencesPaginateResponsedifferences` `beforeBlob`

    Information about a ``beforeBlob`` data type object, including the ID, the file mode
    permission code, and the path.

    - **blobId** *(string) --*

      The full ID of the blob.

    - **path** *(string) --*

      The path to the blob and any associated file name, if any.

    - **mode** *(string) --*

      The file mode permissions of the blob. File mode permission codes include:

      * ``100644`` indicates read/write

      * ``100755`` indicates read/write/execute

      * ``160000`` indicates a submodule

      * ``120000`` indicates a symlink
    """


_GetDifferencesPaginateResponsedifferencesTypeDef = TypedDict(
    "_GetDifferencesPaginateResponsedifferencesTypeDef",
    {
        "beforeBlob": GetDifferencesPaginateResponsedifferencesbeforeBlobTypeDef,
        "afterBlob": GetDifferencesPaginateResponsedifferencesafterBlobTypeDef,
        "changeType": str,
    },
    total=False,
)


class GetDifferencesPaginateResponsedifferencesTypeDef(
    _GetDifferencesPaginateResponsedifferencesTypeDef
):
    """
    Type definition for `GetDifferencesPaginateResponse` `differences`

    Returns information about a set of differences for a commit specifier.

    - **beforeBlob** *(dict) --*

      Information about a ``beforeBlob`` data type object, including the ID, the file mode
      permission code, and the path.

      - **blobId** *(string) --*

        The full ID of the blob.

      - **path** *(string) --*

        The path to the blob and any associated file name, if any.

      - **mode** *(string) --*

        The file mode permissions of the blob. File mode permission codes include:

        * ``100644`` indicates read/write

        * ``100755`` indicates read/write/execute

        * ``160000`` indicates a submodule

        * ``120000`` indicates a symlink

    - **afterBlob** *(dict) --*

      Information about an ``afterBlob`` data type object, including the ID, the file mode
      permission code, and the path.

      - **blobId** *(string) --*

        The full ID of the blob.

      - **path** *(string) --*

        The path to the blob and any associated file name, if any.

      - **mode** *(string) --*

        The file mode permissions of the blob. File mode permission codes include:

        * ``100644`` indicates read/write

        * ``100755`` indicates read/write/execute

        * ``160000`` indicates a submodule

        * ``120000`` indicates a symlink

    - **changeType** *(string) --*

      Whether the change type of the difference is an addition (A), deletion (D), or
      modification (M).
    """


_GetDifferencesPaginateResponseTypeDef = TypedDict(
    "_GetDifferencesPaginateResponseTypeDef",
    {"differences": List[GetDifferencesPaginateResponsedifferencesTypeDef]},
    total=False,
)


class GetDifferencesPaginateResponseTypeDef(_GetDifferencesPaginateResponseTypeDef):
    """
    Type definition for `GetDifferencesPaginate` `Response`

    - **differences** *(list) --*

      A differences data type object that contains information about the differences, including
      whether the difference is added, modified, or deleted (A, D, M).

      - *(dict) --*

        Returns information about a set of differences for a commit specifier.

        - **beforeBlob** *(dict) --*

          Information about a ``beforeBlob`` data type object, including the ID, the file mode
          permission code, and the path.

          - **blobId** *(string) --*

            The full ID of the blob.

          - **path** *(string) --*

            The path to the blob and any associated file name, if any.

          - **mode** *(string) --*

            The file mode permissions of the blob. File mode permission codes include:

            * ``100644`` indicates read/write

            * ``100755`` indicates read/write/execute

            * ``160000`` indicates a submodule

            * ``120000`` indicates a symlink

        - **afterBlob** *(dict) --*

          Information about an ``afterBlob`` data type object, including the ID, the file mode
          permission code, and the path.

          - **blobId** *(string) --*

            The full ID of the blob.

          - **path** *(string) --*

            The path to the blob and any associated file name, if any.

          - **mode** *(string) --*

            The file mode permissions of the blob. File mode permission codes include:

            * ``100644`` indicates read/write

            * ``100755`` indicates read/write/execute

            * ``160000`` indicates a submodule

            * ``120000`` indicates a symlink

        - **changeType** *(string) --*

          Whether the change type of the difference is an addition (A), deletion (D), or
          modification (M).
    """


_ListBranchesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBranchesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListBranchesPaginatePaginationConfigTypeDef(
    _ListBranchesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBranchesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListBranchesPaginateResponseTypeDef = TypedDict(
    "_ListBranchesPaginateResponseTypeDef",
    {"branches": List[str], "NextToken": str},
    total=False,
)


class ListBranchesPaginateResponseTypeDef(_ListBranchesPaginateResponseTypeDef):
    """
    Type definition for `ListBranchesPaginate` `Response`

    Represents the output of a list branches operation.

    - **branches** *(list) --*

      The list of branch names.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPullRequestsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPullRequestsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPullRequestsPaginatePaginationConfigTypeDef(
    _ListPullRequestsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPullRequestsPaginate` `PaginationConfig`

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


_ListPullRequestsPaginateResponseTypeDef = TypedDict(
    "_ListPullRequestsPaginateResponseTypeDef",
    {"pullRequestIds": List[str], "NextToken": str},
    total=False,
)


class ListPullRequestsPaginateResponseTypeDef(_ListPullRequestsPaginateResponseTypeDef):
    """
    Type definition for `ListPullRequestsPaginate` `Response`

    - **pullRequestIds** *(list) --*

      The system-generated IDs of the pull requests.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRepositoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRepositoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListRepositoriesPaginatePaginationConfigTypeDef(
    _ListRepositoriesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRepositoriesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListRepositoriesPaginateResponserepositoriesTypeDef = TypedDict(
    "_ListRepositoriesPaginateResponserepositoriesTypeDef",
    {"repositoryName": str, "repositoryId": str},
    total=False,
)


class ListRepositoriesPaginateResponserepositoriesTypeDef(
    _ListRepositoriesPaginateResponserepositoriesTypeDef
):
    """
    Type definition for `ListRepositoriesPaginateResponse` `repositories`

    Information about a repository name and ID.

    - **repositoryName** *(string) --*

      The name associated with the repository.

    - **repositoryId** *(string) --*

      The ID associated with the repository.
    """


_ListRepositoriesPaginateResponseTypeDef = TypedDict(
    "_ListRepositoriesPaginateResponseTypeDef",
    {
        "repositories": List[ListRepositoriesPaginateResponserepositoriesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListRepositoriesPaginateResponseTypeDef(_ListRepositoriesPaginateResponseTypeDef):
    """
    Type definition for `ListRepositoriesPaginate` `Response`

    Represents the output of a list repositories operation.

    - **repositories** *(list) --*

      Lists the repositories called by the list repositories operation.

      - *(dict) --*

        Information about a repository name and ID.

        - **repositoryName** *(string) --*

          The name associated with the repository.

        - **repositoryId** *(string) --*

          The ID associated with the repository.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
