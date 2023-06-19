from django.urls import path
from tracker_api.views import DailySubsAPIView, DailySubsView, OfferView, OffersAPIView, AddRequisitionsView, \
    WeeklyJoinersPracticeReport, \
    AuditOffers, AuditDailySubs, AuditRequisitions, OffersAddColumn, RequisitionsAddColumn, DailySubAddColumn, \
    InterviewSelectReport, \
    OverAllRequirementReport, OfferStatusSummary, MonthWiseOffersStatus, DropdownListAPIView, AgeingWiseRequisition, \
    PriorityWiseRequisitionReport, Download ,InterviewReport ,DeclineSelectReport ,TotalSummaryReport

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(openapi.Info(
    title="TA Tracker",
    default_version='v1',
),
    public=True,
    permission_classes=(permissions.AllowAny,), )

offer_List_View = OffersAPIView.as_view({'get': 'list', 'post': 'create'})
offer_specific_View = OfferView.as_view({'get': 'retrieve', 'put': 'update'})

dailySubs_List_View = DailySubsAPIView.as_view({'get': 'list', 'post': 'create'})
dailySubs_get = DailySubsAPIView.as_view({'get':'get'})
dailySubs_specific_View = DailySubsView.as_view({'get': 'retrieve', 'put': 'update'})

l1L2reports = InterviewSelectReport.as_view({'get': 'retrieve'})

requisitions = AddRequisitionsView.as_view({'get': 'list', 'post': 'create'})
requisitions_specific = AddRequisitionsView.as_view({'get': 'retrieve', 'put': 'update'})

weekly_joiners_practiceReport = WeeklyJoinersPracticeReport.as_view({'get': 'retrieve'})

audit_offer = AuditOffers.as_view({'get': 'list', 'post': 'create'})
audit_dailysub = AuditDailySubs.as_view({'get': 'list', 'post': 'create'})
audit_requisition = AuditRequisitions.as_view({'get': 'list', 'post': 'create'})
offer_status_summary = OfferStatusSummary.as_view({'get': 'retrieve'})
month_wise_offers_status = MonthWiseOffersStatus.as_view({'get': 'retrieve'})
Ageing_Wise_Requisition = AgeingWiseRequisition.as_view({'get': 'retrieve'})

user_downloads = Download.as_view({'get': 'list'})
specific_download = Download.as_view({'get': 'retrieve'})

urlpatterns = [
    path('ta_tracker_swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('dailysubs/', dailySubs_List_View, name="DailySub"),
    path('dailysubs/<int:pk>', dailySubs_specific_View, name="DailySub-specific"),
    path('dailysubs/download', dailySubs_get, name="DailySub-download"),
    path('dailysubs/add_column/', DailySubAddColumn.as_view({'get': 'list', 'post': 'create'}),
         name="add-dailysub-column"),

    path('offers/', offer_List_View, name="offers"),
    path('offers/<int:pk>', offer_specific_View, name="offer"),
    path('offers/add_column/', OffersAddColumn.as_view({'get': 'list', 'post': 'create'}), name="add-offer-column"),

    path('requisitions/', requisitions, name='Requisitions'),
    path('requisitions/<int:pk>', requisitions_specific, name="specific-Requisition"),
    path('requisitions/add_column', RequisitionsAddColumn.as_view({'get': 'list', 'post': 'create'}),
         name="add-requisition-column"),
    path('audit_offers/', audit_offer, name='audit_offer'),
    path('audit_dailysubs/', audit_dailysub, name='audit_dailysub'),
    path('audit_requisitions/', audit_requisition, name='audit_requisition'),

    # weekly_joiners/?nextorprev=next&day=2023-02-15
    path('weekly_joiners/', weekly_joiners_practiceReport, name="WeeklyJoiners"),

    # l1l2/ (or) l1l2/?date=2022-12-13
    path('l1l2/', l1L2reports, name="l1l2"),

    # offer_status_summary/?year=2023
    path('offer_status_summary/', offer_status_summary, name="OfferStatusSummary"),

    # month_offer_status_summary/?year=2023
    path('month_offer_status_summary/', month_wise_offers_status, name="Month-wise-offer-status"),
    path("overall_requirements/", OverAllRequirementReport.as_view({"get": "retrieve"}), name="overallrequirements"),

    # ageingwise/ (or) ageingwise/?date=2022-12-21
    path('ageingwise/', AgeingWiseRequisition.as_view({'get': 'retrieve'}), name="ageing-wise-requisition"),

    # priority_wise_requisition/ (or) priority_wise_requisition/?raiseDate=2023-01-23
    path("priority_wise_requisition/", PriorityWiseRequisitionReport.as_view({"get": "retrieve"}),
         name="PriorityWiseRequisitionReport"),

    path("dropdown/<str:group>/", DropdownListAPIView.as_view(), name="dropdown"),
    path("dropdown/", DropdownListAPIView.as_view(), name="dropdown"),

    path("user_downloads/", user_downloads),
    path("specific_download/<str:path>", specific_download),

    path("interview/",InterviewReport.as_view({'get': 'retrieve'}), name="interview"),
    path("decline/" , DeclineSelectReport.as_view({'get': 'retrieve'}) , name="decline"),
    path("summary/",TotalSummaryReport.as_view({'get': 'retrieve'}), name="summary"),

]
