"Main interface for rekognition type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef",
    "ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef",
    "ClientCompareFacesResponseFaceMatchesFacePoseTypeDef",
    "ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef",
    "ClientCompareFacesResponseFaceMatchesFaceTypeDef",
    "ClientCompareFacesResponseFaceMatchesTypeDef",
    "ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef",
    "ClientCompareFacesResponseSourceImageFaceTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesPoseTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesQualityTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesTypeDef",
    "ClientCompareFacesResponseTypeDef",
    "ClientCompareFacesSourceImageS3ObjectTypeDef",
    "ClientCompareFacesSourceImageTypeDef",
    "ClientCompareFacesTargetImageS3ObjectTypeDef",
    "ClientCompareFacesTargetImageTypeDef",
    "ClientCreateCollectionResponseTypeDef",
    "ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef",
    "ClientCreateStreamProcessorInputTypeDef",
    "ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef",
    "ClientCreateStreamProcessorOutputTypeDef",
    "ClientCreateStreamProcessorResponseTypeDef",
    "ClientCreateStreamProcessorSettingsFaceSearchTypeDef",
    "ClientCreateStreamProcessorSettingsTypeDef",
    "ClientDeleteCollectionResponseTypeDef",
    "ClientDeleteFacesResponseTypeDef",
    "ClientDescribeCollectionResponseTypeDef",
    "ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef",
    "ClientDescribeStreamProcessorResponseInputTypeDef",
    "ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef",
    "ClientDescribeStreamProcessorResponseOutputTypeDef",
    "ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef",
    "ClientDescribeStreamProcessorResponseSettingsTypeDef",
    "ClientDescribeStreamProcessorResponseTypeDef",
    "ClientDetectFacesImageS3ObjectTypeDef",
    "ClientDetectFacesImageTypeDef",
    "ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef",
    "ClientDetectFacesResponseFaceDetailsBeardTypeDef",
    "ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef",
    "ClientDetectFacesResponseFaceDetailsEmotionsTypeDef",
    "ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef",
    "ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef",
    "ClientDetectFacesResponseFaceDetailsGenderTypeDef",
    "ClientDetectFacesResponseFaceDetailsLandmarksTypeDef",
    "ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef",
    "ClientDetectFacesResponseFaceDetailsMustacheTypeDef",
    "ClientDetectFacesResponseFaceDetailsPoseTypeDef",
    "ClientDetectFacesResponseFaceDetailsQualityTypeDef",
    "ClientDetectFacesResponseFaceDetailsSmileTypeDef",
    "ClientDetectFacesResponseFaceDetailsSunglassesTypeDef",
    "ClientDetectFacesResponseFaceDetailsTypeDef",
    "ClientDetectFacesResponseTypeDef",
    "ClientDetectLabelsImageS3ObjectTypeDef",
    "ClientDetectLabelsImageTypeDef",
    "ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef",
    "ClientDetectLabelsResponseLabelsInstancesTypeDef",
    "ClientDetectLabelsResponseLabelsParentsTypeDef",
    "ClientDetectLabelsResponseLabelsTypeDef",
    "ClientDetectLabelsResponseTypeDef",
    "ClientDetectModerationLabelsImageS3ObjectTypeDef",
    "ClientDetectModerationLabelsImageTypeDef",
    "ClientDetectModerationLabelsResponseModerationLabelsTypeDef",
    "ClientDetectModerationLabelsResponseTypeDef",
    "ClientDetectTextImageS3ObjectTypeDef",
    "ClientDetectTextImageTypeDef",
    "ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef",
    "ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef",
    "ClientDetectTextResponseTextDetectionsGeometryTypeDef",
    "ClientDetectTextResponseTextDetectionsTypeDef",
    "ClientDetectTextResponseTypeDef",
    "ClientGetCelebrityInfoResponseTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesTypeDef",
    "ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef",
    "ClientGetCelebrityRecognitionResponseTypeDef",
    "ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef",
    "ClientGetContentModerationResponseModerationLabelsTypeDef",
    "ClientGetContentModerationResponseVideoMetadataTypeDef",
    "ClientGetContentModerationResponseTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceBeardTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceGenderTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef",
    "ClientGetFaceDetectionResponseFacesFacePoseTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceQualityTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceSmileTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceTypeDef",
    "ClientGetFaceDetectionResponseFacesTypeDef",
    "ClientGetFaceDetectionResponseVideoMetadataTypeDef",
    "ClientGetFaceDetectionResponseTypeDef",
    "ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef",
    "ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef",
    "ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonTypeDef",
    "ClientGetFaceSearchResponsePersonsTypeDef",
    "ClientGetFaceSearchResponseVideoMetadataTypeDef",
    "ClientGetFaceSearchResponseTypeDef",
    "ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef",
    "ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef",
    "ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef",
    "ClientGetLabelDetectionResponseLabelsLabelTypeDef",
    "ClientGetLabelDetectionResponseLabelsTypeDef",
    "ClientGetLabelDetectionResponseVideoMetadataTypeDef",
    "ClientGetLabelDetectionResponseTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonTypeDef",
    "ClientGetPersonTrackingResponsePersonsTypeDef",
    "ClientGetPersonTrackingResponseVideoMetadataTypeDef",
    "ClientGetPersonTrackingResponseTypeDef",
    "ClientIndexFacesImageS3ObjectTypeDef",
    "ClientIndexFacesImageTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceTypeDef",
    "ClientIndexFacesResponseFaceRecordsTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef",
    "ClientIndexFacesResponseUnindexedFacesTypeDef",
    "ClientIndexFacesResponseTypeDef",
    "ClientListCollectionsResponseTypeDef",
    "ClientListFacesResponseFacesBoundingBoxTypeDef",
    "ClientListFacesResponseFacesTypeDef",
    "ClientListFacesResponseTypeDef",
    "ClientListStreamProcessorsResponseStreamProcessorsTypeDef",
    "ClientListStreamProcessorsResponseTypeDef",
    "ClientRecognizeCelebritiesImageS3ObjectTypeDef",
    "ClientRecognizeCelebritiesImageTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef",
    "ClientRecognizeCelebritiesResponseTypeDef",
    "ClientSearchFacesByImageImageS3ObjectTypeDef",
    "ClientSearchFacesByImageImageTypeDef",
    "ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef",
    "ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef",
    "ClientSearchFacesByImageResponseFaceMatchesTypeDef",
    "ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef",
    "ClientSearchFacesByImageResponseTypeDef",
    "ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef",
    "ClientSearchFacesResponseFaceMatchesFaceTypeDef",
    "ClientSearchFacesResponseFaceMatchesTypeDef",
    "ClientSearchFacesResponseTypeDef",
    "ClientStartCelebrityRecognitionNotificationChannelTypeDef",
    "ClientStartCelebrityRecognitionResponseTypeDef",
    "ClientStartCelebrityRecognitionVideoS3ObjectTypeDef",
    "ClientStartCelebrityRecognitionVideoTypeDef",
    "ClientStartContentModerationNotificationChannelTypeDef",
    "ClientStartContentModerationResponseTypeDef",
    "ClientStartContentModerationVideoS3ObjectTypeDef",
    "ClientStartContentModerationVideoTypeDef",
    "ClientStartFaceDetectionNotificationChannelTypeDef",
    "ClientStartFaceDetectionResponseTypeDef",
    "ClientStartFaceDetectionVideoS3ObjectTypeDef",
    "ClientStartFaceDetectionVideoTypeDef",
    "ClientStartFaceSearchNotificationChannelTypeDef",
    "ClientStartFaceSearchResponseTypeDef",
    "ClientStartFaceSearchVideoS3ObjectTypeDef",
    "ClientStartFaceSearchVideoTypeDef",
    "ClientStartLabelDetectionNotificationChannelTypeDef",
    "ClientStartLabelDetectionResponseTypeDef",
    "ClientStartLabelDetectionVideoS3ObjectTypeDef",
    "ClientStartLabelDetectionVideoTypeDef",
    "ClientStartPersonTrackingNotificationChannelTypeDef",
    "ClientStartPersonTrackingResponseTypeDef",
    "ClientStartPersonTrackingVideoS3ObjectTypeDef",
    "ClientStartPersonTrackingVideoTypeDef",
    "ListCollectionsPaginatePaginationConfigTypeDef",
    "ListCollectionsPaginateResponseTypeDef",
    "ListFacesPaginatePaginationConfigTypeDef",
    "ListFacesPaginateResponseFacesBoundingBoxTypeDef",
    "ListFacesPaginateResponseFacesTypeDef",
    "ListFacesPaginateResponseTypeDef",
    "ListStreamProcessorsPaginatePaginationConfigTypeDef",
    "ListStreamProcessorsPaginateResponseStreamProcessorsTypeDef",
    "ListStreamProcessorsPaginateResponseTypeDef",
)


_ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef = TypedDict(
    "_ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef(
    _ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef
):
    """
    Type definition for `ClientCompareFacesResponseFaceMatchesFace` `BoundingBox`

    Bounding box of the face.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef = TypedDict(
    "_ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef",
    {"Type": str, "X": float, "Y": float},
    total=False,
)


class ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef(
    _ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef
):
    """
    Type definition for `ClientCompareFacesResponseFaceMatchesFace` `Landmarks`

    Indicates the location of the landmark on the face.

    - **Type** *(string) --*

      Type of landmark.

    - **X** *(float) --*

      The x-coordinate from the top left of the landmark expressed as the ratio of the
      width of the image. For example, if the image is 700 x 200 and the x-coordinate of
      the landmark is at 350 pixels, this value is 0.5.

    - **Y** *(float) --*

      The y-coordinate from the top left of the landmark expressed as the ratio of the
      height of the image. For example, if the image is 700 x 200 and the y-coordinate of
      the landmark is at 100 pixels, this value is 0.5.
    """


_ClientCompareFacesResponseFaceMatchesFacePoseTypeDef = TypedDict(
    "_ClientCompareFacesResponseFaceMatchesFacePoseTypeDef",
    {"Roll": float, "Yaw": float, "Pitch": float},
    total=False,
)


class ClientCompareFacesResponseFaceMatchesFacePoseTypeDef(
    _ClientCompareFacesResponseFaceMatchesFacePoseTypeDef
):
    """
    Type definition for `ClientCompareFacesResponseFaceMatchesFace` `Pose`

    Indicates the pose of the face as determined by its pitch, roll, and yaw.

    - **Roll** *(float) --*

      Value representing the face rotation on the roll axis.

    - **Yaw** *(float) --*

      Value representing the face rotation on the yaw axis.

    - **Pitch** *(float) --*

      Value representing the face rotation on the pitch axis.
    """


_ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef = TypedDict(
    "_ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef",
    {"Brightness": float, "Sharpness": float},
    total=False,
)


class ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef(
    _ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef
):
    """
    Type definition for `ClientCompareFacesResponseFaceMatchesFace` `Quality`

    Identifies face image brightness and sharpness.

    - **Brightness** *(float) --*

      Value representing brightness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a brighter face image.

    - **Sharpness** *(float) --*

      Value representing sharpness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a sharper face image.
    """


_ClientCompareFacesResponseFaceMatchesFaceTypeDef = TypedDict(
    "_ClientCompareFacesResponseFaceMatchesFaceTypeDef",
    {
        "BoundingBox": ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef,
        "Confidence": float,
        "Landmarks": List[ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef],
        "Pose": ClientCompareFacesResponseFaceMatchesFacePoseTypeDef,
        "Quality": ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef,
    },
    total=False,
)


class ClientCompareFacesResponseFaceMatchesFaceTypeDef(
    _ClientCompareFacesResponseFaceMatchesFaceTypeDef
):
    """
    Type definition for `ClientCompareFacesResponseFaceMatches` `Face`

    Provides face metadata (bounding box and confidence that the bounding box actually
    contains a face).

    - **BoundingBox** *(dict) --*

      Bounding box of the face.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **Confidence** *(float) --*

      Level of confidence that what the bounding box contains is a face.

    - **Landmarks** *(list) --*

      An array of facial landmarks.

      - *(dict) --*

        Indicates the location of the landmark on the face.

        - **Type** *(string) --*

          Type of landmark.

        - **X** *(float) --*

          The x-coordinate from the top left of the landmark expressed as the ratio of the
          width of the image. For example, if the image is 700 x 200 and the x-coordinate of
          the landmark is at 350 pixels, this value is 0.5.

        - **Y** *(float) --*

          The y-coordinate from the top left of the landmark expressed as the ratio of the
          height of the image. For example, if the image is 700 x 200 and the y-coordinate of
          the landmark is at 100 pixels, this value is 0.5.

    - **Pose** *(dict) --*

      Indicates the pose of the face as determined by its pitch, roll, and yaw.

      - **Roll** *(float) --*

        Value representing the face rotation on the roll axis.

      - **Yaw** *(float) --*

        Value representing the face rotation on the yaw axis.

      - **Pitch** *(float) --*

        Value representing the face rotation on the pitch axis.

    - **Quality** *(dict) --*

      Identifies face image brightness and sharpness.

      - **Brightness** *(float) --*

        Value representing brightness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a brighter face image.

      - **Sharpness** *(float) --*

        Value representing sharpness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a sharper face image.
    """


_ClientCompareFacesResponseFaceMatchesTypeDef = TypedDict(
    "_ClientCompareFacesResponseFaceMatchesTypeDef",
    {"Similarity": float, "Face": ClientCompareFacesResponseFaceMatchesFaceTypeDef},
    total=False,
)


class ClientCompareFacesResponseFaceMatchesTypeDef(
    _ClientCompareFacesResponseFaceMatchesTypeDef
):
    """
    Type definition for `ClientCompareFacesResponse` `FaceMatches`

    Provides information about a face in a target image that matches the source image face
    analyzed by ``CompareFaces`` . The ``Face`` property contains the bounding box of the face
    in the target image. The ``Similarity`` property is the confidence that the source image
    face matches the face in the bounding box.

    - **Similarity** *(float) --*

      Level of confidence that the faces match.

    - **Face** *(dict) --*

      Provides face metadata (bounding box and confidence that the bounding box actually
      contains a face).

      - **BoundingBox** *(dict) --*

        Bounding box of the face.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **Confidence** *(float) --*

        Level of confidence that what the bounding box contains is a face.

      - **Landmarks** *(list) --*

        An array of facial landmarks.

        - *(dict) --*

          Indicates the location of the landmark on the face.

          - **Type** *(string) --*

            Type of landmark.

          - **X** *(float) --*

            The x-coordinate from the top left of the landmark expressed as the ratio of the
            width of the image. For example, if the image is 700 x 200 and the x-coordinate of
            the landmark is at 350 pixels, this value is 0.5.

          - **Y** *(float) --*

            The y-coordinate from the top left of the landmark expressed as the ratio of the
            height of the image. For example, if the image is 700 x 200 and the y-coordinate of
            the landmark is at 100 pixels, this value is 0.5.

      - **Pose** *(dict) --*

        Indicates the pose of the face as determined by its pitch, roll, and yaw.

        - **Roll** *(float) --*

          Value representing the face rotation on the roll axis.

        - **Yaw** *(float) --*

          Value representing the face rotation on the yaw axis.

        - **Pitch** *(float) --*

          Value representing the face rotation on the pitch axis.

      - **Quality** *(dict) --*

        Identifies face image brightness and sharpness.

        - **Brightness** *(float) --*

          Value representing brightness of the face. The service returns a value between 0 and
          100 (inclusive). A higher value indicates a brighter face image.

        - **Sharpness** *(float) --*

          Value representing sharpness of the face. The service returns a value between 0 and
          100 (inclusive). A higher value indicates a sharper face image.
    """


_ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef = TypedDict(
    "_ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef(
    _ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef
):
    """
    Type definition for `ClientCompareFacesResponseSourceImageFace` `BoundingBox`

    Bounding box of the face.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientCompareFacesResponseSourceImageFaceTypeDef = TypedDict(
    "_ClientCompareFacesResponseSourceImageFaceTypeDef",
    {
        "BoundingBox": ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef,
        "Confidence": float,
    },
    total=False,
)


class ClientCompareFacesResponseSourceImageFaceTypeDef(
    _ClientCompareFacesResponseSourceImageFaceTypeDef
):
    """
    Type definition for `ClientCompareFacesResponse` `SourceImageFace`

    The face in the source image that was used for comparison.

    - **BoundingBox** *(dict) --*

      Bounding box of the face.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **Confidence** *(float) --*

      Confidence level that the selected bounding box contains a face.
    """


_ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef = TypedDict(
    "_ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef(
    _ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef
):
    """
    Type definition for `ClientCompareFacesResponseUnmatchedFaces` `BoundingBox`

    Bounding box of the face.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef = TypedDict(
    "_ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef",
    {"Type": str, "X": float, "Y": float},
    total=False,
)


class ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef(
    _ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef
):
    """
    Type definition for `ClientCompareFacesResponseUnmatchedFaces` `Landmarks`

    Indicates the location of the landmark on the face.

    - **Type** *(string) --*

      Type of landmark.

    - **X** *(float) --*

      The x-coordinate from the top left of the landmark expressed as the ratio of the
      width of the image. For example, if the image is 700 x 200 and the x-coordinate of
      the landmark is at 350 pixels, this value is 0.5.

    - **Y** *(float) --*

      The y-coordinate from the top left of the landmark expressed as the ratio of the
      height of the image. For example, if the image is 700 x 200 and the y-coordinate of
      the landmark is at 100 pixels, this value is 0.5.
    """


_ClientCompareFacesResponseUnmatchedFacesPoseTypeDef = TypedDict(
    "_ClientCompareFacesResponseUnmatchedFacesPoseTypeDef",
    {"Roll": float, "Yaw": float, "Pitch": float},
    total=False,
)


class ClientCompareFacesResponseUnmatchedFacesPoseTypeDef(
    _ClientCompareFacesResponseUnmatchedFacesPoseTypeDef
):
    """
    Type definition for `ClientCompareFacesResponseUnmatchedFaces` `Pose`

    Indicates the pose of the face as determined by its pitch, roll, and yaw.

    - **Roll** *(float) --*

      Value representing the face rotation on the roll axis.

    - **Yaw** *(float) --*

      Value representing the face rotation on the yaw axis.

    - **Pitch** *(float) --*

      Value representing the face rotation on the pitch axis.
    """


_ClientCompareFacesResponseUnmatchedFacesQualityTypeDef = TypedDict(
    "_ClientCompareFacesResponseUnmatchedFacesQualityTypeDef",
    {"Brightness": float, "Sharpness": float},
    total=False,
)


class ClientCompareFacesResponseUnmatchedFacesQualityTypeDef(
    _ClientCompareFacesResponseUnmatchedFacesQualityTypeDef
):
    """
    Type definition for `ClientCompareFacesResponseUnmatchedFaces` `Quality`

    Identifies face image brightness and sharpness.

    - **Brightness** *(float) --*

      Value representing brightness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a brighter face image.

    - **Sharpness** *(float) --*

      Value representing sharpness of the face. The service returns a value between 0 and 100
      (inclusive). A higher value indicates a sharper face image.
    """


_ClientCompareFacesResponseUnmatchedFacesTypeDef = TypedDict(
    "_ClientCompareFacesResponseUnmatchedFacesTypeDef",
    {
        "BoundingBox": ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef,
        "Confidence": float,
        "Landmarks": List[ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef],
        "Pose": ClientCompareFacesResponseUnmatchedFacesPoseTypeDef,
        "Quality": ClientCompareFacesResponseUnmatchedFacesQualityTypeDef,
    },
    total=False,
)


class ClientCompareFacesResponseUnmatchedFacesTypeDef(
    _ClientCompareFacesResponseUnmatchedFacesTypeDef
):
    """
    Type definition for `ClientCompareFacesResponse` `UnmatchedFaces`

    Provides face metadata for target image faces that are analyzed by ``CompareFaces`` and
    ``RecognizeCelebrities`` .

    - **BoundingBox** *(dict) --*

      Bounding box of the face.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **Confidence** *(float) --*

      Level of confidence that what the bounding box contains is a face.

    - **Landmarks** *(list) --*

      An array of facial landmarks.

      - *(dict) --*

        Indicates the location of the landmark on the face.

        - **Type** *(string) --*

          Type of landmark.

        - **X** *(float) --*

          The x-coordinate from the top left of the landmark expressed as the ratio of the
          width of the image. For example, if the image is 700 x 200 and the x-coordinate of
          the landmark is at 350 pixels, this value is 0.5.

        - **Y** *(float) --*

          The y-coordinate from the top left of the landmark expressed as the ratio of the
          height of the image. For example, if the image is 700 x 200 and the y-coordinate of
          the landmark is at 100 pixels, this value is 0.5.

    - **Pose** *(dict) --*

      Indicates the pose of the face as determined by its pitch, roll, and yaw.

      - **Roll** *(float) --*

        Value representing the face rotation on the roll axis.

      - **Yaw** *(float) --*

        Value representing the face rotation on the yaw axis.

      - **Pitch** *(float) --*

        Value representing the face rotation on the pitch axis.

    - **Quality** *(dict) --*

      Identifies face image brightness and sharpness.

      - **Brightness** *(float) --*

        Value representing brightness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a brighter face image.

      - **Sharpness** *(float) --*

        Value representing sharpness of the face. The service returns a value between 0 and 100
        (inclusive). A higher value indicates a sharper face image.
    """


_ClientCompareFacesResponseTypeDef = TypedDict(
    "_ClientCompareFacesResponseTypeDef",
    {
        "SourceImageFace": ClientCompareFacesResponseSourceImageFaceTypeDef,
        "FaceMatches": List[ClientCompareFacesResponseFaceMatchesTypeDef],
        "UnmatchedFaces": List[ClientCompareFacesResponseUnmatchedFacesTypeDef],
        "SourceImageOrientationCorrection": str,
        "TargetImageOrientationCorrection": str,
    },
    total=False,
)


class ClientCompareFacesResponseTypeDef(_ClientCompareFacesResponseTypeDef):
    """
    Type definition for `ClientCompareFaces` `Response`

    - **SourceImageFace** *(dict) --*

      The face in the source image that was used for comparison.

      - **BoundingBox** *(dict) --*

        Bounding box of the face.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **Confidence** *(float) --*

        Confidence level that the selected bounding box contains a face.

    - **FaceMatches** *(list) --*

      An array of faces in the target image that match the source image face. Each
      ``CompareFacesMatch`` object provides the bounding box, the confidence level that the
      bounding box contains a face, and the similarity score for the face in the bounding box and
      the face in the source image.

      - *(dict) --*

        Provides information about a face in a target image that matches the source image face
        analyzed by ``CompareFaces`` . The ``Face`` property contains the bounding box of the face
        in the target image. The ``Similarity`` property is the confidence that the source image
        face matches the face in the bounding box.

        - **Similarity** *(float) --*

          Level of confidence that the faces match.

        - **Face** *(dict) --*

          Provides face metadata (bounding box and confidence that the bounding box actually
          contains a face).

          - **BoundingBox** *(dict) --*

            Bounding box of the face.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **Confidence** *(float) --*

            Level of confidence that what the bounding box contains is a face.

          - **Landmarks** *(list) --*

            An array of facial landmarks.

            - *(dict) --*

              Indicates the location of the landmark on the face.

              - **Type** *(string) --*

                Type of landmark.

              - **X** *(float) --*

                The x-coordinate from the top left of the landmark expressed as the ratio of the
                width of the image. For example, if the image is 700 x 200 and the x-coordinate of
                the landmark is at 350 pixels, this value is 0.5.

              - **Y** *(float) --*

                The y-coordinate from the top left of the landmark expressed as the ratio of the
                height of the image. For example, if the image is 700 x 200 and the y-coordinate of
                the landmark is at 100 pixels, this value is 0.5.

          - **Pose** *(dict) --*

            Indicates the pose of the face as determined by its pitch, roll, and yaw.

            - **Roll** *(float) --*

              Value representing the face rotation on the roll axis.

            - **Yaw** *(float) --*

              Value representing the face rotation on the yaw axis.

            - **Pitch** *(float) --*

              Value representing the face rotation on the pitch axis.

          - **Quality** *(dict) --*

            Identifies face image brightness and sharpness.

            - **Brightness** *(float) --*

              Value representing brightness of the face. The service returns a value between 0 and
              100 (inclusive). A higher value indicates a brighter face image.

            - **Sharpness** *(float) --*

              Value representing sharpness of the face. The service returns a value between 0 and
              100 (inclusive). A higher value indicates a sharper face image.

    - **UnmatchedFaces** *(list) --*

      An array of faces in the target image that did not match the source image face.

      - *(dict) --*

        Provides face metadata for target image faces that are analyzed by ``CompareFaces`` and
        ``RecognizeCelebrities`` .

        - **BoundingBox** *(dict) --*

          Bounding box of the face.

          - **Width** *(float) --*

            Width of the bounding box as a ratio of the overall image width.

          - **Height** *(float) --*

            Height of the bounding box as a ratio of the overall image height.

          - **Left** *(float) --*

            Left coordinate of the bounding box as a ratio of overall image width.

          - **Top** *(float) --*

            Top coordinate of the bounding box as a ratio of overall image height.

        - **Confidence** *(float) --*

          Level of confidence that what the bounding box contains is a face.

        - **Landmarks** *(list) --*

          An array of facial landmarks.

          - *(dict) --*

            Indicates the location of the landmark on the face.

            - **Type** *(string) --*

              Type of landmark.

            - **X** *(float) --*

              The x-coordinate from the top left of the landmark expressed as the ratio of the
              width of the image. For example, if the image is 700 x 200 and the x-coordinate of
              the landmark is at 350 pixels, this value is 0.5.

            - **Y** *(float) --*

              The y-coordinate from the top left of the landmark expressed as the ratio of the
              height of the image. For example, if the image is 700 x 200 and the y-coordinate of
              the landmark is at 100 pixels, this value is 0.5.

        - **Pose** *(dict) --*

          Indicates the pose of the face as determined by its pitch, roll, and yaw.

          - **Roll** *(float) --*

            Value representing the face rotation on the roll axis.

          - **Yaw** *(float) --*

            Value representing the face rotation on the yaw axis.

          - **Pitch** *(float) --*

            Value representing the face rotation on the pitch axis.

        - **Quality** *(dict) --*

          Identifies face image brightness and sharpness.

          - **Brightness** *(float) --*

            Value representing brightness of the face. The service returns a value between 0 and
            100 (inclusive). A higher value indicates a brighter face image.

          - **Sharpness** *(float) --*

            Value representing sharpness of the face. The service returns a value between 0 and 100
            (inclusive). A higher value indicates a sharper face image.

    - **SourceImageOrientationCorrection** *(string) --*

      The value of ``SourceImageOrientationCorrection`` is always null.

      If the input image is in .jpeg format, it might contain exchangeable image file format (Exif)
      metadata that includes the image's orientation. Amazon Rekognition uses this orientation
      information to perform image correction. The bounding box coordinates are translated to
      represent object locations after the orientation information in the Exif metadata is used to
      correct the image orientation. Images in .png format don't contain Exif metadata.

      Amazon Rekognition doesn’t perform image correction for images in .png format and .jpeg
      images without orientation information in the image Exif metadata. The bounding box
      coordinates aren't translated and represent the object locations before the image is rotated.

    - **TargetImageOrientationCorrection** *(string) --*

      The value of ``TargetImageOrientationCorrection`` is always null.

      If the input image is in .jpeg format, it might contain exchangeable image file format (Exif)
      metadata that includes the image's orientation. Amazon Rekognition uses this orientation
      information to perform image correction. The bounding box coordinates are translated to
      represent object locations after the orientation information in the Exif metadata is used to
      correct the image orientation. Images in .png format don't contain Exif metadata.

      Amazon Rekognition doesn’t perform image correction for images in .png format and .jpeg
      images without orientation information in the image Exif metadata. The bounding box
      coordinates aren't translated and represent the object locations before the image is rotated.
    """


_ClientCompareFacesSourceImageS3ObjectTypeDef = TypedDict(
    "_ClientCompareFacesSourceImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientCompareFacesSourceImageS3ObjectTypeDef(
    _ClientCompareFacesSourceImageS3ObjectTypeDef
):
    """
    Type definition for `ClientCompareFacesSourceImage` `S3Object`

    Identifies an S3 object as the image source.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientCompareFacesSourceImageTypeDef = TypedDict(
    "_ClientCompareFacesSourceImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientCompareFacesSourceImageS3ObjectTypeDef},
    total=False,
)


class ClientCompareFacesSourceImageTypeDef(_ClientCompareFacesSourceImageTypeDef):
    """
    Type definition for `ClientCompareFaces` `SourceImage`

    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes is not supported.

    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image
    bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.

    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.

    - **S3Object** *(dict) --*

      Identifies an S3 object as the image source.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientCompareFacesTargetImageS3ObjectTypeDef = TypedDict(
    "_ClientCompareFacesTargetImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientCompareFacesTargetImageS3ObjectTypeDef(
    _ClientCompareFacesTargetImageS3ObjectTypeDef
):
    """
    Type definition for `ClientCompareFacesTargetImage` `S3Object`

    Identifies an S3 object as the image source.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientCompareFacesTargetImageTypeDef = TypedDict(
    "_ClientCompareFacesTargetImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientCompareFacesTargetImageS3ObjectTypeDef},
    total=False,
)


