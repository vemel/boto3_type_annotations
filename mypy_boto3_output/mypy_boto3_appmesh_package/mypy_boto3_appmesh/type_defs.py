"Main interface for appmesh type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateMeshResponsemeshmetadataTypeDef",
    "ClientCreateMeshResponsemeshspecegressFilterTypeDef",
    "ClientCreateMeshResponsemeshspecTypeDef",
    "ClientCreateMeshResponsemeshstatusTypeDef",
    "ClientCreateMeshResponsemeshTypeDef",
    "ClientCreateMeshResponseTypeDef",
    "ClientCreateMeshspecegressFilterTypeDef",
    "ClientCreateMeshspecTypeDef",
    "ClientCreateMeshtagsTypeDef",
    "ClientCreateRouteResponseroutemetadataTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteactionTypeDef",
    "ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    "ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef",
    "ClientCreateRouteResponseroutespechttp2RoutematchTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteactionTypeDef",
    "ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    "ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef",
    "ClientCreateRouteResponseroutespechttpRoutematchTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteTypeDef",
    "ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteResponseroutespectcpRouteactionTypeDef",
    "ClientCreateRouteResponseroutespectcpRouteTypeDef",
    "ClientCreateRouteResponseroutespecTypeDef",
    "ClientCreateRouteResponseroutestatusTypeDef",
    "ClientCreateRouteResponserouteTypeDef",
    "ClientCreateRouteResponseTypeDef",
    "ClientCreateRoutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientCreateRoutespecgrpcRouteactionTypeDef",
    "ClientCreateRoutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientCreateRoutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientCreateRoutespecgrpcRoutematchmetadataTypeDef",
    "ClientCreateRoutespecgrpcRoutematchTypeDef",
    "ClientCreateRoutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRoutespecgrpcRouteretryPolicyTypeDef",
    "ClientCreateRoutespecgrpcRouteTypeDef",
    "ClientCreateRoutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientCreateRoutespechttp2RouteactionTypeDef",
    "ClientCreateRoutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientCreateRoutespechttp2RoutematchheadersmatchTypeDef",
    "ClientCreateRoutespechttp2RoutematchheadersTypeDef",
    "ClientCreateRoutespechttp2RoutematchTypeDef",
    "ClientCreateRoutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRoutespechttp2RouteretryPolicyTypeDef",
    "ClientCreateRoutespechttp2RouteTypeDef",
    "ClientCreateRoutespechttpRouteactionweightedTargetsTypeDef",
    "ClientCreateRoutespechttpRouteactionTypeDef",
    "ClientCreateRoutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientCreateRoutespechttpRoutematchheadersmatchTypeDef",
    "ClientCreateRoutespechttpRoutematchheadersTypeDef",
    "ClientCreateRoutespechttpRoutematchTypeDef",
    "ClientCreateRoutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRoutespechttpRouteretryPolicyTypeDef",
    "ClientCreateRoutespechttpRouteTypeDef",
    "ClientCreateRoutespectcpRouteactionweightedTargetsTypeDef",
    "ClientCreateRoutespectcpRouteactionTypeDef",
    "ClientCreateRoutespectcpRouteTypeDef",
    "ClientCreateRoutespecTypeDef",
    "ClientCreateRoutetagsTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodeTypeDef",
    "ClientCreateVirtualNodeResponseTypeDef",
    "ClientCreateVirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientCreateVirtualNodespecbackendsTypeDef",
    "ClientCreateVirtualNodespeclistenershealthCheckTypeDef",
    "ClientCreateVirtualNodespeclistenersportMappingTypeDef",
    "ClientCreateVirtualNodespeclistenersTypeDef",
    "ClientCreateVirtualNodespecloggingaccessLogfileTypeDef",
    "ClientCreateVirtualNodespecloggingaccessLogTypeDef",
    "ClientCreateVirtualNodespecloggingTypeDef",
    "ClientCreateVirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientCreateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientCreateVirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientCreateVirtualNodespecserviceDiscoveryTypeDef",
    "ClientCreateVirtualNodespecTypeDef",
    "ClientCreateVirtualNodetagsTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterTypeDef",
    "ClientCreateVirtualRouterResponseTypeDef",
    "ClientCreateVirtualRouterspeclistenersportMappingTypeDef",
    "ClientCreateVirtualRouterspeclistenersTypeDef",
    "ClientCreateVirtualRouterspecTypeDef",
    "ClientCreateVirtualRoutertagsTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicespecTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServiceTypeDef",
    "ClientCreateVirtualServiceResponseTypeDef",
    "ClientCreateVirtualServicespecprovidervirtualNodeTypeDef",
    "ClientCreateVirtualServicespecprovidervirtualRouterTypeDef",
    "ClientCreateVirtualServicespecproviderTypeDef",
    "ClientCreateVirtualServicespecTypeDef",
    "ClientCreateVirtualServicetagsTypeDef",
    "ClientDeleteMeshResponsemeshmetadataTypeDef",
    "ClientDeleteMeshResponsemeshspecegressFilterTypeDef",
    "ClientDeleteMeshResponsemeshspecTypeDef",
    "ClientDeleteMeshResponsemeshstatusTypeDef",
    "ClientDeleteMeshResponsemeshTypeDef",
    "ClientDeleteMeshResponseTypeDef",
    "ClientDeleteRouteResponseroutemetadataTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteactionTypeDef",
    "ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    "ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef",
    "ClientDeleteRouteResponseroutespechttpRoutematchTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteTypeDef",
    "ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    "ClientDeleteRouteResponseroutespectcpRouteactionTypeDef",
    "ClientDeleteRouteResponseroutespectcpRouteTypeDef",
    "ClientDeleteRouteResponseroutespecTypeDef",
    "ClientDeleteRouteResponseroutestatusTypeDef",
    "ClientDeleteRouteResponserouteTypeDef",
    "ClientDeleteRouteResponseTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodeTypeDef",
    "ClientDeleteVirtualNodeResponseTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterTypeDef",
    "ClientDeleteVirtualRouterResponseTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServiceTypeDef",
    "ClientDeleteVirtualServiceResponseTypeDef",
    "ClientDescribeMeshResponsemeshmetadataTypeDef",
    "ClientDescribeMeshResponsemeshspecegressFilterTypeDef",
    "ClientDescribeMeshResponsemeshspecTypeDef",
    "ClientDescribeMeshResponsemeshstatusTypeDef",
    "ClientDescribeMeshResponsemeshTypeDef",
    "ClientDescribeMeshResponseTypeDef",
    "ClientDescribeRouteResponseroutemetadataTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteactionTypeDef",
    "ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    "ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef",
    "ClientDescribeRouteResponseroutespechttpRoutematchTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteTypeDef",
    "ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    "ClientDescribeRouteResponseroutespectcpRouteactionTypeDef",
    "ClientDescribeRouteResponseroutespectcpRouteTypeDef",
    "ClientDescribeRouteResponseroutespecTypeDef",
    "ClientDescribeRouteResponseroutestatusTypeDef",
    "ClientDescribeRouteResponserouteTypeDef",
    "ClientDescribeRouteResponseTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodeTypeDef",
    "ClientDescribeVirtualNodeResponseTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterTypeDef",
    "ClientDescribeVirtualRouterResponseTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServiceTypeDef",
    "ClientDescribeVirtualServiceResponseTypeDef",
    "ClientListMeshesResponsemeshesTypeDef",
    "ClientListMeshesResponseTypeDef",
    "ClientListRoutesResponseroutesTypeDef",
    "ClientListRoutesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListVirtualNodesResponsevirtualNodesTypeDef",
    "ClientListVirtualNodesResponseTypeDef",
    "ClientListVirtualRoutersResponsevirtualRoutersTypeDef",
    "ClientListVirtualRoutersResponseTypeDef",
    "ClientListVirtualServicesResponsevirtualServicesTypeDef",
    "ClientListVirtualServicesResponseTypeDef",
    "ClientTagResourcetagsTypeDef",
    "ClientUpdateMeshResponsemeshmetadataTypeDef",
    "ClientUpdateMeshResponsemeshspecegressFilterTypeDef",
    "ClientUpdateMeshResponsemeshspecTypeDef",
    "ClientUpdateMeshResponsemeshstatusTypeDef",
    "ClientUpdateMeshResponsemeshTypeDef",
    "ClientUpdateMeshResponseTypeDef",
    "ClientUpdateMeshspecegressFilterTypeDef",
    "ClientUpdateMeshspecTypeDef",
    "ClientUpdateRouteResponseroutemetadataTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteactionTypeDef",
    "ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    "ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef",
    "ClientUpdateRouteResponseroutespechttpRoutematchTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteTypeDef",
    "ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteResponseroutespectcpRouteactionTypeDef",
    "ClientUpdateRouteResponseroutespectcpRouteTypeDef",
    "ClientUpdateRouteResponseroutespecTypeDef",
    "ClientUpdateRouteResponseroutestatusTypeDef",
    "ClientUpdateRouteResponserouteTypeDef",
    "ClientUpdateRouteResponseTypeDef",
    "ClientUpdateRoutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientUpdateRoutespecgrpcRouteactionTypeDef",
    "ClientUpdateRoutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientUpdateRoutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientUpdateRoutespecgrpcRoutematchmetadataTypeDef",
    "ClientUpdateRoutespecgrpcRoutematchTypeDef",
    "ClientUpdateRoutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRoutespecgrpcRouteretryPolicyTypeDef",
    "ClientUpdateRoutespecgrpcRouteTypeDef",
    "ClientUpdateRoutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientUpdateRoutespechttp2RouteactionTypeDef",
    "ClientUpdateRoutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientUpdateRoutespechttp2RoutematchheadersmatchTypeDef",
    "ClientUpdateRoutespechttp2RoutematchheadersTypeDef",
    "ClientUpdateRoutespechttp2RoutematchTypeDef",
    "ClientUpdateRoutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRoutespechttp2RouteretryPolicyTypeDef",
    "ClientUpdateRoutespechttp2RouteTypeDef",
    "ClientUpdateRoutespechttpRouteactionweightedTargetsTypeDef",
    "ClientUpdateRoutespechttpRouteactionTypeDef",
    "ClientUpdateRoutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientUpdateRoutespechttpRoutematchheadersmatchTypeDef",
    "ClientUpdateRoutespechttpRoutematchheadersTypeDef",
    "ClientUpdateRoutespechttpRoutematchTypeDef",
    "ClientUpdateRoutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRoutespechttpRouteretryPolicyTypeDef",
    "ClientUpdateRoutespechttpRouteTypeDef",
    "ClientUpdateRoutespectcpRouteactionweightedTargetsTypeDef",
    "ClientUpdateRoutespectcpRouteactionTypeDef",
    "ClientUpdateRoutespectcpRouteTypeDef",
    "ClientUpdateRoutespecTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodeTypeDef",
    "ClientUpdateVirtualNodeResponseTypeDef",
    "ClientUpdateVirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientUpdateVirtualNodespecbackendsTypeDef",
    "ClientUpdateVirtualNodespeclistenershealthCheckTypeDef",
    "ClientUpdateVirtualNodespeclistenersportMappingTypeDef",
    "ClientUpdateVirtualNodespeclistenersTypeDef",
    "ClientUpdateVirtualNodespecloggingaccessLogfileTypeDef",
    "ClientUpdateVirtualNodespecloggingaccessLogTypeDef",
    "ClientUpdateVirtualNodespecloggingTypeDef",
    "ClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientUpdateVirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientUpdateVirtualNodespecserviceDiscoveryTypeDef",
    "ClientUpdateVirtualNodespecTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterTypeDef",
    "ClientUpdateVirtualRouterResponseTypeDef",
    "ClientUpdateVirtualRouterspeclistenersportMappingTypeDef",
    "ClientUpdateVirtualRouterspeclistenersTypeDef",
    "ClientUpdateVirtualRouterspecTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServiceTypeDef",
    "ClientUpdateVirtualServiceResponseTypeDef",
    "ClientUpdateVirtualServicespecprovidervirtualNodeTypeDef",
    "ClientUpdateVirtualServicespecprovidervirtualRouterTypeDef",
    "ClientUpdateVirtualServicespecproviderTypeDef",
    "ClientUpdateVirtualServicespecTypeDef",
    "ListMeshesPaginatePaginationConfigTypeDef",
    "ListMeshesPaginateResponsemeshesTypeDef",
    "ListMeshesPaginateResponseTypeDef",
    "ListRoutesPaginatePaginationConfigTypeDef",
    "ListRoutesPaginateResponseroutesTypeDef",
    "ListRoutesPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponsetagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "ListVirtualNodesPaginatePaginationConfigTypeDef",
    "ListVirtualNodesPaginateResponsevirtualNodesTypeDef",
    "ListVirtualNodesPaginateResponseTypeDef",
    "ListVirtualRoutersPaginatePaginationConfigTypeDef",
    "ListVirtualRoutersPaginateResponsevirtualRoutersTypeDef",
    "ListVirtualRoutersPaginateResponseTypeDef",
    "ListVirtualServicesPaginatePaginationConfigTypeDef",
    "ListVirtualServicesPaginateResponsevirtualServicesTypeDef",
    "ListVirtualServicesPaginateResponseTypeDef",
)


_ClientCreateMeshResponsemeshmetadataTypeDef = TypedDict(
    "_ClientCreateMeshResponsemeshmetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientCreateMeshResponsemeshmetadataTypeDef(
    _ClientCreateMeshResponsemeshmetadataTypeDef
):
    """
    Type definition for `ClientCreateMeshResponsemesh` `metadata`

    The associated metadata for the service mesh.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientCreateMeshResponsemeshspecegressFilterTypeDef = TypedDict(
    "_ClientCreateMeshResponsemeshspecegressFilterTypeDef", {"type": str}, total=False
)


class ClientCreateMeshResponsemeshspecegressFilterTypeDef(
    _ClientCreateMeshResponsemeshspecegressFilterTypeDef
):
    """
    Type definition for `ClientCreateMeshResponsemeshspec` `egressFilter`

    The egress filter rules for the service mesh.

    - **type** *(string) --*

      The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
      from virtual nodes to other defined resources in the service mesh (and any traffic to
      ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
      ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientCreateMeshResponsemeshspecTypeDef = TypedDict(
    "_ClientCreateMeshResponsemeshspecTypeDef",
    {"egressFilter": ClientCreateMeshResponsemeshspecegressFilterTypeDef},
    total=False,
)


class ClientCreateMeshResponsemeshspecTypeDef(_ClientCreateMeshResponsemeshspecTypeDef):
    """
    Type definition for `ClientCreateMeshResponsemesh` `spec`

    The associated specification for the service mesh.

    - **egressFilter** *(dict) --*

      The egress filter rules for the service mesh.

      - **type** *(string) --*

        The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
        from virtual nodes to other defined resources in the service mesh (and any traffic to
        ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
        ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientCreateMeshResponsemeshstatusTypeDef = TypedDict(
    "_ClientCreateMeshResponsemeshstatusTypeDef", {"status": str}, total=False
)


class ClientCreateMeshResponsemeshstatusTypeDef(
    _ClientCreateMeshResponsemeshstatusTypeDef
):
    """
    Type definition for `ClientCreateMeshResponsemesh` `status`

    The status of the service mesh.

    - **status** *(string) --*

      The current mesh status.
    """


_ClientCreateMeshResponsemeshTypeDef = TypedDict(
    "_ClientCreateMeshResponsemeshTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateMeshResponsemeshmetadataTypeDef,
        "spec": ClientCreateMeshResponsemeshspecTypeDef,
        "status": ClientCreateMeshResponsemeshstatusTypeDef,
    },
    total=False,
)


class ClientCreateMeshResponsemeshTypeDef(_ClientCreateMeshResponsemeshTypeDef):
    """
    Type definition for `ClientCreateMeshResponse` `mesh`

    The full description of your service mesh following the create call.

    - **meshName** *(string) --*

      The name of the service mesh.

    - **metadata** *(dict) --*

      The associated metadata for the service mesh.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The associated specification for the service mesh.

      - **egressFilter** *(dict) --*

        The egress filter rules for the service mesh.

        - **type** *(string) --*

          The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
          from virtual nodes to other defined resources in the service mesh (and any traffic to
          ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
          ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.

    - **status** *(dict) --*

      The status of the service mesh.

      - **status** *(string) --*

        The current mesh status.
    """


_ClientCreateMeshResponseTypeDef = TypedDict(
    "_ClientCreateMeshResponseTypeDef",
    {"mesh": ClientCreateMeshResponsemeshTypeDef},
    total=False,
)


class ClientCreateMeshResponseTypeDef(_ClientCreateMeshResponseTypeDef):
    """
    Type definition for `ClientCreateMesh` `Response`

    - **mesh** *(dict) --*

      The full description of your service mesh following the create call.

      - **meshName** *(string) --*

        The name of the service mesh.

      - **metadata** *(dict) --*

        The associated metadata for the service mesh.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The associated specification for the service mesh.

        - **egressFilter** *(dict) --*

          The egress filter rules for the service mesh.

          - **type** *(string) --*

            The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
            from virtual nodes to other defined resources in the service mesh (and any traffic to
            ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
            ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.

      - **status** *(dict) --*

        The status of the service mesh.

        - **status** *(string) --*

          The current mesh status.
    """


_ClientCreateMeshspecegressFilterTypeDef = TypedDict(
    "_ClientCreateMeshspecegressFilterTypeDef", {"type": str}
)


class ClientCreateMeshspecegressFilterTypeDef(_ClientCreateMeshspecegressFilterTypeDef):
    """
    Type definition for `ClientCreateMeshspec` `egressFilter`

    The egress filter rules for the service mesh.

    - **type** *(string) --* **[REQUIRED]**

      The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only from
      virtual nodes to other defined resources in the service mesh (and any traffic to
      ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to ``ALLOW_ALL``
      to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientCreateMeshspecTypeDef = TypedDict(
    "_ClientCreateMeshspecTypeDef",
    {"egressFilter": ClientCreateMeshspecegressFilterTypeDef},
    total=False,
)


class ClientCreateMeshspecTypeDef(_ClientCreateMeshspecTypeDef):
    """
    Type definition for `ClientCreateMesh` `spec`

    The service mesh specification to apply.

    - **egressFilter** *(dict) --*

      The egress filter rules for the service mesh.

      - **type** *(string) --* **[REQUIRED]**

        The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only from
        virtual nodes to other defined resources in the service mesh (and any traffic to
        ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to ``ALLOW_ALL``
        to allow egress to any endpoint inside or outside of the service mesh.
    """


_RequiredClientCreateMeshtagsTypeDef = TypedDict(
    "_RequiredClientCreateMeshtagsTypeDef", {"key": str}
)
_OptionalClientCreateMeshtagsTypeDef = TypedDict(
    "_OptionalClientCreateMeshtagsTypeDef", {"value": str}, total=False
)


class ClientCreateMeshtagsTypeDef(
    _RequiredClientCreateMeshtagsTypeDef, _OptionalClientCreateMeshtagsTypeDef
):
    """
    Type definition for `ClientCreateMesh` `tags`

    Optional metadata that you apply to a resource to assist with categorization and organization.
    Each tag consists of a key and an optional value, both of which you define. Tag keys can have a
    maximum character length of 128 characters, and tag values can have a maximum length of 256
    characters.

    - **key** *(string) --* **[REQUIRED]**

      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
      a category for more specific tag values.

    - **value** *(string) --*

      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
      within a tag category (key).
    """


_ClientCreateRouteResponseroutemetadataTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutemetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientCreateRouteResponseroutemetadataTypeDef(
    _ClientCreateRouteResponseroutemetadataTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroute` `metadata`

    The associated metadata for the route.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespecgrpcRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespecgrpcRoute` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --*

      The end of the range.

    - **start** *(integer) --*

      The start of the range.
    """


_ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespecgrpcRoutematchmetadata` `match`

    An object that represents the data to match from the request.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --*

        The end of the range.

      - **start** *(integer) --*

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    {
        "invert": bool,
        "match": ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespecgrpcRoutematch` `metadata`

    An object that represents the match metadata for the route.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value
      is ``False`` .

    - **match** *(dict) --*

      An object that represents the data to match from the request.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --*

          The end of the range.

        - **start** *(integer) --*

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --*

      The name of the route.
    """


_ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[
            ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef
        ],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespecgrpcRoute` `match`

    An object that represents the criteria for determining a request match.

    - **metadata** *(list) --*

      An object that represents the data to match from the request.

      - *(dict) --*

        An object that represents the match metadata for the route.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value
          is ``False`` .

        - **match** *(dict) --*

          An object that represents the data to match from the request.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --*

              The end of the range.

            - **start** *(integer) --*

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --*

          The name of the route.

    - **methodName** *(string) --*

      The method name to match from the request. If you specify a name, you must also
      specify a ``serviceName`` .

    - **serviceName** *(string) --*

      The fully qualified domain name for the service to match from the request.
    """


_ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespecgrpcRouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[str],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespecgrpcRoute` `retryPolicy`

    An object that represents a retry policy.

    - **grpcRetryEvents** *(list) --*

      Specify at least one of the valid values.

      - *(string) --*

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
      510, and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --*

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --*

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_ClientCreateRouteResponseroutespecgrpcRouteTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRouteTypeDef",
    {
        "action": ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef,
        "match": ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef,
        "retryPolicy": ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRouteTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRouteTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespec` `grpcRoute`

    An object that represents the specification of a GRPC route.

    - **action** *(dict) --*

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.

    - **match** *(dict) --*

      An object that represents the criteria for determining a request match.

      - **metadata** *(list) --*

        An object that represents the data to match from the request.

        - *(dict) --*

          An object that represents the match metadata for the route.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value
            is ``False`` .

          - **match** *(dict) --*

            An object that represents the data to match from the request.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --*

                The end of the range.

              - **start** *(integer) --*

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --*

            The name of the route.

      - **methodName** *(string) --*

        The method name to match from the request. If you specify a name, you must also
        specify a ``serviceName`` .

      - **serviceName** *(string) --*

        The fully qualified domain name for the service to match from the request.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **grpcRetryEvents** *(list) --*

        Specify at least one of the valid values.

        - *(string) --*

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
        510, and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --*

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --*

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef(
    _ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttp2Routeaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientCreateRouteResponseroutespechttp2RouteactionTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RouteactionTypeDef(
    _ClientCreateRouteResponseroutespechttp2RouteactionTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttp2Route` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef(
    _ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttp2Routematchheadersmatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --*

      The end of the range.

    - **start** *(integer) --*

      The start of the range.
    """


_ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef(
    _ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttp2Routematchheaders` `match`

    The ``HeaderMatchMethod`` object.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --*

        The end of the range.

      - **start** *(integer) --*

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef(
    _ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttp2Routematch` `headers`

    An object that represents the HTTP header in the request.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value
      is ``False`` .

    - **match** *(dict) --*

      The ``HeaderMatchMethod`` object.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --*

          The end of the range.

        - **start** *(integer) --*

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --*

      A name for the HTTP header in the client request that will be matched on.
    """


_ClientCreateRouteResponseroutespechttp2RoutematchTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RoutematchTypeDef",
    {
        "headers": List[
            ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef
        ],
        "method": str,
        "prefix": str,
        "scheme": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RoutematchTypeDef(
    _ClientCreateRouteResponseroutespechttp2RoutematchTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttp2Route` `match`

    An object that represents the criteria for determining a request match.

    - **headers** *(list) --*

      An object that represents the client request headers to match on.

      - *(dict) --*

        An object that represents the HTTP header in the request.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value
          is ``False`` .

        - **match** *(dict) --*

          The ``HeaderMatchMethod`` object.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --*

              The end of the range.

            - **start** *(integer) --*

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --*

          A name for the HTTP header in the client request that will be matched on.

    - **method** *(string) --*

      The client request method to match on. Specify only one.

    - **prefix** *(string) --*

      Specifies the path to match requests with. This parameter must always start with
      ``/`` , which by itself matches all requests to the virtual service name. You can
      also match for path-based routing of requests. For example, if your virtual service
      name is ``my-service.local`` and you want the route to match requests to
      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

    - **scheme** *(string) --*

      The client request scheme to match on. Specify only one.
    """


_ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef(
    _ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttp2RouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef(
    _ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttp2Route` `retryPolicy`

    An object that represents a retry policy.

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
      510, and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --*

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --*

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_ClientCreateRouteResponseroutespechttp2RouteTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RouteTypeDef",
    {
        "action": ClientCreateRouteResponseroutespechttp2RouteactionTypeDef,
        "match": ClientCreateRouteResponseroutespechttp2RoutematchTypeDef,
        "retryPolicy": ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RouteTypeDef(
    _ClientCreateRouteResponseroutespechttp2RouteTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespec` `http2Route`

    An object that represents the specification of an HTTP2 route.

    - **action** *(dict) --*

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.

    - **match** *(dict) --*

      An object that represents the criteria for determining a request match.

      - **headers** *(list) --*

        An object that represents the client request headers to match on.

        - *(dict) --*

          An object that represents the HTTP header in the request.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value
            is ``False`` .

          - **match** *(dict) --*

            The ``HeaderMatchMethod`` object.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --*

                The end of the range.

              - **start** *(integer) --*

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --*

            A name for the HTTP header in the client request that will be matched on.

      - **method** *(string) --*

        The client request method to match on. Specify only one.

      - **prefix** *(string) --*

        Specifies the path to match requests with. This parameter must always start with
        ``/`` , which by itself matches all requests to the virtual service name. You can
        also match for path-based routing of requests. For example, if your virtual service
        name is ``my-service.local`` and you want the route to match requests to
        ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

      - **scheme** *(string) --*

        The client request scheme to match on. Specify only one.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
        510, and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --*

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --*

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef(
    _ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttpRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientCreateRouteResponseroutespechttpRouteactionTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttpRouteactionTypeDef(
    _ClientCreateRouteResponseroutespechttpRouteactionTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttpRoute` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef(
    _ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttpRoutematchheadersmatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --*

      The end of the range.

    - **start** *(integer) --*

      The start of the range.
    """


_ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef(
    _ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttpRoutematchheaders` `match`

    The ``HeaderMatchMethod`` object.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --*

        The end of the range.

      - **start** *(integer) --*

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef(
    _ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttpRoutematch` `headers`

    An object that represents the HTTP header in the request.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value
      is ``False`` .

    - **match** *(dict) --*

      The ``HeaderMatchMethod`` object.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --*

          The end of the range.

        - **start** *(integer) --*

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --*

      A name for the HTTP header in the client request that will be matched on.
    """


_ClientCreateRouteResponseroutespechttpRoutematchTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRoutematchTypeDef",
    {
        "headers": List[ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef],
        "method": str,
        "prefix": str,
        "scheme": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttpRoutematchTypeDef(
    _ClientCreateRouteResponseroutespechttpRoutematchTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttpRoute` `match`

    An object that represents the criteria for determining a request match.

    - **headers** *(list) --*

      An object that represents the client request headers to match on.

      - *(dict) --*

        An object that represents the HTTP header in the request.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value
          is ``False`` .

        - **match** *(dict) --*

          The ``HeaderMatchMethod`` object.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --*

              The end of the range.

            - **start** *(integer) --*

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --*

          A name for the HTTP header in the client request that will be matched on.

    - **method** *(string) --*

      The client request method to match on. Specify only one.

    - **prefix** *(string) --*

      Specifies the path to match requests with. This parameter must always start with
      ``/`` , which by itself matches all requests to the virtual service name. You can
      also match for path-based routing of requests. For example, if your virtual service
      name is ``my-service.local`` and you want the route to match requests to
      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

    - **scheme** *(string) --*

      The client request scheme to match on. Specify only one.
    """


_ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttpRouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef(
    _ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespechttpRoute` `retryPolicy`

    An object that represents a retry policy.

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
      510, and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --*

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --*

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_ClientCreateRouteResponseroutespechttpRouteTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRouteTypeDef",
    {
        "action": ClientCreateRouteResponseroutespechttpRouteactionTypeDef,
        "match": ClientCreateRouteResponseroutespechttpRoutematchTypeDef,
        "retryPolicy": ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttpRouteTypeDef(
    _ClientCreateRouteResponseroutespechttpRouteTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespec` `httpRoute`

    An object that represents the specification of an HTTP route.

    - **action** *(dict) --*

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.

    - **match** *(dict) --*

      An object that represents the criteria for determining a request match.

      - **headers** *(list) --*

        An object that represents the client request headers to match on.

        - *(dict) --*

          An object that represents the HTTP header in the request.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value
            is ``False`` .

          - **match** *(dict) --*

            The ``HeaderMatchMethod`` object.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --*

                The end of the range.

              - **start** *(integer) --*

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --*

            A name for the HTTP header in the client request that will be matched on.

      - **method** *(string) --*

        The client request method to match on. Specify only one.

      - **prefix** *(string) --*

        Specifies the path to match requests with. This parameter must always start with
        ``/`` , which by itself matches all requests to the virtual service name. You can
        also match for path-based routing of requests. For example, if your virtual service
        name is ``my-service.local`` and you want the route to match requests to
        ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

      - **scheme** *(string) --*

        The client request scheme to match on. Specify only one.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
        510, and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --*

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --*

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef(
    _ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespectcpRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientCreateRouteResponseroutespectcpRouteactionTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientCreateRouteResponseroutespectcpRouteactionTypeDef(
    _ClientCreateRouteResponseroutespectcpRouteactionTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespectcpRoute` `action`

    The action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientCreateRouteResponseroutespectcpRouteTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespectcpRouteTypeDef",
    {"action": ClientCreateRouteResponseroutespectcpRouteactionTypeDef},
    total=False,
)


class ClientCreateRouteResponseroutespectcpRouteTypeDef(
    _ClientCreateRouteResponseroutespectcpRouteTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroutespec` `tcpRoute`

    An object that represents the specification of a TCP route.

    - **action** *(dict) --*

      The action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.
    """


_ClientCreateRouteResponseroutespecTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecTypeDef",
    {
        "grpcRoute": ClientCreateRouteResponseroutespecgrpcRouteTypeDef,
        "http2Route": ClientCreateRouteResponseroutespechttp2RouteTypeDef,
        "httpRoute": ClientCreateRouteResponseroutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientCreateRouteResponseroutespectcpRouteTypeDef,
    },
    total=False,
)


class ClientCreateRouteResponseroutespecTypeDef(
    _ClientCreateRouteResponseroutespecTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroute` `spec`

    The specifications of the route.

    - **grpcRoute** *(dict) --*

      An object that represents the specification of a GRPC route.

      - **action** *(dict) --*

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.

      - **match** *(dict) --*

        An object that represents the criteria for determining a request match.

        - **metadata** *(list) --*

          An object that represents the data to match from the request.

          - *(dict) --*

            An object that represents the match metadata for the route.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value
              is ``False`` .

            - **match** *(dict) --*

              An object that represents the data to match from the request.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --*

                  The end of the range.

                - **start** *(integer) --*

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --*

              The name of the route.

        - **methodName** *(string) --*

          The method name to match from the request. If you specify a name, you must also
          specify a ``serviceName`` .

        - **serviceName** *(string) --*

          The fully qualified domain name for the service to match from the request.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **grpcRetryEvents** *(list) --*

          Specify at least one of the valid values.

          - *(string) --*

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
          510, and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --*

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --*

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **http2Route** *(dict) --*

      An object that represents the specification of an HTTP2 route.

      - **action** *(dict) --*

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.

      - **match** *(dict) --*

        An object that represents the criteria for determining a request match.

        - **headers** *(list) --*

          An object that represents the client request headers to match on.

          - *(dict) --*

            An object that represents the HTTP header in the request.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value
              is ``False`` .

            - **match** *(dict) --*

              The ``HeaderMatchMethod`` object.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --*

                  The end of the range.

                - **start** *(integer) --*

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --*

              A name for the HTTP header in the client request that will be matched on.

        - **method** *(string) --*

          The client request method to match on. Specify only one.

        - **prefix** *(string) --*

          Specifies the path to match requests with. This parameter must always start with
          ``/`` , which by itself matches all requests to the virtual service name. You can
          also match for path-based routing of requests. For example, if your virtual service
          name is ``my-service.local`` and you want the route to match requests to
          ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

        - **scheme** *(string) --*

          The client request scheme to match on. Specify only one.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
          510, and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --*

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --*

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **httpRoute** *(dict) --*

      An object that represents the specification of an HTTP route.

      - **action** *(dict) --*

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.

      - **match** *(dict) --*

        An object that represents the criteria for determining a request match.

        - **headers** *(list) --*

          An object that represents the client request headers to match on.

          - *(dict) --*

            An object that represents the HTTP header in the request.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value
              is ``False`` .

            - **match** *(dict) --*

              The ``HeaderMatchMethod`` object.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --*

                  The end of the range.

                - **start** *(integer) --*

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --*

              A name for the HTTP header in the client request that will be matched on.

        - **method** *(string) --*

          The client request method to match on. Specify only one.

        - **prefix** *(string) --*

          Specifies the path to match requests with. This parameter must always start with
          ``/`` , which by itself matches all requests to the virtual service name. You can
          also match for path-based routing of requests. For example, if your virtual service
          name is ``my-service.local`` and you want the route to match requests to
          ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

        - **scheme** *(string) --*

          The client request scheme to match on. Specify only one.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
          510, and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --*

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --*

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **priority** *(integer) --*

      The priority for the route. Routes are matched based on the specified value, where 0 is
      the highest priority.

    - **tcpRoute** *(dict) --*

      An object that represents the specification of a TCP route.

      - **action** *(dict) --*

        The action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.
    """


_ClientCreateRouteResponseroutestatusTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutestatusTypeDef", {"status": str}, total=False
)


class ClientCreateRouteResponseroutestatusTypeDef(
    _ClientCreateRouteResponseroutestatusTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseroute` `status`

    The status of the route.

    - **status** *(string) --*

      The current status for the route.
    """


_ClientCreateRouteResponserouteTypeDef = TypedDict(
    "_ClientCreateRouteResponserouteTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateRouteResponseroutemetadataTypeDef,
        "routeName": str,
        "spec": ClientCreateRouteResponseroutespecTypeDef,
        "status": ClientCreateRouteResponseroutestatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientCreateRouteResponserouteTypeDef(_ClientCreateRouteResponserouteTypeDef):
    """
    Type definition for `ClientCreateRouteResponse` `route`

    The full description of your mesh following the create call.

    - **meshName** *(string) --*

      The name of the service mesh that the route resides in.

    - **metadata** *(dict) --*

      The associated metadata for the route.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **routeName** *(string) --*

      The name of the route.

    - **spec** *(dict) --*

      The specifications of the route.

      - **grpcRoute** *(dict) --*

        An object that represents the specification of a GRPC route.

        - **action** *(dict) --*

          An object that represents the action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

        - **match** *(dict) --*

          An object that represents the criteria for determining a request match.

          - **metadata** *(list) --*

            An object that represents the data to match from the request.

            - *(dict) --*

              An object that represents the match metadata for the route.

              - **invert** *(boolean) --*

                Specify ``True`` to match anything except the match criteria. The default value
                is ``False`` .

              - **match** *(dict) --*

                An object that represents the data to match from the request.

                - **exact** *(string) --*

                  The value sent by the client must match the specified value exactly.

                - **prefix** *(string) --*

                  The value sent by the client must begin with the specified characters.

                - **range** *(dict) --*

                  An object that represents the range of values to match on.

                  - **end** *(integer) --*

                    The end of the range.

                  - **start** *(integer) --*

                    The start of the range.

                - **regex** *(string) --*

                  The value sent by the client must include the specified characters.

                - **suffix** *(string) --*

                  The value sent by the client must end with the specified characters.

              - **name** *(string) --*

                The name of the route.

          - **methodName** *(string) --*

            The method name to match from the request. If you specify a name, you must also
            specify a ``serviceName`` .

          - **serviceName** *(string) --*

            The fully qualified domain name for the service to match from the request.

        - **retryPolicy** *(dict) --*

          An object that represents a retry policy.

          - **grpcRetryEvents** *(list) --*

            Specify at least one of the valid values.

            - *(string) --*

          - **httpRetryEvents** *(list) --*

            Specify at least one of the following values.

            * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
            510, and 511

            * **gateway-error** – HTTP status codes 502, 503, and 504

            * **client-error** – HTTP status code 409

            * **stream-error** – Retry on refused stream

            - *(string) --*

          - **maxRetries** *(integer) --*

            The maximum number of retry attempts.

          - **perRetryTimeout** *(dict) --*

            An object that represents a duration of time.

            - **unit** *(string) --*

              A unit of time.

            - **value** *(integer) --*

              A number of time units.

          - **tcpRetryEvents** *(list) --*

            Specify a valid value.

            - *(string) --*

      - **http2Route** *(dict) --*

        An object that represents the specification of an HTTP2 route.

        - **action** *(dict) --*

          An object that represents the action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

        - **match** *(dict) --*

          An object that represents the criteria for determining a request match.

          - **headers** *(list) --*

            An object that represents the client request headers to match on.

            - *(dict) --*

              An object that represents the HTTP header in the request.

              - **invert** *(boolean) --*

                Specify ``True`` to match anything except the match criteria. The default value
                is ``False`` .

              - **match** *(dict) --*

                The ``HeaderMatchMethod`` object.

                - **exact** *(string) --*

                  The value sent by the client must match the specified value exactly.

                - **prefix** *(string) --*

                  The value sent by the client must begin with the specified characters.

                - **range** *(dict) --*

                  An object that represents the range of values to match on.

                  - **end** *(integer) --*

                    The end of the range.

                  - **start** *(integer) --*

                    The start of the range.

                - **regex** *(string) --*

                  The value sent by the client must include the specified characters.

                - **suffix** *(string) --*

                  The value sent by the client must end with the specified characters.

              - **name** *(string) --*

                A name for the HTTP header in the client request that will be matched on.

          - **method** *(string) --*

            The client request method to match on. Specify only one.

          - **prefix** *(string) --*

            Specifies the path to match requests with. This parameter must always start with
            ``/`` , which by itself matches all requests to the virtual service name. You can
            also match for path-based routing of requests. For example, if your virtual service
            name is ``my-service.local`` and you want the route to match requests to
            ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

          - **scheme** *(string) --*

            The client request scheme to match on. Specify only one.

        - **retryPolicy** *(dict) --*

          An object that represents a retry policy.

          - **httpRetryEvents** *(list) --*

            Specify at least one of the following values.

            * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
            510, and 511

            * **gateway-error** – HTTP status codes 502, 503, and 504

            * **client-error** – HTTP status code 409

            * **stream-error** – Retry on refused stream

            - *(string) --*

          - **maxRetries** *(integer) --*

            The maximum number of retry attempts.

          - **perRetryTimeout** *(dict) --*

            An object that represents a duration of time.

            - **unit** *(string) --*

              A unit of time.

            - **value** *(integer) --*

              A number of time units.

          - **tcpRetryEvents** *(list) --*

            Specify a valid value.

            - *(string) --*

      - **httpRoute** *(dict) --*

        An object that represents the specification of an HTTP route.

        - **action** *(dict) --*

          An object that represents the action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

        - **match** *(dict) --*

          An object that represents the criteria for determining a request match.

          - **headers** *(list) --*

            An object that represents the client request headers to match on.

            - *(dict) --*

              An object that represents the HTTP header in the request.

              - **invert** *(boolean) --*

                Specify ``True`` to match anything except the match criteria. The default value
                is ``False`` .

              - **match** *(dict) --*

                The ``HeaderMatchMethod`` object.

                - **exact** *(string) --*

                  The value sent by the client must match the specified value exactly.

                - **prefix** *(string) --*

                  The value sent by the client must begin with the specified characters.

                - **range** *(dict) --*

                  An object that represents the range of values to match on.

                  - **end** *(integer) --*

                    The end of the range.

                  - **start** *(integer) --*

                    The start of the range.

                - **regex** *(string) --*

                  The value sent by the client must include the specified characters.

                - **suffix** *(string) --*

                  The value sent by the client must end with the specified characters.

              - **name** *(string) --*

                A name for the HTTP header in the client request that will be matched on.

          - **method** *(string) --*

            The client request method to match on. Specify only one.

          - **prefix** *(string) --*

            Specifies the path to match requests with. This parameter must always start with
            ``/`` , which by itself matches all requests to the virtual service name. You can
            also match for path-based routing of requests. For example, if your virtual service
            name is ``my-service.local`` and you want the route to match requests to
            ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

          - **scheme** *(string) --*

            The client request scheme to match on. Specify only one.

        - **retryPolicy** *(dict) --*

          An object that represents a retry policy.

          - **httpRetryEvents** *(list) --*

            Specify at least one of the following values.

            * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
            510, and 511

            * **gateway-error** – HTTP status codes 502, 503, and 504

            * **client-error** – HTTP status code 409

            * **stream-error** – Retry on refused stream

            - *(string) --*

          - **maxRetries** *(integer) --*

            The maximum number of retry attempts.

          - **perRetryTimeout** *(dict) --*

            An object that represents a duration of time.

            - **unit** *(string) --*

              A unit of time.

            - **value** *(integer) --*

              A number of time units.

          - **tcpRetryEvents** *(list) --*

            Specify a valid value.

            - *(string) --*

      - **priority** *(integer) --*

        The priority for the route. Routes are matched based on the specified value, where 0 is
        the highest priority.

      - **tcpRoute** *(dict) --*

        An object that represents the specification of a TCP route.

        - **action** *(dict) --*

          The action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

    - **status** *(dict) --*

      The status of the route.

      - **status** *(string) --*

        The current status for the route.

    - **virtualRouterName** *(string) --*

      The virtual router that the route is associated with.
    """


_ClientCreateRouteResponseTypeDef = TypedDict(
    "_ClientCreateRouteResponseTypeDef",
    {"route": ClientCreateRouteResponserouteTypeDef},
    total=False,
)


class ClientCreateRouteResponseTypeDef(_ClientCreateRouteResponseTypeDef):
    """
    Type definition for `ClientCreateRoute` `Response`

    - **route** *(dict) --*

      The full description of your mesh following the create call.

      - **meshName** *(string) --*

        The name of the service mesh that the route resides in.

      - **metadata** *(dict) --*

        The associated metadata for the route.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **routeName** *(string) --*

        The name of the route.

      - **spec** *(dict) --*

        The specifications of the route.

        - **grpcRoute** *(dict) --*

          An object that represents the specification of a GRPC route.

          - **action** *(dict) --*

            An object that represents the action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

          - **match** *(dict) --*

            An object that represents the criteria for determining a request match.

            - **metadata** *(list) --*

              An object that represents the data to match from the request.

              - *(dict) --*

                An object that represents the match metadata for the route.

                - **invert** *(boolean) --*

                  Specify ``True`` to match anything except the match criteria. The default value
                  is ``False`` .

                - **match** *(dict) --*

                  An object that represents the data to match from the request.

                  - **exact** *(string) --*

                    The value sent by the client must match the specified value exactly.

                  - **prefix** *(string) --*

                    The value sent by the client must begin with the specified characters.

                  - **range** *(dict) --*

                    An object that represents the range of values to match on.

                    - **end** *(integer) --*

                      The end of the range.

                    - **start** *(integer) --*

                      The start of the range.

                  - **regex** *(string) --*

                    The value sent by the client must include the specified characters.

                  - **suffix** *(string) --*

                    The value sent by the client must end with the specified characters.

                - **name** *(string) --*

                  The name of the route.

            - **methodName** *(string) --*

              The method name to match from the request. If you specify a name, you must also
              specify a ``serviceName`` .

            - **serviceName** *(string) --*

              The fully qualified domain name for the service to match from the request.

          - **retryPolicy** *(dict) --*

            An object that represents a retry policy.

            - **grpcRetryEvents** *(list) --*

              Specify at least one of the valid values.

              - *(string) --*

            - **httpRetryEvents** *(list) --*

              Specify at least one of the following values.

              * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
              510, and 511

              * **gateway-error** – HTTP status codes 502, 503, and 504

              * **client-error** – HTTP status code 409

              * **stream-error** – Retry on refused stream

              - *(string) --*

            - **maxRetries** *(integer) --*

              The maximum number of retry attempts.

            - **perRetryTimeout** *(dict) --*

              An object that represents a duration of time.

              - **unit** *(string) --*

                A unit of time.

              - **value** *(integer) --*

                A number of time units.

            - **tcpRetryEvents** *(list) --*

              Specify a valid value.

              - *(string) --*

        - **http2Route** *(dict) --*

          An object that represents the specification of an HTTP2 route.

          - **action** *(dict) --*

            An object that represents the action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

          - **match** *(dict) --*

            An object that represents the criteria for determining a request match.

            - **headers** *(list) --*

              An object that represents the client request headers to match on.

              - *(dict) --*

                An object that represents the HTTP header in the request.

                - **invert** *(boolean) --*

                  Specify ``True`` to match anything except the match criteria. The default value
                  is ``False`` .

                - **match** *(dict) --*

                  The ``HeaderMatchMethod`` object.

                  - **exact** *(string) --*

                    The value sent by the client must match the specified value exactly.

                  - **prefix** *(string) --*

                    The value sent by the client must begin with the specified characters.

                  - **range** *(dict) --*

                    An object that represents the range of values to match on.

                    - **end** *(integer) --*

                      The end of the range.

                    - **start** *(integer) --*

                      The start of the range.

                  - **regex** *(string) --*

                    The value sent by the client must include the specified characters.

                  - **suffix** *(string) --*

                    The value sent by the client must end with the specified characters.

                - **name** *(string) --*

                  A name for the HTTP header in the client request that will be matched on.

            - **method** *(string) --*

              The client request method to match on. Specify only one.

            - **prefix** *(string) --*

              Specifies the path to match requests with. This parameter must always start with
              ``/`` , which by itself matches all requests to the virtual service name. You can
              also match for path-based routing of requests. For example, if your virtual service
              name is ``my-service.local`` and you want the route to match requests to
              ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

            - **scheme** *(string) --*

              The client request scheme to match on. Specify only one.

          - **retryPolicy** *(dict) --*

            An object that represents a retry policy.

            - **httpRetryEvents** *(list) --*

              Specify at least one of the following values.

              * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
              510, and 511

              * **gateway-error** – HTTP status codes 502, 503, and 504

              * **client-error** – HTTP status code 409

              * **stream-error** – Retry on refused stream

              - *(string) --*

            - **maxRetries** *(integer) --*

              The maximum number of retry attempts.

            - **perRetryTimeout** *(dict) --*

              An object that represents a duration of time.

              - **unit** *(string) --*

                A unit of time.

              - **value** *(integer) --*

                A number of time units.

            - **tcpRetryEvents** *(list) --*

              Specify a valid value.

              - *(string) --*

        - **httpRoute** *(dict) --*

          An object that represents the specification of an HTTP route.

          - **action** *(dict) --*

            An object that represents the action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

          - **match** *(dict) --*

            An object that represents the criteria for determining a request match.

            - **headers** *(list) --*

              An object that represents the client request headers to match on.

              - *(dict) --*

                An object that represents the HTTP header in the request.

                - **invert** *(boolean) --*

                  Specify ``True`` to match anything except the match criteria. The default value
                  is ``False`` .

                - **match** *(dict) --*

                  The ``HeaderMatchMethod`` object.

                  - **exact** *(string) --*

                    The value sent by the client must match the specified value exactly.

                  - **prefix** *(string) --*

                    The value sent by the client must begin with the specified characters.

                  - **range** *(dict) --*

                    An object that represents the range of values to match on.

                    - **end** *(integer) --*

                      The end of the range.

                    - **start** *(integer) --*

                      The start of the range.

                  - **regex** *(string) --*

                    The value sent by the client must include the specified characters.

                  - **suffix** *(string) --*

                    The value sent by the client must end with the specified characters.

                - **name** *(string) --*

                  A name for the HTTP header in the client request that will be matched on.

            - **method** *(string) --*

              The client request method to match on. Specify only one.

            - **prefix** *(string) --*

              Specifies the path to match requests with. This parameter must always start with
              ``/`` , which by itself matches all requests to the virtual service name. You can
              also match for path-based routing of requests. For example, if your virtual service
              name is ``my-service.local`` and you want the route to match requests to
              ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

            - **scheme** *(string) --*

              The client request scheme to match on. Specify only one.

          - **retryPolicy** *(dict) --*

            An object that represents a retry policy.

            - **httpRetryEvents** *(list) --*

              Specify at least one of the following values.

              * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
              510, and 511

              * **gateway-error** – HTTP status codes 502, 503, and 504

              * **client-error** – HTTP status code 409

              * **stream-error** – Retry on refused stream

              - *(string) --*

            - **maxRetries** *(integer) --*

              The maximum number of retry attempts.

            - **perRetryTimeout** *(dict) --*

              An object that represents a duration of time.

              - **unit** *(string) --*

                A unit of time.

              - **value** *(integer) --*

                A number of time units.

            - **tcpRetryEvents** *(list) --*

              Specify a valid value.

              - *(string) --*

        - **priority** *(integer) --*

          The priority for the route. Routes are matched based on the specified value, where 0 is
          the highest priority.

        - **tcpRoute** *(dict) --*

          An object that represents the specification of a TCP route.

          - **action** *(dict) --*

            The action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

      - **status** *(dict) --*

        The status of the route.

        - **status** *(string) --*

          The current status for the route.

      - **virtualRouterName** *(string) --*

        The virtual router that the route is associated with.
    """


_ClientCreateRoutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRoutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
)


class ClientCreateRoutespecgrpcRouteactionweightedTargetsTypeDef(
    _ClientCreateRoutespecgrpcRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientCreateRoutespecgrpcRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed across
    targets according to their relative weight. For example, a weighted target with a
    relative weight of 50 receives five times as much traffic as one with a relative weight
    of 10. The total weight for all targets combined must be less than or equal to 100.

    - **virtualNode** *(string) --* **[REQUIRED]**

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --* **[REQUIRED]**

      The relative weight of the weighted target.
    """


_ClientCreateRoutespecgrpcRouteactionTypeDef = TypedDict(
    "_ClientCreateRoutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRoutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
)


class ClientCreateRoutespecgrpcRouteactionTypeDef(
    _ClientCreateRoutespecgrpcRouteactionTypeDef
):
    """
    Type definition for `ClientCreateRoutespecgrpcRoute` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --* **[REQUIRED]**

      An object that represents the targets that traffic is routed to when a request matches the
      route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed across
        targets according to their relative weight. For example, a weighted target with a
        relative weight of 50 receives five times as much traffic as one with a relative weight
        of 10. The total weight for all targets combined must be less than or equal to 100.

        - **virtualNode** *(string) --* **[REQUIRED]**

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --* **[REQUIRED]**

          The relative weight of the weighted target.
    """


_ClientCreateRoutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "_ClientCreateRoutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
)


class ClientCreateRoutespecgrpcRoutematchmetadatamatchrangeTypeDef(
    _ClientCreateRoutespecgrpcRoutematchmetadatamatchrangeTypeDef
):
    """
    Type definition for `ClientCreateRoutespecgrpcRoutematchmetadatamatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --* **[REQUIRED]**

      The end of the range.

    - **start** *(integer) --* **[REQUIRED]**

      The start of the range.
    """


_ClientCreateRoutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "_ClientCreateRoutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRoutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientCreateRoutespecgrpcRoutematchmetadatamatchTypeDef(
    _ClientCreateRoutespecgrpcRoutematchmetadatamatchTypeDef
):
    """
    Type definition for `ClientCreateRoutespecgrpcRoutematchmetadata` `match`

    An object that represents the data to match from the request.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --* **[REQUIRED]**

        The end of the range.

      - **start** *(integer) --* **[REQUIRED]**

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_RequiredClientCreateRoutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_RequiredClientCreateRoutespecgrpcRoutematchmetadataTypeDef", {"name": str}
)
_OptionalClientCreateRoutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_OptionalClientCreateRoutespecgrpcRoutematchmetadataTypeDef",
    {"invert": bool, "match": ClientCreateRoutespecgrpcRoutematchmetadatamatchTypeDef},
    total=False,
)


class ClientCreateRoutespecgrpcRoutematchmetadataTypeDef(
    _RequiredClientCreateRoutespecgrpcRoutematchmetadataTypeDef,
    _OptionalClientCreateRoutespecgrpcRoutematchmetadataTypeDef,
):
    """
    Type definition for `ClientCreateRoutespecgrpcRoutematch` `metadata`

    An object that represents the match metadata for the route.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value is
      ``False`` .

    - **match** *(dict) --*

      An object that represents the data to match from the request.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --* **[REQUIRED]**

          The end of the range.

        - **start** *(integer) --* **[REQUIRED]**

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --* **[REQUIRED]**

      The name of the route.
    """


_ClientCreateRoutespecgrpcRoutematchTypeDef = TypedDict(
    "_ClientCreateRoutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientCreateRoutespecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientCreateRoutespecgrpcRoutematchTypeDef(
    _ClientCreateRoutespecgrpcRoutematchTypeDef
):
    """
    Type definition for `ClientCreateRoutespecgrpcRoute` `match`

    An object that represents the criteria for determining a request match.

    - **metadata** *(list) --*

      An object that represents the data to match from the request.

      - *(dict) --*

        An object that represents the match metadata for the route.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value is
          ``False`` .

        - **match** *(dict) --*

          An object that represents the data to match from the request.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --* **[REQUIRED]**

              The end of the range.

            - **start** *(integer) --* **[REQUIRED]**

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --* **[REQUIRED]**

          The name of the route.

    - **methodName** *(string) --*

      The method name to match from the request. If you specify a name, you must also specify a
      ``serviceName`` .

    - **serviceName** *(string) --*

      The fully qualified domain name for the service to match from the request.
    """


_ClientCreateRoutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientCreateRoutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientCreateRoutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientCreateRoutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientCreateRoutespecgrpcRouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_RequiredClientCreateRoutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_RequiredClientCreateRoutespecgrpcRouteretryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRoutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
    },
)
_OptionalClientCreateRoutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_OptionalClientCreateRoutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[str],
        "httpRetryEvents": List[str],
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientCreateRoutespecgrpcRouteretryPolicyTypeDef(
    _RequiredClientCreateRoutespecgrpcRouteretryPolicyTypeDef,
    _OptionalClientCreateRoutespecgrpcRouteretryPolicyTypeDef,
):
    """
    Type definition for `ClientCreateRoutespecgrpcRoute` `retryPolicy`

    An object that represents a retry policy.

    - **grpcRetryEvents** *(list) --*

      Specify at least one of the valid values.

      - *(string) --*

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
      and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --* **[REQUIRED]**

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --* **[REQUIRED]**

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_RequiredClientCreateRoutespecgrpcRouteTypeDef = TypedDict(
    "_RequiredClientCreateRoutespecgrpcRouteTypeDef",
    {
        "action": ClientCreateRoutespecgrpcRouteactionTypeDef,
        "match": ClientCreateRoutespecgrpcRoutematchTypeDef,
    },
)
_OptionalClientCreateRoutespecgrpcRouteTypeDef = TypedDict(
    "_OptionalClientCreateRoutespecgrpcRouteTypeDef",
    {"retryPolicy": ClientCreateRoutespecgrpcRouteretryPolicyTypeDef},
    total=False,
)


class ClientCreateRoutespecgrpcRouteTypeDef(
    _RequiredClientCreateRoutespecgrpcRouteTypeDef,
    _OptionalClientCreateRoutespecgrpcRouteTypeDef,
):
    """
    Type definition for `ClientCreateRoutespec` `grpcRoute`

    An object that represents the specification of a GRPC route.

    - **action** *(dict) --* **[REQUIRED]**

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --* **[REQUIRED]**

        An object that represents the targets that traffic is routed to when a request matches the
        route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed across
          targets according to their relative weight. For example, a weighted target with a
          relative weight of 50 receives five times as much traffic as one with a relative weight
          of 10. The total weight for all targets combined must be less than or equal to 100.

          - **virtualNode** *(string) --* **[REQUIRED]**

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --* **[REQUIRED]**

            The relative weight of the weighted target.

    - **match** *(dict) --* **[REQUIRED]**

      An object that represents the criteria for determining a request match.

      - **metadata** *(list) --*

        An object that represents the data to match from the request.

        - *(dict) --*

          An object that represents the match metadata for the route.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value is
            ``False`` .

          - **match** *(dict) --*

            An object that represents the data to match from the request.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --* **[REQUIRED]**

                The end of the range.

              - **start** *(integer) --* **[REQUIRED]**

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --* **[REQUIRED]**

            The name of the route.

      - **methodName** *(string) --*

        The method name to match from the request. If you specify a name, you must also specify a
        ``serviceName`` .

      - **serviceName** *(string) --*

        The fully qualified domain name for the service to match from the request.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **grpcRetryEvents** *(list) --*

        Specify at least one of the valid values.

        - *(string) --*

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
        and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --* **[REQUIRED]**

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --* **[REQUIRED]**

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientCreateRoutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRoutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
)


class ClientCreateRoutespechttp2RouteactionweightedTargetsTypeDef(
    _ClientCreateRoutespechttp2RouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientCreateRoutespechttp2Routeaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed across
    targets according to their relative weight. For example, a weighted target with a
    relative weight of 50 receives five times as much traffic as one with a relative weight
    of 10. The total weight for all targets combined must be less than or equal to 100.

    - **virtualNode** *(string) --* **[REQUIRED]**

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --* **[REQUIRED]**

      The relative weight of the weighted target.
    """


_ClientCreateRoutespechttp2RouteactionTypeDef = TypedDict(
    "_ClientCreateRoutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRoutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
)


class ClientCreateRoutespechttp2RouteactionTypeDef(
    _ClientCreateRoutespechttp2RouteactionTypeDef
):
    """
    Type definition for `ClientCreateRoutespechttp2Route` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --* **[REQUIRED]**

      An object that represents the targets that traffic is routed to when a request matches the
      route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed across
        targets according to their relative weight. For example, a weighted target with a
        relative weight of 50 receives five times as much traffic as one with a relative weight
        of 10. The total weight for all targets combined must be less than or equal to 100.

        - **virtualNode** *(string) --* **[REQUIRED]**

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --* **[REQUIRED]**

          The relative weight of the weighted target.
    """


_ClientCreateRoutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientCreateRoutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
)


class ClientCreateRoutespechttp2RoutematchheadersmatchrangeTypeDef(
    _ClientCreateRoutespechttp2RoutematchheadersmatchrangeTypeDef
):
    """
    Type definition for `ClientCreateRoutespechttp2Routematchheadersmatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --* **[REQUIRED]**

      The end of the range.

    - **start** *(integer) --* **[REQUIRED]**

      The start of the range.
    """


_ClientCreateRoutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "_ClientCreateRoutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRoutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientCreateRoutespechttp2RoutematchheadersmatchTypeDef(
    _ClientCreateRoutespechttp2RoutematchheadersmatchTypeDef
):
    """
    Type definition for `ClientCreateRoutespechttp2Routematchheaders` `match`

    The ``HeaderMatchMethod`` object.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --* **[REQUIRED]**

        The end of the range.

      - **start** *(integer) --* **[REQUIRED]**

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_RequiredClientCreateRoutespechttp2RoutematchheadersTypeDef = TypedDict(
    "_RequiredClientCreateRoutespechttp2RoutematchheadersTypeDef", {"name": str}
)
_OptionalClientCreateRoutespechttp2RoutematchheadersTypeDef = TypedDict(
    "_OptionalClientCreateRoutespechttp2RoutematchheadersTypeDef",
    {"invert": bool, "match": ClientCreateRoutespechttp2RoutematchheadersmatchTypeDef},
    total=False,
)


class ClientCreateRoutespechttp2RoutematchheadersTypeDef(
    _RequiredClientCreateRoutespechttp2RoutematchheadersTypeDef,
    _OptionalClientCreateRoutespechttp2RoutematchheadersTypeDef,
):
    """
    Type definition for `ClientCreateRoutespechttp2Routematch` `headers`

    An object that represents the HTTP header in the request.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value is
      ``False`` .

    - **match** *(dict) --*

      The ``HeaderMatchMethod`` object.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --* **[REQUIRED]**

          The end of the range.

        - **start** *(integer) --* **[REQUIRED]**

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --* **[REQUIRED]**

      A name for the HTTP header in the client request that will be matched on.
    """


_RequiredClientCreateRoutespechttp2RoutematchTypeDef = TypedDict(
    "_RequiredClientCreateRoutespechttp2RoutematchTypeDef", {"prefix": str}
)
_OptionalClientCreateRoutespechttp2RoutematchTypeDef = TypedDict(
    "_OptionalClientCreateRoutespechttp2RoutematchTypeDef",
    {
        "headers": List[ClientCreateRoutespechttp2RoutematchheadersTypeDef],
        "method": str,
        "scheme": str,
    },
    total=False,
)


class ClientCreateRoutespechttp2RoutematchTypeDef(
    _RequiredClientCreateRoutespechttp2RoutematchTypeDef,
    _OptionalClientCreateRoutespechttp2RoutematchTypeDef,
):
    """
    Type definition for `ClientCreateRoutespechttp2Route` `match`

    An object that represents the criteria for determining a request match.

    - **headers** *(list) --*

      An object that represents the client request headers to match on.

      - *(dict) --*

        An object that represents the HTTP header in the request.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value is
          ``False`` .

        - **match** *(dict) --*

          The ``HeaderMatchMethod`` object.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --* **[REQUIRED]**

              The end of the range.

            - **start** *(integer) --* **[REQUIRED]**

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --* **[REQUIRED]**

          A name for the HTTP header in the client request that will be matched on.

    - **method** *(string) --*

      The client request method to match on. Specify only one.

    - **prefix** *(string) --* **[REQUIRED]**

      Specifies the path to match requests with. This parameter must always start with ``/`` ,
      which by itself matches all requests to the virtual service name. You can also match for
      path-based routing of requests. For example, if your virtual service name is
      ``my-service.local`` and you want the route to match requests to
      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

    - **scheme** *(string) --*

      The client request scheme to match on. Specify only one.
    """


_ClientCreateRoutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientCreateRoutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientCreateRoutespechttp2RouteretryPolicyperRetryTimeoutTypeDef(
    _ClientCreateRoutespechttp2RouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientCreateRoutespechttp2RouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_RequiredClientCreateRoutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "_RequiredClientCreateRoutespechttp2RouteretryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRoutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
    },
)
_OptionalClientCreateRoutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "_OptionalClientCreateRoutespechttp2RouteretryPolicyTypeDef",
    {"httpRetryEvents": List[str], "tcpRetryEvents": List[str]},
    total=False,
)


class ClientCreateRoutespechttp2RouteretryPolicyTypeDef(
    _RequiredClientCreateRoutespechttp2RouteretryPolicyTypeDef,
    _OptionalClientCreateRoutespechttp2RouteretryPolicyTypeDef,
):
    """
    Type definition for `ClientCreateRoutespechttp2Route` `retryPolicy`

    An object that represents a retry policy.

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
      and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --* **[REQUIRED]**

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --* **[REQUIRED]**

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_RequiredClientCreateRoutespechttp2RouteTypeDef = TypedDict(
    "_RequiredClientCreateRoutespechttp2RouteTypeDef",
    {
        "action": ClientCreateRoutespechttp2RouteactionTypeDef,
        "match": ClientCreateRoutespechttp2RoutematchTypeDef,
    },
)
_OptionalClientCreateRoutespechttp2RouteTypeDef = TypedDict(
    "_OptionalClientCreateRoutespechttp2RouteTypeDef",
    {"retryPolicy": ClientCreateRoutespechttp2RouteretryPolicyTypeDef},
    total=False,
)


class ClientCreateRoutespechttp2RouteTypeDef(
    _RequiredClientCreateRoutespechttp2RouteTypeDef,
    _OptionalClientCreateRoutespechttp2RouteTypeDef,
):
    """
    Type definition for `ClientCreateRoutespec` `http2Route`

    An object that represents the specification of an HTTP2 route.

    - **action** *(dict) --* **[REQUIRED]**

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --* **[REQUIRED]**

        An object that represents the targets that traffic is routed to when a request matches the
        route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed across
          targets according to their relative weight. For example, a weighted target with a
          relative weight of 50 receives five times as much traffic as one with a relative weight
          of 10. The total weight for all targets combined must be less than or equal to 100.

          - **virtualNode** *(string) --* **[REQUIRED]**

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --* **[REQUIRED]**

            The relative weight of the weighted target.

    - **match** *(dict) --* **[REQUIRED]**

      An object that represents the criteria for determining a request match.

      - **headers** *(list) --*

        An object that represents the client request headers to match on.

        - *(dict) --*

          An object that represents the HTTP header in the request.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value is
            ``False`` .

          - **match** *(dict) --*

            The ``HeaderMatchMethod`` object.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --* **[REQUIRED]**

                The end of the range.

              - **start** *(integer) --* **[REQUIRED]**

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --* **[REQUIRED]**

            A name for the HTTP header in the client request that will be matched on.

      - **method** *(string) --*

        The client request method to match on. Specify only one.

      - **prefix** *(string) --* **[REQUIRED]**

        Specifies the path to match requests with. This parameter must always start with ``/`` ,
        which by itself matches all requests to the virtual service name. You can also match for
        path-based routing of requests. For example, if your virtual service name is
        ``my-service.local`` and you want the route to match requests to
        ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

      - **scheme** *(string) --*

        The client request scheme to match on. Specify only one.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
        and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --* **[REQUIRED]**

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --* **[REQUIRED]**

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientCreateRoutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRoutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
)


class ClientCreateRoutespechttpRouteactionweightedTargetsTypeDef(
    _ClientCreateRoutespechttpRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientCreateRoutespechttpRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed across
    targets according to their relative weight. For example, a weighted target with a
    relative weight of 50 receives five times as much traffic as one with a relative weight
    of 10. The total weight for all targets combined must be less than or equal to 100.

    - **virtualNode** *(string) --* **[REQUIRED]**

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --* **[REQUIRED]**

      The relative weight of the weighted target.
    """


_ClientCreateRoutespechttpRouteactionTypeDef = TypedDict(
    "_ClientCreateRoutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRoutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
)


class ClientCreateRoutespechttpRouteactionTypeDef(
    _ClientCreateRoutespechttpRouteactionTypeDef
):
    """
    Type definition for `ClientCreateRoutespechttpRoute` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --* **[REQUIRED]**

      An object that represents the targets that traffic is routed to when a request matches the
      route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed across
        targets according to their relative weight. For example, a weighted target with a
        relative weight of 50 receives five times as much traffic as one with a relative weight
        of 10. The total weight for all targets combined must be less than or equal to 100.

        - **virtualNode** *(string) --* **[REQUIRED]**

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --* **[REQUIRED]**

          The relative weight of the weighted target.
    """


_ClientCreateRoutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientCreateRoutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
)


class ClientCreateRoutespechttpRoutematchheadersmatchrangeTypeDef(
    _ClientCreateRoutespechttpRoutematchheadersmatchrangeTypeDef
):
    """
    Type definition for `ClientCreateRoutespechttpRoutematchheadersmatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --* **[REQUIRED]**

      The end of the range.

    - **start** *(integer) --* **[REQUIRED]**

      The start of the range.
    """


_ClientCreateRoutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "_ClientCreateRoutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRoutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientCreateRoutespechttpRoutematchheadersmatchTypeDef(
    _ClientCreateRoutespechttpRoutematchheadersmatchTypeDef
):
    """
    Type definition for `ClientCreateRoutespechttpRoutematchheaders` `match`

    The ``HeaderMatchMethod`` object.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --* **[REQUIRED]**

        The end of the range.

      - **start** *(integer) --* **[REQUIRED]**

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_RequiredClientCreateRoutespechttpRoutematchheadersTypeDef = TypedDict(
    "_RequiredClientCreateRoutespechttpRoutematchheadersTypeDef", {"name": str}
)
_OptionalClientCreateRoutespechttpRoutematchheadersTypeDef = TypedDict(
    "_OptionalClientCreateRoutespechttpRoutematchheadersTypeDef",
    {"invert": bool, "match": ClientCreateRoutespechttpRoutematchheadersmatchTypeDef},
    total=False,
)


class ClientCreateRoutespechttpRoutematchheadersTypeDef(
    _RequiredClientCreateRoutespechttpRoutematchheadersTypeDef,
    _OptionalClientCreateRoutespechttpRoutematchheadersTypeDef,
):
    """
    Type definition for `ClientCreateRoutespechttpRoutematch` `headers`

    An object that represents the HTTP header in the request.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value is
      ``False`` .

    - **match** *(dict) --*

      The ``HeaderMatchMethod`` object.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --* **[REQUIRED]**

          The end of the range.

        - **start** *(integer) --* **[REQUIRED]**

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --* **[REQUIRED]**

      A name for the HTTP header in the client request that will be matched on.
    """


_RequiredClientCreateRoutespechttpRoutematchTypeDef = TypedDict(
    "_RequiredClientCreateRoutespechttpRoutematchTypeDef", {"prefix": str}
)
_OptionalClientCreateRoutespechttpRoutematchTypeDef = TypedDict(
    "_OptionalClientCreateRoutespechttpRoutematchTypeDef",
    {
        "headers": List[ClientCreateRoutespechttpRoutematchheadersTypeDef],
        "method": str,
        "scheme": str,
    },
    total=False,
)


class ClientCreateRoutespechttpRoutematchTypeDef(
    _RequiredClientCreateRoutespechttpRoutematchTypeDef,
    _OptionalClientCreateRoutespechttpRoutematchTypeDef,
):
    """
    Type definition for `ClientCreateRoutespechttpRoute` `match`

    An object that represents the criteria for determining a request match.

    - **headers** *(list) --*

      An object that represents the client request headers to match on.

      - *(dict) --*

        An object that represents the HTTP header in the request.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value is
          ``False`` .

        - **match** *(dict) --*

          The ``HeaderMatchMethod`` object.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --* **[REQUIRED]**

              The end of the range.

            - **start** *(integer) --* **[REQUIRED]**

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --* **[REQUIRED]**

          A name for the HTTP header in the client request that will be matched on.

    - **method** *(string) --*

      The client request method to match on. Specify only one.

    - **prefix** *(string) --* **[REQUIRED]**

      Specifies the path to match requests with. This parameter must always start with ``/`` ,
      which by itself matches all requests to the virtual service name. You can also match for
      path-based routing of requests. For example, if your virtual service name is
      ``my-service.local`` and you want the route to match requests to
      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

    - **scheme** *(string) --*

      The client request scheme to match on. Specify only one.
    """


_ClientCreateRoutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientCreateRoutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientCreateRoutespechttpRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientCreateRoutespechttpRouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientCreateRoutespechttpRouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_RequiredClientCreateRoutespechttpRouteretryPolicyTypeDef = TypedDict(
    "_RequiredClientCreateRoutespechttpRouteretryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRoutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
    },
)
_OptionalClientCreateRoutespechttpRouteretryPolicyTypeDef = TypedDict(
    "_OptionalClientCreateRoutespechttpRouteretryPolicyTypeDef",
    {"httpRetryEvents": List[str], "tcpRetryEvents": List[str]},
    total=False,
)


class ClientCreateRoutespechttpRouteretryPolicyTypeDef(
    _RequiredClientCreateRoutespechttpRouteretryPolicyTypeDef,
    _OptionalClientCreateRoutespechttpRouteretryPolicyTypeDef,
):
    """
    Type definition for `ClientCreateRoutespechttpRoute` `retryPolicy`

    An object that represents a retry policy.

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
      and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --* **[REQUIRED]**

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --* **[REQUIRED]**

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_RequiredClientCreateRoutespechttpRouteTypeDef = TypedDict(
    "_RequiredClientCreateRoutespechttpRouteTypeDef",
    {
        "action": ClientCreateRoutespechttpRouteactionTypeDef,
        "match": ClientCreateRoutespechttpRoutematchTypeDef,
    },
)
_OptionalClientCreateRoutespechttpRouteTypeDef = TypedDict(
    "_OptionalClientCreateRoutespechttpRouteTypeDef",
    {"retryPolicy": ClientCreateRoutespechttpRouteretryPolicyTypeDef},
    total=False,
)


class ClientCreateRoutespechttpRouteTypeDef(
    _RequiredClientCreateRoutespechttpRouteTypeDef,
    _OptionalClientCreateRoutespechttpRouteTypeDef,
):
    """
    Type definition for `ClientCreateRoutespec` `httpRoute`

    An object that represents the specification of an HTTP route.

    - **action** *(dict) --* **[REQUIRED]**

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --* **[REQUIRED]**

        An object that represents the targets that traffic is routed to when a request matches the
        route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed across
          targets according to their relative weight. For example, a weighted target with a
          relative weight of 50 receives five times as much traffic as one with a relative weight
          of 10. The total weight for all targets combined must be less than or equal to 100.

          - **virtualNode** *(string) --* **[REQUIRED]**

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --* **[REQUIRED]**

            The relative weight of the weighted target.

    - **match** *(dict) --* **[REQUIRED]**

      An object that represents the criteria for determining a request match.

      - **headers** *(list) --*

        An object that represents the client request headers to match on.

        - *(dict) --*

          An object that represents the HTTP header in the request.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value is
            ``False`` .

          - **match** *(dict) --*

            The ``HeaderMatchMethod`` object.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --* **[REQUIRED]**

                The end of the range.

              - **start** *(integer) --* **[REQUIRED]**

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --* **[REQUIRED]**

            A name for the HTTP header in the client request that will be matched on.

      - **method** *(string) --*

        The client request method to match on. Specify only one.

      - **prefix** *(string) --* **[REQUIRED]**

        Specifies the path to match requests with. This parameter must always start with ``/`` ,
        which by itself matches all requests to the virtual service name. You can also match for
        path-based routing of requests. For example, if your virtual service name is
        ``my-service.local`` and you want the route to match requests to
        ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

      - **scheme** *(string) --*

        The client request scheme to match on. Specify only one.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
        and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --* **[REQUIRED]**

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --* **[REQUIRED]**

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientCreateRoutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRoutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
)


class ClientCreateRoutespectcpRouteactionweightedTargetsTypeDef(
    _ClientCreateRoutespectcpRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientCreateRoutespectcpRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed across
    targets according to their relative weight. For example, a weighted target with a
    relative weight of 50 receives five times as much traffic as one with a relative weight
    of 10. The total weight for all targets combined must be less than or equal to 100.

    - **virtualNode** *(string) --* **[REQUIRED]**

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --* **[REQUIRED]**

      The relative weight of the weighted target.
    """


_ClientCreateRoutespectcpRouteactionTypeDef = TypedDict(
    "_ClientCreateRoutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRoutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
)


class ClientCreateRoutespectcpRouteactionTypeDef(
    _ClientCreateRoutespectcpRouteactionTypeDef
):
    """
    Type definition for `ClientCreateRoutespectcpRoute` `action`

    The action to take if a match is determined.

    - **weightedTargets** *(list) --* **[REQUIRED]**

      An object that represents the targets that traffic is routed to when a request matches the
      route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed across
        targets according to their relative weight. For example, a weighted target with a
        relative weight of 50 receives five times as much traffic as one with a relative weight
        of 10. The total weight for all targets combined must be less than or equal to 100.

        - **virtualNode** *(string) --* **[REQUIRED]**

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --* **[REQUIRED]**

          The relative weight of the weighted target.
    """


_ClientCreateRoutespectcpRouteTypeDef = TypedDict(
    "_ClientCreateRoutespectcpRouteTypeDef",
    {"action": ClientCreateRoutespectcpRouteactionTypeDef},
)


class ClientCreateRoutespectcpRouteTypeDef(_ClientCreateRoutespectcpRouteTypeDef):
    """
    Type definition for `ClientCreateRoutespec` `tcpRoute`

    An object that represents the specification of a TCP route.

    - **action** *(dict) --* **[REQUIRED]**

      The action to take if a match is determined.

      - **weightedTargets** *(list) --* **[REQUIRED]**

        An object that represents the targets that traffic is routed to when a request matches the
        route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed across
          targets according to their relative weight. For example, a weighted target with a
          relative weight of 50 receives five times as much traffic as one with a relative weight
          of 10. The total weight for all targets combined must be less than or equal to 100.

          - **virtualNode** *(string) --* **[REQUIRED]**

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --* **[REQUIRED]**

            The relative weight of the weighted target.
    """


_ClientCreateRoutespecTypeDef = TypedDict(
    "_ClientCreateRoutespecTypeDef",
    {
        "grpcRoute": ClientCreateRoutespecgrpcRouteTypeDef,
        "http2Route": ClientCreateRoutespechttp2RouteTypeDef,
        "httpRoute": ClientCreateRoutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientCreateRoutespectcpRouteTypeDef,
    },
    total=False,
)


class ClientCreateRoutespecTypeDef(_ClientCreateRoutespecTypeDef):
    """
    Type definition for `ClientCreateRoute` `spec`

    The route specification to apply.

    - **grpcRoute** *(dict) --*

      An object that represents the specification of a GRPC route.

      - **action** *(dict) --* **[REQUIRED]**

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --* **[REQUIRED]**

          An object that represents the targets that traffic is routed to when a request matches the
          route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed across
            targets according to their relative weight. For example, a weighted target with a
            relative weight of 50 receives five times as much traffic as one with a relative weight
            of 10. The total weight for all targets combined must be less than or equal to 100.

            - **virtualNode** *(string) --* **[REQUIRED]**

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --* **[REQUIRED]**

              The relative weight of the weighted target.

      - **match** *(dict) --* **[REQUIRED]**

        An object that represents the criteria for determining a request match.

        - **metadata** *(list) --*

          An object that represents the data to match from the request.

          - *(dict) --*

            An object that represents the match metadata for the route.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value is
              ``False`` .

            - **match** *(dict) --*

              An object that represents the data to match from the request.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --* **[REQUIRED]**

                  The end of the range.

                - **start** *(integer) --* **[REQUIRED]**

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --* **[REQUIRED]**

              The name of the route.

        - **methodName** *(string) --*

          The method name to match from the request. If you specify a name, you must also specify a
          ``serviceName`` .

        - **serviceName** *(string) --*

          The fully qualified domain name for the service to match from the request.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **grpcRetryEvents** *(list) --*

          Specify at least one of the valid values.

          - *(string) --*

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
          and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --* **[REQUIRED]**

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --* **[REQUIRED]**

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **http2Route** *(dict) --*

      An object that represents the specification of an HTTP2 route.

      - **action** *(dict) --* **[REQUIRED]**

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --* **[REQUIRED]**

          An object that represents the targets that traffic is routed to when a request matches the
          route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed across
            targets according to their relative weight. For example, a weighted target with a
            relative weight of 50 receives five times as much traffic as one with a relative weight
            of 10. The total weight for all targets combined must be less than or equal to 100.

            - **virtualNode** *(string) --* **[REQUIRED]**

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --* **[REQUIRED]**

              The relative weight of the weighted target.

      - **match** *(dict) --* **[REQUIRED]**

        An object that represents the criteria for determining a request match.

        - **headers** *(list) --*

          An object that represents the client request headers to match on.

          - *(dict) --*

            An object that represents the HTTP header in the request.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value is
              ``False`` .

            - **match** *(dict) --*

              The ``HeaderMatchMethod`` object.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --* **[REQUIRED]**

                  The end of the range.

                - **start** *(integer) --* **[REQUIRED]**

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --* **[REQUIRED]**

              A name for the HTTP header in the client request that will be matched on.

        - **method** *(string) --*

          The client request method to match on. Specify only one.

        - **prefix** *(string) --* **[REQUIRED]**

          Specifies the path to match requests with. This parameter must always start with ``/`` ,
          which by itself matches all requests to the virtual service name. You can also match for
          path-based routing of requests. For example, if your virtual service name is
          ``my-service.local`` and you want the route to match requests to
          ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

        - **scheme** *(string) --*

          The client request scheme to match on. Specify only one.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
          and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --* **[REQUIRED]**

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --* **[REQUIRED]**

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **httpRoute** *(dict) --*

      An object that represents the specification of an HTTP route.

      - **action** *(dict) --* **[REQUIRED]**

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --* **[REQUIRED]**

          An object that represents the targets that traffic is routed to when a request matches the
          route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed across
            targets according to their relative weight. For example, a weighted target with a
            relative weight of 50 receives five times as much traffic as one with a relative weight
            of 10. The total weight for all targets combined must be less than or equal to 100.

            - **virtualNode** *(string) --* **[REQUIRED]**

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --* **[REQUIRED]**

              The relative weight of the weighted target.

      - **match** *(dict) --* **[REQUIRED]**

        An object that represents the criteria for determining a request match.

        - **headers** *(list) --*

          An object that represents the client request headers to match on.

          - *(dict) --*

            An object that represents the HTTP header in the request.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value is
              ``False`` .

            - **match** *(dict) --*

              The ``HeaderMatchMethod`` object.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --* **[REQUIRED]**

                  The end of the range.

                - **start** *(integer) --* **[REQUIRED]**

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --* **[REQUIRED]**

              A name for the HTTP header in the client request that will be matched on.

        - **method** *(string) --*

          The client request method to match on. Specify only one.

        - **prefix** *(string) --* **[REQUIRED]**

          Specifies the path to match requests with. This parameter must always start with ``/`` ,
          which by itself matches all requests to the virtual service name. You can also match for
          path-based routing of requests. For example, if your virtual service name is
          ``my-service.local`` and you want the route to match requests to
          ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

        - **scheme** *(string) --*

          The client request scheme to match on. Specify only one.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
          and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --* **[REQUIRED]**

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --* **[REQUIRED]**

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **priority** *(integer) --*

      The priority for the route. Routes are matched based on the specified value, where 0 is the
      highest priority.

    - **tcpRoute** *(dict) --*

      An object that represents the specification of a TCP route.

      - **action** *(dict) --* **[REQUIRED]**

        The action to take if a match is determined.

        - **weightedTargets** *(list) --* **[REQUIRED]**

          An object that represents the targets that traffic is routed to when a request matches the
          route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed across
            targets according to their relative weight. For example, a weighted target with a
            relative weight of 50 receives five times as much traffic as one with a relative weight
            of 10. The total weight for all targets combined must be less than or equal to 100.

            - **virtualNode** *(string) --* **[REQUIRED]**

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --* **[REQUIRED]**

              The relative weight of the weighted target.
    """


_RequiredClientCreateRoutetagsTypeDef = TypedDict(
    "_RequiredClientCreateRoutetagsTypeDef", {"key": str}
)
_OptionalClientCreateRoutetagsTypeDef = TypedDict(
    "_OptionalClientCreateRoutetagsTypeDef", {"value": str}, total=False
)


class ClientCreateRoutetagsTypeDef(
    _RequiredClientCreateRoutetagsTypeDef, _OptionalClientCreateRoutetagsTypeDef
):
    """
    Type definition for `ClientCreateRoute` `tags`

    Optional metadata that you apply to a resource to assist with categorization and organization.
    Each tag consists of a key and an optional value, both of which you define. Tag keys can have a
    maximum character length of 128 characters, and tag values can have a maximum length of 256
    characters.

    - **key** *(string) --* **[REQUIRED]**

      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
      a category for more specific tag values.

    - **value** *(string) --*

      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
      within a tag category (key).
    """


_ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNode` `metadata`

    The associated metadata for the virtual node.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNodespecbackends` `virtualService`

    Specifies a virtual service to use as a backend for a virtual node.

    - **virtualServiceName** *(string) --*

      The name of the virtual service that is acting as a virtual node backend.
    """


_ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    {
        "virtualService": ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNodespec` `backends`

    An object that represents the backends that a virtual node is expected to send outbound
    traffic to.

    - **virtualService** *(dict) --*

      Specifies a virtual service to use as a backend for a virtual node.

      - **virtualServiceName** *(string) --*

        The name of the virtual service that is acting as a virtual node backend.
    """


_ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": str,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNodespeclisteners` `healthCheck`

    The health check information for the listener.

    - **healthyThreshold** *(integer) --*

      The number of consecutive successful health checks that must occur before declaring
      listener healthy.

    - **intervalMillis** *(integer) --*

      The time period in milliseconds between each health check execution.

    - **path** *(string) --*

      The destination path for the health check request. This is required only if the
      specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

    - **port** *(integer) --*

      The destination port for the health check request. This port must match the port
      defined in the  PortMapping for the listener.

    - **protocol** *(string) --*

      The protocol for the health check request.

    - **timeoutMillis** *(integer) --*

      The amount of time to wait when receiving a response from the health check, in
      milliseconds.

    - **unhealthyThreshold** *(integer) --*

      The number of consecutive failed health checks that must occur before declaring a
      virtual node unhealthy.
    """


_ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": str},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNodespeclisteners` `portMapping`

    The port mapping information for the listener.

    - **port** *(integer) --*

      The port used for the port mapping.

    - **protocol** *(string) --*

      The protocol used for the port mapping. Specify one protocol.
    """


_ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    {
        "healthCheck": ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef,
        "portMapping": ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef,
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNodespec` `listeners`

    An object that represents a listener for a virtual node.

    - **healthCheck** *(dict) --*

      The health check information for the listener.

      - **healthyThreshold** *(integer) --*

        The number of consecutive successful health checks that must occur before declaring
        listener healthy.

      - **intervalMillis** *(integer) --*

        The time period in milliseconds between each health check execution.

      - **path** *(string) --*

        The destination path for the health check request. This is required only if the
        specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

      - **port** *(integer) --*

        The destination port for the health check request. This port must match the port
        defined in the  PortMapping for the listener.

      - **protocol** *(string) --*

        The protocol for the health check request.

      - **timeoutMillis** *(integer) --*

        The amount of time to wait when receiving a response from the health check, in
        milliseconds.

      - **unhealthyThreshold** *(integer) --*

        The number of consecutive failed health checks that must occur before declaring a
        virtual node unhealthy.

    - **portMapping** *(dict) --*

      The port mapping information for the listener.

      - **port** *(integer) --*

        The port used for the port mapping.

      - **protocol** *(string) --*

        The protocol used for the port mapping. Specify one protocol.
    """


_ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    {"path": str},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLog` `file`

    The file object to send virtual node access logs to.

    - **path** *(string) --*

      The file path to write access logs to. You can use ``/dev/stdout`` to send access
      logs to standard out and configure your Envoy container to use a log driver, such
      as ``awslogs`` , to export the access logs to a log storage service such as Amazon
      CloudWatch Logs. You can also specify a path in the Envoy container's file system
      to write the files to disk.

      .. note::

        The Envoy process must have write permissions to the path that you specify here.
        Otherwise, Envoy fails to bootstrap properly.
    """


_ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    {"file": ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNodespeclogging` `accessLog`

    The access log configuration for a virtual node.

    - **file** *(dict) --*

      The file object to send virtual node access logs to.

      - **path** *(string) --*

        The file path to write access logs to. You can use ``/dev/stdout`` to send access
        logs to standard out and configure your Envoy container to use a log driver, such
        as ``awslogs`` , to export the access logs to a log storage service such as Amazon
        CloudWatch Logs. You can also specify a path in the Envoy container's file system
        to write the files to disk.

        .. note::

          The Envoy process must have write permissions to the path that you specify here.
          Otherwise, Envoy fails to bootstrap properly.
    """


_ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef",
    {
        "accessLog": ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNodespec` `logging`

    The inbound and outbound access logging information for the virtual node.

    - **accessLog** *(dict) --*

      The access log configuration for a virtual node.

      - **file** *(dict) --*

        The file object to send virtual node access logs to.

        - **path** *(string) --*

          The file path to write access logs to. You can use ``/dev/stdout`` to send access
          logs to standard out and configure your Envoy container to use a log driver, such
          as ``awslogs`` , to export the access logs to a log storage service such as Amazon
          CloudWatch Logs. You can also specify a path in the Envoy container's file system
          to write the files to disk.

          .. note::

            The Envoy process must have write permissions to the path that you specify here.
            Otherwise, Envoy fails to bootstrap properly.
    """


_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMap` `attributes`

    An object that represents the AWS Cloud Map attribute information for your virtual
    node.

    - **key** *(string) --*

      The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
      service instance that contains the specified key and value is returned.

    - **value** *(string) --*

      The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
      service instance that contains the specified key and value is returned.
    """


_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscovery` `awsCloudMap`

    Specifies any AWS Cloud Map information for the virtual node.

    - **attributes** *(list) --*

      A string map that contains attributes with values that you can use to filter
      instances by any custom attribute that you specified when you registered the
      instance. Only instances that match all of the specified key/value pairs will be
      returned.

      - *(dict) --*

        An object that represents the AWS Cloud Map attribute information for your virtual
        node.

        - **key** *(string) --*

          The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
          service instance that contains the specified key and value is returned.

        - **value** *(string) --*

          The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
          service instance that contains the specified key and value is returned.

    - **namespaceName** *(string) --*

      The name of the AWS Cloud Map namespace to use.

    - **serviceName** *(string) --*

      The name of the AWS Cloud Map service to use.
    """


_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    {"hostname": str},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscovery` `dns`

    Specifies the DNS information for the virtual node.

    - **hostname** *(string) --*

      Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNodespec` `serviceDiscovery`

    The service discovery information for the virtual node. If your virtual node does not
    expect ingress traffic, you can omit this parameter.

    - **awsCloudMap** *(dict) --*

      Specifies any AWS Cloud Map information for the virtual node.

      - **attributes** *(list) --*

        A string map that contains attributes with values that you can use to filter
        instances by any custom attribute that you specified when you registered the
        instance. Only instances that match all of the specified key/value pairs will be
        returned.

        - *(dict) --*

          An object that represents the AWS Cloud Map attribute information for your virtual
          node.

          - **key** *(string) --*

            The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
            service instance that contains the specified key and value is returned.

          - **value** *(string) --*

            The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
            service instance that contains the specified key and value is returned.

      - **namespaceName** *(string) --*

        The name of the AWS Cloud Map namespace to use.

      - **serviceName** *(string) --*

        The name of the AWS Cloud Map service to use.

    - **dns** *(dict) --*

      Specifies the DNS information for the virtual node.

      - **hostname** *(string) --*

        Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientCreateVirtualNodeResponsevirtualNodespecTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecTypeDef",
    {
        "backends": List[ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef],
        "listeners": List[
            ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef
        ],
        "logging": ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNode` `spec`

    The specifications of the virtual node.

    - **backends** *(list) --*

      The backends that the virtual node is expected to send outbound traffic to.

      - *(dict) --*

        An object that represents the backends that a virtual node is expected to send outbound
        traffic to.

        - **virtualService** *(dict) --*

          Specifies a virtual service to use as a backend for a virtual node.

          - **virtualServiceName** *(string) --*

            The name of the virtual service that is acting as a virtual node backend.

    - **listeners** *(list) --*

      The listeners that the virtual node is expected to receive inbound traffic from. You can
      specify one listener.

      - *(dict) --*

        An object that represents a listener for a virtual node.

        - **healthCheck** *(dict) --*

          The health check information for the listener.

          - **healthyThreshold** *(integer) --*

            The number of consecutive successful health checks that must occur before declaring
            listener healthy.

          - **intervalMillis** *(integer) --*

            The time period in milliseconds between each health check execution.

          - **path** *(string) --*

            The destination path for the health check request. This is required only if the
            specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

          - **port** *(integer) --*

            The destination port for the health check request. This port must match the port
            defined in the  PortMapping for the listener.

          - **protocol** *(string) --*

            The protocol for the health check request.

          - **timeoutMillis** *(integer) --*

            The amount of time to wait when receiving a response from the health check, in
            milliseconds.

          - **unhealthyThreshold** *(integer) --*

            The number of consecutive failed health checks that must occur before declaring a
            virtual node unhealthy.

        - **portMapping** *(dict) --*

          The port mapping information for the listener.

          - **port** *(integer) --*

            The port used for the port mapping.

          - **protocol** *(string) --*

            The protocol used for the port mapping. Specify one protocol.

    - **logging** *(dict) --*

      The inbound and outbound access logging information for the virtual node.

      - **accessLog** *(dict) --*

        The access log configuration for a virtual node.

        - **file** *(dict) --*

          The file object to send virtual node access logs to.

          - **path** *(string) --*

            The file path to write access logs to. You can use ``/dev/stdout`` to send access
            logs to standard out and configure your Envoy container to use a log driver, such
            as ``awslogs`` , to export the access logs to a log storage service such as Amazon
            CloudWatch Logs. You can also specify a path in the Envoy container's file system
            to write the files to disk.

            .. note::

              The Envoy process must have write permissions to the path that you specify here.
              Otherwise, Envoy fails to bootstrap properly.

    - **serviceDiscovery** *(dict) --*

      The service discovery information for the virtual node. If your virtual node does not
      expect ingress traffic, you can omit this parameter.

      - **awsCloudMap** *(dict) --*

        Specifies any AWS Cloud Map information for the virtual node.

        - **attributes** *(list) --*

          A string map that contains attributes with values that you can use to filter
          instances by any custom attribute that you specified when you registered the
          instance. Only instances that match all of the specified key/value pairs will be
          returned.

          - *(dict) --*

            An object that represents the AWS Cloud Map attribute information for your virtual
            node.

            - **key** *(string) --*

              The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
              service instance that contains the specified key and value is returned.

            - **value** *(string) --*

              The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
              service instance that contains the specified key and value is returned.

        - **namespaceName** *(string) --*

          The name of the AWS Cloud Map namespace to use.

        - **serviceName** *(string) --*

          The name of the AWS Cloud Map service to use.

      - **dns** *(dict) --*

        Specifies the DNS information for the virtual node.

        - **hostname** *(string) --*

          Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef",
    {"status": str},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponsevirtualNode` `status`

    The current status for the virtual node.

    - **status** *(string) --*

      The current status of the virtual node.
    """


_ClientCreateVirtualNodeResponsevirtualNodeTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodeTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef,
        "spec": ClientCreateVirtualNodeResponsevirtualNodespecTypeDef,
        "status": ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef,
        "virtualNodeName": str,
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodeTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodeTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodeResponse` `virtualNode`

    The full description of your virtual node following the create call.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual node resides in.

    - **metadata** *(dict) --*

      The associated metadata for the virtual node.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The specifications of the virtual node.

      - **backends** *(list) --*

        The backends that the virtual node is expected to send outbound traffic to.

        - *(dict) --*

          An object that represents the backends that a virtual node is expected to send outbound
          traffic to.

          - **virtualService** *(dict) --*

            Specifies a virtual service to use as a backend for a virtual node.

            - **virtualServiceName** *(string) --*

              The name of the virtual service that is acting as a virtual node backend.

      - **listeners** *(list) --*

        The listeners that the virtual node is expected to receive inbound traffic from. You can
        specify one listener.

        - *(dict) --*

          An object that represents a listener for a virtual node.

          - **healthCheck** *(dict) --*

            The health check information for the listener.

            - **healthyThreshold** *(integer) --*

              The number of consecutive successful health checks that must occur before declaring
              listener healthy.

            - **intervalMillis** *(integer) --*

              The time period in milliseconds between each health check execution.

            - **path** *(string) --*

              The destination path for the health check request. This is required only if the
              specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

            - **port** *(integer) --*

              The destination port for the health check request. This port must match the port
              defined in the  PortMapping for the listener.

            - **protocol** *(string) --*

              The protocol for the health check request.

            - **timeoutMillis** *(integer) --*

              The amount of time to wait when receiving a response from the health check, in
              milliseconds.

            - **unhealthyThreshold** *(integer) --*

              The number of consecutive failed health checks that must occur before declaring a
              virtual node unhealthy.

          - **portMapping** *(dict) --*

            The port mapping information for the listener.

            - **port** *(integer) --*

              The port used for the port mapping.

            - **protocol** *(string) --*

              The protocol used for the port mapping. Specify one protocol.

      - **logging** *(dict) --*

        The inbound and outbound access logging information for the virtual node.

        - **accessLog** *(dict) --*

          The access log configuration for a virtual node.

          - **file** *(dict) --*

            The file object to send virtual node access logs to.

            - **path** *(string) --*

              The file path to write access logs to. You can use ``/dev/stdout`` to send access
              logs to standard out and configure your Envoy container to use a log driver, such
              as ``awslogs`` , to export the access logs to a log storage service such as Amazon
              CloudWatch Logs. You can also specify a path in the Envoy container's file system
              to write the files to disk.

              .. note::

                The Envoy process must have write permissions to the path that you specify here.
                Otherwise, Envoy fails to bootstrap properly.

      - **serviceDiscovery** *(dict) --*

        The service discovery information for the virtual node. If your virtual node does not
        expect ingress traffic, you can omit this parameter.

        - **awsCloudMap** *(dict) --*

          Specifies any AWS Cloud Map information for the virtual node.

          - **attributes** *(list) --*

            A string map that contains attributes with values that you can use to filter
            instances by any custom attribute that you specified when you registered the
            instance. Only instances that match all of the specified key/value pairs will be
            returned.

            - *(dict) --*

              An object that represents the AWS Cloud Map attribute information for your virtual
              node.

              - **key** *(string) --*

                The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                service instance that contains the specified key and value is returned.

              - **value** *(string) --*

                The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                service instance that contains the specified key and value is returned.

          - **namespaceName** *(string) --*

            The name of the AWS Cloud Map namespace to use.

          - **serviceName** *(string) --*

            The name of the AWS Cloud Map service to use.

        - **dns** *(dict) --*

          Specifies the DNS information for the virtual node.

          - **hostname** *(string) --*

            Specifies the DNS service discovery hostname for the virtual node.

    - **status** *(dict) --*

      The current status for the virtual node.

      - **status** *(string) --*

        The current status of the virtual node.

    - **virtualNodeName** *(string) --*

      The name of the virtual node.
    """


_ClientCreateVirtualNodeResponseTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponseTypeDef",
    {"virtualNode": ClientCreateVirtualNodeResponsevirtualNodeTypeDef},
    total=False,
)


class ClientCreateVirtualNodeResponseTypeDef(_ClientCreateVirtualNodeResponseTypeDef):
    """
    Type definition for `ClientCreateVirtualNode` `Response`

    - **virtualNode** *(dict) --*

      The full description of your virtual node following the create call.

      - **meshName** *(string) --*

        The name of the service mesh that the virtual node resides in.

      - **metadata** *(dict) --*

        The associated metadata for the virtual node.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The specifications of the virtual node.

        - **backends** *(list) --*

          The backends that the virtual node is expected to send outbound traffic to.

          - *(dict) --*

            An object that represents the backends that a virtual node is expected to send outbound
            traffic to.

            - **virtualService** *(dict) --*

              Specifies a virtual service to use as a backend for a virtual node.

              - **virtualServiceName** *(string) --*

                The name of the virtual service that is acting as a virtual node backend.

        - **listeners** *(list) --*

          The listeners that the virtual node is expected to receive inbound traffic from. You can
          specify one listener.

          - *(dict) --*

            An object that represents a listener for a virtual node.

            - **healthCheck** *(dict) --*

              The health check information for the listener.

              - **healthyThreshold** *(integer) --*

                The number of consecutive successful health checks that must occur before declaring
                listener healthy.

              - **intervalMillis** *(integer) --*

                The time period in milliseconds between each health check execution.

              - **path** *(string) --*

                The destination path for the health check request. This is required only if the
                specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

              - **port** *(integer) --*

                The destination port for the health check request. This port must match the port
                defined in the  PortMapping for the listener.

              - **protocol** *(string) --*

                The protocol for the health check request.

              - **timeoutMillis** *(integer) --*

                The amount of time to wait when receiving a response from the health check, in
                milliseconds.

              - **unhealthyThreshold** *(integer) --*

                The number of consecutive failed health checks that must occur before declaring a
                virtual node unhealthy.

            - **portMapping** *(dict) --*

              The port mapping information for the listener.

              - **port** *(integer) --*

                The port used for the port mapping.

              - **protocol** *(string) --*

                The protocol used for the port mapping. Specify one protocol.

        - **logging** *(dict) --*

          The inbound and outbound access logging information for the virtual node.

          - **accessLog** *(dict) --*

            The access log configuration for a virtual node.

            - **file** *(dict) --*

              The file object to send virtual node access logs to.

              - **path** *(string) --*

                The file path to write access logs to. You can use ``/dev/stdout`` to send access
                logs to standard out and configure your Envoy container to use a log driver, such
                as ``awslogs`` , to export the access logs to a log storage service such as Amazon
                CloudWatch Logs. You can also specify a path in the Envoy container's file system
                to write the files to disk.

                .. note::

                  The Envoy process must have write permissions to the path that you specify here.
                  Otherwise, Envoy fails to bootstrap properly.

        - **serviceDiscovery** *(dict) --*

          The service discovery information for the virtual node. If your virtual node does not
          expect ingress traffic, you can omit this parameter.

          - **awsCloudMap** *(dict) --*

            Specifies any AWS Cloud Map information for the virtual node.

            - **attributes** *(list) --*

              A string map that contains attributes with values that you can use to filter
              instances by any custom attribute that you specified when you registered the
              instance. Only instances that match all of the specified key/value pairs will be
              returned.

              - *(dict) --*

                An object that represents the AWS Cloud Map attribute information for your virtual
                node.

                - **key** *(string) --*

                  The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                  service instance that contains the specified key and value is returned.

                - **value** *(string) --*

                  The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                  service instance that contains the specified key and value is returned.

            - **namespaceName** *(string) --*

              The name of the AWS Cloud Map namespace to use.

            - **serviceName** *(string) --*

              The name of the AWS Cloud Map service to use.

          - **dns** *(dict) --*

            Specifies the DNS information for the virtual node.

            - **hostname** *(string) --*

              Specifies the DNS service discovery hostname for the virtual node.

      - **status** *(dict) --*

        The current status for the virtual node.

        - **status** *(string) --*

          The current status of the virtual node.

      - **virtualNodeName** *(string) --*

        The name of the virtual node.
    """


_ClientCreateVirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "_ClientCreateVirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
)


class ClientCreateVirtualNodespecbackendsvirtualServiceTypeDef(
    _ClientCreateVirtualNodespecbackendsvirtualServiceTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodespecbackends` `virtualService`

    Specifies a virtual service to use as a backend for a virtual node.

    - **virtualServiceName** *(string) --* **[REQUIRED]**

      The name of the virtual service that is acting as a virtual node backend.
    """


_ClientCreateVirtualNodespecbackendsTypeDef = TypedDict(
    "_ClientCreateVirtualNodespecbackendsTypeDef",
    {"virtualService": ClientCreateVirtualNodespecbackendsvirtualServiceTypeDef},
    total=False,
)


class ClientCreateVirtualNodespecbackendsTypeDef(
    _ClientCreateVirtualNodespecbackendsTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodespec` `backends`

    An object that represents the backends that a virtual node is expected to send outbound
    traffic to.

    - **virtualService** *(dict) --*

      Specifies a virtual service to use as a backend for a virtual node.

      - **virtualServiceName** *(string) --* **[REQUIRED]**

        The name of the virtual service that is acting as a virtual node backend.
    """


_RequiredClientCreateVirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "_RequiredClientCreateVirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": str,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
)
_OptionalClientCreateVirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "_OptionalClientCreateVirtualNodespeclistenershealthCheckTypeDef",
    {"path": str, "port": int},
    total=False,
)


class ClientCreateVirtualNodespeclistenershealthCheckTypeDef(
    _RequiredClientCreateVirtualNodespeclistenershealthCheckTypeDef,
    _OptionalClientCreateVirtualNodespeclistenershealthCheckTypeDef,
):
    """
    Type definition for `ClientCreateVirtualNodespeclisteners` `healthCheck`

    The health check information for the listener.

    - **healthyThreshold** *(integer) --* **[REQUIRED]**

      The number of consecutive successful health checks that must occur before declaring
      listener healthy.

    - **intervalMillis** *(integer) --* **[REQUIRED]**

      The time period in milliseconds between each health check execution.

    - **path** *(string) --*

      The destination path for the health check request. This is required only if the specified
      protocol is HTTP. If the protocol is TCP, this parameter is ignored.

    - **port** *(integer) --*

      The destination port for the health check request. This port must match the port defined
      in the  PortMapping for the listener.

    - **protocol** *(string) --* **[REQUIRED]**

      The protocol for the health check request.

    - **timeoutMillis** *(integer) --* **[REQUIRED]**

      The amount of time to wait when receiving a response from the health check, in
      milliseconds.

    - **unhealthyThreshold** *(integer) --* **[REQUIRED]**

      The number of consecutive failed health checks that must occur before declaring a virtual
      node unhealthy.
    """


_ClientCreateVirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "_ClientCreateVirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": str},
)


class ClientCreateVirtualNodespeclistenersportMappingTypeDef(
    _ClientCreateVirtualNodespeclistenersportMappingTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodespeclisteners` `portMapping`

    The port mapping information for the listener.

    - **port** *(integer) --* **[REQUIRED]**

      The port used for the port mapping.

    - **protocol** *(string) --* **[REQUIRED]**

      The protocol used for the port mapping. Specify one protocol.
    """


_RequiredClientCreateVirtualNodespeclistenersTypeDef = TypedDict(
    "_RequiredClientCreateVirtualNodespeclistenersTypeDef",
    {"portMapping": ClientCreateVirtualNodespeclistenersportMappingTypeDef},
)
_OptionalClientCreateVirtualNodespeclistenersTypeDef = TypedDict(
    "_OptionalClientCreateVirtualNodespeclistenersTypeDef",
    {"healthCheck": ClientCreateVirtualNodespeclistenershealthCheckTypeDef},
    total=False,
)


class ClientCreateVirtualNodespeclistenersTypeDef(
    _RequiredClientCreateVirtualNodespeclistenersTypeDef,
    _OptionalClientCreateVirtualNodespeclistenersTypeDef,
):
    """
    Type definition for `ClientCreateVirtualNodespec` `listeners`

    An object that represents a listener for a virtual node.

    - **healthCheck** *(dict) --*

      The health check information for the listener.

      - **healthyThreshold** *(integer) --* **[REQUIRED]**

        The number of consecutive successful health checks that must occur before declaring
        listener healthy.

      - **intervalMillis** *(integer) --* **[REQUIRED]**

        The time period in milliseconds between each health check execution.

      - **path** *(string) --*

        The destination path for the health check request. This is required only if the specified
        protocol is HTTP. If the protocol is TCP, this parameter is ignored.

      - **port** *(integer) --*

        The destination port for the health check request. This port must match the port defined
        in the  PortMapping for the listener.

      - **protocol** *(string) --* **[REQUIRED]**

        The protocol for the health check request.

      - **timeoutMillis** *(integer) --* **[REQUIRED]**

        The amount of time to wait when receiving a response from the health check, in
        milliseconds.

      - **unhealthyThreshold** *(integer) --* **[REQUIRED]**

        The number of consecutive failed health checks that must occur before declaring a virtual
        node unhealthy.

    - **portMapping** *(dict) --* **[REQUIRED]**

      The port mapping information for the listener.

      - **port** *(integer) --* **[REQUIRED]**

        The port used for the port mapping.

      - **protocol** *(string) --* **[REQUIRED]**

        The protocol used for the port mapping. Specify one protocol.
    """


_ClientCreateVirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "_ClientCreateVirtualNodespecloggingaccessLogfileTypeDef", {"path": str}
)


class ClientCreateVirtualNodespecloggingaccessLogfileTypeDef(
    _ClientCreateVirtualNodespecloggingaccessLogfileTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodespecloggingaccessLog` `file`

    The file object to send virtual node access logs to.

    - **path** *(string) --* **[REQUIRED]**

      The file path to write access logs to. You can use ``/dev/stdout`` to send access logs to
      standard out and configure your Envoy container to use a log driver, such as ``awslogs``
      , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You
      can also specify a path in the Envoy container's file system to write the files to disk.

      .. note::

        The Envoy process must have write permissions to the path that you specify here.
        Otherwise, Envoy fails to bootstrap properly.
    """


_ClientCreateVirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "_ClientCreateVirtualNodespecloggingaccessLogTypeDef",
    {"file": ClientCreateVirtualNodespecloggingaccessLogfileTypeDef},
    total=False,
)


class ClientCreateVirtualNodespecloggingaccessLogTypeDef(
    _ClientCreateVirtualNodespecloggingaccessLogTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodespeclogging` `accessLog`

    The access log configuration for a virtual node.

    - **file** *(dict) --*

      The file object to send virtual node access logs to.

      - **path** *(string) --* **[REQUIRED]**

        The file path to write access logs to. You can use ``/dev/stdout`` to send access logs to
        standard out and configure your Envoy container to use a log driver, such as ``awslogs``
        , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You
        can also specify a path in the Envoy container's file system to write the files to disk.

        .. note::

          The Envoy process must have write permissions to the path that you specify here.
          Otherwise, Envoy fails to bootstrap properly.
    """


_ClientCreateVirtualNodespecloggingTypeDef = TypedDict(
    "_ClientCreateVirtualNodespecloggingTypeDef",
    {"accessLog": ClientCreateVirtualNodespecloggingaccessLogTypeDef},
    total=False,
)


class ClientCreateVirtualNodespecloggingTypeDef(
    _ClientCreateVirtualNodespecloggingTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodespec` `logging`

    The inbound and outbound access logging information for the virtual node.

    - **accessLog** *(dict) --*

      The access log configuration for a virtual node.

      - **file** *(dict) --*

        The file object to send virtual node access logs to.

        - **path** *(string) --* **[REQUIRED]**

          The file path to write access logs to. You can use ``/dev/stdout`` to send access logs to
          standard out and configure your Envoy container to use a log driver, such as ``awslogs``
          , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You
          can also specify a path in the Envoy container's file system to write the files to disk.

          .. note::

            The Envoy process must have write permissions to the path that you specify here.
            Otherwise, Envoy fails to bootstrap properly.
    """


_ClientCreateVirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "_ClientCreateVirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
)


class ClientCreateVirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef(
    _ClientCreateVirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodespecserviceDiscoveryawsCloudMap` `attributes`

    An object that represents the AWS Cloud Map attribute information for your virtual node.

    - **key** *(string) --* **[REQUIRED]**

      The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
      instance that contains the specified key and value is returned.

    - **value** *(string) --* **[REQUIRED]**

      The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
      instance that contains the specified key and value is returned.
    """


_RequiredClientCreateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_RequiredClientCreateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {"namespaceName": str, "serviceName": str},
)
_OptionalClientCreateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_OptionalClientCreateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientCreateVirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ]
    },
    total=False,
)


class ClientCreateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef(
    _RequiredClientCreateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
    _OptionalClientCreateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
):
    """
    Type definition for `ClientCreateVirtualNodespecserviceDiscovery` `awsCloudMap`

    Specifies any AWS Cloud Map information for the virtual node.

    - **attributes** *(list) --*

      A string map that contains attributes with values that you can use to filter instances by
      any custom attribute that you specified when you registered the instance. Only instances
      that match all of the specified key/value pairs will be returned.

      - *(dict) --*

        An object that represents the AWS Cloud Map attribute information for your virtual node.

        - **key** *(string) --* **[REQUIRED]**

          The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
          instance that contains the specified key and value is returned.

        - **value** *(string) --* **[REQUIRED]**

          The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
          instance that contains the specified key and value is returned.

    - **namespaceName** *(string) --* **[REQUIRED]**

      The name of the AWS Cloud Map namespace to use.

    - **serviceName** *(string) --* **[REQUIRED]**

      The name of the AWS Cloud Map service to use.
    """


_ClientCreateVirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "_ClientCreateVirtualNodespecserviceDiscoverydnsTypeDef", {"hostname": str}
)


class ClientCreateVirtualNodespecserviceDiscoverydnsTypeDef(
    _ClientCreateVirtualNodespecserviceDiscoverydnsTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodespecserviceDiscovery` `dns`

    Specifies the DNS information for the virtual node.

    - **hostname** *(string) --* **[REQUIRED]**

      Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientCreateVirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "_ClientCreateVirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientCreateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientCreateVirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)


class ClientCreateVirtualNodespecserviceDiscoveryTypeDef(
    _ClientCreateVirtualNodespecserviceDiscoveryTypeDef
):
    """
    Type definition for `ClientCreateVirtualNodespec` `serviceDiscovery`

    The service discovery information for the virtual node. If your virtual node does not expect
    ingress traffic, you can omit this parameter.

    - **awsCloudMap** *(dict) --*

      Specifies any AWS Cloud Map information for the virtual node.

      - **attributes** *(list) --*

        A string map that contains attributes with values that you can use to filter instances by
        any custom attribute that you specified when you registered the instance. Only instances
        that match all of the specified key/value pairs will be returned.

        - *(dict) --*

          An object that represents the AWS Cloud Map attribute information for your virtual node.

          - **key** *(string) --* **[REQUIRED]**

            The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
            instance that contains the specified key and value is returned.

          - **value** *(string) --* **[REQUIRED]**

            The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
            instance that contains the specified key and value is returned.

      - **namespaceName** *(string) --* **[REQUIRED]**

        The name of the AWS Cloud Map namespace to use.

      - **serviceName** *(string) --* **[REQUIRED]**

        The name of the AWS Cloud Map service to use.

    - **dns** *(dict) --*

      Specifies the DNS information for the virtual node.

      - **hostname** *(string) --* **[REQUIRED]**

        Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientCreateVirtualNodespecTypeDef = TypedDict(
    "_ClientCreateVirtualNodespecTypeDef",
    {
        "backends": List[ClientCreateVirtualNodespecbackendsTypeDef],
        "listeners": List[ClientCreateVirtualNodespeclistenersTypeDef],
        "logging": ClientCreateVirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientCreateVirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)


class ClientCreateVirtualNodespecTypeDef(_ClientCreateVirtualNodespecTypeDef):
    """
    Type definition for `ClientCreateVirtualNode` `spec`

    The virtual node specification to apply.

    - **backends** *(list) --*

      The backends that the virtual node is expected to send outbound traffic to.

      - *(dict) --*

        An object that represents the backends that a virtual node is expected to send outbound
        traffic to.

        - **virtualService** *(dict) --*

          Specifies a virtual service to use as a backend for a virtual node.

          - **virtualServiceName** *(string) --* **[REQUIRED]**

            The name of the virtual service that is acting as a virtual node backend.

    - **listeners** *(list) --*

      The listeners that the virtual node is expected to receive inbound traffic from. You can
      specify one listener.

      - *(dict) --*

        An object that represents a listener for a virtual node.

        - **healthCheck** *(dict) --*

          The health check information for the listener.

          - **healthyThreshold** *(integer) --* **[REQUIRED]**

            The number of consecutive successful health checks that must occur before declaring
            listener healthy.

          - **intervalMillis** *(integer) --* **[REQUIRED]**

            The time period in milliseconds between each health check execution.

          - **path** *(string) --*

            The destination path for the health check request. This is required only if the specified
            protocol is HTTP. If the protocol is TCP, this parameter is ignored.

          - **port** *(integer) --*

            The destination port for the health check request. This port must match the port defined
            in the  PortMapping for the listener.

          - **protocol** *(string) --* **[REQUIRED]**

            The protocol for the health check request.

          - **timeoutMillis** *(integer) --* **[REQUIRED]**

            The amount of time to wait when receiving a response from the health check, in
            milliseconds.

          - **unhealthyThreshold** *(integer) --* **[REQUIRED]**

            The number of consecutive failed health checks that must occur before declaring a virtual
            node unhealthy.

        - **portMapping** *(dict) --* **[REQUIRED]**

          The port mapping information for the listener.

          - **port** *(integer) --* **[REQUIRED]**

            The port used for the port mapping.

          - **protocol** *(string) --* **[REQUIRED]**

            The protocol used for the port mapping. Specify one protocol.

    - **logging** *(dict) --*

      The inbound and outbound access logging information for the virtual node.

      - **accessLog** *(dict) --*

        The access log configuration for a virtual node.

        - **file** *(dict) --*

          The file object to send virtual node access logs to.

          - **path** *(string) --* **[REQUIRED]**

            The file path to write access logs to. You can use ``/dev/stdout`` to send access logs to
            standard out and configure your Envoy container to use a log driver, such as ``awslogs``
            , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You
            can also specify a path in the Envoy container's file system to write the files to disk.

            .. note::

              The Envoy process must have write permissions to the path that you specify here.
              Otherwise, Envoy fails to bootstrap properly.

    - **serviceDiscovery** *(dict) --*

      The service discovery information for the virtual node. If your virtual node does not expect
      ingress traffic, you can omit this parameter.

      - **awsCloudMap** *(dict) --*

        Specifies any AWS Cloud Map information for the virtual node.

        - **attributes** *(list) --*

          A string map that contains attributes with values that you can use to filter instances by
          any custom attribute that you specified when you registered the instance. Only instances
          that match all of the specified key/value pairs will be returned.

          - *(dict) --*

            An object that represents the AWS Cloud Map attribute information for your virtual node.

            - **key** *(string) --* **[REQUIRED]**

              The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
              instance that contains the specified key and value is returned.

            - **value** *(string) --* **[REQUIRED]**

              The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
              instance that contains the specified key and value is returned.

        - **namespaceName** *(string) --* **[REQUIRED]**

          The name of the AWS Cloud Map namespace to use.

        - **serviceName** *(string) --* **[REQUIRED]**

          The name of the AWS Cloud Map service to use.

      - **dns** *(dict) --*

        Specifies the DNS information for the virtual node.

        - **hostname** *(string) --* **[REQUIRED]**

          Specifies the DNS service discovery hostname for the virtual node.
    """


_RequiredClientCreateVirtualNodetagsTypeDef = TypedDict(
    "_RequiredClientCreateVirtualNodetagsTypeDef", {"key": str}
)
_OptionalClientCreateVirtualNodetagsTypeDef = TypedDict(
    "_OptionalClientCreateVirtualNodetagsTypeDef", {"value": str}, total=False
)


class ClientCreateVirtualNodetagsTypeDef(
    _RequiredClientCreateVirtualNodetagsTypeDef,
    _OptionalClientCreateVirtualNodetagsTypeDef,
):
    """
    Type definition for `ClientCreateVirtualNode` `tags`

    Optional metadata that you apply to a resource to assist with categorization and organization.
    Each tag consists of a key and an optional value, both of which you define. Tag keys can have a
    maximum character length of 128 characters, and tag values can have a maximum length of 256
    characters.

    - **key** *(string) --* **[REQUIRED]**

      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
      a category for more specific tag values.

    - **value** *(string) --*

      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
      within a tag category (key).
    """


_ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef(
    _ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef
):
    """
    Type definition for `ClientCreateVirtualRouterResponsevirtualRouter` `metadata`

    The associated metadata for the virtual router.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": str},
    total=False,
)


class ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef(
    _ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
):
    """
    Type definition for `ClientCreateVirtualRouterResponsevirtualRouterspeclisteners` `portMapping`

    An object that represents a port mapping.

    - **port** *(integer) --*

      The port used for the port mapping.

    - **protocol** *(string) --*

      The protocol used for the port mapping. Specify one protocol.
    """


_ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    {
        "portMapping": ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
    },
    total=False,
)


class ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef(
    _ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef
):
    """
    Type definition for `ClientCreateVirtualRouterResponsevirtualRouterspec` `listeners`

    An object that represents a virtual router listener.

    - **portMapping** *(dict) --*

      An object that represents a port mapping.

      - **port** *(integer) --*

        The port used for the port mapping.

      - **protocol** *(string) --*

        The protocol used for the port mapping. Specify one protocol.
    """


_ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef",
    {
        "listeners": List[
            ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef
        ]
    },
    total=False,
)


class ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef(
    _ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef
):
    """
    Type definition for `ClientCreateVirtualRouterResponsevirtualRouter` `spec`

    The specifications of the virtual router.

    - **listeners** *(list) --*

      The listeners that the virtual router is expected to receive inbound traffic from. You
      can specify one listener.

      - *(dict) --*

        An object that represents a virtual router listener.

        - **portMapping** *(dict) --*

          An object that represents a port mapping.

          - **port** *(integer) --*

            The port used for the port mapping.

          - **protocol** *(string) --*

            The protocol used for the port mapping. Specify one protocol.
    """


_ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef",
    {"status": str},
    total=False,
)


class ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef(
    _ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef
):
    """
    Type definition for `ClientCreateVirtualRouterResponsevirtualRouter` `status`

    The current status of the virtual router.

    - **status** *(string) --*

      The current status of the virtual router.
    """


_ClientCreateVirtualRouterResponsevirtualRouterTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponsevirtualRouterTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef,
        "spec": ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef,
        "status": ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientCreateVirtualRouterResponsevirtualRouterTypeDef(
    _ClientCreateVirtualRouterResponsevirtualRouterTypeDef
):
    """
    Type definition for `ClientCreateVirtualRouterResponse` `virtualRouter`

    The full description of your virtual router following the create call.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual router resides in.

    - **metadata** *(dict) --*

      The associated metadata for the virtual router.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The specifications of the virtual router.

      - **listeners** *(list) --*

        The listeners that the virtual router is expected to receive inbound traffic from. You
        can specify one listener.

        - *(dict) --*

          An object that represents a virtual router listener.

          - **portMapping** *(dict) --*

            An object that represents a port mapping.

            - **port** *(integer) --*

              The port used for the port mapping.

            - **protocol** *(string) --*

              The protocol used for the port mapping. Specify one protocol.

    - **status** *(dict) --*

      The current status of the virtual router.

      - **status** *(string) --*

        The current status of the virtual router.

    - **virtualRouterName** *(string) --*

      The name of the virtual router.
    """


_ClientCreateVirtualRouterResponseTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponseTypeDef",
    {"virtualRouter": ClientCreateVirtualRouterResponsevirtualRouterTypeDef},
    total=False,
)


class ClientCreateVirtualRouterResponseTypeDef(
    _ClientCreateVirtualRouterResponseTypeDef
):
    """
    Type definition for `ClientCreateVirtualRouter` `Response`

    - **virtualRouter** *(dict) --*

      The full description of your virtual router following the create call.

      - **meshName** *(string) --*

        The name of the service mesh that the virtual router resides in.

      - **metadata** *(dict) --*

        The associated metadata for the virtual router.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The specifications of the virtual router.

        - **listeners** *(list) --*

          The listeners that the virtual router is expected to receive inbound traffic from. You
          can specify one listener.

          - *(dict) --*

            An object that represents a virtual router listener.

            - **portMapping** *(dict) --*

              An object that represents a port mapping.

              - **port** *(integer) --*

                The port used for the port mapping.

              - **protocol** *(string) --*

                The protocol used for the port mapping. Specify one protocol.

      - **status** *(dict) --*

        The current status of the virtual router.

        - **status** *(string) --*

          The current status of the virtual router.

      - **virtualRouterName** *(string) --*

        The name of the virtual router.
    """


_ClientCreateVirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "_ClientCreateVirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": str},
)


class ClientCreateVirtualRouterspeclistenersportMappingTypeDef(
    _ClientCreateVirtualRouterspeclistenersportMappingTypeDef
):
    """
    Type definition for `ClientCreateVirtualRouterspeclisteners` `portMapping`

    An object that represents a port mapping.

    - **port** *(integer) --* **[REQUIRED]**

      The port used for the port mapping.

    - **protocol** *(string) --* **[REQUIRED]**

      The protocol used for the port mapping. Specify one protocol.
    """


_ClientCreateVirtualRouterspeclistenersTypeDef = TypedDict(
    "_ClientCreateVirtualRouterspeclistenersTypeDef",
    {"portMapping": ClientCreateVirtualRouterspeclistenersportMappingTypeDef},
)


class ClientCreateVirtualRouterspeclistenersTypeDef(
    _ClientCreateVirtualRouterspeclistenersTypeDef
):
    """
    Type definition for `ClientCreateVirtualRouterspec` `listeners`

    An object that represents a virtual router listener.

    - **portMapping** *(dict) --* **[REQUIRED]**

      An object that represents a port mapping.

      - **port** *(integer) --* **[REQUIRED]**

        The port used for the port mapping.

      - **protocol** *(string) --* **[REQUIRED]**

        The protocol used for the port mapping. Specify one protocol.
    """


_ClientCreateVirtualRouterspecTypeDef = TypedDict(
    "_ClientCreateVirtualRouterspecTypeDef",
    {"listeners": List[ClientCreateVirtualRouterspeclistenersTypeDef]},
    total=False,
)


class ClientCreateVirtualRouterspecTypeDef(_ClientCreateVirtualRouterspecTypeDef):
    """
    Type definition for `ClientCreateVirtualRouter` `spec`

    The virtual router specification to apply.

    - **listeners** *(list) --*

      The listeners that the virtual router is expected to receive inbound traffic from. You can
      specify one listener.

      - *(dict) --*

        An object that represents a virtual router listener.

        - **portMapping** *(dict) --* **[REQUIRED]**

          An object that represents a port mapping.

          - **port** *(integer) --* **[REQUIRED]**

            The port used for the port mapping.

          - **protocol** *(string) --* **[REQUIRED]**

            The protocol used for the port mapping. Specify one protocol.
    """


_RequiredClientCreateVirtualRoutertagsTypeDef = TypedDict(
    "_RequiredClientCreateVirtualRoutertagsTypeDef", {"key": str}
)
_OptionalClientCreateVirtualRoutertagsTypeDef = TypedDict(
    "_OptionalClientCreateVirtualRoutertagsTypeDef", {"value": str}, total=False
)


class ClientCreateVirtualRoutertagsTypeDef(
    _RequiredClientCreateVirtualRoutertagsTypeDef,
    _OptionalClientCreateVirtualRoutertagsTypeDef,
):
    """
    Type definition for `ClientCreateVirtualRouter` `tags`

    Optional metadata that you apply to a resource to assist with categorization and organization.
    Each tag consists of a key and an optional value, both of which you define. Tag keys can have a
    maximum character length of 128 characters, and tag values can have a maximum length of 256
    characters.

    - **key** *(string) --* **[REQUIRED]**

      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
      a category for more specific tag values.

    - **value** *(string) --*

      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
      within a tag category (key).
    """


_ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef
):
    """
    Type definition for `ClientCreateVirtualServiceResponsevirtualService` `metadata`

    An object that represents metadata for a resource.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef
):
    """
    Type definition for `ClientCreateVirtualServiceResponsevirtualServicespecprovider` `virtualNode`

    The virtual node associated with a virtual service.

    - **virtualNodeName** *(string) --*

      The name of the virtual node that is acting as a service provider.
    """


_ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef
):
    """
    Type definition for `ClientCreateVirtualServiceResponsevirtualServicespecprovider` `virtualRouter`

    The virtual router associated with a virtual service.

    - **virtualRouterName** *(string) --*

      The name of the virtual router that is acting as a service provider.
    """


_ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef
):
    """
    Type definition for `ClientCreateVirtualServiceResponsevirtualServicespec` `provider`

    The App Mesh object that is acting as the provider for a virtual service. You can specify
    a single virtual node or virtual router.

    - **virtualNode** *(dict) --*

      The virtual node associated with a virtual service.

      - **virtualNodeName** *(string) --*

        The name of the virtual node that is acting as a service provider.

    - **virtualRouter** *(dict) --*

      The virtual router associated with a virtual service.

      - **virtualRouterName** *(string) --*

        The name of the virtual router that is acting as a service provider.
    """


_ClientCreateVirtualServiceResponsevirtualServicespecTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServicespecTypeDef",
    {"provider": ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef},
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServicespecTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServicespecTypeDef
):
    """
    Type definition for `ClientCreateVirtualServiceResponsevirtualService` `spec`

    The specifications of the virtual service.

    - **provider** *(dict) --*

      The App Mesh object that is acting as the provider for a virtual service. You can specify
      a single virtual node or virtual router.

      - **virtualNode** *(dict) --*

        The virtual node associated with a virtual service.

        - **virtualNodeName** *(string) --*

          The name of the virtual node that is acting as a service provider.

      - **virtualRouter** *(dict) --*

        The virtual router associated with a virtual service.

        - **virtualRouterName** *(string) --*

          The name of the virtual router that is acting as a service provider.
    """


_ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef",
    {"status": str},
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef
):
    """
    Type definition for `ClientCreateVirtualServiceResponsevirtualService` `status`

    The current status of the virtual service.

    - **status** *(string) --*

      The current status of the virtual service.
    """


_ClientCreateVirtualServiceResponsevirtualServiceTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServiceTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef,
        "spec": ClientCreateVirtualServiceResponsevirtualServicespecTypeDef,
        "status": ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef,
        "virtualServiceName": str,
    },
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServiceTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServiceTypeDef
):
    """
    Type definition for `ClientCreateVirtualServiceResponse` `virtualService`

    The full description of your virtual service following the create call.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual service resides in.

    - **metadata** *(dict) --*

      An object that represents metadata for a resource.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The specifications of the virtual service.

      - **provider** *(dict) --*

        The App Mesh object that is acting as the provider for a virtual service. You can specify
        a single virtual node or virtual router.

        - **virtualNode** *(dict) --*

          The virtual node associated with a virtual service.

          - **virtualNodeName** *(string) --*

            The name of the virtual node that is acting as a service provider.

        - **virtualRouter** *(dict) --*

          The virtual router associated with a virtual service.

          - **virtualRouterName** *(string) --*

            The name of the virtual router that is acting as a service provider.

    - **status** *(dict) --*

      The current status of the virtual service.

      - **status** *(string) --*

        The current status of the virtual service.

    - **virtualServiceName** *(string) --*

      The name of the virtual service.
    """


_ClientCreateVirtualServiceResponseTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponseTypeDef",
    {"virtualService": ClientCreateVirtualServiceResponsevirtualServiceTypeDef},
    total=False,
)


class ClientCreateVirtualServiceResponseTypeDef(
    _ClientCreateVirtualServiceResponseTypeDef
):
    """
    Type definition for `ClientCreateVirtualService` `Response`

    - **virtualService** *(dict) --*

      The full description of your virtual service following the create call.

      - **meshName** *(string) --*

        The name of the service mesh that the virtual service resides in.

      - **metadata** *(dict) --*

        An object that represents metadata for a resource.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The specifications of the virtual service.

        - **provider** *(dict) --*

          The App Mesh object that is acting as the provider for a virtual service. You can specify
          a single virtual node or virtual router.

          - **virtualNode** *(dict) --*

            The virtual node associated with a virtual service.

            - **virtualNodeName** *(string) --*

              The name of the virtual node that is acting as a service provider.

          - **virtualRouter** *(dict) --*

            The virtual router associated with a virtual service.

            - **virtualRouterName** *(string) --*

              The name of the virtual router that is acting as a service provider.

      - **status** *(dict) --*

        The current status of the virtual service.

        - **status** *(string) --*

          The current status of the virtual service.

      - **virtualServiceName** *(string) --*

        The name of the virtual service.
    """


_ClientCreateVirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "_ClientCreateVirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
)


class ClientCreateVirtualServicespecprovidervirtualNodeTypeDef(
    _ClientCreateVirtualServicespecprovidervirtualNodeTypeDef
):
    """
    Type definition for `ClientCreateVirtualServicespecprovider` `virtualNode`

    The virtual node associated with a virtual service.

    - **virtualNodeName** *(string) --* **[REQUIRED]**

      The name of the virtual node that is acting as a service provider.
    """


_ClientCreateVirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "_ClientCreateVirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
)


class ClientCreateVirtualServicespecprovidervirtualRouterTypeDef(
    _ClientCreateVirtualServicespecprovidervirtualRouterTypeDef
):
    """
    Type definition for `ClientCreateVirtualServicespecprovider` `virtualRouter`

    The virtual router associated with a virtual service.

    - **virtualRouterName** *(string) --* **[REQUIRED]**

      The name of the virtual router that is acting as a service provider.
    """


_ClientCreateVirtualServicespecproviderTypeDef = TypedDict(
    "_ClientCreateVirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientCreateVirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientCreateVirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)


class ClientCreateVirtualServicespecproviderTypeDef(
    _ClientCreateVirtualServicespecproviderTypeDef
):
    """
    Type definition for `ClientCreateVirtualServicespec` `provider`

    The App Mesh object that is acting as the provider for a virtual service. You can specify a
    single virtual node or virtual router.

    - **virtualNode** *(dict) --*

      The virtual node associated with a virtual service.

      - **virtualNodeName** *(string) --* **[REQUIRED]**

        The name of the virtual node that is acting as a service provider.

    - **virtualRouter** *(dict) --*

      The virtual router associated with a virtual service.

      - **virtualRouterName** *(string) --* **[REQUIRED]**

        The name of the virtual router that is acting as a service provider.
    """


_ClientCreateVirtualServicespecTypeDef = TypedDict(
    "_ClientCreateVirtualServicespecTypeDef",
    {"provider": ClientCreateVirtualServicespecproviderTypeDef},
    total=False,
)


class ClientCreateVirtualServicespecTypeDef(_ClientCreateVirtualServicespecTypeDef):
    """
    Type definition for `ClientCreateVirtualService` `spec`

    The virtual service specification to apply.

    - **provider** *(dict) --*

      The App Mesh object that is acting as the provider for a virtual service. You can specify a
      single virtual node or virtual router.

      - **virtualNode** *(dict) --*

        The virtual node associated with a virtual service.

        - **virtualNodeName** *(string) --* **[REQUIRED]**

          The name of the virtual node that is acting as a service provider.

      - **virtualRouter** *(dict) --*

        The virtual router associated with a virtual service.

        - **virtualRouterName** *(string) --* **[REQUIRED]**

          The name of the virtual router that is acting as a service provider.
    """


_RequiredClientCreateVirtualServicetagsTypeDef = TypedDict(
    "_RequiredClientCreateVirtualServicetagsTypeDef", {"key": str}
)
_OptionalClientCreateVirtualServicetagsTypeDef = TypedDict(
    "_OptionalClientCreateVirtualServicetagsTypeDef", {"value": str}, total=False
)


class ClientCreateVirtualServicetagsTypeDef(
    _RequiredClientCreateVirtualServicetagsTypeDef,
    _OptionalClientCreateVirtualServicetagsTypeDef,
):
    """
    Type definition for `ClientCreateVirtualService` `tags`

    Optional metadata that you apply to a resource to assist with categorization and organization.
    Each tag consists of a key and an optional value, both of which you define. Tag keys can have a
    maximum character length of 128 characters, and tag values can have a maximum length of 256
    characters.

    - **key** *(string) --* **[REQUIRED]**

      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
      a category for more specific tag values.

    - **value** *(string) --*

      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
      within a tag category (key).
    """


_ClientDeleteMeshResponsemeshmetadataTypeDef = TypedDict(
    "_ClientDeleteMeshResponsemeshmetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientDeleteMeshResponsemeshmetadataTypeDef(
    _ClientDeleteMeshResponsemeshmetadataTypeDef
):
    """
    Type definition for `ClientDeleteMeshResponsemesh` `metadata`

    The associated metadata for the service mesh.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientDeleteMeshResponsemeshspecegressFilterTypeDef = TypedDict(
    "_ClientDeleteMeshResponsemeshspecegressFilterTypeDef", {"type": str}, total=False
)


class ClientDeleteMeshResponsemeshspecegressFilterTypeDef(
    _ClientDeleteMeshResponsemeshspecegressFilterTypeDef
):
    """
    Type definition for `ClientDeleteMeshResponsemeshspec` `egressFilter`

    The egress filter rules for the service mesh.

    - **type** *(string) --*

      The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
      from virtual nodes to other defined resources in the service mesh (and any traffic to
      ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
      ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientDeleteMeshResponsemeshspecTypeDef = TypedDict(
    "_ClientDeleteMeshResponsemeshspecTypeDef",
    {"egressFilter": ClientDeleteMeshResponsemeshspecegressFilterTypeDef},
    total=False,
)


class ClientDeleteMeshResponsemeshspecTypeDef(_ClientDeleteMeshResponsemeshspecTypeDef):
    """
    Type definition for `ClientDeleteMeshResponsemesh` `spec`

    The associated specification for the service mesh.

    - **egressFilter** *(dict) --*

      The egress filter rules for the service mesh.

      - **type** *(string) --*

        The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
        from virtual nodes to other defined resources in the service mesh (and any traffic to
        ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
        ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientDeleteMeshResponsemeshstatusTypeDef = TypedDict(
    "_ClientDeleteMeshResponsemeshstatusTypeDef", {"status": str}, total=False
)


class ClientDeleteMeshResponsemeshstatusTypeDef(
    _ClientDeleteMeshResponsemeshstatusTypeDef
):
    """
    Type definition for `ClientDeleteMeshResponsemesh` `status`

    The status of the service mesh.

    - **status** *(string) --*

      The current mesh status.
    """


_ClientDeleteMeshResponsemeshTypeDef = TypedDict(
    "_ClientDeleteMeshResponsemeshTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteMeshResponsemeshmetadataTypeDef,
        "spec": ClientDeleteMeshResponsemeshspecTypeDef,
        "status": ClientDeleteMeshResponsemeshstatusTypeDef,
    },
    total=False,
)


class ClientDeleteMeshResponsemeshTypeDef(_ClientDeleteMeshResponsemeshTypeDef):
    """
    Type definition for `ClientDeleteMeshResponse` `mesh`

    The service mesh that was deleted.

    - **meshName** *(string) --*

      The name of the service mesh.

    - **metadata** *(dict) --*

      The associated metadata for the service mesh.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The associated specification for the service mesh.

      - **egressFilter** *(dict) --*

        The egress filter rules for the service mesh.

        - **type** *(string) --*

          The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
          from virtual nodes to other defined resources in the service mesh (and any traffic to
          ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
          ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.

    - **status** *(dict) --*

      The status of the service mesh.

      - **status** *(string) --*

        The current mesh status.
    """


_ClientDeleteMeshResponseTypeDef = TypedDict(
    "_ClientDeleteMeshResponseTypeDef",
    {"mesh": ClientDeleteMeshResponsemeshTypeDef},
    total=False,
)


class ClientDeleteMeshResponseTypeDef(_ClientDeleteMeshResponseTypeDef):
    """
    Type definition for `ClientDeleteMesh` `Response`

    - **mesh** *(dict) --*

      The service mesh that was deleted.

      - **meshName** *(string) --*

        The name of the service mesh.

      - **metadata** *(dict) --*

        The associated metadata for the service mesh.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The associated specification for the service mesh.

        - **egressFilter** *(dict) --*

          The egress filter rules for the service mesh.

          - **type** *(string) --*

            The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
            from virtual nodes to other defined resources in the service mesh (and any traffic to
            ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
            ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.

      - **status** *(dict) --*

        The status of the service mesh.

        - **status** *(string) --*

          The current mesh status.
    """


_ClientDeleteRouteResponseroutemetadataTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutemetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientDeleteRouteResponseroutemetadataTypeDef(
    _ClientDeleteRouteResponseroutemetadataTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroute` `metadata`

    The associated metadata for the route.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespecgrpcRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespecgrpcRoute` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --*

      The end of the range.

    - **start** *(integer) --*

      The start of the range.
    """


_ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespecgrpcRoutematchmetadata` `match`

    An object that represents the data to match from the request.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --*

        The end of the range.

      - **start** *(integer) --*

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    {
        "invert": bool,
        "match": ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespecgrpcRoutematch` `metadata`

    An object that represents the match metadata for the route.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value
      is ``False`` .

    - **match** *(dict) --*

      An object that represents the data to match from the request.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --*

          The end of the range.

        - **start** *(integer) --*

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --*

      The name of the route.
    """


_ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[
            ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef
        ],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespecgrpcRoute` `match`

    An object that represents the criteria for determining a request match.

    - **metadata** *(list) --*

      An object that represents the data to match from the request.

      - *(dict) --*

        An object that represents the match metadata for the route.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value
          is ``False`` .

        - **match** *(dict) --*

          An object that represents the data to match from the request.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --*

              The end of the range.

            - **start** *(integer) --*

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --*

          The name of the route.

    - **methodName** *(string) --*

      The method name to match from the request. If you specify a name, you must also
      specify a ``serviceName`` .

    - **serviceName** *(string) --*

      The fully qualified domain name for the service to match from the request.
    """


_ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespecgrpcRouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[str],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespecgrpcRoute` `retryPolicy`

    An object that represents a retry policy.

    - **grpcRetryEvents** *(list) --*

      Specify at least one of the valid values.

      - *(string) --*

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
      510, and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --*

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --*

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_ClientDeleteRouteResponseroutespecgrpcRouteTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRouteTypeDef",
    {
        "action": ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef,
        "match": ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef,
        "retryPolicy": ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRouteTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRouteTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespec` `grpcRoute`

    An object that represents the specification of a GRPC route.

    - **action** *(dict) --*

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.

    - **match** *(dict) --*

      An object that represents the criteria for determining a request match.

      - **metadata** *(list) --*

        An object that represents the data to match from the request.

        - *(dict) --*

          An object that represents the match metadata for the route.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value
            is ``False`` .

          - **match** *(dict) --*

            An object that represents the data to match from the request.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --*

                The end of the range.

              - **start** *(integer) --*

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --*

            The name of the route.

      - **methodName** *(string) --*

        The method name to match from the request. If you specify a name, you must also
        specify a ``serviceName`` .

      - **serviceName** *(string) --*

        The fully qualified domain name for the service to match from the request.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **grpcRetryEvents** *(list) --*

        Specify at least one of the valid values.

        - *(string) --*

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
        510, and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --*

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --*

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttp2Routeaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttp2Route` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttp2Routematchheadersmatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --*

      The end of the range.

    - **start** *(integer) --*

      The start of the range.
    """


_ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttp2Routematchheaders` `match`

    The ``HeaderMatchMethod`` object.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --*

        The end of the range.

      - **start** *(integer) --*

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttp2Routematch` `headers`

    An object that represents the HTTP header in the request.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value
      is ``False`` .

    - **match** *(dict) --*

      The ``HeaderMatchMethod`` object.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --*

          The end of the range.

        - **start** *(integer) --*

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --*

      A name for the HTTP header in the client request that will be matched on.
    """


_ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef",
    {
        "headers": List[
            ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef
        ],
        "method": str,
        "prefix": str,
        "scheme": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttp2Route` `match`

    An object that represents the criteria for determining a request match.

    - **headers** *(list) --*

      An object that represents the client request headers to match on.

      - *(dict) --*

        An object that represents the HTTP header in the request.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value
          is ``False`` .

        - **match** *(dict) --*

          The ``HeaderMatchMethod`` object.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --*

              The end of the range.

            - **start** *(integer) --*

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --*

          A name for the HTTP header in the client request that will be matched on.

    - **method** *(string) --*

      The client request method to match on. Specify only one.

    - **prefix** *(string) --*

      Specifies the path to match requests with. This parameter must always start with
      ``/`` , which by itself matches all requests to the virtual service name. You can
      also match for path-based routing of requests. For example, if your virtual service
      name is ``my-service.local`` and you want the route to match requests to
      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

    - **scheme** *(string) --*

      The client request scheme to match on. Specify only one.
    """


_ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttp2RouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttp2Route` `retryPolicy`

    An object that represents a retry policy.

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
      510, and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --*

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --*

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_ClientDeleteRouteResponseroutespechttp2RouteTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RouteTypeDef",
    {
        "action": ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef,
        "match": ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef,
        "retryPolicy": ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RouteTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RouteTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespec` `http2Route`

    An object that represents the specification of an HTTP2 route.

    - **action** *(dict) --*

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.

    - **match** *(dict) --*

      An object that represents the criteria for determining a request match.

      - **headers** *(list) --*

        An object that represents the client request headers to match on.

        - *(dict) --*

          An object that represents the HTTP header in the request.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value
            is ``False`` .

          - **match** *(dict) --*

            The ``HeaderMatchMethod`` object.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --*

                The end of the range.

              - **start** *(integer) --*

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --*

            A name for the HTTP header in the client request that will be matched on.

      - **method** *(string) --*

        The client request method to match on. Specify only one.

      - **prefix** *(string) --*

        Specifies the path to match requests with. This parameter must always start with
        ``/`` , which by itself matches all requests to the virtual service name. You can
        also match for path-based routing of requests. For example, if your virtual service
        name is ``my-service.local`` and you want the route to match requests to
        ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

      - **scheme** *(string) --*

        The client request scheme to match on. Specify only one.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
        510, and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --*

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --*

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef(
    _ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttpRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientDeleteRouteResponseroutespechttpRouteactionTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRouteactionTypeDef(
    _ClientDeleteRouteResponseroutespechttpRouteactionTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttpRoute` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef(
    _ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttpRoutematchheadersmatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --*

      The end of the range.

    - **start** *(integer) --*

      The start of the range.
    """


_ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef(
    _ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttpRoutematchheaders` `match`

    The ``HeaderMatchMethod`` object.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --*

        The end of the range.

      - **start** *(integer) --*

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef(
    _ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttpRoutematch` `headers`

    An object that represents the HTTP header in the request.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value
      is ``False`` .

    - **match** *(dict) --*

      The ``HeaderMatchMethod`` object.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --*

          The end of the range.

        - **start** *(integer) --*

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --*

      A name for the HTTP header in the client request that will be matched on.
    """


_ClientDeleteRouteResponseroutespechttpRoutematchTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRoutematchTypeDef",
    {
        "headers": List[ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef],
        "method": str,
        "prefix": str,
        "scheme": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRoutematchTypeDef(
    _ClientDeleteRouteResponseroutespechttpRoutematchTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttpRoute` `match`

    An object that represents the criteria for determining a request match.

    - **headers** *(list) --*

      An object that represents the client request headers to match on.

      - *(dict) --*

        An object that represents the HTTP header in the request.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value
          is ``False`` .

        - **match** *(dict) --*

          The ``HeaderMatchMethod`` object.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --*

              The end of the range.

            - **start** *(integer) --*

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --*

          A name for the HTTP header in the client request that will be matched on.

    - **method** *(string) --*

      The client request method to match on. Specify only one.

    - **prefix** *(string) --*

      Specifies the path to match requests with. This parameter must always start with
      ``/`` , which by itself matches all requests to the virtual service name. You can
      also match for path-based routing of requests. For example, if your virtual service
      name is ``my-service.local`` and you want the route to match requests to
      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

    - **scheme** *(string) --*

      The client request scheme to match on. Specify only one.
    """


_ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttpRouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef(
    _ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespechttpRoute` `retryPolicy`

    An object that represents a retry policy.

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
      510, and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --*

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --*

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_ClientDeleteRouteResponseroutespechttpRouteTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRouteTypeDef",
    {
        "action": ClientDeleteRouteResponseroutespechttpRouteactionTypeDef,
        "match": ClientDeleteRouteResponseroutespechttpRoutematchTypeDef,
        "retryPolicy": ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRouteTypeDef(
    _ClientDeleteRouteResponseroutespechttpRouteTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespec` `httpRoute`

    An object that represents the specification of an HTTP route.

    - **action** *(dict) --*

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.

    - **match** *(dict) --*

      An object that represents the criteria for determining a request match.

      - **headers** *(list) --*

        An object that represents the client request headers to match on.

        - *(dict) --*

          An object that represents the HTTP header in the request.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value
            is ``False`` .

          - **match** *(dict) --*

            The ``HeaderMatchMethod`` object.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --*

                The end of the range.

              - **start** *(integer) --*

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --*

            A name for the HTTP header in the client request that will be matched on.

      - **method** *(string) --*

        The client request method to match on. Specify only one.

      - **prefix** *(string) --*

        Specifies the path to match requests with. This parameter must always start with
        ``/`` , which by itself matches all requests to the virtual service name. You can
        also match for path-based routing of requests. For example, if your virtual service
        name is ``my-service.local`` and you want the route to match requests to
        ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

      - **scheme** *(string) --*

        The client request scheme to match on. Specify only one.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
        510, and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --*

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --*

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef(
    _ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespectcpRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientDeleteRouteResponseroutespectcpRouteactionTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDeleteRouteResponseroutespectcpRouteactionTypeDef(
    _ClientDeleteRouteResponseroutespectcpRouteactionTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespectcpRoute` `action`

    The action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientDeleteRouteResponseroutespectcpRouteTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespectcpRouteTypeDef",
    {"action": ClientDeleteRouteResponseroutespectcpRouteactionTypeDef},
    total=False,
)


class ClientDeleteRouteResponseroutespectcpRouteTypeDef(
    _ClientDeleteRouteResponseroutespectcpRouteTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroutespec` `tcpRoute`

    An object that represents the specification of a TCP route.

    - **action** *(dict) --*

      The action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.
    """


_ClientDeleteRouteResponseroutespecTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecTypeDef",
    {
        "grpcRoute": ClientDeleteRouteResponseroutespecgrpcRouteTypeDef,
        "http2Route": ClientDeleteRouteResponseroutespechttp2RouteTypeDef,
        "httpRoute": ClientDeleteRouteResponseroutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientDeleteRouteResponseroutespectcpRouteTypeDef,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecTypeDef(
    _ClientDeleteRouteResponseroutespecTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroute` `spec`

    The specifications of the route.

    - **grpcRoute** *(dict) --*

      An object that represents the specification of a GRPC route.

      - **action** *(dict) --*

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.

      - **match** *(dict) --*

        An object that represents the criteria for determining a request match.

        - **metadata** *(list) --*

          An object that represents the data to match from the request.

          - *(dict) --*

            An object that represents the match metadata for the route.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value
              is ``False`` .

            - **match** *(dict) --*

              An object that represents the data to match from the request.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --*

                  The end of the range.

                - **start** *(integer) --*

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --*

              The name of the route.

        - **methodName** *(string) --*

          The method name to match from the request. If you specify a name, you must also
          specify a ``serviceName`` .

        - **serviceName** *(string) --*

          The fully qualified domain name for the service to match from the request.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **grpcRetryEvents** *(list) --*

          Specify at least one of the valid values.

          - *(string) --*

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
          510, and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --*

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --*

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **http2Route** *(dict) --*

      An object that represents the specification of an HTTP2 route.

      - **action** *(dict) --*

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.

      - **match** *(dict) --*

        An object that represents the criteria for determining a request match.

        - **headers** *(list) --*

          An object that represents the client request headers to match on.

          - *(dict) --*

            An object that represents the HTTP header in the request.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value
              is ``False`` .

            - **match** *(dict) --*

              The ``HeaderMatchMethod`` object.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --*

                  The end of the range.

                - **start** *(integer) --*

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --*

              A name for the HTTP header in the client request that will be matched on.

        - **method** *(string) --*

          The client request method to match on. Specify only one.

        - **prefix** *(string) --*

          Specifies the path to match requests with. This parameter must always start with
          ``/`` , which by itself matches all requests to the virtual service name. You can
          also match for path-based routing of requests. For example, if your virtual service
          name is ``my-service.local`` and you want the route to match requests to
          ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

        - **scheme** *(string) --*

          The client request scheme to match on. Specify only one.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
          510, and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --*

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --*

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **httpRoute** *(dict) --*

      An object that represents the specification of an HTTP route.

      - **action** *(dict) --*

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.

      - **match** *(dict) --*

        An object that represents the criteria for determining a request match.

        - **headers** *(list) --*

          An object that represents the client request headers to match on.

          - *(dict) --*

            An object that represents the HTTP header in the request.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value
              is ``False`` .

            - **match** *(dict) --*

              The ``HeaderMatchMethod`` object.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --*

                  The end of the range.

                - **start** *(integer) --*

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --*

              A name for the HTTP header in the client request that will be matched on.

        - **method** *(string) --*

          The client request method to match on. Specify only one.

        - **prefix** *(string) --*

          Specifies the path to match requests with. This parameter must always start with
          ``/`` , which by itself matches all requests to the virtual service name. You can
          also match for path-based routing of requests. For example, if your virtual service
          name is ``my-service.local`` and you want the route to match requests to
          ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

        - **scheme** *(string) --*

          The client request scheme to match on. Specify only one.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
          510, and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --*

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --*

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **priority** *(integer) --*

      The priority for the route. Routes are matched based on the specified value, where 0 is
      the highest priority.

    - **tcpRoute** *(dict) --*

      An object that represents the specification of a TCP route.

      - **action** *(dict) --*

        The action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.
    """


_ClientDeleteRouteResponseroutestatusTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutestatusTypeDef", {"status": str}, total=False
)


class ClientDeleteRouteResponseroutestatusTypeDef(
    _ClientDeleteRouteResponseroutestatusTypeDef
):
    """
    Type definition for `ClientDeleteRouteResponseroute` `status`

    The status of the route.

    - **status** *(string) --*

      The current status for the route.
    """


_ClientDeleteRouteResponserouteTypeDef = TypedDict(
    "_ClientDeleteRouteResponserouteTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteRouteResponseroutemetadataTypeDef,
        "routeName": str,
        "spec": ClientDeleteRouteResponseroutespecTypeDef,
        "status": ClientDeleteRouteResponseroutestatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientDeleteRouteResponserouteTypeDef(_ClientDeleteRouteResponserouteTypeDef):
    """
    Type definition for `ClientDeleteRouteResponse` `route`

    The route that was deleted.

    - **meshName** *(string) --*

      The name of the service mesh that the route resides in.

    - **metadata** *(dict) --*

      The associated metadata for the route.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **routeName** *(string) --*

      The name of the route.

    - **spec** *(dict) --*

      The specifications of the route.

      - **grpcRoute** *(dict) --*

        An object that represents the specification of a GRPC route.

        - **action** *(dict) --*

          An object that represents the action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

        - **match** *(dict) --*

          An object that represents the criteria for determining a request match.

          - **metadata** *(list) --*

            An object that represents the data to match from the request.

            - *(dict) --*

              An object that represents the match metadata for the route.

              - **invert** *(boolean) --*

                Specify ``True`` to match anything except the match criteria. The default value
                is ``False`` .

              - **match** *(dict) --*

                An object that represents the data to match from the request.

                - **exact** *(string) --*

                  The value sent by the client must match the specified value exactly.

                - **prefix** *(string) --*

                  The value sent by the client must begin with the specified characters.

                - **range** *(dict) --*

                  An object that represents the range of values to match on.

                  - **end** *(integer) --*

                    The end of the range.

                  - **start** *(integer) --*

                    The start of the range.

                - **regex** *(string) --*

                  The value sent by the client must include the specified characters.

                - **suffix** *(string) --*

                  The value sent by the client must end with the specified characters.

              - **name** *(string) --*

                The name of the route.

          - **methodName** *(string) --*

            The method name to match from the request. If you specify a name, you must also
            specify a ``serviceName`` .

          - **serviceName** *(string) --*

            The fully qualified domain name for the service to match from the request.

        - **retryPolicy** *(dict) --*

          An object that represents a retry policy.

          - **grpcRetryEvents** *(list) --*

            Specify at least one of the valid values.

            - *(string) --*

          - **httpRetryEvents** *(list) --*

            Specify at least one of the following values.

            * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
            510, and 511

            * **gateway-error** – HTTP status codes 502, 503, and 504

            * **client-error** – HTTP status code 409

            * **stream-error** – Retry on refused stream

            - *(string) --*

          - **maxRetries** *(integer) --*

            The maximum number of retry attempts.

          - **perRetryTimeout** *(dict) --*

            An object that represents a duration of time.

            - **unit** *(string) --*

              A unit of time.

            - **value** *(integer) --*

              A number of time units.

          - **tcpRetryEvents** *(list) --*

            Specify a valid value.

            - *(string) --*

      - **http2Route** *(dict) --*

        An object that represents the specification of an HTTP2 route.

        - **action** *(dict) --*

          An object that represents the action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

        - **match** *(dict) --*

          An object that represents the criteria for determining a request match.

          - **headers** *(list) --*

            An object that represents the client request headers to match on.

            - *(dict) --*

              An object that represents the HTTP header in the request.

              - **invert** *(boolean) --*

                Specify ``True`` to match anything except the match criteria. The default value
                is ``False`` .

              - **match** *(dict) --*

                The ``HeaderMatchMethod`` object.

                - **exact** *(string) --*

                  The value sent by the client must match the specified value exactly.

                - **prefix** *(string) --*

                  The value sent by the client must begin with the specified characters.

                - **range** *(dict) --*

                  An object that represents the range of values to match on.

                  - **end** *(integer) --*

                    The end of the range.

                  - **start** *(integer) --*

                    The start of the range.

                - **regex** *(string) --*

                  The value sent by the client must include the specified characters.

                - **suffix** *(string) --*

                  The value sent by the client must end with the specified characters.

              - **name** *(string) --*

                A name for the HTTP header in the client request that will be matched on.

          - **method** *(string) --*

            The client request method to match on. Specify only one.

          - **prefix** *(string) --*

            Specifies the path to match requests with. This parameter must always start with
            ``/`` , which by itself matches all requests to the virtual service name. You can
            also match for path-based routing of requests. For example, if your virtual service
            name is ``my-service.local`` and you want the route to match requests to
            ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

          - **scheme** *(string) --*

            The client request scheme to match on. Specify only one.

        - **retryPolicy** *(dict) --*

          An object that represents a retry policy.

          - **httpRetryEvents** *(list) --*

            Specify at least one of the following values.

            * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
            510, and 511

            * **gateway-error** – HTTP status codes 502, 503, and 504

            * **client-error** – HTTP status code 409

            * **stream-error** – Retry on refused stream

            - *(string) --*

          - **maxRetries** *(integer) --*

            The maximum number of retry attempts.

          - **perRetryTimeout** *(dict) --*

            An object that represents a duration of time.

            - **unit** *(string) --*

              A unit of time.

            - **value** *(integer) --*

              A number of time units.

          - **tcpRetryEvents** *(list) --*

            Specify a valid value.

            - *(string) --*

      - **httpRoute** *(dict) --*

        An object that represents the specification of an HTTP route.

        - **action** *(dict) --*

          An object that represents the action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

        - **match** *(dict) --*

          An object that represents the criteria for determining a request match.

          - **headers** *(list) --*

            An object that represents the client request headers to match on.

            - *(dict) --*

              An object that represents the HTTP header in the request.

              - **invert** *(boolean) --*

                Specify ``True`` to match anything except the match criteria. The default value
                is ``False`` .

              - **match** *(dict) --*

                The ``HeaderMatchMethod`` object.

                - **exact** *(string) --*

                  The value sent by the client must match the specified value exactly.

                - **prefix** *(string) --*

                  The value sent by the client must begin with the specified characters.

                - **range** *(dict) --*

                  An object that represents the range of values to match on.

                  - **end** *(integer) --*

                    The end of the range.

                  - **start** *(integer) --*

                    The start of the range.

                - **regex** *(string) --*

                  The value sent by the client must include the specified characters.

                - **suffix** *(string) --*

                  The value sent by the client must end with the specified characters.

              - **name** *(string) --*

                A name for the HTTP header in the client request that will be matched on.

          - **method** *(string) --*

            The client request method to match on. Specify only one.

          - **prefix** *(string) --*

            Specifies the path to match requests with. This parameter must always start with
            ``/`` , which by itself matches all requests to the virtual service name. You can
            also match for path-based routing of requests. For example, if your virtual service
            name is ``my-service.local`` and you want the route to match requests to
            ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

          - **scheme** *(string) --*

            The client request scheme to match on. Specify only one.

        - **retryPolicy** *(dict) --*

          An object that represents a retry policy.

          - **httpRetryEvents** *(list) --*

            Specify at least one of the following values.

            * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
            510, and 511

            * **gateway-error** – HTTP status codes 502, 503, and 504

            * **client-error** – HTTP status code 409

            * **stream-error** – Retry on refused stream

            - *(string) --*

          - **maxRetries** *(integer) --*

            The maximum number of retry attempts.

          - **perRetryTimeout** *(dict) --*

            An object that represents a duration of time.

            - **unit** *(string) --*

              A unit of time.

            - **value** *(integer) --*

              A number of time units.

          - **tcpRetryEvents** *(list) --*

            Specify a valid value.

            - *(string) --*

      - **priority** *(integer) --*

        The priority for the route. Routes are matched based on the specified value, where 0 is
        the highest priority.

      - **tcpRoute** *(dict) --*

        An object that represents the specification of a TCP route.

        - **action** *(dict) --*

          The action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

    - **status** *(dict) --*

      The status of the route.

      - **status** *(string) --*

        The current status for the route.

    - **virtualRouterName** *(string) --*

      The virtual router that the route is associated with.
    """


_ClientDeleteRouteResponseTypeDef = TypedDict(
    "_ClientDeleteRouteResponseTypeDef",
    {"route": ClientDeleteRouteResponserouteTypeDef},
    total=False,
)


class ClientDeleteRouteResponseTypeDef(_ClientDeleteRouteResponseTypeDef):
    """
    Type definition for `ClientDeleteRoute` `Response`

    - **route** *(dict) --*

      The route that was deleted.

      - **meshName** *(string) --*

        The name of the service mesh that the route resides in.

      - **metadata** *(dict) --*

        The associated metadata for the route.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **routeName** *(string) --*

        The name of the route.

      - **spec** *(dict) --*

        The specifications of the route.

        - **grpcRoute** *(dict) --*

          An object that represents the specification of a GRPC route.

          - **action** *(dict) --*

            An object that represents the action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

          - **match** *(dict) --*

            An object that represents the criteria for determining a request match.

            - **metadata** *(list) --*

              An object that represents the data to match from the request.

              - *(dict) --*

                An object that represents the match metadata for the route.

                - **invert** *(boolean) --*

                  Specify ``True`` to match anything except the match criteria. The default value
                  is ``False`` .

                - **match** *(dict) --*

                  An object that represents the data to match from the request.

                  - **exact** *(string) --*

                    The value sent by the client must match the specified value exactly.

                  - **prefix** *(string) --*

                    The value sent by the client must begin with the specified characters.

                  - **range** *(dict) --*

                    An object that represents the range of values to match on.

                    - **end** *(integer) --*

                      The end of the range.

                    - **start** *(integer) --*

                      The start of the range.

                  - **regex** *(string) --*

                    The value sent by the client must include the specified characters.

                  - **suffix** *(string) --*

                    The value sent by the client must end with the specified characters.

                - **name** *(string) --*

                  The name of the route.

            - **methodName** *(string) --*

              The method name to match from the request. If you specify a name, you must also
              specify a ``serviceName`` .

            - **serviceName** *(string) --*

              The fully qualified domain name for the service to match from the request.

          - **retryPolicy** *(dict) --*

            An object that represents a retry policy.

            - **grpcRetryEvents** *(list) --*

              Specify at least one of the valid values.

              - *(string) --*

            - **httpRetryEvents** *(list) --*

              Specify at least one of the following values.

              * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
              510, and 511

              * **gateway-error** – HTTP status codes 502, 503, and 504

              * **client-error** – HTTP status code 409

              * **stream-error** – Retry on refused stream

              - *(string) --*

            - **maxRetries** *(integer) --*

              The maximum number of retry attempts.

            - **perRetryTimeout** *(dict) --*

              An object that represents a duration of time.

              - **unit** *(string) --*

                A unit of time.

              - **value** *(integer) --*

                A number of time units.

            - **tcpRetryEvents** *(list) --*

              Specify a valid value.

              - *(string) --*

        - **http2Route** *(dict) --*

          An object that represents the specification of an HTTP2 route.

          - **action** *(dict) --*

            An object that represents the action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

          - **match** *(dict) --*

            An object that represents the criteria for determining a request match.

            - **headers** *(list) --*

              An object that represents the client request headers to match on.

              - *(dict) --*

                An object that represents the HTTP header in the request.

                - **invert** *(boolean) --*

                  Specify ``True`` to match anything except the match criteria. The default value
                  is ``False`` .

                - **match** *(dict) --*

                  The ``HeaderMatchMethod`` object.

                  - **exact** *(string) --*

                    The value sent by the client must match the specified value exactly.

                  - **prefix** *(string) --*

                    The value sent by the client must begin with the specified characters.

                  - **range** *(dict) --*

                    An object that represents the range of values to match on.

                    - **end** *(integer) --*

                      The end of the range.

                    - **start** *(integer) --*

                      The start of the range.

                  - **regex** *(string) --*

                    The value sent by the client must include the specified characters.

                  - **suffix** *(string) --*

                    The value sent by the client must end with the specified characters.

                - **name** *(string) --*

                  A name for the HTTP header in the client request that will be matched on.

            - **method** *(string) --*

              The client request method to match on. Specify only one.

            - **prefix** *(string) --*

              Specifies the path to match requests with. This parameter must always start with
              ``/`` , which by itself matches all requests to the virtual service name. You can
              also match for path-based routing of requests. For example, if your virtual service
              name is ``my-service.local`` and you want the route to match requests to
              ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

            - **scheme** *(string) --*

              The client request scheme to match on. Specify only one.

          - **retryPolicy** *(dict) --*

            An object that represents a retry policy.

            - **httpRetryEvents** *(list) --*

              Specify at least one of the following values.

              * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
              510, and 511

              * **gateway-error** – HTTP status codes 502, 503, and 504

              * **client-error** – HTTP status code 409

              * **stream-error** – Retry on refused stream

              - *(string) --*

            - **maxRetries** *(integer) --*

              The maximum number of retry attempts.

            - **perRetryTimeout** *(dict) --*

              An object that represents a duration of time.

              - **unit** *(string) --*

                A unit of time.

              - **value** *(integer) --*

                A number of time units.

            - **tcpRetryEvents** *(list) --*

              Specify a valid value.

              - *(string) --*

        - **httpRoute** *(dict) --*

          An object that represents the specification of an HTTP route.

          - **action** *(dict) --*

            An object that represents the action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

          - **match** *(dict) --*

            An object that represents the criteria for determining a request match.

            - **headers** *(list) --*

              An object that represents the client request headers to match on.

              - *(dict) --*

                An object that represents the HTTP header in the request.

                - **invert** *(boolean) --*

                  Specify ``True`` to match anything except the match criteria. The default value
                  is ``False`` .

                - **match** *(dict) --*

                  The ``HeaderMatchMethod`` object.

                  - **exact** *(string) --*

                    The value sent by the client must match the specified value exactly.

                  - **prefix** *(string) --*

                    The value sent by the client must begin with the specified characters.

                  - **range** *(dict) --*

                    An object that represents the range of values to match on.

                    - **end** *(integer) --*

                      The end of the range.

                    - **start** *(integer) --*

                      The start of the range.

                  - **regex** *(string) --*

                    The value sent by the client must include the specified characters.

                  - **suffix** *(string) --*

                    The value sent by the client must end with the specified characters.

                - **name** *(string) --*

                  A name for the HTTP header in the client request that will be matched on.

            - **method** *(string) --*

              The client request method to match on. Specify only one.

            - **prefix** *(string) --*

              Specifies the path to match requests with. This parameter must always start with
              ``/`` , which by itself matches all requests to the virtual service name. You can
              also match for path-based routing of requests. For example, if your virtual service
              name is ``my-service.local`` and you want the route to match requests to
              ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

            - **scheme** *(string) --*

              The client request scheme to match on. Specify only one.

          - **retryPolicy** *(dict) --*

            An object that represents a retry policy.

            - **httpRetryEvents** *(list) --*

              Specify at least one of the following values.

              * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
              510, and 511

              * **gateway-error** – HTTP status codes 502, 503, and 504

              * **client-error** – HTTP status code 409

              * **stream-error** – Retry on refused stream

              - *(string) --*

            - **maxRetries** *(integer) --*

              The maximum number of retry attempts.

            - **perRetryTimeout** *(dict) --*

              An object that represents a duration of time.

              - **unit** *(string) --*

                A unit of time.

              - **value** *(integer) --*

                A number of time units.

            - **tcpRetryEvents** *(list) --*

              Specify a valid value.

              - *(string) --*

        - **priority** *(integer) --*

          The priority for the route. Routes are matched based on the specified value, where 0 is
          the highest priority.

        - **tcpRoute** *(dict) --*

          An object that represents the specification of a TCP route.

          - **action** *(dict) --*

            The action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

      - **status** *(dict) --*

        The status of the route.

        - **status** *(string) --*

          The current status for the route.

      - **virtualRouterName** *(string) --*

        The virtual router that the route is associated with.
    """


_ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNode` `metadata`

    The associated metadata for the virtual node.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNodespecbackends` `virtualService`

    Specifies a virtual service to use as a backend for a virtual node.

    - **virtualServiceName** *(string) --*

      The name of the virtual service that is acting as a virtual node backend.
    """


_ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    {
        "virtualService": ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNodespec` `backends`

    An object that represents the backends that a virtual node is expected to send outbound
    traffic to.

    - **virtualService** *(dict) --*

      Specifies a virtual service to use as a backend for a virtual node.

      - **virtualServiceName** *(string) --*

        The name of the virtual service that is acting as a virtual node backend.
    """


_ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": str,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNodespeclisteners` `healthCheck`

    The health check information for the listener.

    - **healthyThreshold** *(integer) --*

      The number of consecutive successful health checks that must occur before declaring
      listener healthy.

    - **intervalMillis** *(integer) --*

      The time period in milliseconds between each health check execution.

    - **path** *(string) --*

      The destination path for the health check request. This is required only if the
      specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

    - **port** *(integer) --*

      The destination port for the health check request. This port must match the port
      defined in the  PortMapping for the listener.

    - **protocol** *(string) --*

      The protocol for the health check request.

    - **timeoutMillis** *(integer) --*

      The amount of time to wait when receiving a response from the health check, in
      milliseconds.

    - **unhealthyThreshold** *(integer) --*

      The number of consecutive failed health checks that must occur before declaring a
      virtual node unhealthy.
    """


_ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": str},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNodespeclisteners` `portMapping`

    The port mapping information for the listener.

    - **port** *(integer) --*

      The port used for the port mapping.

    - **protocol** *(string) --*

      The protocol used for the port mapping. Specify one protocol.
    """


_ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    {
        "healthCheck": ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef,
        "portMapping": ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef,
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNodespec` `listeners`

    An object that represents a listener for a virtual node.

    - **healthCheck** *(dict) --*

      The health check information for the listener.

      - **healthyThreshold** *(integer) --*

        The number of consecutive successful health checks that must occur before declaring
        listener healthy.

      - **intervalMillis** *(integer) --*

        The time period in milliseconds between each health check execution.

      - **path** *(string) --*

        The destination path for the health check request. This is required only if the
        specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

      - **port** *(integer) --*

        The destination port for the health check request. This port must match the port
        defined in the  PortMapping for the listener.

      - **protocol** *(string) --*

        The protocol for the health check request.

      - **timeoutMillis** *(integer) --*

        The amount of time to wait when receiving a response from the health check, in
        milliseconds.

      - **unhealthyThreshold** *(integer) --*

        The number of consecutive failed health checks that must occur before declaring a
        virtual node unhealthy.

    - **portMapping** *(dict) --*

      The port mapping information for the listener.

      - **port** *(integer) --*

        The port used for the port mapping.

      - **protocol** *(string) --*

        The protocol used for the port mapping. Specify one protocol.
    """


_ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    {"path": str},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLog` `file`

    The file object to send virtual node access logs to.

    - **path** *(string) --*

      The file path to write access logs to. You can use ``/dev/stdout`` to send access
      logs to standard out and configure your Envoy container to use a log driver, such
      as ``awslogs`` , to export the access logs to a log storage service such as Amazon
      CloudWatch Logs. You can also specify a path in the Envoy container's file system
      to write the files to disk.

      .. note::

        The Envoy process must have write permissions to the path that you specify here.
        Otherwise, Envoy fails to bootstrap properly.
    """


_ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    {"file": ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNodespeclogging` `accessLog`

    The access log configuration for a virtual node.

    - **file** *(dict) --*

      The file object to send virtual node access logs to.

      - **path** *(string) --*

        The file path to write access logs to. You can use ``/dev/stdout`` to send access
        logs to standard out and configure your Envoy container to use a log driver, such
        as ``awslogs`` , to export the access logs to a log storage service such as Amazon
        CloudWatch Logs. You can also specify a path in the Envoy container's file system
        to write the files to disk.

        .. note::

          The Envoy process must have write permissions to the path that you specify here.
          Otherwise, Envoy fails to bootstrap properly.
    """


_ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef",
    {
        "accessLog": ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNodespec` `logging`

    The inbound and outbound access logging information for the virtual node.

    - **accessLog** *(dict) --*

      The access log configuration for a virtual node.

      - **file** *(dict) --*

        The file object to send virtual node access logs to.

        - **path** *(string) --*

          The file path to write access logs to. You can use ``/dev/stdout`` to send access
          logs to standard out and configure your Envoy container to use a log driver, such
          as ``awslogs`` , to export the access logs to a log storage service such as Amazon
          CloudWatch Logs. You can also specify a path in the Envoy container's file system
          to write the files to disk.

          .. note::

            The Envoy process must have write permissions to the path that you specify here.
            Otherwise, Envoy fails to bootstrap properly.
    """


_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMap` `attributes`

    An object that represents the AWS Cloud Map attribute information for your virtual
    node.

    - **key** *(string) --*

      The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
      service instance that contains the specified key and value is returned.

    - **value** *(string) --*

      The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
      service instance that contains the specified key and value is returned.
    """


_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscovery` `awsCloudMap`

    Specifies any AWS Cloud Map information for the virtual node.

    - **attributes** *(list) --*

      A string map that contains attributes with values that you can use to filter
      instances by any custom attribute that you specified when you registered the
      instance. Only instances that match all of the specified key/value pairs will be
      returned.

      - *(dict) --*

        An object that represents the AWS Cloud Map attribute information for your virtual
        node.

        - **key** *(string) --*

          The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
          service instance that contains the specified key and value is returned.

        - **value** *(string) --*

          The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
          service instance that contains the specified key and value is returned.

    - **namespaceName** *(string) --*

      The name of the AWS Cloud Map namespace to use.

    - **serviceName** *(string) --*

      The name of the AWS Cloud Map service to use.
    """


_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    {"hostname": str},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscovery` `dns`

    Specifies the DNS information for the virtual node.

    - **hostname** *(string) --*

      Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNodespec` `serviceDiscovery`

    The service discovery information for the virtual node. If your virtual node does not
    expect ingress traffic, you can omit this parameter.

    - **awsCloudMap** *(dict) --*

      Specifies any AWS Cloud Map information for the virtual node.

      - **attributes** *(list) --*

        A string map that contains attributes with values that you can use to filter
        instances by any custom attribute that you specified when you registered the
        instance. Only instances that match all of the specified key/value pairs will be
        returned.

        - *(dict) --*

          An object that represents the AWS Cloud Map attribute information for your virtual
          node.

          - **key** *(string) --*

            The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
            service instance that contains the specified key and value is returned.

          - **value** *(string) --*

            The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
            service instance that contains the specified key and value is returned.

      - **namespaceName** *(string) --*

        The name of the AWS Cloud Map namespace to use.

      - **serviceName** *(string) --*

        The name of the AWS Cloud Map service to use.

    - **dns** *(dict) --*

      Specifies the DNS information for the virtual node.

      - **hostname** *(string) --*

        Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef",
    {
        "backends": List[ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef],
        "listeners": List[
            ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef
        ],
        "logging": ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNode` `spec`

    The specifications of the virtual node.

    - **backends** *(list) --*

      The backends that the virtual node is expected to send outbound traffic to.

      - *(dict) --*

        An object that represents the backends that a virtual node is expected to send outbound
        traffic to.

        - **virtualService** *(dict) --*

          Specifies a virtual service to use as a backend for a virtual node.

          - **virtualServiceName** *(string) --*

            The name of the virtual service that is acting as a virtual node backend.

    - **listeners** *(list) --*

      The listeners that the virtual node is expected to receive inbound traffic from. You can
      specify one listener.

      - *(dict) --*

        An object that represents a listener for a virtual node.

        - **healthCheck** *(dict) --*

          The health check information for the listener.

          - **healthyThreshold** *(integer) --*

            The number of consecutive successful health checks that must occur before declaring
            listener healthy.

          - **intervalMillis** *(integer) --*

            The time period in milliseconds between each health check execution.

          - **path** *(string) --*

            The destination path for the health check request. This is required only if the
            specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

          - **port** *(integer) --*

            The destination port for the health check request. This port must match the port
            defined in the  PortMapping for the listener.

          - **protocol** *(string) --*

            The protocol for the health check request.

          - **timeoutMillis** *(integer) --*

            The amount of time to wait when receiving a response from the health check, in
            milliseconds.

          - **unhealthyThreshold** *(integer) --*

            The number of consecutive failed health checks that must occur before declaring a
            virtual node unhealthy.

        - **portMapping** *(dict) --*

          The port mapping information for the listener.

          - **port** *(integer) --*

            The port used for the port mapping.

          - **protocol** *(string) --*

            The protocol used for the port mapping. Specify one protocol.

    - **logging** *(dict) --*

      The inbound and outbound access logging information for the virtual node.

      - **accessLog** *(dict) --*

        The access log configuration for a virtual node.

        - **file** *(dict) --*

          The file object to send virtual node access logs to.

          - **path** *(string) --*

            The file path to write access logs to. You can use ``/dev/stdout`` to send access
            logs to standard out and configure your Envoy container to use a log driver, such
            as ``awslogs`` , to export the access logs to a log storage service such as Amazon
            CloudWatch Logs. You can also specify a path in the Envoy container's file system
            to write the files to disk.

            .. note::

              The Envoy process must have write permissions to the path that you specify here.
              Otherwise, Envoy fails to bootstrap properly.

    - **serviceDiscovery** *(dict) --*

      The service discovery information for the virtual node. If your virtual node does not
      expect ingress traffic, you can omit this parameter.

      - **awsCloudMap** *(dict) --*

        Specifies any AWS Cloud Map information for the virtual node.

        - **attributes** *(list) --*

          A string map that contains attributes with values that you can use to filter
          instances by any custom attribute that you specified when you registered the
          instance. Only instances that match all of the specified key/value pairs will be
          returned.

          - *(dict) --*

            An object that represents the AWS Cloud Map attribute information for your virtual
            node.

            - **key** *(string) --*

              The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
              service instance that contains the specified key and value is returned.

            - **value** *(string) --*

              The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
              service instance that contains the specified key and value is returned.

        - **namespaceName** *(string) --*

          The name of the AWS Cloud Map namespace to use.

        - **serviceName** *(string) --*

          The name of the AWS Cloud Map service to use.

      - **dns** *(dict) --*

        Specifies the DNS information for the virtual node.

        - **hostname** *(string) --*

          Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef",
    {"status": str},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponsevirtualNode` `status`

    The current status for the virtual node.

    - **status** *(string) --*

      The current status of the virtual node.
    """


_ClientDeleteVirtualNodeResponsevirtualNodeTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodeTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef,
        "spec": ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef,
        "status": ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef,
        "virtualNodeName": str,
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodeTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodeTypeDef
):
    """
    Type definition for `ClientDeleteVirtualNodeResponse` `virtualNode`

    The virtual node that was deleted.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual node resides in.

    - **metadata** *(dict) --*

      The associated metadata for the virtual node.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The specifications of the virtual node.

      - **backends** *(list) --*

        The backends that the virtual node is expected to send outbound traffic to.

        - *(dict) --*

          An object that represents the backends that a virtual node is expected to send outbound
          traffic to.

          - **virtualService** *(dict) --*

            Specifies a virtual service to use as a backend for a virtual node.

            - **virtualServiceName** *(string) --*

              The name of the virtual service that is acting as a virtual node backend.

      - **listeners** *(list) --*

        The listeners that the virtual node is expected to receive inbound traffic from. You can
        specify one listener.

        - *(dict) --*

          An object that represents a listener for a virtual node.

          - **healthCheck** *(dict) --*

            The health check information for the listener.

            - **healthyThreshold** *(integer) --*

              The number of consecutive successful health checks that must occur before declaring
              listener healthy.

            - **intervalMillis** *(integer) --*

              The time period in milliseconds between each health check execution.

            - **path** *(string) --*

              The destination path for the health check request. This is required only if the
              specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

            - **port** *(integer) --*

              The destination port for the health check request. This port must match the port
              defined in the  PortMapping for the listener.

            - **protocol** *(string) --*

              The protocol for the health check request.

            - **timeoutMillis** *(integer) --*

              The amount of time to wait when receiving a response from the health check, in
              milliseconds.

            - **unhealthyThreshold** *(integer) --*

              The number of consecutive failed health checks that must occur before declaring a
              virtual node unhealthy.

          - **portMapping** *(dict) --*

            The port mapping information for the listener.

            - **port** *(integer) --*

              The port used for the port mapping.

            - **protocol** *(string) --*

              The protocol used for the port mapping. Specify one protocol.

      - **logging** *(dict) --*

        The inbound and outbound access logging information for the virtual node.

        - **accessLog** *(dict) --*

          The access log configuration for a virtual node.

          - **file** *(dict) --*

            The file object to send virtual node access logs to.

            - **path** *(string) --*

              The file path to write access logs to. You can use ``/dev/stdout`` to send access
              logs to standard out and configure your Envoy container to use a log driver, such
              as ``awslogs`` , to export the access logs to a log storage service such as Amazon
              CloudWatch Logs. You can also specify a path in the Envoy container's file system
              to write the files to disk.

              .. note::

                The Envoy process must have write permissions to the path that you specify here.
                Otherwise, Envoy fails to bootstrap properly.

      - **serviceDiscovery** *(dict) --*

        The service discovery information for the virtual node. If your virtual node does not
        expect ingress traffic, you can omit this parameter.

        - **awsCloudMap** *(dict) --*

          Specifies any AWS Cloud Map information for the virtual node.

          - **attributes** *(list) --*

            A string map that contains attributes with values that you can use to filter
            instances by any custom attribute that you specified when you registered the
            instance. Only instances that match all of the specified key/value pairs will be
            returned.

            - *(dict) --*

              An object that represents the AWS Cloud Map attribute information for your virtual
              node.

              - **key** *(string) --*

                The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                service instance that contains the specified key and value is returned.

              - **value** *(string) --*

                The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                service instance that contains the specified key and value is returned.

          - **namespaceName** *(string) --*

            The name of the AWS Cloud Map namespace to use.

          - **serviceName** *(string) --*

            The name of the AWS Cloud Map service to use.

        - **dns** *(dict) --*

          Specifies the DNS information for the virtual node.

          - **hostname** *(string) --*

            Specifies the DNS service discovery hostname for the virtual node.

    - **status** *(dict) --*

      The current status for the virtual node.

      - **status** *(string) --*

        The current status of the virtual node.

    - **virtualNodeName** *(string) --*

      The name of the virtual node.
    """


_ClientDeleteVirtualNodeResponseTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponseTypeDef",
    {"virtualNode": ClientDeleteVirtualNodeResponsevirtualNodeTypeDef},
    total=False,
)


class ClientDeleteVirtualNodeResponseTypeDef(_ClientDeleteVirtualNodeResponseTypeDef):
    """
    Type definition for `ClientDeleteVirtualNode` `Response`

    - **virtualNode** *(dict) --*

      The virtual node that was deleted.

      - **meshName** *(string) --*

        The name of the service mesh that the virtual node resides in.

      - **metadata** *(dict) --*

        The associated metadata for the virtual node.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The specifications of the virtual node.

        - **backends** *(list) --*

          The backends that the virtual node is expected to send outbound traffic to.

          - *(dict) --*

            An object that represents the backends that a virtual node is expected to send outbound
            traffic to.

            - **virtualService** *(dict) --*

              Specifies a virtual service to use as a backend for a virtual node.

              - **virtualServiceName** *(string) --*

                The name of the virtual service that is acting as a virtual node backend.

        - **listeners** *(list) --*

          The listeners that the virtual node is expected to receive inbound traffic from. You can
          specify one listener.

          - *(dict) --*

            An object that represents a listener for a virtual node.

            - **healthCheck** *(dict) --*

              The health check information for the listener.

              - **healthyThreshold** *(integer) --*

                The number of consecutive successful health checks that must occur before declaring
                listener healthy.

              - **intervalMillis** *(integer) --*

                The time period in milliseconds between each health check execution.

              - **path** *(string) --*

                The destination path for the health check request. This is required only if the
                specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

              - **port** *(integer) --*

                The destination port for the health check request. This port must match the port
                defined in the  PortMapping for the listener.

              - **protocol** *(string) --*

                The protocol for the health check request.

              - **timeoutMillis** *(integer) --*

                The amount of time to wait when receiving a response from the health check, in
                milliseconds.

              - **unhealthyThreshold** *(integer) --*

                The number of consecutive failed health checks that must occur before declaring a
                virtual node unhealthy.

            - **portMapping** *(dict) --*

              The port mapping information for the listener.

              - **port** *(integer) --*

                The port used for the port mapping.

              - **protocol** *(string) --*

                The protocol used for the port mapping. Specify one protocol.

        - **logging** *(dict) --*

          The inbound and outbound access logging information for the virtual node.

          - **accessLog** *(dict) --*

            The access log configuration for a virtual node.

            - **file** *(dict) --*

              The file object to send virtual node access logs to.

              - **path** *(string) --*

                The file path to write access logs to. You can use ``/dev/stdout`` to send access
                logs to standard out and configure your Envoy container to use a log driver, such
                as ``awslogs`` , to export the access logs to a log storage service such as Amazon
                CloudWatch Logs. You can also specify a path in the Envoy container's file system
                to write the files to disk.

                .. note::

                  The Envoy process must have write permissions to the path that you specify here.
                  Otherwise, Envoy fails to bootstrap properly.

        - **serviceDiscovery** *(dict) --*

          The service discovery information for the virtual node. If your virtual node does not
          expect ingress traffic, you can omit this parameter.

          - **awsCloudMap** *(dict) --*

            Specifies any AWS Cloud Map information for the virtual node.

            - **attributes** *(list) --*

              A string map that contains attributes with values that you can use to filter
              instances by any custom attribute that you specified when you registered the
              instance. Only instances that match all of the specified key/value pairs will be
              returned.

              - *(dict) --*

                An object that represents the AWS Cloud Map attribute information for your virtual
                node.

                - **key** *(string) --*

                  The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                  service instance that contains the specified key and value is returned.

                - **value** *(string) --*

                  The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                  service instance that contains the specified key and value is returned.

            - **namespaceName** *(string) --*

              The name of the AWS Cloud Map namespace to use.

            - **serviceName** *(string) --*

              The name of the AWS Cloud Map service to use.

          - **dns** *(dict) --*

            Specifies the DNS information for the virtual node.

            - **hostname** *(string) --*

              Specifies the DNS service discovery hostname for the virtual node.

      - **status** *(dict) --*

        The current status for the virtual node.

        - **status** *(string) --*

          The current status of the virtual node.

      - **virtualNodeName** *(string) --*

        The name of the virtual node.
    """


_ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef(
    _ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef
):
    """
    Type definition for `ClientDeleteVirtualRouterResponsevirtualRouter` `metadata`

    The associated metadata for the virtual router.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": str},
    total=False,
)


class ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef(
    _ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
):
    """
    Type definition for `ClientDeleteVirtualRouterResponsevirtualRouterspeclisteners` `portMapping`

    An object that represents a port mapping.

    - **port** *(integer) --*

      The port used for the port mapping.

    - **protocol** *(string) --*

      The protocol used for the port mapping. Specify one protocol.
    """


_ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    {
        "portMapping": ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
    },
    total=False,
)


class ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef(
    _ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef
):
    """
    Type definition for `ClientDeleteVirtualRouterResponsevirtualRouterspec` `listeners`

    An object that represents a virtual router listener.

    - **portMapping** *(dict) --*

      An object that represents a port mapping.

      - **port** *(integer) --*

        The port used for the port mapping.

      - **protocol** *(string) --*

        The protocol used for the port mapping. Specify one protocol.
    """


_ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef",
    {
        "listeners": List[
            ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef
        ]
    },
    total=False,
)


class ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef(
    _ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef
):
    """
    Type definition for `ClientDeleteVirtualRouterResponsevirtualRouter` `spec`

    The specifications of the virtual router.

    - **listeners** *(list) --*

      The listeners that the virtual router is expected to receive inbound traffic from. You
      can specify one listener.

      - *(dict) --*

        An object that represents a virtual router listener.

        - **portMapping** *(dict) --*

          An object that represents a port mapping.

          - **port** *(integer) --*

            The port used for the port mapping.

          - **protocol** *(string) --*

            The protocol used for the port mapping. Specify one protocol.
    """


_ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef",
    {"status": str},
    total=False,
)


class ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef(
    _ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef
):
    """
    Type definition for `ClientDeleteVirtualRouterResponsevirtualRouter` `status`

    The current status of the virtual router.

    - **status** *(string) --*

      The current status of the virtual router.
    """


_ClientDeleteVirtualRouterResponsevirtualRouterTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponsevirtualRouterTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef,
        "spec": ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef,
        "status": ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientDeleteVirtualRouterResponsevirtualRouterTypeDef(
    _ClientDeleteVirtualRouterResponsevirtualRouterTypeDef
):
    """
    Type definition for `ClientDeleteVirtualRouterResponse` `virtualRouter`

    The virtual router that was deleted.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual router resides in.

    - **metadata** *(dict) --*

      The associated metadata for the virtual router.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The specifications of the virtual router.

      - **listeners** *(list) --*

        The listeners that the virtual router is expected to receive inbound traffic from. You
        can specify one listener.

        - *(dict) --*

          An object that represents a virtual router listener.

          - **portMapping** *(dict) --*

            An object that represents a port mapping.

            - **port** *(integer) --*

              The port used for the port mapping.

            - **protocol** *(string) --*

              The protocol used for the port mapping. Specify one protocol.

    - **status** *(dict) --*

      The current status of the virtual router.

      - **status** *(string) --*

        The current status of the virtual router.

    - **virtualRouterName** *(string) --*

      The name of the virtual router.
    """


_ClientDeleteVirtualRouterResponseTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponseTypeDef",
    {"virtualRouter": ClientDeleteVirtualRouterResponsevirtualRouterTypeDef},
    total=False,
)


class ClientDeleteVirtualRouterResponseTypeDef(
    _ClientDeleteVirtualRouterResponseTypeDef
):
    """
    Type definition for `ClientDeleteVirtualRouter` `Response`

    - **virtualRouter** *(dict) --*

      The virtual router that was deleted.

      - **meshName** *(string) --*

        The name of the service mesh that the virtual router resides in.

      - **metadata** *(dict) --*

        The associated metadata for the virtual router.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The specifications of the virtual router.

        - **listeners** *(list) --*

          The listeners that the virtual router is expected to receive inbound traffic from. You
          can specify one listener.

          - *(dict) --*

            An object that represents a virtual router listener.

            - **portMapping** *(dict) --*

              An object that represents a port mapping.

              - **port** *(integer) --*

                The port used for the port mapping.

              - **protocol** *(string) --*

                The protocol used for the port mapping. Specify one protocol.

      - **status** *(dict) --*

        The current status of the virtual router.

        - **status** *(string) --*

          The current status of the virtual router.

      - **virtualRouterName** *(string) --*

        The name of the virtual router.
    """


_ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef
):
    """
    Type definition for `ClientDeleteVirtualServiceResponsevirtualService` `metadata`

    An object that represents metadata for a resource.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef
):
    """
    Type definition for `ClientDeleteVirtualServiceResponsevirtualServicespecprovider` `virtualNode`

    The virtual node associated with a virtual service.

    - **virtualNodeName** *(string) --*

      The name of the virtual node that is acting as a service provider.
    """


_ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef
):
    """
    Type definition for `ClientDeleteVirtualServiceResponsevirtualServicespecprovider` `virtualRouter`

    The virtual router associated with a virtual service.

    - **virtualRouterName** *(string) --*

      The name of the virtual router that is acting as a service provider.
    """


_ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef
):
    """
    Type definition for `ClientDeleteVirtualServiceResponsevirtualServicespec` `provider`

    The App Mesh object that is acting as the provider for a virtual service. You can specify
    a single virtual node or virtual router.

    - **virtualNode** *(dict) --*

      The virtual node associated with a virtual service.

      - **virtualNodeName** *(string) --*

        The name of the virtual node that is acting as a service provider.

    - **virtualRouter** *(dict) --*

      The virtual router associated with a virtual service.

      - **virtualRouterName** *(string) --*

        The name of the virtual router that is acting as a service provider.
    """


_ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef",
    {"provider": ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef},
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef
):
    """
    Type definition for `ClientDeleteVirtualServiceResponsevirtualService` `spec`

    The specifications of the virtual service.

    - **provider** *(dict) --*

      The App Mesh object that is acting as the provider for a virtual service. You can specify
      a single virtual node or virtual router.

      - **virtualNode** *(dict) --*

        The virtual node associated with a virtual service.

        - **virtualNodeName** *(string) --*

          The name of the virtual node that is acting as a service provider.

      - **virtualRouter** *(dict) --*

        The virtual router associated with a virtual service.

        - **virtualRouterName** *(string) --*

          The name of the virtual router that is acting as a service provider.
    """


_ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef",
    {"status": str},
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef
):
    """
    Type definition for `ClientDeleteVirtualServiceResponsevirtualService` `status`

    The current status of the virtual service.

    - **status** *(string) --*

      The current status of the virtual service.
    """


_ClientDeleteVirtualServiceResponsevirtualServiceTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServiceTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef,
        "spec": ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef,
        "status": ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef,
        "virtualServiceName": str,
    },
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServiceTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServiceTypeDef
):
    """
    Type definition for `ClientDeleteVirtualServiceResponse` `virtualService`

    The virtual service that was deleted.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual service resides in.

    - **metadata** *(dict) --*

      An object that represents metadata for a resource.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The specifications of the virtual service.

      - **provider** *(dict) --*

        The App Mesh object that is acting as the provider for a virtual service. You can specify
        a single virtual node or virtual router.

        - **virtualNode** *(dict) --*

          The virtual node associated with a virtual service.

          - **virtualNodeName** *(string) --*

            The name of the virtual node that is acting as a service provider.

        - **virtualRouter** *(dict) --*

          The virtual router associated with a virtual service.

          - **virtualRouterName** *(string) --*

            The name of the virtual router that is acting as a service provider.

    - **status** *(dict) --*

      The current status of the virtual service.

      - **status** *(string) --*

        The current status of the virtual service.

    - **virtualServiceName** *(string) --*

      The name of the virtual service.
    """


_ClientDeleteVirtualServiceResponseTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponseTypeDef",
    {"virtualService": ClientDeleteVirtualServiceResponsevirtualServiceTypeDef},
    total=False,
)


class ClientDeleteVirtualServiceResponseTypeDef(
    _ClientDeleteVirtualServiceResponseTypeDef
):
    """
    Type definition for `ClientDeleteVirtualService` `Response`

    - **virtualService** *(dict) --*

      The virtual service that was deleted.

      - **meshName** *(string) --*

        The name of the service mesh that the virtual service resides in.

      - **metadata** *(dict) --*

        An object that represents metadata for a resource.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The specifications of the virtual service.

        - **provider** *(dict) --*

          The App Mesh object that is acting as the provider for a virtual service. You can specify
          a single virtual node or virtual router.

          - **virtualNode** *(dict) --*

            The virtual node associated with a virtual service.

            - **virtualNodeName** *(string) --*

              The name of the virtual node that is acting as a service provider.

          - **virtualRouter** *(dict) --*

            The virtual router associated with a virtual service.

            - **virtualRouterName** *(string) --*

              The name of the virtual router that is acting as a service provider.

      - **status** *(dict) --*

        The current status of the virtual service.

        - **status** *(string) --*

          The current status of the virtual service.

      - **virtualServiceName** *(string) --*

        The name of the virtual service.
    """


_ClientDescribeMeshResponsemeshmetadataTypeDef = TypedDict(
    "_ClientDescribeMeshResponsemeshmetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientDescribeMeshResponsemeshmetadataTypeDef(
    _ClientDescribeMeshResponsemeshmetadataTypeDef
):
    """
    Type definition for `ClientDescribeMeshResponsemesh` `metadata`

    The associated metadata for the service mesh.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientDescribeMeshResponsemeshspecegressFilterTypeDef = TypedDict(
    "_ClientDescribeMeshResponsemeshspecegressFilterTypeDef", {"type": str}, total=False
)


class ClientDescribeMeshResponsemeshspecegressFilterTypeDef(
    _ClientDescribeMeshResponsemeshspecegressFilterTypeDef
):
    """
    Type definition for `ClientDescribeMeshResponsemeshspec` `egressFilter`

    The egress filter rules for the service mesh.

    - **type** *(string) --*

      The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
      from virtual nodes to other defined resources in the service mesh (and any traffic to
      ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
      ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientDescribeMeshResponsemeshspecTypeDef = TypedDict(
    "_ClientDescribeMeshResponsemeshspecTypeDef",
    {"egressFilter": ClientDescribeMeshResponsemeshspecegressFilterTypeDef},
    total=False,
)


class ClientDescribeMeshResponsemeshspecTypeDef(
    _ClientDescribeMeshResponsemeshspecTypeDef
):
    """
    Type definition for `ClientDescribeMeshResponsemesh` `spec`

    The associated specification for the service mesh.

    - **egressFilter** *(dict) --*

      The egress filter rules for the service mesh.

      - **type** *(string) --*

        The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
        from virtual nodes to other defined resources in the service mesh (and any traffic to
        ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
        ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientDescribeMeshResponsemeshstatusTypeDef = TypedDict(
    "_ClientDescribeMeshResponsemeshstatusTypeDef", {"status": str}, total=False
)


class ClientDescribeMeshResponsemeshstatusTypeDef(
    _ClientDescribeMeshResponsemeshstatusTypeDef
):
    """
    Type definition for `ClientDescribeMeshResponsemesh` `status`

    The status of the service mesh.

    - **status** *(string) --*

      The current mesh status.
    """


_ClientDescribeMeshResponsemeshTypeDef = TypedDict(
    "_ClientDescribeMeshResponsemeshTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeMeshResponsemeshmetadataTypeDef,
        "spec": ClientDescribeMeshResponsemeshspecTypeDef,
        "status": ClientDescribeMeshResponsemeshstatusTypeDef,
    },
    total=False,
)


class ClientDescribeMeshResponsemeshTypeDef(_ClientDescribeMeshResponsemeshTypeDef):
    """
    Type definition for `ClientDescribeMeshResponse` `mesh`

    The full description of your service mesh.

    - **meshName** *(string) --*

      The name of the service mesh.

    - **metadata** *(dict) --*

      The associated metadata for the service mesh.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The associated specification for the service mesh.

      - **egressFilter** *(dict) --*

        The egress filter rules for the service mesh.

        - **type** *(string) --*

          The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
          from virtual nodes to other defined resources in the service mesh (and any traffic to
          ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
          ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.

    - **status** *(dict) --*

      The status of the service mesh.

      - **status** *(string) --*

        The current mesh status.
    """


_ClientDescribeMeshResponseTypeDef = TypedDict(
    "_ClientDescribeMeshResponseTypeDef",
    {"mesh": ClientDescribeMeshResponsemeshTypeDef},
    total=False,
)


class ClientDescribeMeshResponseTypeDef(_ClientDescribeMeshResponseTypeDef):
    """
    Type definition for `ClientDescribeMesh` `Response`

    - **mesh** *(dict) --*

      The full description of your service mesh.

      - **meshName** *(string) --*

        The name of the service mesh.

      - **metadata** *(dict) --*

        The associated metadata for the service mesh.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The associated specification for the service mesh.

        - **egressFilter** *(dict) --*

          The egress filter rules for the service mesh.

          - **type** *(string) --*

            The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
            from virtual nodes to other defined resources in the service mesh (and any traffic to
            ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
            ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.

      - **status** *(dict) --*

        The status of the service mesh.

        - **status** *(string) --*

          The current mesh status.
    """


_ClientDescribeRouteResponseroutemetadataTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutemetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientDescribeRouteResponseroutemetadataTypeDef(
    _ClientDescribeRouteResponseroutemetadataTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroute` `metadata`

    The associated metadata for the route.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespecgrpcRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespecgrpcRoute` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --*

      The end of the range.

    - **start** *(integer) --*

      The start of the range.
    """


_ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespecgrpcRoutematchmetadata` `match`

    An object that represents the data to match from the request.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --*

        The end of the range.

      - **start** *(integer) --*

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    {
        "invert": bool,
        "match": ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespecgrpcRoutematch` `metadata`

    An object that represents the match metadata for the route.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value
      is ``False`` .

    - **match** *(dict) --*

      An object that represents the data to match from the request.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --*

          The end of the range.

        - **start** *(integer) --*

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --*

      The name of the route.
    """


_ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[
            ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef
        ],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespecgrpcRoute` `match`

    An object that represents the criteria for determining a request match.

    - **metadata** *(list) --*

      An object that represents the data to match from the request.

      - *(dict) --*

        An object that represents the match metadata for the route.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value
          is ``False`` .

        - **match** *(dict) --*

          An object that represents the data to match from the request.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --*

              The end of the range.

            - **start** *(integer) --*

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --*

          The name of the route.

    - **methodName** *(string) --*

      The method name to match from the request. If you specify a name, you must also
      specify a ``serviceName`` .

    - **serviceName** *(string) --*

      The fully qualified domain name for the service to match from the request.
    """


_ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespecgrpcRouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[str],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespecgrpcRoute` `retryPolicy`

    An object that represents a retry policy.

    - **grpcRetryEvents** *(list) --*

      Specify at least one of the valid values.

      - *(string) --*

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
      510, and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --*

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --*

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_ClientDescribeRouteResponseroutespecgrpcRouteTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRouteTypeDef",
    {
        "action": ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef,
        "match": ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef,
        "retryPolicy": ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRouteTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRouteTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespec` `grpcRoute`

    An object that represents the specification of a GRPC route.

    - **action** *(dict) --*

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.

    - **match** *(dict) --*

      An object that represents the criteria for determining a request match.

      - **metadata** *(list) --*

        An object that represents the data to match from the request.

        - *(dict) --*

          An object that represents the match metadata for the route.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value
            is ``False`` .

          - **match** *(dict) --*

            An object that represents the data to match from the request.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --*

                The end of the range.

              - **start** *(integer) --*

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --*

            The name of the route.

      - **methodName** *(string) --*

        The method name to match from the request. If you specify a name, you must also
        specify a ``serviceName`` .

      - **serviceName** *(string) --*

        The fully qualified domain name for the service to match from the request.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **grpcRetryEvents** *(list) --*

        Specify at least one of the valid values.

        - *(string) --*

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
        510, and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --*

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --*

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttp2Routeaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttp2Route` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttp2Routematchheadersmatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --*

      The end of the range.

    - **start** *(integer) --*

      The start of the range.
    """


_ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttp2Routematchheaders` `match`

    The ``HeaderMatchMethod`` object.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --*

        The end of the range.

      - **start** *(integer) --*

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttp2Routematch` `headers`

    An object that represents the HTTP header in the request.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value
      is ``False`` .

    - **match** *(dict) --*

      The ``HeaderMatchMethod`` object.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --*

          The end of the range.

        - **start** *(integer) --*

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --*

      A name for the HTTP header in the client request that will be matched on.
    """


_ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef",
    {
        "headers": List[
            ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef
        ],
        "method": str,
        "prefix": str,
        "scheme": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttp2Route` `match`

    An object that represents the criteria for determining a request match.

    - **headers** *(list) --*

      An object that represents the client request headers to match on.

      - *(dict) --*

        An object that represents the HTTP header in the request.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value
          is ``False`` .

        - **match** *(dict) --*

          The ``HeaderMatchMethod`` object.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --*

              The end of the range.

            - **start** *(integer) --*

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --*

          A name for the HTTP header in the client request that will be matched on.

    - **method** *(string) --*

      The client request method to match on. Specify only one.

    - **prefix** *(string) --*

      Specifies the path to match requests with. This parameter must always start with
      ``/`` , which by itself matches all requests to the virtual service name. You can
      also match for path-based routing of requests. For example, if your virtual service
      name is ``my-service.local`` and you want the route to match requests to
      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

    - **scheme** *(string) --*

      The client request scheme to match on. Specify only one.
    """


_ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttp2RouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttp2Route` `retryPolicy`

    An object that represents a retry policy.

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
      510, and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --*

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --*

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_ClientDescribeRouteResponseroutespechttp2RouteTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RouteTypeDef",
    {
        "action": ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef,
        "match": ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef,
        "retryPolicy": ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RouteTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RouteTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespec` `http2Route`

    An object that represents the specification of an HTTP2 route.

    - **action** *(dict) --*

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.

    - **match** *(dict) --*

      An object that represents the criteria for determining a request match.

      - **headers** *(list) --*

        An object that represents the client request headers to match on.

        - *(dict) --*

          An object that represents the HTTP header in the request.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value
            is ``False`` .

          - **match** *(dict) --*

            The ``HeaderMatchMethod`` object.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --*

                The end of the range.

              - **start** *(integer) --*

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --*

            A name for the HTTP header in the client request that will be matched on.

      - **method** *(string) --*

        The client request method to match on. Specify only one.

      - **prefix** *(string) --*

        Specifies the path to match requests with. This parameter must always start with
        ``/`` , which by itself matches all requests to the virtual service name. You can
        also match for path-based routing of requests. For example, if your virtual service
        name is ``my-service.local`` and you want the route to match requests to
        ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

      - **scheme** *(string) --*

        The client request scheme to match on. Specify only one.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
        510, and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --*

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --*

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef(
    _ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttpRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientDescribeRouteResponseroutespechttpRouteactionTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRouteactionTypeDef(
    _ClientDescribeRouteResponseroutespechttpRouteactionTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttpRoute` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef(
    _ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttpRoutematchheadersmatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --*

      The end of the range.

    - **start** *(integer) --*

      The start of the range.
    """


_ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef(
    _ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttpRoutematchheaders` `match`

    The ``HeaderMatchMethod`` object.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --*

        The end of the range.

      - **start** *(integer) --*

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef(
    _ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttpRoutematch` `headers`

    An object that represents the HTTP header in the request.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value
      is ``False`` .

    - **match** *(dict) --*

      The ``HeaderMatchMethod`` object.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --*

          The end of the range.

        - **start** *(integer) --*

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --*

      A name for the HTTP header in the client request that will be matched on.
    """


_ClientDescribeRouteResponseroutespechttpRoutematchTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRoutematchTypeDef",
    {
        "headers": List[
            ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef
        ],
        "method": str,
        "prefix": str,
        "scheme": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRoutematchTypeDef(
    _ClientDescribeRouteResponseroutespechttpRoutematchTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttpRoute` `match`

    An object that represents the criteria for determining a request match.

    - **headers** *(list) --*

      An object that represents the client request headers to match on.

      - *(dict) --*

        An object that represents the HTTP header in the request.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value
          is ``False`` .

        - **match** *(dict) --*

          The ``HeaderMatchMethod`` object.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --*

              The end of the range.

            - **start** *(integer) --*

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --*

          A name for the HTTP header in the client request that will be matched on.

    - **method** *(string) --*

      The client request method to match on. Specify only one.

    - **prefix** *(string) --*

      Specifies the path to match requests with. This parameter must always start with
      ``/`` , which by itself matches all requests to the virtual service name. You can
      also match for path-based routing of requests. For example, if your virtual service
      name is ``my-service.local`` and you want the route to match requests to
      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

    - **scheme** *(string) --*

      The client request scheme to match on. Specify only one.
    """


_ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttpRouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef(
    _ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespechttpRoute` `retryPolicy`

    An object that represents a retry policy.

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
      510, and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --*

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --*

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_ClientDescribeRouteResponseroutespechttpRouteTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRouteTypeDef",
    {
        "action": ClientDescribeRouteResponseroutespechttpRouteactionTypeDef,
        "match": ClientDescribeRouteResponseroutespechttpRoutematchTypeDef,
        "retryPolicy": ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRouteTypeDef(
    _ClientDescribeRouteResponseroutespechttpRouteTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespec` `httpRoute`

    An object that represents the specification of an HTTP route.

    - **action** *(dict) --*

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.

    - **match** *(dict) --*

      An object that represents the criteria for determining a request match.

      - **headers** *(list) --*

        An object that represents the client request headers to match on.

        - *(dict) --*

          An object that represents the HTTP header in the request.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value
            is ``False`` .

          - **match** *(dict) --*

            The ``HeaderMatchMethod`` object.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --*

                The end of the range.

              - **start** *(integer) --*

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --*

            A name for the HTTP header in the client request that will be matched on.

      - **method** *(string) --*

        The client request method to match on. Specify only one.

      - **prefix** *(string) --*

        Specifies the path to match requests with. This parameter must always start with
        ``/`` , which by itself matches all requests to the virtual service name. You can
        also match for path-based routing of requests. For example, if your virtual service
        name is ``my-service.local`` and you want the route to match requests to
        ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

      - **scheme** *(string) --*

        The client request scheme to match on. Specify only one.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
        510, and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --*

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --*

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef(
    _ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespectcpRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientDescribeRouteResponseroutespectcpRouteactionTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeRouteResponseroutespectcpRouteactionTypeDef(
    _ClientDescribeRouteResponseroutespectcpRouteactionTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespectcpRoute` `action`

    The action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientDescribeRouteResponseroutespectcpRouteTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespectcpRouteTypeDef",
    {"action": ClientDescribeRouteResponseroutespectcpRouteactionTypeDef},
    total=False,
)


class ClientDescribeRouteResponseroutespectcpRouteTypeDef(
    _ClientDescribeRouteResponseroutespectcpRouteTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroutespec` `tcpRoute`

    An object that represents the specification of a TCP route.

    - **action** *(dict) --*

      The action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.
    """


_ClientDescribeRouteResponseroutespecTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecTypeDef",
    {
        "grpcRoute": ClientDescribeRouteResponseroutespecgrpcRouteTypeDef,
        "http2Route": ClientDescribeRouteResponseroutespechttp2RouteTypeDef,
        "httpRoute": ClientDescribeRouteResponseroutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientDescribeRouteResponseroutespectcpRouteTypeDef,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecTypeDef(
    _ClientDescribeRouteResponseroutespecTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroute` `spec`

    The specifications of the route.

    - **grpcRoute** *(dict) --*

      An object that represents the specification of a GRPC route.

      - **action** *(dict) --*

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.

      - **match** *(dict) --*

        An object that represents the criteria for determining a request match.

        - **metadata** *(list) --*

          An object that represents the data to match from the request.

          - *(dict) --*

            An object that represents the match metadata for the route.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value
              is ``False`` .

            - **match** *(dict) --*

              An object that represents the data to match from the request.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --*

                  The end of the range.

                - **start** *(integer) --*

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --*

              The name of the route.

        - **methodName** *(string) --*

          The method name to match from the request. If you specify a name, you must also
          specify a ``serviceName`` .

        - **serviceName** *(string) --*

          The fully qualified domain name for the service to match from the request.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **grpcRetryEvents** *(list) --*

          Specify at least one of the valid values.

          - *(string) --*

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
          510, and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --*

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --*

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **http2Route** *(dict) --*

      An object that represents the specification of an HTTP2 route.

      - **action** *(dict) --*

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.

      - **match** *(dict) --*

        An object that represents the criteria for determining a request match.

        - **headers** *(list) --*

          An object that represents the client request headers to match on.

          - *(dict) --*

            An object that represents the HTTP header in the request.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value
              is ``False`` .

            - **match** *(dict) --*

              The ``HeaderMatchMethod`` object.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --*

                  The end of the range.

                - **start** *(integer) --*

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --*

              A name for the HTTP header in the client request that will be matched on.

        - **method** *(string) --*

          The client request method to match on. Specify only one.

        - **prefix** *(string) --*

          Specifies the path to match requests with. This parameter must always start with
          ``/`` , which by itself matches all requests to the virtual service name. You can
          also match for path-based routing of requests. For example, if your virtual service
          name is ``my-service.local`` and you want the route to match requests to
          ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

        - **scheme** *(string) --*

          The client request scheme to match on. Specify only one.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
          510, and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --*

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --*

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **httpRoute** *(dict) --*

      An object that represents the specification of an HTTP route.

      - **action** *(dict) --*

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.

      - **match** *(dict) --*

        An object that represents the criteria for determining a request match.

        - **headers** *(list) --*

          An object that represents the client request headers to match on.

          - *(dict) --*

            An object that represents the HTTP header in the request.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value
              is ``False`` .

            - **match** *(dict) --*

              The ``HeaderMatchMethod`` object.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --*

                  The end of the range.

                - **start** *(integer) --*

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --*

              A name for the HTTP header in the client request that will be matched on.

        - **method** *(string) --*

          The client request method to match on. Specify only one.

        - **prefix** *(string) --*

          Specifies the path to match requests with. This parameter must always start with
          ``/`` , which by itself matches all requests to the virtual service name. You can
          also match for path-based routing of requests. For example, if your virtual service
          name is ``my-service.local`` and you want the route to match requests to
          ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

        - **scheme** *(string) --*

          The client request scheme to match on. Specify only one.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
          510, and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --*

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --*

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **priority** *(integer) --*

      The priority for the route. Routes are matched based on the specified value, where 0 is
      the highest priority.

    - **tcpRoute** *(dict) --*

      An object that represents the specification of a TCP route.

      - **action** *(dict) --*

        The action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.
    """


_ClientDescribeRouteResponseroutestatusTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutestatusTypeDef", {"status": str}, total=False
)


class ClientDescribeRouteResponseroutestatusTypeDef(
    _ClientDescribeRouteResponseroutestatusTypeDef
):
    """
    Type definition for `ClientDescribeRouteResponseroute` `status`

    The status of the route.

    - **status** *(string) --*

      The current status for the route.
    """


_ClientDescribeRouteResponserouteTypeDef = TypedDict(
    "_ClientDescribeRouteResponserouteTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeRouteResponseroutemetadataTypeDef,
        "routeName": str,
        "spec": ClientDescribeRouteResponseroutespecTypeDef,
        "status": ClientDescribeRouteResponseroutestatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientDescribeRouteResponserouteTypeDef(_ClientDescribeRouteResponserouteTypeDef):
    """
    Type definition for `ClientDescribeRouteResponse` `route`

    The full description of your route.

    - **meshName** *(string) --*

      The name of the service mesh that the route resides in.

    - **metadata** *(dict) --*

      The associated metadata for the route.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **routeName** *(string) --*

      The name of the route.

    - **spec** *(dict) --*

      The specifications of the route.

      - **grpcRoute** *(dict) --*

        An object that represents the specification of a GRPC route.

        - **action** *(dict) --*

          An object that represents the action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

        - **match** *(dict) --*

          An object that represents the criteria for determining a request match.

          - **metadata** *(list) --*

            An object that represents the data to match from the request.

            - *(dict) --*

              An object that represents the match metadata for the route.

              - **invert** *(boolean) --*

                Specify ``True`` to match anything except the match criteria. The default value
                is ``False`` .

              - **match** *(dict) --*

                An object that represents the data to match from the request.

                - **exact** *(string) --*

                  The value sent by the client must match the specified value exactly.

                - **prefix** *(string) --*

                  The value sent by the client must begin with the specified characters.

                - **range** *(dict) --*

                  An object that represents the range of values to match on.

                  - **end** *(integer) --*

                    The end of the range.

                  - **start** *(integer) --*

                    The start of the range.

                - **regex** *(string) --*

                  The value sent by the client must include the specified characters.

                - **suffix** *(string) --*

                  The value sent by the client must end with the specified characters.

              - **name** *(string) --*

                The name of the route.

          - **methodName** *(string) --*

            The method name to match from the request. If you specify a name, you must also
            specify a ``serviceName`` .

          - **serviceName** *(string) --*

            The fully qualified domain name for the service to match from the request.

        - **retryPolicy** *(dict) --*

          An object that represents a retry policy.

          - **grpcRetryEvents** *(list) --*

            Specify at least one of the valid values.

            - *(string) --*

          - **httpRetryEvents** *(list) --*

            Specify at least one of the following values.

            * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
            510, and 511

            * **gateway-error** – HTTP status codes 502, 503, and 504

            * **client-error** – HTTP status code 409

            * **stream-error** – Retry on refused stream

            - *(string) --*

          - **maxRetries** *(integer) --*

            The maximum number of retry attempts.

          - **perRetryTimeout** *(dict) --*

            An object that represents a duration of time.

            - **unit** *(string) --*

              A unit of time.

            - **value** *(integer) --*

              A number of time units.

          - **tcpRetryEvents** *(list) --*

            Specify a valid value.

            - *(string) --*

      - **http2Route** *(dict) --*

        An object that represents the specification of an HTTP2 route.

        - **action** *(dict) --*

          An object that represents the action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

        - **match** *(dict) --*

          An object that represents the criteria for determining a request match.

          - **headers** *(list) --*

            An object that represents the client request headers to match on.

            - *(dict) --*

              An object that represents the HTTP header in the request.

              - **invert** *(boolean) --*

                Specify ``True`` to match anything except the match criteria. The default value
                is ``False`` .

              - **match** *(dict) --*

                The ``HeaderMatchMethod`` object.

                - **exact** *(string) --*

                  The value sent by the client must match the specified value exactly.

                - **prefix** *(string) --*

                  The value sent by the client must begin with the specified characters.

                - **range** *(dict) --*

                  An object that represents the range of values to match on.

                  - **end** *(integer) --*

                    The end of the range.

                  - **start** *(integer) --*

                    The start of the range.

                - **regex** *(string) --*

                  The value sent by the client must include the specified characters.

                - **suffix** *(string) --*

                  The value sent by the client must end with the specified characters.

              - **name** *(string) --*

                A name for the HTTP header in the client request that will be matched on.

          - **method** *(string) --*

            The client request method to match on. Specify only one.

          - **prefix** *(string) --*

            Specifies the path to match requests with. This parameter must always start with
            ``/`` , which by itself matches all requests to the virtual service name. You can
            also match for path-based routing of requests. For example, if your virtual service
            name is ``my-service.local`` and you want the route to match requests to
            ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

          - **scheme** *(string) --*

            The client request scheme to match on. Specify only one.

        - **retryPolicy** *(dict) --*

          An object that represents a retry policy.

          - **httpRetryEvents** *(list) --*

            Specify at least one of the following values.

            * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
            510, and 511

            * **gateway-error** – HTTP status codes 502, 503, and 504

            * **client-error** – HTTP status code 409

            * **stream-error** – Retry on refused stream

            - *(string) --*

          - **maxRetries** *(integer) --*

            The maximum number of retry attempts.

          - **perRetryTimeout** *(dict) --*

            An object that represents a duration of time.

            - **unit** *(string) --*

              A unit of time.

            - **value** *(integer) --*

              A number of time units.

          - **tcpRetryEvents** *(list) --*

            Specify a valid value.

            - *(string) --*

      - **httpRoute** *(dict) --*

        An object that represents the specification of an HTTP route.

        - **action** *(dict) --*

          An object that represents the action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

        - **match** *(dict) --*

          An object that represents the criteria for determining a request match.

          - **headers** *(list) --*

            An object that represents the client request headers to match on.

            - *(dict) --*

              An object that represents the HTTP header in the request.

              - **invert** *(boolean) --*

                Specify ``True`` to match anything except the match criteria. The default value
                is ``False`` .

              - **match** *(dict) --*

                The ``HeaderMatchMethod`` object.

                - **exact** *(string) --*

                  The value sent by the client must match the specified value exactly.

                - **prefix** *(string) --*

                  The value sent by the client must begin with the specified characters.

                - **range** *(dict) --*

                  An object that represents the range of values to match on.

                  - **end** *(integer) --*

                    The end of the range.

                  - **start** *(integer) --*

                    The start of the range.

                - **regex** *(string) --*

                  The value sent by the client must include the specified characters.

                - **suffix** *(string) --*

                  The value sent by the client must end with the specified characters.

              - **name** *(string) --*

                A name for the HTTP header in the client request that will be matched on.

          - **method** *(string) --*

            The client request method to match on. Specify only one.

          - **prefix** *(string) --*

            Specifies the path to match requests with. This parameter must always start with
            ``/`` , which by itself matches all requests to the virtual service name. You can
            also match for path-based routing of requests. For example, if your virtual service
            name is ``my-service.local`` and you want the route to match requests to
            ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

          - **scheme** *(string) --*

            The client request scheme to match on. Specify only one.

        - **retryPolicy** *(dict) --*

          An object that represents a retry policy.

          - **httpRetryEvents** *(list) --*

            Specify at least one of the following values.

            * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
            510, and 511

            * **gateway-error** – HTTP status codes 502, 503, and 504

            * **client-error** – HTTP status code 409

            * **stream-error** – Retry on refused stream

            - *(string) --*

          - **maxRetries** *(integer) --*

            The maximum number of retry attempts.

          - **perRetryTimeout** *(dict) --*

            An object that represents a duration of time.

            - **unit** *(string) --*

              A unit of time.

            - **value** *(integer) --*

              A number of time units.

          - **tcpRetryEvents** *(list) --*

            Specify a valid value.

            - *(string) --*

      - **priority** *(integer) --*

        The priority for the route. Routes are matched based on the specified value, where 0 is
        the highest priority.

      - **tcpRoute** *(dict) --*

        An object that represents the specification of a TCP route.

        - **action** *(dict) --*

          The action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

    - **status** *(dict) --*

      The status of the route.

      - **status** *(string) --*

        The current status for the route.

    - **virtualRouterName** *(string) --*

      The virtual router that the route is associated with.
    """


_ClientDescribeRouteResponseTypeDef = TypedDict(
    "_ClientDescribeRouteResponseTypeDef",
    {"route": ClientDescribeRouteResponserouteTypeDef},
    total=False,
)


class ClientDescribeRouteResponseTypeDef(_ClientDescribeRouteResponseTypeDef):
    """
    Type definition for `ClientDescribeRoute` `Response`

    - **route** *(dict) --*

      The full description of your route.

      - **meshName** *(string) --*

        The name of the service mesh that the route resides in.

      - **metadata** *(dict) --*

        The associated metadata for the route.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **routeName** *(string) --*

        The name of the route.

      - **spec** *(dict) --*

        The specifications of the route.

        - **grpcRoute** *(dict) --*

          An object that represents the specification of a GRPC route.

          - **action** *(dict) --*

            An object that represents the action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

          - **match** *(dict) --*

            An object that represents the criteria for determining a request match.

            - **metadata** *(list) --*

              An object that represents the data to match from the request.

              - *(dict) --*

                An object that represents the match metadata for the route.

                - **invert** *(boolean) --*

                  Specify ``True`` to match anything except the match criteria. The default value
                  is ``False`` .

                - **match** *(dict) --*

                  An object that represents the data to match from the request.

                  - **exact** *(string) --*

                    The value sent by the client must match the specified value exactly.

                  - **prefix** *(string) --*

                    The value sent by the client must begin with the specified characters.

                  - **range** *(dict) --*

                    An object that represents the range of values to match on.

                    - **end** *(integer) --*

                      The end of the range.

                    - **start** *(integer) --*

                      The start of the range.

                  - **regex** *(string) --*

                    The value sent by the client must include the specified characters.

                  - **suffix** *(string) --*

                    The value sent by the client must end with the specified characters.

                - **name** *(string) --*

                  The name of the route.

            - **methodName** *(string) --*

              The method name to match from the request. If you specify a name, you must also
              specify a ``serviceName`` .

            - **serviceName** *(string) --*

              The fully qualified domain name for the service to match from the request.

          - **retryPolicy** *(dict) --*

            An object that represents a retry policy.

            - **grpcRetryEvents** *(list) --*

              Specify at least one of the valid values.

              - *(string) --*

            - **httpRetryEvents** *(list) --*

              Specify at least one of the following values.

              * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
              510, and 511

              * **gateway-error** – HTTP status codes 502, 503, and 504

              * **client-error** – HTTP status code 409

              * **stream-error** – Retry on refused stream

              - *(string) --*

            - **maxRetries** *(integer) --*

              The maximum number of retry attempts.

            - **perRetryTimeout** *(dict) --*

              An object that represents a duration of time.

              - **unit** *(string) --*

                A unit of time.

              - **value** *(integer) --*

                A number of time units.

            - **tcpRetryEvents** *(list) --*

              Specify a valid value.

              - *(string) --*

        - **http2Route** *(dict) --*

          An object that represents the specification of an HTTP2 route.

          - **action** *(dict) --*

            An object that represents the action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

          - **match** *(dict) --*

            An object that represents the criteria for determining a request match.

            - **headers** *(list) --*

              An object that represents the client request headers to match on.

              - *(dict) --*

                An object that represents the HTTP header in the request.

                - **invert** *(boolean) --*

                  Specify ``True`` to match anything except the match criteria. The default value
                  is ``False`` .

                - **match** *(dict) --*

                  The ``HeaderMatchMethod`` object.

                  - **exact** *(string) --*

                    The value sent by the client must match the specified value exactly.

                  - **prefix** *(string) --*

                    The value sent by the client must begin with the specified characters.

                  - **range** *(dict) --*

                    An object that represents the range of values to match on.

                    - **end** *(integer) --*

                      The end of the range.

                    - **start** *(integer) --*

                      The start of the range.

                  - **regex** *(string) --*

                    The value sent by the client must include the specified characters.

                  - **suffix** *(string) --*

                    The value sent by the client must end with the specified characters.

                - **name** *(string) --*

                  A name for the HTTP header in the client request that will be matched on.

            - **method** *(string) --*

              The client request method to match on. Specify only one.

            - **prefix** *(string) --*

              Specifies the path to match requests with. This parameter must always start with
              ``/`` , which by itself matches all requests to the virtual service name. You can
              also match for path-based routing of requests. For example, if your virtual service
              name is ``my-service.local`` and you want the route to match requests to
              ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

            - **scheme** *(string) --*

              The client request scheme to match on. Specify only one.

          - **retryPolicy** *(dict) --*

            An object that represents a retry policy.

            - **httpRetryEvents** *(list) --*

              Specify at least one of the following values.

              * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
              510, and 511

              * **gateway-error** – HTTP status codes 502, 503, and 504

              * **client-error** – HTTP status code 409

              * **stream-error** – Retry on refused stream

              - *(string) --*

            - **maxRetries** *(integer) --*

              The maximum number of retry attempts.

            - **perRetryTimeout** *(dict) --*

              An object that represents a duration of time.

              - **unit** *(string) --*

                A unit of time.

              - **value** *(integer) --*

                A number of time units.

            - **tcpRetryEvents** *(list) --*

              Specify a valid value.

              - *(string) --*

        - **httpRoute** *(dict) --*

          An object that represents the specification of an HTTP route.

          - **action** *(dict) --*

            An object that represents the action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

          - **match** *(dict) --*

            An object that represents the criteria for determining a request match.

            - **headers** *(list) --*

              An object that represents the client request headers to match on.

              - *(dict) --*

                An object that represents the HTTP header in the request.

                - **invert** *(boolean) --*

                  Specify ``True`` to match anything except the match criteria. The default value
                  is ``False`` .

                - **match** *(dict) --*

                  The ``HeaderMatchMethod`` object.

                  - **exact** *(string) --*

                    The value sent by the client must match the specified value exactly.

                  - **prefix** *(string) --*

                    The value sent by the client must begin with the specified characters.

                  - **range** *(dict) --*

                    An object that represents the range of values to match on.

                    - **end** *(integer) --*

                      The end of the range.

                    - **start** *(integer) --*

                      The start of the range.

                  - **regex** *(string) --*

                    The value sent by the client must include the specified characters.

                  - **suffix** *(string) --*

                    The value sent by the client must end with the specified characters.

                - **name** *(string) --*

                  A name for the HTTP header in the client request that will be matched on.

            - **method** *(string) --*

              The client request method to match on. Specify only one.

            - **prefix** *(string) --*

              Specifies the path to match requests with. This parameter must always start with
              ``/`` , which by itself matches all requests to the virtual service name. You can
              also match for path-based routing of requests. For example, if your virtual service
              name is ``my-service.local`` and you want the route to match requests to
              ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

            - **scheme** *(string) --*

              The client request scheme to match on. Specify only one.

          - **retryPolicy** *(dict) --*

            An object that represents a retry policy.

            - **httpRetryEvents** *(list) --*

              Specify at least one of the following values.

              * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
              510, and 511

              * **gateway-error** – HTTP status codes 502, 503, and 504

              * **client-error** – HTTP status code 409

              * **stream-error** – Retry on refused stream

              - *(string) --*

            - **maxRetries** *(integer) --*

              The maximum number of retry attempts.

            - **perRetryTimeout** *(dict) --*

              An object that represents a duration of time.

              - **unit** *(string) --*

                A unit of time.

              - **value** *(integer) --*

                A number of time units.

            - **tcpRetryEvents** *(list) --*

              Specify a valid value.

              - *(string) --*

        - **priority** *(integer) --*

          The priority for the route. Routes are matched based on the specified value, where 0 is
          the highest priority.

        - **tcpRoute** *(dict) --*

          An object that represents the specification of a TCP route.

          - **action** *(dict) --*

            The action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

      - **status** *(dict) --*

        The status of the route.

        - **status** *(string) --*

          The current status for the route.

      - **virtualRouterName** *(string) --*

        The virtual router that the route is associated with.
    """


_ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNode` `metadata`

    The associated metadata for the virtual node.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNodespecbackends` `virtualService`

    Specifies a virtual service to use as a backend for a virtual node.

    - **virtualServiceName** *(string) --*

      The name of the virtual service that is acting as a virtual node backend.
    """


_ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    {
        "virtualService": ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNodespec` `backends`

    An object that represents the backends that a virtual node is expected to send outbound
    traffic to.

    - **virtualService** *(dict) --*

      Specifies a virtual service to use as a backend for a virtual node.

      - **virtualServiceName** *(string) --*

        The name of the virtual service that is acting as a virtual node backend.
    """


_ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": str,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNodespeclisteners` `healthCheck`

    The health check information for the listener.

    - **healthyThreshold** *(integer) --*

      The number of consecutive successful health checks that must occur before declaring
      listener healthy.

    - **intervalMillis** *(integer) --*

      The time period in milliseconds between each health check execution.

    - **path** *(string) --*

      The destination path for the health check request. This is required only if the
      specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

    - **port** *(integer) --*

      The destination port for the health check request. This port must match the port
      defined in the  PortMapping for the listener.

    - **protocol** *(string) --*

      The protocol for the health check request.

    - **timeoutMillis** *(integer) --*

      The amount of time to wait when receiving a response from the health check, in
      milliseconds.

    - **unhealthyThreshold** *(integer) --*

      The number of consecutive failed health checks that must occur before declaring a
      virtual node unhealthy.
    """


_ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": str},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNodespeclisteners` `portMapping`

    The port mapping information for the listener.

    - **port** *(integer) --*

      The port used for the port mapping.

    - **protocol** *(string) --*

      The protocol used for the port mapping. Specify one protocol.
    """


_ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    {
        "healthCheck": ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef,
        "portMapping": ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef,
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNodespec` `listeners`

    An object that represents a listener for a virtual node.

    - **healthCheck** *(dict) --*

      The health check information for the listener.

      - **healthyThreshold** *(integer) --*

        The number of consecutive successful health checks that must occur before declaring
        listener healthy.

      - **intervalMillis** *(integer) --*

        The time period in milliseconds between each health check execution.

      - **path** *(string) --*

        The destination path for the health check request. This is required only if the
        specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

      - **port** *(integer) --*

        The destination port for the health check request. This port must match the port
        defined in the  PortMapping for the listener.

      - **protocol** *(string) --*

        The protocol for the health check request.

      - **timeoutMillis** *(integer) --*

        The amount of time to wait when receiving a response from the health check, in
        milliseconds.

      - **unhealthyThreshold** *(integer) --*

        The number of consecutive failed health checks that must occur before declaring a
        virtual node unhealthy.

    - **portMapping** *(dict) --*

      The port mapping information for the listener.

      - **port** *(integer) --*

        The port used for the port mapping.

      - **protocol** *(string) --*

        The protocol used for the port mapping. Specify one protocol.
    """


_ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    {"path": str},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLog` `file`

    The file object to send virtual node access logs to.

    - **path** *(string) --*

      The file path to write access logs to. You can use ``/dev/stdout`` to send access
      logs to standard out and configure your Envoy container to use a log driver, such
      as ``awslogs`` , to export the access logs to a log storage service such as Amazon
      CloudWatch Logs. You can also specify a path in the Envoy container's file system
      to write the files to disk.

      .. note::

        The Envoy process must have write permissions to the path that you specify here.
        Otherwise, Envoy fails to bootstrap properly.
    """


_ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    {
        "file": ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNodespeclogging` `accessLog`

    The access log configuration for a virtual node.

    - **file** *(dict) --*

      The file object to send virtual node access logs to.

      - **path** *(string) --*

        The file path to write access logs to. You can use ``/dev/stdout`` to send access
        logs to standard out and configure your Envoy container to use a log driver, such
        as ``awslogs`` , to export the access logs to a log storage service such as Amazon
        CloudWatch Logs. You can also specify a path in the Envoy container's file system
        to write the files to disk.

        .. note::

          The Envoy process must have write permissions to the path that you specify here.
          Otherwise, Envoy fails to bootstrap properly.
    """


_ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef",
    {
        "accessLog": ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNodespec` `logging`

    The inbound and outbound access logging information for the virtual node.

    - **accessLog** *(dict) --*

      The access log configuration for a virtual node.

      - **file** *(dict) --*

        The file object to send virtual node access logs to.

        - **path** *(string) --*

          The file path to write access logs to. You can use ``/dev/stdout`` to send access
          logs to standard out and configure your Envoy container to use a log driver, such
          as ``awslogs`` , to export the access logs to a log storage service such as Amazon
          CloudWatch Logs. You can also specify a path in the Envoy container's file system
          to write the files to disk.

          .. note::

            The Envoy process must have write permissions to the path that you specify here.
            Otherwise, Envoy fails to bootstrap properly.
    """


_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMap` `attributes`

    An object that represents the AWS Cloud Map attribute information for your virtual
    node.

    - **key** *(string) --*

      The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
      service instance that contains the specified key and value is returned.

    - **value** *(string) --*

      The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
      service instance that contains the specified key and value is returned.
    """


_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscovery` `awsCloudMap`

    Specifies any AWS Cloud Map information for the virtual node.

    - **attributes** *(list) --*

      A string map that contains attributes with values that you can use to filter
      instances by any custom attribute that you specified when you registered the
      instance. Only instances that match all of the specified key/value pairs will be
      returned.

      - *(dict) --*

        An object that represents the AWS Cloud Map attribute information for your virtual
        node.

        - **key** *(string) --*

          The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
          service instance that contains the specified key and value is returned.

        - **value** *(string) --*

          The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
          service instance that contains the specified key and value is returned.

    - **namespaceName** *(string) --*

      The name of the AWS Cloud Map namespace to use.

    - **serviceName** *(string) --*

      The name of the AWS Cloud Map service to use.
    """


_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    {"hostname": str},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscovery` `dns`

    Specifies the DNS information for the virtual node.

    - **hostname** *(string) --*

      Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNodespec` `serviceDiscovery`

    The service discovery information for the virtual node. If your virtual node does not
    expect ingress traffic, you can omit this parameter.

    - **awsCloudMap** *(dict) --*

      Specifies any AWS Cloud Map information for the virtual node.

      - **attributes** *(list) --*

        A string map that contains attributes with values that you can use to filter
        instances by any custom attribute that you specified when you registered the
        instance. Only instances that match all of the specified key/value pairs will be
        returned.

        - *(dict) --*

          An object that represents the AWS Cloud Map attribute information for your virtual
          node.

          - **key** *(string) --*

            The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
            service instance that contains the specified key and value is returned.

          - **value** *(string) --*

            The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
            service instance that contains the specified key and value is returned.

      - **namespaceName** *(string) --*

        The name of the AWS Cloud Map namespace to use.

      - **serviceName** *(string) --*

        The name of the AWS Cloud Map service to use.

    - **dns** *(dict) --*

      Specifies the DNS information for the virtual node.

      - **hostname** *(string) --*

        Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef",
    {
        "backends": List[
            ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef
        ],
        "listeners": List[
            ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef
        ],
        "logging": ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNode` `spec`

    The specifications of the virtual node.

    - **backends** *(list) --*

      The backends that the virtual node is expected to send outbound traffic to.

      - *(dict) --*

        An object that represents the backends that a virtual node is expected to send outbound
        traffic to.

        - **virtualService** *(dict) --*

          Specifies a virtual service to use as a backend for a virtual node.

          - **virtualServiceName** *(string) --*

            The name of the virtual service that is acting as a virtual node backend.

    - **listeners** *(list) --*

      The listeners that the virtual node is expected to receive inbound traffic from. You can
      specify one listener.

      - *(dict) --*

        An object that represents a listener for a virtual node.

        - **healthCheck** *(dict) --*

          The health check information for the listener.

          - **healthyThreshold** *(integer) --*

            The number of consecutive successful health checks that must occur before declaring
            listener healthy.

          - **intervalMillis** *(integer) --*

            The time period in milliseconds between each health check execution.

          - **path** *(string) --*

            The destination path for the health check request. This is required only if the
            specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

          - **port** *(integer) --*

            The destination port for the health check request. This port must match the port
            defined in the  PortMapping for the listener.

          - **protocol** *(string) --*

            The protocol for the health check request.

          - **timeoutMillis** *(integer) --*

            The amount of time to wait when receiving a response from the health check, in
            milliseconds.

          - **unhealthyThreshold** *(integer) --*

            The number of consecutive failed health checks that must occur before declaring a
            virtual node unhealthy.

        - **portMapping** *(dict) --*

          The port mapping information for the listener.

          - **port** *(integer) --*

            The port used for the port mapping.

          - **protocol** *(string) --*

            The protocol used for the port mapping. Specify one protocol.

    - **logging** *(dict) --*

      The inbound and outbound access logging information for the virtual node.

      - **accessLog** *(dict) --*

        The access log configuration for a virtual node.

        - **file** *(dict) --*

          The file object to send virtual node access logs to.

          - **path** *(string) --*

            The file path to write access logs to. You can use ``/dev/stdout`` to send access
            logs to standard out and configure your Envoy container to use a log driver, such
            as ``awslogs`` , to export the access logs to a log storage service such as Amazon
            CloudWatch Logs. You can also specify a path in the Envoy container's file system
            to write the files to disk.

            .. note::

              The Envoy process must have write permissions to the path that you specify here.
              Otherwise, Envoy fails to bootstrap properly.

    - **serviceDiscovery** *(dict) --*

      The service discovery information for the virtual node. If your virtual node does not
      expect ingress traffic, you can omit this parameter.

      - **awsCloudMap** *(dict) --*

        Specifies any AWS Cloud Map information for the virtual node.

        - **attributes** *(list) --*

          A string map that contains attributes with values that you can use to filter
          instances by any custom attribute that you specified when you registered the
          instance. Only instances that match all of the specified key/value pairs will be
          returned.

          - *(dict) --*

            An object that represents the AWS Cloud Map attribute information for your virtual
            node.

            - **key** *(string) --*

              The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
              service instance that contains the specified key and value is returned.

            - **value** *(string) --*

              The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
              service instance that contains the specified key and value is returned.

        - **namespaceName** *(string) --*

          The name of the AWS Cloud Map namespace to use.

        - **serviceName** *(string) --*

          The name of the AWS Cloud Map service to use.

      - **dns** *(dict) --*

        Specifies the DNS information for the virtual node.

        - **hostname** *(string) --*

          Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef",
    {"status": str},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponsevirtualNode` `status`

    The current status for the virtual node.

    - **status** *(string) --*

      The current status of the virtual node.
    """


_ClientDescribeVirtualNodeResponsevirtualNodeTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodeTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef,
        "spec": ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef,
        "status": ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef,
        "virtualNodeName": str,
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodeTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodeTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNodeResponse` `virtualNode`

    The full description of your virtual node.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual node resides in.

    - **metadata** *(dict) --*

      The associated metadata for the virtual node.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The specifications of the virtual node.

      - **backends** *(list) --*

        The backends that the virtual node is expected to send outbound traffic to.

        - *(dict) --*

          An object that represents the backends that a virtual node is expected to send outbound
          traffic to.

          - **virtualService** *(dict) --*

            Specifies a virtual service to use as a backend for a virtual node.

            - **virtualServiceName** *(string) --*

              The name of the virtual service that is acting as a virtual node backend.

      - **listeners** *(list) --*

        The listeners that the virtual node is expected to receive inbound traffic from. You can
        specify one listener.

        - *(dict) --*

          An object that represents a listener for a virtual node.

          - **healthCheck** *(dict) --*

            The health check information for the listener.

            - **healthyThreshold** *(integer) --*

              The number of consecutive successful health checks that must occur before declaring
              listener healthy.

            - **intervalMillis** *(integer) --*

              The time period in milliseconds between each health check execution.

            - **path** *(string) --*

              The destination path for the health check request. This is required only if the
              specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

            - **port** *(integer) --*

              The destination port for the health check request. This port must match the port
              defined in the  PortMapping for the listener.

            - **protocol** *(string) --*

              The protocol for the health check request.

            - **timeoutMillis** *(integer) --*

              The amount of time to wait when receiving a response from the health check, in
              milliseconds.

            - **unhealthyThreshold** *(integer) --*

              The number of consecutive failed health checks that must occur before declaring a
              virtual node unhealthy.

          - **portMapping** *(dict) --*

            The port mapping information for the listener.

            - **port** *(integer) --*

              The port used for the port mapping.

            - **protocol** *(string) --*

              The protocol used for the port mapping. Specify one protocol.

      - **logging** *(dict) --*

        The inbound and outbound access logging information for the virtual node.

        - **accessLog** *(dict) --*

          The access log configuration for a virtual node.

          - **file** *(dict) --*

            The file object to send virtual node access logs to.

            - **path** *(string) --*

              The file path to write access logs to. You can use ``/dev/stdout`` to send access
              logs to standard out and configure your Envoy container to use a log driver, such
              as ``awslogs`` , to export the access logs to a log storage service such as Amazon
              CloudWatch Logs. You can also specify a path in the Envoy container's file system
              to write the files to disk.

              .. note::

                The Envoy process must have write permissions to the path that you specify here.
                Otherwise, Envoy fails to bootstrap properly.

      - **serviceDiscovery** *(dict) --*

        The service discovery information for the virtual node. If your virtual node does not
        expect ingress traffic, you can omit this parameter.

        - **awsCloudMap** *(dict) --*

          Specifies any AWS Cloud Map information for the virtual node.

          - **attributes** *(list) --*

            A string map that contains attributes with values that you can use to filter
            instances by any custom attribute that you specified when you registered the
            instance. Only instances that match all of the specified key/value pairs will be
            returned.

            - *(dict) --*

              An object that represents the AWS Cloud Map attribute information for your virtual
              node.

              - **key** *(string) --*

                The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                service instance that contains the specified key and value is returned.

              - **value** *(string) --*

                The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                service instance that contains the specified key and value is returned.

          - **namespaceName** *(string) --*

            The name of the AWS Cloud Map namespace to use.

          - **serviceName** *(string) --*

            The name of the AWS Cloud Map service to use.

        - **dns** *(dict) --*

          Specifies the DNS information for the virtual node.

          - **hostname** *(string) --*

            Specifies the DNS service discovery hostname for the virtual node.

    - **status** *(dict) --*

      The current status for the virtual node.

      - **status** *(string) --*

        The current status of the virtual node.

    - **virtualNodeName** *(string) --*

      The name of the virtual node.
    """


_ClientDescribeVirtualNodeResponseTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponseTypeDef",
    {"virtualNode": ClientDescribeVirtualNodeResponsevirtualNodeTypeDef},
    total=False,
)


class ClientDescribeVirtualNodeResponseTypeDef(
    _ClientDescribeVirtualNodeResponseTypeDef
):
    """
    Type definition for `ClientDescribeVirtualNode` `Response`

    - **virtualNode** *(dict) --*

      The full description of your virtual node.

      - **meshName** *(string) --*

        The name of the service mesh that the virtual node resides in.

      - **metadata** *(dict) --*

        The associated metadata for the virtual node.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The specifications of the virtual node.

        - **backends** *(list) --*

          The backends that the virtual node is expected to send outbound traffic to.

          - *(dict) --*

            An object that represents the backends that a virtual node is expected to send outbound
            traffic to.

            - **virtualService** *(dict) --*

              Specifies a virtual service to use as a backend for a virtual node.

              - **virtualServiceName** *(string) --*

                The name of the virtual service that is acting as a virtual node backend.

        - **listeners** *(list) --*

          The listeners that the virtual node is expected to receive inbound traffic from. You can
          specify one listener.

          - *(dict) --*

            An object that represents a listener for a virtual node.

            - **healthCheck** *(dict) --*

              The health check information for the listener.

              - **healthyThreshold** *(integer) --*

                The number of consecutive successful health checks that must occur before declaring
                listener healthy.

              - **intervalMillis** *(integer) --*

                The time period in milliseconds between each health check execution.

              - **path** *(string) --*

                The destination path for the health check request. This is required only if the
                specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

              - **port** *(integer) --*

                The destination port for the health check request. This port must match the port
                defined in the  PortMapping for the listener.

              - **protocol** *(string) --*

                The protocol for the health check request.

              - **timeoutMillis** *(integer) --*

                The amount of time to wait when receiving a response from the health check, in
                milliseconds.

              - **unhealthyThreshold** *(integer) --*

                The number of consecutive failed health checks that must occur before declaring a
                virtual node unhealthy.

            - **portMapping** *(dict) --*

              The port mapping information for the listener.

              - **port** *(integer) --*

                The port used for the port mapping.

              - **protocol** *(string) --*

                The protocol used for the port mapping. Specify one protocol.

        - **logging** *(dict) --*

          The inbound and outbound access logging information for the virtual node.

          - **accessLog** *(dict) --*

            The access log configuration for a virtual node.

            - **file** *(dict) --*

              The file object to send virtual node access logs to.

              - **path** *(string) --*

                The file path to write access logs to. You can use ``/dev/stdout`` to send access
                logs to standard out and configure your Envoy container to use a log driver, such
                as ``awslogs`` , to export the access logs to a log storage service such as Amazon
                CloudWatch Logs. You can also specify a path in the Envoy container's file system
                to write the files to disk.

                .. note::

                  The Envoy process must have write permissions to the path that you specify here.
                  Otherwise, Envoy fails to bootstrap properly.

        - **serviceDiscovery** *(dict) --*

          The service discovery information for the virtual node. If your virtual node does not
          expect ingress traffic, you can omit this parameter.

          - **awsCloudMap** *(dict) --*

            Specifies any AWS Cloud Map information for the virtual node.

            - **attributes** *(list) --*

              A string map that contains attributes with values that you can use to filter
              instances by any custom attribute that you specified when you registered the
              instance. Only instances that match all of the specified key/value pairs will be
              returned.

              - *(dict) --*

                An object that represents the AWS Cloud Map attribute information for your virtual
                node.

                - **key** *(string) --*

                  The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                  service instance that contains the specified key and value is returned.

                - **value** *(string) --*

                  The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                  service instance that contains the specified key and value is returned.

            - **namespaceName** *(string) --*

              The name of the AWS Cloud Map namespace to use.

            - **serviceName** *(string) --*

              The name of the AWS Cloud Map service to use.

          - **dns** *(dict) --*

            Specifies the DNS information for the virtual node.

            - **hostname** *(string) --*

              Specifies the DNS service discovery hostname for the virtual node.

      - **status** *(dict) --*

        The current status for the virtual node.

        - **status** *(string) --*

          The current status of the virtual node.

      - **virtualNodeName** *(string) --*

        The name of the virtual node.
    """


_ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef(
    _ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef
):
    """
    Type definition for `ClientDescribeVirtualRouterResponsevirtualRouter` `metadata`

    The associated metadata for the virtual router.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": str},
    total=False,
)


class ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef(
    _ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
):
    """
    Type definition for `ClientDescribeVirtualRouterResponsevirtualRouterspeclisteners` `portMapping`

    An object that represents a port mapping.

    - **port** *(integer) --*

      The port used for the port mapping.

    - **protocol** *(string) --*

      The protocol used for the port mapping. Specify one protocol.
    """


_ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    {
        "portMapping": ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
    },
    total=False,
)


class ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef(
    _ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef
):
    """
    Type definition for `ClientDescribeVirtualRouterResponsevirtualRouterspec` `listeners`

    An object that represents a virtual router listener.

    - **portMapping** *(dict) --*

      An object that represents a port mapping.

      - **port** *(integer) --*

        The port used for the port mapping.

      - **protocol** *(string) --*

        The protocol used for the port mapping. Specify one protocol.
    """


_ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef",
    {
        "listeners": List[
            ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef
        ]
    },
    total=False,
)


class ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef(
    _ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef
):
    """
    Type definition for `ClientDescribeVirtualRouterResponsevirtualRouter` `spec`

    The specifications of the virtual router.

    - **listeners** *(list) --*

      The listeners that the virtual router is expected to receive inbound traffic from. You
      can specify one listener.

      - *(dict) --*

        An object that represents a virtual router listener.

        - **portMapping** *(dict) --*

          An object that represents a port mapping.

          - **port** *(integer) --*

            The port used for the port mapping.

          - **protocol** *(string) --*

            The protocol used for the port mapping. Specify one protocol.
    """


_ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef",
    {"status": str},
    total=False,
)


class ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef(
    _ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef
):
    """
    Type definition for `ClientDescribeVirtualRouterResponsevirtualRouter` `status`

    The current status of the virtual router.

    - **status** *(string) --*

      The current status of the virtual router.
    """


_ClientDescribeVirtualRouterResponsevirtualRouterTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponsevirtualRouterTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef,
        "spec": ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef,
        "status": ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientDescribeVirtualRouterResponsevirtualRouterTypeDef(
    _ClientDescribeVirtualRouterResponsevirtualRouterTypeDef
):
    """
    Type definition for `ClientDescribeVirtualRouterResponse` `virtualRouter`

    The full description of your virtual router.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual router resides in.

    - **metadata** *(dict) --*

      The associated metadata for the virtual router.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The specifications of the virtual router.

      - **listeners** *(list) --*

        The listeners that the virtual router is expected to receive inbound traffic from. You
        can specify one listener.

        - *(dict) --*

          An object that represents a virtual router listener.

          - **portMapping** *(dict) --*

            An object that represents a port mapping.

            - **port** *(integer) --*

              The port used for the port mapping.

            - **protocol** *(string) --*

              The protocol used for the port mapping. Specify one protocol.

    - **status** *(dict) --*

      The current status of the virtual router.

      - **status** *(string) --*

        The current status of the virtual router.

    - **virtualRouterName** *(string) --*

      The name of the virtual router.
    """


_ClientDescribeVirtualRouterResponseTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponseTypeDef",
    {"virtualRouter": ClientDescribeVirtualRouterResponsevirtualRouterTypeDef},
    total=False,
)


class ClientDescribeVirtualRouterResponseTypeDef(
    _ClientDescribeVirtualRouterResponseTypeDef
):
    """
    Type definition for `ClientDescribeVirtualRouter` `Response`

    - **virtualRouter** *(dict) --*

      The full description of your virtual router.

      - **meshName** *(string) --*

        The name of the service mesh that the virtual router resides in.

      - **metadata** *(dict) --*

        The associated metadata for the virtual router.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The specifications of the virtual router.

        - **listeners** *(list) --*

          The listeners that the virtual router is expected to receive inbound traffic from. You
          can specify one listener.

          - *(dict) --*

            An object that represents a virtual router listener.

            - **portMapping** *(dict) --*

              An object that represents a port mapping.

              - **port** *(integer) --*

                The port used for the port mapping.

              - **protocol** *(string) --*

                The protocol used for the port mapping. Specify one protocol.

      - **status** *(dict) --*

        The current status of the virtual router.

        - **status** *(string) --*

          The current status of the virtual router.

      - **virtualRouterName** *(string) --*

        The name of the virtual router.
    """


_ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef
):
    """
    Type definition for `ClientDescribeVirtualServiceResponsevirtualService` `metadata`

    An object that represents metadata for a resource.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef
):
    """
    Type definition for `ClientDescribeVirtualServiceResponsevirtualServicespecprovider` `virtualNode`

    The virtual node associated with a virtual service.

    - **virtualNodeName** *(string) --*

      The name of the virtual node that is acting as a service provider.
    """


_ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef
):
    """
    Type definition for `ClientDescribeVirtualServiceResponsevirtualServicespecprovider` `virtualRouter`

    The virtual router associated with a virtual service.

    - **virtualRouterName** *(string) --*

      The name of the virtual router that is acting as a service provider.
    """


_ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef
):
    """
    Type definition for `ClientDescribeVirtualServiceResponsevirtualServicespec` `provider`

    The App Mesh object that is acting as the provider for a virtual service. You can specify
    a single virtual node or virtual router.

    - **virtualNode** *(dict) --*

      The virtual node associated with a virtual service.

      - **virtualNodeName** *(string) --*

        The name of the virtual node that is acting as a service provider.

    - **virtualRouter** *(dict) --*

      The virtual router associated with a virtual service.

      - **virtualRouterName** *(string) --*

        The name of the virtual router that is acting as a service provider.
    """


_ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef",
    {"provider": ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef},
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef
):
    """
    Type definition for `ClientDescribeVirtualServiceResponsevirtualService` `spec`

    The specifications of the virtual service.

    - **provider** *(dict) --*

      The App Mesh object that is acting as the provider for a virtual service. You can specify
      a single virtual node or virtual router.

      - **virtualNode** *(dict) --*

        The virtual node associated with a virtual service.

        - **virtualNodeName** *(string) --*

          The name of the virtual node that is acting as a service provider.

      - **virtualRouter** *(dict) --*

        The virtual router associated with a virtual service.

        - **virtualRouterName** *(string) --*

          The name of the virtual router that is acting as a service provider.
    """


_ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef",
    {"status": str},
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef
):
    """
    Type definition for `ClientDescribeVirtualServiceResponsevirtualService` `status`

    The current status of the virtual service.

    - **status** *(string) --*

      The current status of the virtual service.
    """


_ClientDescribeVirtualServiceResponsevirtualServiceTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServiceTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef,
        "spec": ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef,
        "status": ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef,
        "virtualServiceName": str,
    },
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServiceTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServiceTypeDef
):
    """
    Type definition for `ClientDescribeVirtualServiceResponse` `virtualService`

    The full description of your virtual service.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual service resides in.

    - **metadata** *(dict) --*

      An object that represents metadata for a resource.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The specifications of the virtual service.

      - **provider** *(dict) --*

        The App Mesh object that is acting as the provider for a virtual service. You can specify
        a single virtual node or virtual router.

        - **virtualNode** *(dict) --*

          The virtual node associated with a virtual service.

          - **virtualNodeName** *(string) --*

            The name of the virtual node that is acting as a service provider.

        - **virtualRouter** *(dict) --*

          The virtual router associated with a virtual service.

          - **virtualRouterName** *(string) --*

            The name of the virtual router that is acting as a service provider.

    - **status** *(dict) --*

      The current status of the virtual service.

      - **status** *(string) --*

        The current status of the virtual service.

    - **virtualServiceName** *(string) --*

      The name of the virtual service.
    """


_ClientDescribeVirtualServiceResponseTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponseTypeDef",
    {"virtualService": ClientDescribeVirtualServiceResponsevirtualServiceTypeDef},
    total=False,
)


class ClientDescribeVirtualServiceResponseTypeDef(
    _ClientDescribeVirtualServiceResponseTypeDef
):
    """
    Type definition for `ClientDescribeVirtualService` `Response`

    - **virtualService** *(dict) --*

      The full description of your virtual service.

      - **meshName** *(string) --*

        The name of the service mesh that the virtual service resides in.

      - **metadata** *(dict) --*

        An object that represents metadata for a resource.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The specifications of the virtual service.

        - **provider** *(dict) --*

          The App Mesh object that is acting as the provider for a virtual service. You can specify
          a single virtual node or virtual router.

          - **virtualNode** *(dict) --*

            The virtual node associated with a virtual service.

            - **virtualNodeName** *(string) --*

              The name of the virtual node that is acting as a service provider.

          - **virtualRouter** *(dict) --*

            The virtual router associated with a virtual service.

            - **virtualRouterName** *(string) --*

              The name of the virtual router that is acting as a service provider.

      - **status** *(dict) --*

        The current status of the virtual service.

        - **status** *(string) --*

          The current status of the virtual service.

      - **virtualServiceName** *(string) --*

        The name of the virtual service.
    """


_ClientListMeshesResponsemeshesTypeDef = TypedDict(
    "_ClientListMeshesResponsemeshesTypeDef", {"arn": str, "meshName": str}, total=False
)


class ClientListMeshesResponsemeshesTypeDef(_ClientListMeshesResponsemeshesTypeDef):
    """
    Type definition for `ClientListMeshesResponse` `meshes`

    An object that represents a service mesh returned by a list operation.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) of the service mesh.

    - **meshName** *(string) --*

      The name of the service mesh.
    """


_ClientListMeshesResponseTypeDef = TypedDict(
    "_ClientListMeshesResponseTypeDef",
    {"meshes": List[ClientListMeshesResponsemeshesTypeDef], "nextToken": str},
    total=False,
)


class ClientListMeshesResponseTypeDef(_ClientListMeshesResponseTypeDef):
    """
    Type definition for `ClientListMeshes` `Response`

    - **meshes** *(list) --*

      The list of existing service meshes.

      - *(dict) --*

        An object that represents a service mesh returned by a list operation.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) of the service mesh.

        - **meshName** *(string) --*

          The name of the service mesh.

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListMeshes`` request. When the results of a
      ``ListMeshes`` request exceed ``limit`` , you can use this value to retrieve the next page of
      results. This value is ``null`` when there are no more results to return.
    """


_ClientListRoutesResponseroutesTypeDef = TypedDict(
    "_ClientListRoutesResponseroutesTypeDef",
    {"arn": str, "meshName": str, "routeName": str, "virtualRouterName": str},
    total=False,
)


class ClientListRoutesResponseroutesTypeDef(_ClientListRoutesResponseroutesTypeDef):
    """
    Type definition for `ClientListRoutesResponse` `routes`

    An object that represents a route returned by a list operation.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the route.

    - **meshName** *(string) --*

      The name of the service mesh that the route resides in.

    - **routeName** *(string) --*

      The name of the route.

    - **virtualRouterName** *(string) --*

      The virtual router that the route is associated with.
    """


_ClientListRoutesResponseTypeDef = TypedDict(
    "_ClientListRoutesResponseTypeDef",
    {"nextToken": str, "routes": List[ClientListRoutesResponseroutesTypeDef]},
    total=False,
)


class ClientListRoutesResponseTypeDef(_ClientListRoutesResponseTypeDef):
    """
    Type definition for `ClientListRoutes` `Response`

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListRoutes`` request. When the results of a
      ``ListRoutes`` request exceed ``limit`` , you can use this value to retrieve the next page of
      results. This value is ``null`` when there are no more results to return.

    - **routes** *(list) --*

      The list of existing routes for the specified service mesh and virtual router.

      - *(dict) --*

        An object that represents a route returned by a list operation.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the route.

        - **meshName** *(string) --*

          The name of the service mesh that the route resides in.

        - **routeName** *(string) --*

          The name of the route.

        - **virtualRouterName** *(string) --*

          The virtual router that the route is associated with.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientListTagsForResourceResponsetagsTypeDef(
    _ClientListTagsForResourceResponsetagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `tags`

    Optional metadata that you apply to a resource to assist with categorization and
    organization. Each tag consists of a key and an optional value, both of which you define.
    Tag keys can have a maximum character length of 128 characters, and tag values can have a
    maximum length of 256 characters.

    - **key** *(string) --*

      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts
      like a category for more specific tag values.

    - **value** *(string) --*

      The optional part of a key-value pair that make up a tag. A ``value`` acts as a
      descriptor within a tag category (key).
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"nextToken": str, "tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListTagsForResource`` request. When the
      results of a ``ListTagsForResource`` request exceed ``limit`` , you can use this value to
      retrieve the next page of results. This value is ``null`` when there are no more results to
      return.

    - **tags** *(list) --*

      The tags for the resource.

      - *(dict) --*

        Optional metadata that you apply to a resource to assist with categorization and
        organization. Each tag consists of a key and an optional value, both of which you define.
        Tag keys can have a maximum character length of 128 characters, and tag values can have a
        maximum length of 256 characters.

        - **key** *(string) --*

          One part of a key-value pair that make up a tag. A ``key`` is a general label that acts
          like a category for more specific tag values.

        - **value** *(string) --*

          The optional part of a key-value pair that make up a tag. A ``value`` acts as a
          descriptor within a tag category (key).
    """


_ClientListVirtualNodesResponsevirtualNodesTypeDef = TypedDict(
    "_ClientListVirtualNodesResponsevirtualNodesTypeDef",
    {"arn": str, "meshName": str, "virtualNodeName": str},
    total=False,
)


class ClientListVirtualNodesResponsevirtualNodesTypeDef(
    _ClientListVirtualNodesResponsevirtualNodesTypeDef
):
    """
    Type definition for `ClientListVirtualNodesResponse` `virtualNodes`

    An object that represents a virtual node returned by a list operation.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the virtual node.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual node resides in.

    - **virtualNodeName** *(string) --*

      The name of the virtual node.
    """


_ClientListVirtualNodesResponseTypeDef = TypedDict(
    "_ClientListVirtualNodesResponseTypeDef",
    {
        "nextToken": str,
        "virtualNodes": List[ClientListVirtualNodesResponsevirtualNodesTypeDef],
    },
    total=False,
)


class ClientListVirtualNodesResponseTypeDef(_ClientListVirtualNodesResponseTypeDef):
    """
    Type definition for `ClientListVirtualNodes` `Response`

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListVirtualNodes`` request. When the results
      of a ``ListVirtualNodes`` request exceed ``limit`` , you can use this value to retrieve the
      next page of results. This value is ``null`` when there are no more results to return.

    - **virtualNodes** *(list) --*

      The list of existing virtual nodes for the specified service mesh.

      - *(dict) --*

        An object that represents a virtual node returned by a list operation.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the virtual node.

        - **meshName** *(string) --*

          The name of the service mesh that the virtual node resides in.

        - **virtualNodeName** *(string) --*

          The name of the virtual node.
    """


_ClientListVirtualRoutersResponsevirtualRoutersTypeDef = TypedDict(
    "_ClientListVirtualRoutersResponsevirtualRoutersTypeDef",
    {"arn": str, "meshName": str, "virtualRouterName": str},
    total=False,
)


class ClientListVirtualRoutersResponsevirtualRoutersTypeDef(
    _ClientListVirtualRoutersResponsevirtualRoutersTypeDef
):
    """
    Type definition for `ClientListVirtualRoutersResponse` `virtualRouters`

    An object that represents a virtual router returned by a list operation.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the virtual router.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual router resides in.

    - **virtualRouterName** *(string) --*

      The name of the virtual router.
    """


_ClientListVirtualRoutersResponseTypeDef = TypedDict(
    "_ClientListVirtualRoutersResponseTypeDef",
    {
        "nextToken": str,
        "virtualRouters": List[ClientListVirtualRoutersResponsevirtualRoutersTypeDef],
    },
    total=False,
)


class ClientListVirtualRoutersResponseTypeDef(_ClientListVirtualRoutersResponseTypeDef):
    """
    Type definition for `ClientListVirtualRouters` `Response`

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListVirtualRouters`` request. When the
      results of a ``ListVirtualRouters`` request exceed ``limit`` , you can use this value to
      retrieve the next page of results. This value is ``null`` when there are no more results to
      return.

    - **virtualRouters** *(list) --*

      The list of existing virtual routers for the specified service mesh.

      - *(dict) --*

        An object that represents a virtual router returned by a list operation.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the virtual router.

        - **meshName** *(string) --*

          The name of the service mesh that the virtual router resides in.

        - **virtualRouterName** *(string) --*

          The name of the virtual router.
    """


_ClientListVirtualServicesResponsevirtualServicesTypeDef = TypedDict(
    "_ClientListVirtualServicesResponsevirtualServicesTypeDef",
    {"arn": str, "meshName": str, "virtualServiceName": str},
    total=False,
)


class ClientListVirtualServicesResponsevirtualServicesTypeDef(
    _ClientListVirtualServicesResponsevirtualServicesTypeDef
):
    """
    Type definition for `ClientListVirtualServicesResponse` `virtualServices`

    An object that represents a virtual service returned by a list operation.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the virtual service.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual service resides in.

    - **virtualServiceName** *(string) --*

      The name of the virtual service.
    """


_ClientListVirtualServicesResponseTypeDef = TypedDict(
    "_ClientListVirtualServicesResponseTypeDef",
    {
        "nextToken": str,
        "virtualServices": List[
            ClientListVirtualServicesResponsevirtualServicesTypeDef
        ],
    },
    total=False,
)


class ClientListVirtualServicesResponseTypeDef(
    _ClientListVirtualServicesResponseTypeDef
):
    """
    Type definition for `ClientListVirtualServices` `Response`

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListVirtualServices`` request. When the
      results of a ``ListVirtualServices`` request exceed ``limit`` , you can use this value to
      retrieve the next page of results. This value is ``null`` when there are no more results to
      return.

    - **virtualServices** *(list) --*

      The list of existing virtual services for the specified service mesh.

      - *(dict) --*

        An object that represents a virtual service returned by a list operation.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the virtual service.

        - **meshName** *(string) --*

          The name of the service mesh that the virtual service resides in.

        - **virtualServiceName** *(string) --*

          The name of the virtual service.
    """


_RequiredClientTagResourcetagsTypeDef = TypedDict(
    "_RequiredClientTagResourcetagsTypeDef", {"key": str}
)
_OptionalClientTagResourcetagsTypeDef = TypedDict(
    "_OptionalClientTagResourcetagsTypeDef", {"value": str}, total=False
)


class ClientTagResourcetagsTypeDef(
    _RequiredClientTagResourcetagsTypeDef, _OptionalClientTagResourcetagsTypeDef
):
    """
    Type definition for `ClientTagResource` `tags`

    Optional metadata that you apply to a resource to assist with categorization and organization.
    Each tag consists of a key and an optional value, both of which you define. Tag keys can have a
    maximum character length of 128 characters, and tag values can have a maximum length of 256
    characters.

    - **key** *(string) --* **[REQUIRED]**

      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
      a category for more specific tag values.

    - **value** *(string) --*

      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
      within a tag category (key).
    """


_ClientUpdateMeshResponsemeshmetadataTypeDef = TypedDict(
    "_ClientUpdateMeshResponsemeshmetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientUpdateMeshResponsemeshmetadataTypeDef(
    _ClientUpdateMeshResponsemeshmetadataTypeDef
):
    """
    Type definition for `ClientUpdateMeshResponsemesh` `metadata`

    The associated metadata for the service mesh.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientUpdateMeshResponsemeshspecegressFilterTypeDef = TypedDict(
    "_ClientUpdateMeshResponsemeshspecegressFilterTypeDef", {"type": str}, total=False
)


class ClientUpdateMeshResponsemeshspecegressFilterTypeDef(
    _ClientUpdateMeshResponsemeshspecegressFilterTypeDef
):
    """
    Type definition for `ClientUpdateMeshResponsemeshspec` `egressFilter`

    The egress filter rules for the service mesh.

    - **type** *(string) --*

      The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
      from virtual nodes to other defined resources in the service mesh (and any traffic to
      ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
      ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientUpdateMeshResponsemeshspecTypeDef = TypedDict(
    "_ClientUpdateMeshResponsemeshspecTypeDef",
    {"egressFilter": ClientUpdateMeshResponsemeshspecegressFilterTypeDef},
    total=False,
)


class ClientUpdateMeshResponsemeshspecTypeDef(_ClientUpdateMeshResponsemeshspecTypeDef):
    """
    Type definition for `ClientUpdateMeshResponsemesh` `spec`

    The associated specification for the service mesh.

    - **egressFilter** *(dict) --*

      The egress filter rules for the service mesh.

      - **type** *(string) --*

        The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
        from virtual nodes to other defined resources in the service mesh (and any traffic to
        ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
        ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientUpdateMeshResponsemeshstatusTypeDef = TypedDict(
    "_ClientUpdateMeshResponsemeshstatusTypeDef", {"status": str}, total=False
)


class ClientUpdateMeshResponsemeshstatusTypeDef(
    _ClientUpdateMeshResponsemeshstatusTypeDef
):
    """
    Type definition for `ClientUpdateMeshResponsemesh` `status`

    The status of the service mesh.

    - **status** *(string) --*

      The current mesh status.
    """


_ClientUpdateMeshResponsemeshTypeDef = TypedDict(
    "_ClientUpdateMeshResponsemeshTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateMeshResponsemeshmetadataTypeDef,
        "spec": ClientUpdateMeshResponsemeshspecTypeDef,
        "status": ClientUpdateMeshResponsemeshstatusTypeDef,
    },
    total=False,
)


class ClientUpdateMeshResponsemeshTypeDef(_ClientUpdateMeshResponsemeshTypeDef):
    """
    Type definition for `ClientUpdateMeshResponse` `mesh`

    An object that represents a service mesh returned by a describe operation.

    - **meshName** *(string) --*

      The name of the service mesh.

    - **metadata** *(dict) --*

      The associated metadata for the service mesh.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The associated specification for the service mesh.

      - **egressFilter** *(dict) --*

        The egress filter rules for the service mesh.

        - **type** *(string) --*

          The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
          from virtual nodes to other defined resources in the service mesh (and any traffic to
          ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
          ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.

    - **status** *(dict) --*

      The status of the service mesh.

      - **status** *(string) --*

        The current mesh status.
    """


_ClientUpdateMeshResponseTypeDef = TypedDict(
    "_ClientUpdateMeshResponseTypeDef",
    {"mesh": ClientUpdateMeshResponsemeshTypeDef},
    total=False,
)


class ClientUpdateMeshResponseTypeDef(_ClientUpdateMeshResponseTypeDef):
    """
    Type definition for `ClientUpdateMesh` `Response`

    - **mesh** *(dict) --*

      An object that represents a service mesh returned by a describe operation.

      - **meshName** *(string) --*

        The name of the service mesh.

      - **metadata** *(dict) --*

        The associated metadata for the service mesh.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The associated specification for the service mesh.

        - **egressFilter** *(dict) --*

          The egress filter rules for the service mesh.

          - **type** *(string) --*

            The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
            from virtual nodes to other defined resources in the service mesh (and any traffic to
            ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
            ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.

      - **status** *(dict) --*

        The status of the service mesh.

        - **status** *(string) --*

          The current mesh status.
    """


_ClientUpdateMeshspecegressFilterTypeDef = TypedDict(
    "_ClientUpdateMeshspecegressFilterTypeDef", {"type": str}
)


class ClientUpdateMeshspecegressFilterTypeDef(_ClientUpdateMeshspecegressFilterTypeDef):
    """
    Type definition for `ClientUpdateMeshspec` `egressFilter`

    The egress filter rules for the service mesh.

    - **type** *(string) --* **[REQUIRED]**

      The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only from
      virtual nodes to other defined resources in the service mesh (and any traffic to
      ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to ``ALLOW_ALL``
      to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientUpdateMeshspecTypeDef = TypedDict(
    "_ClientUpdateMeshspecTypeDef",
    {"egressFilter": ClientUpdateMeshspecegressFilterTypeDef},
    total=False,
)


class ClientUpdateMeshspecTypeDef(_ClientUpdateMeshspecTypeDef):
    """
    Type definition for `ClientUpdateMesh` `spec`

    The service mesh specification to apply.

    - **egressFilter** *(dict) --*

      The egress filter rules for the service mesh.

      - **type** *(string) --* **[REQUIRED]**

        The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only from
        virtual nodes to other defined resources in the service mesh (and any traffic to
        ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to ``ALLOW_ALL``
        to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientUpdateRouteResponseroutemetadataTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutemetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientUpdateRouteResponseroutemetadataTypeDef(
    _ClientUpdateRouteResponseroutemetadataTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroute` `metadata`

    The associated metadata for the route.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespecgrpcRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespecgrpcRoute` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --*

      The end of the range.

    - **start** *(integer) --*

      The start of the range.
    """


_ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespecgrpcRoutematchmetadata` `match`

    An object that represents the data to match from the request.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --*

        The end of the range.

      - **start** *(integer) --*

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    {
        "invert": bool,
        "match": ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespecgrpcRoutematch` `metadata`

    An object that represents the match metadata for the route.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value
      is ``False`` .

    - **match** *(dict) --*

      An object that represents the data to match from the request.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --*

          The end of the range.

        - **start** *(integer) --*

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --*

      The name of the route.
    """


_ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[
            ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef
        ],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespecgrpcRoute` `match`

    An object that represents the criteria for determining a request match.

    - **metadata** *(list) --*

      An object that represents the data to match from the request.

      - *(dict) --*

        An object that represents the match metadata for the route.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value
          is ``False`` .

        - **match** *(dict) --*

          An object that represents the data to match from the request.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --*

              The end of the range.

            - **start** *(integer) --*

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --*

          The name of the route.

    - **methodName** *(string) --*

      The method name to match from the request. If you specify a name, you must also
      specify a ``serviceName`` .

    - **serviceName** *(string) --*

      The fully qualified domain name for the service to match from the request.
    """


_ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespecgrpcRouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[str],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespecgrpcRoute` `retryPolicy`

    An object that represents a retry policy.

    - **grpcRetryEvents** *(list) --*

      Specify at least one of the valid values.

      - *(string) --*

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
      510, and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --*

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --*

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_ClientUpdateRouteResponseroutespecgrpcRouteTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRouteTypeDef",
    {
        "action": ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef,
        "match": ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRouteTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRouteTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespec` `grpcRoute`

    An object that represents the specification of a GRPC route.

    - **action** *(dict) --*

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.

    - **match** *(dict) --*

      An object that represents the criteria for determining a request match.

      - **metadata** *(list) --*

        An object that represents the data to match from the request.

        - *(dict) --*

          An object that represents the match metadata for the route.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value
            is ``False`` .

          - **match** *(dict) --*

            An object that represents the data to match from the request.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --*

                The end of the range.

              - **start** *(integer) --*

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --*

            The name of the route.

      - **methodName** *(string) --*

        The method name to match from the request. If you specify a name, you must also
        specify a ``serviceName`` .

      - **serviceName** *(string) --*

        The fully qualified domain name for the service to match from the request.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **grpcRetryEvents** *(list) --*

        Specify at least one of the valid values.

        - *(string) --*

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
        510, and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --*

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --*

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttp2Routeaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttp2Route` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttp2Routematchheadersmatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --*

      The end of the range.

    - **start** *(integer) --*

      The start of the range.
    """


_ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttp2Routematchheaders` `match`

    The ``HeaderMatchMethod`` object.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --*

        The end of the range.

      - **start** *(integer) --*

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttp2Routematch` `headers`

    An object that represents the HTTP header in the request.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value
      is ``False`` .

    - **match** *(dict) --*

      The ``HeaderMatchMethod`` object.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --*

          The end of the range.

        - **start** *(integer) --*

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --*

      A name for the HTTP header in the client request that will be matched on.
    """


_ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef",
    {
        "headers": List[
            ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef
        ],
        "method": str,
        "prefix": str,
        "scheme": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttp2Route` `match`

    An object that represents the criteria for determining a request match.

    - **headers** *(list) --*

      An object that represents the client request headers to match on.

      - *(dict) --*

        An object that represents the HTTP header in the request.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value
          is ``False`` .

        - **match** *(dict) --*

          The ``HeaderMatchMethod`` object.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --*

              The end of the range.

            - **start** *(integer) --*

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --*

          A name for the HTTP header in the client request that will be matched on.

    - **method** *(string) --*

      The client request method to match on. Specify only one.

    - **prefix** *(string) --*

      Specifies the path to match requests with. This parameter must always start with
      ``/`` , which by itself matches all requests to the virtual service name. You can
      also match for path-based routing of requests. For example, if your virtual service
      name is ``my-service.local`` and you want the route to match requests to
      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

    - **scheme** *(string) --*

      The client request scheme to match on. Specify only one.
    """


_ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttp2RouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttp2Route` `retryPolicy`

    An object that represents a retry policy.

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
      510, and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --*

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --*

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_ClientUpdateRouteResponseroutespechttp2RouteTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RouteTypeDef",
    {
        "action": ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef,
        "match": ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RouteTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RouteTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespec` `http2Route`

    An object that represents the specification of an HTTP2 route.

    - **action** *(dict) --*

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.

    - **match** *(dict) --*

      An object that represents the criteria for determining a request match.

      - **headers** *(list) --*

        An object that represents the client request headers to match on.

        - *(dict) --*

          An object that represents the HTTP header in the request.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value
            is ``False`` .

          - **match** *(dict) --*

            The ``HeaderMatchMethod`` object.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --*

                The end of the range.

              - **start** *(integer) --*

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --*

            A name for the HTTP header in the client request that will be matched on.

      - **method** *(string) --*

        The client request method to match on. Specify only one.

      - **prefix** *(string) --*

        Specifies the path to match requests with. This parameter must always start with
        ``/`` , which by itself matches all requests to the virtual service name. You can
        also match for path-based routing of requests. For example, if your virtual service
        name is ``my-service.local`` and you want the route to match requests to
        ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

      - **scheme** *(string) --*

        The client request scheme to match on. Specify only one.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
        510, and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --*

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --*

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef(
    _ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttpRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientUpdateRouteResponseroutespechttpRouteactionTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRouteactionTypeDef(
    _ClientUpdateRouteResponseroutespechttpRouteactionTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttpRoute` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef(
    _ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttpRoutematchheadersmatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --*

      The end of the range.

    - **start** *(integer) --*

      The start of the range.
    """


_ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef(
    _ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttpRoutematchheaders` `match`

    The ``HeaderMatchMethod`` object.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --*

        The end of the range.

      - **start** *(integer) --*

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef(
    _ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttpRoutematch` `headers`

    An object that represents the HTTP header in the request.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value
      is ``False`` .

    - **match** *(dict) --*

      The ``HeaderMatchMethod`` object.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --*

          The end of the range.

        - **start** *(integer) --*

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --*

      A name for the HTTP header in the client request that will be matched on.
    """


_ClientUpdateRouteResponseroutespechttpRoutematchTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRoutematchTypeDef",
    {
        "headers": List[ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef],
        "method": str,
        "prefix": str,
        "scheme": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRoutematchTypeDef(
    _ClientUpdateRouteResponseroutespechttpRoutematchTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttpRoute` `match`

    An object that represents the criteria for determining a request match.

    - **headers** *(list) --*

      An object that represents the client request headers to match on.

      - *(dict) --*

        An object that represents the HTTP header in the request.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value
          is ``False`` .

        - **match** *(dict) --*

          The ``HeaderMatchMethod`` object.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --*

              The end of the range.

            - **start** *(integer) --*

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --*

          A name for the HTTP header in the client request that will be matched on.

    - **method** *(string) --*

      The client request method to match on. Specify only one.

    - **prefix** *(string) --*

      Specifies the path to match requests with. This parameter must always start with
      ``/`` , which by itself matches all requests to the virtual service name. You can
      also match for path-based routing of requests. For example, if your virtual service
      name is ``my-service.local`` and you want the route to match requests to
      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

    - **scheme** *(string) --*

      The client request scheme to match on. Specify only one.
    """


_ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttpRouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef(
    _ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespechttpRoute` `retryPolicy`

    An object that represents a retry policy.

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
      510, and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --*

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --*

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_ClientUpdateRouteResponseroutespechttpRouteTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRouteTypeDef",
    {
        "action": ClientUpdateRouteResponseroutespechttpRouteactionTypeDef,
        "match": ClientUpdateRouteResponseroutespechttpRoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRouteTypeDef(
    _ClientUpdateRouteResponseroutespechttpRouteTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespec` `httpRoute`

    An object that represents the specification of an HTTP route.

    - **action** *(dict) --*

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.

    - **match** *(dict) --*

      An object that represents the criteria for determining a request match.

      - **headers** *(list) --*

        An object that represents the client request headers to match on.

        - *(dict) --*

          An object that represents the HTTP header in the request.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value
            is ``False`` .

          - **match** *(dict) --*

            The ``HeaderMatchMethod`` object.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --*

                The end of the range.

              - **start** *(integer) --*

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --*

            A name for the HTTP header in the client request that will be matched on.

      - **method** *(string) --*

        The client request method to match on. Specify only one.

      - **prefix** *(string) --*

        Specifies the path to match requests with. This parameter must always start with
        ``/`` , which by itself matches all requests to the virtual service name. You can
        also match for path-based routing of requests. For example, if your virtual service
        name is ``my-service.local`` and you want the route to match requests to
        ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

      - **scheme** *(string) --*

        The client request scheme to match on. Specify only one.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
        510, and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --*

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --*

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef(
    _ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespectcpRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed
    across targets according to their relative weight. For example, a weighted target
    with a relative weight of 50 receives five times as much traffic as one with a
    relative weight of 10. The total weight for all targets combined must be less than
    or equal to 100.

    - **virtualNode** *(string) --*

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --*

      The relative weight of the weighted target.
    """


_ClientUpdateRouteResponseroutespectcpRouteactionTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateRouteResponseroutespectcpRouteactionTypeDef(
    _ClientUpdateRouteResponseroutespectcpRouteactionTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespectcpRoute` `action`

    The action to take if a match is determined.

    - **weightedTargets** *(list) --*

      An object that represents the targets that traffic is routed to when a request
      matches the route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed
        across targets according to their relative weight. For example, a weighted target
        with a relative weight of 50 receives five times as much traffic as one with a
        relative weight of 10. The total weight for all targets combined must be less than
        or equal to 100.

        - **virtualNode** *(string) --*

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --*

          The relative weight of the weighted target.
    """


_ClientUpdateRouteResponseroutespectcpRouteTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespectcpRouteTypeDef",
    {"action": ClientUpdateRouteResponseroutespectcpRouteactionTypeDef},
    total=False,
)


class ClientUpdateRouteResponseroutespectcpRouteTypeDef(
    _ClientUpdateRouteResponseroutespectcpRouteTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroutespec` `tcpRoute`

    An object that represents the specification of a TCP route.

    - **action** *(dict) --*

      The action to take if a match is determined.

      - **weightedTargets** *(list) --*

        An object that represents the targets that traffic is routed to when a request
        matches the route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed
          across targets according to their relative weight. For example, a weighted target
          with a relative weight of 50 receives five times as much traffic as one with a
          relative weight of 10. The total weight for all targets combined must be less than
          or equal to 100.

          - **virtualNode** *(string) --*

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --*

            The relative weight of the weighted target.
    """


_ClientUpdateRouteResponseroutespecTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecTypeDef",
    {
        "grpcRoute": ClientUpdateRouteResponseroutespecgrpcRouteTypeDef,
        "http2Route": ClientUpdateRouteResponseroutespechttp2RouteTypeDef,
        "httpRoute": ClientUpdateRouteResponseroutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientUpdateRouteResponseroutespectcpRouteTypeDef,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecTypeDef(
    _ClientUpdateRouteResponseroutespecTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroute` `spec`

    The specifications of the route.

    - **grpcRoute** *(dict) --*

      An object that represents the specification of a GRPC route.

      - **action** *(dict) --*

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.

      - **match** *(dict) --*

        An object that represents the criteria for determining a request match.

        - **metadata** *(list) --*

          An object that represents the data to match from the request.

          - *(dict) --*

            An object that represents the match metadata for the route.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value
              is ``False`` .

            - **match** *(dict) --*

              An object that represents the data to match from the request.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --*

                  The end of the range.

                - **start** *(integer) --*

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --*

              The name of the route.

        - **methodName** *(string) --*

          The method name to match from the request. If you specify a name, you must also
          specify a ``serviceName`` .

        - **serviceName** *(string) --*

          The fully qualified domain name for the service to match from the request.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **grpcRetryEvents** *(list) --*

          Specify at least one of the valid values.

          - *(string) --*

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
          510, and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --*

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --*

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **http2Route** *(dict) --*

      An object that represents the specification of an HTTP2 route.

      - **action** *(dict) --*

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.

      - **match** *(dict) --*

        An object that represents the criteria for determining a request match.

        - **headers** *(list) --*

          An object that represents the client request headers to match on.

          - *(dict) --*

            An object that represents the HTTP header in the request.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value
              is ``False`` .

            - **match** *(dict) --*

              The ``HeaderMatchMethod`` object.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --*

                  The end of the range.

                - **start** *(integer) --*

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --*

              A name for the HTTP header in the client request that will be matched on.

        - **method** *(string) --*

          The client request method to match on. Specify only one.

        - **prefix** *(string) --*

          Specifies the path to match requests with. This parameter must always start with
          ``/`` , which by itself matches all requests to the virtual service name. You can
          also match for path-based routing of requests. For example, if your virtual service
          name is ``my-service.local`` and you want the route to match requests to
          ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

        - **scheme** *(string) --*

          The client request scheme to match on. Specify only one.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
          510, and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --*

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --*

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **httpRoute** *(dict) --*

      An object that represents the specification of an HTTP route.

      - **action** *(dict) --*

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.

      - **match** *(dict) --*

        An object that represents the criteria for determining a request match.

        - **headers** *(list) --*

          An object that represents the client request headers to match on.

          - *(dict) --*

            An object that represents the HTTP header in the request.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value
              is ``False`` .

            - **match** *(dict) --*

              The ``HeaderMatchMethod`` object.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --*

                  The end of the range.

                - **start** *(integer) --*

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --*

              A name for the HTTP header in the client request that will be matched on.

        - **method** *(string) --*

          The client request method to match on. Specify only one.

        - **prefix** *(string) --*

          Specifies the path to match requests with. This parameter must always start with
          ``/`` , which by itself matches all requests to the virtual service name. You can
          also match for path-based routing of requests. For example, if your virtual service
          name is ``my-service.local`` and you want the route to match requests to
          ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

        - **scheme** *(string) --*

          The client request scheme to match on. Specify only one.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
          510, and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --*

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --*

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **priority** *(integer) --*

      The priority for the route. Routes are matched based on the specified value, where 0 is
      the highest priority.

    - **tcpRoute** *(dict) --*

      An object that represents the specification of a TCP route.

      - **action** *(dict) --*

        The action to take if a match is determined.

        - **weightedTargets** *(list) --*

          An object that represents the targets that traffic is routed to when a request
          matches the route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target
            with a relative weight of 50 receives five times as much traffic as one with a
            relative weight of 10. The total weight for all targets combined must be less than
            or equal to 100.

            - **virtualNode** *(string) --*

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --*

              The relative weight of the weighted target.
    """


_ClientUpdateRouteResponseroutestatusTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutestatusTypeDef", {"status": str}, total=False
)


class ClientUpdateRouteResponseroutestatusTypeDef(
    _ClientUpdateRouteResponseroutestatusTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseroute` `status`

    The status of the route.

    - **status** *(string) --*

      The current status for the route.
    """


_ClientUpdateRouteResponserouteTypeDef = TypedDict(
    "_ClientUpdateRouteResponserouteTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateRouteResponseroutemetadataTypeDef,
        "routeName": str,
        "spec": ClientUpdateRouteResponseroutespecTypeDef,
        "status": ClientUpdateRouteResponseroutestatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientUpdateRouteResponserouteTypeDef(_ClientUpdateRouteResponserouteTypeDef):
    """
    Type definition for `ClientUpdateRouteResponse` `route`

    A full description of the route that was updated.

    - **meshName** *(string) --*

      The name of the service mesh that the route resides in.

    - **metadata** *(dict) --*

      The associated metadata for the route.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **routeName** *(string) --*

      The name of the route.

    - **spec** *(dict) --*

      The specifications of the route.

      - **grpcRoute** *(dict) --*

        An object that represents the specification of a GRPC route.

        - **action** *(dict) --*

          An object that represents the action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

        - **match** *(dict) --*

          An object that represents the criteria for determining a request match.

          - **metadata** *(list) --*

            An object that represents the data to match from the request.

            - *(dict) --*

              An object that represents the match metadata for the route.

              - **invert** *(boolean) --*

                Specify ``True`` to match anything except the match criteria. The default value
                is ``False`` .

              - **match** *(dict) --*

                An object that represents the data to match from the request.

                - **exact** *(string) --*

                  The value sent by the client must match the specified value exactly.

                - **prefix** *(string) --*

                  The value sent by the client must begin with the specified characters.

                - **range** *(dict) --*

                  An object that represents the range of values to match on.

                  - **end** *(integer) --*

                    The end of the range.

                  - **start** *(integer) --*

                    The start of the range.

                - **regex** *(string) --*

                  The value sent by the client must include the specified characters.

                - **suffix** *(string) --*

                  The value sent by the client must end with the specified characters.

              - **name** *(string) --*

                The name of the route.

          - **methodName** *(string) --*

            The method name to match from the request. If you specify a name, you must also
            specify a ``serviceName`` .

          - **serviceName** *(string) --*

            The fully qualified domain name for the service to match from the request.

        - **retryPolicy** *(dict) --*

          An object that represents a retry policy.

          - **grpcRetryEvents** *(list) --*

            Specify at least one of the valid values.

            - *(string) --*

          - **httpRetryEvents** *(list) --*

            Specify at least one of the following values.

            * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
            510, and 511

            * **gateway-error** – HTTP status codes 502, 503, and 504

            * **client-error** – HTTP status code 409

            * **stream-error** – Retry on refused stream

            - *(string) --*

          - **maxRetries** *(integer) --*

            The maximum number of retry attempts.

          - **perRetryTimeout** *(dict) --*

            An object that represents a duration of time.

            - **unit** *(string) --*

              A unit of time.

            - **value** *(integer) --*

              A number of time units.

          - **tcpRetryEvents** *(list) --*

            Specify a valid value.

            - *(string) --*

      - **http2Route** *(dict) --*

        An object that represents the specification of an HTTP2 route.

        - **action** *(dict) --*

          An object that represents the action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

        - **match** *(dict) --*

          An object that represents the criteria for determining a request match.

          - **headers** *(list) --*

            An object that represents the client request headers to match on.

            - *(dict) --*

              An object that represents the HTTP header in the request.

              - **invert** *(boolean) --*

                Specify ``True`` to match anything except the match criteria. The default value
                is ``False`` .

              - **match** *(dict) --*

                The ``HeaderMatchMethod`` object.

                - **exact** *(string) --*

                  The value sent by the client must match the specified value exactly.

                - **prefix** *(string) --*

                  The value sent by the client must begin with the specified characters.

                - **range** *(dict) --*

                  An object that represents the range of values to match on.

                  - **end** *(integer) --*

                    The end of the range.

                  - **start** *(integer) --*

                    The start of the range.

                - **regex** *(string) --*

                  The value sent by the client must include the specified characters.

                - **suffix** *(string) --*

                  The value sent by the client must end with the specified characters.

              - **name** *(string) --*

                A name for the HTTP header in the client request that will be matched on.

          - **method** *(string) --*

            The client request method to match on. Specify only one.

          - **prefix** *(string) --*

            Specifies the path to match requests with. This parameter must always start with
            ``/`` , which by itself matches all requests to the virtual service name. You can
            also match for path-based routing of requests. For example, if your virtual service
            name is ``my-service.local`` and you want the route to match requests to
            ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

          - **scheme** *(string) --*

            The client request scheme to match on. Specify only one.

        - **retryPolicy** *(dict) --*

          An object that represents a retry policy.

          - **httpRetryEvents** *(list) --*

            Specify at least one of the following values.

            * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
            510, and 511

            * **gateway-error** – HTTP status codes 502, 503, and 504

            * **client-error** – HTTP status code 409

            * **stream-error** – Retry on refused stream

            - *(string) --*

          - **maxRetries** *(integer) --*

            The maximum number of retry attempts.

          - **perRetryTimeout** *(dict) --*

            An object that represents a duration of time.

            - **unit** *(string) --*

              A unit of time.

            - **value** *(integer) --*

              A number of time units.

          - **tcpRetryEvents** *(list) --*

            Specify a valid value.

            - *(string) --*

      - **httpRoute** *(dict) --*

        An object that represents the specification of an HTTP route.

        - **action** *(dict) --*

          An object that represents the action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

        - **match** *(dict) --*

          An object that represents the criteria for determining a request match.

          - **headers** *(list) --*

            An object that represents the client request headers to match on.

            - *(dict) --*

              An object that represents the HTTP header in the request.

              - **invert** *(boolean) --*

                Specify ``True`` to match anything except the match criteria. The default value
                is ``False`` .

              - **match** *(dict) --*

                The ``HeaderMatchMethod`` object.

                - **exact** *(string) --*

                  The value sent by the client must match the specified value exactly.

                - **prefix** *(string) --*

                  The value sent by the client must begin with the specified characters.

                - **range** *(dict) --*

                  An object that represents the range of values to match on.

                  - **end** *(integer) --*

                    The end of the range.

                  - **start** *(integer) --*

                    The start of the range.

                - **regex** *(string) --*

                  The value sent by the client must include the specified characters.

                - **suffix** *(string) --*

                  The value sent by the client must end with the specified characters.

              - **name** *(string) --*

                A name for the HTTP header in the client request that will be matched on.

          - **method** *(string) --*

            The client request method to match on. Specify only one.

          - **prefix** *(string) --*

            Specifies the path to match requests with. This parameter must always start with
            ``/`` , which by itself matches all requests to the virtual service name. You can
            also match for path-based routing of requests. For example, if your virtual service
            name is ``my-service.local`` and you want the route to match requests to
            ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

          - **scheme** *(string) --*

            The client request scheme to match on. Specify only one.

        - **retryPolicy** *(dict) --*

          An object that represents a retry policy.

          - **httpRetryEvents** *(list) --*

            Specify at least one of the following values.

            * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
            510, and 511

            * **gateway-error** – HTTP status codes 502, 503, and 504

            * **client-error** – HTTP status code 409

            * **stream-error** – Retry on refused stream

            - *(string) --*

          - **maxRetries** *(integer) --*

            The maximum number of retry attempts.

          - **perRetryTimeout** *(dict) --*

            An object that represents a duration of time.

            - **unit** *(string) --*

              A unit of time.

            - **value** *(integer) --*

              A number of time units.

          - **tcpRetryEvents** *(list) --*

            Specify a valid value.

            - *(string) --*

      - **priority** *(integer) --*

        The priority for the route. Routes are matched based on the specified value, where 0 is
        the highest priority.

      - **tcpRoute** *(dict) --*

        An object that represents the specification of a TCP route.

        - **action** *(dict) --*

          The action to take if a match is determined.

          - **weightedTargets** *(list) --*

            An object that represents the targets that traffic is routed to when a request
            matches the route.

            - *(dict) --*

              An object that represents a target and its relative weight. Traffic is distributed
              across targets according to their relative weight. For example, a weighted target
              with a relative weight of 50 receives five times as much traffic as one with a
              relative weight of 10. The total weight for all targets combined must be less than
              or equal to 100.

              - **virtualNode** *(string) --*

                The virtual node to associate with the weighted target.

              - **weight** *(integer) --*

                The relative weight of the weighted target.

    - **status** *(dict) --*

      The status of the route.

      - **status** *(string) --*

        The current status for the route.

    - **virtualRouterName** *(string) --*

      The virtual router that the route is associated with.
    """


_ClientUpdateRouteResponseTypeDef = TypedDict(
    "_ClientUpdateRouteResponseTypeDef",
    {"route": ClientUpdateRouteResponserouteTypeDef},
    total=False,
)


class ClientUpdateRouteResponseTypeDef(_ClientUpdateRouteResponseTypeDef):
    """
    Type definition for `ClientUpdateRoute` `Response`

    - **route** *(dict) --*

      A full description of the route that was updated.

      - **meshName** *(string) --*

        The name of the service mesh that the route resides in.

      - **metadata** *(dict) --*

        The associated metadata for the route.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **routeName** *(string) --*

        The name of the route.

      - **spec** *(dict) --*

        The specifications of the route.

        - **grpcRoute** *(dict) --*

          An object that represents the specification of a GRPC route.

          - **action** *(dict) --*

            An object that represents the action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

          - **match** *(dict) --*

            An object that represents the criteria for determining a request match.

            - **metadata** *(list) --*

              An object that represents the data to match from the request.

              - *(dict) --*

                An object that represents the match metadata for the route.

                - **invert** *(boolean) --*

                  Specify ``True`` to match anything except the match criteria. The default value
                  is ``False`` .

                - **match** *(dict) --*

                  An object that represents the data to match from the request.

                  - **exact** *(string) --*

                    The value sent by the client must match the specified value exactly.

                  - **prefix** *(string) --*

                    The value sent by the client must begin with the specified characters.

                  - **range** *(dict) --*

                    An object that represents the range of values to match on.

                    - **end** *(integer) --*

                      The end of the range.

                    - **start** *(integer) --*

                      The start of the range.

                  - **regex** *(string) --*

                    The value sent by the client must include the specified characters.

                  - **suffix** *(string) --*

                    The value sent by the client must end with the specified characters.

                - **name** *(string) --*

                  The name of the route.

            - **methodName** *(string) --*

              The method name to match from the request. If you specify a name, you must also
              specify a ``serviceName`` .

            - **serviceName** *(string) --*

              The fully qualified domain name for the service to match from the request.

          - **retryPolicy** *(dict) --*

            An object that represents a retry policy.

            - **grpcRetryEvents** *(list) --*

              Specify at least one of the valid values.

              - *(string) --*

            - **httpRetryEvents** *(list) --*

              Specify at least one of the following values.

              * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
              510, and 511

              * **gateway-error** – HTTP status codes 502, 503, and 504

              * **client-error** – HTTP status code 409

              * **stream-error** – Retry on refused stream

              - *(string) --*

            - **maxRetries** *(integer) --*

              The maximum number of retry attempts.

            - **perRetryTimeout** *(dict) --*

              An object that represents a duration of time.

              - **unit** *(string) --*

                A unit of time.

              - **value** *(integer) --*

                A number of time units.

            - **tcpRetryEvents** *(list) --*

              Specify a valid value.

              - *(string) --*

        - **http2Route** *(dict) --*

          An object that represents the specification of an HTTP2 route.

          - **action** *(dict) --*

            An object that represents the action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

          - **match** *(dict) --*

            An object that represents the criteria for determining a request match.

            - **headers** *(list) --*

              An object that represents the client request headers to match on.

              - *(dict) --*

                An object that represents the HTTP header in the request.

                - **invert** *(boolean) --*

                  Specify ``True`` to match anything except the match criteria. The default value
                  is ``False`` .

                - **match** *(dict) --*

                  The ``HeaderMatchMethod`` object.

                  - **exact** *(string) --*

                    The value sent by the client must match the specified value exactly.

                  - **prefix** *(string) --*

                    The value sent by the client must begin with the specified characters.

                  - **range** *(dict) --*

                    An object that represents the range of values to match on.

                    - **end** *(integer) --*

                      The end of the range.

                    - **start** *(integer) --*

                      The start of the range.

                  - **regex** *(string) --*

                    The value sent by the client must include the specified characters.

                  - **suffix** *(string) --*

                    The value sent by the client must end with the specified characters.

                - **name** *(string) --*

                  A name for the HTTP header in the client request that will be matched on.

            - **method** *(string) --*

              The client request method to match on. Specify only one.

            - **prefix** *(string) --*

              Specifies the path to match requests with. This parameter must always start with
              ``/`` , which by itself matches all requests to the virtual service name. You can
              also match for path-based routing of requests. For example, if your virtual service
              name is ``my-service.local`` and you want the route to match requests to
              ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

            - **scheme** *(string) --*

              The client request scheme to match on. Specify only one.

          - **retryPolicy** *(dict) --*

            An object that represents a retry policy.

            - **httpRetryEvents** *(list) --*

              Specify at least one of the following values.

              * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
              510, and 511

              * **gateway-error** – HTTP status codes 502, 503, and 504

              * **client-error** – HTTP status code 409

              * **stream-error** – Retry on refused stream

              - *(string) --*

            - **maxRetries** *(integer) --*

              The maximum number of retry attempts.

            - **perRetryTimeout** *(dict) --*

              An object that represents a duration of time.

              - **unit** *(string) --*

                A unit of time.

              - **value** *(integer) --*

                A number of time units.

            - **tcpRetryEvents** *(list) --*

              Specify a valid value.

              - *(string) --*

        - **httpRoute** *(dict) --*

          An object that represents the specification of an HTTP route.

          - **action** *(dict) --*

            An object that represents the action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

          - **match** *(dict) --*

            An object that represents the criteria for determining a request match.

            - **headers** *(list) --*

              An object that represents the client request headers to match on.

              - *(dict) --*

                An object that represents the HTTP header in the request.

                - **invert** *(boolean) --*

                  Specify ``True`` to match anything except the match criteria. The default value
                  is ``False`` .

                - **match** *(dict) --*

                  The ``HeaderMatchMethod`` object.

                  - **exact** *(string) --*

                    The value sent by the client must match the specified value exactly.

                  - **prefix** *(string) --*

                    The value sent by the client must begin with the specified characters.

                  - **range** *(dict) --*

                    An object that represents the range of values to match on.

                    - **end** *(integer) --*

                      The end of the range.

                    - **start** *(integer) --*

                      The start of the range.

                  - **regex** *(string) --*

                    The value sent by the client must include the specified characters.

                  - **suffix** *(string) --*

                    The value sent by the client must end with the specified characters.

                - **name** *(string) --*

                  A name for the HTTP header in the client request that will be matched on.

            - **method** *(string) --*

              The client request method to match on. Specify only one.

            - **prefix** *(string) --*

              Specifies the path to match requests with. This parameter must always start with
              ``/`` , which by itself matches all requests to the virtual service name. You can
              also match for path-based routing of requests. For example, if your virtual service
              name is ``my-service.local`` and you want the route to match requests to
              ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

            - **scheme** *(string) --*

              The client request scheme to match on. Specify only one.

          - **retryPolicy** *(dict) --*

            An object that represents a retry policy.

            - **httpRetryEvents** *(list) --*

              Specify at least one of the following values.

              * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
              510, and 511

              * **gateway-error** – HTTP status codes 502, 503, and 504

              * **client-error** – HTTP status code 409

              * **stream-error** – Retry on refused stream

              - *(string) --*

            - **maxRetries** *(integer) --*

              The maximum number of retry attempts.

            - **perRetryTimeout** *(dict) --*

              An object that represents a duration of time.

              - **unit** *(string) --*

                A unit of time.

              - **value** *(integer) --*

                A number of time units.

            - **tcpRetryEvents** *(list) --*

              Specify a valid value.

              - *(string) --*

        - **priority** *(integer) --*

          The priority for the route. Routes are matched based on the specified value, where 0 is
          the highest priority.

        - **tcpRoute** *(dict) --*

          An object that represents the specification of a TCP route.

          - **action** *(dict) --*

            The action to take if a match is determined.

            - **weightedTargets** *(list) --*

              An object that represents the targets that traffic is routed to when a request
              matches the route.

              - *(dict) --*

                An object that represents a target and its relative weight. Traffic is distributed
                across targets according to their relative weight. For example, a weighted target
                with a relative weight of 50 receives five times as much traffic as one with a
                relative weight of 10. The total weight for all targets combined must be less than
                or equal to 100.

                - **virtualNode** *(string) --*

                  The virtual node to associate with the weighted target.

                - **weight** *(integer) --*

                  The relative weight of the weighted target.

      - **status** *(dict) --*

        The status of the route.

        - **status** *(string) --*

          The current status for the route.

      - **virtualRouterName** *(string) --*

        The virtual router that the route is associated with.
    """


_ClientUpdateRoutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRoutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
)


class ClientUpdateRoutespecgrpcRouteactionweightedTargetsTypeDef(
    _ClientUpdateRoutespecgrpcRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientUpdateRoutespecgrpcRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed across
    targets according to their relative weight. For example, a weighted target with a
    relative weight of 50 receives five times as much traffic as one with a relative weight
    of 10. The total weight for all targets combined must be less than or equal to 100.

    - **virtualNode** *(string) --* **[REQUIRED]**

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --* **[REQUIRED]**

      The relative weight of the weighted target.
    """


_ClientUpdateRoutespecgrpcRouteactionTypeDef = TypedDict(
    "_ClientUpdateRoutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRoutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
)


class ClientUpdateRoutespecgrpcRouteactionTypeDef(
    _ClientUpdateRoutespecgrpcRouteactionTypeDef
):
    """
    Type definition for `ClientUpdateRoutespecgrpcRoute` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --* **[REQUIRED]**

      An object that represents the targets that traffic is routed to when a request matches the
      route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed across
        targets according to their relative weight. For example, a weighted target with a
        relative weight of 50 receives five times as much traffic as one with a relative weight
        of 10. The total weight for all targets combined must be less than or equal to 100.

        - **virtualNode** *(string) --* **[REQUIRED]**

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --* **[REQUIRED]**

          The relative weight of the weighted target.
    """


_ClientUpdateRoutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "_ClientUpdateRoutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
)


class ClientUpdateRoutespecgrpcRoutematchmetadatamatchrangeTypeDef(
    _ClientUpdateRoutespecgrpcRoutematchmetadatamatchrangeTypeDef
):
    """
    Type definition for `ClientUpdateRoutespecgrpcRoutematchmetadatamatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --* **[REQUIRED]**

      The end of the range.

    - **start** *(integer) --* **[REQUIRED]**

      The start of the range.
    """


_ClientUpdateRoutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "_ClientUpdateRoutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRoutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientUpdateRoutespecgrpcRoutematchmetadatamatchTypeDef(
    _ClientUpdateRoutespecgrpcRoutematchmetadatamatchTypeDef
):
    """
    Type definition for `ClientUpdateRoutespecgrpcRoutematchmetadata` `match`

    An object that represents the data to match from the request.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --* **[REQUIRED]**

        The end of the range.

      - **start** *(integer) --* **[REQUIRED]**

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_RequiredClientUpdateRoutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_RequiredClientUpdateRoutespecgrpcRoutematchmetadataTypeDef", {"name": str}
)
_OptionalClientUpdateRoutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_OptionalClientUpdateRoutespecgrpcRoutematchmetadataTypeDef",
    {"invert": bool, "match": ClientUpdateRoutespecgrpcRoutematchmetadatamatchTypeDef},
    total=False,
)


class ClientUpdateRoutespecgrpcRoutematchmetadataTypeDef(
    _RequiredClientUpdateRoutespecgrpcRoutematchmetadataTypeDef,
    _OptionalClientUpdateRoutespecgrpcRoutematchmetadataTypeDef,
):
    """
    Type definition for `ClientUpdateRoutespecgrpcRoutematch` `metadata`

    An object that represents the match metadata for the route.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value is
      ``False`` .

    - **match** *(dict) --*

      An object that represents the data to match from the request.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --* **[REQUIRED]**

          The end of the range.

        - **start** *(integer) --* **[REQUIRED]**

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --* **[REQUIRED]**

      The name of the route.
    """


_ClientUpdateRoutespecgrpcRoutematchTypeDef = TypedDict(
    "_ClientUpdateRoutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientUpdateRoutespecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientUpdateRoutespecgrpcRoutematchTypeDef(
    _ClientUpdateRoutespecgrpcRoutematchTypeDef
):
    """
    Type definition for `ClientUpdateRoutespecgrpcRoute` `match`

    An object that represents the criteria for determining a request match.

    - **metadata** *(list) --*

      An object that represents the data to match from the request.

      - *(dict) --*

        An object that represents the match metadata for the route.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value is
          ``False`` .

        - **match** *(dict) --*

          An object that represents the data to match from the request.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --* **[REQUIRED]**

              The end of the range.

            - **start** *(integer) --* **[REQUIRED]**

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --* **[REQUIRED]**

          The name of the route.

    - **methodName** *(string) --*

      The method name to match from the request. If you specify a name, you must also specify a
      ``serviceName`` .

    - **serviceName** *(string) --*

      The fully qualified domain name for the service to match from the request.
    """


_ClientUpdateRoutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientUpdateRoutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientUpdateRoutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientUpdateRoutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientUpdateRoutespecgrpcRouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_RequiredClientUpdateRoutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_RequiredClientUpdateRoutespecgrpcRouteretryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRoutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
    },
)
_OptionalClientUpdateRoutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_OptionalClientUpdateRoutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[str],
        "httpRetryEvents": List[str],
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientUpdateRoutespecgrpcRouteretryPolicyTypeDef(
    _RequiredClientUpdateRoutespecgrpcRouteretryPolicyTypeDef,
    _OptionalClientUpdateRoutespecgrpcRouteretryPolicyTypeDef,
):
    """
    Type definition for `ClientUpdateRoutespecgrpcRoute` `retryPolicy`

    An object that represents a retry policy.

    - **grpcRetryEvents** *(list) --*

      Specify at least one of the valid values.

      - *(string) --*

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
      and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --* **[REQUIRED]**

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --* **[REQUIRED]**

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_RequiredClientUpdateRoutespecgrpcRouteTypeDef = TypedDict(
    "_RequiredClientUpdateRoutespecgrpcRouteTypeDef",
    {
        "action": ClientUpdateRoutespecgrpcRouteactionTypeDef,
        "match": ClientUpdateRoutespecgrpcRoutematchTypeDef,
    },
)
_OptionalClientUpdateRoutespecgrpcRouteTypeDef = TypedDict(
    "_OptionalClientUpdateRoutespecgrpcRouteTypeDef",
    {"retryPolicy": ClientUpdateRoutespecgrpcRouteretryPolicyTypeDef},
    total=False,
)


class ClientUpdateRoutespecgrpcRouteTypeDef(
    _RequiredClientUpdateRoutespecgrpcRouteTypeDef,
    _OptionalClientUpdateRoutespecgrpcRouteTypeDef,
):
    """
    Type definition for `ClientUpdateRoutespec` `grpcRoute`

    An object that represents the specification of a GRPC route.

    - **action** *(dict) --* **[REQUIRED]**

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --* **[REQUIRED]**

        An object that represents the targets that traffic is routed to when a request matches the
        route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed across
          targets according to their relative weight. For example, a weighted target with a
          relative weight of 50 receives five times as much traffic as one with a relative weight
          of 10. The total weight for all targets combined must be less than or equal to 100.

          - **virtualNode** *(string) --* **[REQUIRED]**

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --* **[REQUIRED]**

            The relative weight of the weighted target.

    - **match** *(dict) --* **[REQUIRED]**

      An object that represents the criteria for determining a request match.

      - **metadata** *(list) --*

        An object that represents the data to match from the request.

        - *(dict) --*

          An object that represents the match metadata for the route.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value is
            ``False`` .

          - **match** *(dict) --*

            An object that represents the data to match from the request.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --* **[REQUIRED]**

                The end of the range.

              - **start** *(integer) --* **[REQUIRED]**

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --* **[REQUIRED]**

            The name of the route.

      - **methodName** *(string) --*

        The method name to match from the request. If you specify a name, you must also specify a
        ``serviceName`` .

      - **serviceName** *(string) --*

        The fully qualified domain name for the service to match from the request.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **grpcRetryEvents** *(list) --*

        Specify at least one of the valid values.

        - *(string) --*

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
        and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --* **[REQUIRED]**

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --* **[REQUIRED]**

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientUpdateRoutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRoutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
)


class ClientUpdateRoutespechttp2RouteactionweightedTargetsTypeDef(
    _ClientUpdateRoutespechttp2RouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientUpdateRoutespechttp2Routeaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed across
    targets according to their relative weight. For example, a weighted target with a
    relative weight of 50 receives five times as much traffic as one with a relative weight
    of 10. The total weight for all targets combined must be less than or equal to 100.

    - **virtualNode** *(string) --* **[REQUIRED]**

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --* **[REQUIRED]**

      The relative weight of the weighted target.
    """


_ClientUpdateRoutespechttp2RouteactionTypeDef = TypedDict(
    "_ClientUpdateRoutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRoutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
)


class ClientUpdateRoutespechttp2RouteactionTypeDef(
    _ClientUpdateRoutespechttp2RouteactionTypeDef
):
    """
    Type definition for `ClientUpdateRoutespechttp2Route` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --* **[REQUIRED]**

      An object that represents the targets that traffic is routed to when a request matches the
      route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed across
        targets according to their relative weight. For example, a weighted target with a
        relative weight of 50 receives five times as much traffic as one with a relative weight
        of 10. The total weight for all targets combined must be less than or equal to 100.

        - **virtualNode** *(string) --* **[REQUIRED]**

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --* **[REQUIRED]**

          The relative weight of the weighted target.
    """


_ClientUpdateRoutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientUpdateRoutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
)


class ClientUpdateRoutespechttp2RoutematchheadersmatchrangeTypeDef(
    _ClientUpdateRoutespechttp2RoutematchheadersmatchrangeTypeDef
):
    """
    Type definition for `ClientUpdateRoutespechttp2Routematchheadersmatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --* **[REQUIRED]**

      The end of the range.

    - **start** *(integer) --* **[REQUIRED]**

      The start of the range.
    """


_ClientUpdateRoutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "_ClientUpdateRoutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRoutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientUpdateRoutespechttp2RoutematchheadersmatchTypeDef(
    _ClientUpdateRoutespechttp2RoutematchheadersmatchTypeDef
):
    """
    Type definition for `ClientUpdateRoutespechttp2Routematchheaders` `match`

    The ``HeaderMatchMethod`` object.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --* **[REQUIRED]**

        The end of the range.

      - **start** *(integer) --* **[REQUIRED]**

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_RequiredClientUpdateRoutespechttp2RoutematchheadersTypeDef = TypedDict(
    "_RequiredClientUpdateRoutespechttp2RoutematchheadersTypeDef", {"name": str}
)
_OptionalClientUpdateRoutespechttp2RoutematchheadersTypeDef = TypedDict(
    "_OptionalClientUpdateRoutespechttp2RoutematchheadersTypeDef",
    {"invert": bool, "match": ClientUpdateRoutespechttp2RoutematchheadersmatchTypeDef},
    total=False,
)


class ClientUpdateRoutespechttp2RoutematchheadersTypeDef(
    _RequiredClientUpdateRoutespechttp2RoutematchheadersTypeDef,
    _OptionalClientUpdateRoutespechttp2RoutematchheadersTypeDef,
):
    """
    Type definition for `ClientUpdateRoutespechttp2Routematch` `headers`

    An object that represents the HTTP header in the request.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value is
      ``False`` .

    - **match** *(dict) --*

      The ``HeaderMatchMethod`` object.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --* **[REQUIRED]**

          The end of the range.

        - **start** *(integer) --* **[REQUIRED]**

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --* **[REQUIRED]**

      A name for the HTTP header in the client request that will be matched on.
    """


_RequiredClientUpdateRoutespechttp2RoutematchTypeDef = TypedDict(
    "_RequiredClientUpdateRoutespechttp2RoutematchTypeDef", {"prefix": str}
)
_OptionalClientUpdateRoutespechttp2RoutematchTypeDef = TypedDict(
    "_OptionalClientUpdateRoutespechttp2RoutematchTypeDef",
    {
        "headers": List[ClientUpdateRoutespechttp2RoutematchheadersTypeDef],
        "method": str,
        "scheme": str,
    },
    total=False,
)


class ClientUpdateRoutespechttp2RoutematchTypeDef(
    _RequiredClientUpdateRoutespechttp2RoutematchTypeDef,
    _OptionalClientUpdateRoutespechttp2RoutematchTypeDef,
):
    """
    Type definition for `ClientUpdateRoutespechttp2Route` `match`

    An object that represents the criteria for determining a request match.

    - **headers** *(list) --*

      An object that represents the client request headers to match on.

      - *(dict) --*

        An object that represents the HTTP header in the request.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value is
          ``False`` .

        - **match** *(dict) --*

          The ``HeaderMatchMethod`` object.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --* **[REQUIRED]**

              The end of the range.

            - **start** *(integer) --* **[REQUIRED]**

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --* **[REQUIRED]**

          A name for the HTTP header in the client request that will be matched on.

    - **method** *(string) --*

      The client request method to match on. Specify only one.

    - **prefix** *(string) --* **[REQUIRED]**

      Specifies the path to match requests with. This parameter must always start with ``/`` ,
      which by itself matches all requests to the virtual service name. You can also match for
      path-based routing of requests. For example, if your virtual service name is
      ``my-service.local`` and you want the route to match requests to
      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

    - **scheme** *(string) --*

      The client request scheme to match on. Specify only one.
    """


_ClientUpdateRoutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientUpdateRoutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientUpdateRoutespechttp2RouteretryPolicyperRetryTimeoutTypeDef(
    _ClientUpdateRoutespechttp2RouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientUpdateRoutespechttp2RouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_RequiredClientUpdateRoutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "_RequiredClientUpdateRoutespechttp2RouteretryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRoutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
    },
)
_OptionalClientUpdateRoutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "_OptionalClientUpdateRoutespechttp2RouteretryPolicyTypeDef",
    {"httpRetryEvents": List[str], "tcpRetryEvents": List[str]},
    total=False,
)


class ClientUpdateRoutespechttp2RouteretryPolicyTypeDef(
    _RequiredClientUpdateRoutespechttp2RouteretryPolicyTypeDef,
    _OptionalClientUpdateRoutespechttp2RouteretryPolicyTypeDef,
):
    """
    Type definition for `ClientUpdateRoutespechttp2Route` `retryPolicy`

    An object that represents a retry policy.

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
      and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --* **[REQUIRED]**

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --* **[REQUIRED]**

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_RequiredClientUpdateRoutespechttp2RouteTypeDef = TypedDict(
    "_RequiredClientUpdateRoutespechttp2RouteTypeDef",
    {
        "action": ClientUpdateRoutespechttp2RouteactionTypeDef,
        "match": ClientUpdateRoutespechttp2RoutematchTypeDef,
    },
)
_OptionalClientUpdateRoutespechttp2RouteTypeDef = TypedDict(
    "_OptionalClientUpdateRoutespechttp2RouteTypeDef",
    {"retryPolicy": ClientUpdateRoutespechttp2RouteretryPolicyTypeDef},
    total=False,
)


class ClientUpdateRoutespechttp2RouteTypeDef(
    _RequiredClientUpdateRoutespechttp2RouteTypeDef,
    _OptionalClientUpdateRoutespechttp2RouteTypeDef,
):
    """
    Type definition for `ClientUpdateRoutespec` `http2Route`

    An object that represents the specification of an HTTP2 route.

    - **action** *(dict) --* **[REQUIRED]**

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --* **[REQUIRED]**

        An object that represents the targets that traffic is routed to when a request matches the
        route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed across
          targets according to their relative weight. For example, a weighted target with a
          relative weight of 50 receives five times as much traffic as one with a relative weight
          of 10. The total weight for all targets combined must be less than or equal to 100.

          - **virtualNode** *(string) --* **[REQUIRED]**

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --* **[REQUIRED]**

            The relative weight of the weighted target.

    - **match** *(dict) --* **[REQUIRED]**

      An object that represents the criteria for determining a request match.

      - **headers** *(list) --*

        An object that represents the client request headers to match on.

        - *(dict) --*

          An object that represents the HTTP header in the request.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value is
            ``False`` .

          - **match** *(dict) --*

            The ``HeaderMatchMethod`` object.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --* **[REQUIRED]**

                The end of the range.

              - **start** *(integer) --* **[REQUIRED]**

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --* **[REQUIRED]**

            A name for the HTTP header in the client request that will be matched on.

      - **method** *(string) --*

        The client request method to match on. Specify only one.

      - **prefix** *(string) --* **[REQUIRED]**

        Specifies the path to match requests with. This parameter must always start with ``/`` ,
        which by itself matches all requests to the virtual service name. You can also match for
        path-based routing of requests. For example, if your virtual service name is
        ``my-service.local`` and you want the route to match requests to
        ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

      - **scheme** *(string) --*

        The client request scheme to match on. Specify only one.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
        and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --* **[REQUIRED]**

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --* **[REQUIRED]**

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientUpdateRoutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRoutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
)


class ClientUpdateRoutespechttpRouteactionweightedTargetsTypeDef(
    _ClientUpdateRoutespechttpRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientUpdateRoutespechttpRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed across
    targets according to their relative weight. For example, a weighted target with a
    relative weight of 50 receives five times as much traffic as one with a relative weight
    of 10. The total weight for all targets combined must be less than or equal to 100.

    - **virtualNode** *(string) --* **[REQUIRED]**

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --* **[REQUIRED]**

      The relative weight of the weighted target.
    """


_ClientUpdateRoutespechttpRouteactionTypeDef = TypedDict(
    "_ClientUpdateRoutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRoutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
)


class ClientUpdateRoutespechttpRouteactionTypeDef(
    _ClientUpdateRoutespechttpRouteactionTypeDef
):
    """
    Type definition for `ClientUpdateRoutespechttpRoute` `action`

    An object that represents the action to take if a match is determined.

    - **weightedTargets** *(list) --* **[REQUIRED]**

      An object that represents the targets that traffic is routed to when a request matches the
      route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed across
        targets according to their relative weight. For example, a weighted target with a
        relative weight of 50 receives five times as much traffic as one with a relative weight
        of 10. The total weight for all targets combined must be less than or equal to 100.

        - **virtualNode** *(string) --* **[REQUIRED]**

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --* **[REQUIRED]**

          The relative weight of the weighted target.
    """


_ClientUpdateRoutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientUpdateRoutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
)


class ClientUpdateRoutespechttpRoutematchheadersmatchrangeTypeDef(
    _ClientUpdateRoutespechttpRoutematchheadersmatchrangeTypeDef
):
    """
    Type definition for `ClientUpdateRoutespechttpRoutematchheadersmatch` `range`

    An object that represents the range of values to match on.

    - **end** *(integer) --* **[REQUIRED]**

      The end of the range.

    - **start** *(integer) --* **[REQUIRED]**

      The start of the range.
    """


_ClientUpdateRoutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "_ClientUpdateRoutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRoutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientUpdateRoutespechttpRoutematchheadersmatchTypeDef(
    _ClientUpdateRoutespechttpRoutematchheadersmatchTypeDef
):
    """
    Type definition for `ClientUpdateRoutespechttpRoutematchheaders` `match`

    The ``HeaderMatchMethod`` object.

    - **exact** *(string) --*

      The value sent by the client must match the specified value exactly.

    - **prefix** *(string) --*

      The value sent by the client must begin with the specified characters.

    - **range** *(dict) --*

      An object that represents the range of values to match on.

      - **end** *(integer) --* **[REQUIRED]**

        The end of the range.

      - **start** *(integer) --* **[REQUIRED]**

        The start of the range.

    - **regex** *(string) --*

      The value sent by the client must include the specified characters.

    - **suffix** *(string) --*

      The value sent by the client must end with the specified characters.
    """


_RequiredClientUpdateRoutespechttpRoutematchheadersTypeDef = TypedDict(
    "_RequiredClientUpdateRoutespechttpRoutematchheadersTypeDef", {"name": str}
)
_OptionalClientUpdateRoutespechttpRoutematchheadersTypeDef = TypedDict(
    "_OptionalClientUpdateRoutespechttpRoutematchheadersTypeDef",
    {"invert": bool, "match": ClientUpdateRoutespechttpRoutematchheadersmatchTypeDef},
    total=False,
)


class ClientUpdateRoutespechttpRoutematchheadersTypeDef(
    _RequiredClientUpdateRoutespechttpRoutematchheadersTypeDef,
    _OptionalClientUpdateRoutespechttpRoutematchheadersTypeDef,
):
    """
    Type definition for `ClientUpdateRoutespechttpRoutematch` `headers`

    An object that represents the HTTP header in the request.

    - **invert** *(boolean) --*

      Specify ``True`` to match anything except the match criteria. The default value is
      ``False`` .

    - **match** *(dict) --*

      The ``HeaderMatchMethod`` object.

      - **exact** *(string) --*

        The value sent by the client must match the specified value exactly.

      - **prefix** *(string) --*

        The value sent by the client must begin with the specified characters.

      - **range** *(dict) --*

        An object that represents the range of values to match on.

        - **end** *(integer) --* **[REQUIRED]**

          The end of the range.

        - **start** *(integer) --* **[REQUIRED]**

          The start of the range.

      - **regex** *(string) --*

        The value sent by the client must include the specified characters.

      - **suffix** *(string) --*

        The value sent by the client must end with the specified characters.

    - **name** *(string) --* **[REQUIRED]**

      A name for the HTTP header in the client request that will be matched on.
    """


_RequiredClientUpdateRoutespechttpRoutematchTypeDef = TypedDict(
    "_RequiredClientUpdateRoutespechttpRoutematchTypeDef", {"prefix": str}
)
_OptionalClientUpdateRoutespechttpRoutematchTypeDef = TypedDict(
    "_OptionalClientUpdateRoutespechttpRoutematchTypeDef",
    {
        "headers": List[ClientUpdateRoutespechttpRoutematchheadersTypeDef],
        "method": str,
        "scheme": str,
    },
    total=False,
)


class ClientUpdateRoutespechttpRoutematchTypeDef(
    _RequiredClientUpdateRoutespechttpRoutematchTypeDef,
    _OptionalClientUpdateRoutespechttpRoutematchTypeDef,
):
    """
    Type definition for `ClientUpdateRoutespechttpRoute` `match`

    An object that represents the criteria for determining a request match.

    - **headers** *(list) --*

      An object that represents the client request headers to match on.

      - *(dict) --*

        An object that represents the HTTP header in the request.

        - **invert** *(boolean) --*

          Specify ``True`` to match anything except the match criteria. The default value is
          ``False`` .

        - **match** *(dict) --*

          The ``HeaderMatchMethod`` object.

          - **exact** *(string) --*

            The value sent by the client must match the specified value exactly.

          - **prefix** *(string) --*

            The value sent by the client must begin with the specified characters.

          - **range** *(dict) --*

            An object that represents the range of values to match on.

            - **end** *(integer) --* **[REQUIRED]**

              The end of the range.

            - **start** *(integer) --* **[REQUIRED]**

              The start of the range.

          - **regex** *(string) --*

            The value sent by the client must include the specified characters.

          - **suffix** *(string) --*

            The value sent by the client must end with the specified characters.

        - **name** *(string) --* **[REQUIRED]**

          A name for the HTTP header in the client request that will be matched on.

    - **method** *(string) --*

      The client request method to match on. Specify only one.

    - **prefix** *(string) --* **[REQUIRED]**

      Specifies the path to match requests with. This parameter must always start with ``/`` ,
      which by itself matches all requests to the virtual service name. You can also match for
      path-based routing of requests. For example, if your virtual service name is
      ``my-service.local`` and you want the route to match requests to
      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

    - **scheme** *(string) --*

      The client request scheme to match on. Specify only one.
    """


_ClientUpdateRoutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientUpdateRoutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": str, "value": int},
    total=False,
)


class ClientUpdateRoutespechttpRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientUpdateRoutespechttpRouteretryPolicyperRetryTimeoutTypeDef
):
    """
    Type definition for `ClientUpdateRoutespechttpRouteretryPolicy` `perRetryTimeout`

    An object that represents a duration of time.

    - **unit** *(string) --*

      A unit of time.

    - **value** *(integer) --*

      A number of time units.
    """


_RequiredClientUpdateRoutespechttpRouteretryPolicyTypeDef = TypedDict(
    "_RequiredClientUpdateRoutespechttpRouteretryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRoutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
    },
)
_OptionalClientUpdateRoutespechttpRouteretryPolicyTypeDef = TypedDict(
    "_OptionalClientUpdateRoutespechttpRouteretryPolicyTypeDef",
    {"httpRetryEvents": List[str], "tcpRetryEvents": List[str]},
    total=False,
)


class ClientUpdateRoutespechttpRouteretryPolicyTypeDef(
    _RequiredClientUpdateRoutespechttpRouteretryPolicyTypeDef,
    _OptionalClientUpdateRoutespechttpRouteretryPolicyTypeDef,
):
    """
    Type definition for `ClientUpdateRoutespechttpRoute` `retryPolicy`

    An object that represents a retry policy.

    - **httpRetryEvents** *(list) --*

      Specify at least one of the following values.

      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
      and 511

      * **gateway-error** – HTTP status codes 502, 503, and 504

      * **client-error** – HTTP status code 409

      * **stream-error** – Retry on refused stream

      - *(string) --*

    - **maxRetries** *(integer) --* **[REQUIRED]**

      The maximum number of retry attempts.

    - **perRetryTimeout** *(dict) --* **[REQUIRED]**

      An object that represents a duration of time.

      - **unit** *(string) --*

        A unit of time.

      - **value** *(integer) --*

        A number of time units.

    - **tcpRetryEvents** *(list) --*

      Specify a valid value.

      - *(string) --*
    """


_RequiredClientUpdateRoutespechttpRouteTypeDef = TypedDict(
    "_RequiredClientUpdateRoutespechttpRouteTypeDef",
    {
        "action": ClientUpdateRoutespechttpRouteactionTypeDef,
        "match": ClientUpdateRoutespechttpRoutematchTypeDef,
    },
)
_OptionalClientUpdateRoutespechttpRouteTypeDef = TypedDict(
    "_OptionalClientUpdateRoutespechttpRouteTypeDef",
    {"retryPolicy": ClientUpdateRoutespechttpRouteretryPolicyTypeDef},
    total=False,
)


class ClientUpdateRoutespechttpRouteTypeDef(
    _RequiredClientUpdateRoutespechttpRouteTypeDef,
    _OptionalClientUpdateRoutespechttpRouteTypeDef,
):
    """
    Type definition for `ClientUpdateRoutespec` `httpRoute`

    An object that represents the specification of an HTTP route.

    - **action** *(dict) --* **[REQUIRED]**

      An object that represents the action to take if a match is determined.

      - **weightedTargets** *(list) --* **[REQUIRED]**

        An object that represents the targets that traffic is routed to when a request matches the
        route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed across
          targets according to their relative weight. For example, a weighted target with a
          relative weight of 50 receives five times as much traffic as one with a relative weight
          of 10. The total weight for all targets combined must be less than or equal to 100.

          - **virtualNode** *(string) --* **[REQUIRED]**

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --* **[REQUIRED]**

            The relative weight of the weighted target.

    - **match** *(dict) --* **[REQUIRED]**

      An object that represents the criteria for determining a request match.

      - **headers** *(list) --*

        An object that represents the client request headers to match on.

        - *(dict) --*

          An object that represents the HTTP header in the request.

          - **invert** *(boolean) --*

            Specify ``True`` to match anything except the match criteria. The default value is
            ``False`` .

          - **match** *(dict) --*

            The ``HeaderMatchMethod`` object.

            - **exact** *(string) --*

              The value sent by the client must match the specified value exactly.

            - **prefix** *(string) --*

              The value sent by the client must begin with the specified characters.

            - **range** *(dict) --*

              An object that represents the range of values to match on.

              - **end** *(integer) --* **[REQUIRED]**

                The end of the range.

              - **start** *(integer) --* **[REQUIRED]**

                The start of the range.

            - **regex** *(string) --*

              The value sent by the client must include the specified characters.

            - **suffix** *(string) --*

              The value sent by the client must end with the specified characters.

          - **name** *(string) --* **[REQUIRED]**

            A name for the HTTP header in the client request that will be matched on.

      - **method** *(string) --*

        The client request method to match on. Specify only one.

      - **prefix** *(string) --* **[REQUIRED]**

        Specifies the path to match requests with. This parameter must always start with ``/`` ,
        which by itself matches all requests to the virtual service name. You can also match for
        path-based routing of requests. For example, if your virtual service name is
        ``my-service.local`` and you want the route to match requests to
        ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

      - **scheme** *(string) --*

        The client request scheme to match on. Specify only one.

    - **retryPolicy** *(dict) --*

      An object that represents a retry policy.

      - **httpRetryEvents** *(list) --*

        Specify at least one of the following values.

        * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
        and 511

        * **gateway-error** – HTTP status codes 502, 503, and 504

        * **client-error** – HTTP status code 409

        * **stream-error** – Retry on refused stream

        - *(string) --*

      - **maxRetries** *(integer) --* **[REQUIRED]**

        The maximum number of retry attempts.

      - **perRetryTimeout** *(dict) --* **[REQUIRED]**

        An object that represents a duration of time.

        - **unit** *(string) --*

          A unit of time.

        - **value** *(integer) --*

          A number of time units.

      - **tcpRetryEvents** *(list) --*

        Specify a valid value.

        - *(string) --*
    """


_ClientUpdateRoutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRoutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
)


class ClientUpdateRoutespectcpRouteactionweightedTargetsTypeDef(
    _ClientUpdateRoutespectcpRouteactionweightedTargetsTypeDef
):
    """
    Type definition for `ClientUpdateRoutespectcpRouteaction` `weightedTargets`

    An object that represents a target and its relative weight. Traffic is distributed across
    targets according to their relative weight. For example, a weighted target with a
    relative weight of 50 receives five times as much traffic as one with a relative weight
    of 10. The total weight for all targets combined must be less than or equal to 100.

    - **virtualNode** *(string) --* **[REQUIRED]**

      The virtual node to associate with the weighted target.

    - **weight** *(integer) --* **[REQUIRED]**

      The relative weight of the weighted target.
    """


_ClientUpdateRoutespectcpRouteactionTypeDef = TypedDict(
    "_ClientUpdateRoutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRoutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
)


class ClientUpdateRoutespectcpRouteactionTypeDef(
    _ClientUpdateRoutespectcpRouteactionTypeDef
):
    """
    Type definition for `ClientUpdateRoutespectcpRoute` `action`

    The action to take if a match is determined.

    - **weightedTargets** *(list) --* **[REQUIRED]**

      An object that represents the targets that traffic is routed to when a request matches the
      route.

      - *(dict) --*

        An object that represents a target and its relative weight. Traffic is distributed across
        targets according to their relative weight. For example, a weighted target with a
        relative weight of 50 receives five times as much traffic as one with a relative weight
        of 10. The total weight for all targets combined must be less than or equal to 100.

        - **virtualNode** *(string) --* **[REQUIRED]**

          The virtual node to associate with the weighted target.

        - **weight** *(integer) --* **[REQUIRED]**

          The relative weight of the weighted target.
    """


_ClientUpdateRoutespectcpRouteTypeDef = TypedDict(
    "_ClientUpdateRoutespectcpRouteTypeDef",
    {"action": ClientUpdateRoutespectcpRouteactionTypeDef},
)


class ClientUpdateRoutespectcpRouteTypeDef(_ClientUpdateRoutespectcpRouteTypeDef):
    """
    Type definition for `ClientUpdateRoutespec` `tcpRoute`

    An object that represents the specification of a TCP route.

    - **action** *(dict) --* **[REQUIRED]**

      The action to take if a match is determined.

      - **weightedTargets** *(list) --* **[REQUIRED]**

        An object that represents the targets that traffic is routed to when a request matches the
        route.

        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed across
          targets according to their relative weight. For example, a weighted target with a
          relative weight of 50 receives five times as much traffic as one with a relative weight
          of 10. The total weight for all targets combined must be less than or equal to 100.

          - **virtualNode** *(string) --* **[REQUIRED]**

            The virtual node to associate with the weighted target.

          - **weight** *(integer) --* **[REQUIRED]**

            The relative weight of the weighted target.
    """


_ClientUpdateRoutespecTypeDef = TypedDict(
    "_ClientUpdateRoutespecTypeDef",
    {
        "grpcRoute": ClientUpdateRoutespecgrpcRouteTypeDef,
        "http2Route": ClientUpdateRoutespechttp2RouteTypeDef,
        "httpRoute": ClientUpdateRoutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientUpdateRoutespectcpRouteTypeDef,
    },
    total=False,
)


class ClientUpdateRoutespecTypeDef(_ClientUpdateRoutespecTypeDef):
    """
    Type definition for `ClientUpdateRoute` `spec`

    The new route specification to apply. This overwrites the existing data.

    - **grpcRoute** *(dict) --*

      An object that represents the specification of a GRPC route.

      - **action** *(dict) --* **[REQUIRED]**

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --* **[REQUIRED]**

          An object that represents the targets that traffic is routed to when a request matches the
          route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed across
            targets according to their relative weight. For example, a weighted target with a
            relative weight of 50 receives five times as much traffic as one with a relative weight
            of 10. The total weight for all targets combined must be less than or equal to 100.

            - **virtualNode** *(string) --* **[REQUIRED]**

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --* **[REQUIRED]**

              The relative weight of the weighted target.

      - **match** *(dict) --* **[REQUIRED]**

        An object that represents the criteria for determining a request match.

        - **metadata** *(list) --*

          An object that represents the data to match from the request.

          - *(dict) --*

            An object that represents the match metadata for the route.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value is
              ``False`` .

            - **match** *(dict) --*

              An object that represents the data to match from the request.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --* **[REQUIRED]**

                  The end of the range.

                - **start** *(integer) --* **[REQUIRED]**

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --* **[REQUIRED]**

              The name of the route.

        - **methodName** *(string) --*

          The method name to match from the request. If you specify a name, you must also specify a
          ``serviceName`` .

        - **serviceName** *(string) --*

          The fully qualified domain name for the service to match from the request.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **grpcRetryEvents** *(list) --*

          Specify at least one of the valid values.

          - *(string) --*

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
          and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --* **[REQUIRED]**

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --* **[REQUIRED]**

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **http2Route** *(dict) --*

      An object that represents the specification of an HTTP2 route.

      - **action** *(dict) --* **[REQUIRED]**

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --* **[REQUIRED]**

          An object that represents the targets that traffic is routed to when a request matches the
          route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed across
            targets according to their relative weight. For example, a weighted target with a
            relative weight of 50 receives five times as much traffic as one with a relative weight
            of 10. The total weight for all targets combined must be less than or equal to 100.

            - **virtualNode** *(string) --* **[REQUIRED]**

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --* **[REQUIRED]**

              The relative weight of the weighted target.

      - **match** *(dict) --* **[REQUIRED]**

        An object that represents the criteria for determining a request match.

        - **headers** *(list) --*

          An object that represents the client request headers to match on.

          - *(dict) --*

            An object that represents the HTTP header in the request.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value is
              ``False`` .

            - **match** *(dict) --*

              The ``HeaderMatchMethod`` object.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --* **[REQUIRED]**

                  The end of the range.

                - **start** *(integer) --* **[REQUIRED]**

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --* **[REQUIRED]**

              A name for the HTTP header in the client request that will be matched on.

        - **method** *(string) --*

          The client request method to match on. Specify only one.

        - **prefix** *(string) --* **[REQUIRED]**

          Specifies the path to match requests with. This parameter must always start with ``/`` ,
          which by itself matches all requests to the virtual service name. You can also match for
          path-based routing of requests. For example, if your virtual service name is
          ``my-service.local`` and you want the route to match requests to
          ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

        - **scheme** *(string) --*

          The client request scheme to match on. Specify only one.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
          and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --* **[REQUIRED]**

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --* **[REQUIRED]**

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **httpRoute** *(dict) --*

      An object that represents the specification of an HTTP route.

      - **action** *(dict) --* **[REQUIRED]**

        An object that represents the action to take if a match is determined.

        - **weightedTargets** *(list) --* **[REQUIRED]**

          An object that represents the targets that traffic is routed to when a request matches the
          route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed across
            targets according to their relative weight. For example, a weighted target with a
            relative weight of 50 receives five times as much traffic as one with a relative weight
            of 10. The total weight for all targets combined must be less than or equal to 100.

            - **virtualNode** *(string) --* **[REQUIRED]**

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --* **[REQUIRED]**

              The relative weight of the weighted target.

      - **match** *(dict) --* **[REQUIRED]**

        An object that represents the criteria for determining a request match.

        - **headers** *(list) --*

          An object that represents the client request headers to match on.

          - *(dict) --*

            An object that represents the HTTP header in the request.

            - **invert** *(boolean) --*

              Specify ``True`` to match anything except the match criteria. The default value is
              ``False`` .

            - **match** *(dict) --*

              The ``HeaderMatchMethod`` object.

              - **exact** *(string) --*

                The value sent by the client must match the specified value exactly.

              - **prefix** *(string) --*

                The value sent by the client must begin with the specified characters.

              - **range** *(dict) --*

                An object that represents the range of values to match on.

                - **end** *(integer) --* **[REQUIRED]**

                  The end of the range.

                - **start** *(integer) --* **[REQUIRED]**

                  The start of the range.

              - **regex** *(string) --*

                The value sent by the client must include the specified characters.

              - **suffix** *(string) --*

                The value sent by the client must end with the specified characters.

            - **name** *(string) --* **[REQUIRED]**

              A name for the HTTP header in the client request that will be matched on.

        - **method** *(string) --*

          The client request method to match on. Specify only one.

        - **prefix** *(string) --* **[REQUIRED]**

          Specifies the path to match requests with. This parameter must always start with ``/`` ,
          which by itself matches all requests to the virtual service name. You can also match for
          path-based routing of requests. For example, if your virtual service name is
          ``my-service.local`` and you want the route to match requests to
          ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

        - **scheme** *(string) --*

          The client request scheme to match on. Specify only one.

      - **retryPolicy** *(dict) --*

        An object that represents a retry policy.

        - **httpRetryEvents** *(list) --*

          Specify at least one of the following values.

          * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
          and 511

          * **gateway-error** – HTTP status codes 502, 503, and 504

          * **client-error** – HTTP status code 409

          * **stream-error** – Retry on refused stream

          - *(string) --*

        - **maxRetries** *(integer) --* **[REQUIRED]**

          The maximum number of retry attempts.

        - **perRetryTimeout** *(dict) --* **[REQUIRED]**

          An object that represents a duration of time.

          - **unit** *(string) --*

            A unit of time.

          - **value** *(integer) --*

            A number of time units.

        - **tcpRetryEvents** *(list) --*

          Specify a valid value.

          - *(string) --*

    - **priority** *(integer) --*

      The priority for the route. Routes are matched based on the specified value, where 0 is the
      highest priority.

    - **tcpRoute** *(dict) --*

      An object that represents the specification of a TCP route.

      - **action** *(dict) --* **[REQUIRED]**

        The action to take if a match is determined.

        - **weightedTargets** *(list) --* **[REQUIRED]**

          An object that represents the targets that traffic is routed to when a request matches the
          route.

          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed across
            targets according to their relative weight. For example, a weighted target with a
            relative weight of 50 receives five times as much traffic as one with a relative weight
            of 10. The total weight for all targets combined must be less than or equal to 100.

            - **virtualNode** *(string) --* **[REQUIRED]**

              The virtual node to associate with the weighted target.

            - **weight** *(integer) --* **[REQUIRED]**

              The relative weight of the weighted target.
    """


_ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNode` `metadata`

    The associated metadata for the virtual node.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNodespecbackends` `virtualService`

    Specifies a virtual service to use as a backend for a virtual node.

    - **virtualServiceName** *(string) --*

      The name of the virtual service that is acting as a virtual node backend.
    """


_ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    {
        "virtualService": ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNodespec` `backends`

    An object that represents the backends that a virtual node is expected to send outbound
    traffic to.

    - **virtualService** *(dict) --*

      Specifies a virtual service to use as a backend for a virtual node.

      - **virtualServiceName** *(string) --*

        The name of the virtual service that is acting as a virtual node backend.
    """


_ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": str,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNodespeclisteners` `healthCheck`

    The health check information for the listener.

    - **healthyThreshold** *(integer) --*

      The number of consecutive successful health checks that must occur before declaring
      listener healthy.

    - **intervalMillis** *(integer) --*

      The time period in milliseconds between each health check execution.

    - **path** *(string) --*

      The destination path for the health check request. This is required only if the
      specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

    - **port** *(integer) --*

      The destination port for the health check request. This port must match the port
      defined in the  PortMapping for the listener.

    - **protocol** *(string) --*

      The protocol for the health check request.

    - **timeoutMillis** *(integer) --*

      The amount of time to wait when receiving a response from the health check, in
      milliseconds.

    - **unhealthyThreshold** *(integer) --*

      The number of consecutive failed health checks that must occur before declaring a
      virtual node unhealthy.
    """


_ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": str},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNodespeclisteners` `portMapping`

    The port mapping information for the listener.

    - **port** *(integer) --*

      The port used for the port mapping.

    - **protocol** *(string) --*

      The protocol used for the port mapping. Specify one protocol.
    """


_ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    {
        "healthCheck": ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef,
        "portMapping": ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNodespec` `listeners`

    An object that represents a listener for a virtual node.

    - **healthCheck** *(dict) --*

      The health check information for the listener.

      - **healthyThreshold** *(integer) --*

        The number of consecutive successful health checks that must occur before declaring
        listener healthy.

      - **intervalMillis** *(integer) --*

        The time period in milliseconds between each health check execution.

      - **path** *(string) --*

        The destination path for the health check request. This is required only if the
        specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

      - **port** *(integer) --*

        The destination port for the health check request. This port must match the port
        defined in the  PortMapping for the listener.

      - **protocol** *(string) --*

        The protocol for the health check request.

      - **timeoutMillis** *(integer) --*

        The amount of time to wait when receiving a response from the health check, in
        milliseconds.

      - **unhealthyThreshold** *(integer) --*

        The number of consecutive failed health checks that must occur before declaring a
        virtual node unhealthy.

    - **portMapping** *(dict) --*

      The port mapping information for the listener.

      - **port** *(integer) --*

        The port used for the port mapping.

      - **protocol** *(string) --*

        The protocol used for the port mapping. Specify one protocol.
    """


_ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    {"path": str},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLog` `file`

    The file object to send virtual node access logs to.

    - **path** *(string) --*

      The file path to write access logs to. You can use ``/dev/stdout`` to send access
      logs to standard out and configure your Envoy container to use a log driver, such
      as ``awslogs`` , to export the access logs to a log storage service such as Amazon
      CloudWatch Logs. You can also specify a path in the Envoy container's file system
      to write the files to disk.

      .. note::

        The Envoy process must have write permissions to the path that you specify here.
        Otherwise, Envoy fails to bootstrap properly.
    """


_ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    {"file": ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNodespeclogging` `accessLog`

    The access log configuration for a virtual node.

    - **file** *(dict) --*

      The file object to send virtual node access logs to.

      - **path** *(string) --*

        The file path to write access logs to. You can use ``/dev/stdout`` to send access
        logs to standard out and configure your Envoy container to use a log driver, such
        as ``awslogs`` , to export the access logs to a log storage service such as Amazon
        CloudWatch Logs. You can also specify a path in the Envoy container's file system
        to write the files to disk.

        .. note::

          The Envoy process must have write permissions to the path that you specify here.
          Otherwise, Envoy fails to bootstrap properly.
    """


_ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef",
    {
        "accessLog": ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNodespec` `logging`

    The inbound and outbound access logging information for the virtual node.

    - **accessLog** *(dict) --*

      The access log configuration for a virtual node.

      - **file** *(dict) --*

        The file object to send virtual node access logs to.

        - **path** *(string) --*

          The file path to write access logs to. You can use ``/dev/stdout`` to send access
          logs to standard out and configure your Envoy container to use a log driver, such
          as ``awslogs`` , to export the access logs to a log storage service such as Amazon
          CloudWatch Logs. You can also specify a path in the Envoy container's file system
          to write the files to disk.

          .. note::

            The Envoy process must have write permissions to the path that you specify here.
            Otherwise, Envoy fails to bootstrap properly.
    """


_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMap` `attributes`

    An object that represents the AWS Cloud Map attribute information for your virtual
    node.

    - **key** *(string) --*

      The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
      service instance that contains the specified key and value is returned.

    - **value** *(string) --*

      The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
      service instance that contains the specified key and value is returned.
    """


_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscovery` `awsCloudMap`

    Specifies any AWS Cloud Map information for the virtual node.

    - **attributes** *(list) --*

      A string map that contains attributes with values that you can use to filter
      instances by any custom attribute that you specified when you registered the
      instance. Only instances that match all of the specified key/value pairs will be
      returned.

      - *(dict) --*

        An object that represents the AWS Cloud Map attribute information for your virtual
        node.

        - **key** *(string) --*

          The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
          service instance that contains the specified key and value is returned.

        - **value** *(string) --*

          The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
          service instance that contains the specified key and value is returned.

    - **namespaceName** *(string) --*

      The name of the AWS Cloud Map namespace to use.

    - **serviceName** *(string) --*

      The name of the AWS Cloud Map service to use.
    """


_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    {"hostname": str},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscovery` `dns`

    Specifies the DNS information for the virtual node.

    - **hostname** *(string) --*

      Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNodespec` `serviceDiscovery`

    The service discovery information for the virtual node. If your virtual node does not
    expect ingress traffic, you can omit this parameter.

    - **awsCloudMap** *(dict) --*

      Specifies any AWS Cloud Map information for the virtual node.

      - **attributes** *(list) --*

        A string map that contains attributes with values that you can use to filter
        instances by any custom attribute that you specified when you registered the
        instance. Only instances that match all of the specified key/value pairs will be
        returned.

        - *(dict) --*

          An object that represents the AWS Cloud Map attribute information for your virtual
          node.

          - **key** *(string) --*

            The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
            service instance that contains the specified key and value is returned.

          - **value** *(string) --*

            The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
            service instance that contains the specified key and value is returned.

      - **namespaceName** *(string) --*

        The name of the AWS Cloud Map namespace to use.

      - **serviceName** *(string) --*

        The name of the AWS Cloud Map service to use.

    - **dns** *(dict) --*

      Specifies the DNS information for the virtual node.

      - **hostname** *(string) --*

        Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef",
    {
        "backends": List[ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef],
        "listeners": List[
            ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef
        ],
        "logging": ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNode` `spec`

    The specifications of the virtual node.

    - **backends** *(list) --*

      The backends that the virtual node is expected to send outbound traffic to.

      - *(dict) --*

        An object that represents the backends that a virtual node is expected to send outbound
        traffic to.

        - **virtualService** *(dict) --*

          Specifies a virtual service to use as a backend for a virtual node.

          - **virtualServiceName** *(string) --*

            The name of the virtual service that is acting as a virtual node backend.

    - **listeners** *(list) --*

      The listeners that the virtual node is expected to receive inbound traffic from. You can
      specify one listener.

      - *(dict) --*

        An object that represents a listener for a virtual node.

        - **healthCheck** *(dict) --*

          The health check information for the listener.

          - **healthyThreshold** *(integer) --*

            The number of consecutive successful health checks that must occur before declaring
            listener healthy.

          - **intervalMillis** *(integer) --*

            The time period in milliseconds between each health check execution.

          - **path** *(string) --*

            The destination path for the health check request. This is required only if the
            specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

          - **port** *(integer) --*

            The destination port for the health check request. This port must match the port
            defined in the  PortMapping for the listener.

          - **protocol** *(string) --*

            The protocol for the health check request.

          - **timeoutMillis** *(integer) --*

            The amount of time to wait when receiving a response from the health check, in
            milliseconds.

          - **unhealthyThreshold** *(integer) --*

            The number of consecutive failed health checks that must occur before declaring a
            virtual node unhealthy.

        - **portMapping** *(dict) --*

          The port mapping information for the listener.

          - **port** *(integer) --*

            The port used for the port mapping.

          - **protocol** *(string) --*

            The protocol used for the port mapping. Specify one protocol.

    - **logging** *(dict) --*

      The inbound and outbound access logging information for the virtual node.

      - **accessLog** *(dict) --*

        The access log configuration for a virtual node.

        - **file** *(dict) --*

          The file object to send virtual node access logs to.

          - **path** *(string) --*

            The file path to write access logs to. You can use ``/dev/stdout`` to send access
            logs to standard out and configure your Envoy container to use a log driver, such
            as ``awslogs`` , to export the access logs to a log storage service such as Amazon
            CloudWatch Logs. You can also specify a path in the Envoy container's file system
            to write the files to disk.

            .. note::

              The Envoy process must have write permissions to the path that you specify here.
              Otherwise, Envoy fails to bootstrap properly.

    - **serviceDiscovery** *(dict) --*

      The service discovery information for the virtual node. If your virtual node does not
      expect ingress traffic, you can omit this parameter.

      - **awsCloudMap** *(dict) --*

        Specifies any AWS Cloud Map information for the virtual node.

        - **attributes** *(list) --*

          A string map that contains attributes with values that you can use to filter
          instances by any custom attribute that you specified when you registered the
          instance. Only instances that match all of the specified key/value pairs will be
          returned.

          - *(dict) --*

            An object that represents the AWS Cloud Map attribute information for your virtual
            node.

            - **key** *(string) --*

              The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
              service instance that contains the specified key and value is returned.

            - **value** *(string) --*

              The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
              service instance that contains the specified key and value is returned.

        - **namespaceName** *(string) --*

          The name of the AWS Cloud Map namespace to use.

        - **serviceName** *(string) --*

          The name of the AWS Cloud Map service to use.

      - **dns** *(dict) --*

        Specifies the DNS information for the virtual node.

        - **hostname** *(string) --*

          Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef",
    {"status": str},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponsevirtualNode` `status`

    The current status for the virtual node.

    - **status** *(string) --*

      The current status of the virtual node.
    """


_ClientUpdateVirtualNodeResponsevirtualNodeTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodeTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef,
        "spec": ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef,
        "status": ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef,
        "virtualNodeName": str,
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodeTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodeTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodeResponse` `virtualNode`

    A full description of the virtual node that was updated.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual node resides in.

    - **metadata** *(dict) --*

      The associated metadata for the virtual node.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The specifications of the virtual node.

      - **backends** *(list) --*

        The backends that the virtual node is expected to send outbound traffic to.

        - *(dict) --*

          An object that represents the backends that a virtual node is expected to send outbound
          traffic to.

          - **virtualService** *(dict) --*

            Specifies a virtual service to use as a backend for a virtual node.

            - **virtualServiceName** *(string) --*

              The name of the virtual service that is acting as a virtual node backend.

      - **listeners** *(list) --*

        The listeners that the virtual node is expected to receive inbound traffic from. You can
        specify one listener.

        - *(dict) --*

          An object that represents a listener for a virtual node.

          - **healthCheck** *(dict) --*

            The health check information for the listener.

            - **healthyThreshold** *(integer) --*

              The number of consecutive successful health checks that must occur before declaring
              listener healthy.

            - **intervalMillis** *(integer) --*

              The time period in milliseconds between each health check execution.

            - **path** *(string) --*

              The destination path for the health check request. This is required only if the
              specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

            - **port** *(integer) --*

              The destination port for the health check request. This port must match the port
              defined in the  PortMapping for the listener.

            - **protocol** *(string) --*

              The protocol for the health check request.

            - **timeoutMillis** *(integer) --*

              The amount of time to wait when receiving a response from the health check, in
              milliseconds.

            - **unhealthyThreshold** *(integer) --*

              The number of consecutive failed health checks that must occur before declaring a
              virtual node unhealthy.

          - **portMapping** *(dict) --*

            The port mapping information for the listener.

            - **port** *(integer) --*

              The port used for the port mapping.

            - **protocol** *(string) --*

              The protocol used for the port mapping. Specify one protocol.

      - **logging** *(dict) --*

        The inbound and outbound access logging information for the virtual node.

        - **accessLog** *(dict) --*

          The access log configuration for a virtual node.

          - **file** *(dict) --*

            The file object to send virtual node access logs to.

            - **path** *(string) --*

              The file path to write access logs to. You can use ``/dev/stdout`` to send access
              logs to standard out and configure your Envoy container to use a log driver, such
              as ``awslogs`` , to export the access logs to a log storage service such as Amazon
              CloudWatch Logs. You can also specify a path in the Envoy container's file system
              to write the files to disk.

              .. note::

                The Envoy process must have write permissions to the path that you specify here.
                Otherwise, Envoy fails to bootstrap properly.

      - **serviceDiscovery** *(dict) --*

        The service discovery information for the virtual node. If your virtual node does not
        expect ingress traffic, you can omit this parameter.

        - **awsCloudMap** *(dict) --*

          Specifies any AWS Cloud Map information for the virtual node.

          - **attributes** *(list) --*

            A string map that contains attributes with values that you can use to filter
            instances by any custom attribute that you specified when you registered the
            instance. Only instances that match all of the specified key/value pairs will be
            returned.

            - *(dict) --*

              An object that represents the AWS Cloud Map attribute information for your virtual
              node.

              - **key** *(string) --*

                The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                service instance that contains the specified key and value is returned.

              - **value** *(string) --*

                The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                service instance that contains the specified key and value is returned.

          - **namespaceName** *(string) --*

            The name of the AWS Cloud Map namespace to use.

          - **serviceName** *(string) --*

            The name of the AWS Cloud Map service to use.

        - **dns** *(dict) --*

          Specifies the DNS information for the virtual node.

          - **hostname** *(string) --*

            Specifies the DNS service discovery hostname for the virtual node.

    - **status** *(dict) --*

      The current status for the virtual node.

      - **status** *(string) --*

        The current status of the virtual node.

    - **virtualNodeName** *(string) --*

      The name of the virtual node.
    """


_ClientUpdateVirtualNodeResponseTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponseTypeDef",
    {"virtualNode": ClientUpdateVirtualNodeResponsevirtualNodeTypeDef},
    total=False,
)


class ClientUpdateVirtualNodeResponseTypeDef(_ClientUpdateVirtualNodeResponseTypeDef):
    """
    Type definition for `ClientUpdateVirtualNode` `Response`

    - **virtualNode** *(dict) --*

      A full description of the virtual node that was updated.

      - **meshName** *(string) --*

        The name of the service mesh that the virtual node resides in.

      - **metadata** *(dict) --*

        The associated metadata for the virtual node.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The specifications of the virtual node.

        - **backends** *(list) --*

          The backends that the virtual node is expected to send outbound traffic to.

          - *(dict) --*

            An object that represents the backends that a virtual node is expected to send outbound
            traffic to.

            - **virtualService** *(dict) --*

              Specifies a virtual service to use as a backend for a virtual node.

              - **virtualServiceName** *(string) --*

                The name of the virtual service that is acting as a virtual node backend.

        - **listeners** *(list) --*

          The listeners that the virtual node is expected to receive inbound traffic from. You can
          specify one listener.

          - *(dict) --*

            An object that represents a listener for a virtual node.

            - **healthCheck** *(dict) --*

              The health check information for the listener.

              - **healthyThreshold** *(integer) --*

                The number of consecutive successful health checks that must occur before declaring
                listener healthy.

              - **intervalMillis** *(integer) --*

                The time period in milliseconds between each health check execution.

              - **path** *(string) --*

                The destination path for the health check request. This is required only if the
                specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

              - **port** *(integer) --*

                The destination port for the health check request. This port must match the port
                defined in the  PortMapping for the listener.

              - **protocol** *(string) --*

                The protocol for the health check request.

              - **timeoutMillis** *(integer) --*

                The amount of time to wait when receiving a response from the health check, in
                milliseconds.

              - **unhealthyThreshold** *(integer) --*

                The number of consecutive failed health checks that must occur before declaring a
                virtual node unhealthy.

            - **portMapping** *(dict) --*

              The port mapping information for the listener.

              - **port** *(integer) --*

                The port used for the port mapping.

              - **protocol** *(string) --*

                The protocol used for the port mapping. Specify one protocol.

        - **logging** *(dict) --*

          The inbound and outbound access logging information for the virtual node.

          - **accessLog** *(dict) --*

            The access log configuration for a virtual node.

            - **file** *(dict) --*

              The file object to send virtual node access logs to.

              - **path** *(string) --*

                The file path to write access logs to. You can use ``/dev/stdout`` to send access
                logs to standard out and configure your Envoy container to use a log driver, such
                as ``awslogs`` , to export the access logs to a log storage service such as Amazon
                CloudWatch Logs. You can also specify a path in the Envoy container's file system
                to write the files to disk.

                .. note::

                  The Envoy process must have write permissions to the path that you specify here.
                  Otherwise, Envoy fails to bootstrap properly.

        - **serviceDiscovery** *(dict) --*

          The service discovery information for the virtual node. If your virtual node does not
          expect ingress traffic, you can omit this parameter.

          - **awsCloudMap** *(dict) --*

            Specifies any AWS Cloud Map information for the virtual node.

            - **attributes** *(list) --*

              A string map that contains attributes with values that you can use to filter
              instances by any custom attribute that you specified when you registered the
              instance. Only instances that match all of the specified key/value pairs will be
              returned.

              - *(dict) --*

                An object that represents the AWS Cloud Map attribute information for your virtual
                node.

                - **key** *(string) --*

                  The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                  service instance that contains the specified key and value is returned.

                - **value** *(string) --*

                  The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                  service instance that contains the specified key and value is returned.

            - **namespaceName** *(string) --*

              The name of the AWS Cloud Map namespace to use.

            - **serviceName** *(string) --*

              The name of the AWS Cloud Map service to use.

          - **dns** *(dict) --*

            Specifies the DNS information for the virtual node.

            - **hostname** *(string) --*

              Specifies the DNS service discovery hostname for the virtual node.

      - **status** *(dict) --*

        The current status for the virtual node.

        - **status** *(string) --*

          The current status of the virtual node.

      - **virtualNodeName** *(string) --*

        The name of the virtual node.
    """


_ClientUpdateVirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "_ClientUpdateVirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
)


class ClientUpdateVirtualNodespecbackendsvirtualServiceTypeDef(
    _ClientUpdateVirtualNodespecbackendsvirtualServiceTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodespecbackends` `virtualService`

    Specifies a virtual service to use as a backend for a virtual node.

    - **virtualServiceName** *(string) --* **[REQUIRED]**

      The name of the virtual service that is acting as a virtual node backend.
    """


_ClientUpdateVirtualNodespecbackendsTypeDef = TypedDict(
    "_ClientUpdateVirtualNodespecbackendsTypeDef",
    {"virtualService": ClientUpdateVirtualNodespecbackendsvirtualServiceTypeDef},
    total=False,
)


class ClientUpdateVirtualNodespecbackendsTypeDef(
    _ClientUpdateVirtualNodespecbackendsTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodespec` `backends`

    An object that represents the backends that a virtual node is expected to send outbound
    traffic to.

    - **virtualService** *(dict) --*

      Specifies a virtual service to use as a backend for a virtual node.

      - **virtualServiceName** *(string) --* **[REQUIRED]**

        The name of the virtual service that is acting as a virtual node backend.
    """


_RequiredClientUpdateVirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "_RequiredClientUpdateVirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": str,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
)
_OptionalClientUpdateVirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "_OptionalClientUpdateVirtualNodespeclistenershealthCheckTypeDef",
    {"path": str, "port": int},
    total=False,
)


class ClientUpdateVirtualNodespeclistenershealthCheckTypeDef(
    _RequiredClientUpdateVirtualNodespeclistenershealthCheckTypeDef,
    _OptionalClientUpdateVirtualNodespeclistenershealthCheckTypeDef,
):
    """
    Type definition for `ClientUpdateVirtualNodespeclisteners` `healthCheck`

    The health check information for the listener.

    - **healthyThreshold** *(integer) --* **[REQUIRED]**

      The number of consecutive successful health checks that must occur before declaring
      listener healthy.

    - **intervalMillis** *(integer) --* **[REQUIRED]**

      The time period in milliseconds between each health check execution.

    - **path** *(string) --*

      The destination path for the health check request. This is required only if the specified
      protocol is HTTP. If the protocol is TCP, this parameter is ignored.

    - **port** *(integer) --*

      The destination port for the health check request. This port must match the port defined
      in the  PortMapping for the listener.

    - **protocol** *(string) --* **[REQUIRED]**

      The protocol for the health check request.

    - **timeoutMillis** *(integer) --* **[REQUIRED]**

      The amount of time to wait when receiving a response from the health check, in
      milliseconds.

    - **unhealthyThreshold** *(integer) --* **[REQUIRED]**

      The number of consecutive failed health checks that must occur before declaring a virtual
      node unhealthy.
    """


_ClientUpdateVirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "_ClientUpdateVirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": str},
)


class ClientUpdateVirtualNodespeclistenersportMappingTypeDef(
    _ClientUpdateVirtualNodespeclistenersportMappingTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodespeclisteners` `portMapping`

    The port mapping information for the listener.

    - **port** *(integer) --* **[REQUIRED]**

      The port used for the port mapping.

    - **protocol** *(string) --* **[REQUIRED]**

      The protocol used for the port mapping. Specify one protocol.
    """


_RequiredClientUpdateVirtualNodespeclistenersTypeDef = TypedDict(
    "_RequiredClientUpdateVirtualNodespeclistenersTypeDef",
    {"portMapping": ClientUpdateVirtualNodespeclistenersportMappingTypeDef},
)
_OptionalClientUpdateVirtualNodespeclistenersTypeDef = TypedDict(
    "_OptionalClientUpdateVirtualNodespeclistenersTypeDef",
    {"healthCheck": ClientUpdateVirtualNodespeclistenershealthCheckTypeDef},
    total=False,
)


class ClientUpdateVirtualNodespeclistenersTypeDef(
    _RequiredClientUpdateVirtualNodespeclistenersTypeDef,
    _OptionalClientUpdateVirtualNodespeclistenersTypeDef,
):
    """
    Type definition for `ClientUpdateVirtualNodespec` `listeners`

    An object that represents a listener for a virtual node.

    - **healthCheck** *(dict) --*

      The health check information for the listener.

      - **healthyThreshold** *(integer) --* **[REQUIRED]**

        The number of consecutive successful health checks that must occur before declaring
        listener healthy.

      - **intervalMillis** *(integer) --* **[REQUIRED]**

        The time period in milliseconds between each health check execution.

      - **path** *(string) --*

        The destination path for the health check request. This is required only if the specified
        protocol is HTTP. If the protocol is TCP, this parameter is ignored.

      - **port** *(integer) --*

        The destination port for the health check request. This port must match the port defined
        in the  PortMapping for the listener.

      - **protocol** *(string) --* **[REQUIRED]**

        The protocol for the health check request.

      - **timeoutMillis** *(integer) --* **[REQUIRED]**

        The amount of time to wait when receiving a response from the health check, in
        milliseconds.

      - **unhealthyThreshold** *(integer) --* **[REQUIRED]**

        The number of consecutive failed health checks that must occur before declaring a virtual
        node unhealthy.

    - **portMapping** *(dict) --* **[REQUIRED]**

      The port mapping information for the listener.

      - **port** *(integer) --* **[REQUIRED]**

        The port used for the port mapping.

      - **protocol** *(string) --* **[REQUIRED]**

        The protocol used for the port mapping. Specify one protocol.
    """


_ClientUpdateVirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "_ClientUpdateVirtualNodespecloggingaccessLogfileTypeDef", {"path": str}
)


class ClientUpdateVirtualNodespecloggingaccessLogfileTypeDef(
    _ClientUpdateVirtualNodespecloggingaccessLogfileTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodespecloggingaccessLog` `file`

    The file object to send virtual node access logs to.

    - **path** *(string) --* **[REQUIRED]**

      The file path to write access logs to. You can use ``/dev/stdout`` to send access logs to
      standard out and configure your Envoy container to use a log driver, such as ``awslogs``
      , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You
      can also specify a path in the Envoy container's file system to write the files to disk.

      .. note::

        The Envoy process must have write permissions to the path that you specify here.
        Otherwise, Envoy fails to bootstrap properly.
    """


_ClientUpdateVirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "_ClientUpdateVirtualNodespecloggingaccessLogTypeDef",
    {"file": ClientUpdateVirtualNodespecloggingaccessLogfileTypeDef},
    total=False,
)


class ClientUpdateVirtualNodespecloggingaccessLogTypeDef(
    _ClientUpdateVirtualNodespecloggingaccessLogTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodespeclogging` `accessLog`

    The access log configuration for a virtual node.

    - **file** *(dict) --*

      The file object to send virtual node access logs to.

      - **path** *(string) --* **[REQUIRED]**

        The file path to write access logs to. You can use ``/dev/stdout`` to send access logs to
        standard out and configure your Envoy container to use a log driver, such as ``awslogs``
        , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You
        can also specify a path in the Envoy container's file system to write the files to disk.

        .. note::

          The Envoy process must have write permissions to the path that you specify here.
          Otherwise, Envoy fails to bootstrap properly.
    """


_ClientUpdateVirtualNodespecloggingTypeDef = TypedDict(
    "_ClientUpdateVirtualNodespecloggingTypeDef",
    {"accessLog": ClientUpdateVirtualNodespecloggingaccessLogTypeDef},
    total=False,
)


class ClientUpdateVirtualNodespecloggingTypeDef(
    _ClientUpdateVirtualNodespecloggingTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodespec` `logging`

    The inbound and outbound access logging information for the virtual node.

    - **accessLog** *(dict) --*

      The access log configuration for a virtual node.

      - **file** *(dict) --*

        The file object to send virtual node access logs to.

        - **path** *(string) --* **[REQUIRED]**

          The file path to write access logs to. You can use ``/dev/stdout`` to send access logs to
          standard out and configure your Envoy container to use a log driver, such as ``awslogs``
          , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You
          can also specify a path in the Envoy container's file system to write the files to disk.

          .. note::

            The Envoy process must have write permissions to the path that you specify here.
            Otherwise, Envoy fails to bootstrap properly.
    """


_ClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "_ClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
)


class ClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef(
    _ClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodespecserviceDiscoveryawsCloudMap` `attributes`

    An object that represents the AWS Cloud Map attribute information for your virtual node.

    - **key** *(string) --* **[REQUIRED]**

      The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
      instance that contains the specified key and value is returned.

    - **value** *(string) --* **[REQUIRED]**

      The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
      instance that contains the specified key and value is returned.
    """


_RequiredClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_RequiredClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {"namespaceName": str, "serviceName": str},
)
_OptionalClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_OptionalClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ]
    },
    total=False,
)


class ClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef(
    _RequiredClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
    _OptionalClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
):
    """
    Type definition for `ClientUpdateVirtualNodespecserviceDiscovery` `awsCloudMap`

    Specifies any AWS Cloud Map information for the virtual node.

    - **attributes** *(list) --*

      A string map that contains attributes with values that you can use to filter instances by
      any custom attribute that you specified when you registered the instance. Only instances
      that match all of the specified key/value pairs will be returned.

      - *(dict) --*

        An object that represents the AWS Cloud Map attribute information for your virtual node.

        - **key** *(string) --* **[REQUIRED]**

          The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
          instance that contains the specified key and value is returned.

        - **value** *(string) --* **[REQUIRED]**

          The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
          instance that contains the specified key and value is returned.

    - **namespaceName** *(string) --* **[REQUIRED]**

      The name of the AWS Cloud Map namespace to use.

    - **serviceName** *(string) --* **[REQUIRED]**

      The name of the AWS Cloud Map service to use.
    """


_ClientUpdateVirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "_ClientUpdateVirtualNodespecserviceDiscoverydnsTypeDef", {"hostname": str}
)


class ClientUpdateVirtualNodespecserviceDiscoverydnsTypeDef(
    _ClientUpdateVirtualNodespecserviceDiscoverydnsTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodespecserviceDiscovery` `dns`

    Specifies the DNS information for the virtual node.

    - **hostname** *(string) --* **[REQUIRED]**

      Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientUpdateVirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "_ClientUpdateVirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientUpdateVirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientUpdateVirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualNodespecserviceDiscoveryTypeDef(
    _ClientUpdateVirtualNodespecserviceDiscoveryTypeDef
):
    """
    Type definition for `ClientUpdateVirtualNodespec` `serviceDiscovery`

    The service discovery information for the virtual node. If your virtual node does not expect
    ingress traffic, you can omit this parameter.

    - **awsCloudMap** *(dict) --*

      Specifies any AWS Cloud Map information for the virtual node.

      - **attributes** *(list) --*

        A string map that contains attributes with values that you can use to filter instances by
        any custom attribute that you specified when you registered the instance. Only instances
        that match all of the specified key/value pairs will be returned.

        - *(dict) --*

          An object that represents the AWS Cloud Map attribute information for your virtual node.

          - **key** *(string) --* **[REQUIRED]**

            The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
            instance that contains the specified key and value is returned.

          - **value** *(string) --* **[REQUIRED]**

            The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
            instance that contains the specified key and value is returned.

      - **namespaceName** *(string) --* **[REQUIRED]**

        The name of the AWS Cloud Map namespace to use.

      - **serviceName** *(string) --* **[REQUIRED]**

        The name of the AWS Cloud Map service to use.

    - **dns** *(dict) --*

      Specifies the DNS information for the virtual node.

      - **hostname** *(string) --* **[REQUIRED]**

        Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientUpdateVirtualNodespecTypeDef = TypedDict(
    "_ClientUpdateVirtualNodespecTypeDef",
    {
        "backends": List[ClientUpdateVirtualNodespecbackendsTypeDef],
        "listeners": List[ClientUpdateVirtualNodespeclistenersTypeDef],
        "logging": ClientUpdateVirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientUpdateVirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualNodespecTypeDef(_ClientUpdateVirtualNodespecTypeDef):
    """
    Type definition for `ClientUpdateVirtualNode` `spec`

    The new virtual node specification to apply. This overwrites the existing data.

    - **backends** *(list) --*

      The backends that the virtual node is expected to send outbound traffic to.

      - *(dict) --*

        An object that represents the backends that a virtual node is expected to send outbound
        traffic to.

        - **virtualService** *(dict) --*

          Specifies a virtual service to use as a backend for a virtual node.

          - **virtualServiceName** *(string) --* **[REQUIRED]**

            The name of the virtual service that is acting as a virtual node backend.

    - **listeners** *(list) --*

      The listeners that the virtual node is expected to receive inbound traffic from. You can
      specify one listener.

      - *(dict) --*

        An object that represents a listener for a virtual node.

        - **healthCheck** *(dict) --*

          The health check information for the listener.

          - **healthyThreshold** *(integer) --* **[REQUIRED]**

            The number of consecutive successful health checks that must occur before declaring
            listener healthy.

          - **intervalMillis** *(integer) --* **[REQUIRED]**

            The time period in milliseconds between each health check execution.

          - **path** *(string) --*

            The destination path for the health check request. This is required only if the specified
            protocol is HTTP. If the protocol is TCP, this parameter is ignored.

          - **port** *(integer) --*

            The destination port for the health check request. This port must match the port defined
            in the  PortMapping for the listener.

          - **protocol** *(string) --* **[REQUIRED]**

            The protocol for the health check request.

          - **timeoutMillis** *(integer) --* **[REQUIRED]**

            The amount of time to wait when receiving a response from the health check, in
            milliseconds.

          - **unhealthyThreshold** *(integer) --* **[REQUIRED]**

            The number of consecutive failed health checks that must occur before declaring a virtual
            node unhealthy.

        - **portMapping** *(dict) --* **[REQUIRED]**

          The port mapping information for the listener.

          - **port** *(integer) --* **[REQUIRED]**

            The port used for the port mapping.

          - **protocol** *(string) --* **[REQUIRED]**

            The protocol used for the port mapping. Specify one protocol.

    - **logging** *(dict) --*

      The inbound and outbound access logging information for the virtual node.

      - **accessLog** *(dict) --*

        The access log configuration for a virtual node.

        - **file** *(dict) --*

          The file object to send virtual node access logs to.

          - **path** *(string) --* **[REQUIRED]**

            The file path to write access logs to. You can use ``/dev/stdout`` to send access logs to
            standard out and configure your Envoy container to use a log driver, such as ``awslogs``
            , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You
            can also specify a path in the Envoy container's file system to write the files to disk.

            .. note::

              The Envoy process must have write permissions to the path that you specify here.
              Otherwise, Envoy fails to bootstrap properly.

    - **serviceDiscovery** *(dict) --*

      The service discovery information for the virtual node. If your virtual node does not expect
      ingress traffic, you can omit this parameter.

      - **awsCloudMap** *(dict) --*

        Specifies any AWS Cloud Map information for the virtual node.

        - **attributes** *(list) --*

          A string map that contains attributes with values that you can use to filter instances by
          any custom attribute that you specified when you registered the instance. Only instances
          that match all of the specified key/value pairs will be returned.

          - *(dict) --*

            An object that represents the AWS Cloud Map attribute information for your virtual node.

            - **key** *(string) --* **[REQUIRED]**

              The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
              instance that contains the specified key and value is returned.

            - **value** *(string) --* **[REQUIRED]**

              The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
              instance that contains the specified key and value is returned.

        - **namespaceName** *(string) --* **[REQUIRED]**

          The name of the AWS Cloud Map namespace to use.

        - **serviceName** *(string) --* **[REQUIRED]**

          The name of the AWS Cloud Map service to use.

      - **dns** *(dict) --*

        Specifies the DNS information for the virtual node.

        - **hostname** *(string) --* **[REQUIRED]**

          Specifies the DNS service discovery hostname for the virtual node.
    """


_ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef(
    _ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef
):
    """
    Type definition for `ClientUpdateVirtualRouterResponsevirtualRouter` `metadata`

    The associated metadata for the virtual router.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": str},
    total=False,
)


class ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef(
    _ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
):
    """
    Type definition for `ClientUpdateVirtualRouterResponsevirtualRouterspeclisteners` `portMapping`

    An object that represents a port mapping.

    - **port** *(integer) --*

      The port used for the port mapping.

    - **protocol** *(string) --*

      The protocol used for the port mapping. Specify one protocol.
    """


_ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    {
        "portMapping": ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
    },
    total=False,
)


class ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef(
    _ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef
):
    """
    Type definition for `ClientUpdateVirtualRouterResponsevirtualRouterspec` `listeners`

    An object that represents a virtual router listener.

    - **portMapping** *(dict) --*

      An object that represents a port mapping.

      - **port** *(integer) --*

        The port used for the port mapping.

      - **protocol** *(string) --*

        The protocol used for the port mapping. Specify one protocol.
    """


_ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef",
    {
        "listeners": List[
            ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef
        ]
    },
    total=False,
)


class ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef(
    _ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef
):
    """
    Type definition for `ClientUpdateVirtualRouterResponsevirtualRouter` `spec`

    The specifications of the virtual router.

    - **listeners** *(list) --*

      The listeners that the virtual router is expected to receive inbound traffic from. You
      can specify one listener.

      - *(dict) --*

        An object that represents a virtual router listener.

        - **portMapping** *(dict) --*

          An object that represents a port mapping.

          - **port** *(integer) --*

            The port used for the port mapping.

          - **protocol** *(string) --*

            The protocol used for the port mapping. Specify one protocol.
    """


_ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef",
    {"status": str},
    total=False,
)


class ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef(
    _ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef
):
    """
    Type definition for `ClientUpdateVirtualRouterResponsevirtualRouter` `status`

    The current status of the virtual router.

    - **status** *(string) --*

      The current status of the virtual router.
    """


_ClientUpdateVirtualRouterResponsevirtualRouterTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponsevirtualRouterTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef,
        "spec": ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef,
        "status": ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientUpdateVirtualRouterResponsevirtualRouterTypeDef(
    _ClientUpdateVirtualRouterResponsevirtualRouterTypeDef
):
    """
    Type definition for `ClientUpdateVirtualRouterResponse` `virtualRouter`

    A full description of the virtual router that was updated.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual router resides in.

    - **metadata** *(dict) --*

      The associated metadata for the virtual router.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The specifications of the virtual router.

      - **listeners** *(list) --*

        The listeners that the virtual router is expected to receive inbound traffic from. You
        can specify one listener.

        - *(dict) --*

          An object that represents a virtual router listener.

          - **portMapping** *(dict) --*

            An object that represents a port mapping.

            - **port** *(integer) --*

              The port used for the port mapping.

            - **protocol** *(string) --*

              The protocol used for the port mapping. Specify one protocol.

    - **status** *(dict) --*

      The current status of the virtual router.

      - **status** *(string) --*

        The current status of the virtual router.

    - **virtualRouterName** *(string) --*

      The name of the virtual router.
    """


_ClientUpdateVirtualRouterResponseTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponseTypeDef",
    {"virtualRouter": ClientUpdateVirtualRouterResponsevirtualRouterTypeDef},
    total=False,
)


class ClientUpdateVirtualRouterResponseTypeDef(
    _ClientUpdateVirtualRouterResponseTypeDef
):
    """
    Type definition for `ClientUpdateVirtualRouter` `Response`

    - **virtualRouter** *(dict) --*

      A full description of the virtual router that was updated.

      - **meshName** *(string) --*

        The name of the service mesh that the virtual router resides in.

      - **metadata** *(dict) --*

        The associated metadata for the virtual router.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The specifications of the virtual router.

        - **listeners** *(list) --*

          The listeners that the virtual router is expected to receive inbound traffic from. You
          can specify one listener.

          - *(dict) --*

            An object that represents a virtual router listener.

            - **portMapping** *(dict) --*

              An object that represents a port mapping.

              - **port** *(integer) --*

                The port used for the port mapping.

              - **protocol** *(string) --*

                The protocol used for the port mapping. Specify one protocol.

      - **status** *(dict) --*

        The current status of the virtual router.

        - **status** *(string) --*

          The current status of the virtual router.

      - **virtualRouterName** *(string) --*

        The name of the virtual router.
    """


_ClientUpdateVirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": str},
)


class ClientUpdateVirtualRouterspeclistenersportMappingTypeDef(
    _ClientUpdateVirtualRouterspeclistenersportMappingTypeDef
):
    """
    Type definition for `ClientUpdateVirtualRouterspeclisteners` `portMapping`

    An object that represents a port mapping.

    - **port** *(integer) --* **[REQUIRED]**

      The port used for the port mapping.

    - **protocol** *(string) --* **[REQUIRED]**

      The protocol used for the port mapping. Specify one protocol.
    """


_ClientUpdateVirtualRouterspeclistenersTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterspeclistenersTypeDef",
    {"portMapping": ClientUpdateVirtualRouterspeclistenersportMappingTypeDef},
)


class ClientUpdateVirtualRouterspeclistenersTypeDef(
    _ClientUpdateVirtualRouterspeclistenersTypeDef
):
    """
    Type definition for `ClientUpdateVirtualRouterspec` `listeners`

    An object that represents a virtual router listener.

    - **portMapping** *(dict) --* **[REQUIRED]**

      An object that represents a port mapping.

      - **port** *(integer) --* **[REQUIRED]**

        The port used for the port mapping.

      - **protocol** *(string) --* **[REQUIRED]**

        The protocol used for the port mapping. Specify one protocol.
    """


_ClientUpdateVirtualRouterspecTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterspecTypeDef",
    {"listeners": List[ClientUpdateVirtualRouterspeclistenersTypeDef]},
    total=False,
)


class ClientUpdateVirtualRouterspecTypeDef(_ClientUpdateVirtualRouterspecTypeDef):
    """
    Type definition for `ClientUpdateVirtualRouter` `spec`

    The new virtual router specification to apply. This overwrites the existing data.

    - **listeners** *(list) --*

      The listeners that the virtual router is expected to receive inbound traffic from. You can
      specify one listener.

      - *(dict) --*

        An object that represents a virtual router listener.

        - **portMapping** *(dict) --* **[REQUIRED]**

          An object that represents a port mapping.

          - **port** *(integer) --* **[REQUIRED]**

            The port used for the port mapping.

          - **protocol** *(string) --* **[REQUIRED]**

            The protocol used for the port mapping. Specify one protocol.
    """


_ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "uid": str,
        "version": int,
    },
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef
):
    """
    Type definition for `ClientUpdateVirtualServiceResponsevirtualService` `metadata`

    An object that represents metadata for a resource.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the resource.

    - **createdAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was created.

    - **lastUpdatedAt** *(datetime) --*

      The Unix epoch timestamp in seconds for when the resource was last updated.

    - **uid** *(string) --*

      The unique identifier for the resource.

    - **version** *(integer) --*

      The version of the resource. Resources are created at version 1, and this version is
      incremented each time that they're updated.
    """


_ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef
):
    """
    Type definition for `ClientUpdateVirtualServiceResponsevirtualServicespecprovider` `virtualNode`

    The virtual node associated with a virtual service.

    - **virtualNodeName** *(string) --*

      The name of the virtual node that is acting as a service provider.
    """


_ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef
):
    """
    Type definition for `ClientUpdateVirtualServiceResponsevirtualServicespecprovider` `virtualRouter`

    The virtual router associated with a virtual service.

    - **virtualRouterName** *(string) --*

      The name of the virtual router that is acting as a service provider.
    """


_ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef
):
    """
    Type definition for `ClientUpdateVirtualServiceResponsevirtualServicespec` `provider`

    The App Mesh object that is acting as the provider for a virtual service. You can specify
    a single virtual node or virtual router.

    - **virtualNode** *(dict) --*

      The virtual node associated with a virtual service.

      - **virtualNodeName** *(string) --*

        The name of the virtual node that is acting as a service provider.

    - **virtualRouter** *(dict) --*

      The virtual router associated with a virtual service.

      - **virtualRouterName** *(string) --*

        The name of the virtual router that is acting as a service provider.
    """


_ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef",
    {"provider": ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef},
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef
):
    """
    Type definition for `ClientUpdateVirtualServiceResponsevirtualService` `spec`

    The specifications of the virtual service.

    - **provider** *(dict) --*

      The App Mesh object that is acting as the provider for a virtual service. You can specify
      a single virtual node or virtual router.

      - **virtualNode** *(dict) --*

        The virtual node associated with a virtual service.

        - **virtualNodeName** *(string) --*

          The name of the virtual node that is acting as a service provider.

      - **virtualRouter** *(dict) --*

        The virtual router associated with a virtual service.

        - **virtualRouterName** *(string) --*

          The name of the virtual router that is acting as a service provider.
    """


_ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef",
    {"status": str},
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef
):
    """
    Type definition for `ClientUpdateVirtualServiceResponsevirtualService` `status`

    The current status of the virtual service.

    - **status** *(string) --*

      The current status of the virtual service.
    """


_ClientUpdateVirtualServiceResponsevirtualServiceTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServiceTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef,
        "spec": ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef,
        "status": ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef,
        "virtualServiceName": str,
    },
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServiceTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServiceTypeDef
):
    """
    Type definition for `ClientUpdateVirtualServiceResponse` `virtualService`

    A full description of the virtual service that was updated.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual service resides in.

    - **metadata** *(dict) --*

      An object that represents metadata for a resource.

      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the resource.

      - **createdAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was created.

      - **lastUpdatedAt** *(datetime) --*

        The Unix epoch timestamp in seconds for when the resource was last updated.

      - **uid** *(string) --*

        The unique identifier for the resource.

      - **version** *(integer) --*

        The version of the resource. Resources are created at version 1, and this version is
        incremented each time that they're updated.

    - **spec** *(dict) --*

      The specifications of the virtual service.

      - **provider** *(dict) --*

        The App Mesh object that is acting as the provider for a virtual service. You can specify
        a single virtual node or virtual router.

        - **virtualNode** *(dict) --*

          The virtual node associated with a virtual service.

          - **virtualNodeName** *(string) --*

            The name of the virtual node that is acting as a service provider.

        - **virtualRouter** *(dict) --*

          The virtual router associated with a virtual service.

          - **virtualRouterName** *(string) --*

            The name of the virtual router that is acting as a service provider.

    - **status** *(dict) --*

      The current status of the virtual service.

      - **status** *(string) --*

        The current status of the virtual service.

    - **virtualServiceName** *(string) --*

      The name of the virtual service.
    """


_ClientUpdateVirtualServiceResponseTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponseTypeDef",
    {"virtualService": ClientUpdateVirtualServiceResponsevirtualServiceTypeDef},
    total=False,
)


class ClientUpdateVirtualServiceResponseTypeDef(
    _ClientUpdateVirtualServiceResponseTypeDef
):
    """
    Type definition for `ClientUpdateVirtualService` `Response`

    - **virtualService** *(dict) --*

      A full description of the virtual service that was updated.

      - **meshName** *(string) --*

        The name of the service mesh that the virtual service resides in.

      - **metadata** *(dict) --*

        An object that represents metadata for a resource.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the resource.

        - **createdAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was created.

        - **lastUpdatedAt** *(datetime) --*

          The Unix epoch timestamp in seconds for when the resource was last updated.

        - **uid** *(string) --*

          The unique identifier for the resource.

        - **version** *(integer) --*

          The version of the resource. Resources are created at version 1, and this version is
          incremented each time that they're updated.

      - **spec** *(dict) --*

        The specifications of the virtual service.

        - **provider** *(dict) --*

          The App Mesh object that is acting as the provider for a virtual service. You can specify
          a single virtual node or virtual router.

          - **virtualNode** *(dict) --*

            The virtual node associated with a virtual service.

            - **virtualNodeName** *(string) --*

              The name of the virtual node that is acting as a service provider.

          - **virtualRouter** *(dict) --*

            The virtual router associated with a virtual service.

            - **virtualRouterName** *(string) --*

              The name of the virtual router that is acting as a service provider.

      - **status** *(dict) --*

        The current status of the virtual service.

        - **status** *(string) --*

          The current status of the virtual service.

      - **virtualServiceName** *(string) --*

        The name of the virtual service.
    """


_ClientUpdateVirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "_ClientUpdateVirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
)


class ClientUpdateVirtualServicespecprovidervirtualNodeTypeDef(
    _ClientUpdateVirtualServicespecprovidervirtualNodeTypeDef
):
    """
    Type definition for `ClientUpdateVirtualServicespecprovider` `virtualNode`

    The virtual node associated with a virtual service.

    - **virtualNodeName** *(string) --* **[REQUIRED]**

      The name of the virtual node that is acting as a service provider.
    """


_ClientUpdateVirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "_ClientUpdateVirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
)


class ClientUpdateVirtualServicespecprovidervirtualRouterTypeDef(
    _ClientUpdateVirtualServicespecprovidervirtualRouterTypeDef
):
    """
    Type definition for `ClientUpdateVirtualServicespecprovider` `virtualRouter`

    The virtual router associated with a virtual service.

    - **virtualRouterName** *(string) --* **[REQUIRED]**

      The name of the virtual router that is acting as a service provider.
    """


_ClientUpdateVirtualServicespecproviderTypeDef = TypedDict(
    "_ClientUpdateVirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientUpdateVirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientUpdateVirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualServicespecproviderTypeDef(
    _ClientUpdateVirtualServicespecproviderTypeDef
):
    """
    Type definition for `ClientUpdateVirtualServicespec` `provider`

    The App Mesh object that is acting as the provider for a virtual service. You can specify a
    single virtual node or virtual router.

    - **virtualNode** *(dict) --*

      The virtual node associated with a virtual service.

      - **virtualNodeName** *(string) --* **[REQUIRED]**

        The name of the virtual node that is acting as a service provider.

    - **virtualRouter** *(dict) --*

      The virtual router associated with a virtual service.

      - **virtualRouterName** *(string) --* **[REQUIRED]**

        The name of the virtual router that is acting as a service provider.
    """


_ClientUpdateVirtualServicespecTypeDef = TypedDict(
    "_ClientUpdateVirtualServicespecTypeDef",
    {"provider": ClientUpdateVirtualServicespecproviderTypeDef},
    total=False,
)


class ClientUpdateVirtualServicespecTypeDef(_ClientUpdateVirtualServicespecTypeDef):
    """
    Type definition for `ClientUpdateVirtualService` `spec`

    The new virtual service specification to apply. This overwrites the existing data.

    - **provider** *(dict) --*

      The App Mesh object that is acting as the provider for a virtual service. You can specify a
      single virtual node or virtual router.

      - **virtualNode** *(dict) --*

        The virtual node associated with a virtual service.

        - **virtualNodeName** *(string) --* **[REQUIRED]**

          The name of the virtual node that is acting as a service provider.

      - **virtualRouter** *(dict) --*

        The virtual router associated with a virtual service.

        - **virtualRouterName** *(string) --* **[REQUIRED]**

          The name of the virtual router that is acting as a service provider.
    """


_ListMeshesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMeshesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMeshesPaginatePaginationConfigTypeDef(
    _ListMeshesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListMeshesPaginate` `PaginationConfig`

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


_ListMeshesPaginateResponsemeshesTypeDef = TypedDict(
    "_ListMeshesPaginateResponsemeshesTypeDef",
    {"arn": str, "meshName": str},
    total=False,
)


class ListMeshesPaginateResponsemeshesTypeDef(_ListMeshesPaginateResponsemeshesTypeDef):
    """
    Type definition for `ListMeshesPaginateResponse` `meshes`

    An object that represents a service mesh returned by a list operation.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) of the service mesh.

    - **meshName** *(string) --*

      The name of the service mesh.
    """


_ListMeshesPaginateResponseTypeDef = TypedDict(
    "_ListMeshesPaginateResponseTypeDef",
    {"meshes": List[ListMeshesPaginateResponsemeshesTypeDef], "NextToken": str},
    total=False,
)


class ListMeshesPaginateResponseTypeDef(_ListMeshesPaginateResponseTypeDef):
    """
    Type definition for `ListMeshesPaginate` `Response`

    - **meshes** *(list) --*

      The list of existing service meshes.

      - *(dict) --*

        An object that represents a service mesh returned by a list operation.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) of the service mesh.

        - **meshName** *(string) --*

          The name of the service mesh.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRoutesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRoutesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRoutesPaginatePaginationConfigTypeDef(
    _ListRoutesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRoutesPaginate` `PaginationConfig`

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


_ListRoutesPaginateResponseroutesTypeDef = TypedDict(
    "_ListRoutesPaginateResponseroutesTypeDef",
    {"arn": str, "meshName": str, "routeName": str, "virtualRouterName": str},
    total=False,
)


class ListRoutesPaginateResponseroutesTypeDef(_ListRoutesPaginateResponseroutesTypeDef):
    """
    Type definition for `ListRoutesPaginateResponse` `routes`

    An object that represents a route returned by a list operation.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the route.

    - **meshName** *(string) --*

      The name of the service mesh that the route resides in.

    - **routeName** *(string) --*

      The name of the route.

    - **virtualRouterName** *(string) --*

      The virtual router that the route is associated with.
    """


_ListRoutesPaginateResponseTypeDef = TypedDict(
    "_ListRoutesPaginateResponseTypeDef",
    {"routes": List[ListRoutesPaginateResponseroutesTypeDef], "NextToken": str},
    total=False,
)


class ListRoutesPaginateResponseTypeDef(_ListRoutesPaginateResponseTypeDef):
    """
    Type definition for `ListRoutesPaginate` `Response`

    - **routes** *(list) --*

      The list of existing routes for the specified service mesh and virtual router.

      - *(dict) --*

        An object that represents a route returned by a list operation.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the route.

        - **meshName** *(string) --*

          The name of the service mesh that the route resides in.

        - **routeName** *(string) --*

          The name of the route.

        - **virtualRouterName** *(string) --*

          The virtual router that the route is associated with.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `PaginationConfig`

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


_ListTagsForResourcePaginateResponsetagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ListTagsForResourcePaginateResponsetagsTypeDef(
    _ListTagsForResourcePaginateResponsetagsTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginateResponse` `tags`

    Optional metadata that you apply to a resource to assist with categorization and
    organization. Each tag consists of a key and an optional value, both of which you define.
    Tag keys can have a maximum character length of 128 characters, and tag values can have a
    maximum length of 256 characters.

    - **key** *(string) --*

      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts
      like a category for more specific tag values.

    - **value** *(string) --*

      The optional part of a key-value pair that make up a tag. A ``value`` acts as a
      descriptor within a tag category (key).
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"tags": List[ListTagsForResourcePaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(
    _ListTagsForResourcePaginateResponseTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `Response`

    - **tags** *(list) --*

      The tags for the resource.

      - *(dict) --*

        Optional metadata that you apply to a resource to assist with categorization and
        organization. Each tag consists of a key and an optional value, both of which you define.
        Tag keys can have a maximum character length of 128 characters, and tag values can have a
        maximum length of 256 characters.

        - **key** *(string) --*

          One part of a key-value pair that make up a tag. A ``key`` is a general label that acts
          like a category for more specific tag values.

        - **value** *(string) --*

          The optional part of a key-value pair that make up a tag. A ``value`` acts as a
          descriptor within a tag category (key).

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListVirtualNodesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVirtualNodesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVirtualNodesPaginatePaginationConfigTypeDef(
    _ListVirtualNodesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListVirtualNodesPaginate` `PaginationConfig`

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


_ListVirtualNodesPaginateResponsevirtualNodesTypeDef = TypedDict(
    "_ListVirtualNodesPaginateResponsevirtualNodesTypeDef",
    {"arn": str, "meshName": str, "virtualNodeName": str},
    total=False,
)


class ListVirtualNodesPaginateResponsevirtualNodesTypeDef(
    _ListVirtualNodesPaginateResponsevirtualNodesTypeDef
):
    """
    Type definition for `ListVirtualNodesPaginateResponse` `virtualNodes`

    An object that represents a virtual node returned by a list operation.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the virtual node.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual node resides in.

    - **virtualNodeName** *(string) --*

      The name of the virtual node.
    """


_ListVirtualNodesPaginateResponseTypeDef = TypedDict(
    "_ListVirtualNodesPaginateResponseTypeDef",
    {
        "virtualNodes": List[ListVirtualNodesPaginateResponsevirtualNodesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListVirtualNodesPaginateResponseTypeDef(_ListVirtualNodesPaginateResponseTypeDef):
    """
    Type definition for `ListVirtualNodesPaginate` `Response`

    - **virtualNodes** *(list) --*

      The list of existing virtual nodes for the specified service mesh.

      - *(dict) --*

        An object that represents a virtual node returned by a list operation.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the virtual node.

        - **meshName** *(string) --*

          The name of the service mesh that the virtual node resides in.

        - **virtualNodeName** *(string) --*

          The name of the virtual node.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListVirtualRoutersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVirtualRoutersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVirtualRoutersPaginatePaginationConfigTypeDef(
    _ListVirtualRoutersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListVirtualRoutersPaginate` `PaginationConfig`

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


_ListVirtualRoutersPaginateResponsevirtualRoutersTypeDef = TypedDict(
    "_ListVirtualRoutersPaginateResponsevirtualRoutersTypeDef",
    {"arn": str, "meshName": str, "virtualRouterName": str},
    total=False,
)


class ListVirtualRoutersPaginateResponsevirtualRoutersTypeDef(
    _ListVirtualRoutersPaginateResponsevirtualRoutersTypeDef
):
    """
    Type definition for `ListVirtualRoutersPaginateResponse` `virtualRouters`

    An object that represents a virtual router returned by a list operation.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the virtual router.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual router resides in.

    - **virtualRouterName** *(string) --*

      The name of the virtual router.
    """


_ListVirtualRoutersPaginateResponseTypeDef = TypedDict(
    "_ListVirtualRoutersPaginateResponseTypeDef",
    {
        "virtualRouters": List[ListVirtualRoutersPaginateResponsevirtualRoutersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListVirtualRoutersPaginateResponseTypeDef(
    _ListVirtualRoutersPaginateResponseTypeDef
):
    """
    Type definition for `ListVirtualRoutersPaginate` `Response`

    - **virtualRouters** *(list) --*

      The list of existing virtual routers for the specified service mesh.

      - *(dict) --*

        An object that represents a virtual router returned by a list operation.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the virtual router.

        - **meshName** *(string) --*

          The name of the service mesh that the virtual router resides in.

        - **virtualRouterName** *(string) --*

          The name of the virtual router.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListVirtualServicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVirtualServicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVirtualServicesPaginatePaginationConfigTypeDef(
    _ListVirtualServicesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListVirtualServicesPaginate` `PaginationConfig`

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


_ListVirtualServicesPaginateResponsevirtualServicesTypeDef = TypedDict(
    "_ListVirtualServicesPaginateResponsevirtualServicesTypeDef",
    {"arn": str, "meshName": str, "virtualServiceName": str},
    total=False,
)


class ListVirtualServicesPaginateResponsevirtualServicesTypeDef(
    _ListVirtualServicesPaginateResponsevirtualServicesTypeDef
):
    """
    Type definition for `ListVirtualServicesPaginateResponse` `virtualServices`

    An object that represents a virtual service returned by a list operation.

    - **arn** *(string) --*

      The full Amazon Resource Name (ARN) for the virtual service.

    - **meshName** *(string) --*

      The name of the service mesh that the virtual service resides in.

    - **virtualServiceName** *(string) --*

      The name of the virtual service.
    """


_ListVirtualServicesPaginateResponseTypeDef = TypedDict(
    "_ListVirtualServicesPaginateResponseTypeDef",
    {
        "virtualServices": List[
            ListVirtualServicesPaginateResponsevirtualServicesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListVirtualServicesPaginateResponseTypeDef(
    _ListVirtualServicesPaginateResponseTypeDef
):
    """
    Type definition for `ListVirtualServicesPaginate` `Response`

    - **virtualServices** *(list) --*

      The list of existing virtual services for the specified service mesh.

      - *(dict) --*

        An object that represents a virtual service returned by a list operation.

        - **arn** *(string) --*

          The full Amazon Resource Name (ARN) for the virtual service.

        - **meshName** *(string) --*

          The name of the service mesh that the virtual service resides in.

        - **virtualServiceName** *(string) --*

          The name of the virtual service.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
