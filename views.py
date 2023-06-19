from .serializers import DailySubSerializer, OfferSerialize, RequisitionSerializer, AuditOfferSerializer, \
    OfferAddColumnSerializer, GroupMasterSerializer, \
    RequisitionAddColumnSerializer, DailySubAddColumnSerializer, AuditDailySubSerializer, AuditRequisitionSerializer,DownloadSerializer
from .models import DailySub, Offer, Requisition, AuditOffer, AuditRequisition, AuditDailySub, MasterTable, GroupMaster,Downloads
from rest_framework.response import Response
from rest_framework import viewsets, status, views
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.db.models.functions import Extract
import datetime
from datetime import datetime, timedelta, timezone
from django.db.models import Count, Q
import calendar
import pandas as pd
from django.http import HttpResponse
from django.conf import settings
from django.http import FileResponse



PUBLIC_DIR = settings.BASE_DIR / "tracker_api" / "public"

class DailySubsAPIView(viewsets.ModelViewSet):
    """
        Class for the DailySub Create and Retrieve operations
    """
    queryset = DailySub.objects.all().order_by('id')
    serializer_class = DailySubSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ('__all__')
    ordering_fields = ('__all__')
    tableName = "DailySub"

    def list(self, request):

        """
            This method is to fetch all the data from DailySub model.
        :param request:
        :return: returns the fetched data from DailySub model with status code.
        """
        fields = MasterTable.objects.values("columnField").filter(
            tableName=self.tableName)  # get field names queryset from MasterTable.
        fieldList = [field["columnField"] for field in fields]  #
        columns = [f.name for f in DailySub._meta.get_fields()][:38] + fieldList
        filters = self.filter_queryset(self.queryset)
        page = self.paginate_queryset(filters)
        serializer = DailySubSerializer(page, fields=columns, many=True)
        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)

    def create(self, request):
        """
            This method is to post the data into DailySub model.
        :param request: The request data from the api call to POST.
        :return: returns the posted data to DailySub model with status code.
        """
        fields = MasterTable.objects.values("columnField").filter(
            tableName=self.tableName)  # get field names queryset from MasterTable.
        fieldList = [field["columnField"] for field in fields]  #
        columns = [f.name for f in DailySub._meta.get_fields()][:38] + fieldList

        serializer = self.serializer_class(data=request.data, fields=columns)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        obj = DailySub.objects.all()
        serializer = DailySubSerializer(obj, many=True)
        df = pd.DataFrame(serializer.data)
        dt = datetime.now()
        pth = f"DailySubReport{str(int(dt.replace(tzinfo=timezone.utc).timestamp()))}.xlsx"

        user = request.usr['name']
        Downloads.objects.create(user_name = user, path = pth)
        df.to_excel(PUBLIC_DIR / pth,encoding="UTF-8", index=False)

        return Response({'status': 200})