class ClientCompareFacesTargetImageTypeDef(_ClientCompareFacesTargetImageTypeDef):
    """
    Type definition for `ClientCompareFaces` `TargetImage`

    The target image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes is not supported.

    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image
    bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.

    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.

    - **S3Object** *(dict) --*

      Identifies an S3 object as the image source.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientCreateCollectionResponseTypeDef = TypedDict(
    "_ClientCreateCollectionResponseTypeDef",
    {"StatusCode": int, "CollectionArn": str, "FaceModelVersion": str},
    total=False,
)


class ClientCreateCollectionResponseTypeDef(_ClientCreateCollectionResponseTypeDef):
    """
    Type definition for `ClientCreateCollection` `Response`

    - **StatusCode** *(integer) --*

      HTTP status code indicating the result of the operation.

    - **CollectionArn** *(string) --*

      Amazon Resource Name (ARN) of the collection. You can use this to manage permissions on your
      resources.

    - **FaceModelVersion** *(string) --*

      Version number of the face detection model associated with the collection you are creating.
    """


_ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef = TypedDict(
    "_ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef",
    {"Arn": str},
    total=False,
)


class ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef(
    _ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef
):
    """
    Type definition for `ClientCreateStreamProcessorInput` `KinesisVideoStream`

    The Kinesis video stream input stream for the source streaming video.

    - **Arn** *(string) --*

      ARN of the Kinesis video stream stream that streams the source video.
    """


_ClientCreateStreamProcessorInputTypeDef = TypedDict(
    "_ClientCreateStreamProcessorInputTypeDef",
    {"KinesisVideoStream": ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef},
    total=False,
)


class ClientCreateStreamProcessorInputTypeDef(_ClientCreateStreamProcessorInputTypeDef):
    """
    Type definition for `ClientCreateStreamProcessor` `Input`

    Kinesis video stream stream that provides the source streaming video. If you are using the AWS
    CLI, the parameter name is ``StreamProcessorInput`` .

    - **KinesisVideoStream** *(dict) --*

      The Kinesis video stream input stream for the source streaming video.

      - **Arn** *(string) --*

        ARN of the Kinesis video stream stream that streams the source video.
    """


_ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef = TypedDict(
    "_ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef",
    {"Arn": str},
    total=False,
)


class ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef(
    _ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef
):
    """
    Type definition for `ClientCreateStreamProcessorOutput` `KinesisDataStream`

    The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor streams
    the analysis results.

    - **Arn** *(string) --*

      ARN of the output Amazon Kinesis Data Streams stream.
    """


_ClientCreateStreamProcessorOutputTypeDef = TypedDict(
    "_ClientCreateStreamProcessorOutputTypeDef",
    {"KinesisDataStream": ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef},
    total=False,
)


class ClientCreateStreamProcessorOutputTypeDef(
    _ClientCreateStreamProcessorOutputTypeDef
):
    """
    Type definition for `ClientCreateStreamProcessor` `Output`

    Kinesis data stream stream to which Amazon Rekognition Video puts the analysis results. If you
    are using the AWS CLI, the parameter name is ``StreamProcessorOutput`` .

    - **KinesisDataStream** *(dict) --*

      The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor streams
      the analysis results.

      - **Arn** *(string) --*

        ARN of the output Amazon Kinesis Data Streams stream.
    """


_ClientCreateStreamProcessorResponseTypeDef = TypedDict(
    "_ClientCreateStreamProcessorResponseTypeDef",
    {"StreamProcessorArn": str},
    total=False,
)


class ClientCreateStreamProcessorResponseTypeDef(
    _ClientCreateStreamProcessorResponseTypeDef
):
    """
    Type definition for `ClientCreateStreamProcessor` `Response`

    - **StreamProcessorArn** *(string) --*

      ARN for the newly create stream processor.
    """


_ClientCreateStreamProcessorSettingsFaceSearchTypeDef = TypedDict(
    "_ClientCreateStreamProcessorSettingsFaceSearchTypeDef",
    {"CollectionId": str, "FaceMatchThreshold": float},
    total=False,
)


class ClientCreateStreamProcessorSettingsFaceSearchTypeDef(
    _ClientCreateStreamProcessorSettingsFaceSearchTypeDef
):
    """
    Type definition for `ClientCreateStreamProcessorSettings` `FaceSearch`

    Face search settings to use on a streaming video.

    - **CollectionId** *(string) --*

      The ID of a collection that contains faces that you want to search for.

    - **FaceMatchThreshold** *(float) --*

      Minimum face match confidence score that must be met to return a result for a recognized
      face. Default is 70. 0 is the lowest confidence. 100 is the highest confidence.
    """


_ClientCreateStreamProcessorSettingsTypeDef = TypedDict(
    "_ClientCreateStreamProcessorSettingsTypeDef",
    {"FaceSearch": ClientCreateStreamProcessorSettingsFaceSearchTypeDef},
    total=False,
)


class ClientCreateStreamProcessorSettingsTypeDef(
    _ClientCreateStreamProcessorSettingsTypeDef
):
    """
    Type definition for `ClientCreateStreamProcessor` `Settings`

    Face recognition input parameters to be used by the stream processor. Includes the collection to
    use for face recognition and the face attributes to detect.

    - **FaceSearch** *(dict) --*

      Face search settings to use on a streaming video.

      - **CollectionId** *(string) --*

        The ID of a collection that contains faces that you want to search for.

      - **FaceMatchThreshold** *(float) --*

        Minimum face match confidence score that must be met to return a result for a recognized
        face. Default is 70. 0 is the lowest confidence. 100 is the highest confidence.
    """


_ClientDeleteCollectionResponseTypeDef = TypedDict(
    "_ClientDeleteCollectionResponseTypeDef", {"StatusCode": int}, total=False
)


class ClientDeleteCollectionResponseTypeDef(_ClientDeleteCollectionResponseTypeDef):
    """
    Type definition for `ClientDeleteCollection` `Response`

    - **StatusCode** *(integer) --*

      HTTP status code that indicates the result of the operation.
    """


_ClientDeleteFacesResponseTypeDef = TypedDict(
    "_ClientDeleteFacesResponseTypeDef", {"DeletedFaces": List[str]}, total=False
)


class ClientDeleteFacesResponseTypeDef(_ClientDeleteFacesResponseTypeDef):
    """
    Type definition for `ClientDeleteFaces` `Response`

    - **DeletedFaces** *(list) --*

      An array of strings (face IDs) of the faces that were deleted.

      - *(string) --*
    """


_ClientDescribeCollectionResponseTypeDef = TypedDict(
    "_ClientDescribeCollectionResponseTypeDef",
    {
        "FaceCount": int,
        "FaceModelVersion": str,
        "CollectionARN": str,
        "CreationTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeCollectionResponseTypeDef(_ClientDescribeCollectionResponseTypeDef):
    """
    Type definition for `ClientDescribeCollection` `Response`

    - **FaceCount** *(integer) --*

      The number of faces that are indexed into the collection. To index faces into a collection,
      use  IndexFaces .

    - **FaceModelVersion** *(string) --*

      The version of the face model that's used by the collection for face detection.

      For more information, see Model Versioning in the Amazon Rekognition Developer Guide.

    - **CollectionARN** *(string) --*

      The Amazon Resource Name (ARN) of the collection.

    - **CreationTimestamp** *(datetime) --*

      The number of milliseconds since the Unix epoch time until the creation of the collection.
      The Unix epoch time is 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970.
    """


_ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef",
    {"Arn": str},
    total=False,
)


class ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef(
    _ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef
):
    """
    Type definition for `ClientDescribeStreamProcessorResponseInput` `KinesisVideoStream`

    The Kinesis video stream input stream for the source streaming video.

    - **Arn** *(string) --*

      ARN of the Kinesis video stream stream that streams the source video.
    """


_ClientDescribeStreamProcessorResponseInputTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseInputTypeDef",
    {
        "KinesisVideoStream": ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef
    },
    total=False,
)


class ClientDescribeStreamProcessorResponseInputTypeDef(
    _ClientDescribeStreamProcessorResponseInputTypeDef
):
    """
    Type definition for `ClientDescribeStreamProcessorResponse` `Input`

    Kinesis video stream that provides the source streaming video.

    - **KinesisVideoStream** *(dict) --*

      The Kinesis video stream input stream for the source streaming video.

      - **Arn** *(string) --*

        ARN of the Kinesis video stream stream that streams the source video.
    """


_ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef",
    {"Arn": str},
    total=False,
)


class ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef(
    _ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef
):
    """
    Type definition for `ClientDescribeStreamProcessorResponseOutput` `KinesisDataStream`

    The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor
    streams the analysis results.

    - **Arn** *(string) --*

      ARN of the output Amazon Kinesis Data Streams stream.
    """


_ClientDescribeStreamProcessorResponseOutputTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseOutputTypeDef",
    {
        "KinesisDataStream": ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef
    },
    total=False,
)


class ClientDescribeStreamProcessorResponseOutputTypeDef(
    _ClientDescribeStreamProcessorResponseOutputTypeDef
):
    """
    Type definition for `ClientDescribeStreamProcessorResponse` `Output`

    Kinesis data stream to which Amazon Rekognition Video puts the analysis results.

    - **KinesisDataStream** *(dict) --*

      The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor
      streams the analysis results.

      - **Arn** *(string) --*

        ARN of the output Amazon Kinesis Data Streams stream.
    """


_ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef",
    {"CollectionId": str, "FaceMatchThreshold": float},
    total=False,
)


class ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef(
    _ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef
):
    """
    Type definition for `ClientDescribeStreamProcessorResponseSettings` `FaceSearch`

    Face search settings to use on a streaming video.

    - **CollectionId** *(string) --*

      The ID of a collection that contains faces that you want to search for.

    - **FaceMatchThreshold** *(float) --*

      Minimum face match confidence score that must be met to return a result for a recognized
      face. Default is 70. 0 is the lowest confidence. 100 is the highest confidence.
    """


_ClientDescribeStreamProcessorResponseSettingsTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseSettingsTypeDef",
    {"FaceSearch": ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef},
    total=False,
)


class ClientDescribeStreamProcessorResponseSettingsTypeDef(
    _ClientDescribeStreamProcessorResponseSettingsTypeDef
):
    """
    Type definition for `ClientDescribeStreamProcessorResponse` `Settings`

    Face recognition input parameters that are being used by the stream processor. Includes the
    collection to use for face recognition and the face attributes to detect.

    - **FaceSearch** *(dict) --*

      Face search settings to use on a streaming video.

      - **CollectionId** *(string) --*

        The ID of a collection that contains faces that you want to search for.

      - **FaceMatchThreshold** *(float) --*

        Minimum face match confidence score that must be met to return a result for a recognized
        face. Default is 70. 0 is the lowest confidence. 100 is the highest confidence.
    """


_ClientDescribeStreamProcessorResponseTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseTypeDef",
    {
        "Name": str,
        "StreamProcessorArn": str,
        "Status": str,
        "StatusMessage": str,
        "CreationTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "Input": ClientDescribeStreamProcessorResponseInputTypeDef,
        "Output": ClientDescribeStreamProcessorResponseOutputTypeDef,
        "RoleArn": str,
        "Settings": ClientDescribeStreamProcessorResponseSettingsTypeDef,
    },
    total=False,
)


class ClientDescribeStreamProcessorResponseTypeDef(
    _ClientDescribeStreamProcessorResponseTypeDef
):
    """
    Type definition for `ClientDescribeStreamProcessor` `Response`

    - **Name** *(string) --*

      Name of the stream processor.

    - **StreamProcessorArn** *(string) --*

      ARN of the stream processor.

    - **Status** *(string) --*

      Current status of the stream processor.

    - **StatusMessage** *(string) --*

      Detailed status message about the stream processor.

    - **CreationTimestamp** *(datetime) --*

      Date and time the stream processor was created

    - **LastUpdateTimestamp** *(datetime) --*

      The time, in Unix format, the stream processor was last updated. For example, when the stream
      processor moves from a running state to a failed state, or when the user starts or stops the
      stream processor.

    - **Input** *(dict) --*

      Kinesis video stream that provides the source streaming video.

      - **KinesisVideoStream** *(dict) --*

        The Kinesis video stream input stream for the source streaming video.

        - **Arn** *(string) --*

          ARN of the Kinesis video stream stream that streams the source video.

    - **Output** *(dict) --*

      Kinesis data stream to which Amazon Rekognition Video puts the analysis results.

      - **KinesisDataStream** *(dict) --*

        The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor
        streams the analysis results.

        - **Arn** *(string) --*

          ARN of the output Amazon Kinesis Data Streams stream.

    - **RoleArn** *(string) --*

      ARN of the IAM role that allows access to the stream processor.

    - **Settings** *(dict) --*

      Face recognition input parameters that are being used by the stream processor. Includes the
      collection to use for face recognition and the face attributes to detect.

      - **FaceSearch** *(dict) --*

        Face search settings to use on a streaming video.

        - **CollectionId** *(string) --*

          The ID of a collection that contains faces that you want to search for.

        - **FaceMatchThreshold** *(float) --*

          Minimum face match confidence score that must be met to return a result for a recognized
          face. Default is 70. 0 is the lowest confidence. 100 is the highest confidence.
    """


_ClientDetectFacesImageS3ObjectTypeDef = TypedDict(
    "_ClientDetectFacesImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDetectFacesImageS3ObjectTypeDef(_ClientDetectFacesImageS3ObjectTypeDef):
    """
    Type definition for `ClientDetectFacesImage` `S3Object`

    Identifies an S3 object as the image source.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientDetectFacesImageTypeDef = TypedDict(
    "_ClientDetectFacesImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectFacesImageS3ObjectTypeDef},
    total=False,
)


class ClientDetectFacesImageTypeDef(_ClientDetectFacesImageTypeDef):
    """
    Type definition for `ClientDetectFaces` `Image`

    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes is not supported.

    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image
    bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.

    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.

    - **S3Object** *(dict) --*

      Identifies an S3 object as the image source.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef(
    _ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `AgeRange`

    The estimated age range, in years, for the face. Low represents the lowest estimated age
    and High represents the highest estimated age.

    - **Low** *(integer) --*

      The lowest estimated age.

    - **High** *(integer) --*

      The highest estimated age.
    """


_ClientDetectFacesResponseFaceDetailsBeardTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsBeardTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsBeardTypeDef(
    _ClientDetectFacesResponseFaceDetailsBeardTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `Beard`

    Indicates whether or not the face has a beard, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has beard or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef(
    _ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `BoundingBox`

    Bounding box of the face. Default attribute.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientDetectFacesResponseFaceDetailsEmotionsTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsEmotionsTypeDef",
    {"Type": str, "Confidence": float},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsEmotionsTypeDef(
    _ClientDetectFacesResponseFaceDetailsEmotionsTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `Emotions`

    The emotions that appear to be expressed on the face, and the confidence level in the
    determination. The API is only making a determination of the physical appearance of a
    person's face. It is not a determination of the person’s internal emotional state and
    should not be used in such a way. For example, a person pretending to have a sad face
    might not be sad emotionally.

    - **Type** *(string) --*

      Type of emotion detected.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef(
    _ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `Eyeglasses`

    Indicates whether or not the face is wearing eye glasses, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing eye glasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef(
    _ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `EyesOpen`

    Indicates whether or not the eyes on the face are open, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the eyes on the face are open.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientDetectFacesResponseFaceDetailsGenderTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsGenderTypeDef",
    {"Value": str, "Confidence": float},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsGenderTypeDef(
    _ClientDetectFacesResponseFaceDetailsGenderTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `Gender`

    Gender of the face and the confidence level in the determination.

    - **Value** *(string) --*

      Gender of the face.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientDetectFacesResponseFaceDetailsLandmarksTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsLandmarksTypeDef",
    {"Type": str, "X": float, "Y": float},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsLandmarksTypeDef(
    _ClientDetectFacesResponseFaceDetailsLandmarksTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `Landmarks`

    Indicates the location of the landmark on the face.

    - **Type** *(string) --*

      Type of landmark.

    - **X** *(float) --*

      The x-coordinate from the top left of the landmark expressed as the ratio of the
      width of the image. For example, if the image is 700 x 200 and the x-coordinate of
      the landmark is at 350 pixels, this value is 0.5.

    - **Y** *(float) --*

      The y-coordinate from the top left of the landmark expressed as the ratio of the
      height of the image. For example, if the image is 700 x 200 and the y-coordinate of
      the landmark is at 100 pixels, this value is 0.5.
    """


_ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef(
    _ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `MouthOpen`

    Indicates whether or not the mouth on the face is open, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the mouth on the face is open or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientDetectFacesResponseFaceDetailsMustacheTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsMustacheTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsMustacheTypeDef(
    _ClientDetectFacesResponseFaceDetailsMustacheTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `Mustache`

    Indicates whether or not the face has a mustache, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has mustache or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientDetectFacesResponseFaceDetailsPoseTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsPoseTypeDef",
    {"Roll": float, "Yaw": float, "Pitch": float},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsPoseTypeDef(
    _ClientDetectFacesResponseFaceDetailsPoseTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `Pose`

    Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
    attribute.

    - **Roll** *(float) --*

      Value representing the face rotation on the roll axis.

    - **Yaw** *(float) --*

      Value representing the face rotation on the yaw axis.

    - **Pitch** *(float) --*

      Value representing the face rotation on the pitch axis.
    """


_ClientDetectFacesResponseFaceDetailsQualityTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsQualityTypeDef",
    {"Brightness": float, "Sharpness": float},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsQualityTypeDef(
    _ClientDetectFacesResponseFaceDetailsQualityTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `Quality`

    Identifies image brightness and sharpness. Default attribute.

    - **Brightness** *(float) --*

      Value representing brightness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a brighter face image.

    - **Sharpness** *(float) --*

      Value representing sharpness of the face. The service returns a value between 0 and 100
      (inclusive). A higher value indicates a sharper face image.
    """


_ClientDetectFacesResponseFaceDetailsSmileTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsSmileTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsSmileTypeDef(
    _ClientDetectFacesResponseFaceDetailsSmileTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `Smile`

    Indicates whether or not the face is smiling, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is smiling or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientDetectFacesResponseFaceDetailsSunglassesTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsSunglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsSunglassesTypeDef(
    _ClientDetectFacesResponseFaceDetailsSunglassesTypeDef
):
    """
    Type definition for `ClientDetectFacesResponseFaceDetails` `Sunglasses`

    Indicates whether or not the face is wearing sunglasses, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing sunglasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientDetectFacesResponseFaceDetailsTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsTypeDef",
    {
        "BoundingBox": ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef,
        "AgeRange": ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef,
        "Smile": ClientDetectFacesResponseFaceDetailsSmileTypeDef,
        "Eyeglasses": ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef,
        "Sunglasses": ClientDetectFacesResponseFaceDetailsSunglassesTypeDef,
        "Gender": ClientDetectFacesResponseFaceDetailsGenderTypeDef,
        "Beard": ClientDetectFacesResponseFaceDetailsBeardTypeDef,
        "Mustache": ClientDetectFacesResponseFaceDetailsMustacheTypeDef,
        "EyesOpen": ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef,
        "MouthOpen": ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef,
        "Emotions": List[ClientDetectFacesResponseFaceDetailsEmotionsTypeDef],
        "Landmarks": List[ClientDetectFacesResponseFaceDetailsLandmarksTypeDef],
        "Pose": ClientDetectFacesResponseFaceDetailsPoseTypeDef,
        "Quality": ClientDetectFacesResponseFaceDetailsQualityTypeDef,
        "Confidence": float,
    },
    total=False,
)


class ClientDetectFacesResponseFaceDetailsTypeDef(
    _ClientDetectFacesResponseFaceDetailsTypeDef
):
    """
    Type definition for `ClientDetectFacesResponse` `FaceDetails`

    Structure containing attributes of the face that the algorithm detected.

    A ``FaceDetail`` object contains either the default facial attributes or all facial
    attributes. The default attributes are ``BoundingBox`` , ``Confidence`` , ``Landmarks`` ,
    ``Pose`` , and ``Quality`` .

      GetFaceDetection is the only Amazon Rekognition Video stored video operation that can
      return a ``FaceDetail`` object with all attributes. To specify which attributes to
      return, use the ``FaceAttributes`` input parameter for  StartFaceDetection . The
      following Amazon Rekognition Video operations return only the default attributes. The
      corresponding Start operations don't have a ``FaceAttributes`` input parameter.

    * GetCelebrityRecognition

    * GetPersonTracking

    * GetFaceSearch

    The Amazon Rekognition Image  DetectFaces and  IndexFaces operations can return all facial
    attributes. To specify which attributes to return, use the ``Attributes`` input parameter
    for ``DetectFaces`` . For ``IndexFaces`` , use the ``DetectAttributes`` input parameter.

    - **BoundingBox** *(dict) --*

      Bounding box of the face. Default attribute.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **AgeRange** *(dict) --*

      The estimated age range, in years, for the face. Low represents the lowest estimated age
      and High represents the highest estimated age.

      - **Low** *(integer) --*

        The lowest estimated age.

      - **High** *(integer) --*

        The highest estimated age.

    - **Smile** *(dict) --*

      Indicates whether or not the face is smiling, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is smiling or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Eyeglasses** *(dict) --*

      Indicates whether or not the face is wearing eye glasses, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing eye glasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Sunglasses** *(dict) --*

      Indicates whether or not the face is wearing sunglasses, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing sunglasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Gender** *(dict) --*

      Gender of the face and the confidence level in the determination.

      - **Value** *(string) --*

        Gender of the face.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Beard** *(dict) --*

      Indicates whether or not the face has a beard, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has beard or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Mustache** *(dict) --*

      Indicates whether or not the face has a mustache, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has mustache or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **EyesOpen** *(dict) --*

      Indicates whether or not the eyes on the face are open, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the eyes on the face are open.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **MouthOpen** *(dict) --*

      Indicates whether or not the mouth on the face is open, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the mouth on the face is open or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Emotions** *(list) --*

      The emotions that appear to be expressed on the face, and the confidence level in the
      determination. The API is only making a determination of the physical appearance of a
      person's face. It is not a determination of the person’s internal emotional state and
      should not be used in such a way. For example, a person pretending to have a sad face
      might not be sad emotionally.

      - *(dict) --*

        The emotions that appear to be expressed on the face, and the confidence level in the
        determination. The API is only making a determination of the physical appearance of a
        person's face. It is not a determination of the person’s internal emotional state and
        should not be used in such a way. For example, a person pretending to have a sad face
        might not be sad emotionally.

        - **Type** *(string) --*

          Type of emotion detected.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

    - **Landmarks** *(list) --*

      Indicates the location of landmarks on the face. Default attribute.

      - *(dict) --*

        Indicates the location of the landmark on the face.

        - **Type** *(string) --*

          Type of landmark.

        - **X** *(float) --*

          The x-coordinate from the top left of the landmark expressed as the ratio of the
          width of the image. For example, if the image is 700 x 200 and the x-coordinate of
          the landmark is at 350 pixels, this value is 0.5.

        - **Y** *(float) --*

          The y-coordinate from the top left of the landmark expressed as the ratio of the
          height of the image. For example, if the image is 700 x 200 and the y-coordinate of
          the landmark is at 100 pixels, this value is 0.5.

    - **Pose** *(dict) --*

      Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
      attribute.

      - **Roll** *(float) --*

        Value representing the face rotation on the roll axis.

      - **Yaw** *(float) --*

        Value representing the face rotation on the yaw axis.

      - **Pitch** *(float) --*

        Value representing the face rotation on the pitch axis.

    - **Quality** *(dict) --*

      Identifies image brightness and sharpness. Default attribute.

      - **Brightness** *(float) --*

        Value representing brightness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a brighter face image.

      - **Sharpness** *(float) --*

        Value representing sharpness of the face. The service returns a value between 0 and 100
        (inclusive). A higher value indicates a sharper face image.

    - **Confidence** *(float) --*

      Confidence level that the bounding box contains a face (and not a different object such
      as a tree). Default attribute.
    """


_ClientDetectFacesResponseTypeDef = TypedDict(
    "_ClientDetectFacesResponseTypeDef",
    {
        "FaceDetails": List[ClientDetectFacesResponseFaceDetailsTypeDef],
        "OrientationCorrection": str,
    },
    total=False,
)


class ClientDetectFacesResponseTypeDef(_ClientDetectFacesResponseTypeDef):
    """
    Type definition for `ClientDetectFaces` `Response`

    - **FaceDetails** *(list) --*

      Details of each face found in the image.

      - *(dict) --*

        Structure containing attributes of the face that the algorithm detected.

        A ``FaceDetail`` object contains either the default facial attributes or all facial
        attributes. The default attributes are ``BoundingBox`` , ``Confidence`` , ``Landmarks`` ,
        ``Pose`` , and ``Quality`` .

          GetFaceDetection is the only Amazon Rekognition Video stored video operation that can
          return a ``FaceDetail`` object with all attributes. To specify which attributes to
          return, use the ``FaceAttributes`` input parameter for  StartFaceDetection . The
          following Amazon Rekognition Video operations return only the default attributes. The
          corresponding Start operations don't have a ``FaceAttributes`` input parameter.

        * GetCelebrityRecognition

        * GetPersonTracking

        * GetFaceSearch

        The Amazon Rekognition Image  DetectFaces and  IndexFaces operations can return all facial
        attributes. To specify which attributes to return, use the ``Attributes`` input parameter
        for ``DetectFaces`` . For ``IndexFaces`` , use the ``DetectAttributes`` input parameter.

        - **BoundingBox** *(dict) --*

          Bounding box of the face. Default attribute.

          - **Width** *(float) --*

            Width of the bounding box as a ratio of the overall image width.

          - **Height** *(float) --*

            Height of the bounding box as a ratio of the overall image height.

          - **Left** *(float) --*

            Left coordinate of the bounding box as a ratio of overall image width.

          - **Top** *(float) --*

            Top coordinate of the bounding box as a ratio of overall image height.

        - **AgeRange** *(dict) --*

          The estimated age range, in years, for the face. Low represents the lowest estimated age
          and High represents the highest estimated age.

          - **Low** *(integer) --*

            The lowest estimated age.

          - **High** *(integer) --*

            The highest estimated age.

        - **Smile** *(dict) --*

          Indicates whether or not the face is smiling, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face is smiling or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Eyeglasses** *(dict) --*

          Indicates whether or not the face is wearing eye glasses, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face is wearing eye glasses or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Sunglasses** *(dict) --*

          Indicates whether or not the face is wearing sunglasses, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face is wearing sunglasses or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Gender** *(dict) --*

          Gender of the face and the confidence level in the determination.

          - **Value** *(string) --*

            Gender of the face.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Beard** *(dict) --*

          Indicates whether or not the face has a beard, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face has beard or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Mustache** *(dict) --*

          Indicates whether or not the face has a mustache, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face has mustache or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **EyesOpen** *(dict) --*

          Indicates whether or not the eyes on the face are open, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the eyes on the face are open.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **MouthOpen** *(dict) --*

          Indicates whether or not the mouth on the face is open, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the mouth on the face is open or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Emotions** *(list) --*

          The emotions that appear to be expressed on the face, and the confidence level in the
          determination. The API is only making a determination of the physical appearance of a
          person's face. It is not a determination of the person’s internal emotional state and
          should not be used in such a way. For example, a person pretending to have a sad face
          might not be sad emotionally.

          - *(dict) --*

            The emotions that appear to be expressed on the face, and the confidence level in the
            determination. The API is only making a determination of the physical appearance of a
            person's face. It is not a determination of the person’s internal emotional state and
            should not be used in such a way. For example, a person pretending to have a sad face
            might not be sad emotionally.

            - **Type** *(string) --*

              Type of emotion detected.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

        - **Landmarks** *(list) --*

          Indicates the location of landmarks on the face. Default attribute.

          - *(dict) --*

            Indicates the location of the landmark on the face.

            - **Type** *(string) --*

              Type of landmark.

            - **X** *(float) --*

              The x-coordinate from the top left of the landmark expressed as the ratio of the
              width of the image. For example, if the image is 700 x 200 and the x-coordinate of
              the landmark is at 350 pixels, this value is 0.5.

            - **Y** *(float) --*

              The y-coordinate from the top left of the landmark expressed as the ratio of the
              height of the image. For example, if the image is 700 x 200 and the y-coordinate of
              the landmark is at 100 pixels, this value is 0.5.

        - **Pose** *(dict) --*

          Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
          attribute.

          - **Roll** *(float) --*

            Value representing the face rotation on the roll axis.

          - **Yaw** *(float) --*

            Value representing the face rotation on the yaw axis.

          - **Pitch** *(float) --*

            Value representing the face rotation on the pitch axis.

        - **Quality** *(dict) --*

          Identifies image brightness and sharpness. Default attribute.

          - **Brightness** *(float) --*

            Value representing brightness of the face. The service returns a value between 0 and
            100 (inclusive). A higher value indicates a brighter face image.

          - **Sharpness** *(float) --*

            Value representing sharpness of the face. The service returns a value between 0 and 100
            (inclusive). A higher value indicates a sharper face image.

        - **Confidence** *(float) --*

          Confidence level that the bounding box contains a face (and not a different object such
          as a tree). Default attribute.

    - **OrientationCorrection** *(string) --*

      The value of ``OrientationCorrection`` is always null.

      If the input image is in .jpeg format, it might contain exchangeable image file format (Exif)
      metadata that includes the image's orientation. Amazon Rekognition uses this orientation
      information to perform image correction. The bounding box coordinates are translated to
      represent object locations after the orientation information in the Exif metadata is used to
      correct the image orientation. Images in .png format don't contain Exif metadata.

      Amazon Rekognition doesn’t perform image correction for images in .png format and .jpeg
      images without orientation information in the image Exif metadata. The bounding box
      coordinates aren't translated and represent the object locations before the image is rotated.
    """


_ClientDetectLabelsImageS3ObjectTypeDef = TypedDict(
    "_ClientDetectLabelsImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDetectLabelsImageS3ObjectTypeDef(_ClientDetectLabelsImageS3ObjectTypeDef):
    """
    Type definition for `ClientDetectLabelsImage` `S3Object`

    Identifies an S3 object as the image source.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientDetectLabelsImageTypeDef = TypedDict(
    "_ClientDetectLabelsImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectLabelsImageS3ObjectTypeDef},
    total=False,
)


class ClientDetectLabelsImageTypeDef(_ClientDetectLabelsImageTypeDef):
    """
    Type definition for `ClientDetectLabels` `Image`

    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing image bytes is not supported. Images stored in an S3 Bucket do
    not need to be base64-encoded.

    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image
    bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.

    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.

    - **S3Object** *(dict) --*

      Identifies an S3 object as the image source.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef = TypedDict(
    "_ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef(
    _ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef
):
    """
    Type definition for `ClientDetectLabelsResponseLabelsInstances` `BoundingBox`

    The position of the label instance on the image.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientDetectLabelsResponseLabelsInstancesTypeDef = TypedDict(
    "_ClientDetectLabelsResponseLabelsInstancesTypeDef",
    {
        "BoundingBox": ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef,
        "Confidence": float,
    },
    total=False,
)


class ClientDetectLabelsResponseLabelsInstancesTypeDef(
    _ClientDetectLabelsResponseLabelsInstancesTypeDef
):
    """
    Type definition for `ClientDetectLabelsResponseLabels` `Instances`

    An instance of a label returned by Amazon Rekognition Image ( DetectLabels ) or by
    Amazon Rekognition Video ( GetLabelDetection ).

    - **BoundingBox** *(dict) --*

      The position of the label instance on the image.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **Confidence** *(float) --*

      The confidence that Amazon Rekognition has in the accuracy of the bounding box.
    """


_ClientDetectLabelsResponseLabelsParentsTypeDef = TypedDict(
    "_ClientDetectLabelsResponseLabelsParentsTypeDef", {"Name": str}, total=False
)


class ClientDetectLabelsResponseLabelsParentsTypeDef(
    _ClientDetectLabelsResponseLabelsParentsTypeDef
):
    """
    Type definition for `ClientDetectLabelsResponseLabels` `Parents`

    A parent label for a label. A label can have 0, 1, or more parents.

    - **Name** *(string) --*

      The name of the parent label.
    """


_ClientDetectLabelsResponseLabelsTypeDef = TypedDict(
    "_ClientDetectLabelsResponseLabelsTypeDef",
    {
        "Name": str,
        "Confidence": float,
        "Instances": List[ClientDetectLabelsResponseLabelsInstancesTypeDef],
        "Parents": List[ClientDetectLabelsResponseLabelsParentsTypeDef],
    },
    total=False,
)


class ClientDetectLabelsResponseLabelsTypeDef(_ClientDetectLabelsResponseLabelsTypeDef):
    """
    Type definition for `ClientDetectLabelsResponse` `Labels`

    Structure containing details about the detected label, including the name, detected
    instances, parent labels, and level of confidence.

    - **Name** *(string) --*

      The name (label) of the object or scene.

    - **Confidence** *(float) --*

      Level of confidence.

    - **Instances** *(list) --*

      If ``Label`` represents an object, ``Instances`` contains the bounding boxes for each
      instance of the detected object. Bounding boxes are returned for common object labels
      such as people, cars, furniture, apparel or pets.

      - *(dict) --*

        An instance of a label returned by Amazon Rekognition Image ( DetectLabels ) or by
        Amazon Rekognition Video ( GetLabelDetection ).

        - **BoundingBox** *(dict) --*

          The position of the label instance on the image.

          - **Width** *(float) --*

            Width of the bounding box as a ratio of the overall image width.

          - **Height** *(float) --*

            Height of the bounding box as a ratio of the overall image height.

          - **Left** *(float) --*

            Left coordinate of the bounding box as a ratio of overall image width.

          - **Top** *(float) --*

            Top coordinate of the bounding box as a ratio of overall image height.

        - **Confidence** *(float) --*

          The confidence that Amazon Rekognition has in the accuracy of the bounding box.

    - **Parents** *(list) --*

      The parent labels for a label. The response includes all ancestor labels.

      - *(dict) --*

        A parent label for a label. A label can have 0, 1, or more parents.

        - **Name** *(string) --*

          The name of the parent label.
    """


_ClientDetectLabelsResponseTypeDef = TypedDict(
    "_ClientDetectLabelsResponseTypeDef",
    {
        "Labels": List[ClientDetectLabelsResponseLabelsTypeDef],
        "OrientationCorrection": str,
        "LabelModelVersion": str,
    },
    total=False,
)


class ClientDetectLabelsResponseTypeDef(_ClientDetectLabelsResponseTypeDef):
    """
    Type definition for `ClientDetectLabels` `Response`

    - **Labels** *(list) --*

      An array of labels for the real-world objects detected.

      - *(dict) --*

        Structure containing details about the detected label, including the name, detected
        instances, parent labels, and level of confidence.

        - **Name** *(string) --*

          The name (label) of the object or scene.

        - **Confidence** *(float) --*

          Level of confidence.

        - **Instances** *(list) --*

          If ``Label`` represents an object, ``Instances`` contains the bounding boxes for each
          instance of the detected object. Bounding boxes are returned for common object labels
          such as people, cars, furniture, apparel or pets.

          - *(dict) --*

            An instance of a label returned by Amazon Rekognition Image ( DetectLabels ) or by
            Amazon Rekognition Video ( GetLabelDetection ).

            - **BoundingBox** *(dict) --*

              The position of the label instance on the image.

              - **Width** *(float) --*

                Width of the bounding box as a ratio of the overall image width.

              - **Height** *(float) --*

                Height of the bounding box as a ratio of the overall image height.

              - **Left** *(float) --*

                Left coordinate of the bounding box as a ratio of overall image width.

              - **Top** *(float) --*

                Top coordinate of the bounding box as a ratio of overall image height.

            - **Confidence** *(float) --*

              The confidence that Amazon Rekognition has in the accuracy of the bounding box.

        - **Parents** *(list) --*

          The parent labels for a label. The response includes all ancestor labels.

          - *(dict) --*

            A parent label for a label. A label can have 0, 1, or more parents.

            - **Name** *(string) --*

              The name of the parent label.

    - **OrientationCorrection** *(string) --*

      The value of ``OrientationCorrection`` is always null.

      If the input image is in .jpeg format, it might contain exchangeable image file format (Exif)
      metadata that includes the image's orientation. Amazon Rekognition uses this orientation
      information to perform image correction. The bounding box coordinates are translated to
      represent object locations after the orientation information in the Exif metadata is used to
      correct the image orientation. Images in .png format don't contain Exif metadata.

      Amazon Rekognition doesn’t perform image correction for images in .png format and .jpeg
      images without orientation information in the image Exif metadata. The bounding box
      coordinates aren't translated and represent the object locations before the image is rotated.

    - **LabelModelVersion** *(string) --*

      Version number of the label detection model that was used to detect labels.
    """


_ClientDetectModerationLabelsImageS3ObjectTypeDef = TypedDict(
    "_ClientDetectModerationLabelsImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDetectModerationLabelsImageS3ObjectTypeDef(
    _ClientDetectModerationLabelsImageS3ObjectTypeDef
):
    """
    Type definition for `ClientDetectModerationLabelsImage` `S3Object`

    Identifies an S3 object as the image source.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientDetectModerationLabelsImageTypeDef = TypedDict(
    "_ClientDetectModerationLabelsImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectModerationLabelsImageS3ObjectTypeDef},
    total=False,
)


class ClientDetectModerationLabelsImageTypeDef(
    _ClientDetectModerationLabelsImageTypeDef
):
    """
    Type definition for `ClientDetectModerationLabels` `Image`

    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes is not supported.

    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image
    bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.

    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.

    - **S3Object** *(dict) --*

      Identifies an S3 object as the image source.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientDetectModerationLabelsResponseModerationLabelsTypeDef = TypedDict(
    "_ClientDetectModerationLabelsResponseModerationLabelsTypeDef",
    {"Confidence": float, "Name": str, "ParentName": str},
    total=False,
)


class ClientDetectModerationLabelsResponseModerationLabelsTypeDef(
    _ClientDetectModerationLabelsResponseModerationLabelsTypeDef
):
    """
    Type definition for `ClientDetectModerationLabelsResponse` `ModerationLabels`

    Provides information about a single type of unsafe content found in an image or video. Each
    type of moderated content has a label within a hierarchical taxonomy. For more information,
    see Detecting Unsafe Content in the Amazon Rekognition Developer Guide.

    - **Confidence** *(float) --*

      Specifies the confidence that Amazon Rekognition has that the label has been correctly
      identified.

      If you don't specify the ``MinConfidence`` parameter in the call to
      ``DetectModerationLabels`` , the operation returns labels with a confidence value greater
      than or equal to 50 percent.

    - **Name** *(string) --*

      The label name for the type of unsafe content detected in the image.

    - **ParentName** *(string) --*

      The name for the parent label. Labels at the top level of the hierarchy have the parent
      label ``""`` .
    """


_ClientDetectModerationLabelsResponseTypeDef = TypedDict(
    "_ClientDetectModerationLabelsResponseTypeDef",
    {
        "ModerationLabels": List[
            ClientDetectModerationLabelsResponseModerationLabelsTypeDef
        ],
        "ModerationModelVersion": str,
    },
    total=False,
)


class ClientDetectModerationLabelsResponseTypeDef(
    _ClientDetectModerationLabelsResponseTypeDef
):
    """
    Type definition for `ClientDetectModerationLabels` `Response`

    - **ModerationLabels** *(list) --*

      Array of detected Moderation labels and the time, in milliseconds from the start of the
      video, they were detected.

      - *(dict) --*

        Provides information about a single type of unsafe content found in an image or video. Each
        type of moderated content has a label within a hierarchical taxonomy. For more information,
        see Detecting Unsafe Content in the Amazon Rekognition Developer Guide.

        - **Confidence** *(float) --*

          Specifies the confidence that Amazon Rekognition has that the label has been correctly
          identified.

          If you don't specify the ``MinConfidence`` parameter in the call to
          ``DetectModerationLabels`` , the operation returns labels with a confidence value greater
          than or equal to 50 percent.

        - **Name** *(string) --*

          The label name for the type of unsafe content detected in the image.

        - **ParentName** *(string) --*

          The name for the parent label. Labels at the top level of the hierarchy have the parent
          label ``""`` .

    - **ModerationModelVersion** *(string) --*

      Version number of the moderation detection model that was used to detect unsafe content.
    """


_ClientDetectTextImageS3ObjectTypeDef = TypedDict(
    "_ClientDetectTextImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDetectTextImageS3ObjectTypeDef(_ClientDetectTextImageS3ObjectTypeDef):
    """
    Type definition for `ClientDetectTextImage` `S3Object`

    Identifies an S3 object as the image source.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientDetectTextImageTypeDef = TypedDict(
    "_ClientDetectTextImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectTextImageS3ObjectTypeDef},
    total=False,
)


class ClientDetectTextImageTypeDef(_ClientDetectTextImageTypeDef):
    """
    Type definition for `ClientDetectText` `Image`

    The input image as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call
    Amazon Rekognition operations, you can't pass image bytes.

    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image
    bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.

    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.

    - **S3Object** *(dict) --*

      Identifies an S3 object as the image source.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef = TypedDict(
    "_ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef(
    _ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef
):
    """
    Type definition for `ClientDetectTextResponseTextDetectionsGeometry` `BoundingBox`

    An axis-aligned coarse representation of the detected text's location on the image.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef = TypedDict(
    "_ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef",
    {"X": float, "Y": float},
    total=False,
)


class ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef(
    _ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef
):
    """
    Type definition for `ClientDetectTextResponseTextDetectionsGeometry` `Polygon`

    The X and Y coordinates of a point on an image. The X and Y values returned are
    ratios of the overall image size. For example, if the input image is 700x200 and the
    operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel
    coordinate on the image.

    An array of ``Point`` objects, ``Polygon`` , is returned by  DetectText . ``Polygon``
    represents a fine-grained polygon around detected text. For more information, see
    Geometry in the Amazon Rekognition Developer Guide.

    - **X** *(float) --*

      The value of the X coordinate for a point on a ``Polygon`` .

    - **Y** *(float) --*

      The value of the Y coordinate for a point on a ``Polygon`` .
    """


_ClientDetectTextResponseTextDetectionsGeometryTypeDef = TypedDict(
    "_ClientDetectTextResponseTextDetectionsGeometryTypeDef",
    {
        "BoundingBox": ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef],
    },
    total=False,
)


class ClientDetectTextResponseTextDetectionsGeometryTypeDef(
    _ClientDetectTextResponseTextDetectionsGeometryTypeDef
):
    """
    Type definition for `ClientDetectTextResponseTextDetections` `Geometry`

    The location of the detected text on the image. Includes an axis aligned coarse bounding
    box surrounding the text and a finer grain polygon for more accurate spatial information.

    - **BoundingBox** *(dict) --*

      An axis-aligned coarse representation of the detected text's location on the image.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **Polygon** *(list) --*

      Within the bounding box, a fine-grained polygon around the detected text.

      - *(dict) --*

        The X and Y coordinates of a point on an image. The X and Y values returned are
        ratios of the overall image size. For example, if the input image is 700x200 and the
        operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel
        coordinate on the image.

        An array of ``Point`` objects, ``Polygon`` , is returned by  DetectText . ``Polygon``
        represents a fine-grained polygon around detected text. For more information, see
        Geometry in the Amazon Rekognition Developer Guide.

        - **X** *(float) --*

          The value of the X coordinate for a point on a ``Polygon`` .

        - **Y** *(float) --*

          The value of the Y coordinate for a point on a ``Polygon`` .
    """


_ClientDetectTextResponseTextDetectionsTypeDef = TypedDict(
    "_ClientDetectTextResponseTextDetectionsTypeDef",
    {
        "DetectedText": str,
        "Type": str,
        "Id": int,
        "ParentId": int,
        "Confidence": float,
        "Geometry": ClientDetectTextResponseTextDetectionsGeometryTypeDef,
    },
    total=False,
)


class ClientDetectTextResponseTextDetectionsTypeDef(
    _ClientDetectTextResponseTextDetectionsTypeDef
):
    """
    Type definition for `ClientDetectTextResponse` `TextDetections`

    Information about a word or line of text detected by  DetectText .

    The ``DetectedText`` field contains the text that Amazon Rekognition detected in the image.

    Every word and line has an identifier (``Id`` ). Each word belongs to a line and has a
    parent identifier (``ParentId`` ) that identifies the line of text in which the word
    appears. The word ``Id`` is also an index for the word within a line of words.

    For more information, see Detecting Text in the Amazon Rekognition Developer Guide.

    - **DetectedText** *(string) --*

      The word or line of text recognized by Amazon Rekognition.

    - **Type** *(string) --*

      The type of text that was detected.

    - **Id** *(integer) --*

      The identifier for the detected text. The identifier is only unique for a single call to
      ``DetectText`` .

    - **ParentId** *(integer) --*

      The Parent identifier for the detected text identified by the value of ``ID`` . If the
      type of detected text is ``LINE`` , the value of ``ParentId`` is ``Null`` .

    - **Confidence** *(float) --*

      The confidence that Amazon Rekognition has in the accuracy of the detected text and the
      accuracy of the geometry points around the detected text.

    - **Geometry** *(dict) --*

      The location of the detected text on the image. Includes an axis aligned coarse bounding
      box surrounding the text and a finer grain polygon for more accurate spatial information.

      - **BoundingBox** *(dict) --*

        An axis-aligned coarse representation of the detected text's location on the image.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **Polygon** *(list) --*

        Within the bounding box, a fine-grained polygon around the detected text.

        - *(dict) --*

          The X and Y coordinates of a point on an image. The X and Y values returned are
          ratios of the overall image size. For example, if the input image is 700x200 and the
          operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel
          coordinate on the image.

          An array of ``Point`` objects, ``Polygon`` , is returned by  DetectText . ``Polygon``
          represents a fine-grained polygon around detected text. For more information, see
          Geometry in the Amazon Rekognition Developer Guide.

          - **X** *(float) --*

            The value of the X coordinate for a point on a ``Polygon`` .

          - **Y** *(float) --*

            The value of the Y coordinate for a point on a ``Polygon`` .
    """


_ClientDetectTextResponseTypeDef = TypedDict(
    "_ClientDetectTextResponseTypeDef",
    {"TextDetections": List[ClientDetectTextResponseTextDetectionsTypeDef]},
    total=False,
)


class ClientDetectTextResponseTypeDef(_ClientDetectTextResponseTypeDef):
    """
    Type definition for `ClientDetectText` `Response`

    - **TextDetections** *(list) --*

      An array of text that was detected in the input image.

      - *(dict) --*

        Information about a word or line of text detected by  DetectText .

        The ``DetectedText`` field contains the text that Amazon Rekognition detected in the image.

        Every word and line has an identifier (``Id`` ). Each word belongs to a line and has a
        parent identifier (``ParentId`` ) that identifies the line of text in which the word
        appears. The word ``Id`` is also an index for the word within a line of words.

        For more information, see Detecting Text in the Amazon Rekognition Developer Guide.

        - **DetectedText** *(string) --*

          The word or line of text recognized by Amazon Rekognition.

        - **Type** *(string) --*

          The type of text that was detected.

        - **Id** *(integer) --*

          The identifier for the detected text. The identifier is only unique for a single call to
          ``DetectText`` .

        - **ParentId** *(integer) --*

          The Parent identifier for the detected text identified by the value of ``ID`` . If the
          type of detected text is ``LINE`` , the value of ``ParentId`` is ``Null`` .

        - **Confidence** *(float) --*

          The confidence that Amazon Rekognition has in the accuracy of the detected text and the
          accuracy of the geometry points around the detected text.

        - **Geometry** *(dict) --*

          The location of the detected text on the image. Includes an axis aligned coarse bounding
          box surrounding the text and a finer grain polygon for more accurate spatial information.

          - **BoundingBox** *(dict) --*

            An axis-aligned coarse representation of the detected text's location on the image.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **Polygon** *(list) --*

            Within the bounding box, a fine-grained polygon around the detected text.

            - *(dict) --*

              The X and Y coordinates of a point on an image. The X and Y values returned are
              ratios of the overall image size. For example, if the input image is 700x200 and the
              operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel
              coordinate on the image.

              An array of ``Point`` objects, ``Polygon`` , is returned by  DetectText . ``Polygon``
              represents a fine-grained polygon around detected text. For more information, see
              Geometry in the Amazon Rekognition Developer Guide.

              - **X** *(float) --*

                The value of the X coordinate for a point on a ``Polygon`` .

              - **Y** *(float) --*

                The value of the Y coordinate for a point on a ``Polygon`` .
    """


_ClientGetCelebrityInfoResponseTypeDef = TypedDict(
    "_ClientGetCelebrityInfoResponseTypeDef",
    {"Urls": List[str], "Name": str},
    total=False,
)


class ClientGetCelebrityInfoResponseTypeDef(_ClientGetCelebrityInfoResponseTypeDef):
    """
    Type definition for `ClientGetCelebrityInfo` `Response`

    - **Urls** *(list) --*

      An array of URLs pointing to additional celebrity information.

      - *(string) --*

    - **Name** *(string) --*

      The name of the celebrity.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrity` `BoundingBox`

    Bounding box around the body of a celebrity.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `AgeRange`

    The estimated age range, in years, for the face. Low represents the lowest estimated
    age and High represents the highest estimated age.

    - **Low** *(integer) --*

      The lowest estimated age.

    - **High** *(integer) --*

      The highest estimated age.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `Beard`

    Indicates whether or not the face has a beard, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has beard or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `BoundingBox`

    Bounding box of the face. Default attribute.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef",
    {"Type": str, "Confidence": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `Emotions`

    The emotions that appear to be expressed on the face, and the confidence level in
    the determination. The API is only making a determination of the physical
    appearance of a person's face. It is not a determination of the person’s internal
    emotional state and should not be used in such a way. For example, a person
    pretending to have a sad face might not be sad emotionally.

    - **Type** *(string) --*

      Type of emotion detected.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `Eyeglasses`

    Indicates whether or not the face is wearing eye glasses, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing eye glasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `EyesOpen`

    Indicates whether or not the eyes on the face are open, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the eyes on the face are open.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef",
    {"Value": str, "Confidence": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `Gender`

    Gender of the face and the confidence level in the determination.

    - **Value** *(string) --*

      Gender of the face.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef",
    {"Type": str, "X": float, "Y": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `Landmarks`

    Indicates the location of the landmark on the face.

    - **Type** *(string) --*

      Type of landmark.

    - **X** *(float) --*

      The x-coordinate from the top left of the landmark expressed as the ratio of the
      width of the image. For example, if the image is 700 x 200 and the x-coordinate
      of the landmark is at 350 pixels, this value is 0.5.

    - **Y** *(float) --*

      The y-coordinate from the top left of the landmark expressed as the ratio of the
      height of the image. For example, if the image is 700 x 200 and the y-coordinate
      of the landmark is at 100 pixels, this value is 0.5.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `MouthOpen`

    Indicates whether or not the mouth on the face is open, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the mouth on the face is open or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `Mustache`

    Indicates whether or not the face has a mustache, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has mustache or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef",
    {"Roll": float, "Yaw": float, "Pitch": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `Pose`

    Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
    attribute.

    - **Roll** *(float) --*

      Value representing the face rotation on the roll axis.

    - **Yaw** *(float) --*

      Value representing the face rotation on the yaw axis.

    - **Pitch** *(float) --*

      Value representing the face rotation on the pitch axis.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef",
    {"Brightness": float, "Sharpness": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `Quality`

    Identifies image brightness and sharpness. Default attribute.

    - **Brightness** *(float) --*

      Value representing brightness of the face. The service returns a value between 0
      and 100 (inclusive). A higher value indicates a brighter face image.

    - **Sharpness** *(float) --*

      Value representing sharpness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a sharper face image.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `Smile`

    Indicates whether or not the face is smiling, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is smiling or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFace` `Sunglasses`

    Indicates whether or not the face is wearing sunglasses, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing sunglasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef",
    {
        "BoundingBox": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef,
        "AgeRange": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef,
        "Smile": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef,
        "Eyeglasses": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef,
        "Sunglasses": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef,
        "Gender": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef,
        "Beard": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef,
        "Mustache": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef,
        "EyesOpen": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef,
        "MouthOpen": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef,
        "Emotions": List[
            ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef
        ],
        "Landmarks": List[
            ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef
        ],
        "Pose": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef,
        "Quality": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef,
        "Confidence": float,
    },
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebritiesCelebrity` `Face`

    Face details for the recognized celebrity.

    - **BoundingBox** *(dict) --*

      Bounding box of the face. Default attribute.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **AgeRange** *(dict) --*

      The estimated age range, in years, for the face. Low represents the lowest estimated
      age and High represents the highest estimated age.

      - **Low** *(integer) --*

        The lowest estimated age.

      - **High** *(integer) --*

        The highest estimated age.

    - **Smile** *(dict) --*

      Indicates whether or not the face is smiling, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is smiling or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Eyeglasses** *(dict) --*

      Indicates whether or not the face is wearing eye glasses, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing eye glasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Sunglasses** *(dict) --*

      Indicates whether or not the face is wearing sunglasses, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing sunglasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Gender** *(dict) --*

      Gender of the face and the confidence level in the determination.

      - **Value** *(string) --*

        Gender of the face.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Beard** *(dict) --*

      Indicates whether or not the face has a beard, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has beard or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Mustache** *(dict) --*

      Indicates whether or not the face has a mustache, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has mustache or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **EyesOpen** *(dict) --*

      Indicates whether or not the eyes on the face are open, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the eyes on the face are open.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **MouthOpen** *(dict) --*

      Indicates whether or not the mouth on the face is open, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the mouth on the face is open or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Emotions** *(list) --*

      The emotions that appear to be expressed on the face, and the confidence level in the
      determination. The API is only making a determination of the physical appearance of a
      person's face. It is not a determination of the person’s internal emotional state and
      should not be used in such a way. For example, a person pretending to have a sad face
      might not be sad emotionally.

      - *(dict) --*

        The emotions that appear to be expressed on the face, and the confidence level in
        the determination. The API is only making a determination of the physical
        appearance of a person's face. It is not a determination of the person’s internal
        emotional state and should not be used in such a way. For example, a person
        pretending to have a sad face might not be sad emotionally.

        - **Type** *(string) --*

          Type of emotion detected.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

    - **Landmarks** *(list) --*

      Indicates the location of landmarks on the face. Default attribute.

      - *(dict) --*

        Indicates the location of the landmark on the face.

        - **Type** *(string) --*

          Type of landmark.

        - **X** *(float) --*

          The x-coordinate from the top left of the landmark expressed as the ratio of the
          width of the image. For example, if the image is 700 x 200 and the x-coordinate
          of the landmark is at 350 pixels, this value is 0.5.

        - **Y** *(float) --*

          The y-coordinate from the top left of the landmark expressed as the ratio of the
          height of the image. For example, if the image is 700 x 200 and the y-coordinate
          of the landmark is at 100 pixels, this value is 0.5.

    - **Pose** *(dict) --*

      Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
      attribute.

      - **Roll** *(float) --*

        Value representing the face rotation on the roll axis.

      - **Yaw** *(float) --*

        Value representing the face rotation on the yaw axis.

      - **Pitch** *(float) --*

        Value representing the face rotation on the pitch axis.

    - **Quality** *(dict) --*

      Identifies image brightness and sharpness. Default attribute.

      - **Brightness** *(float) --*

        Value representing brightness of the face. The service returns a value between 0
        and 100 (inclusive). A higher value indicates a brighter face image.

      - **Sharpness** *(float) --*

        Value representing sharpness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a sharper face image.

    - **Confidence** *(float) --*

      Confidence level that the bounding box contains a face (and not a different object
      such as a tree). Default attribute.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "Id": str,
        "Confidence": float,
        "BoundingBox": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef,
        "Face": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef,
    },
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponseCelebrities` `Celebrity`

    Information about a recognized celebrity.

    - **Urls** *(list) --*

      An array of URLs pointing to additional celebrity information.

      - *(string) --*

    - **Name** *(string) --*

      The name of the celebrity.

    - **Id** *(string) --*

      The unique identifier for the celebrity.

    - **Confidence** *(float) --*

      The confidence, in percentage, that Amazon Rekognition has that the recognized face is
      the celebrity.

    - **BoundingBox** *(dict) --*

      Bounding box around the body of a celebrity.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **Face** *(dict) --*

      Face details for the recognized celebrity.

      - **BoundingBox** *(dict) --*

        Bounding box of the face. Default attribute.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **AgeRange** *(dict) --*

        The estimated age range, in years, for the face. Low represents the lowest estimated
        age and High represents the highest estimated age.

        - **Low** *(integer) --*

          The lowest estimated age.

        - **High** *(integer) --*

          The highest estimated age.

      - **Smile** *(dict) --*

        Indicates whether or not the face is smiling, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is smiling or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Eyeglasses** *(dict) --*

        Indicates whether or not the face is wearing eye glasses, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is wearing eye glasses or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Sunglasses** *(dict) --*

        Indicates whether or not the face is wearing sunglasses, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is wearing sunglasses or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Gender** *(dict) --*

        Gender of the face and the confidence level in the determination.

        - **Value** *(string) --*

          Gender of the face.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Beard** *(dict) --*

        Indicates whether or not the face has a beard, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face has beard or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Mustache** *(dict) --*

        Indicates whether or not the face has a mustache, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face has mustache or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **EyesOpen** *(dict) --*

        Indicates whether or not the eyes on the face are open, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the eyes on the face are open.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **MouthOpen** *(dict) --*

        Indicates whether or not the mouth on the face is open, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the mouth on the face is open or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Emotions** *(list) --*

        The emotions that appear to be expressed on the face, and the confidence level in the
        determination. The API is only making a determination of the physical appearance of a
        person's face. It is not a determination of the person’s internal emotional state and
        should not be used in such a way. For example, a person pretending to have a sad face
        might not be sad emotionally.

        - *(dict) --*

          The emotions that appear to be expressed on the face, and the confidence level in
          the determination. The API is only making a determination of the physical
          appearance of a person's face. It is not a determination of the person’s internal
          emotional state and should not be used in such a way. For example, a person
          pretending to have a sad face might not be sad emotionally.

          - **Type** *(string) --*

            Type of emotion detected.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

      - **Landmarks** *(list) --*

        Indicates the location of landmarks on the face. Default attribute.

        - *(dict) --*

          Indicates the location of the landmark on the face.

          - **Type** *(string) --*

            Type of landmark.

          - **X** *(float) --*

            The x-coordinate from the top left of the landmark expressed as the ratio of the
            width of the image. For example, if the image is 700 x 200 and the x-coordinate
            of the landmark is at 350 pixels, this value is 0.5.

          - **Y** *(float) --*

            The y-coordinate from the top left of the landmark expressed as the ratio of the
            height of the image. For example, if the image is 700 x 200 and the y-coordinate
            of the landmark is at 100 pixels, this value is 0.5.

      - **Pose** *(dict) --*

        Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
        attribute.

        - **Roll** *(float) --*

          Value representing the face rotation on the roll axis.

        - **Yaw** *(float) --*

          Value representing the face rotation on the yaw axis.

        - **Pitch** *(float) --*

          Value representing the face rotation on the pitch axis.

      - **Quality** *(dict) --*

        Identifies image brightness and sharpness. Default attribute.

        - **Brightness** *(float) --*

          Value representing brightness of the face. The service returns a value between 0
          and 100 (inclusive). A higher value indicates a brighter face image.

        - **Sharpness** *(float) --*

          Value representing sharpness of the face. The service returns a value between 0 and
          100 (inclusive). A higher value indicates a sharper face image.

      - **Confidence** *(float) --*

        Confidence level that the bounding box contains a face (and not a different object
        such as a tree). Default attribute.
    """


_ClientGetCelebrityRecognitionResponseCelebritiesTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesTypeDef",
    {
        "Timestamp": int,
        "Celebrity": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef,
    },
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponse` `Celebrities`

    Information about a detected celebrity and the time the celebrity was detected in a stored
    video. For more information, see GetCelebrityRecognition in the Amazon Rekognition
    Developer Guide.

    - **Timestamp** *(integer) --*

      The time, in milliseconds from the start of the video, that the celebrity was recognized.

    - **Celebrity** *(dict) --*

      Information about a recognized celebrity.

      - **Urls** *(list) --*

        An array of URLs pointing to additional celebrity information.

        - *(string) --*

      - **Name** *(string) --*

        The name of the celebrity.

      - **Id** *(string) --*

        The unique identifier for the celebrity.

      - **Confidence** *(float) --*

        The confidence, in percentage, that Amazon Rekognition has that the recognized face is
        the celebrity.

      - **BoundingBox** *(dict) --*

        Bounding box around the body of a celebrity.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **Face** *(dict) --*

        Face details for the recognized celebrity.

        - **BoundingBox** *(dict) --*

          Bounding box of the face. Default attribute.

          - **Width** *(float) --*

            Width of the bounding box as a ratio of the overall image width.

          - **Height** *(float) --*

            Height of the bounding box as a ratio of the overall image height.

          - **Left** *(float) --*

            Left coordinate of the bounding box as a ratio of overall image width.

          - **Top** *(float) --*

            Top coordinate of the bounding box as a ratio of overall image height.

        - **AgeRange** *(dict) --*

          The estimated age range, in years, for the face. Low represents the lowest estimated
          age and High represents the highest estimated age.

          - **Low** *(integer) --*

            The lowest estimated age.

          - **High** *(integer) --*

            The highest estimated age.

        - **Smile** *(dict) --*

          Indicates whether or not the face is smiling, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face is smiling or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Eyeglasses** *(dict) --*

          Indicates whether or not the face is wearing eye glasses, and the confidence level in
          the determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face is wearing eye glasses or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Sunglasses** *(dict) --*

          Indicates whether or not the face is wearing sunglasses, and the confidence level in
          the determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face is wearing sunglasses or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Gender** *(dict) --*

          Gender of the face and the confidence level in the determination.

          - **Value** *(string) --*

            Gender of the face.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Beard** *(dict) --*

          Indicates whether or not the face has a beard, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face has beard or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Mustache** *(dict) --*

          Indicates whether or not the face has a mustache, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face has mustache or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **EyesOpen** *(dict) --*

          Indicates whether or not the eyes on the face are open, and the confidence level in
          the determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the eyes on the face are open.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **MouthOpen** *(dict) --*

          Indicates whether or not the mouth on the face is open, and the confidence level in
          the determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the mouth on the face is open or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Emotions** *(list) --*

          The emotions that appear to be expressed on the face, and the confidence level in the
          determination. The API is only making a determination of the physical appearance of a
          person's face. It is not a determination of the person’s internal emotional state and
          should not be used in such a way. For example, a person pretending to have a sad face
          might not be sad emotionally.

          - *(dict) --*

            The emotions that appear to be expressed on the face, and the confidence level in
            the determination. The API is only making a determination of the physical
            appearance of a person's face. It is not a determination of the person’s internal
            emotional state and should not be used in such a way. For example, a person
            pretending to have a sad face might not be sad emotionally.

            - **Type** *(string) --*

              Type of emotion detected.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

        - **Landmarks** *(list) --*

          Indicates the location of landmarks on the face. Default attribute.

          - *(dict) --*

            Indicates the location of the landmark on the face.

            - **Type** *(string) --*

              Type of landmark.

            - **X** *(float) --*

              The x-coordinate from the top left of the landmark expressed as the ratio of the
              width of the image. For example, if the image is 700 x 200 and the x-coordinate
              of the landmark is at 350 pixels, this value is 0.5.

            - **Y** *(float) --*

              The y-coordinate from the top left of the landmark expressed as the ratio of the
              height of the image. For example, if the image is 700 x 200 and the y-coordinate
              of the landmark is at 100 pixels, this value is 0.5.

        - **Pose** *(dict) --*

          Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
          attribute.

          - **Roll** *(float) --*

            Value representing the face rotation on the roll axis.

          - **Yaw** *(float) --*

            Value representing the face rotation on the yaw axis.

          - **Pitch** *(float) --*

            Value representing the face rotation on the pitch axis.

        - **Quality** *(dict) --*

          Identifies image brightness and sharpness. Default attribute.

          - **Brightness** *(float) --*

            Value representing brightness of the face. The service returns a value between 0
            and 100 (inclusive). A higher value indicates a brighter face image.

          - **Sharpness** *(float) --*

            Value representing sharpness of the face. The service returns a value between 0 and
            100 (inclusive). A higher value indicates a sharper face image.

        - **Confidence** *(float) --*

          Confidence level that the bounding box contains a face (and not a different object
          such as a tree). Default attribute.
    """


_ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": float,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)


class ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef(
    _ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognitionResponse` `VideoMetadata`

    Information about a video that Amazon Rekognition Video analyzed. ``Videometadata`` is
    returned in every page of paginated responses from a Amazon Rekognition Video operation.

    - **Codec** *(string) --*

      Type of compression used in the analyzed video.

    - **DurationMillis** *(integer) --*

      Length of the video in milliseconds.

    - **Format** *(string) --*

      Format of the analyzed video. Possible values are MP4, MOV and AVI.

    - **FrameRate** *(float) --*

      Number of frames per second in the video.

    - **FrameHeight** *(integer) --*

      Vertical pixel dimension of the video.

    - **FrameWidth** *(integer) --*

      Horizontal pixel dimension of the video.
    """


_ClientGetCelebrityRecognitionResponseTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseTypeDef",
    {
        "JobStatus": str,
        "StatusMessage": str,
        "VideoMetadata": ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef,
        "NextToken": str,
        "Celebrities": List[ClientGetCelebrityRecognitionResponseCelebritiesTypeDef],
    },
    total=False,
)


class ClientGetCelebrityRecognitionResponseTypeDef(
    _ClientGetCelebrityRecognitionResponseTypeDef
):
    """
    Type definition for `ClientGetCelebrityRecognition` `Response`

    - **JobStatus** *(string) --*

      The current status of the celebrity recognition job.

    - **StatusMessage** *(string) --*

      If the job fails, ``StatusMessage`` provides a descriptive error message.

    - **VideoMetadata** *(dict) --*

      Information about a video that Amazon Rekognition Video analyzed. ``Videometadata`` is
      returned in every page of paginated responses from a Amazon Rekognition Video operation.

      - **Codec** *(string) --*

        Type of compression used in the analyzed video.

      - **DurationMillis** *(integer) --*

        Length of the video in milliseconds.

      - **Format** *(string) --*

        Format of the analyzed video. Possible values are MP4, MOV and AVI.

      - **FrameRate** *(float) --*

        Number of frames per second in the video.

      - **FrameHeight** *(integer) --*

        Vertical pixel dimension of the video.

      - **FrameWidth** *(integer) --*

        Horizontal pixel dimension of the video.

    - **NextToken** *(string) --*

      If the response is truncated, Amazon Rekognition Video returns this token that you can use in
      the subsequent request to retrieve the next set of celebrities.

    - **Celebrities** *(list) --*

      Array of celebrities recognized in the video.

      - *(dict) --*

        Information about a detected celebrity and the time the celebrity was detected in a stored
        video. For more information, see GetCelebrityRecognition in the Amazon Rekognition
        Developer Guide.

        - **Timestamp** *(integer) --*

          The time, in milliseconds from the start of the video, that the celebrity was recognized.

        - **Celebrity** *(dict) --*

          Information about a recognized celebrity.

          - **Urls** *(list) --*

            An array of URLs pointing to additional celebrity information.

            - *(string) --*

          - **Name** *(string) --*

            The name of the celebrity.

          - **Id** *(string) --*

            The unique identifier for the celebrity.

          - **Confidence** *(float) --*

            The confidence, in percentage, that Amazon Rekognition has that the recognized face is
            the celebrity.

          - **BoundingBox** *(dict) --*

            Bounding box around the body of a celebrity.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **Face** *(dict) --*

            Face details for the recognized celebrity.

            - **BoundingBox** *(dict) --*

              Bounding box of the face. Default attribute.

              - **Width** *(float) --*

                Width of the bounding box as a ratio of the overall image width.

              - **Height** *(float) --*

                Height of the bounding box as a ratio of the overall image height.

              - **Left** *(float) --*

                Left coordinate of the bounding box as a ratio of overall image width.

              - **Top** *(float) --*

                Top coordinate of the bounding box as a ratio of overall image height.

            - **AgeRange** *(dict) --*

              The estimated age range, in years, for the face. Low represents the lowest estimated
              age and High represents the highest estimated age.

              - **Low** *(integer) --*

                The lowest estimated age.

              - **High** *(integer) --*

                The highest estimated age.

            - **Smile** *(dict) --*

              Indicates whether or not the face is smiling, and the confidence level in the
              determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face is smiling or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Eyeglasses** *(dict) --*

              Indicates whether or not the face is wearing eye glasses, and the confidence level in
              the determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face is wearing eye glasses or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Sunglasses** *(dict) --*

              Indicates whether or not the face is wearing sunglasses, and the confidence level in
              the determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face is wearing sunglasses or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Gender** *(dict) --*

              Gender of the face and the confidence level in the determination.

              - **Value** *(string) --*

                Gender of the face.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Beard** *(dict) --*

              Indicates whether or not the face has a beard, and the confidence level in the
              determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face has beard or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Mustache** *(dict) --*

              Indicates whether or not the face has a mustache, and the confidence level in the
              determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face has mustache or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **EyesOpen** *(dict) --*

              Indicates whether or not the eyes on the face are open, and the confidence level in
              the determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the eyes on the face are open.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **MouthOpen** *(dict) --*

              Indicates whether or not the mouth on the face is open, and the confidence level in
              the determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the mouth on the face is open or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Emotions** *(list) --*

              The emotions that appear to be expressed on the face, and the confidence level in the
              determination. The API is only making a determination of the physical appearance of a
              person's face. It is not a determination of the person’s internal emotional state and
              should not be used in such a way. For example, a person pretending to have a sad face
              might not be sad emotionally.

              - *(dict) --*

                The emotions that appear to be expressed on the face, and the confidence level in
                the determination. The API is only making a determination of the physical
                appearance of a person's face. It is not a determination of the person’s internal
                emotional state and should not be used in such a way. For example, a person
                pretending to have a sad face might not be sad emotionally.

                - **Type** *(string) --*

                  Type of emotion detected.

                - **Confidence** *(float) --*

                  Level of confidence in the determination.

            - **Landmarks** *(list) --*

              Indicates the location of landmarks on the face. Default attribute.

              - *(dict) --*

                Indicates the location of the landmark on the face.

                - **Type** *(string) --*

                  Type of landmark.

                - **X** *(float) --*

                  The x-coordinate from the top left of the landmark expressed as the ratio of the
                  width of the image. For example, if the image is 700 x 200 and the x-coordinate
                  of the landmark is at 350 pixels, this value is 0.5.

                - **Y** *(float) --*

                  The y-coordinate from the top left of the landmark expressed as the ratio of the
                  height of the image. For example, if the image is 700 x 200 and the y-coordinate
                  of the landmark is at 100 pixels, this value is 0.5.

            - **Pose** *(dict) --*

              Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
              attribute.

              - **Roll** *(float) --*

                Value representing the face rotation on the roll axis.

              - **Yaw** *(float) --*

                Value representing the face rotation on the yaw axis.

              - **Pitch** *(float) --*

                Value representing the face rotation on the pitch axis.

            - **Quality** *(dict) --*

              Identifies image brightness and sharpness. Default attribute.

              - **Brightness** *(float) --*

                Value representing brightness of the face. The service returns a value between 0
                and 100 (inclusive). A higher value indicates a brighter face image.

              - **Sharpness** *(float) --*

                Value representing sharpness of the face. The service returns a value between 0 and
                100 (inclusive). A higher value indicates a sharper face image.

            - **Confidence** *(float) --*

              Confidence level that the bounding box contains a face (and not a different object
              such as a tree). Default attribute.
    """


_ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef = TypedDict(
    "_ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef",
    {"Confidence": float, "Name": str, "ParentName": str},
    total=False,
)


class ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef(
    _ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef
):
    """
    Type definition for `ClientGetContentModerationResponseModerationLabels` `ModerationLabel`

    The unsafe content label detected by in the stored video.

    - **Confidence** *(float) --*

      Specifies the confidence that Amazon Rekognition has that the label has been correctly
      identified.

      If you don't specify the ``MinConfidence`` parameter in the call to
      ``DetectModerationLabels`` , the operation returns labels with a confidence value
      greater than or equal to 50 percent.

    - **Name** *(string) --*

      The label name for the type of unsafe content detected in the image.

    - **ParentName** *(string) --*

      The name for the parent label. Labels at the top level of the hierarchy have the parent
      label ``""`` .
    """


_ClientGetContentModerationResponseModerationLabelsTypeDef = TypedDict(
    "_ClientGetContentModerationResponseModerationLabelsTypeDef",
    {
        "Timestamp": int,
        "ModerationLabel": ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef,
    },
    total=False,
)


class ClientGetContentModerationResponseModerationLabelsTypeDef(
    _ClientGetContentModerationResponseModerationLabelsTypeDef
):
    """
    Type definition for `ClientGetContentModerationResponse` `ModerationLabels`

    Information about an unsafe content label detection in a stored video.

    - **Timestamp** *(integer) --*

      Time, in milliseconds from the beginning of the video, that the unsafe content label was
      detected.

    - **ModerationLabel** *(dict) --*

      The unsafe content label detected by in the stored video.

      - **Confidence** *(float) --*

        Specifies the confidence that Amazon Rekognition has that the label has been correctly
        identified.

        If you don't specify the ``MinConfidence`` parameter in the call to
        ``DetectModerationLabels`` , the operation returns labels with a confidence value
        greater than or equal to 50 percent.

      - **Name** *(string) --*

        The label name for the type of unsafe content detected in the image.

      - **ParentName** *(string) --*

        The name for the parent label. Labels at the top level of the hierarchy have the parent
        label ``""`` .
    """


_ClientGetContentModerationResponseVideoMetadataTypeDef = TypedDict(
    "_ClientGetContentModerationResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": float,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)


class ClientGetContentModerationResponseVideoMetadataTypeDef(
    _ClientGetContentModerationResponseVideoMetadataTypeDef
):
    """
    Type definition for `ClientGetContentModerationResponse` `VideoMetadata`

    Information about a video that Amazon Rekognition analyzed. ``Videometadata`` is returned in
    every page of paginated responses from ``GetContentModeration`` .

    - **Codec** *(string) --*

      Type of compression used in the analyzed video.

    - **DurationMillis** *(integer) --*

      Length of the video in milliseconds.

    - **Format** *(string) --*

      Format of the analyzed video. Possible values are MP4, MOV and AVI.

    - **FrameRate** *(float) --*

      Number of frames per second in the video.

    - **FrameHeight** *(integer) --*

      Vertical pixel dimension of the video.

    - **FrameWidth** *(integer) --*

      Horizontal pixel dimension of the video.
    """


_ClientGetContentModerationResponseTypeDef = TypedDict(
    "_ClientGetContentModerationResponseTypeDef",
    {
        "JobStatus": str,
        "StatusMessage": str,
        "VideoMetadata": ClientGetContentModerationResponseVideoMetadataTypeDef,
        "ModerationLabels": List[
            ClientGetContentModerationResponseModerationLabelsTypeDef
        ],
        "NextToken": str,
        "ModerationModelVersion": str,
    },
    total=False,
)


class ClientGetContentModerationResponseTypeDef(
    _ClientGetContentModerationResponseTypeDef
):
    """
    Type definition for `ClientGetContentModeration` `Response`

    - **JobStatus** *(string) --*

      The current status of the unsafe content analysis job.

    - **StatusMessage** *(string) --*

      If the job fails, ``StatusMessage`` provides a descriptive error message.

    - **VideoMetadata** *(dict) --*

      Information about a video that Amazon Rekognition analyzed. ``Videometadata`` is returned in
      every page of paginated responses from ``GetContentModeration`` .

      - **Codec** *(string) --*

        Type of compression used in the analyzed video.

      - **DurationMillis** *(integer) --*

        Length of the video in milliseconds.

      - **Format** *(string) --*

        Format of the analyzed video. Possible values are MP4, MOV and AVI.

      - **FrameRate** *(float) --*

        Number of frames per second in the video.

      - **FrameHeight** *(integer) --*

        Vertical pixel dimension of the video.

      - **FrameWidth** *(integer) --*

        Horizontal pixel dimension of the video.

    - **ModerationLabels** *(list) --*

      The detected unsafe content labels and the time(s) they were detected.

      - *(dict) --*

        Information about an unsafe content label detection in a stored video.

        - **Timestamp** *(integer) --*

          Time, in milliseconds from the beginning of the video, that the unsafe content label was
          detected.

        - **ModerationLabel** *(dict) --*

          The unsafe content label detected by in the stored video.

          - **Confidence** *(float) --*

            Specifies the confidence that Amazon Rekognition has that the label has been correctly
            identified.

            If you don't specify the ``MinConfidence`` parameter in the call to
            ``DetectModerationLabels`` , the operation returns labels with a confidence value
            greater than or equal to 50 percent.

          - **Name** *(string) --*

            The label name for the type of unsafe content detected in the image.

          - **ParentName** *(string) --*

            The name for the parent label. Labels at the top level of the hierarchy have the parent
            label ``""`` .

    - **NextToken** *(string) --*

      If the response is truncated, Amazon Rekognition Video returns this token that you can use in
      the subsequent request to retrieve the next set of unsafe content labels.

    - **ModerationModelVersion** *(string) --*

      Version number of the moderation detection model that was used to detect unsafe content.
    """


_ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `AgeRange`

    The estimated age range, in years, for the face. Low represents the lowest estimated
    age and High represents the highest estimated age.

    - **Low** *(integer) --*

      The lowest estimated age.

    - **High** *(integer) --*

      The highest estimated age.
    """


_ClientGetFaceDetectionResponseFacesFaceBeardTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceBeardTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceBeardTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceBeardTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `Beard`

    Indicates whether or not the face has a beard, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has beard or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `BoundingBox`

    Bounding box of the face. Default attribute.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef",
    {"Type": str, "Confidence": float},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `Emotions`

    The emotions that appear to be expressed on the face, and the confidence level in the
    determination. The API is only making a determination of the physical appearance of a
    person's face. It is not a determination of the person’s internal emotional state and
    should not be used in such a way. For example, a person pretending to have a sad face
    might not be sad emotionally.

    - **Type** *(string) --*

      Type of emotion detected.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `Eyeglasses`

    Indicates whether or not the face is wearing eye glasses, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing eye glasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `EyesOpen`

    Indicates whether or not the eyes on the face are open, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the eyes on the face are open.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceDetectionResponseFacesFaceGenderTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceGenderTypeDef",
    {"Value": str, "Confidence": float},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceGenderTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceGenderTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `Gender`

    Gender of the face and the confidence level in the determination.

    - **Value** *(string) --*

      Gender of the face.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef",
    {"Type": str, "X": float, "Y": float},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `Landmarks`

    Indicates the location of the landmark on the face.

    - **Type** *(string) --*

      Type of landmark.

    - **X** *(float) --*

      The x-coordinate from the top left of the landmark expressed as the ratio of the
      width of the image. For example, if the image is 700 x 200 and the x-coordinate of
      the landmark is at 350 pixels, this value is 0.5.

    - **Y** *(float) --*

      The y-coordinate from the top left of the landmark expressed as the ratio of the
      height of the image. For example, if the image is 700 x 200 and the y-coordinate of
      the landmark is at 100 pixels, this value is 0.5.
    """


_ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `MouthOpen`

    Indicates whether or not the mouth on the face is open, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the mouth on the face is open or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `Mustache`

    Indicates whether or not the face has a mustache, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has mustache or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceDetectionResponseFacesFacePoseTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFacePoseTypeDef",
    {"Roll": float, "Yaw": float, "Pitch": float},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFacePoseTypeDef(
    _ClientGetFaceDetectionResponseFacesFacePoseTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `Pose`

    Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
    attribute.

    - **Roll** *(float) --*

      Value representing the face rotation on the roll axis.

    - **Yaw** *(float) --*

      Value representing the face rotation on the yaw axis.

    - **Pitch** *(float) --*

      Value representing the face rotation on the pitch axis.
    """


_ClientGetFaceDetectionResponseFacesFaceQualityTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceQualityTypeDef",
    {"Brightness": float, "Sharpness": float},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceQualityTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceQualityTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `Quality`

    Identifies image brightness and sharpness. Default attribute.

    - **Brightness** *(float) --*

      Value representing brightness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a brighter face image.

    - **Sharpness** *(float) --*

      Value representing sharpness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a sharper face image.
    """


_ClientGetFaceDetectionResponseFacesFaceSmileTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceSmileTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceSmileTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceSmileTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `Smile`

    Indicates whether or not the face is smiling, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is smiling or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFacesFace` `Sunglasses`

    Indicates whether or not the face is wearing sunglasses, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing sunglasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceDetectionResponseFacesFaceTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceTypeDef",
    {
        "BoundingBox": ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef,
        "AgeRange": ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef,
        "Smile": ClientGetFaceDetectionResponseFacesFaceSmileTypeDef,
        "Eyeglasses": ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef,
        "Sunglasses": ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef,
        "Gender": ClientGetFaceDetectionResponseFacesFaceGenderTypeDef,
        "Beard": ClientGetFaceDetectionResponseFacesFaceBeardTypeDef,
        "Mustache": ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef,
        "EyesOpen": ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef,
        "MouthOpen": ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef,
        "Emotions": List[ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef],
        "Landmarks": List[ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef],
        "Pose": ClientGetFaceDetectionResponseFacesFacePoseTypeDef,
        "Quality": ClientGetFaceDetectionResponseFacesFaceQualityTypeDef,
        "Confidence": float,
    },
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponseFaces` `Face`

    The face properties for the detected face.

    - **BoundingBox** *(dict) --*

      Bounding box of the face. Default attribute.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **AgeRange** *(dict) --*

      The estimated age range, in years, for the face. Low represents the lowest estimated
      age and High represents the highest estimated age.

      - **Low** *(integer) --*

        The lowest estimated age.

      - **High** *(integer) --*

        The highest estimated age.

    - **Smile** *(dict) --*

      Indicates whether or not the face is smiling, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is smiling or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Eyeglasses** *(dict) --*

      Indicates whether or not the face is wearing eye glasses, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing eye glasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Sunglasses** *(dict) --*

      Indicates whether or not the face is wearing sunglasses, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing sunglasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Gender** *(dict) --*

      Gender of the face and the confidence level in the determination.

      - **Value** *(string) --*

        Gender of the face.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Beard** *(dict) --*

      Indicates whether or not the face has a beard, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has beard or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Mustache** *(dict) --*

      Indicates whether or not the face has a mustache, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has mustache or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **EyesOpen** *(dict) --*

      Indicates whether or not the eyes on the face are open, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the eyes on the face are open.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **MouthOpen** *(dict) --*

      Indicates whether or not the mouth on the face is open, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the mouth on the face is open or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Emotions** *(list) --*

      The emotions that appear to be expressed on the face, and the confidence level in the
      determination. The API is only making a determination of the physical appearance of a
      person's face. It is not a determination of the person’s internal emotional state and
      should not be used in such a way. For example, a person pretending to have a sad face
      might not be sad emotionally.

      - *(dict) --*

        The emotions that appear to be expressed on the face, and the confidence level in the
        determination. The API is only making a determination of the physical appearance of a
        person's face. It is not a determination of the person’s internal emotional state and
        should not be used in such a way. For example, a person pretending to have a sad face
        might not be sad emotionally.

        - **Type** *(string) --*

          Type of emotion detected.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

    - **Landmarks** *(list) --*

      Indicates the location of landmarks on the face. Default attribute.

      - *(dict) --*

        Indicates the location of the landmark on the face.

        - **Type** *(string) --*

          Type of landmark.

        - **X** *(float) --*

          The x-coordinate from the top left of the landmark expressed as the ratio of the
          width of the image. For example, if the image is 700 x 200 and the x-coordinate of
          the landmark is at 350 pixels, this value is 0.5.

        - **Y** *(float) --*

          The y-coordinate from the top left of the landmark expressed as the ratio of the
          height of the image. For example, if the image is 700 x 200 and the y-coordinate of
          the landmark is at 100 pixels, this value is 0.5.

    - **Pose** *(dict) --*

      Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
      attribute.

      - **Roll** *(float) --*

        Value representing the face rotation on the roll axis.

      - **Yaw** *(float) --*

        Value representing the face rotation on the yaw axis.

      - **Pitch** *(float) --*

        Value representing the face rotation on the pitch axis.

    - **Quality** *(dict) --*

      Identifies image brightness and sharpness. Default attribute.

      - **Brightness** *(float) --*

        Value representing brightness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a brighter face image.

      - **Sharpness** *(float) --*

        Value representing sharpness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a sharper face image.

    - **Confidence** *(float) --*

      Confidence level that the bounding box contains a face (and not a different object such
      as a tree). Default attribute.
    """


_ClientGetFaceDetectionResponseFacesTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesTypeDef",
    {"Timestamp": int, "Face": ClientGetFaceDetectionResponseFacesFaceTypeDef},
    total=False,
)


class ClientGetFaceDetectionResponseFacesTypeDef(
    _ClientGetFaceDetectionResponseFacesTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponse` `Faces`

    Information about a face detected in a video analysis request and the time the face was
    detected in the video.

    - **Timestamp** *(integer) --*

      Time, in milliseconds from the start of the video, that the face was detected.

    - **Face** *(dict) --*

      The face properties for the detected face.

      - **BoundingBox** *(dict) --*

        Bounding box of the face. Default attribute.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **AgeRange** *(dict) --*

        The estimated age range, in years, for the face. Low represents the lowest estimated
        age and High represents the highest estimated age.

        - **Low** *(integer) --*

          The lowest estimated age.

        - **High** *(integer) --*

          The highest estimated age.

      - **Smile** *(dict) --*

        Indicates whether or not the face is smiling, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is smiling or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Eyeglasses** *(dict) --*

        Indicates whether or not the face is wearing eye glasses, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is wearing eye glasses or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Sunglasses** *(dict) --*

        Indicates whether or not the face is wearing sunglasses, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is wearing sunglasses or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Gender** *(dict) --*

        Gender of the face and the confidence level in the determination.

        - **Value** *(string) --*

          Gender of the face.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Beard** *(dict) --*

        Indicates whether or not the face has a beard, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face has beard or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Mustache** *(dict) --*

        Indicates whether or not the face has a mustache, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face has mustache or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **EyesOpen** *(dict) --*

        Indicates whether or not the eyes on the face are open, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the eyes on the face are open.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **MouthOpen** *(dict) --*

        Indicates whether or not the mouth on the face is open, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the mouth on the face is open or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Emotions** *(list) --*

        The emotions that appear to be expressed on the face, and the confidence level in the
        determination. The API is only making a determination of the physical appearance of a
        person's face. It is not a determination of the person’s internal emotional state and
        should not be used in such a way. For example, a person pretending to have a sad face
        might not be sad emotionally.

        - *(dict) --*

          The emotions that appear to be expressed on the face, and the confidence level in the
          determination. The API is only making a determination of the physical appearance of a
          person's face. It is not a determination of the person’s internal emotional state and
          should not be used in such a way. For example, a person pretending to have a sad face
          might not be sad emotionally.

          - **Type** *(string) --*

            Type of emotion detected.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

      - **Landmarks** *(list) --*

        Indicates the location of landmarks on the face. Default attribute.

        - *(dict) --*

          Indicates the location of the landmark on the face.

          - **Type** *(string) --*

            Type of landmark.

          - **X** *(float) --*

            The x-coordinate from the top left of the landmark expressed as the ratio of the
            width of the image. For example, if the image is 700 x 200 and the x-coordinate of
            the landmark is at 350 pixels, this value is 0.5.

          - **Y** *(float) --*

            The y-coordinate from the top left of the landmark expressed as the ratio of the
            height of the image. For example, if the image is 700 x 200 and the y-coordinate of
            the landmark is at 100 pixels, this value is 0.5.

      - **Pose** *(dict) --*

        Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
        attribute.

        - **Roll** *(float) --*

          Value representing the face rotation on the roll axis.

        - **Yaw** *(float) --*

          Value representing the face rotation on the yaw axis.

        - **Pitch** *(float) --*

          Value representing the face rotation on the pitch axis.

      - **Quality** *(dict) --*

        Identifies image brightness and sharpness. Default attribute.

        - **Brightness** *(float) --*

          Value representing brightness of the face. The service returns a value between 0 and
          100 (inclusive). A higher value indicates a brighter face image.

        - **Sharpness** *(float) --*

          Value representing sharpness of the face. The service returns a value between 0 and
          100 (inclusive). A higher value indicates a sharper face image.

      - **Confidence** *(float) --*

        Confidence level that the bounding box contains a face (and not a different object such
        as a tree). Default attribute.
    """


_ClientGetFaceDetectionResponseVideoMetadataTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": float,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)


class ClientGetFaceDetectionResponseVideoMetadataTypeDef(
    _ClientGetFaceDetectionResponseVideoMetadataTypeDef
):
    """
    Type definition for `ClientGetFaceDetectionResponse` `VideoMetadata`

    Information about a video that Amazon Rekognition Video analyzed. ``Videometadata`` is
    returned in every page of paginated responses from a Amazon Rekognition video operation.

    - **Codec** *(string) --*

      Type of compression used in the analyzed video.

    - **DurationMillis** *(integer) --*

      Length of the video in milliseconds.

    - **Format** *(string) --*

      Format of the analyzed video. Possible values are MP4, MOV and AVI.

    - **FrameRate** *(float) --*

      Number of frames per second in the video.

    - **FrameHeight** *(integer) --*

      Vertical pixel dimension of the video.

    - **FrameWidth** *(integer) --*

      Horizontal pixel dimension of the video.
    """


_ClientGetFaceDetectionResponseTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseTypeDef",
    {
        "JobStatus": str,
        "StatusMessage": str,
        "VideoMetadata": ClientGetFaceDetectionResponseVideoMetadataTypeDef,
        "NextToken": str,
        "Faces": List[ClientGetFaceDetectionResponseFacesTypeDef],
    },
    total=False,
)


class ClientGetFaceDetectionResponseTypeDef(_ClientGetFaceDetectionResponseTypeDef):
    """
    Type definition for `ClientGetFaceDetection` `Response`

    - **JobStatus** *(string) --*

      The current status of the face detection job.

    - **StatusMessage** *(string) --*

      If the job fails, ``StatusMessage`` provides a descriptive error message.

    - **VideoMetadata** *(dict) --*

      Information about a video that Amazon Rekognition Video analyzed. ``Videometadata`` is
      returned in every page of paginated responses from a Amazon Rekognition video operation.

      - **Codec** *(string) --*

        Type of compression used in the analyzed video.

      - **DurationMillis** *(integer) --*

        Length of the video in milliseconds.

      - **Format** *(string) --*

        Format of the analyzed video. Possible values are MP4, MOV and AVI.

      - **FrameRate** *(float) --*

        Number of frames per second in the video.

      - **FrameHeight** *(integer) --*

        Vertical pixel dimension of the video.

      - **FrameWidth** *(integer) --*

        Horizontal pixel dimension of the video.

    - **NextToken** *(string) --*

      If the response is truncated, Amazon Rekognition returns this token that you can use in the
      subsequent request to retrieve the next set of faces.

    - **Faces** *(list) --*

      An array of faces detected in the video. Each element contains a detected face's details and
      the time, in milliseconds from the start of the video, the face was detected.

      - *(dict) --*

        Information about a face detected in a video analysis request and the time the face was
        detected in the video.

        - **Timestamp** *(integer) --*

          Time, in milliseconds from the start of the video, that the face was detected.

        - **Face** *(dict) --*

          The face properties for the detected face.

          - **BoundingBox** *(dict) --*

            Bounding box of the face. Default attribute.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **AgeRange** *(dict) --*

            The estimated age range, in years, for the face. Low represents the lowest estimated
            age and High represents the highest estimated age.

            - **Low** *(integer) --*

              The lowest estimated age.

            - **High** *(integer) --*

              The highest estimated age.

          - **Smile** *(dict) --*

            Indicates whether or not the face is smiling, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face is smiling or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Eyeglasses** *(dict) --*

            Indicates whether or not the face is wearing eye glasses, and the confidence level in
            the determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face is wearing eye glasses or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Sunglasses** *(dict) --*

            Indicates whether or not the face is wearing sunglasses, and the confidence level in
            the determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face is wearing sunglasses or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Gender** *(dict) --*

            Gender of the face and the confidence level in the determination.

            - **Value** *(string) --*

              Gender of the face.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Beard** *(dict) --*

            Indicates whether or not the face has a beard, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face has beard or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Mustache** *(dict) --*

            Indicates whether or not the face has a mustache, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face has mustache or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **EyesOpen** *(dict) --*

            Indicates whether or not the eyes on the face are open, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the eyes on the face are open.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **MouthOpen** *(dict) --*

            Indicates whether or not the mouth on the face is open, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the mouth on the face is open or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Emotions** *(list) --*

            The emotions that appear to be expressed on the face, and the confidence level in the
            determination. The API is only making a determination of the physical appearance of a
            person's face. It is not a determination of the person’s internal emotional state and
            should not be used in such a way. For example, a person pretending to have a sad face
            might not be sad emotionally.

            - *(dict) --*

              The emotions that appear to be expressed on the face, and the confidence level in the
              determination. The API is only making a determination of the physical appearance of a
              person's face. It is not a determination of the person’s internal emotional state and
              should not be used in such a way. For example, a person pretending to have a sad face
              might not be sad emotionally.

              - **Type** *(string) --*

                Type of emotion detected.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

          - **Landmarks** *(list) --*

            Indicates the location of landmarks on the face. Default attribute.

            - *(dict) --*

              Indicates the location of the landmark on the face.

              - **Type** *(string) --*

                Type of landmark.

              - **X** *(float) --*

                The x-coordinate from the top left of the landmark expressed as the ratio of the
                width of the image. For example, if the image is 700 x 200 and the x-coordinate of
                the landmark is at 350 pixels, this value is 0.5.

              - **Y** *(float) --*

                The y-coordinate from the top left of the landmark expressed as the ratio of the
                height of the image. For example, if the image is 700 x 200 and the y-coordinate of
                the landmark is at 100 pixels, this value is 0.5.

          - **Pose** *(dict) --*

            Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
            attribute.

            - **Roll** *(float) --*

              Value representing the face rotation on the roll axis.

            - **Yaw** *(float) --*

              Value representing the face rotation on the yaw axis.

            - **Pitch** *(float) --*

              Value representing the face rotation on the pitch axis.

          - **Quality** *(dict) --*

            Identifies image brightness and sharpness. Default attribute.

            - **Brightness** *(float) --*

              Value representing brightness of the face. The service returns a value between 0 and
              100 (inclusive). A higher value indicates a brighter face image.

            - **Sharpness** *(float) --*

              Value representing sharpness of the face. The service returns a value between 0 and
              100 (inclusive). A higher value indicates a sharper face image.

          - **Confidence** *(float) --*

            Confidence level that the bounding box contains a face (and not a different object such
            as a tree). Default attribute.
    """


_ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef(
    _ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsFaceMatchesFace` `BoundingBox`

    Bounding box of the face.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": float,
    },
    total=False,
)


class ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef(
    _ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsFaceMatches` `Face`

    Describes the face properties such as the bounding box, face ID, image ID of the
    source image, and external image ID that you assigned.

    - **FaceId** *(string) --*

      Unique identifier that Amazon Rekognition assigns to the face.

    - **BoundingBox** *(dict) --*

      Bounding box of the face.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **ImageId** *(string) --*

      Unique identifier that Amazon Rekognition assigns to the input image.

    - **ExternalImageId** *(string) --*

      Identifier that you assign to all the faces in the input image.

    - **Confidence** *(float) --*

      Confidence level that the bounding box contains a face (and not a different object
      such as a tree).
    """


_ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef",
    {
        "Similarity": float,
        "Face": ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef,
    },
    total=False,
)


class ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef(
    _ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersons` `FaceMatches`

    Provides face metadata. In addition, it also provides the confidence in the match of
    this face with the input face.

    - **Similarity** *(float) --*

      Confidence in the match of this face with the input face.

    - **Face** *(dict) --*

      Describes the face properties such as the bounding box, face ID, image ID of the
      source image, and external image ID that you assigned.

      - **FaceId** *(string) --*

        Unique identifier that Amazon Rekognition assigns to the face.

      - **BoundingBox** *(dict) --*

        Bounding box of the face.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **ImageId** *(string) --*

        Unique identifier that Amazon Rekognition assigns to the input image.

      - **ExternalImageId** *(string) --*

        Identifier that you assign to all the faces in the input image.

      - **Confidence** *(float) --*

        Confidence level that the bounding box contains a face (and not a different object
        such as a tree).
    """


_ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPerson` `BoundingBox`

    Bounding box around the detected person.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `AgeRange`

    The estimated age range, in years, for the face. Low represents the lowest estimated
    age and High represents the highest estimated age.

    - **Low** *(integer) --*

      The lowest estimated age.

    - **High** *(integer) --*

      The highest estimated age.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `Beard`

    Indicates whether or not the face has a beard, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has beard or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `BoundingBox`

    Bounding box of the face. Default attribute.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef",
    {"Type": str, "Confidence": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `Emotions`

    The emotions that appear to be expressed on the face, and the confidence level in
    the determination. The API is only making a determination of the physical
    appearance of a person's face. It is not a determination of the person’s internal
    emotional state and should not be used in such a way. For example, a person
    pretending to have a sad face might not be sad emotionally.

    - **Type** *(string) --*

      Type of emotion detected.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `Eyeglasses`

    Indicates whether or not the face is wearing eye glasses, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing eye glasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `EyesOpen`

    Indicates whether or not the eyes on the face are open, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the eyes on the face are open.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef",
    {"Value": str, "Confidence": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `Gender`

    Gender of the face and the confidence level in the determination.

    - **Value** *(string) --*

      Gender of the face.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef",
    {"Type": str, "X": float, "Y": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `Landmarks`

    Indicates the location of the landmark on the face.

    - **Type** *(string) --*

      Type of landmark.

    - **X** *(float) --*

      The x-coordinate from the top left of the landmark expressed as the ratio of the
      width of the image. For example, if the image is 700 x 200 and the x-coordinate
      of the landmark is at 350 pixels, this value is 0.5.

    - **Y** *(float) --*

      The y-coordinate from the top left of the landmark expressed as the ratio of the
      height of the image. For example, if the image is 700 x 200 and the y-coordinate
      of the landmark is at 100 pixels, this value is 0.5.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `MouthOpen`

    Indicates whether or not the mouth on the face is open, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the mouth on the face is open or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `Mustache`

    Indicates whether or not the face has a mustache, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has mustache or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef",
    {"Roll": float, "Yaw": float, "Pitch": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `Pose`

    Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
    attribute.

    - **Roll** *(float) --*

      Value representing the face rotation on the roll axis.

    - **Yaw** *(float) --*

      Value representing the face rotation on the yaw axis.

    - **Pitch** *(float) --*

      Value representing the face rotation on the pitch axis.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef",
    {"Brightness": float, "Sharpness": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `Quality`

    Identifies image brightness and sharpness. Default attribute.

    - **Brightness** *(float) --*

      Value representing brightness of the face. The service returns a value between 0
      and 100 (inclusive). A higher value indicates a brighter face image.

    - **Sharpness** *(float) --*

      Value representing sharpness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a sharper face image.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `Smile`

    Indicates whether or not the face is smiling, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is smiling or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPersonFace` `Sunglasses`

    Indicates whether or not the face is wearing sunglasses, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing sunglasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetFaceSearchResponsePersonsPersonFaceTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceTypeDef",
    {
        "BoundingBox": ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef,
        "AgeRange": ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef,
        "Smile": ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef,
        "Eyeglasses": ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef,
        "Sunglasses": ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef,
        "Gender": ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef,
        "Beard": ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef,
        "Mustache": ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef,
        "EyesOpen": ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef,
        "MouthOpen": ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef,
        "Emotions": List[ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef],
        "Landmarks": List[ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef],
        "Pose": ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef,
        "Quality": ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef,
        "Confidence": float,
    },
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersonsPerson` `Face`

    Face details for the detected person.

    - **BoundingBox** *(dict) --*

      Bounding box of the face. Default attribute.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **AgeRange** *(dict) --*

      The estimated age range, in years, for the face. Low represents the lowest estimated
      age and High represents the highest estimated age.

      - **Low** *(integer) --*

        The lowest estimated age.

      - **High** *(integer) --*

        The highest estimated age.

    - **Smile** *(dict) --*

      Indicates whether or not the face is smiling, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is smiling or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Eyeglasses** *(dict) --*

      Indicates whether or not the face is wearing eye glasses, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing eye glasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Sunglasses** *(dict) --*

      Indicates whether or not the face is wearing sunglasses, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing sunglasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Gender** *(dict) --*

      Gender of the face and the confidence level in the determination.

      - **Value** *(string) --*

        Gender of the face.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Beard** *(dict) --*

      Indicates whether or not the face has a beard, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has beard or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Mustache** *(dict) --*

      Indicates whether or not the face has a mustache, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has mustache or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **EyesOpen** *(dict) --*

      Indicates whether or not the eyes on the face are open, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the eyes on the face are open.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **MouthOpen** *(dict) --*

      Indicates whether or not the mouth on the face is open, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the mouth on the face is open or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Emotions** *(list) --*

      The emotions that appear to be expressed on the face, and the confidence level in the
      determination. The API is only making a determination of the physical appearance of a
      person's face. It is not a determination of the person’s internal emotional state and
      should not be used in such a way. For example, a person pretending to have a sad face
      might not be sad emotionally.

      - *(dict) --*

        The emotions that appear to be expressed on the face, and the confidence level in
        the determination. The API is only making a determination of the physical
        appearance of a person's face. It is not a determination of the person’s internal
        emotional state and should not be used in such a way. For example, a person
        pretending to have a sad face might not be sad emotionally.

        - **Type** *(string) --*

          Type of emotion detected.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

    - **Landmarks** *(list) --*

      Indicates the location of landmarks on the face. Default attribute.

      - *(dict) --*

        Indicates the location of the landmark on the face.

        - **Type** *(string) --*

          Type of landmark.

        - **X** *(float) --*

          The x-coordinate from the top left of the landmark expressed as the ratio of the
          width of the image. For example, if the image is 700 x 200 and the x-coordinate
          of the landmark is at 350 pixels, this value is 0.5.

        - **Y** *(float) --*

          The y-coordinate from the top left of the landmark expressed as the ratio of the
          height of the image. For example, if the image is 700 x 200 and the y-coordinate
          of the landmark is at 100 pixels, this value is 0.5.

    - **Pose** *(dict) --*

      Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
      attribute.

      - **Roll** *(float) --*

        Value representing the face rotation on the roll axis.

      - **Yaw** *(float) --*

        Value representing the face rotation on the yaw axis.

      - **Pitch** *(float) --*

        Value representing the face rotation on the pitch axis.

    - **Quality** *(dict) --*

      Identifies image brightness and sharpness. Default attribute.

      - **Brightness** *(float) --*

        Value representing brightness of the face. The service returns a value between 0
        and 100 (inclusive). A higher value indicates a brighter face image.

      - **Sharpness** *(float) --*

        Value representing sharpness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a sharper face image.

    - **Confidence** *(float) --*

      Confidence level that the bounding box contains a face (and not a different object
      such as a tree). Default attribute.
    """


_ClientGetFaceSearchResponsePersonsPersonTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonTypeDef",
    {
        "Index": int,
        "BoundingBox": ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef,
        "Face": ClientGetFaceSearchResponsePersonsPersonFaceTypeDef,
    },
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponsePersons` `Person`

    Information about the matched person.

    - **Index** *(integer) --*

      Identifier for the person detected person within a video. Use to keep track of the
      person throughout the video. The identifier is not stored by Amazon Rekognition.

    - **BoundingBox** *(dict) --*

      Bounding box around the detected person.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **Face** *(dict) --*

      Face details for the detected person.

      - **BoundingBox** *(dict) --*

        Bounding box of the face. Default attribute.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **AgeRange** *(dict) --*

        The estimated age range, in years, for the face. Low represents the lowest estimated
        age and High represents the highest estimated age.

        - **Low** *(integer) --*

          The lowest estimated age.

        - **High** *(integer) --*

          The highest estimated age.

      - **Smile** *(dict) --*

        Indicates whether or not the face is smiling, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is smiling or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Eyeglasses** *(dict) --*

        Indicates whether or not the face is wearing eye glasses, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is wearing eye glasses or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Sunglasses** *(dict) --*

        Indicates whether or not the face is wearing sunglasses, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is wearing sunglasses or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Gender** *(dict) --*

        Gender of the face and the confidence level in the determination.

        - **Value** *(string) --*

          Gender of the face.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Beard** *(dict) --*

        Indicates whether or not the face has a beard, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face has beard or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Mustache** *(dict) --*

        Indicates whether or not the face has a mustache, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face has mustache or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **EyesOpen** *(dict) --*

        Indicates whether or not the eyes on the face are open, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the eyes on the face are open.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **MouthOpen** *(dict) --*

        Indicates whether or not the mouth on the face is open, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the mouth on the face is open or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Emotions** *(list) --*

        The emotions that appear to be expressed on the face, and the confidence level in the
        determination. The API is only making a determination of the physical appearance of a
        person's face. It is not a determination of the person’s internal emotional state and
        should not be used in such a way. For example, a person pretending to have a sad face
        might not be sad emotionally.

        - *(dict) --*

          The emotions that appear to be expressed on the face, and the confidence level in
          the determination. The API is only making a determination of the physical
          appearance of a person's face. It is not a determination of the person’s internal
          emotional state and should not be used in such a way. For example, a person
          pretending to have a sad face might not be sad emotionally.

          - **Type** *(string) --*

            Type of emotion detected.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

      - **Landmarks** *(list) --*

        Indicates the location of landmarks on the face. Default attribute.

        - *(dict) --*

          Indicates the location of the landmark on the face.

          - **Type** *(string) --*

            Type of landmark.

          - **X** *(float) --*

            The x-coordinate from the top left of the landmark expressed as the ratio of the
            width of the image. For example, if the image is 700 x 200 and the x-coordinate
            of the landmark is at 350 pixels, this value is 0.5.

          - **Y** *(float) --*

            The y-coordinate from the top left of the landmark expressed as the ratio of the
            height of the image. For example, if the image is 700 x 200 and the y-coordinate
            of the landmark is at 100 pixels, this value is 0.5.

      - **Pose** *(dict) --*

        Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
        attribute.

        - **Roll** *(float) --*

          Value representing the face rotation on the roll axis.

        - **Yaw** *(float) --*

          Value representing the face rotation on the yaw axis.

        - **Pitch** *(float) --*

          Value representing the face rotation on the pitch axis.

      - **Quality** *(dict) --*

        Identifies image brightness and sharpness. Default attribute.

        - **Brightness** *(float) --*

          Value representing brightness of the face. The service returns a value between 0
          and 100 (inclusive). A higher value indicates a brighter face image.

        - **Sharpness** *(float) --*

          Value representing sharpness of the face. The service returns a value between 0 and
          100 (inclusive). A higher value indicates a sharper face image.

      - **Confidence** *(float) --*

        Confidence level that the bounding box contains a face (and not a different object
        such as a tree). Default attribute.
    """


_ClientGetFaceSearchResponsePersonsTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsTypeDef",
    {
        "Timestamp": int,
        "Person": ClientGetFaceSearchResponsePersonsPersonTypeDef,
        "FaceMatches": List[ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef],
    },
    total=False,
)


class ClientGetFaceSearchResponsePersonsTypeDef(
    _ClientGetFaceSearchResponsePersonsTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponse` `Persons`

    Information about a person whose face matches a face(s) in an Amazon Rekognition
    collection. Includes information about the faces in the Amazon Rekognition collection (
    FaceMatch ), information about the person ( PersonDetail ), and the time stamp for when the
    person was detected in a video. An array of ``PersonMatch`` objects is returned by
    GetFaceSearch .

    - **Timestamp** *(integer) --*

      The time, in milliseconds from the beginning of the video, that the person was matched in
      the video.

    - **Person** *(dict) --*

      Information about the matched person.

      - **Index** *(integer) --*

        Identifier for the person detected person within a video. Use to keep track of the
        person throughout the video. The identifier is not stored by Amazon Rekognition.

      - **BoundingBox** *(dict) --*

        Bounding box around the detected person.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **Face** *(dict) --*

        Face details for the detected person.

        - **BoundingBox** *(dict) --*

          Bounding box of the face. Default attribute.

          - **Width** *(float) --*

            Width of the bounding box as a ratio of the overall image width.

          - **Height** *(float) --*

            Height of the bounding box as a ratio of the overall image height.

          - **Left** *(float) --*

            Left coordinate of the bounding box as a ratio of overall image width.

          - **Top** *(float) --*

            Top coordinate of the bounding box as a ratio of overall image height.

        - **AgeRange** *(dict) --*

          The estimated age range, in years, for the face. Low represents the lowest estimated
          age and High represents the highest estimated age.

          - **Low** *(integer) --*

            The lowest estimated age.

          - **High** *(integer) --*

            The highest estimated age.

        - **Smile** *(dict) --*

          Indicates whether or not the face is smiling, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face is smiling or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Eyeglasses** *(dict) --*

          Indicates whether or not the face is wearing eye glasses, and the confidence level in
          the determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face is wearing eye glasses or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Sunglasses** *(dict) --*

          Indicates whether or not the face is wearing sunglasses, and the confidence level in
          the determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face is wearing sunglasses or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Gender** *(dict) --*

          Gender of the face and the confidence level in the determination.

          - **Value** *(string) --*

            Gender of the face.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Beard** *(dict) --*

          Indicates whether or not the face has a beard, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face has beard or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Mustache** *(dict) --*

          Indicates whether or not the face has a mustache, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face has mustache or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **EyesOpen** *(dict) --*

          Indicates whether or not the eyes on the face are open, and the confidence level in
          the determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the eyes on the face are open.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **MouthOpen** *(dict) --*

          Indicates whether or not the mouth on the face is open, and the confidence level in
          the determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the mouth on the face is open or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Emotions** *(list) --*

          The emotions that appear to be expressed on the face, and the confidence level in the
          determination. The API is only making a determination of the physical appearance of a
          person's face. It is not a determination of the person’s internal emotional state and
          should not be used in such a way. For example, a person pretending to have a sad face
          might not be sad emotionally.

          - *(dict) --*

            The emotions that appear to be expressed on the face, and the confidence level in
            the determination. The API is only making a determination of the physical
            appearance of a person's face. It is not a determination of the person’s internal
            emotional state and should not be used in such a way. For example, a person
            pretending to have a sad face might not be sad emotionally.

            - **Type** *(string) --*

              Type of emotion detected.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

        - **Landmarks** *(list) --*

          Indicates the location of landmarks on the face. Default attribute.

          - *(dict) --*

            Indicates the location of the landmark on the face.

            - **Type** *(string) --*

              Type of landmark.

            - **X** *(float) --*

              The x-coordinate from the top left of the landmark expressed as the ratio of the
              width of the image. For example, if the image is 700 x 200 and the x-coordinate
              of the landmark is at 350 pixels, this value is 0.5.

            - **Y** *(float) --*

              The y-coordinate from the top left of the landmark expressed as the ratio of the
              height of the image. For example, if the image is 700 x 200 and the y-coordinate
              of the landmark is at 100 pixels, this value is 0.5.

        - **Pose** *(dict) --*

          Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
          attribute.

          - **Roll** *(float) --*

            Value representing the face rotation on the roll axis.

          - **Yaw** *(float) --*

            Value representing the face rotation on the yaw axis.

          - **Pitch** *(float) --*

            Value representing the face rotation on the pitch axis.

        - **Quality** *(dict) --*

          Identifies image brightness and sharpness. Default attribute.

          - **Brightness** *(float) --*

            Value representing brightness of the face. The service returns a value between 0
            and 100 (inclusive). A higher value indicates a brighter face image.

          - **Sharpness** *(float) --*

            Value representing sharpness of the face. The service returns a value between 0 and
            100 (inclusive). A higher value indicates a sharper face image.

        - **Confidence** *(float) --*

          Confidence level that the bounding box contains a face (and not a different object
          such as a tree). Default attribute.

    - **FaceMatches** *(list) --*

      Information about the faces in the input collection that match the face of a person in
      the video.

      - *(dict) --*

        Provides face metadata. In addition, it also provides the confidence in the match of
        this face with the input face.

        - **Similarity** *(float) --*

          Confidence in the match of this face with the input face.

        - **Face** *(dict) --*

          Describes the face properties such as the bounding box, face ID, image ID of the
          source image, and external image ID that you assigned.

          - **FaceId** *(string) --*

            Unique identifier that Amazon Rekognition assigns to the face.

          - **BoundingBox** *(dict) --*

            Bounding box of the face.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **ImageId** *(string) --*

            Unique identifier that Amazon Rekognition assigns to the input image.

          - **ExternalImageId** *(string) --*

            Identifier that you assign to all the faces in the input image.

          - **Confidence** *(float) --*

            Confidence level that the bounding box contains a face (and not a different object
            such as a tree).
    """


_ClientGetFaceSearchResponseVideoMetadataTypeDef = TypedDict(
    "_ClientGetFaceSearchResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": float,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)


class ClientGetFaceSearchResponseVideoMetadataTypeDef(
    _ClientGetFaceSearchResponseVideoMetadataTypeDef
):
    """
    Type definition for `ClientGetFaceSearchResponse` `VideoMetadata`

    Information about a video that Amazon Rekognition analyzed. ``Videometadata`` is returned in
    every page of paginated responses from a Amazon Rekognition Video operation.

    - **Codec** *(string) --*

      Type of compression used in the analyzed video.

    - **DurationMillis** *(integer) --*

      Length of the video in milliseconds.

    - **Format** *(string) --*

      Format of the analyzed video. Possible values are MP4, MOV and AVI.

    - **FrameRate** *(float) --*

      Number of frames per second in the video.

    - **FrameHeight** *(integer) --*

      Vertical pixel dimension of the video.

    - **FrameWidth** *(integer) --*

      Horizontal pixel dimension of the video.
    """


_ClientGetFaceSearchResponseTypeDef = TypedDict(
    "_ClientGetFaceSearchResponseTypeDef",
    {
        "JobStatus": str,
        "StatusMessage": str,
        "NextToken": str,
        "VideoMetadata": ClientGetFaceSearchResponseVideoMetadataTypeDef,
        "Persons": List[ClientGetFaceSearchResponsePersonsTypeDef],
    },
    total=False,
)


class ClientGetFaceSearchResponseTypeDef(_ClientGetFaceSearchResponseTypeDef):
    """
    Type definition for `ClientGetFaceSearch` `Response`

    - **JobStatus** *(string) --*

      The current status of the face search job.

    - **StatusMessage** *(string) --*

      If the job fails, ``StatusMessage`` provides a descriptive error message.

    - **NextToken** *(string) --*

      If the response is truncated, Amazon Rekognition Video returns this token that you can use in
      the subsequent request to retrieve the next set of search results.

    - **VideoMetadata** *(dict) --*

      Information about a video that Amazon Rekognition analyzed. ``Videometadata`` is returned in
      every page of paginated responses from a Amazon Rekognition Video operation.

      - **Codec** *(string) --*

        Type of compression used in the analyzed video.

      - **DurationMillis** *(integer) --*

        Length of the video in milliseconds.

      - **Format** *(string) --*

        Format of the analyzed video. Possible values are MP4, MOV and AVI.

      - **FrameRate** *(float) --*

        Number of frames per second in the video.

      - **FrameHeight** *(integer) --*

        Vertical pixel dimension of the video.

      - **FrameWidth** *(integer) --*

        Horizontal pixel dimension of the video.

    - **Persons** *(list) --*

      An array of persons,  PersonMatch , in the video whose face(s) match the face(s) in an Amazon
      Rekognition collection. It also includes time information for when persons are matched in the
      video. You specify the input collection in an initial call to ``StartFaceSearch`` . Each
      ``Persons`` element includes a time the person was matched, face match details
      (``FaceMatches`` ) for matching faces in the collection, and person information (``Person`` )
      for the matched person.

      - *(dict) --*

        Information about a person whose face matches a face(s) in an Amazon Rekognition
        collection. Includes information about the faces in the Amazon Rekognition collection (
        FaceMatch ), information about the person ( PersonDetail ), and the time stamp for when the
        person was detected in a video. An array of ``PersonMatch`` objects is returned by
        GetFaceSearch .

        - **Timestamp** *(integer) --*

          The time, in milliseconds from the beginning of the video, that the person was matched in
          the video.

        - **Person** *(dict) --*

          Information about the matched person.

          - **Index** *(integer) --*

            Identifier for the person detected person within a video. Use to keep track of the
            person throughout the video. The identifier is not stored by Amazon Rekognition.

          - **BoundingBox** *(dict) --*

            Bounding box around the detected person.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **Face** *(dict) --*

            Face details for the detected person.

            - **BoundingBox** *(dict) --*

              Bounding box of the face. Default attribute.

              - **Width** *(float) --*

                Width of the bounding box as a ratio of the overall image width.

              - **Height** *(float) --*

                Height of the bounding box as a ratio of the overall image height.

              - **Left** *(float) --*

                Left coordinate of the bounding box as a ratio of overall image width.

              - **Top** *(float) --*

                Top coordinate of the bounding box as a ratio of overall image height.

            - **AgeRange** *(dict) --*

              The estimated age range, in years, for the face. Low represents the lowest estimated
              age and High represents the highest estimated age.

              - **Low** *(integer) --*

                The lowest estimated age.

              - **High** *(integer) --*

                The highest estimated age.

            - **Smile** *(dict) --*

              Indicates whether or not the face is smiling, and the confidence level in the
              determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face is smiling or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Eyeglasses** *(dict) --*

              Indicates whether or not the face is wearing eye glasses, and the confidence level in
              the determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face is wearing eye glasses or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Sunglasses** *(dict) --*

              Indicates whether or not the face is wearing sunglasses, and the confidence level in
              the determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face is wearing sunglasses or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Gender** *(dict) --*

              Gender of the face and the confidence level in the determination.

              - **Value** *(string) --*

                Gender of the face.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Beard** *(dict) --*

              Indicates whether or not the face has a beard, and the confidence level in the
              determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face has beard or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Mustache** *(dict) --*

              Indicates whether or not the face has a mustache, and the confidence level in the
              determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face has mustache or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **EyesOpen** *(dict) --*

              Indicates whether or not the eyes on the face are open, and the confidence level in
              the determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the eyes on the face are open.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **MouthOpen** *(dict) --*

              Indicates whether or not the mouth on the face is open, and the confidence level in
              the determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the mouth on the face is open or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Emotions** *(list) --*

              The emotions that appear to be expressed on the face, and the confidence level in the
              determination. The API is only making a determination of the physical appearance of a
              person's face. It is not a determination of the person’s internal emotional state and
              should not be used in such a way. For example, a person pretending to have a sad face
              might not be sad emotionally.

              - *(dict) --*

                The emotions that appear to be expressed on the face, and the confidence level in
                the determination. The API is only making a determination of the physical
                appearance of a person's face. It is not a determination of the person’s internal
                emotional state and should not be used in such a way. For example, a person
                pretending to have a sad face might not be sad emotionally.

                - **Type** *(string) --*

                  Type of emotion detected.

                - **Confidence** *(float) --*

                  Level of confidence in the determination.

            - **Landmarks** *(list) --*

              Indicates the location of landmarks on the face. Default attribute.

              - *(dict) --*

                Indicates the location of the landmark on the face.

                - **Type** *(string) --*

                  Type of landmark.

                - **X** *(float) --*

                  The x-coordinate from the top left of the landmark expressed as the ratio of the
                  width of the image. For example, if the image is 700 x 200 and the x-coordinate
                  of the landmark is at 350 pixels, this value is 0.5.

                - **Y** *(float) --*

                  The y-coordinate from the top left of the landmark expressed as the ratio of the
                  height of the image. For example, if the image is 700 x 200 and the y-coordinate
                  of the landmark is at 100 pixels, this value is 0.5.

            - **Pose** *(dict) --*

              Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
              attribute.

              - **Roll** *(float) --*

                Value representing the face rotation on the roll axis.

              - **Yaw** *(float) --*

                Value representing the face rotation on the yaw axis.

              - **Pitch** *(float) --*

                Value representing the face rotation on the pitch axis.

            - **Quality** *(dict) --*

              Identifies image brightness and sharpness. Default attribute.

              - **Brightness** *(float) --*

                Value representing brightness of the face. The service returns a value between 0
                and 100 (inclusive). A higher value indicates a brighter face image.

              - **Sharpness** *(float) --*

                Value representing sharpness of the face. The service returns a value between 0 and
                100 (inclusive). A higher value indicates a sharper face image.

            - **Confidence** *(float) --*

              Confidence level that the bounding box contains a face (and not a different object
              such as a tree). Default attribute.

        - **FaceMatches** *(list) --*

          Information about the faces in the input collection that match the face of a person in
          the video.

          - *(dict) --*

            Provides face metadata. In addition, it also provides the confidence in the match of
            this face with the input face.

            - **Similarity** *(float) --*

              Confidence in the match of this face with the input face.

            - **Face** *(dict) --*

              Describes the face properties such as the bounding box, face ID, image ID of the
              source image, and external image ID that you assigned.

              - **FaceId** *(string) --*

                Unique identifier that Amazon Rekognition assigns to the face.

              - **BoundingBox** *(dict) --*

                Bounding box of the face.

                - **Width** *(float) --*

                  Width of the bounding box as a ratio of the overall image width.

                - **Height** *(float) --*

                  Height of the bounding box as a ratio of the overall image height.

                - **Left** *(float) --*

                  Left coordinate of the bounding box as a ratio of overall image width.

                - **Top** *(float) --*

                  Top coordinate of the bounding box as a ratio of overall image height.

              - **ImageId** *(string) --*

                Unique identifier that Amazon Rekognition assigns to the input image.

              - **ExternalImageId** *(string) --*

                Identifier that you assign to all the faces in the input image.

              - **Confidence** *(float) --*

                Confidence level that the bounding box contains a face (and not a different object
                such as a tree).
    """


_ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef(
    _ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef
):
    """
    Type definition for `ClientGetLabelDetectionResponseLabelsLabelInstances` `BoundingBox`

    The position of the label instance on the image.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef",
    {
        "BoundingBox": ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef,
        "Confidence": float,
    },
    total=False,
)


class ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef(
    _ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef
):
    """
    Type definition for `ClientGetLabelDetectionResponseLabelsLabel` `Instances`

    An instance of a label returned by Amazon Rekognition Image ( DetectLabels ) or by
    Amazon Rekognition Video ( GetLabelDetection ).

    - **BoundingBox** *(dict) --*

      The position of the label instance on the image.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **Confidence** *(float) --*

      The confidence that Amazon Rekognition has in the accuracy of the bounding box.
    """


_ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef",
    {"Name": str},
    total=False,
)


class ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef(
    _ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef
):
    """
    Type definition for `ClientGetLabelDetectionResponseLabelsLabel` `Parents`

    A parent label for a label. A label can have 0, 1, or more parents.

    - **Name** *(string) --*

      The name of the parent label.
    """


_ClientGetLabelDetectionResponseLabelsLabelTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseLabelsLabelTypeDef",
    {
        "Name": str,
        "Confidence": float,
        "Instances": List[ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef],
        "Parents": List[ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef],
    },
    total=False,
)


class ClientGetLabelDetectionResponseLabelsLabelTypeDef(
    _ClientGetLabelDetectionResponseLabelsLabelTypeDef
):
    """
    Type definition for `ClientGetLabelDetectionResponseLabels` `Label`

    Details about the detected label.

    - **Name** *(string) --*

      The name (label) of the object or scene.

    - **Confidence** *(float) --*

      Level of confidence.

    - **Instances** *(list) --*

      If ``Label`` represents an object, ``Instances`` contains the bounding boxes for each
      instance of the detected object. Bounding boxes are returned for common object labels
      such as people, cars, furniture, apparel or pets.

      - *(dict) --*

        An instance of a label returned by Amazon Rekognition Image ( DetectLabels ) or by
        Amazon Rekognition Video ( GetLabelDetection ).

        - **BoundingBox** *(dict) --*

          The position of the label instance on the image.

          - **Width** *(float) --*

            Width of the bounding box as a ratio of the overall image width.

          - **Height** *(float) --*

            Height of the bounding box as a ratio of the overall image height.

          - **Left** *(float) --*

            Left coordinate of the bounding box as a ratio of overall image width.

          - **Top** *(float) --*

            Top coordinate of the bounding box as a ratio of overall image height.

        - **Confidence** *(float) --*

          The confidence that Amazon Rekognition has in the accuracy of the bounding box.

    - **Parents** *(list) --*

      The parent labels for a label. The response includes all ancestor labels.

      - *(dict) --*

        A parent label for a label. A label can have 0, 1, or more parents.

        - **Name** *(string) --*

          The name of the parent label.
    """


_ClientGetLabelDetectionResponseLabelsTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseLabelsTypeDef",
    {"Timestamp": int, "Label": ClientGetLabelDetectionResponseLabelsLabelTypeDef},
    total=False,
)


class ClientGetLabelDetectionResponseLabelsTypeDef(
    _ClientGetLabelDetectionResponseLabelsTypeDef
):
    """
    Type definition for `ClientGetLabelDetectionResponse` `Labels`

    Information about a label detected in a video analysis request and the time the label was
    detected in the video.

    - **Timestamp** *(integer) --*

      Time, in milliseconds from the start of the video, that the label was detected.

    - **Label** *(dict) --*

      Details about the detected label.

      - **Name** *(string) --*

        The name (label) of the object or scene.

      - **Confidence** *(float) --*

        Level of confidence.

      - **Instances** *(list) --*

        If ``Label`` represents an object, ``Instances`` contains the bounding boxes for each
        instance of the detected object. Bounding boxes are returned for common object labels
        such as people, cars, furniture, apparel or pets.

        - *(dict) --*

          An instance of a label returned by Amazon Rekognition Image ( DetectLabels ) or by
          Amazon Rekognition Video ( GetLabelDetection ).

          - **BoundingBox** *(dict) --*

            The position of the label instance on the image.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **Confidence** *(float) --*

            The confidence that Amazon Rekognition has in the accuracy of the bounding box.

      - **Parents** *(list) --*

        The parent labels for a label. The response includes all ancestor labels.

        - *(dict) --*

          A parent label for a label. A label can have 0, 1, or more parents.

          - **Name** *(string) --*

            The name of the parent label.
    """


_ClientGetLabelDetectionResponseVideoMetadataTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": float,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)


class ClientGetLabelDetectionResponseVideoMetadataTypeDef(
    _ClientGetLabelDetectionResponseVideoMetadataTypeDef
):
    """
    Type definition for `ClientGetLabelDetectionResponse` `VideoMetadata`

    Information about a video that Amazon Rekognition Video analyzed. ``Videometadata`` is
    returned in every page of paginated responses from a Amazon Rekognition video operation.

    - **Codec** *(string) --*

      Type of compression used in the analyzed video.

    - **DurationMillis** *(integer) --*

      Length of the video in milliseconds.

    - **Format** *(string) --*

      Format of the analyzed video. Possible values are MP4, MOV and AVI.

    - **FrameRate** *(float) --*

      Number of frames per second in the video.

    - **FrameHeight** *(integer) --*

      Vertical pixel dimension of the video.

    - **FrameWidth** *(integer) --*

      Horizontal pixel dimension of the video.
    """


_ClientGetLabelDetectionResponseTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseTypeDef",
    {
        "JobStatus": str,
        "StatusMessage": str,
        "VideoMetadata": ClientGetLabelDetectionResponseVideoMetadataTypeDef,
        "NextToken": str,
        "Labels": List[ClientGetLabelDetectionResponseLabelsTypeDef],
        "LabelModelVersion": str,
    },
    total=False,
)