class DailySubsView(viewsets.ModelViewSet):
    """
    This class based view is used to perform update and retrieve a specific data
    """
    serializer_class = DailySubSerializer
    queryset = DailySub.objects.all().order_by('id')
    tableName = "DailySub"

    def update(self, request, pk=None):
        """
            This method is used to update a specific data by performing certain field validations.
        :param request: the request data to perform update on the specific data.
        :param pk: the id of the specific data row in DailySub model.
        :return: Returns updated data for success and error message for failure, and status code.
        """
        fields = MasterTable.objects.values("columnField").filter(
            tableName=self.tableName)  # get field names queryset from MasterTable.
        fieldList = [field["columnField"] for field in fields]  #
        columns = [f.name for f in DailySub._meta.get_fields()][:38] + fieldList

        queryset = get_object_or_404(DailySub, id=pk)
        DailySubSerializer = self.serializer_class(queryset, data=request.data, fields=fieldList)
        if DailySubSerializer.is_valid():
            DailySubSerializer.save()
            return Response(DailySubSerializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(DailySubSerializer.errors, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        """
            This method is used to update a specific data by performing certain field validations.
        :param request: request data from api.
        :param pk: the id of the specific data row in DailySub model.
        :return: Returns specific row data in DailySub model.
        """
        if pk is not None:
            fields = MasterTable.objects.values("columnField").filter(
                tableName=self.tableName)  # get field names queryset from MasterTable.
            fieldList = [field["columnField"] for field in fields]  #
            columns = [f.name for f in DailySub._meta.get_fields()][:38] + fieldList

            queryset = get_object_or_404(DailySub, id=pk)
            SingleRecord = self.serializer_class(queryset, fields=fieldList)
            return Response(SingleRecord.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class OffersAPIView(viewsets.ModelViewSet):
    """
    This Class has two functions create and list.
    """
    queryset = Offer.objects.all().order_by('id')
    serializer_class = OfferSerialize
    filterset_fields = ('__all__')
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    ordering_fields = ('__all__')
    tableName = "Offer"

    def list(self, request):
        """
        This method is used to fetch all records from Offer Model.

        Args: 
            request:
        Returns: 
            Returns all existing offers.
        """
        fields = MasterTable.objects.values("columnField").filter(
            tableName=self.tableName)  # get field names queryset from MasterTable.
        fieldList = [field["columnField"] for field in fields]  #
        columns = [f.name for f in Offer._meta.get_fields()][:37] + fieldList

        filters = self.filter_queryset(self.queryset)
        page = self.paginate_queryset(filters)
        serializer = self.serializer_class(page, fields=columns, many=True)

        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)

    def create(self, request):
        """
        This function is used to add new record to Offer model.

        Args: 
            request: request body
        Returns:
            returns a newly added record.
        """
        fields = MasterTable.objects.values("columnField").filter(
            tableName=self.tableName)  # get field names queryset from MasterTable.
        fieldList = [field["columnField"] for field in fields]  #
        columns = [f.name for f in Offer._meta.get_fields()][:37] + fieldList

        serializer = self.serializer_class(data=request.data, fields=columns)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OfferView(viewsets.ModelViewSet):
    """
    This Class has two functions retrieve and update.
    """
    serializer_class = OfferSerialize
    queryset = Offer.objects.all().order_by('id')
    tableName = "Offer"

    def retrieve(self, request, pk=None):
        """
        This method is used to retrieve specific record form Offer.
        Args:
            request:
            pk: primary key of specific record.
        Returns:
             Returns the specific record if available or returns error status code.
        """
        fields = MasterTable.objects.values("columnField").filter(
            tableName=self.tableName)  # get field names queryset from MasterTable.
        fieldList = [field["columnField"] for field in fields]
        columns = [f.name for f in Offer._meta.get_fields()][:37] + fieldList

        if pk is not None:
            queryset = get_object_or_404(Offer, id=pk)

            offerSerialize = self.serializer_class(queryset, fields=fieldList)
            return Response(offerSerialize.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """
        This method is used to update a specific record.
        Args:
            request:
            pk: primary key of specific record.
        Returns:
            Either returns specific record after successful update if available or returns error status code.
        """
        fields = MasterTable.objects.values("columnField").filter(
            tableName=self.tableName)  # get field names queryset from MasterTable.
        fieldList = [field["columnField"] for field in fields]
        columns = [f.name for f in Offer._meta.get_fields()][:37] + fieldList

        queryset = get_object_or_404(Offer, id=pk)

        offerSerialize = self.serializer_class(queryset, data=request.data, fields=fieldList)

        if offerSerialize.is_valid():
            offerSerialize.save()
            return Response(offerSerialize.data, status=status.HTTP_202_ACCEPTED)

        return Response(offerSerialize.errors, status=status.HTTP_404_NOT_FOUND)


class AddRequisitionsView(viewsets.ModelViewSet):
    """
    This Class is used to perform the CURD operations on Requisition.
    It is inherited the viewsets.ModelViewSet Class

    Methods :
        list method gets all the records from the Requisitions Model
        create method creates a new record and adds to the Requisitions Model
        update method updates the specific record in the Requisitions Model
        retrieve method gets the specific record in the Requisitions Model
    """
    queryset = Requisition.objects.all().order_by('id')
    tableName = "Requisition"
    serializer_class = RequisitionSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ('__all__')
    ordering_fields = ('__all__')

    def list(self, request):
        """
        This function is used to fetch all records from requisitions

        Returns:
            Returns all requisitions records along with pagination
        """
        fields = MasterTable.objects.values("columnField").filter(
            tableName=self.tableName)  # get field names queryset from MasterTable.
        fieldList = [field["columnField"] for field in fields]
        columns = [f.name for f in Requisition._meta.get_fields()][:27] + fieldList

        filters = self.filter_queryset(self.queryset)
        page = self.paginate_queryset(filters)
        serializer = self.serializer_class(page, fields=columns, many=True)

        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)

    def create(self, request, format=None):
        """
        This function is used to create a new record and adds to the Requisitions.

        Params: request
        Return: Returns newly added record, or Returns error status code.
        """
        fields = MasterTable.objects.values("columnField").filter(
            tableName=self.tableName)  # get field names queryset from MasterTable.
        fieldList = [field["columnField"] for field in fields]
        columns = [f.name for f in Requisition._meta.get_fields()][:27] + fieldList

        serializer = RequisitionSerializer(data=request.data, fields=columns)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        This method is used to retrieve specific record form Requisition.
        :param request:
        :param pk: primary key of specific record.
        :return: Either returns specific record if available or returns error status code.
        """
        fields = MasterTable.objects.values("columnField").filter(
            tableName=self.tableName)  # get field names queryset from MasterTable.
        fieldList = [field["columnField"] for field in fields]
        columns = [f.name for f in Requisition._meta.get_fields()][:26] + fieldList

        if pk is not None:
            queryset = get_object_or_404(Requisition, id=pk)
            RequisitionSerializer = self.serializer_class(queryset, fields=fieldList)
            return Response(RequisitionSerializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """
        This method is used to update a specific record of Requisition.
        :param request:
        :param pk: primary key of specific record.
        :return: Either returns specific record after successful update if available or returns error status code.
        """
        fields = MasterTable.objects.values("columnField").filter(
            tableName=self.tableName)  # get field names queryset from MasterTable.
        fieldList = [field["columnField"] for field in fields]
        columns = [f.name for f in Requisition._meta.get_fields()][:26] + fieldList

        queryset = get_object_or_404(Requisition, id=pk)
        RequisitionSerializer = self.serializer_class(queryset, data=request.data, fields=fieldList)

        if RequisitionSerializer.is_valid():
            RequisitionSerializer.save()
            return Response(RequisitionSerializer.data, status=status.HTTP_200_OK)
        return Response(RequisitionSerializer.errors, status=status.HTTP_404_NOT_FOUND)


class WeeklyJoinersPracticeReport(viewsets.ModelViewSet):
    queryset = Offer.objects.all().order_by('id')
    serializer_class = OfferSerialize

    def weeksOfThree(self, monday, nextOrPrev):
        """
        This function is used to return the next three days of week in json format
        Params: day,next or previous day
        Return: Returns next three dates of week

        """
        list1 = []
        for _ in range(3):
            if nextOrPrev == "next":
                monday = monday + timedelta(days=7)
            elif nextOrPrev == "prev":
                monday = monday - timedelta(days=7)
            monthName = calendar.month_abbr[monday.month]
            column = ("Week Of " + (("0" + str(monday.day)) if (len(str(monday.day)) == 1)
                                    else str(monday.day)) + "-" + str(monthName) + "-" + monday.strftime("%Y"))
            list1.append(column)
        if nextOrPrev == "prev":
            return list1[::-1]
        return list1

    def retrieve(self, request):

        """
        This function is used to fetch WeeklyJoinersPractice report.
        Args:
        request (_type_): None

        Returns:
         Returns the weekly joiners practice report as response.
        """
        try:
            nextOrPrev = request.query_params.get('nextorprev')
            date1=request.query_params.get('day')
            if nextOrPrev in ['next', 'prev'] and date1:
                try :
                    today = datetime.strptime(date1, '%Y-%m-%d').date()
                except ValueError:
                    return Response({"message": "Please provide date format YYYY-MM-DD"}, status=status.HTTP_406_NOT_ACCEPTABLE)
                # get day of week as an integer
                dayNo = today.weekday()
                # get a monday's Date
                monday = today - timedelta(days=dayNo)
                days = self.weeksOfThree(monday, nextOrPrev)
                # Practice Data from GroupMaster Table
                data = GroupMaster.objects.values("value").filter(
                    group='Practice').order_by("value")
                # Retrieving the practices from data
                # print("data", data)
                practiceList = [name.get("value") for name in data]

                #  Table beings here
                ## Table header
                resultDict = {"results": []}

                ## Table body
                data = Offer.objects.values('practices', 'joiningWeek').filter(
                    Q(status="Offered") & (Q(joiningWeek=days[0]) | Q(
                        joiningWeek=days[1]) | Q(joiningWeek=days[2]))).annotate(pcount=Count('practices'),
                                                                                 wcount=Count('joiningWeek'))
                selectedPractices = [item.get('practices') for item in data]
                #  practices from MasterGroup Table
                week1GrandTotal = 0
                week2GrandTotal = 0
                week3GrandTotal = 0
                # print("practices", practiceList)

                for practice in practiceList:
                    row = {"practices": practice,
                           "week1": 0,
                           "week2": 0,
                           "week3": 0,
                           "grandTotal": 0}
                    # print("Rows---", row)
                    if practice in selectedPractices:

                        for item in data:
                            if item['practices'] == practice and item["joiningWeek"] == days[0]:
                                row["week1"] = item['pcount']
                                week1GrandTotal += row["week1"]
                            if item['practices'] == practice and item["joiningWeek"] == days[1]:
                                row["week2"] = item['pcount']
                                week2GrandTotal += row["week2"]
                            if item['practices'] == practice and item["joiningWeek"] == days[2]:
                                row["week3"] = item['pcount']
                                week3GrandTotal += row["week3"]
                        row["grandTotal"] = row["week1"] + row["week2"] + row["week3"]
                    # print("Rows---", row)
                    resultDict['results'].append(row)

                # Table Footer
                grandTotal = {
                    "practices": "Grand Total",
                    "week1": week1GrandTotal,
                    "week2": week2GrandTotal,
                    "week3": week3GrandTotal,
                    "grandTotal": (week1GrandTotal + week2GrandTotal + week3GrandTotal),

                }

                resultDict["results"].append(grandTotal)

                return Response(resultDict, status=status.HTTP_200_OK)
            return Response({"message": "Please check the URL"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f"There is an issue while processing the data {e}"},status=status.HTTP_406_NOT_ACCEPTABLE)


class InterviewSelectReport(viewsets.ModelViewSet):
    serializer_class = DailySubSerializer
    queryset = DailySub.objects.all().order_by('id')
    l1totalCount = 0

    def calculation(self, practice, data, selectedpractices):

        if practice in selectedpractices:
            for item in data:
                if practice == item["practice"]:
                    return item["interviewCount"]

        return 0

    def retrieve(self, request):
        # global l1totalCount
        data = GroupMaster.objects.values('value').filter(
            group='Practice').order_by("value")

        practicesList = [name['value'] for name in data]
        resultData = {"results": []}
        date1 = request.query_params.get("date")

        if date1:
            date1 = datetime.strptime(date1, '%Y-%m-%d').date()
            l1Data = DailySub.objects.values('practice').filter(
                status="L1InterviewSelect", sourceDate=date1).annotate(interviewCount=Count('practice'))
            l2Data = DailySub.objects.values('practice').filter(
                status="L2InterviewSelect", sourceDate=date1).annotate(interviewCount=Count('practice'))
        else:
            todayYear = datetime.now().year
            l1Data = DailySub.objects.values('practice').filter(
                status="L1InterviewSelect", sourceDate__year=todayYear).annotate(interviewCount=Count('practice'))
            l2Data = DailySub.objects.values('practice').filter(
                status="L2InterviewSelect", sourceDate__year=todayYear).annotate(interviewCount=Count('practice'))

        selectedpracticesL1 = [data['practice'] for data in l1Data]
        selectedpracticesL2 = [data['practice'] for data in l2Data]
        l1TotalCount = 0
        l2TotalCount = 0
        for practice in practicesList:
            l1count = self.calculation(practice, l1Data, selectedpracticesL1)
            l2count = self.calculation(practice, l2Data, selectedpracticesL2)
            row = {
                "practice": practice,
                "l1InterviewSelect": l1count,
                "l2InterviewSelect": l2count,
            }
            l1TotalCount += l1count
            l2TotalCount += l2count

            resultData["results"].append(row)
        # Table Footer Grand Total
        row = {
            "practice": "Grand Total",
            "l1InterviewSelect": l1TotalCount,
            "l2InterviewSelect": l2TotalCount,
        }
        resultData["results"].append(row)

        return Response(resultData)


class OffersAddColumn(viewsets.ModelViewSet):
    """
    This class is used to add a new dynamic column to Offers.
    """
    serializer_class = OfferAddColumnSerializer
    queryset = MasterTable.objects.filter(tableName="Offer")

    def list(self, request):
        """
        This function is used to fetch all the dynamic columns for Offers.

        Args:
            request:
        Returns:
            Returns the details of dynamic columns with status code.
        """
        queryset = MasterTable.objects.filter(tableName="Offer")
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        This function is used to create the dynamic column with name and type of the column.

        Args:
            request:
        Returns:
            Returns the created column data or error data with status code.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuditOffers(viewsets.ModelViewSet):
    """
    This Class has two functions create and list.

    create:
        This fuction is used to create a new record

    list:
        This fuction is used to list out all records
    """
    queryset = AuditOffer.objects.all().order_by('id')
    serializer_class = AuditOfferSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ('offer_id',)

    def create(self, request):
        """
        This function is used to add record, 
        whenever create or update operation performed on Offer Model

        Args:
            request:
        Returns: 
            Returns newly added record.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """
        This method is used to fetch all records form AuditOffer Model.

        Args:
            request:
        Returns:
            Returns all existing records.
        """
        filters = self.filter_queryset(self.queryset)
        page = self.paginate_queryset(filters)
        serializer = self.serializer_class(page, many=True)
        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)


class OverAllRequirementReport(viewsets.ModelViewSet):
    """View to add overall requirement report"""
    serializer_class = RequisitionSerializer

    queryset = Requisition.objects.all().order_by('id')

    totalrequirementcount = 0

    def calculation(self, practice, data, selectedpractices):
        """
         This method is used to check the values and match them with desired practices
         of the requisition and return the correct item

         """

        if practice in selectedpractices:

            for item in data:

                if practice == item["practice"]:
                    return item["totalCount"]

        return 0

    def retrieve(self, request):
        """
         This method is used to display default json format
         param request: Request
         return: Returns OverallRecruitmentReport.
        """
        result_data = {
            "results": []
        }
        """ For filter objects using practice field in requisition"""
        practices = {
            p["practice"]: Requisition.objects.filter(**p).count()
            for p in Requisition.objects.values("practice").distinct()
        }
        practice_status = {
            p: {
                s["status"]: Requisition.objects.filter(**s, practice=p).count()
                for s in Requisition.objects.values("status").distinct()
            }
            for p in practices.keys()
        }

        offers = {
            p["practices"]: Offer.objects.filter(**p).count()
            for p in Offer.objects.values("practices").distinct()
        }
        offer_status = {
            p: {
                s["status"]: Offer.objects.filter(**s, practices=p).count()
                for s in Offer.objects.values("status").distinct()
            }
            for p in offers.keys()
        }
        """ For displaying sum of all the practices at end"""
        practice_grand_sum = {}
        for practice in practices.keys():
            practice_grand_sum[practice] = 0
            for stat in ("OfferDeclined", "Offered", "Joined"):
                practice_grand_sum[practice] += practice_status[practice].get(stat, 0)
        total_offers = sum(practice_grand_sum[p] for p in practices.keys())

        for practice in practices:
            row = {
                "practice": practice,
                "totalRequirementsRaised": practices[practice],
                "approvalAwaited": practice_status.get(practice, {}).get("ApprovalAwaited", 0),
                "cancelled": practice_status.get(practice, {}).get("Cancelled", 0),
                "closed": practice_status.get(practice, {}).get("Closed", 0),
                "filled": practice_status.get(practice, {}).get("Filled", 0),
                "filledInternally": practice_status.get(practice, {}).get("FilledInternally", 0),
                "onhold": practice_status.get(practice, {}).get("OnHold", 0),
                "open": practice_status.get(practice, {}).get("Open", 0),
                "totaloffers": total_offers,
                "joined": offer_status.get(practice, {}).get("Joined", 0),
                "decline": offer_status.get(practice, {}).get("OfferDeclined", 0),
                "yettojoin": offer_status.get(practice, {}).get("Offered", 0)
            }
            result_data["results"].append(row)

        result_data["results"].append({
            "practice": "Grand Total",
            "totalRequirementsRaised": Requisition.objects.count(),
            "approvalAwaited": sum([practice_status[p].get("ApprovalAwaited", 0) for p in practices]),
            "cancelled": sum([practice_status[p].get("Cancelled", 0) for p in practices]),
            "closed": sum([practice_status[p].get("Closed", 0) for p in practices]),
            "filled": sum([practice_status[p].get("Filled", 0) for p in practices]),
            "filledInternally": sum([practice_status[p].get("FilledInternally", 0) for p in practices]),
            "onhold": sum([practice_status[p].get("OnHold", 0) for p in practices]),
            "open": sum([practice_status[p].get("Open", 0) for p in practices]),
            "totaloffers": total_offers,
            "joined": sum([offer_status[p].get("Joined", 0) for p in offers]),
            "decline": sum([offer_status[p].get("OfferDeclined", 0) for p in offers]),
            "yettojoin": sum([offer_status[p].get("Offered", 0) for p in offers]),
        })
        return Response(result_data)


class DailySubAddColumn(viewsets.ModelViewSet):
    """
        This class is to implement dynamic column functionality for DailySub model.
    """
    serializer_class = DailySubAddColumnSerializer
    queryset = MasterTable.objects.filter(tableName="DailySub")

    def list(self, request):
        """
         This method is used to fetch all the dynamic columns for DailySub.
        :param request:
        :return: returns the details of dynamic columns with status code.
        """
        queryset = MasterTable.objects.filter(tableName="DailySub")
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        This method is used to create a dynamic column with name and type of the column.
        :param request: the request body contains column data to be created.
        :return: returns the created column data or error data with status code..
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuditDailySubs(viewsets.ModelViewSet):
    """
    This Class has two functions create and list.

    create:
        This fuction is used to create a new record

    list:
        This fuction is used to list out all records
    """
    queryset = AuditDailySub.objects.all().order_by('id')
    serializer_class = AuditDailySubSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ('dailysub_id',)

    def create(self, request):
        """
        This function is used to add record, 
        whenever create or update operation performed on DailySubs Model

        Args:
            request:
        Returns: 
            Returns newly added record.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """
        This method is used to fetch all records form AuditDailySub Model.

        Args:
            request:
        Returns:
            Returns all existing records.
        """
        filters = self.filter_queryset(self.queryset)
        page = self.paginate_queryset(filters)
        serializer = self.serializer_class(page, many=True)
        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)


class RequisitionsAddColumn(viewsets.ModelViewSet):
    """
    This class is used to add the dynamic columns to Requisition.
    """
    serializer_class = RequisitionAddColumnSerializer
    queryset = MasterTable.objects.filter(tableName="Requisition")

    def list(self, request):
        """
        This method is used to fetch all the dynamic columns for Requisitions
        Returns:
            returns the details of dynamic columns with status Code
        """
        queryset = MasterTable.objects.filter(tableName="Requisition")
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """This method is used to create a dynamic column with name and type of the column.
        Args:
            request (dict): the request body contains column data to be created.

        Returns:
            returns the created column data or error data with status code.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuditRequisitions(viewsets.ModelViewSet):
    """
    This Class has two functions create and list.

    create:
        This fuction is used to create a new record

    list:
        This fuction is used to list out all records
    """
    queryset = AuditRequisition.objects.all().order_by('id')
    serializer_class = AuditRequisitionSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ('requisition_id',)

    def create(self, request):
        """
        This function is used to add record, 
        whenever create or update operation performed on Requisition Model

        Args:
            request:
        Returns: 
            Returns newly added record.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """
        This method is used to fetch all records form AuditRequisition Model.

        Args:
            request:
        Returns:
            Returns all existing records.
        """
        filters = self.filter_queryset(self.queryset)
        page = self.paginate_queryset(filters)
        serializer = self.serializer_class(page, many=True)
        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)


class OfferStatusSummary(viewsets.ModelViewSet):
    """ 
       This class-based view is used to create the report for Offers Status Summary based on practices
    """
    serializer_class = OfferSerialize
    queryset = Offer.objects.all().order_by('id')

    def retrieve(self, request):
        """ 
            This method is used to get the offer status summary report based on practices in a specific year
            param request: Request body to retrieve the data
            return: Returns a offer status summary report based on practices
        """

        joiningYear = request.query_params.get('year')
        if joiningYear:
            data = GroupMaster.objects.values('value').filter(
                group='Practice').order_by("value")

            practicesList = [name['value'] for name in data]
            resultData = {"results": []}
            data = Offer.objects.values("practices", "status").filter(
                Q(dateOfJoining__year=joiningYear) & (Q(status="Joined") | Q(status="OfferDeclined") | Q(
                    status="OfferAccepted"))).annotate(pCount=Count('practices'), sCount=Count('status'))

            selectedPractice = [item['practices'] for item in data]
            totalJoined = 0
            totalOfferDeclined = 0
            totalYetToJoinData = 0
            for practice in practicesList:
                row = {
                    "practices": practice,
                    "Joined": 0,
                    "Declined": 0,
                    "YetToJoinData": 0,
                    "total": 0,
                }

                if practice in selectedPractice:

                    for item in data:
                        if practice == item['practices'] and item['status'] == "Joined":
                            row['Joined'] = item['pCount']
                            totalJoined += row['Joined']
                        if practice == item['practices'] and item['status'] == "OfferDeclined":
                            row['Declined'] = item['pCount']
                            totalOfferDeclined += row['Declined']
                        if practice == item['practices'] and item['status'] == "OfferAccepted":
                            row['YetToJoinData'] = item['pCount']
                            totalYetToJoinData += row['YetToJoinData']
                    row['total'] = row['Joined'] + \
                                   row['Declined'] + row['YetToJoinData']

                resultData["results"].append(row)

            row = {
                "practices": "Grand Total",
                "Joined": totalJoined,
                "Declined": totalOfferDeclined,
                "YetToJoinData": totalYetToJoinData,
                "total": (totalJoined + totalOfferDeclined + totalYetToJoinData),
            }
            resultData["results"].append(row)

            return Response(resultData)
        return Response(status=status.HTTP_404_NOT_FOUND)


class MonthWiseOffersStatus(viewsets.ModelViewSet):
    """
       This class-based view is used to create the report for Month wise offers Status Summary  
    """

    serializer_class = OfferSerialize
    queryset = Offer.objects.all().order_by('id')

    def retrieve(self, request):
        """ 
            This method is used to get  offers status summary report based on specific month
            param request: Request body to retrieve the data
            return: Returns a offers status summary report based on specific month in a year
        """

        joiningYear = request.query_params.get('year')
        if joiningYear:
            monthsData = Offer.objects.annotate(month_stamp=Extract('dateOfJoining', 'month')).values('month_stamp',
                                                                                                      'status').filter(
                Q(dateOfJoining__year=joiningYear) & (
                        Q(status="Joined") | Q(status="OfferDeclined") | Q(status="OfferAccepted"))).annotate(
                count1=Count('month_stamp'), count2=Count('status'))

            resultData = {"results": []}
            months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            selectedMonths = [item['month_stamp'] for item in monthsData]
            totalJoined = 0
            totalOfferDeclined = 0
            totalYetToJoinData = 0
            for monthNum in months:
                row = {
                    "months": calendar.month_abbr[monthNum],
                    "joined": 0,
                    "declined": 0,
                    "yetToJoinData": 0,
                    "total": 0
                }
                if monthNum in selectedMonths:
                    for item in monthsData:
                        if item["month_stamp"] == monthNum and item["status"] == "Joined":
                            row["joined"] = item["count1"]
                            totalJoined += row['joined']
                        elif item["month_stamp"] == monthNum and item["status"] == "OfferDeclined":
                            row["declined"] = item["count1"]
                            totalOfferDeclined += row['declined']
                        elif item["month_stamp"] == monthNum and item["status"] == "OfferAccepted":
                            row["yetToJoinData"] = item["count1"]
                            totalYetToJoinData += row['yetToJoinData']
                    row['total'] = row['joined'] + \
                                   row['declined'] + row['yetToJoinData']
                resultData["results"].append(row)
            row = {
                "months": "Grand Total",
                "joined": totalJoined,
                "declined": totalOfferDeclined,
                "yetToJoinData": totalYetToJoinData,
                "total": (totalJoined + totalOfferDeclined + totalYetToJoinData),
            }
            resultData["results"].append(row)

            return Response(resultData)
        return Response(status=status.HTTP_404_NOT_FOUND)


class DropdownListAPIView(views.APIView):
    """Dropdown List API View"""

    queryset = GroupMaster.objects.all().order_by('id')
    serializer_class = GroupMasterSerializer

    def get(self, request, *args, **kwargs):

        groups = self.queryset.filter(**self.kwargs).values("group").distinct()
        data = {}
        for group in groups:
            grouped_data = []
            for record in self.queryset.filter(**group):
                grouped_data.append({
                    "id": record.name,
                    "name": record.name,
                    "isActive": record.isActive,
                })
            data[group["group"]] = grouped_data
        return Response(data, status.HTTP_200_OK)


class AgeingWiseRequisition(viewsets.ModelViewSet):
    """ Class based view to extract age wise requisition """

    queryset = Requisition.objects.all()

    queryset = Requisition.objects.all().order_by('id')
    serializer_class = RequisitionSerializer

    def retrieve(self, request):
        """ This method extracts data by meeting all the defined criteria to return proper JSON Response"""

        requisition_data = Requisition.objects.all().filter(status='open')
        date1 = request.query_params.get("date")

        if date1:
            date1 = datetime.strptime(date1, "%Y-%m-%d").date()
            requisitionData = Requisition.objects.all().order_by('id').filter(status='open', requisitionRaiseDate=date1)
        else:
            todayYear = datetime.now().year
            requisitionData = Requisition.objects.all().order_by('id').filter(status='open',
                                                                              requisitionRaiseDate__year=todayYear)
        # print(requisitionData)

        """ Default JSON Response that will be returned when endpoint is hit """

        result_data = {

            "result":[]
        }

        """ Initializing high,medium and low values to zero as default and predefining days for ageing """

        high_total = 0
        medium_total = 0
        low_total = 0
        row_0_30 = {"ageing": "0-30 Days", "high": 0, "medium": 0, "low": 0, "total": 0}
        row_31_60 = {"ageing": "31-60 Days", "high": 0, "medium": 0, "low": 0, "total": 0}
        row_61_90 = {"ageing": "61-90 Days", "high": 0, "medium": 0, "low": 0, "total": 0}
        row_90 = {"ageing": "90+ Days", "high": 0, "medium": 0, "low": 0, "total": 0}

        """ This loop filters data according to Criteria 1 and Criteria 2 as defined in requirements """

        for requisition in requisition_data:
            print(requisition.days)
            if requisition.days == "0-30 Days":
                # requisition.currentWeekPriority
                if requisition.currentWeekPriority == "High":
                    row_0_30["high"] += 1
                    high_total += 1

                elif requisition.currentWeekPriority == "medium":
                    row_0_30["medium"] += 1
                    medium_total += 1

                elif requisition.currentWeekPriority == "low":
                    row_0_30["low"] += 1
                    low_total += 1
                    row_0_30["total"] += 1

            elif requisition.days == "31-60 Days":

                if requisition.currentWeekPriority == "High":
                    row_31_60["high"] += 1
                    high_total += 1

                elif requisition.currentWeekPriority == "medium":
                    row_31_60["medium"] += 1
                    medium_total += 1

                elif requisition.currentWeekPriority == "low":
                    row_31_60["low"] += 1
                    low_total += 1
                    row_31_60["total"] += 1

            elif requisition.days == "61-90 Days":

                if requisition.currentWeekPriority == "High":
                    row_61_90["high"] += 1
                    high_total += 1

                elif requisition.currentWeekPriority == "medium":
                    row_61_90["medium"] += 1
                    medium_total += 1

                elif requisition.currentWeekPriority == "low":
                    row_61_90["low"] += 1
                    low_total += 1
                    row_61_90["total"] += 1

            elif requisition.days == "90+ Days":

                if requisition.currentWeekPriority == "High":
                    row_90["high"] += 1
                    high_total += 1

                elif requisition.currentWeekPriority == "medium":
                    row_90["medium"] += 1
                    medium_total += 1

                elif requisition.currentWeekPriority == "low":
                    row_90["low"] += 1
                    low_total += 1
                    row_90["total"] += 1

                """ Final JSON Response format that will be returned when Endpoint is hit"""

        last_row = {
            "grandTotal": "Grand Total",
            "high": high_total,
            "medium": medium_total,
            "low": low_total,
            "grand_total": (high_total + medium_total + low_total),
        }
        result_data["result"].extend([row_0_30, row_31_60, row_61_90, row_90, last_row])

        return Response(result_data)


class PriorityWiseRequisitionReport(viewsets.ModelViewSet):
    """
    This class-based view is used to create the report for Offers Status Summary based on practices
    """
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer

    def retrieve(self, request):

        """
        This method is used to get the PriorityWiseRequsition summary report based on practices using
        currentweekpriority
        param request: Request body to retrieve the data
        return: Returns  PriorityWiseRequsition summary report based on practices
        """





        raiseDate = request.query_params.get('raiseDate')

        # Practice Data from GroupMaster Table

        data = GroupMaster.objects.values("value").filter(

            group='Practice').order_by("value")

        practiceList = [name["value"] for name in data]

        if (raiseDate):

            raiseDate = datetime.strptime(raiseDate, '%Y-%m-%d').date()

            data = Requisition.objects.values("practice", "currentWeekPriority").filter(

                status="Open", requisitionRaiseDate=raiseDate).annotate(pCount=Count("practice"),
                                                                        cwpCount=Count("currentWeekPriority"))
        else:

            todayYear = datetime.now().year

            data = Requisition.objects.values("practice", "currentWeekPriority").filter(

                status="Open", requisitionRaiseDate__year=todayYear).annotate(pCount=Count("practice"),
                                                                              cwpCount=Count("currentWeekPriority"))
        resultData = {'results': []}

        selectedPractices = [item['practice'] for item in data]

        highGrandTotal = 0

        mediumGrandTotal = 0

        lowGrandTotal = 0

        for practice in practiceList:

            row = {"practices": practice,

                   "high": 0,

                   "medium": 0,

                   "low": 0,

                   "grandTotal": 0

                   }

            if practice in selectedPractices:

                for item in data:

                    if item['practice'] == practice and item["currentWeekPriority"] == "High":
                        row["high"] = item['pCount']

                        highGrandTotal += row["high"]

                    if item['practice'] == practice and item["currentWeekPriority"] == "Medium":
                        row["medium"] = item['pCount']

                        mediumGrandTotal += row["medium"]

                    if item['practice'] == practice and item["currentWeekPriority"] == "Low":
                        row["low"] = item['pCount']

                        lowGrandTotal += row["low"]

                row["grandTotal"] = row["high"] + row["medium"] + row["low"]

            resultData['results'].append(row)

        # Table Footer

        grandTotal = {

            "practices": "Grand Total",

            "high": highGrandTotal,

            "medium": mediumGrandTotal,

            "low": lowGrandTotal,

            "grandTotal": (highGrandTotal + mediumGrandTotal + lowGrandTotal),

        }

        resultData["results"].append(grandTotal)

        return Response(resultData, status=status.HTTP_200_OK)


class Download(viewsets.ModelViewSet):

    serializer_class = DownloadSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('__all__')
    ordering_fields = ('__all__')

    def list(self, request):
        name = request.query_params.get("user_name")
        if name is not None:
            queryset = Downloads.objects.filter(user_name = name)
            user_downloads = self.serializer_class(queryset,  many=True)
            return Response(user_downloads.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, path=None):

        if path is not None:
            queryset = get_object_or_404(Downloads, path = path)
            SingleRecord = self.serializer_class(queryset)

            file_path = PUBLIC_DIR / SingleRecord.data['path']

            response = FileResponse(open(file_path, 'rb')) 
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_path) 
            return response
            # data = pd.read_excel(file_path)
            # context = {'data': data.to_dict()}
            # response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            # response['Content-Disposition'] = f'attachment; filename={path}'

            # print(response)
            # return response
        return Response(status=status.HTTP_404_NOT_FOUND)


class InterviewReport(viewsets.ModelViewSet):
    serializer_class = DailySubSerializer
    queryset = DailySub.objects.all()
    l1totalCount = 0

    def calculation(self, practice, data, selectedpractices):

        if practice in selectedpractices:
            for item in data:
                if practice == item["practice"]:
                    return item["interviewCount"]

        return 0

    def retrieve(self, request):
        # global l1totalCount
        data = GroupMaster.objects.values('value').filter(
            group='Practice').order_by("value")

        practicesList = [name['value'] for name in data]
        resultData = {"interview": [

        ]}
        date1 = request.query_params.get("date")

        if (date1):
            date1 = datetime.strptime(date1, '%Y-%m-%d').date()
            l1Data = DailySub.objects.values('practice').filter(
                status="L1InterviewSelect", sourceDate=date1).annotate(interviewCount=Count('practice'))
            l2Data = DailySub.objects.values('practice').filter(
                status="L2InterviewSelect", sourceDate=date1).annotate(interviewCount=Count('practice'))
        else:
            todayYear = datetime.now().year
            l1Data = DailySub.objects.values('practice').filter(
                status="L1InterviewSelect", sourceDate__year=todayYear).annotate(interviewCount=Count('practice'))
            l2Data = DailySub.objects.values('practice').filter(
                status="L2InterviewSelect", sourceDate__year=todayYear).annotate(interviewCount=Count('practice'))

        selectedpracticesL1 = [data['practice'] for data in l1Data]
        selectedpracticesL2 = [data['practice'] for data in l2Data]
        l1TotalCount = 0
        l2TotalCount = 0
        for practice in practicesList:
            l1count = self.calculation(practice, l1Data, selectedpracticesL1)
            l2count = self.calculation(practice, l2Data, selectedpracticesL2)
            row = {
                "practice": practice,
                "l1": l1count,
                "l2": l2count,
            }
            l1TotalCount += l1count
            l2TotalCount += l2count

            resultData["interview"].append(row)



        return Response(resultData)


class DeclineSelectReport(viewsets.ModelViewSet):
    serializer_class = DailySubSerializer
    queryset = DailySub.objects.all()
    l1totalCount = 0

    def calculation(self, declineReasons, data, selectedpractices):

        if declineReasons in selectedpractices:
            for item in data:
                if declineReasons == item["declineReasons"]:
                    return item["interviewCount"]

        return 0

    def retrieve(self, request):
        data = GroupMaster.objects.values('value').filter(
            group='DeclineReasons').order_by("value")

        practicesList = [name['value'] for name in data]
        resultData = {"Decline": [

        ]}
        date1 = request.query_params.get("date")

        if (date1):
            date1 = datetime.strptime(date1, '%Y-%m-%d').date()
            l1Data = DailySub.objects.values('declineReasons').filter(
                status="OfferDeclined", sourceDate=date1).annotate(interviewCount=Count('declineReasons'))
        else:
            todayYear = datetime.now().year
            l1Data = DailySub.objects.values('declineReasons').filter(
                status="OfferDeclined", sourceDate__year=todayYear).annotate(interviewCount=Count('declineReasons'))

        selectedpracticesL1 = [data['declineReasons'] for data in l1Data]
        l1TotalCount = 0
        for declineReasons in practicesList:
            l1count = self.calculation(declineReasons, l1Data, selectedpracticesL1)

            row = {
                "reason": declineReasons,
                "data": l1count,
            }
            l1TotalCount += l1count


            resultData["Decline"].append(row)



        return Response(resultData)


class TotalSummaryReport(viewsets.ModelViewSet):
    serializer_class = RequisitionSerializer

    queryset = Requisition.objects.all()

    totalrequirementcount = 0

    def calculation(self, practice, data, selectedpractices):

        if practice in selectedpractices:

            for item in data:

                if practice == item["practice"]:
                    return item["totalCount"]

        return 0

    def retrieve(self, request, *args, **kwargs):
        result_data = {"SummaryTableData": []}
        practices = {
            p["practice"]: Requisition.objects.filter(**p).count()
            for p in Requisition.objects.values("practice").distinct()
        }
        practice_status = {
            p: {
                s["status"]: Requisition.objects.filter(**s, practice=p).count()
                for s in Requisition.objects.values("status").distinct()
            }
            for p in practices.keys()
        }

        offers = {
            p["practices"]: Offer.objects.filter(**p).count()
            for p in Offer.objects.values("practices").distinct()
        }
        offer_status = {
            p: {
                s["status"]: Offer.objects.filter(**s, practices=p).count()
                for s in Offer.objects.values("status").distinct()
            }
            for p in offers.keys()
        }

        offer_grand_sum = {}
        for offer in offers.keys():
            offer_grand_sum[offer] = 0
            for stat in ("OfferDeclined", "Offered", "Joined"):
                offer_grand_sum[offer] += offer_status[offer].get(stat, 0)
        total_offers = sum(o for o in offers.values())

        result_data["SummaryTableData"].append({
            "offers": [
                {
                    "totaloffers": total_offers,
                    "joined": sum([offer_status[p].get("Joined", 0) for p in offers]),
                    "decline": sum([offer_status[p].get("OfferDeclined", 0) for p in offers]),
                    "yettojoin": sum([offer_status[p].get("Offered", 0) for p in offers]),
                }
            ],
            "approvalawaited": sum([practice_status[p].get("ApprovalAwaited", 0) for p in practices]),
            "cancelled": sum([practice_status[p].get("Cancelled", 0) for p in practices]),
            "filled": sum([practice_status[p].get("Filled", 0) for p in practices]),
            "filledinternally": sum([practice_status[p].get("FilledInternally", 0) for p in practices]),
            "onhold": sum([practice_status[p].get("OnHold", 0) for p in practices]),
            "open": sum([practice_status[p].get("Open", 0) for p in practices]),
            "closed": sum([practice_status[p].get("Closed", 0) for p in practices]),
        })
        result_data["SummaryTableData"][-1]["totalrequirementraised"] = sum(
            [v for v in result_data["SummaryTableData"][-1].values() if isinstance(v, int)]
        )
        return Response(result_data)