class ClientGetLabelDetectionResponseTypeDef(_ClientGetLabelDetectionResponseTypeDef):
    """
    Type definition for `ClientGetLabelDetection` `Response`

    - **JobStatus** *(string) --*

      The current status of the label detection job.

    - **StatusMessage** *(string) --*

      If the job fails, ``StatusMessage`` provides a descriptive error message.

    - **VideoMetadata** *(dict) --*

      Information about a video that Amazon Rekognition Video analyzed. ``Videometadata`` is
      returned in every page of paginated responses from a Amazon Rekognition video operation.

      - **Codec** *(string) --*

        Type of compression used in the analyzed video.

      - **DurationMillis** *(integer) --*

        Length of the video in milliseconds.

      - **Format** *(string) --*

        Format of the analyzed video. Possible values are MP4, MOV and AVI.

      - **FrameRate** *(float) --*

        Number of frames per second in the video.

      - **FrameHeight** *(integer) --*

        Vertical pixel dimension of the video.

      - **FrameWidth** *(integer) --*

        Horizontal pixel dimension of the video.

    - **NextToken** *(string) --*

      If the response is truncated, Amazon Rekognition Video returns this token that you can use in
      the subsequent request to retrieve the next set of labels.

    - **Labels** *(list) --*

      An array of labels detected in the video. Each element contains the detected label and the
      time, in milliseconds from the start of the video, that the label was detected.

      - *(dict) --*

        Information about a label detected in a video analysis request and the time the label was
        detected in the video.

        - **Timestamp** *(integer) --*

          Time, in milliseconds from the start of the video, that the label was detected.

        - **Label** *(dict) --*

          Details about the detected label.

          - **Name** *(string) --*

            The name (label) of the object or scene.

          - **Confidence** *(float) --*

            Level of confidence.

          - **Instances** *(list) --*

            If ``Label`` represents an object, ``Instances`` contains the bounding boxes for each
            instance of the detected object. Bounding boxes are returned for common object labels
            such as people, cars, furniture, apparel or pets.

            - *(dict) --*

              An instance of a label returned by Amazon Rekognition Image ( DetectLabels ) or by
              Amazon Rekognition Video ( GetLabelDetection ).

              - **BoundingBox** *(dict) --*

                The position of the label instance on the image.

                - **Width** *(float) --*

                  Width of the bounding box as a ratio of the overall image width.

                - **Height** *(float) --*

                  Height of the bounding box as a ratio of the overall image height.

                - **Left** *(float) --*

                  Left coordinate of the bounding box as a ratio of overall image width.

                - **Top** *(float) --*

                  Top coordinate of the bounding box as a ratio of overall image height.

              - **Confidence** *(float) --*

                The confidence that Amazon Rekognition has in the accuracy of the bounding box.

          - **Parents** *(list) --*

            The parent labels for a label. The response includes all ancestor labels.

            - *(dict) --*

              A parent label for a label. A label can have 0, 1, or more parents.

              - **Name** *(string) --*

                The name of the parent label.

    - **LabelModelVersion** *(string) --*

      Version number of the label detection model that was used to detect labels.
    """


_ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPerson` `BoundingBox`

    Bounding box around the detected person.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `AgeRange`

    The estimated age range, in years, for the face. Low represents the lowest estimated
    age and High represents the highest estimated age.

    - **Low** *(integer) --*

      The lowest estimated age.

    - **High** *(integer) --*

      The highest estimated age.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `Beard`

    Indicates whether or not the face has a beard, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has beard or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `BoundingBox`

    Bounding box of the face. Default attribute.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef",
    {"Type": str, "Confidence": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `Emotions`

    The emotions that appear to be expressed on the face, and the confidence level in
    the determination. The API is only making a determination of the physical
    appearance of a person's face. It is not a determination of the person’s internal
    emotional state and should not be used in such a way. For example, a person
    pretending to have a sad face might not be sad emotionally.

    - **Type** *(string) --*

      Type of emotion detected.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `Eyeglasses`

    Indicates whether or not the face is wearing eye glasses, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing eye glasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `EyesOpen`

    Indicates whether or not the eyes on the face are open, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the eyes on the face are open.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef",
    {"Value": str, "Confidence": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `Gender`

    Gender of the face and the confidence level in the determination.

    - **Value** *(string) --*

      Gender of the face.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef",
    {"Type": str, "X": float, "Y": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `Landmarks`

    Indicates the location of the landmark on the face.

    - **Type** *(string) --*

      Type of landmark.

    - **X** *(float) --*

      The x-coordinate from the top left of the landmark expressed as the ratio of the
      width of the image. For example, if the image is 700 x 200 and the x-coordinate
      of the landmark is at 350 pixels, this value is 0.5.

    - **Y** *(float) --*

      The y-coordinate from the top left of the landmark expressed as the ratio of the
      height of the image. For example, if the image is 700 x 200 and the y-coordinate
      of the landmark is at 100 pixels, this value is 0.5.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `MouthOpen`

    Indicates whether or not the mouth on the face is open, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the mouth on the face is open or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `Mustache`

    Indicates whether or not the face has a mustache, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has mustache or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef",
    {"Roll": float, "Yaw": float, "Pitch": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `Pose`

    Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
    attribute.

    - **Roll** *(float) --*

      Value representing the face rotation on the roll axis.

    - **Yaw** *(float) --*

      Value representing the face rotation on the yaw axis.

    - **Pitch** *(float) --*

      Value representing the face rotation on the pitch axis.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef",
    {"Brightness": float, "Sharpness": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `Quality`

    Identifies image brightness and sharpness. Default attribute.

    - **Brightness** *(float) --*

      Value representing brightness of the face. The service returns a value between 0
      and 100 (inclusive). A higher value indicates a brighter face image.

    - **Sharpness** *(float) --*

      Value representing sharpness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a sharper face image.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `Smile`

    Indicates whether or not the face is smiling, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is smiling or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPersonFace` `Sunglasses`

    Indicates whether or not the face is wearing sunglasses, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing sunglasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef",
    {
        "BoundingBox": ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef,
        "AgeRange": ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef,
        "Smile": ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef,
        "Eyeglasses": ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef,
        "Sunglasses": ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef,
        "Gender": ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef,
        "Beard": ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef,
        "Mustache": ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef,
        "EyesOpen": ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef,
        "MouthOpen": ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef,
        "Emotions": List[
            ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef
        ],
        "Landmarks": List[
            ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef
        ],
        "Pose": ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef,
        "Quality": ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef,
        "Confidence": float,
    },
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersonsPerson` `Face`

    Face details for the detected person.

    - **BoundingBox** *(dict) --*

      Bounding box of the face. Default attribute.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **AgeRange** *(dict) --*

      The estimated age range, in years, for the face. Low represents the lowest estimated
      age and High represents the highest estimated age.

      - **Low** *(integer) --*

        The lowest estimated age.

      - **High** *(integer) --*

        The highest estimated age.

    - **Smile** *(dict) --*

      Indicates whether or not the face is smiling, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is smiling or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Eyeglasses** *(dict) --*

      Indicates whether or not the face is wearing eye glasses, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing eye glasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Sunglasses** *(dict) --*

      Indicates whether or not the face is wearing sunglasses, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing sunglasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Gender** *(dict) --*

      Gender of the face and the confidence level in the determination.

      - **Value** *(string) --*

        Gender of the face.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Beard** *(dict) --*

      Indicates whether or not the face has a beard, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has beard or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Mustache** *(dict) --*

      Indicates whether or not the face has a mustache, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has mustache or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **EyesOpen** *(dict) --*

      Indicates whether or not the eyes on the face are open, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the eyes on the face are open.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **MouthOpen** *(dict) --*

      Indicates whether or not the mouth on the face is open, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the mouth on the face is open or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Emotions** *(list) --*

      The emotions that appear to be expressed on the face, and the confidence level in the
      determination. The API is only making a determination of the physical appearance of a
      person's face. It is not a determination of the person’s internal emotional state and
      should not be used in such a way. For example, a person pretending to have a sad face
      might not be sad emotionally.

      - *(dict) --*

        The emotions that appear to be expressed on the face, and the confidence level in
        the determination. The API is only making a determination of the physical
        appearance of a person's face. It is not a determination of the person’s internal
        emotional state and should not be used in such a way. For example, a person
        pretending to have a sad face might not be sad emotionally.

        - **Type** *(string) --*

          Type of emotion detected.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

    - **Landmarks** *(list) --*

      Indicates the location of landmarks on the face. Default attribute.

      - *(dict) --*

        Indicates the location of the landmark on the face.

        - **Type** *(string) --*

          Type of landmark.

        - **X** *(float) --*

          The x-coordinate from the top left of the landmark expressed as the ratio of the
          width of the image. For example, if the image is 700 x 200 and the x-coordinate
          of the landmark is at 350 pixels, this value is 0.5.

        - **Y** *(float) --*

          The y-coordinate from the top left of the landmark expressed as the ratio of the
          height of the image. For example, if the image is 700 x 200 and the y-coordinate
          of the landmark is at 100 pixels, this value is 0.5.

    - **Pose** *(dict) --*

      Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
      attribute.

      - **Roll** *(float) --*

        Value representing the face rotation on the roll axis.

      - **Yaw** *(float) --*

        Value representing the face rotation on the yaw axis.

      - **Pitch** *(float) --*

        Value representing the face rotation on the pitch axis.

    - **Quality** *(dict) --*

      Identifies image brightness and sharpness. Default attribute.

      - **Brightness** *(float) --*

        Value representing brightness of the face. The service returns a value between 0
        and 100 (inclusive). A higher value indicates a brighter face image.

      - **Sharpness** *(float) --*

        Value representing sharpness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a sharper face image.

    - **Confidence** *(float) --*

      Confidence level that the bounding box contains a face (and not a different object
      such as a tree). Default attribute.
    """


_ClientGetPersonTrackingResponsePersonsPersonTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonTypeDef",
    {
        "Index": int,
        "BoundingBox": ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef,
        "Face": ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef,
    },
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponsePersons` `Person`

    Details about a person whose path was tracked in a video.

    - **Index** *(integer) --*

      Identifier for the person detected person within a video. Use to keep track of the
      person throughout the video. The identifier is not stored by Amazon Rekognition.

    - **BoundingBox** *(dict) --*

      Bounding box around the detected person.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **Face** *(dict) --*

      Face details for the detected person.

      - **BoundingBox** *(dict) --*

        Bounding box of the face. Default attribute.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **AgeRange** *(dict) --*

        The estimated age range, in years, for the face. Low represents the lowest estimated
        age and High represents the highest estimated age.

        - **Low** *(integer) --*

          The lowest estimated age.

        - **High** *(integer) --*

          The highest estimated age.

      - **Smile** *(dict) --*

        Indicates whether or not the face is smiling, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is smiling or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Eyeglasses** *(dict) --*

        Indicates whether or not the face is wearing eye glasses, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is wearing eye glasses or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Sunglasses** *(dict) --*

        Indicates whether or not the face is wearing sunglasses, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is wearing sunglasses or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Gender** *(dict) --*

        Gender of the face and the confidence level in the determination.

        - **Value** *(string) --*

          Gender of the face.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Beard** *(dict) --*

        Indicates whether or not the face has a beard, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face has beard or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Mustache** *(dict) --*

        Indicates whether or not the face has a mustache, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face has mustache or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **EyesOpen** *(dict) --*

        Indicates whether or not the eyes on the face are open, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the eyes on the face are open.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **MouthOpen** *(dict) --*

        Indicates whether or not the mouth on the face is open, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the mouth on the face is open or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Emotions** *(list) --*

        The emotions that appear to be expressed on the face, and the confidence level in the
        determination. The API is only making a determination of the physical appearance of a
        person's face. It is not a determination of the person’s internal emotional state and
        should not be used in such a way. For example, a person pretending to have a sad face
        might not be sad emotionally.

        - *(dict) --*

          The emotions that appear to be expressed on the face, and the confidence level in
          the determination. The API is only making a determination of the physical
          appearance of a person's face. It is not a determination of the person’s internal
          emotional state and should not be used in such a way. For example, a person
          pretending to have a sad face might not be sad emotionally.

          - **Type** *(string) --*

            Type of emotion detected.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

      - **Landmarks** *(list) --*

        Indicates the location of landmarks on the face. Default attribute.

        - *(dict) --*

          Indicates the location of the landmark on the face.

          - **Type** *(string) --*

            Type of landmark.

          - **X** *(float) --*

            The x-coordinate from the top left of the landmark expressed as the ratio of the
            width of the image. For example, if the image is 700 x 200 and the x-coordinate
            of the landmark is at 350 pixels, this value is 0.5.

          - **Y** *(float) --*

            The y-coordinate from the top left of the landmark expressed as the ratio of the
            height of the image. For example, if the image is 700 x 200 and the y-coordinate
            of the landmark is at 100 pixels, this value is 0.5.

      - **Pose** *(dict) --*

        Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
        attribute.

        - **Roll** *(float) --*

          Value representing the face rotation on the roll axis.

        - **Yaw** *(float) --*

          Value representing the face rotation on the yaw axis.

        - **Pitch** *(float) --*

          Value representing the face rotation on the pitch axis.

      - **Quality** *(dict) --*

        Identifies image brightness and sharpness. Default attribute.

        - **Brightness** *(float) --*

          Value representing brightness of the face. The service returns a value between 0
          and 100 (inclusive). A higher value indicates a brighter face image.

        - **Sharpness** *(float) --*

          Value representing sharpness of the face. The service returns a value between 0 and
          100 (inclusive). A higher value indicates a sharper face image.

      - **Confidence** *(float) --*

        Confidence level that the bounding box contains a face (and not a different object
        such as a tree). Default attribute.
    """


_ClientGetPersonTrackingResponsePersonsTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsTypeDef",
    {"Timestamp": int, "Person": ClientGetPersonTrackingResponsePersonsPersonTypeDef},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsTypeDef(
    _ClientGetPersonTrackingResponsePersonsTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponse` `Persons`

    Details and path tracking information for a single time a person's path is tracked in a
    video. Amazon Rekognition operations that track people's paths return an array of
    ``PersonDetection`` objects with elements for each time a person's path is tracked in a
    video.

    For more information, see GetPersonTracking in the Amazon Rekognition Developer Guide.

    - **Timestamp** *(integer) --*

      The time, in milliseconds from the start of the video, that the person's path was tracked.

    - **Person** *(dict) --*

      Details about a person whose path was tracked in a video.

      - **Index** *(integer) --*

        Identifier for the person detected person within a video. Use to keep track of the
        person throughout the video. The identifier is not stored by Amazon Rekognition.

      - **BoundingBox** *(dict) --*

        Bounding box around the detected person.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **Face** *(dict) --*

        Face details for the detected person.

        - **BoundingBox** *(dict) --*

          Bounding box of the face. Default attribute.

          - **Width** *(float) --*

            Width of the bounding box as a ratio of the overall image width.

          - **Height** *(float) --*

            Height of the bounding box as a ratio of the overall image height.

          - **Left** *(float) --*

            Left coordinate of the bounding box as a ratio of overall image width.

          - **Top** *(float) --*

            Top coordinate of the bounding box as a ratio of overall image height.

        - **AgeRange** *(dict) --*

          The estimated age range, in years, for the face. Low represents the lowest estimated
          age and High represents the highest estimated age.

          - **Low** *(integer) --*

            The lowest estimated age.

          - **High** *(integer) --*

            The highest estimated age.

        - **Smile** *(dict) --*

          Indicates whether or not the face is smiling, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face is smiling or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Eyeglasses** *(dict) --*

          Indicates whether or not the face is wearing eye glasses, and the confidence level in
          the determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face is wearing eye glasses or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Sunglasses** *(dict) --*

          Indicates whether or not the face is wearing sunglasses, and the confidence level in
          the determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face is wearing sunglasses or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Gender** *(dict) --*

          Gender of the face and the confidence level in the determination.

          - **Value** *(string) --*

            Gender of the face.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Beard** *(dict) --*

          Indicates whether or not the face has a beard, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face has beard or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Mustache** *(dict) --*

          Indicates whether or not the face has a mustache, and the confidence level in the
          determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the face has mustache or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **EyesOpen** *(dict) --*

          Indicates whether or not the eyes on the face are open, and the confidence level in
          the determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the eyes on the face are open.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **MouthOpen** *(dict) --*

          Indicates whether or not the mouth on the face is open, and the confidence level in
          the determination.

          - **Value** *(boolean) --*

            Boolean value that indicates whether the mouth on the face is open or not.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

        - **Emotions** *(list) --*

          The emotions that appear to be expressed on the face, and the confidence level in the
          determination. The API is only making a determination of the physical appearance of a
          person's face. It is not a determination of the person’s internal emotional state and
          should not be used in such a way. For example, a person pretending to have a sad face
          might not be sad emotionally.

          - *(dict) --*

            The emotions that appear to be expressed on the face, and the confidence level in
            the determination. The API is only making a determination of the physical
            appearance of a person's face. It is not a determination of the person’s internal
            emotional state and should not be used in such a way. For example, a person
            pretending to have a sad face might not be sad emotionally.

            - **Type** *(string) --*

              Type of emotion detected.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

        - **Landmarks** *(list) --*

          Indicates the location of landmarks on the face. Default attribute.

          - *(dict) --*

            Indicates the location of the landmark on the face.

            - **Type** *(string) --*

              Type of landmark.

            - **X** *(float) --*

              The x-coordinate from the top left of the landmark expressed as the ratio of the
              width of the image. For example, if the image is 700 x 200 and the x-coordinate
              of the landmark is at 350 pixels, this value is 0.5.

            - **Y** *(float) --*

              The y-coordinate from the top left of the landmark expressed as the ratio of the
              height of the image. For example, if the image is 700 x 200 and the y-coordinate
              of the landmark is at 100 pixels, this value is 0.5.

        - **Pose** *(dict) --*

          Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
          attribute.

          - **Roll** *(float) --*

            Value representing the face rotation on the roll axis.

          - **Yaw** *(float) --*

            Value representing the face rotation on the yaw axis.

          - **Pitch** *(float) --*

            Value representing the face rotation on the pitch axis.

        - **Quality** *(dict) --*

          Identifies image brightness and sharpness. Default attribute.

          - **Brightness** *(float) --*

            Value representing brightness of the face. The service returns a value between 0
            and 100 (inclusive). A higher value indicates a brighter face image.

          - **Sharpness** *(float) --*

            Value representing sharpness of the face. The service returns a value between 0 and
            100 (inclusive). A higher value indicates a sharper face image.

        - **Confidence** *(float) --*

          Confidence level that the bounding box contains a face (and not a different object
          such as a tree). Default attribute.
    """


_ClientGetPersonTrackingResponseVideoMetadataTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": float,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)


class ClientGetPersonTrackingResponseVideoMetadataTypeDef(
    _ClientGetPersonTrackingResponseVideoMetadataTypeDef
):
    """
    Type definition for `ClientGetPersonTrackingResponse` `VideoMetadata`

    Information about a video that Amazon Rekognition Video analyzed. ``Videometadata`` is
    returned in every page of paginated responses from a Amazon Rekognition Video operation.

    - **Codec** *(string) --*

      Type of compression used in the analyzed video.

    - **DurationMillis** *(integer) --*

      Length of the video in milliseconds.

    - **Format** *(string) --*

      Format of the analyzed video. Possible values are MP4, MOV and AVI.

    - **FrameRate** *(float) --*

      Number of frames per second in the video.

    - **FrameHeight** *(integer) --*

      Vertical pixel dimension of the video.

    - **FrameWidth** *(integer) --*

      Horizontal pixel dimension of the video.
    """


_ClientGetPersonTrackingResponseTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponseTypeDef",
    {
        "JobStatus": str,
        "StatusMessage": str,
        "VideoMetadata": ClientGetPersonTrackingResponseVideoMetadataTypeDef,
        "NextToken": str,
        "Persons": List[ClientGetPersonTrackingResponsePersonsTypeDef],
    },
    total=False,
)


class ClientGetPersonTrackingResponseTypeDef(_ClientGetPersonTrackingResponseTypeDef):
    """
    Type definition for `ClientGetPersonTracking` `Response`

    - **JobStatus** *(string) --*

      The current status of the person tracking job.

    - **StatusMessage** *(string) --*

      If the job fails, ``StatusMessage`` provides a descriptive error message.

    - **VideoMetadata** *(dict) --*

      Information about a video that Amazon Rekognition Video analyzed. ``Videometadata`` is
      returned in every page of paginated responses from a Amazon Rekognition Video operation.

      - **Codec** *(string) --*

        Type of compression used in the analyzed video.

      - **DurationMillis** *(integer) --*

        Length of the video in milliseconds.

      - **Format** *(string) --*

        Format of the analyzed video. Possible values are MP4, MOV and AVI.

      - **FrameRate** *(float) --*

        Number of frames per second in the video.

      - **FrameHeight** *(integer) --*

        Vertical pixel dimension of the video.

      - **FrameWidth** *(integer) --*

        Horizontal pixel dimension of the video.

    - **NextToken** *(string) --*

      If the response is truncated, Amazon Rekognition Video returns this token that you can use in
      the subsequent request to retrieve the next set of persons.

    - **Persons** *(list) --*

      An array of the persons detected in the video and the time(s) their path was tracked
      throughout the video. An array element will exist for each time a person's path is tracked.

      - *(dict) --*

        Details and path tracking information for a single time a person's path is tracked in a
        video. Amazon Rekognition operations that track people's paths return an array of
        ``PersonDetection`` objects with elements for each time a person's path is tracked in a
        video.

        For more information, see GetPersonTracking in the Amazon Rekognition Developer Guide.

        - **Timestamp** *(integer) --*

          The time, in milliseconds from the start of the video, that the person's path was tracked.

        - **Person** *(dict) --*

          Details about a person whose path was tracked in a video.

          - **Index** *(integer) --*

            Identifier for the person detected person within a video. Use to keep track of the
            person throughout the video. The identifier is not stored by Amazon Rekognition.

          - **BoundingBox** *(dict) --*

            Bounding box around the detected person.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **Face** *(dict) --*

            Face details for the detected person.

            - **BoundingBox** *(dict) --*

              Bounding box of the face. Default attribute.

              - **Width** *(float) --*

                Width of the bounding box as a ratio of the overall image width.

              - **Height** *(float) --*

                Height of the bounding box as a ratio of the overall image height.

              - **Left** *(float) --*

                Left coordinate of the bounding box as a ratio of overall image width.

              - **Top** *(float) --*

                Top coordinate of the bounding box as a ratio of overall image height.

            - **AgeRange** *(dict) --*

              The estimated age range, in years, for the face. Low represents the lowest estimated
              age and High represents the highest estimated age.

              - **Low** *(integer) --*

                The lowest estimated age.

              - **High** *(integer) --*

                The highest estimated age.

            - **Smile** *(dict) --*

              Indicates whether or not the face is smiling, and the confidence level in the
              determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face is smiling or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Eyeglasses** *(dict) --*

              Indicates whether or not the face is wearing eye glasses, and the confidence level in
              the determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face is wearing eye glasses or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Sunglasses** *(dict) --*

              Indicates whether or not the face is wearing sunglasses, and the confidence level in
              the determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face is wearing sunglasses or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Gender** *(dict) --*

              Gender of the face and the confidence level in the determination.

              - **Value** *(string) --*

                Gender of the face.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Beard** *(dict) --*

              Indicates whether or not the face has a beard, and the confidence level in the
              determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face has beard or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Mustache** *(dict) --*

              Indicates whether or not the face has a mustache, and the confidence level in the
              determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the face has mustache or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **EyesOpen** *(dict) --*

              Indicates whether or not the eyes on the face are open, and the confidence level in
              the determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the eyes on the face are open.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **MouthOpen** *(dict) --*

              Indicates whether or not the mouth on the face is open, and the confidence level in
              the determination.

              - **Value** *(boolean) --*

                Boolean value that indicates whether the mouth on the face is open or not.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

            - **Emotions** *(list) --*

              The emotions that appear to be expressed on the face, and the confidence level in the
              determination. The API is only making a determination of the physical appearance of a
              person's face. It is not a determination of the person’s internal emotional state and
              should not be used in such a way. For example, a person pretending to have a sad face
              might not be sad emotionally.

              - *(dict) --*

                The emotions that appear to be expressed on the face, and the confidence level in
                the determination. The API is only making a determination of the physical
                appearance of a person's face. It is not a determination of the person’s internal
                emotional state and should not be used in such a way. For example, a person
                pretending to have a sad face might not be sad emotionally.

                - **Type** *(string) --*

                  Type of emotion detected.

                - **Confidence** *(float) --*

                  Level of confidence in the determination.

            - **Landmarks** *(list) --*

              Indicates the location of landmarks on the face. Default attribute.

              - *(dict) --*

                Indicates the location of the landmark on the face.

                - **Type** *(string) --*

                  Type of landmark.

                - **X** *(float) --*

                  The x-coordinate from the top left of the landmark expressed as the ratio of the
                  width of the image. For example, if the image is 700 x 200 and the x-coordinate
                  of the landmark is at 350 pixels, this value is 0.5.

                - **Y** *(float) --*

                  The y-coordinate from the top left of the landmark expressed as the ratio of the
                  height of the image. For example, if the image is 700 x 200 and the y-coordinate
                  of the landmark is at 100 pixels, this value is 0.5.

            - **Pose** *(dict) --*

              Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
              attribute.

              - **Roll** *(float) --*

                Value representing the face rotation on the roll axis.

              - **Yaw** *(float) --*

                Value representing the face rotation on the yaw axis.

              - **Pitch** *(float) --*

                Value representing the face rotation on the pitch axis.

            - **Quality** *(dict) --*

              Identifies image brightness and sharpness. Default attribute.

              - **Brightness** *(float) --*

                Value representing brightness of the face. The service returns a value between 0
                and 100 (inclusive). A higher value indicates a brighter face image.

              - **Sharpness** *(float) --*

                Value representing sharpness of the face. The service returns a value between 0 and
                100 (inclusive). A higher value indicates a sharper face image.

            - **Confidence** *(float) --*

              Confidence level that the bounding box contains a face (and not a different object
              such as a tree). Default attribute.
    """


_ClientIndexFacesImageS3ObjectTypeDef = TypedDict(
    "_ClientIndexFacesImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientIndexFacesImageS3ObjectTypeDef(_ClientIndexFacesImageS3ObjectTypeDef):
    """
    Type definition for `ClientIndexFacesImage` `S3Object`

    Identifies an S3 object as the image source.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientIndexFacesImageTypeDef = TypedDict(
    "_ClientIndexFacesImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientIndexFacesImageS3ObjectTypeDef},
    total=False,
)


class ClientIndexFacesImageTypeDef(_ClientIndexFacesImageTypeDef):
    """
    Type definition for `ClientIndexFaces` `Image`

    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes isn't supported.

    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image
    bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.

    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.

    - **S3Object** *(dict) --*

      Identifies an S3 object as the image source.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `AgeRange`

    The estimated age range, in years, for the face. Low represents the lowest estimated
    age and High represents the highest estimated age.

    - **Low** *(integer) --*

      The lowest estimated age.

    - **High** *(integer) --*

      The highest estimated age.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `Beard`

    Indicates whether or not the face has a beard, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has beard or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `BoundingBox`

    Bounding box of the face. Default attribute.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef",
    {"Type": str, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `Emotions`

    The emotions that appear to be expressed on the face, and the confidence level in the
    determination. The API is only making a determination of the physical appearance of a
    person's face. It is not a determination of the person’s internal emotional state and
    should not be used in such a way. For example, a person pretending to have a sad face
    might not be sad emotionally.

    - **Type** *(string) --*

      Type of emotion detected.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `Eyeglasses`

    Indicates whether or not the face is wearing eye glasses, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing eye glasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `EyesOpen`

    Indicates whether or not the eyes on the face are open, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the eyes on the face are open.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef",
    {"Value": str, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `Gender`

    Gender of the face and the confidence level in the determination.

    - **Value** *(string) --*

      Gender of the face.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef",
    {"Type": str, "X": float, "Y": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `Landmarks`

    Indicates the location of the landmark on the face.

    - **Type** *(string) --*

      Type of landmark.

    - **X** *(float) --*

      The x-coordinate from the top left of the landmark expressed as the ratio of the
      width of the image. For example, if the image is 700 x 200 and the x-coordinate of
      the landmark is at 350 pixels, this value is 0.5.

    - **Y** *(float) --*

      The y-coordinate from the top left of the landmark expressed as the ratio of the
      height of the image. For example, if the image is 700 x 200 and the y-coordinate of
      the landmark is at 100 pixels, this value is 0.5.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `MouthOpen`

    Indicates whether or not the mouth on the face is open, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the mouth on the face is open or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `Mustache`

    Indicates whether or not the face has a mustache, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has mustache or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef",
    {"Roll": float, "Yaw": float, "Pitch": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `Pose`

    Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
    attribute.

    - **Roll** *(float) --*

      Value representing the face rotation on the roll axis.

    - **Yaw** *(float) --*

      Value representing the face rotation on the yaw axis.

    - **Pitch** *(float) --*

      Value representing the face rotation on the pitch axis.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef",
    {"Brightness": float, "Sharpness": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `Quality`

    Identifies image brightness and sharpness. Default attribute.

    - **Brightness** *(float) --*

      Value representing brightness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a brighter face image.

    - **Sharpness** *(float) --*

      Value representing sharpness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a sharper face image.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `Smile`

    Indicates whether or not the face is smiling, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is smiling or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFaceDetail` `Sunglasses`

    Indicates whether or not the face is wearing sunglasses, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing sunglasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef",
    {
        "BoundingBox": ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef,
        "AgeRange": ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef,
        "Smile": ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef,
        "Eyeglasses": ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef,
        "Sunglasses": ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef,
        "Gender": ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef,
        "Beard": ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef,
        "Mustache": ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef,
        "EyesOpen": ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef,
        "MouthOpen": ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef,
        "Emotions": List[ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef],
        "Landmarks": List[
            ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef
        ],
        "Pose": ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef,
        "Quality": ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef,
        "Confidence": float,
    },
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecords` `FaceDetail`

    Structure containing attributes of the face that the algorithm detected.

    - **BoundingBox** *(dict) --*

      Bounding box of the face. Default attribute.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **AgeRange** *(dict) --*

      The estimated age range, in years, for the face. Low represents the lowest estimated
      age and High represents the highest estimated age.

      - **Low** *(integer) --*

        The lowest estimated age.

      - **High** *(integer) --*

        The highest estimated age.

    - **Smile** *(dict) --*

      Indicates whether or not the face is smiling, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is smiling or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Eyeglasses** *(dict) --*

      Indicates whether or not the face is wearing eye glasses, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing eye glasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Sunglasses** *(dict) --*

      Indicates whether or not the face is wearing sunglasses, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing sunglasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Gender** *(dict) --*

      Gender of the face and the confidence level in the determination.

      - **Value** *(string) --*

        Gender of the face.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Beard** *(dict) --*

      Indicates whether or not the face has a beard, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has beard or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Mustache** *(dict) --*

      Indicates whether or not the face has a mustache, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has mustache or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **EyesOpen** *(dict) --*

      Indicates whether or not the eyes on the face are open, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the eyes on the face are open.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **MouthOpen** *(dict) --*

      Indicates whether or not the mouth on the face is open, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the mouth on the face is open or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Emotions** *(list) --*

      The emotions that appear to be expressed on the face, and the confidence level in the
      determination. The API is only making a determination of the physical appearance of a
      person's face. It is not a determination of the person’s internal emotional state and
      should not be used in such a way. For example, a person pretending to have a sad face
      might not be sad emotionally.

      - *(dict) --*

        The emotions that appear to be expressed on the face, and the confidence level in the
        determination. The API is only making a determination of the physical appearance of a
        person's face. It is not a determination of the person’s internal emotional state and
        should not be used in such a way. For example, a person pretending to have a sad face
        might not be sad emotionally.

        - **Type** *(string) --*

          Type of emotion detected.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

    - **Landmarks** *(list) --*

      Indicates the location of landmarks on the face. Default attribute.

      - *(dict) --*

        Indicates the location of the landmark on the face.

        - **Type** *(string) --*

          Type of landmark.

        - **X** *(float) --*

          The x-coordinate from the top left of the landmark expressed as the ratio of the
          width of the image. For example, if the image is 700 x 200 and the x-coordinate of
          the landmark is at 350 pixels, this value is 0.5.

        - **Y** *(float) --*

          The y-coordinate from the top left of the landmark expressed as the ratio of the
          height of the image. For example, if the image is 700 x 200 and the y-coordinate of
          the landmark is at 100 pixels, this value is 0.5.

    - **Pose** *(dict) --*

      Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
      attribute.

      - **Roll** *(float) --*

        Value representing the face rotation on the roll axis.

      - **Yaw** *(float) --*

        Value representing the face rotation on the yaw axis.

      - **Pitch** *(float) --*

        Value representing the face rotation on the pitch axis.

    - **Quality** *(dict) --*

      Identifies image brightness and sharpness. Default attribute.

      - **Brightness** *(float) --*

        Value representing brightness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a brighter face image.

      - **Sharpness** *(float) --*

        Value representing sharpness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a sharper face image.

    - **Confidence** *(float) --*

      Confidence level that the bounding box contains a face (and not a different object such
      as a tree). Default attribute.
    """


_ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecordsFace` `BoundingBox`

    Bounding box of the face.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientIndexFacesResponseFaceRecordsFaceTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": float,
    },
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseFaceRecords` `Face`

    Describes the face properties such as the bounding box, face ID, image ID of the input
    image, and external image ID that you assigned.

    - **FaceId** *(string) --*

      Unique identifier that Amazon Rekognition assigns to the face.

    - **BoundingBox** *(dict) --*

      Bounding box of the face.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **ImageId** *(string) --*

      Unique identifier that Amazon Rekognition assigns to the input image.

    - **ExternalImageId** *(string) --*

      Identifier that you assign to all the faces in the input image.

    - **Confidence** *(float) --*

      Confidence level that the bounding box contains a face (and not a different object such
      as a tree).
    """


_ClientIndexFacesResponseFaceRecordsTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsTypeDef",
    {
        "Face": ClientIndexFacesResponseFaceRecordsFaceTypeDef,
        "FaceDetail": ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef,
    },
    total=False,
)


class ClientIndexFacesResponseFaceRecordsTypeDef(
    _ClientIndexFacesResponseFaceRecordsTypeDef
):
    """
    Type definition for `ClientIndexFacesResponse` `FaceRecords`

    Object containing both the face metadata (stored in the backend database), and facial
    attributes that are detected but aren't stored in the database.

    - **Face** *(dict) --*

      Describes the face properties such as the bounding box, face ID, image ID of the input
      image, and external image ID that you assigned.

      - **FaceId** *(string) --*

        Unique identifier that Amazon Rekognition assigns to the face.

      - **BoundingBox** *(dict) --*

        Bounding box of the face.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **ImageId** *(string) --*

        Unique identifier that Amazon Rekognition assigns to the input image.

      - **ExternalImageId** *(string) --*

        Identifier that you assign to all the faces in the input image.

      - **Confidence** *(float) --*

        Confidence level that the bounding box contains a face (and not a different object such
        as a tree).

    - **FaceDetail** *(dict) --*

      Structure containing attributes of the face that the algorithm detected.

      - **BoundingBox** *(dict) --*

        Bounding box of the face. Default attribute.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **AgeRange** *(dict) --*

        The estimated age range, in years, for the face. Low represents the lowest estimated
        age and High represents the highest estimated age.

        - **Low** *(integer) --*

          The lowest estimated age.

        - **High** *(integer) --*

          The highest estimated age.

      - **Smile** *(dict) --*

        Indicates whether or not the face is smiling, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is smiling or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Eyeglasses** *(dict) --*

        Indicates whether or not the face is wearing eye glasses, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is wearing eye glasses or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Sunglasses** *(dict) --*

        Indicates whether or not the face is wearing sunglasses, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is wearing sunglasses or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Gender** *(dict) --*

        Gender of the face and the confidence level in the determination.

        - **Value** *(string) --*

          Gender of the face.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Beard** *(dict) --*

        Indicates whether or not the face has a beard, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face has beard or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Mustache** *(dict) --*

        Indicates whether or not the face has a mustache, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face has mustache or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **EyesOpen** *(dict) --*

        Indicates whether or not the eyes on the face are open, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the eyes on the face are open.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **MouthOpen** *(dict) --*

        Indicates whether or not the mouth on the face is open, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the mouth on the face is open or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Emotions** *(list) --*

        The emotions that appear to be expressed on the face, and the confidence level in the
        determination. The API is only making a determination of the physical appearance of a
        person's face. It is not a determination of the person’s internal emotional state and
        should not be used in such a way. For example, a person pretending to have a sad face
        might not be sad emotionally.

        - *(dict) --*

          The emotions that appear to be expressed on the face, and the confidence level in the
          determination. The API is only making a determination of the physical appearance of a
          person's face. It is not a determination of the person’s internal emotional state and
          should not be used in such a way. For example, a person pretending to have a sad face
          might not be sad emotionally.

          - **Type** *(string) --*

            Type of emotion detected.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

      - **Landmarks** *(list) --*

        Indicates the location of landmarks on the face. Default attribute.

        - *(dict) --*

          Indicates the location of the landmark on the face.

          - **Type** *(string) --*

            Type of landmark.

          - **X** *(float) --*

            The x-coordinate from the top left of the landmark expressed as the ratio of the
            width of the image. For example, if the image is 700 x 200 and the x-coordinate of
            the landmark is at 350 pixels, this value is 0.5.

          - **Y** *(float) --*

            The y-coordinate from the top left of the landmark expressed as the ratio of the
            height of the image. For example, if the image is 700 x 200 and the y-coordinate of
            the landmark is at 100 pixels, this value is 0.5.

      - **Pose** *(dict) --*

        Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
        attribute.

        - **Roll** *(float) --*

          Value representing the face rotation on the roll axis.

        - **Yaw** *(float) --*

          Value representing the face rotation on the yaw axis.

        - **Pitch** *(float) --*

          Value representing the face rotation on the pitch axis.

      - **Quality** *(dict) --*

        Identifies image brightness and sharpness. Default attribute.

        - **Brightness** *(float) --*

          Value representing brightness of the face. The service returns a value between 0 and
          100 (inclusive). A higher value indicates a brighter face image.

        - **Sharpness** *(float) --*

          Value representing sharpness of the face. The service returns a value between 0 and
          100 (inclusive). A higher value indicates a sharper face image.

      - **Confidence** *(float) --*

        Confidence level that the bounding box contains a face (and not a different object such
        as a tree). Default attribute.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `AgeRange`

    The estimated age range, in years, for the face. Low represents the lowest estimated
    age and High represents the highest estimated age.

    - **Low** *(integer) --*

      The lowest estimated age.

    - **High** *(integer) --*

      The highest estimated age.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `Beard`

    Indicates whether or not the face has a beard, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has beard or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `BoundingBox`

    Bounding box of the face. Default attribute.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef",
    {"Type": str, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `Emotions`

    The emotions that appear to be expressed on the face, and the confidence level in the
    determination. The API is only making a determination of the physical appearance of a
    person's face. It is not a determination of the person’s internal emotional state and
    should not be used in such a way. For example, a person pretending to have a sad face
    might not be sad emotionally.

    - **Type** *(string) --*

      Type of emotion detected.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `Eyeglasses`

    Indicates whether or not the face is wearing eye glasses, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing eye glasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `EyesOpen`

    Indicates whether or not the eyes on the face are open, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the eyes on the face are open.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef",
    {"Value": str, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `Gender`

    Gender of the face and the confidence level in the determination.

    - **Value** *(string) --*

      Gender of the face.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef",
    {"Type": str, "X": float, "Y": float},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `Landmarks`

    Indicates the location of the landmark on the face.

    - **Type** *(string) --*

      Type of landmark.

    - **X** *(float) --*

      The x-coordinate from the top left of the landmark expressed as the ratio of the
      width of the image. For example, if the image is 700 x 200 and the x-coordinate of
      the landmark is at 350 pixels, this value is 0.5.

    - **Y** *(float) --*

      The y-coordinate from the top left of the landmark expressed as the ratio of the
      height of the image. For example, if the image is 700 x 200 and the y-coordinate of
      the landmark is at 100 pixels, this value is 0.5.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `MouthOpen`

    Indicates whether or not the mouth on the face is open, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the mouth on the face is open or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `Mustache`

    Indicates whether or not the face has a mustache, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face has mustache or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef",
    {"Roll": float, "Yaw": float, "Pitch": float},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `Pose`

    Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
    attribute.

    - **Roll** *(float) --*

      Value representing the face rotation on the roll axis.

    - **Yaw** *(float) --*

      Value representing the face rotation on the yaw axis.

    - **Pitch** *(float) --*

      Value representing the face rotation on the pitch axis.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef",
    {"Brightness": float, "Sharpness": float},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `Quality`

    Identifies image brightness and sharpness. Default attribute.

    - **Brightness** *(float) --*

      Value representing brightness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a brighter face image.

    - **Sharpness** *(float) --*

      Value representing sharpness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a sharper face image.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `Smile`

    Indicates whether or not the face is smiling, and the confidence level in the
    determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is smiling or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef",
    {"Value": bool, "Confidence": float},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFacesFaceDetail` `Sunglasses`

    Indicates whether or not the face is wearing sunglasses, and the confidence level in
    the determination.

    - **Value** *(boolean) --*

      Boolean value that indicates whether the face is wearing sunglasses or not.

    - **Confidence** *(float) --*

      Level of confidence in the determination.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef",
    {
        "BoundingBox": ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef,
        "AgeRange": ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef,
        "Smile": ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef,
        "Eyeglasses": ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef,
        "Sunglasses": ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef,
        "Gender": ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef,
        "Beard": ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef,
        "Mustache": ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef,
        "EyesOpen": ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef,
        "MouthOpen": ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef,
        "Emotions": List[
            ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef
        ],
        "Landmarks": List[
            ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef
        ],
        "Pose": ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef,
        "Quality": ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef,
        "Confidence": float,
    },
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef
):
    """
    Type definition for `ClientIndexFacesResponseUnindexedFaces` `FaceDetail`

    The structure that contains attributes of a face that ``IndexFaces`` detected, but didn't
    index.

    - **BoundingBox** *(dict) --*

      Bounding box of the face. Default attribute.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **AgeRange** *(dict) --*

      The estimated age range, in years, for the face. Low represents the lowest estimated
      age and High represents the highest estimated age.

      - **Low** *(integer) --*

        The lowest estimated age.

      - **High** *(integer) --*

        The highest estimated age.

    - **Smile** *(dict) --*

      Indicates whether or not the face is smiling, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is smiling or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Eyeglasses** *(dict) --*

      Indicates whether or not the face is wearing eye glasses, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing eye glasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Sunglasses** *(dict) --*

      Indicates whether or not the face is wearing sunglasses, and the confidence level in
      the determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face is wearing sunglasses or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Gender** *(dict) --*

      Gender of the face and the confidence level in the determination.

      - **Value** *(string) --*

        Gender of the face.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Beard** *(dict) --*

      Indicates whether or not the face has a beard, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has beard or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Mustache** *(dict) --*

      Indicates whether or not the face has a mustache, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the face has mustache or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **EyesOpen** *(dict) --*

      Indicates whether or not the eyes on the face are open, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the eyes on the face are open.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **MouthOpen** *(dict) --*

      Indicates whether or not the mouth on the face is open, and the confidence level in the
      determination.

      - **Value** *(boolean) --*

        Boolean value that indicates whether the mouth on the face is open or not.

      - **Confidence** *(float) --*

        Level of confidence in the determination.

    - **Emotions** *(list) --*

      The emotions that appear to be expressed on the face, and the confidence level in the
      determination. The API is only making a determination of the physical appearance of a
      person's face. It is not a determination of the person’s internal emotional state and
      should not be used in such a way. For example, a person pretending to have a sad face
      might not be sad emotionally.

      - *(dict) --*

        The emotions that appear to be expressed on the face, and the confidence level in the
        determination. The API is only making a determination of the physical appearance of a
        person's face. It is not a determination of the person’s internal emotional state and
        should not be used in such a way. For example, a person pretending to have a sad face
        might not be sad emotionally.

        - **Type** *(string) --*

          Type of emotion detected.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

    - **Landmarks** *(list) --*

      Indicates the location of landmarks on the face. Default attribute.

      - *(dict) --*

        Indicates the location of the landmark on the face.

        - **Type** *(string) --*

          Type of landmark.

        - **X** *(float) --*

          The x-coordinate from the top left of the landmark expressed as the ratio of the
          width of the image. For example, if the image is 700 x 200 and the x-coordinate of
          the landmark is at 350 pixels, this value is 0.5.

        - **Y** *(float) --*

          The y-coordinate from the top left of the landmark expressed as the ratio of the
          height of the image. For example, if the image is 700 x 200 and the y-coordinate of
          the landmark is at 100 pixels, this value is 0.5.

    - **Pose** *(dict) --*

      Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
      attribute.

      - **Roll** *(float) --*

        Value representing the face rotation on the roll axis.

      - **Yaw** *(float) --*

        Value representing the face rotation on the yaw axis.

      - **Pitch** *(float) --*

        Value representing the face rotation on the pitch axis.

    - **Quality** *(dict) --*

      Identifies image brightness and sharpness. Default attribute.

      - **Brightness** *(float) --*

        Value representing brightness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a brighter face image.

      - **Sharpness** *(float) --*

        Value representing sharpness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a sharper face image.

    - **Confidence** *(float) --*

      Confidence level that the bounding box contains a face (and not a different object such
      as a tree). Default attribute.
    """


_ClientIndexFacesResponseUnindexedFacesTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesTypeDef",
    {
        "Reasons": List[str],
        "FaceDetail": ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef,
    },
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesTypeDef(
    _ClientIndexFacesResponseUnindexedFacesTypeDef
):
    """
    Type definition for `ClientIndexFacesResponse` `UnindexedFaces`

    A face that  IndexFaces detected, but didn't index. Use the ``Reasons`` response attribute
    to determine why a face wasn't indexed.

    - **Reasons** *(list) --*

      An array of reasons that specify why a face wasn't indexed.

      * EXTREME_POSE - The face is at a pose that can't be detected. For example, the head is
      turned too far away from the camera.

      * EXCEEDS_MAX_FACES - The number of faces detected is already higher than that specified
      by the ``MaxFaces`` input parameter for ``IndexFaces`` .

      * LOW_BRIGHTNESS - The image is too dark.

      * LOW_SHARPNESS - The image is too blurry.

      * LOW_CONFIDENCE - The face was detected with a low confidence.

      * SMALL_BOUNDING_BOX - The bounding box around the face is too small.

      - *(string) --*

    - **FaceDetail** *(dict) --*

      The structure that contains attributes of a face that ``IndexFaces`` detected, but didn't
      index.

      - **BoundingBox** *(dict) --*

        Bounding box of the face. Default attribute.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **AgeRange** *(dict) --*

        The estimated age range, in years, for the face. Low represents the lowest estimated
        age and High represents the highest estimated age.

        - **Low** *(integer) --*

          The lowest estimated age.

        - **High** *(integer) --*

          The highest estimated age.

      - **Smile** *(dict) --*

        Indicates whether or not the face is smiling, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is smiling or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Eyeglasses** *(dict) --*

        Indicates whether or not the face is wearing eye glasses, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is wearing eye glasses or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Sunglasses** *(dict) --*

        Indicates whether or not the face is wearing sunglasses, and the confidence level in
        the determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face is wearing sunglasses or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Gender** *(dict) --*

        Gender of the face and the confidence level in the determination.

        - **Value** *(string) --*

          Gender of the face.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Beard** *(dict) --*

        Indicates whether or not the face has a beard, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face has beard or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Mustache** *(dict) --*

        Indicates whether or not the face has a mustache, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the face has mustache or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **EyesOpen** *(dict) --*

        Indicates whether or not the eyes on the face are open, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the eyes on the face are open.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **MouthOpen** *(dict) --*

        Indicates whether or not the mouth on the face is open, and the confidence level in the
        determination.

        - **Value** *(boolean) --*

          Boolean value that indicates whether the mouth on the face is open or not.

        - **Confidence** *(float) --*

          Level of confidence in the determination.

      - **Emotions** *(list) --*

        The emotions that appear to be expressed on the face, and the confidence level in the
        determination. The API is only making a determination of the physical appearance of a
        person's face. It is not a determination of the person’s internal emotional state and
        should not be used in such a way. For example, a person pretending to have a sad face
        might not be sad emotionally.

        - *(dict) --*

          The emotions that appear to be expressed on the face, and the confidence level in the
          determination. The API is only making a determination of the physical appearance of a
          person's face. It is not a determination of the person’s internal emotional state and
          should not be used in such a way. For example, a person pretending to have a sad face
          might not be sad emotionally.

          - **Type** *(string) --*

            Type of emotion detected.

          - **Confidence** *(float) --*

            Level of confidence in the determination.

      - **Landmarks** *(list) --*

        Indicates the location of landmarks on the face. Default attribute.

        - *(dict) --*

          Indicates the location of the landmark on the face.

          - **Type** *(string) --*

            Type of landmark.

          - **X** *(float) --*

            The x-coordinate from the top left of the landmark expressed as the ratio of the
            width of the image. For example, if the image is 700 x 200 and the x-coordinate of
            the landmark is at 350 pixels, this value is 0.5.

          - **Y** *(float) --*

            The y-coordinate from the top left of the landmark expressed as the ratio of the
            height of the image. For example, if the image is 700 x 200 and the y-coordinate of
            the landmark is at 100 pixels, this value is 0.5.

      - **Pose** *(dict) --*

        Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
        attribute.

        - **Roll** *(float) --*

          Value representing the face rotation on the roll axis.

        - **Yaw** *(float) --*

          Value representing the face rotation on the yaw axis.

        - **Pitch** *(float) --*

          Value representing the face rotation on the pitch axis.

      - **Quality** *(dict) --*

        Identifies image brightness and sharpness. Default attribute.

        - **Brightness** *(float) --*

          Value representing brightness of the face. The service returns a value between 0 and
          100 (inclusive). A higher value indicates a brighter face image.

        - **Sharpness** *(float) --*

          Value representing sharpness of the face. The service returns a value between 0 and
          100 (inclusive). A higher value indicates a sharper face image.

      - **Confidence** *(float) --*

        Confidence level that the bounding box contains a face (and not a different object such
        as a tree). Default attribute.
    """


_ClientIndexFacesResponseTypeDef = TypedDict(
    "_ClientIndexFacesResponseTypeDef",
    {
        "FaceRecords": List[ClientIndexFacesResponseFaceRecordsTypeDef],
        "OrientationCorrection": str,
        "FaceModelVersion": str,
        "UnindexedFaces": List[ClientIndexFacesResponseUnindexedFacesTypeDef],
    },
    total=False,
)


class ClientIndexFacesResponseTypeDef(_ClientIndexFacesResponseTypeDef):
    """
    Type definition for `ClientIndexFaces` `Response`

    - **FaceRecords** *(list) --*

      An array of faces detected and added to the collection. For more information, see Searching
      Faces in a Collection in the Amazon Rekognition Developer Guide.

      - *(dict) --*

        Object containing both the face metadata (stored in the backend database), and facial
        attributes that are detected but aren't stored in the database.

        - **Face** *(dict) --*

          Describes the face properties such as the bounding box, face ID, image ID of the input
          image, and external image ID that you assigned.

          - **FaceId** *(string) --*

            Unique identifier that Amazon Rekognition assigns to the face.

          - **BoundingBox** *(dict) --*

            Bounding box of the face.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **ImageId** *(string) --*

            Unique identifier that Amazon Rekognition assigns to the input image.

          - **ExternalImageId** *(string) --*

            Identifier that you assign to all the faces in the input image.

          - **Confidence** *(float) --*

            Confidence level that the bounding box contains a face (and not a different object such
            as a tree).

        - **FaceDetail** *(dict) --*

          Structure containing attributes of the face that the algorithm detected.

          - **BoundingBox** *(dict) --*

            Bounding box of the face. Default attribute.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **AgeRange** *(dict) --*

            The estimated age range, in years, for the face. Low represents the lowest estimated
            age and High represents the highest estimated age.

            - **Low** *(integer) --*

              The lowest estimated age.

            - **High** *(integer) --*

              The highest estimated age.

          - **Smile** *(dict) --*

            Indicates whether or not the face is smiling, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face is smiling or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Eyeglasses** *(dict) --*

            Indicates whether or not the face is wearing eye glasses, and the confidence level in
            the determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face is wearing eye glasses or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Sunglasses** *(dict) --*

            Indicates whether or not the face is wearing sunglasses, and the confidence level in
            the determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face is wearing sunglasses or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Gender** *(dict) --*

            Gender of the face and the confidence level in the determination.

            - **Value** *(string) --*

              Gender of the face.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Beard** *(dict) --*

            Indicates whether or not the face has a beard, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face has beard or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Mustache** *(dict) --*

            Indicates whether or not the face has a mustache, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face has mustache or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **EyesOpen** *(dict) --*

            Indicates whether or not the eyes on the face are open, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the eyes on the face are open.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **MouthOpen** *(dict) --*

            Indicates whether or not the mouth on the face is open, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the mouth on the face is open or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Emotions** *(list) --*

            The emotions that appear to be expressed on the face, and the confidence level in the
            determination. The API is only making a determination of the physical appearance of a
            person's face. It is not a determination of the person’s internal emotional state and
            should not be used in such a way. For example, a person pretending to have a sad face
            might not be sad emotionally.

            - *(dict) --*

              The emotions that appear to be expressed on the face, and the confidence level in the
              determination. The API is only making a determination of the physical appearance of a
              person's face. It is not a determination of the person’s internal emotional state and
              should not be used in such a way. For example, a person pretending to have a sad face
              might not be sad emotionally.

              - **Type** *(string) --*

                Type of emotion detected.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

          - **Landmarks** *(list) --*

            Indicates the location of landmarks on the face. Default attribute.

            - *(dict) --*

              Indicates the location of the landmark on the face.

              - **Type** *(string) --*

                Type of landmark.

              - **X** *(float) --*

                The x-coordinate from the top left of the landmark expressed as the ratio of the
                width of the image. For example, if the image is 700 x 200 and the x-coordinate of
                the landmark is at 350 pixels, this value is 0.5.

              - **Y** *(float) --*

                The y-coordinate from the top left of the landmark expressed as the ratio of the
                height of the image. For example, if the image is 700 x 200 and the y-coordinate of
                the landmark is at 100 pixels, this value is 0.5.

          - **Pose** *(dict) --*

            Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
            attribute.

            - **Roll** *(float) --*

              Value representing the face rotation on the roll axis.

            - **Yaw** *(float) --*

              Value representing the face rotation on the yaw axis.

            - **Pitch** *(float) --*

              Value representing the face rotation on the pitch axis.

          - **Quality** *(dict) --*

            Identifies image brightness and sharpness. Default attribute.

            - **Brightness** *(float) --*

              Value representing brightness of the face. The service returns a value between 0 and
              100 (inclusive). A higher value indicates a brighter face image.

            - **Sharpness** *(float) --*

              Value representing sharpness of the face. The service returns a value between 0 and
              100 (inclusive). A higher value indicates a sharper face image.

          - **Confidence** *(float) --*

            Confidence level that the bounding box contains a face (and not a different object such
            as a tree). Default attribute.

    - **OrientationCorrection** *(string) --*

      If your collection is associated with a face detection model that's later than version 3.0,
      the value of ``OrientationCorrection`` is always null and no orientation information is
      returned.

      If your collection is associated with a face detection model that's version 3.0 or earlier,
      the following applies:

      * If the input image is in .jpeg format, it might contain exchangeable image file format
      (Exif) metadata that includes the image's orientation. Amazon Rekognition uses this
      orientation information to perform image correction - the bounding box coordinates are
      translated to represent object locations after the orientation information in the Exif
      metadata is used to correct the image orientation. Images in .png format don't contain Exif
      metadata. The value of ``OrientationCorrection`` is null.

      * If the image doesn't contain orientation information in its Exif metadata, Amazon
      Rekognition returns an estimated orientation (ROTATE_0, ROTATE_90, ROTATE_180, ROTATE_270).
      Amazon Rekognition doesn’t perform image correction for images. The bounding box coordinates
      aren't translated and represent the object locations before the image is rotated.

      Bounding box information is returned in the ``FaceRecords`` array. You can get the version of
      the face detection model by calling  DescribeCollection .

    - **FaceModelVersion** *(string) --*

      The version number of the face detection model that's associated with the input collection
      (``CollectionId`` ).

    - **UnindexedFaces** *(list) --*

      An array of faces that were detected in the image but weren't indexed. They weren't indexed
      because the quality filter identified them as low quality, or the ``MaxFaces`` request
      parameter filtered them out. To use the quality filter, you specify the ``QualityFilter``
      request parameter.

      - *(dict) --*

        A face that  IndexFaces detected, but didn't index. Use the ``Reasons`` response attribute
        to determine why a face wasn't indexed.

        - **Reasons** *(list) --*

          An array of reasons that specify why a face wasn't indexed.

          * EXTREME_POSE - The face is at a pose that can't be detected. For example, the head is
          turned too far away from the camera.

          * EXCEEDS_MAX_FACES - The number of faces detected is already higher than that specified
          by the ``MaxFaces`` input parameter for ``IndexFaces`` .

          * LOW_BRIGHTNESS - The image is too dark.

          * LOW_SHARPNESS - The image is too blurry.

          * LOW_CONFIDENCE - The face was detected with a low confidence.

          * SMALL_BOUNDING_BOX - The bounding box around the face is too small.

          - *(string) --*

        - **FaceDetail** *(dict) --*

          The structure that contains attributes of a face that ``IndexFaces`` detected, but didn't
          index.

          - **BoundingBox** *(dict) --*

            Bounding box of the face. Default attribute.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **AgeRange** *(dict) --*

            The estimated age range, in years, for the face. Low represents the lowest estimated
            age and High represents the highest estimated age.

            - **Low** *(integer) --*

              The lowest estimated age.

            - **High** *(integer) --*

              The highest estimated age.

          - **Smile** *(dict) --*

            Indicates whether or not the face is smiling, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face is smiling or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Eyeglasses** *(dict) --*

            Indicates whether or not the face is wearing eye glasses, and the confidence level in
            the determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face is wearing eye glasses or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Sunglasses** *(dict) --*

            Indicates whether or not the face is wearing sunglasses, and the confidence level in
            the determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face is wearing sunglasses or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Gender** *(dict) --*

            Gender of the face and the confidence level in the determination.

            - **Value** *(string) --*

              Gender of the face.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Beard** *(dict) --*

            Indicates whether or not the face has a beard, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face has beard or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Mustache** *(dict) --*

            Indicates whether or not the face has a mustache, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the face has mustache or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **EyesOpen** *(dict) --*

            Indicates whether or not the eyes on the face are open, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the eyes on the face are open.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **MouthOpen** *(dict) --*

            Indicates whether or not the mouth on the face is open, and the confidence level in the
            determination.

            - **Value** *(boolean) --*

              Boolean value that indicates whether the mouth on the face is open or not.

            - **Confidence** *(float) --*

              Level of confidence in the determination.

          - **Emotions** *(list) --*

            The emotions that appear to be expressed on the face, and the confidence level in the
            determination. The API is only making a determination of the physical appearance of a
            person's face. It is not a determination of the person’s internal emotional state and
            should not be used in such a way. For example, a person pretending to have a sad face
            might not be sad emotionally.

            - *(dict) --*

              The emotions that appear to be expressed on the face, and the confidence level in the
              determination. The API is only making a determination of the physical appearance of a
              person's face. It is not a determination of the person’s internal emotional state and
              should not be used in such a way. For example, a person pretending to have a sad face
              might not be sad emotionally.

              - **Type** *(string) --*

                Type of emotion detected.

              - **Confidence** *(float) --*

                Level of confidence in the determination.

          - **Landmarks** *(list) --*

            Indicates the location of landmarks on the face. Default attribute.

            - *(dict) --*

              Indicates the location of the landmark on the face.

              - **Type** *(string) --*

                Type of landmark.

              - **X** *(float) --*

                The x-coordinate from the top left of the landmark expressed as the ratio of the
                width of the image. For example, if the image is 700 x 200 and the x-coordinate of
                the landmark is at 350 pixels, this value is 0.5.

              - **Y** *(float) --*

                The y-coordinate from the top left of the landmark expressed as the ratio of the
                height of the image. For example, if the image is 700 x 200 and the y-coordinate of
                the landmark is at 100 pixels, this value is 0.5.

          - **Pose** *(dict) --*

            Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
            attribute.

            - **Roll** *(float) --*

              Value representing the face rotation on the roll axis.

            - **Yaw** *(float) --*

              Value representing the face rotation on the yaw axis.

            - **Pitch** *(float) --*

              Value representing the face rotation on the pitch axis.

          - **Quality** *(dict) --*

            Identifies image brightness and sharpness. Default attribute.

            - **Brightness** *(float) --*

              Value representing brightness of the face. The service returns a value between 0 and
              100 (inclusive). A higher value indicates a brighter face image.

            - **Sharpness** *(float) --*

              Value representing sharpness of the face. The service returns a value between 0 and
              100 (inclusive). A higher value indicates a sharper face image.

          - **Confidence** *(float) --*

            Confidence level that the bounding box contains a face (and not a different object such
            as a tree). Default attribute.
    """


_ClientListCollectionsResponseTypeDef = TypedDict(
    "_ClientListCollectionsResponseTypeDef",
    {"CollectionIds": List[str], "NextToken": str, "FaceModelVersions": List[str]},
    total=False,
)


class ClientListCollectionsResponseTypeDef(_ClientListCollectionsResponseTypeDef):
    """
    Type definition for `ClientListCollections` `Response`

    - **CollectionIds** *(list) --*

      An array of collection IDs.

      - *(string) --*

    - **NextToken** *(string) --*

      If the result is truncated, the response provides a ``NextToken`` that you can use in the
      subsequent request to fetch the next set of collection IDs.

    - **FaceModelVersions** *(list) --*

      Version numbers of the face detection models associated with the collections in the array
      ``CollectionIds`` . For example, the value of ``FaceModelVersions[2]`` is the version number
      for the face detection model used by the collection in ``CollectionId[2]`` .

      - *(string) --*
    """


_ClientListFacesResponseFacesBoundingBoxTypeDef = TypedDict(
    "_ClientListFacesResponseFacesBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientListFacesResponseFacesBoundingBoxTypeDef(
    _ClientListFacesResponseFacesBoundingBoxTypeDef
):
    """
    Type definition for `ClientListFacesResponseFaces` `BoundingBox`

    Bounding box of the face.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientListFacesResponseFacesTypeDef = TypedDict(
    "_ClientListFacesResponseFacesTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientListFacesResponseFacesBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": float,
    },
    total=False,
)


class ClientListFacesResponseFacesTypeDef(_ClientListFacesResponseFacesTypeDef):
    """
    Type definition for `ClientListFacesResponse` `Faces`

    Describes the face properties such as the bounding box, face ID, image ID of the input
    image, and external image ID that you assigned.

    - **FaceId** *(string) --*

      Unique identifier that Amazon Rekognition assigns to the face.

    - **BoundingBox** *(dict) --*

      Bounding box of the face.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **ImageId** *(string) --*

      Unique identifier that Amazon Rekognition assigns to the input image.

    - **ExternalImageId** *(string) --*

      Identifier that you assign to all the faces in the input image.

    - **Confidence** *(float) --*

      Confidence level that the bounding box contains a face (and not a different object such
      as a tree).
    """


_ClientListFacesResponseTypeDef = TypedDict(
    "_ClientListFacesResponseTypeDef",
    {
        "Faces": List[ClientListFacesResponseFacesTypeDef],
        "NextToken": str,
        "FaceModelVersion": str,
    },
    total=False,
)


class ClientListFacesResponseTypeDef(_ClientListFacesResponseTypeDef):
    """
    Type definition for `ClientListFaces` `Response`

    - **Faces** *(list) --*

      An array of ``Face`` objects.

      - *(dict) --*

        Describes the face properties such as the bounding box, face ID, image ID of the input
        image, and external image ID that you assigned.

        - **FaceId** *(string) --*

          Unique identifier that Amazon Rekognition assigns to the face.

        - **BoundingBox** *(dict) --*

          Bounding box of the face.

          - **Width** *(float) --*

            Width of the bounding box as a ratio of the overall image width.

          - **Height** *(float) --*

            Height of the bounding box as a ratio of the overall image height.

          - **Left** *(float) --*

            Left coordinate of the bounding box as a ratio of overall image width.

          - **Top** *(float) --*

            Top coordinate of the bounding box as a ratio of overall image height.

        - **ImageId** *(string) --*

          Unique identifier that Amazon Rekognition assigns to the input image.

        - **ExternalImageId** *(string) --*

          Identifier that you assign to all the faces in the input image.

        - **Confidence** *(float) --*

          Confidence level that the bounding box contains a face (and not a different object such
          as a tree).

    - **NextToken** *(string) --*

      If the response is truncated, Amazon Rekognition returns this token that you can use in the
      subsequent request to retrieve the next set of faces.

    - **FaceModelVersion** *(string) --*

      Version number of the face detection model associated with the input collection
      (``CollectionId`` ).
    """


_ClientListStreamProcessorsResponseStreamProcessorsTypeDef = TypedDict(
    "_ClientListStreamProcessorsResponseStreamProcessorsTypeDef",
    {"Name": str, "Status": str},
    total=False,
)


class ClientListStreamProcessorsResponseStreamProcessorsTypeDef(
    _ClientListStreamProcessorsResponseStreamProcessorsTypeDef
):
    """
    Type definition for `ClientListStreamProcessorsResponse` `StreamProcessors`

    An object that recognizes faces in a streaming video. An Amazon Rekognition stream
    processor is created by a call to  CreateStreamProcessor . The request parameters for
    ``CreateStreamProcessor`` describe the Kinesis video stream source for the streaming video,
    face recognition parameters, and where to stream the analysis resullts.

    - **Name** *(string) --*

      Name of the Amazon Rekognition stream processor.

    - **Status** *(string) --*

      Current status of the Amazon Rekognition stream processor.
    """


_ClientListStreamProcessorsResponseTypeDef = TypedDict(
    "_ClientListStreamProcessorsResponseTypeDef",
    {
        "NextToken": str,
        "StreamProcessors": List[
            ClientListStreamProcessorsResponseStreamProcessorsTypeDef
        ],
    },
    total=False,
)


class ClientListStreamProcessorsResponseTypeDef(
    _ClientListStreamProcessorsResponseTypeDef
):
    """
    Type definition for `ClientListStreamProcessors` `Response`

    - **NextToken** *(string) --*

      If the response is truncated, Amazon Rekognition Video returns this token that you can use in
      the subsequent request to retrieve the next set of stream processors.

    - **StreamProcessors** *(list) --*

      List of stream processors that you have created.

      - *(dict) --*

        An object that recognizes faces in a streaming video. An Amazon Rekognition stream
        processor is created by a call to  CreateStreamProcessor . The request parameters for
        ``CreateStreamProcessor`` describe the Kinesis video stream source for the streaming video,
        face recognition parameters, and where to stream the analysis resullts.

        - **Name** *(string) --*

          Name of the Amazon Rekognition stream processor.

        - **Status** *(string) --*

          Current status of the Amazon Rekognition stream processor.
    """


_ClientRecognizeCelebritiesImageS3ObjectTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientRecognizeCelebritiesImageS3ObjectTypeDef(
    _ClientRecognizeCelebritiesImageS3ObjectTypeDef
):
    """
    Type definition for `ClientRecognizeCelebritiesImage` `S3Object`

    Identifies an S3 object as the image source.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientRecognizeCelebritiesImageTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientRecognizeCelebritiesImageS3ObjectTypeDef},
    total=False,
)


class ClientRecognizeCelebritiesImageTypeDef(_ClientRecognizeCelebritiesImageTypeDef):
    """
    Type definition for `ClientRecognizeCelebrities` `Image`

    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes is not supported.

    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image
    bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.

    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.

    - **S3Object** *(dict) --*

      Identifies an S3 object as the image source.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef(
    _ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef
):
    """
    Type definition for `ClientRecognizeCelebritiesResponseCelebrityFacesFace` `BoundingBox`

    Bounding box of the face.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef",
    {"Type": str, "X": float, "Y": float},
    total=False,
)


class ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef(
    _ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef
):
    """
    Type definition for `ClientRecognizeCelebritiesResponseCelebrityFacesFace` `Landmarks`

    Indicates the location of the landmark on the face.

    - **Type** *(string) --*

      Type of landmark.

    - **X** *(float) --*

      The x-coordinate from the top left of the landmark expressed as the ratio of the
      width of the image. For example, if the image is 700 x 200 and the x-coordinate of
      the landmark is at 350 pixels, this value is 0.5.

    - **Y** *(float) --*

      The y-coordinate from the top left of the landmark expressed as the ratio of the
      height of the image. For example, if the image is 700 x 200 and the y-coordinate of
      the landmark is at 100 pixels, this value is 0.5.
    """


_ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef",
    {"Roll": float, "Yaw": float, "Pitch": float},
    total=False,
)


class ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef(
    _ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef
):
    """
    Type definition for `ClientRecognizeCelebritiesResponseCelebrityFacesFace` `Pose`

    Indicates the pose of the face as determined by its pitch, roll, and yaw.

    - **Roll** *(float) --*

      Value representing the face rotation on the roll axis.

    - **Yaw** *(float) --*

      Value representing the face rotation on the yaw axis.

    - **Pitch** *(float) --*

      Value representing the face rotation on the pitch axis.
    """


_ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef",
    {"Brightness": float, "Sharpness": float},
    total=False,
)


class ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef(
    _ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef
):
    """
    Type definition for `ClientRecognizeCelebritiesResponseCelebrityFacesFace` `Quality`

    Identifies face image brightness and sharpness.

    - **Brightness** *(float) --*

      Value representing brightness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a brighter face image.

    - **Sharpness** *(float) --*

      Value representing sharpness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a sharper face image.
    """


_ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef",
    {
        "BoundingBox": ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef,
        "Confidence": float,
        "Landmarks": List[
            ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef
        ],
        "Pose": ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef,
        "Quality": ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef,
    },
    total=False,
)


class ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef(
    _ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef
):
    """
    Type definition for `ClientRecognizeCelebritiesResponseCelebrityFaces` `Face`

    Provides information about the celebrity's face, such as its location on the image.

    - **BoundingBox** *(dict) --*

      Bounding box of the face.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **Confidence** *(float) --*

      Level of confidence that what the bounding box contains is a face.

    - **Landmarks** *(list) --*

      An array of facial landmarks.

      - *(dict) --*

        Indicates the location of the landmark on the face.

        - **Type** *(string) --*

          Type of landmark.

        - **X** *(float) --*

          The x-coordinate from the top left of the landmark expressed as the ratio of the
          width of the image. For example, if the image is 700 x 200 and the x-coordinate of
          the landmark is at 350 pixels, this value is 0.5.

        - **Y** *(float) --*

          The y-coordinate from the top left of the landmark expressed as the ratio of the
          height of the image. For example, if the image is 700 x 200 and the y-coordinate of
          the landmark is at 100 pixels, this value is 0.5.

    - **Pose** *(dict) --*

      Indicates the pose of the face as determined by its pitch, roll, and yaw.

      - **Roll** *(float) --*

        Value representing the face rotation on the roll axis.

      - **Yaw** *(float) --*

        Value representing the face rotation on the yaw axis.

      - **Pitch** *(float) --*

        Value representing the face rotation on the pitch axis.

    - **Quality** *(dict) --*

      Identifies face image brightness and sharpness.

      - **Brightness** *(float) --*

        Value representing brightness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a brighter face image.

      - **Sharpness** *(float) --*

        Value representing sharpness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a sharper face image.
    """


_ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "Id": str,
        "Face": ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef,
        "MatchConfidence": float,
    },
    total=False,
)


class ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef(
    _ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef
):
    """
    Type definition for `ClientRecognizeCelebritiesResponse` `CelebrityFaces`

    Provides information about a celebrity recognized by the  RecognizeCelebrities operation.

    - **Urls** *(list) --*

      An array of URLs pointing to additional information about the celebrity. If there is no
      additional information about the celebrity, this list is empty.

      - *(string) --*

    - **Name** *(string) --*

      The name of the celebrity.

    - **Id** *(string) --*

      A unique identifier for the celebrity.

    - **Face** *(dict) --*

      Provides information about the celebrity's face, such as its location on the image.

      - **BoundingBox** *(dict) --*

        Bounding box of the face.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **Confidence** *(float) --*

        Level of confidence that what the bounding box contains is a face.

      - **Landmarks** *(list) --*

        An array of facial landmarks.

        - *(dict) --*

          Indicates the location of the landmark on the face.

          - **Type** *(string) --*

            Type of landmark.

          - **X** *(float) --*

            The x-coordinate from the top left of the landmark expressed as the ratio of the
            width of the image. For example, if the image is 700 x 200 and the x-coordinate of
            the landmark is at 350 pixels, this value is 0.5.

          - **Y** *(float) --*

            The y-coordinate from the top left of the landmark expressed as the ratio of the
            height of the image. For example, if the image is 700 x 200 and the y-coordinate of
            the landmark is at 100 pixels, this value is 0.5.

      - **Pose** *(dict) --*

        Indicates the pose of the face as determined by its pitch, roll, and yaw.

        - **Roll** *(float) --*

          Value representing the face rotation on the roll axis.

        - **Yaw** *(float) --*

          Value representing the face rotation on the yaw axis.

        - **Pitch** *(float) --*

          Value representing the face rotation on the pitch axis.

      - **Quality** *(dict) --*

        Identifies face image brightness and sharpness.

        - **Brightness** *(float) --*

          Value representing brightness of the face. The service returns a value between 0 and
          100 (inclusive). A higher value indicates a brighter face image.

        - **Sharpness** *(float) --*

          Value representing sharpness of the face. The service returns a value between 0 and
          100 (inclusive). A higher value indicates a sharper face image.

    - **MatchConfidence** *(float) --*

      The confidence, in percentage, that Amazon Rekognition has that the recognized face is
      the celebrity.
    """


_ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef(
    _ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef
):
    """
    Type definition for `ClientRecognizeCelebritiesResponseUnrecognizedFaces` `BoundingBox`

    Bounding box of the face.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef",
    {"Type": str, "X": float, "Y": float},
    total=False,
)


class ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef(
    _ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef
):
    """
    Type definition for `ClientRecognizeCelebritiesResponseUnrecognizedFaces` `Landmarks`

    Indicates the location of the landmark on the face.

    - **Type** *(string) --*

      Type of landmark.

    - **X** *(float) --*

      The x-coordinate from the top left of the landmark expressed as the ratio of the
      width of the image. For example, if the image is 700 x 200 and the x-coordinate of
      the landmark is at 350 pixels, this value is 0.5.

    - **Y** *(float) --*

      The y-coordinate from the top left of the landmark expressed as the ratio of the
      height of the image. For example, if the image is 700 x 200 and the y-coordinate of
      the landmark is at 100 pixels, this value is 0.5.
    """


_ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef",
    {"Roll": float, "Yaw": float, "Pitch": float},
    total=False,
)


class ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef(
    _ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef
):
    """
    Type definition for `ClientRecognizeCelebritiesResponseUnrecognizedFaces` `Pose`

    Indicates the pose of the face as determined by its pitch, roll, and yaw.

    - **Roll** *(float) --*

      Value representing the face rotation on the roll axis.

    - **Yaw** *(float) --*

      Value representing the face rotation on the yaw axis.

    - **Pitch** *(float) --*

      Value representing the face rotation on the pitch axis.
    """


_ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef",
    {"Brightness": float, "Sharpness": float},
    total=False,
)


class ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef(
    _ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef
):
    """
    Type definition for `ClientRecognizeCelebritiesResponseUnrecognizedFaces` `Quality`

    Identifies face image brightness and sharpness.

    - **Brightness** *(float) --*

      Value representing brightness of the face. The service returns a value between 0 and
      100 (inclusive). A higher value indicates a brighter face image.

    - **Sharpness** *(float) --*

      Value representing sharpness of the face. The service returns a value between 0 and 100
      (inclusive). A higher value indicates a sharper face image.
    """


_ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef",
    {
        "BoundingBox": ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef,
        "Confidence": float,
        "Landmarks": List[
            ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef
        ],
        "Pose": ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef,
        "Quality": ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef,
    },
    total=False,
)


class ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef(
    _ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef
):
    """
    Type definition for `ClientRecognizeCelebritiesResponse` `UnrecognizedFaces`

    Provides face metadata for target image faces that are analyzed by ``CompareFaces`` and
    ``RecognizeCelebrities`` .

    - **BoundingBox** *(dict) --*

      Bounding box of the face.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **Confidence** *(float) --*

      Level of confidence that what the bounding box contains is a face.

    - **Landmarks** *(list) --*

      An array of facial landmarks.

      - *(dict) --*

        Indicates the location of the landmark on the face.

        - **Type** *(string) --*

          Type of landmark.

        - **X** *(float) --*

          The x-coordinate from the top left of the landmark expressed as the ratio of the
          width of the image. For example, if the image is 700 x 200 and the x-coordinate of
          the landmark is at 350 pixels, this value is 0.5.

        - **Y** *(float) --*

          The y-coordinate from the top left of the landmark expressed as the ratio of the
          height of the image. For example, if the image is 700 x 200 and the y-coordinate of
          the landmark is at 100 pixels, this value is 0.5.

    - **Pose** *(dict) --*

      Indicates the pose of the face as determined by its pitch, roll, and yaw.

      - **Roll** *(float) --*

        Value representing the face rotation on the roll axis.

      - **Yaw** *(float) --*

        Value representing the face rotation on the yaw axis.

      - **Pitch** *(float) --*

        Value representing the face rotation on the pitch axis.

    - **Quality** *(dict) --*

      Identifies face image brightness and sharpness.

      - **Brightness** *(float) --*

        Value representing brightness of the face. The service returns a value between 0 and
        100 (inclusive). A higher value indicates a brighter face image.

      - **Sharpness** *(float) --*

        Value representing sharpness of the face. The service returns a value between 0 and 100
        (inclusive). A higher value indicates a sharper face image.
    """


_ClientRecognizeCelebritiesResponseTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseTypeDef",
    {
        "CelebrityFaces": List[ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef],
        "UnrecognizedFaces": List[
            ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef
        ],
        "OrientationCorrection": str,
    },
    total=False,
)


class ClientRecognizeCelebritiesResponseTypeDef(
    _ClientRecognizeCelebritiesResponseTypeDef
):
    """
    Type definition for `ClientRecognizeCelebrities` `Response`

    - **CelebrityFaces** *(list) --*

      Details about each celebrity found in the image. Amazon Rekognition can detect a maximum of
      15 celebrities in an image.

      - *(dict) --*

        Provides information about a celebrity recognized by the  RecognizeCelebrities operation.

        - **Urls** *(list) --*

          An array of URLs pointing to additional information about the celebrity. If there is no
          additional information about the celebrity, this list is empty.

          - *(string) --*

        - **Name** *(string) --*

          The name of the celebrity.

        - **Id** *(string) --*

          A unique identifier for the celebrity.

        - **Face** *(dict) --*

          Provides information about the celebrity's face, such as its location on the image.

          - **BoundingBox** *(dict) --*

            Bounding box of the face.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **Confidence** *(float) --*

            Level of confidence that what the bounding box contains is a face.

          - **Landmarks** *(list) --*

            An array of facial landmarks.

            - *(dict) --*

              Indicates the location of the landmark on the face.

              - **Type** *(string) --*

                Type of landmark.

              - **X** *(float) --*

                The x-coordinate from the top left of the landmark expressed as the ratio of the
                width of the image. For example, if the image is 700 x 200 and the x-coordinate of
                the landmark is at 350 pixels, this value is 0.5.

              - **Y** *(float) --*

                The y-coordinate from the top left of the landmark expressed as the ratio of the
                height of the image. For example, if the image is 700 x 200 and the y-coordinate of
                the landmark is at 100 pixels, this value is 0.5.

          - **Pose** *(dict) --*

            Indicates the pose of the face as determined by its pitch, roll, and yaw.

            - **Roll** *(float) --*

              Value representing the face rotation on the roll axis.

            - **Yaw** *(float) --*

              Value representing the face rotation on the yaw axis.

            - **Pitch** *(float) --*

              Value representing the face rotation on the pitch axis.

          - **Quality** *(dict) --*

            Identifies face image brightness and sharpness.

            - **Brightness** *(float) --*

              Value representing brightness of the face. The service returns a value between 0 and
              100 (inclusive). A higher value indicates a brighter face image.

            - **Sharpness** *(float) --*

              Value representing sharpness of the face. The service returns a value between 0 and
              100 (inclusive). A higher value indicates a sharper face image.

        - **MatchConfidence** *(float) --*

          The confidence, in percentage, that Amazon Rekognition has that the recognized face is
          the celebrity.

    - **UnrecognizedFaces** *(list) --*

      Details about each unrecognized face in the image.

      - *(dict) --*

        Provides face metadata for target image faces that are analyzed by ``CompareFaces`` and
        ``RecognizeCelebrities`` .

        - **BoundingBox** *(dict) --*

          Bounding box of the face.

          - **Width** *(float) --*

            Width of the bounding box as a ratio of the overall image width.

          - **Height** *(float) --*

            Height of the bounding box as a ratio of the overall image height.

          - **Left** *(float) --*

            Left coordinate of the bounding box as a ratio of overall image width.

          - **Top** *(float) --*

            Top coordinate of the bounding box as a ratio of overall image height.

        - **Confidence** *(float) --*

          Level of confidence that what the bounding box contains is a face.

        - **Landmarks** *(list) --*

          An array of facial landmarks.

          - *(dict) --*

            Indicates the location of the landmark on the face.

            - **Type** *(string) --*

              Type of landmark.

            - **X** *(float) --*

              The x-coordinate from the top left of the landmark expressed as the ratio of the
              width of the image. For example, if the image is 700 x 200 and the x-coordinate of
              the landmark is at 350 pixels, this value is 0.5.

            - **Y** *(float) --*

              The y-coordinate from the top left of the landmark expressed as the ratio of the
              height of the image. For example, if the image is 700 x 200 and the y-coordinate of
              the landmark is at 100 pixels, this value is 0.5.

        - **Pose** *(dict) --*

          Indicates the pose of the face as determined by its pitch, roll, and yaw.

          - **Roll** *(float) --*

            Value representing the face rotation on the roll axis.

          - **Yaw** *(float) --*

            Value representing the face rotation on the yaw axis.

          - **Pitch** *(float) --*

            Value representing the face rotation on the pitch axis.

        - **Quality** *(dict) --*

          Identifies face image brightness and sharpness.

          - **Brightness** *(float) --*

            Value representing brightness of the face. The service returns a value between 0 and
            100 (inclusive). A higher value indicates a brighter face image.

          - **Sharpness** *(float) --*

            Value representing sharpness of the face. The service returns a value between 0 and 100
            (inclusive). A higher value indicates a sharper face image.

    - **OrientationCorrection** *(string) --*

      The orientation of the input image (counterclockwise direction). If your application displays
      the image, you can use this value to correct the orientation. The bounding box coordinates
      returned in ``CelebrityFaces`` and ``UnrecognizedFaces`` represent face locations before the
      image orientation is corrected.

      .. note::

        If the input image is in .jpeg format, it might contain exchangeable image (Exif) metadata
        that includes the image's orientation. If so, and the Exif metadata for the input image
        populates the orientation field, the value of ``OrientationCorrection`` is null. The
        ``CelebrityFaces`` and ``UnrecognizedFaces`` bounding box coordinates represent face
        locations after Exif metadata is used to correct the image orientation. Images in .png
        format don't contain Exif metadata.
    """


_ClientSearchFacesByImageImageS3ObjectTypeDef = TypedDict(
    "_ClientSearchFacesByImageImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientSearchFacesByImageImageS3ObjectTypeDef(
    _ClientSearchFacesByImageImageS3ObjectTypeDef
):
    """
    Type definition for `ClientSearchFacesByImageImage` `S3Object`

    Identifies an S3 object as the image source.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientSearchFacesByImageImageTypeDef = TypedDict(
    "_ClientSearchFacesByImageImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientSearchFacesByImageImageS3ObjectTypeDef},
    total=False,
)


class ClientSearchFacesByImageImageTypeDef(_ClientSearchFacesByImageImageTypeDef):
    """
    Type definition for `ClientSearchFacesByImage` `Image`

    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes is not supported.

    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image
    bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.

    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.

    - **S3Object** *(dict) --*

      Identifies an S3 object as the image source.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef = TypedDict(
    "_ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef(
    _ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef
):
    """
    Type definition for `ClientSearchFacesByImageResponseFaceMatchesFace` `BoundingBox`

    Bounding box of the face.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef = TypedDict(
    "_ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": float,
    },
    total=False,
)


class ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef(
    _ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef
):
    """
    Type definition for `ClientSearchFacesByImageResponseFaceMatches` `Face`

    Describes the face properties such as the bounding box, face ID, image ID of the source
    image, and external image ID that you assigned.

    - **FaceId** *(string) --*

      Unique identifier that Amazon Rekognition assigns to the face.

    - **BoundingBox** *(dict) --*

      Bounding box of the face.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **ImageId** *(string) --*

      Unique identifier that Amazon Rekognition assigns to the input image.

    - **ExternalImageId** *(string) --*

      Identifier that you assign to all the faces in the input image.

    - **Confidence** *(float) --*

      Confidence level that the bounding box contains a face (and not a different object such
      as a tree).
    """


_ClientSearchFacesByImageResponseFaceMatchesTypeDef = TypedDict(
    "_ClientSearchFacesByImageResponseFaceMatchesTypeDef",
    {
        "Similarity": float,
        "Face": ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef,
    },
    total=False,
)


class ClientSearchFacesByImageResponseFaceMatchesTypeDef(
    _ClientSearchFacesByImageResponseFaceMatchesTypeDef
):
    """
    Type definition for `ClientSearchFacesByImageResponse` `FaceMatches`

    Provides face metadata. In addition, it also provides the confidence in the match of this
    face with the input face.

    - **Similarity** *(float) --*

      Confidence in the match of this face with the input face.

    - **Face** *(dict) --*

      Describes the face properties such as the bounding box, face ID, image ID of the source
      image, and external image ID that you assigned.

      - **FaceId** *(string) --*

        Unique identifier that Amazon Rekognition assigns to the face.

      - **BoundingBox** *(dict) --*

        Bounding box of the face.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **ImageId** *(string) --*

        Unique identifier that Amazon Rekognition assigns to the input image.

      - **ExternalImageId** *(string) --*

        Identifier that you assign to all the faces in the input image.

      - **Confidence** *(float) --*

        Confidence level that the bounding box contains a face (and not a different object such
        as a tree).
    """


_ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef = TypedDict(
    "_ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef(
    _ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef
):
    """
    Type definition for `ClientSearchFacesByImageResponse` `SearchedFaceBoundingBox`

    The bounding box around the face in the input image that Amazon Rekognition used for the
    search.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientSearchFacesByImageResponseTypeDef = TypedDict(
    "_ClientSearchFacesByImageResponseTypeDef",
    {
        "SearchedFaceBoundingBox": ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef,
        "SearchedFaceConfidence": float,
        "FaceMatches": List[ClientSearchFacesByImageResponseFaceMatchesTypeDef],
        "FaceModelVersion": str,
    },
    total=False,
)


class ClientSearchFacesByImageResponseTypeDef(_ClientSearchFacesByImageResponseTypeDef):
    """
    Type definition for `ClientSearchFacesByImage` `Response`

    - **SearchedFaceBoundingBox** *(dict) --*

      The bounding box around the face in the input image that Amazon Rekognition used for the
      search.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **SearchedFaceConfidence** *(float) --*

      The level of confidence that the ``searchedFaceBoundingBox`` , contains a face.

    - **FaceMatches** *(list) --*

      An array of faces that match the input face, along with the confidence in the match.

      - *(dict) --*

        Provides face metadata. In addition, it also provides the confidence in the match of this
        face with the input face.

        - **Similarity** *(float) --*

          Confidence in the match of this face with the input face.

        - **Face** *(dict) --*

          Describes the face properties such as the bounding box, face ID, image ID of the source
          image, and external image ID that you assigned.

          - **FaceId** *(string) --*

            Unique identifier that Amazon Rekognition assigns to the face.

          - **BoundingBox** *(dict) --*

            Bounding box of the face.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **ImageId** *(string) --*

            Unique identifier that Amazon Rekognition assigns to the input image.

          - **ExternalImageId** *(string) --*

            Identifier that you assign to all the faces in the input image.

          - **Confidence** *(float) --*

            Confidence level that the bounding box contains a face (and not a different object such
            as a tree).

    - **FaceModelVersion** *(string) --*

      Version number of the face detection model associated with the input collection
      (``CollectionId`` ).
    """


_ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef = TypedDict(
    "_ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef(
    _ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef
):
    """
    Type definition for `ClientSearchFacesResponseFaceMatchesFace` `BoundingBox`

    Bounding box of the face.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ClientSearchFacesResponseFaceMatchesFaceTypeDef = TypedDict(
    "_ClientSearchFacesResponseFaceMatchesFaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": float,
    },
    total=False,
)


class ClientSearchFacesResponseFaceMatchesFaceTypeDef(
    _ClientSearchFacesResponseFaceMatchesFaceTypeDef
):
    """
    Type definition for `ClientSearchFacesResponseFaceMatches` `Face`

    Describes the face properties such as the bounding box, face ID, image ID of the source
    image, and external image ID that you assigned.

    - **FaceId** *(string) --*

      Unique identifier that Amazon Rekognition assigns to the face.

    - **BoundingBox** *(dict) --*

      Bounding box of the face.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **ImageId** *(string) --*

      Unique identifier that Amazon Rekognition assigns to the input image.

    - **ExternalImageId** *(string) --*

      Identifier that you assign to all the faces in the input image.

    - **Confidence** *(float) --*

      Confidence level that the bounding box contains a face (and not a different object such
      as a tree).
    """


_ClientSearchFacesResponseFaceMatchesTypeDef = TypedDict(
    "_ClientSearchFacesResponseFaceMatchesTypeDef",
    {"Similarity": float, "Face": ClientSearchFacesResponseFaceMatchesFaceTypeDef},
    total=False,
)


class ClientSearchFacesResponseFaceMatchesTypeDef(
    _ClientSearchFacesResponseFaceMatchesTypeDef
):
    """
    Type definition for `ClientSearchFacesResponse` `FaceMatches`

    Provides face metadata. In addition, it also provides the confidence in the match of this
    face with the input face.

    - **Similarity** *(float) --*

      Confidence in the match of this face with the input face.

    - **Face** *(dict) --*

      Describes the face properties such as the bounding box, face ID, image ID of the source
      image, and external image ID that you assigned.

      - **FaceId** *(string) --*

        Unique identifier that Amazon Rekognition assigns to the face.

      - **BoundingBox** *(dict) --*

        Bounding box of the face.

        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.

        - **Height** *(float) --*

          Height of the bounding box as a ratio of the overall image height.

        - **Left** *(float) --*

          Left coordinate of the bounding box as a ratio of overall image width.

        - **Top** *(float) --*

          Top coordinate of the bounding box as a ratio of overall image height.

      - **ImageId** *(string) --*

        Unique identifier that Amazon Rekognition assigns to the input image.

      - **ExternalImageId** *(string) --*

        Identifier that you assign to all the faces in the input image.

      - **Confidence** *(float) --*

        Confidence level that the bounding box contains a face (and not a different object such
        as a tree).
    """


_ClientSearchFacesResponseTypeDef = TypedDict(
    "_ClientSearchFacesResponseTypeDef",
    {
        "SearchedFaceId": str,
        "FaceMatches": List[ClientSearchFacesResponseFaceMatchesTypeDef],
        "FaceModelVersion": str,
    },
    total=False,
)


class ClientSearchFacesResponseTypeDef(_ClientSearchFacesResponseTypeDef):
    """
    Type definition for `ClientSearchFaces` `Response`

    - **SearchedFaceId** *(string) --*

      ID of the face that was searched for matches in a collection.

    - **FaceMatches** *(list) --*

      An array of faces that matched the input face, along with the confidence in the match.

      - *(dict) --*

        Provides face metadata. In addition, it also provides the confidence in the match of this
        face with the input face.

        - **Similarity** *(float) --*

          Confidence in the match of this face with the input face.

        - **Face** *(dict) --*

          Describes the face properties such as the bounding box, face ID, image ID of the source
          image, and external image ID that you assigned.

          - **FaceId** *(string) --*

            Unique identifier that Amazon Rekognition assigns to the face.

          - **BoundingBox** *(dict) --*

            Bounding box of the face.

            - **Width** *(float) --*

              Width of the bounding box as a ratio of the overall image width.

            - **Height** *(float) --*

              Height of the bounding box as a ratio of the overall image height.

            - **Left** *(float) --*

              Left coordinate of the bounding box as a ratio of overall image width.

            - **Top** *(float) --*

              Top coordinate of the bounding box as a ratio of overall image height.

          - **ImageId** *(string) --*

            Unique identifier that Amazon Rekognition assigns to the input image.

          - **ExternalImageId** *(string) --*

            Identifier that you assign to all the faces in the input image.

          - **Confidence** *(float) --*

            Confidence level that the bounding box contains a face (and not a different object such
            as a tree).

    - **FaceModelVersion** *(string) --*

      Version number of the face detection model associated with the input collection
      (``CollectionId`` ).
    """


_ClientStartCelebrityRecognitionNotificationChannelTypeDef = TypedDict(
    "_ClientStartCelebrityRecognitionNotificationChannelTypeDef",
    {"SNSTopicArn": str, "RoleArn": str},
)


class ClientStartCelebrityRecognitionNotificationChannelTypeDef(
    _ClientStartCelebrityRecognitionNotificationChannelTypeDef
):
    """
    Type definition for `ClientStartCelebrityRecognition` `NotificationChannel`

    The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish the completion status
    of the celebrity recognition analysis to.

    - **SNSTopicArn** *(string) --* **[REQUIRED]**

      The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

    - **RoleArn** *(string) --* **[REQUIRED]**

      The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS
      topic.
    """


_ClientStartCelebrityRecognitionResponseTypeDef = TypedDict(
    "_ClientStartCelebrityRecognitionResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartCelebrityRecognitionResponseTypeDef(
    _ClientStartCelebrityRecognitionResponseTypeDef
):
    """
    Type definition for `ClientStartCelebrityRecognition` `Response`

    - **JobId** *(string) --*

      The identifier for the celebrity recognition analysis job. Use ``JobId`` to identify the job
      in a subsequent call to ``GetCelebrityRecognition`` .
    """


_ClientStartCelebrityRecognitionVideoS3ObjectTypeDef = TypedDict(
    "_ClientStartCelebrityRecognitionVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartCelebrityRecognitionVideoS3ObjectTypeDef(
    _ClientStartCelebrityRecognitionVideoS3ObjectTypeDef
):
    """
    Type definition for `ClientStartCelebrityRecognitionVideo` `S3Object`

    The Amazon S3 bucket name and file name for the video.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientStartCelebrityRecognitionVideoTypeDef = TypedDict(
    "_ClientStartCelebrityRecognitionVideoTypeDef",
    {"S3Object": ClientStartCelebrityRecognitionVideoS3ObjectTypeDef},
    total=False,
)


class ClientStartCelebrityRecognitionVideoTypeDef(
    _ClientStartCelebrityRecognitionVideoTypeDef
):
    """
    Type definition for `ClientStartCelebrityRecognition` `Video`

    The video in which you want to recognize celebrities. The video must be stored in an Amazon S3
    bucket.

    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientStartContentModerationNotificationChannelTypeDef = TypedDict(
    "_ClientStartContentModerationNotificationChannelTypeDef",
    {"SNSTopicArn": str, "RoleArn": str},
)


class ClientStartContentModerationNotificationChannelTypeDef(
    _ClientStartContentModerationNotificationChannelTypeDef
):
    """
    Type definition for `ClientStartContentModeration` `NotificationChannel`

    The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish the completion status
    of the unsafe content analysis to.

    - **SNSTopicArn** *(string) --* **[REQUIRED]**

      The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

    - **RoleArn** *(string) --* **[REQUIRED]**

      The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS
      topic.
    """


_ClientStartContentModerationResponseTypeDef = TypedDict(
    "_ClientStartContentModerationResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartContentModerationResponseTypeDef(
    _ClientStartContentModerationResponseTypeDef
):
    """
    Type definition for `ClientStartContentModeration` `Response`

    - **JobId** *(string) --*

      The identifier for the unsafe content analysis job. Use ``JobId`` to identify the job in a
      subsequent call to ``GetContentModeration`` .
    """


_ClientStartContentModerationVideoS3ObjectTypeDef = TypedDict(
    "_ClientStartContentModerationVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartContentModerationVideoS3ObjectTypeDef(
    _ClientStartContentModerationVideoS3ObjectTypeDef
):
    """
    Type definition for `ClientStartContentModerationVideo` `S3Object`

    The Amazon S3 bucket name and file name for the video.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientStartContentModerationVideoTypeDef = TypedDict(
    "_ClientStartContentModerationVideoTypeDef",
    {"S3Object": ClientStartContentModerationVideoS3ObjectTypeDef},
    total=False,
)


class ClientStartContentModerationVideoTypeDef(
    _ClientStartContentModerationVideoTypeDef
):
    """
    Type definition for `ClientStartContentModeration` `Video`

    The video in which you want to detect unsafe content. The video must be stored in an Amazon S3
    bucket.

    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientStartFaceDetectionNotificationChannelTypeDef = TypedDict(
    "_ClientStartFaceDetectionNotificationChannelTypeDef",
    {"SNSTopicArn": str, "RoleArn": str},
)


class ClientStartFaceDetectionNotificationChannelTypeDef(
    _ClientStartFaceDetectionNotificationChannelTypeDef
):
    """
    Type definition for `ClientStartFaceDetection` `NotificationChannel`

    The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the
    completion status of the face detection operation.

    - **SNSTopicArn** *(string) --* **[REQUIRED]**

      The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

    - **RoleArn** *(string) --* **[REQUIRED]**

      The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS
      topic.
    """


_ClientStartFaceDetectionResponseTypeDef = TypedDict(
    "_ClientStartFaceDetectionResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartFaceDetectionResponseTypeDef(_ClientStartFaceDetectionResponseTypeDef):
    """
    Type definition for `ClientStartFaceDetection` `Response`

    - **JobId** *(string) --*

      The identifier for the face detection job. Use ``JobId`` to identify the job in a subsequent
      call to ``GetFaceDetection`` .
    """


_ClientStartFaceDetectionVideoS3ObjectTypeDef = TypedDict(
    "_ClientStartFaceDetectionVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartFaceDetectionVideoS3ObjectTypeDef(
    _ClientStartFaceDetectionVideoS3ObjectTypeDef
):
    """
    Type definition for `ClientStartFaceDetectionVideo` `S3Object`

    The Amazon S3 bucket name and file name for the video.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientStartFaceDetectionVideoTypeDef = TypedDict(
    "_ClientStartFaceDetectionVideoTypeDef",
    {"S3Object": ClientStartFaceDetectionVideoS3ObjectTypeDef},
    total=False,
)


class ClientStartFaceDetectionVideoTypeDef(_ClientStartFaceDetectionVideoTypeDef):
    """
    Type definition for `ClientStartFaceDetection` `Video`

    The video in which you want to detect faces. The video must be stored in an Amazon S3 bucket.

    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientStartFaceSearchNotificationChannelTypeDef = TypedDict(
    "_ClientStartFaceSearchNotificationChannelTypeDef",
    {"SNSTopicArn": str, "RoleArn": str},
)


class ClientStartFaceSearchNotificationChannelTypeDef(
    _ClientStartFaceSearchNotificationChannelTypeDef
):
    """
    Type definition for `ClientStartFaceSearch` `NotificationChannel`

    The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the
    completion status of the search.

    - **SNSTopicArn** *(string) --* **[REQUIRED]**

      The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

    - **RoleArn** *(string) --* **[REQUIRED]**

      The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS
      topic.
    """


_ClientStartFaceSearchResponseTypeDef = TypedDict(
    "_ClientStartFaceSearchResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartFaceSearchResponseTypeDef(_ClientStartFaceSearchResponseTypeDef):
    """
    Type definition for `ClientStartFaceSearch` `Response`

    - **JobId** *(string) --*

      The identifier for the search job. Use ``JobId`` to identify the job in a subsequent call to
      ``GetFaceSearch`` .
    """


_ClientStartFaceSearchVideoS3ObjectTypeDef = TypedDict(
    "_ClientStartFaceSearchVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartFaceSearchVideoS3ObjectTypeDef(
    _ClientStartFaceSearchVideoS3ObjectTypeDef
):
    """
    Type definition for `ClientStartFaceSearchVideo` `S3Object`

    The Amazon S3 bucket name and file name for the video.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientStartFaceSearchVideoTypeDef = TypedDict(
    "_ClientStartFaceSearchVideoTypeDef",
    {"S3Object": ClientStartFaceSearchVideoS3ObjectTypeDef},
    total=False,
)


class ClientStartFaceSearchVideoTypeDef(_ClientStartFaceSearchVideoTypeDef):
    """
    Type definition for `ClientStartFaceSearch` `Video`

    The video you want to search. The video must be stored in an Amazon S3 bucket.

    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientStartLabelDetectionNotificationChannelTypeDef = TypedDict(
    "_ClientStartLabelDetectionNotificationChannelTypeDef",
    {"SNSTopicArn": str, "RoleArn": str},
)


class ClientStartLabelDetectionNotificationChannelTypeDef(
    _ClientStartLabelDetectionNotificationChannelTypeDef
):
    """
    Type definition for `ClientStartLabelDetection` `NotificationChannel`

    The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the completion status of
    the label detection operation to.

    - **SNSTopicArn** *(string) --* **[REQUIRED]**

      The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

    - **RoleArn** *(string) --* **[REQUIRED]**

      The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS
      topic.
    """


_ClientStartLabelDetectionResponseTypeDef = TypedDict(
    "_ClientStartLabelDetectionResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartLabelDetectionResponseTypeDef(
    _ClientStartLabelDetectionResponseTypeDef
):
    """
    Type definition for `ClientStartLabelDetection` `Response`

    - **JobId** *(string) --*

      The identifier for the label detection job. Use ``JobId`` to identify the job in a subsequent
      call to ``GetLabelDetection`` .
    """


_ClientStartLabelDetectionVideoS3ObjectTypeDef = TypedDict(
    "_ClientStartLabelDetectionVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartLabelDetectionVideoS3ObjectTypeDef(
    _ClientStartLabelDetectionVideoS3ObjectTypeDef
):
    """
    Type definition for `ClientStartLabelDetectionVideo` `S3Object`

    The Amazon S3 bucket name and file name for the video.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientStartLabelDetectionVideoTypeDef = TypedDict(
    "_ClientStartLabelDetectionVideoTypeDef",
    {"S3Object": ClientStartLabelDetectionVideoS3ObjectTypeDef},
    total=False,
)


class ClientStartLabelDetectionVideoTypeDef(_ClientStartLabelDetectionVideoTypeDef):
    """
    Type definition for `ClientStartLabelDetection` `Video`

    The video in which you want to detect labels. The video must be stored in an Amazon S3 bucket.

    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ClientStartPersonTrackingNotificationChannelTypeDef = TypedDict(
    "_ClientStartPersonTrackingNotificationChannelTypeDef",
    {"SNSTopicArn": str, "RoleArn": str},
)


class ClientStartPersonTrackingNotificationChannelTypeDef(
    _ClientStartPersonTrackingNotificationChannelTypeDef
):
    """
    Type definition for `ClientStartPersonTracking` `NotificationChannel`

    The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the completion status of
    the people detection operation to.

    - **SNSTopicArn** *(string) --* **[REQUIRED]**

      The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

    - **RoleArn** *(string) --* **[REQUIRED]**

      The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS
      topic.
    """


_ClientStartPersonTrackingResponseTypeDef = TypedDict(
    "_ClientStartPersonTrackingResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartPersonTrackingResponseTypeDef(
    _ClientStartPersonTrackingResponseTypeDef
):
    """
    Type definition for `ClientStartPersonTracking` `Response`

    - **JobId** *(string) --*

      The identifier for the person detection job. Use ``JobId`` to identify the job in a
      subsequent call to ``GetPersonTracking`` .
    """


_ClientStartPersonTrackingVideoS3ObjectTypeDef = TypedDict(
    "_ClientStartPersonTrackingVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartPersonTrackingVideoS3ObjectTypeDef(
    _ClientStartPersonTrackingVideoS3ObjectTypeDef
):
    """
    Type definition for `ClientStartPersonTrackingVideo` `S3Object`

    The Amazon S3 bucket name and file name for the video.

    - **Bucket** *(string) --*

      Name of the S3 bucket.

    - **Name** *(string) --*

      S3 object key name.

    - **Version** *(string) --*

      If the bucket is versioning enabled, you can specify the object version.
    """


_ClientStartPersonTrackingVideoTypeDef = TypedDict(
    "_ClientStartPersonTrackingVideoTypeDef",
    {"S3Object": ClientStartPersonTrackingVideoS3ObjectTypeDef},
    total=False,
)


class ClientStartPersonTrackingVideoTypeDef(_ClientStartPersonTrackingVideoTypeDef):
    """
    Type definition for `ClientStartPersonTracking` `Video`

    The video in which you want to detect people. The video must be stored in an Amazon S3 bucket.

    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.

      - **Bucket** *(string) --*

        Name of the S3 bucket.

      - **Name** *(string) --*

        S3 object key name.

      - **Version** *(string) --*

        If the bucket is versioning enabled, you can specify the object version.
    """


_ListCollectionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCollectionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCollectionsPaginatePaginationConfigTypeDef(
    _ListCollectionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCollectionsPaginate` `PaginationConfig`

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


_ListCollectionsPaginateResponseTypeDef = TypedDict(
    "_ListCollectionsPaginateResponseTypeDef",
    {"CollectionIds": List[str], "FaceModelVersions": List[str]},
    total=False,
)


class ListCollectionsPaginateResponseTypeDef(_ListCollectionsPaginateResponseTypeDef):
    """
    Type definition for `ListCollectionsPaginate` `Response`

    - **CollectionIds** *(list) --*

      An array of collection IDs.

      - *(string) --*

    - **FaceModelVersions** *(list) --*

      Version numbers of the face detection models associated with the collections in the array
      ``CollectionIds`` . For example, the value of ``FaceModelVersions[2]`` is the version number
      for the face detection model used by the collection in ``CollectionId[2]`` .

      - *(string) --*
    """


_ListFacesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFacesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFacesPaginatePaginationConfigTypeDef(
    _ListFacesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFacesPaginate` `PaginationConfig`

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


_ListFacesPaginateResponseFacesBoundingBoxTypeDef = TypedDict(
    "_ListFacesPaginateResponseFacesBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ListFacesPaginateResponseFacesBoundingBoxTypeDef(
    _ListFacesPaginateResponseFacesBoundingBoxTypeDef
):
    """
    Type definition for `ListFacesPaginateResponseFaces` `BoundingBox`

    Bounding box of the face.

    - **Width** *(float) --*

      Width of the bounding box as a ratio of the overall image width.

    - **Height** *(float) --*

      Height of the bounding box as a ratio of the overall image height.

    - **Left** *(float) --*

      Left coordinate of the bounding box as a ratio of overall image width.

    - **Top** *(float) --*

      Top coordinate of the bounding box as a ratio of overall image height.
    """


_ListFacesPaginateResponseFacesTypeDef = TypedDict(
    "_ListFacesPaginateResponseFacesTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ListFacesPaginateResponseFacesBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": float,
    },
    total=False,
)


class ListFacesPaginateResponseFacesTypeDef(_ListFacesPaginateResponseFacesTypeDef):
    """
    Type definition for `ListFacesPaginateResponse` `Faces`

    Describes the face properties such as the bounding box, face ID, image ID of the input
    image, and external image ID that you assigned.

    - **FaceId** *(string) --*

      Unique identifier that Amazon Rekognition assigns to the face.

    - **BoundingBox** *(dict) --*

      Bounding box of the face.

      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.

      - **Height** *(float) --*

        Height of the bounding box as a ratio of the overall image height.

      - **Left** *(float) --*

        Left coordinate of the bounding box as a ratio of overall image width.

      - **Top** *(float) --*

        Top coordinate of the bounding box as a ratio of overall image height.

    - **ImageId** *(string) --*

      Unique identifier that Amazon Rekognition assigns to the input image.

    - **ExternalImageId** *(string) --*

      Identifier that you assign to all the faces in the input image.

    - **Confidence** *(float) --*

      Confidence level that the bounding box contains a face (and not a different object such
      as a tree).
    """


_ListFacesPaginateResponseTypeDef = TypedDict(
    "_ListFacesPaginateResponseTypeDef",
    {"Faces": List[ListFacesPaginateResponseFacesTypeDef], "FaceModelVersion": str},
    total=False,
)


class ListFacesPaginateResponseTypeDef(_ListFacesPaginateResponseTypeDef):
    """
    Type definition for `ListFacesPaginate` `Response`

    - **Faces** *(list) --*

      An array of ``Face`` objects.

      - *(dict) --*

        Describes the face properties such as the bounding box, face ID, image ID of the input
        image, and external image ID that you assigned.

        - **FaceId** *(string) --*

          Unique identifier that Amazon Rekognition assigns to the face.

        - **BoundingBox** *(dict) --*

          Bounding box of the face.

          - **Width** *(float) --*

            Width of the bounding box as a ratio of the overall image width.

          - **Height** *(float) --*

            Height of the bounding box as a ratio of the overall image height.

          - **Left** *(float) --*

            Left coordinate of the bounding box as a ratio of overall image width.

          - **Top** *(float) --*

            Top coordinate of the bounding box as a ratio of overall image height.

        - **ImageId** *(string) --*

          Unique identifier that Amazon Rekognition assigns to the input image.

        - **ExternalImageId** *(string) --*

          Identifier that you assign to all the faces in the input image.

        - **Confidence** *(float) --*

          Confidence level that the bounding box contains a face (and not a different object such
          as a tree).

    - **FaceModelVersion** *(string) --*

      Version number of the face detection model associated with the input collection
      (``CollectionId`` ).
    """


_ListStreamProcessorsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStreamProcessorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStreamProcessorsPaginatePaginationConfigTypeDef(
    _ListStreamProcessorsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListStreamProcessorsPaginate` `PaginationConfig`

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


_ListStreamProcessorsPaginateResponseStreamProcessorsTypeDef = TypedDict(
    "_ListStreamProcessorsPaginateResponseStreamProcessorsTypeDef",
    {"Name": str, "Status": str},
    total=False,
)


class ListStreamProcessorsPaginateResponseStreamProcessorsTypeDef(
    _ListStreamProcessorsPaginateResponseStreamProcessorsTypeDef
):
    """
    Type definition for `ListStreamProcessorsPaginateResponse` `StreamProcessors`

    An object that recognizes faces in a streaming video. An Amazon Rekognition stream
    processor is created by a call to  CreateStreamProcessor . The request parameters for
    ``CreateStreamProcessor`` describe the Kinesis video stream source for the streaming video,
    face recognition parameters, and where to stream the analysis resullts.

    - **Name** *(string) --*

      Name of the Amazon Rekognition stream processor.

    - **Status** *(string) --*

      Current status of the Amazon Rekognition stream processor.
    """


_ListStreamProcessorsPaginateResponseTypeDef = TypedDict(
    "_ListStreamProcessorsPaginateResponseTypeDef",
    {
        "StreamProcessors": List[
            ListStreamProcessorsPaginateResponseStreamProcessorsTypeDef
        ]
    },
    total=False,
)


class ListStreamProcessorsPaginateResponseTypeDef(
    _ListStreamProcessorsPaginateResponseTypeDef
):
    """
    Type definition for `ListStreamProcessorsPaginate` `Response`

    - **StreamProcessors** *(list) --*

      List of stream processors that you have created.

      - *(dict) --*

        An object that recognizes faces in a streaming video. An Amazon Rekognition stream
        processor is created by a call to  CreateStreamProcessor . The request parameters for
        ``CreateStreamProcessor`` describe the Kinesis video stream source for the streaming video,
        face recognition parameters, and where to stream the analysis resullts.

        - **Name** *(string) --*

          Name of the Amazon Rekognition stream processor.

        - **Status** *(string) --*

          Current status of the Amazon Rekognition stream processor.
    """
