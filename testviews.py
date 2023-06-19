from django.test import TestCase, Client
from django.urls import reverse
from tracker_api.models import DailySub, Requisition, Offer, MasterTable
from tracker_api.models import DailySub, Requisition, Offer

import json
from rest_framework import status, test



class TestDailySubView(TestCase):
    """
    This class is for test cases to DailySub API endpoints.
    """
    client = Client()

    @classmethod
    def setUpTestData(cls):
        number_of_candidates = 4
        for a in range(number_of_candidates):
            DailySub.objects.create(
                businessGroup=1,
                sourceDate='2022-07-01',
                sourcer='abc',
                recruiter='Feroz',
                manager='Sruesh',
                rrID=3632 + a,
                jobLocation='Hyderabad',
                practice='DotNet',
                skill='Angular',
                source='SocialMedia',
                source2='Naukri',
                fullName='abc',
                candidateName='Ajay',
                emailID='ajay@gmail.com',
                contactNo=9696969696,
                currentLocation='Hyderbad',
                experienceIn='2.0',
                currentOrg='TCS',
                currentCTC='6.0',
                expectedCTC='9',
                noticePeriod='16',
                l1InterviewDate='2022-07-04',
                l1Interviewer='Hari Varma',
                l2InterviewDate='2022-07-08',
                l2Interviewer='shaik Feroz',
                l3InterviewDate='2022-07-15',
                l3Interviewer='Suresh Kumar',
                status='Offered',
                feedback='Good Technical knowledge',
                dateOfOffer='2022-07-27',
                dateOfJoining='2022-08-22',
                dateOfDecline='2022-07-14',
                declineReasons='abc',
                week='Week of 27 June 2022',
                recordingLinkL1='abc',
                recordingLinkL2='abc',
                remarks='abc'
            )

        for a in range(number_of_candidates):
            DailySub.objects.create(
                businessGroup="2",
                sourceDate='2022-07-01',
                sourcer='abc',
                recruiter='Feroz',
                manager='Sruesh',
                rrID=3632 + a,
                jobLocation='Hyderabad',
                practice='Python',
                skill='Django',
                source='SocialMedia',
                source2='Naukri',
                fullName='abc',
                candidateName='Kishore',
                emailID='kishore@gmail.com',
                contactNo=9000270001,
                currentLocation='Hyderbad',
                experienceIn='2.0',
                currentOrg='TCS',
                currentCTC='6.0',
                expectedCTC='10',
                noticePeriod='16',
                l1InterviewDate='2022-07-04',
                l1Interviewer='Hari Varma',
                l2InterviewDate='2022-07-08',
                l2Interviewer='shaik Feroz',
                l3InterviewDate='2022-07-15',
                l3Interviewer='Suresh Kumar',
                status='Offered',
                feedback='Good Technical knowledge',
                dateOfOffer='2022-07-27',
                dateOfJoining='2022-08-22',
                dateOfDecline='2022-07-14',
                declineReasons='abc',
                week='Week of 27 June 2022',
                recordingLinkL1='abc',
                recordingLinkL2='abc',
                remarks='abc'
            )

        MasterTable.objects.create(
            columnName="Address",
            columnType="String",
            columnField="column_1",
            tableName="DailySub"
        )

    def test_url_GET(self):
        """
        This test case is implemented to check if the DailySub endpoint is working or not.
        :param: None
        :return: None
        """
        response = self.client.get(reverse('DailySub'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_correct_or_not(self):
        """
        This test case is to check if pagination is working or not.
        :param: None
        :return: None.
        """
        response = self.client.get(reverse('DailySub'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 5)

    def test_filter(self):
        """
        This test case is to check the filtering of data from DailySub model.
        :param: None.
        :return: None.
        """
        response = self.client.get(reverse('DailySubs'), {'practice': 'DotNet'})
        self.assertEqual(len(response.json()['results']), 2)

    def test_filter2(self):
        response = self.client.get(reverse('DailySub'), {'practice': 'DotNet'})
        response_1 = self.client.get(reverse('DailySub'), {'practice': 'Data'})
        self.assertEqual((response.json()['results'][0]['practice']), 'DotNet')
        self.assertEqual((response_1.json()['results']), [])

    def test_DailySub_view_GET_specific_data(self):
        """
        This test case is to retrieve a specific record from DailySub API endpoint.
        :param: None.
        :return: None.
        """
        response = self.client.get(reverse('DailySub-specific', args=[1]))
        response_1 = self.client.get(reverse('DailySub-specific', args=[1000]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_1.status_code, 404)

    def test_DailySub_view_PUT_specific_data(self):
        """
        This test case is to check if updating a specific-record is working or not.
        :param: None.
        :return: None.
        """
        specific_record = json.dumps(
            {
                "businessGroup": 1,
                "sourceDate": '2022-07-01',
                "sourcer": 'abc', "recruiter": 'Feroz',
                "manager": 'Sruesh',
                "rrID": 3632 + 1,
                "jobLocation": 'Hyderabad',
                "practice": ' DotNet',
                "skill": 'Angular',
                "source": 'SocialMedia',
                "source2": 'Naukri',
                "fullName": 'abc',
                "candidateName": 'Shreya',
                "emailID": 'shreya@gmail.com',
                "contactNo": 9848145594,
                "currentLocation": 'Hyderbad',
                "experienceIn": '2.0',
                "currentOrg": 'TCS',
                "currentCTC": '6.0',
                "expectedCTC": '8.0',
                "noticePeriod": '16',
                "l1InterviewDate": '2022-07-04',
                "l1Interviewer": 'Hari Varma',
                "l2InterviewDate": '2022-07-08',
                "l2Interviewer": 'shaik Feroz',
                "l3InterviewDate": '2022-07-15',
                "l3Interviewer": 'Suresh Kumar',
                "status": 'Offered',
                "feedback": 'Good Technical knowledge',
                "dateOfOffer": '2022-07-27',
                "dateOfJoining": '2022-08-22',
                "dateOfDecline": '2022-07-14',
                "declineReasons": 'abc',
                "week": 'Week of 27 June 2022',
                "recordingLinkL1": 'abc',
                "recordingLinkL2": 'abc',
                "remarks": 'abc'
            })

        specific_record_1 = json.dumps(
            {"businessGroup": 1,
             "sourceDate": '2022-07-01',
             "sourcer": 'abc',
             "recruiter": 'Feroz',
             "manager": 'Sruesh',
             "rrID": 3632 + 1,
             "jobLocation": 'Hyderabad',
             "practice": ' DotNet',
             "skill": 'Angular',
             "source": 'SocialMedia',
             "source2": 'Naukri',
             "fullName": 'abc',
             "candidateName": 'Shreya',
             "emailID": 'sureshgmail.com',
             "contactNo": 9848145594,
             "currentLocation": 'Hyderbad',
             "experienceIn": '2.0',
             "currentOrg": 'TCS',
             "currentCTC": '6.0',
             "expectedCTC": '8.0',
             "noticePeriod": '16',
             "l1InterviewDate": '2022-07-04',
             "l1Interviewer": 'Hari Varma',
             "l2InterviewDate": '2022-07-08',
             "l2Interviewer": 'shaik Feroz',
             "l3InterviewDate": '2022-07-15',
             "l3Interviewer": 'Suresh Kumar',
             "status": 'Offered',
             "feedback": 'Good Technical knowledge',
             "dateOfOffer": '2022-07-27',
             "dateOfJoining": '2022-08-22',
             "dateOfDecline": '2022-07-14',
             "declineReasons": 'abc',
             "week": 'Week of 27 June 2022',
             "recordingLinkL1": 'abc',
             "recordingLinkL2": 'abc',
             "remarks": 'abc'
             })

        specific_record_2 = json.dumps(
            {"businessGroup": 2,
             "sourceDate": '2022-07-01',
             "sourcer": 'abc',
             "recruiter": 'Feroz',
             "manager": 'Sruesh',
             "rrID": 3632 + 1,
             "jobLocation": 'Hyderabad',
             "practice": ' DotNet',
             "skill": 'Angular',
             "source": 'SocialMedia',
             "source2": 'Naukri',
             "fullName": 'abc',
             "candidateName": 'Shreya',
             "emailID": 'suresh@gmail.com',
             "contactNo": 984814559,
             "currentLocation": 'Hyderbad',
             "experienceIn": '2.0',
             "currentOrg": 'TCS',
             "currentCTC": '6.0',
             "expectedCTC": '8.0',
             "noticePeriod": '16',
             "l1InterviewDate": '2022-07-04',
             "l1Interviewer": 'Hari Varma',
             "l2InterviewDate": '2022-07-08',
             "l2Interviewer": 'shaik Feroz',
             "l3InterviewDate": '2022-07-15',
             "l3Interviewer": 'Suresh Kumar',
             "status": 'Offered',
             "feedback": 'Good Technical knowledge',
             "dateOfOffer": '2022-07-27',
             "dateOfJoining": '2022-08-22',
             "dateOfDecline": '2022-07-14',
             "declineReasons": 'abc',
             "week": 'Week of 27 June 2022',
             "recordingLinkL1": 'abc',
             "recordingLinkL2": 'abc',
             "remarks": 'abc'
             })

        specific_record_3 = json.dumps(
            {"businessGroup": 2,
             "sourceDate": '2022-07-01',
             "sourcer": 'abc',
             "recruiter": 'Feroz',
             "manager": 'Sruesh',
             "rrID": 3632 + 1,
             "jobLocation": 'Hyderabad',
             "practice": ' DotNet',
             "skill": 'Angular',
             "source": 'SocialMedia',
             "source2": 'Naukri',
             "fullName": 'abc',
             "candidateName": 'Shreya',
             "emailID": 'suresh@gmail.com',
             "contactNo": 6666666666,
             "currentLocation": 'Hyderbad',
             "experienceIn": '2.0',
             "currentOrg": 'TCS',
             "currentCTC": '10.0',
             "expectedCTC": '8.0',
             "noticePeriod": '16',
             "l1InterviewDate": '2022-07-04',
             "l1Interviewer": 'Hari Varma',
             "l2InterviewDate": '2022-07-08',
             "l2Interviewer": 'shaik Feroz',
             "l3InterviewDate": '2022-07-15',
             "l3Interviewer": 'Suresh Kumar',
             "status": 'Offered',
             "feedback": 'Good Technical knowledge',
             "dateOfOffer": '2022-07-27',
             "dateOfJoining": '2022-08-22',
             "dateOfDecline": '2022-07-14',
             "declineReasons": 'abc',
             "week": 'Week of 27 June 2022',
             "recordingLinkL1": 'abc',
             "recordingLinkL2": 'abc',
             "remarks": 'abc'
             })

        response = self.client.put(reverse('DailySub-specific', args=[1]), data=specific_record,
                                   content_type="application/json")
        response_1 = self.client.put(reverse('DailySub-specific', args=[1]), data=specific_record_1,
                                     content_type="application/json")
        response_2 = self.client.put(reverse('DailySub-specific', args=[1]), data=specific_record_2,
                                     content_type="application/json")
        response_3 = self.client.put(reverse('DailySub-specific', args=[1]), data=specific_record_3,
                                     content_type="application/json")

        self.assertEquals(response.status_code, 202)
        self.assertEquals(response_1.status_code, 404)
        self.assertEquals(response_2.status_code, 404)
        self.assertEquals(response_3.status_code, 404)

    def test_POST(self):
        """
        This test is to check if post request is working or not for DailySub endpoints.
        :return:
        """
        postData = json.dumps({"businessGroup": 7,
                               "sourceDate": '2022-07-01',
                               "sourcer": 'abc',
                               "recruiter": 'Feroz',
                               "manager": 'Sruesh',
                               "rrID": 3632 + 1,
                               "jobLocation": 'Hyderabad',
                               "practice": 'DotNet',
                               "skill": 'Angular',
                               "source": 'SocialMedia',
                               "source2": 'Naukri',
                               "fullName": 'abc',
                               "candidateName": 'Karthik',
                               "emailID": 'karthik@gmail.com',
                               "contactNo": 9550639342,
                               "currentLocation": 'Hyderbad',
                               "experienceIn": '2.0',
                               "currentOrg": 'TCS',
                               "currentCTC": '6.0',
                               "expectedCTC": '8.0',
                               "noticePeriod": '16',
                               "l1InterviewDate": '2022-07-04',
                               "l1Interviewer": 'Hari Varma',
                               "l2InterviewDate": '2022-07-08',
                               "l2Interviewer": 'shaik Feroz',
                               "l3InterviewDate": '2022-07-15',
                               "l3Interviewer": 'Suresh Kumar',
                               "status": 'Offered',
                               "feedback": 'Good Technical knowledge',
                               "dateOfOffer": '2022-07-27',
                               "dateOfJoining": '2022-08-22',
                               "dateOfDecline": '2022-07-14',
                               "declineReasons": 'abc',
                               "week": 'Week of 27 June 2022',
                               "recordingLinkL1": 'abc',
                               "recordingLinkL2": 'abc',
                               "remarks": 'abc'
                               })

        postData_1 = json.dumps({"businessGroup": 7,
                                 "sourceDate": '2022-07-01',
                                 "sourcer": 'abc',
                                 "recruiter": 'Feroz',
                                 "manager": 'Sruesh',
                                 "rrID": 3632 + 1,
                                 "jobLocation": 'Hyderabad',
                                 "practice": 'DotNet',
                                 "skill": 'Angular',
                                 "source": 'SocialMedia',
                                 "source2": 'Naukri',
                                 "fullName": 'abc',
                                 "candidateName": 'Karthik',
                                 "emailID": 'karthikgmail.com',
                                 "contactNo": 955063934,
                                 "currentLocation": 'Hyderbad',
                                 "experienceIn": '2.0',
                                 "currentOrg": 'TCS',
                                 "currentCTC": '10.0',
                                 "expectedCTC": '8.0',
                                 "noticePeriod": '16',
                                 "l1InterviewDate": '2022-07-04',
                                 "l1Interviewer": 'Hari Varma',
                                 "l2InterviewDate": '2022-07-08',
                                 "l2Interviewer": 'shaik Feroz',
                                 "l3InterviewDate": '2022-07-15',
                                 "l3Interviewer": 'Suresh Kumar',
                                 "status": 'Offered',
                                 "feedback": 'Good Technical knowledge',
                                 "dateOfOffer": '2022-07-27',
                                 "dateOfJoining": '2022-08-22',
                                 "dateOfDecline": '2022-07-14',
                                 "declineReasons": 'abc',
                                 "week": 'Week of 27 June 2022',
                                 "recordingLinkL1": 'abc',
                                 "recordingLinkL2": 'abc',
                                 "remarks": 'abc'
                                 })

        postData_2 = json.dumps({"businessGroup": 7,
                                 "sourceDate": '2022-07-01',
                                 "sourcer": 'abc',
                                 "recruiter": 'Feroz',
                                 "manager": 'Sruesh',
                                 "rrID": 3632 + 1,
                                 "jobLocation": 'Hyderabad',
                                 "practice": 'DotNet',
                                 "skill": 'Angular',
                                 "source": 'SocialMedia',
                                 "source2": 'Naukri',
                                 "fullName": 'abc',
                                 "candidateName": 'Karthik',
                                 "emailID": 'karthik@gmail.com',
                                 "contactNo": 6666666666,
                                 "currentLocation": 'Hyderbad',
                                 "experienceIn": '2.0',
                                 "currentOrg": 'TCS',
                                 "currentCTC": '6.0',
                                 "expectedCTC": '8.0',
                                 "noticePeriod": '16',
                                 "l1InterviewDate": '2022-07-04',
                                 "l1Interviewer": 'Hari Varma',
                                 "l2InterviewDate": '2022-07-08',
                                 "l2Interviewer": 'shaik Feroz',
                                 "l3InterviewDate": '2022-07-15',
                                 "l3Interviewer": 'Suresh Kumar',
                                 "status": 'Offered',
                                 "feedback": 'Good Technical knowledge',
                                 "dateOfOffer": '2022-07-27',
                                 "dateOfJoining": '2022-08-22',
                                 "dateOfDecline": '2022-07-14',
                                 "declineReasons": 'abc',
                                 "week": 'Week of 27 June 2022',
                                 "recordingLinkL1": 'abc',
                                 "recordingLinkL2": 'abc',
                                 "remarks": 'abc'
                                 })

        response = self.client.post(reverse('DailySub'), data=postData, content_type="application/json")
        response_1 = self.client.post(reverse('DailySub'), data=postData_1, content_type="application/json")
        response_2 = self.client.post(reverse('DailySub'), data=postData_2, content_type="application/json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_1.status_code, 400)
        self.assertEqual(response_2.status_code, 400)

    def test_get_daily_sub_dynamic_columns(self):
        """
        This test case is to check the fetching of dynamic column data.
        :return: None
        """
        response = self.client.get(reverse("add-dailysub-column"))
        self.assertEquals(response.status_code, 200)

    def test_post_daily_sub_dynamic_columns(self):
        """
        This test case is to check the creating of dynamic column data.
        :return: None
        """
        postData = json.dumps({
            "columnName": "ResidentialAddress",
            "columnType": "String"
        })

        response = self.client.post(reverse("add-dailysub-column"), data=postData, content_type="application/json")
        self.assertEquals(response.status_code, 201)


class TestRequisition(TestCase):
    """
    This class is for test cases to Requisition API endpoints.
    """
    client = Client()

    @classmethod
    def setUpTestData(cls):
        number_of_candidates = 3
        for a in range(number_of_candidates):
            Requisition.objects.create(
                skill=".Net + React or (.Net + MVC)",
                superClass="DA",
                jobFamily="FS",
                yearOfExp="2-4 Yrs",
                grade="L3B",
                status="Cancelled",
                currentWeekPriority="Low",
                hiringManager="Shivakanth Pilly",
                hod="Umesh Udayaprakash",
                projectClient="Talent Pool",
                rrID=1001,
                practice="Microsoft",
                allocatedResource="#N/A",
                PMOStatus="#N/A",
                recruiter="Khushboo Sethi",
                permSubconContract="Permanent",
                requisitionRaiseDate="2022-11-27",
                requirement=0,
                profilesShared=0,
                screenReject=0,
                shortlistedforInterviews=0,
                selected=6,
                offersReleased=6,
                joined=1,
                yetToJoin=0,
                decline=5,
            )
        MasterTable.objects.create(
            columnName="Address",
            columnType="String",
            columnField="column_1",
            tableName="DailySub"
        )

    def test_url_exists(self):
        """
        This test case is implemented to check if the Requisitions endpoint is working or not.
        :param: None
        :return: None
        """
        response = self.client.get(reverse('Requisitions'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_correct_or_not(self):
        """
        This test case is to check if the Pagination is working or not.
        :param: None
        :return: None
        """
        response = self.client.get(reverse('Requisitions'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 3)

    def test_filter(self):
        """
        This test case is to check whether the filters is working or not.
        :param: None
        :return: None
        """
        response = self.client.get(reverse('Requisitions'), {'practice': 'Microsoft'})
        self.assertEqual(len(response.json()['results']), 3)
        response = self.client.get(reverse('Requisitions'), {'practice': 'Microsoft1'})
        self.assertEqual(len(response.json()['results']), 0)

    def test_filter_value(self):
        """
        This test case is to check whether the filters is working or not.
        :param: None
        :return: None
        """
        response = self.client.get(reverse('Requisitions'), {'practice': 'Microsoft'})
        self.assertEqual((response.json()['results'][0]['practice']), 'Microsoft')

    def test_Requisitions_view_GET_specific_data(self):
        """
        This test case is to check whether the endpoint is fetching a specific record
        :param: None
        :return: None
        """
        response = self.client.get(reverse('specific-Requisition', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_requisition_post(self):
        """
        This function is to test whether the newly record added or not
        """
        data = json.dumps({
            "skill": "AWS Cloud Engineer&DevOps",
            "superClass": "AS",
            "jobFamily": "CD",
            "yearOfExp": "5-7 yrs",
            "grade": "L5B",
            "status": "open",
            "currentWeekPriority": "Low",
            "hiringManager": "Sireesha Potla",
            "hod": "Sathyashila Muddem",
            "rrID": "1002",
            "projectClient": "Talent Pool",
            "practice": "Devops",
            "allocatedResource": "N/A",
            "PMOStatus": "N/A",
            "recruiter": "Vikash Kumar",
            "permSubconContract": "Permanent",
            "requisitionRaiseDate": "2022-08-02",
            "requirement": 1,
            "profilesShared": 706,
            "screenReject": 0,
            "shortlistedforInterviews": 0,
            "selected": 1,
            "offersReleased": 1,
            "joined": 0,
            "yetToJoin": 0,
            "decline": 1
        })

        response = self.client.post(reverse('Requisitions'), data=data, content_type="application/json")
        self.assertEqual(response.status_code, 201)

        data = json.dumps({
            "skill": "AWS Cloud Engineer&DevOps",
            "superClass": "AS",
            "jobFamily": "CD",
            "yearOfExp": "5-7 yrs",
            "grade": "L5B",
            "status": "open",
            "currentWeekPriority": "Low",
            "hiringManager": "Sireesha Potla",
            "hod": "Sathyashila Muddem",
            "rrID": "1002",
            "projectClient": "Talent Pool",
            "practice": "Devops",
            "allocatedResource": "N/A",
            "PMOStatus": "N/A",
            "recruiter": "Vikash Kumar",
            "permSubconContract": "Permanent",
            "requisitionRaiseDate": "2022-08-02",
            "requirement": 1,
            "profilesShared": 706,
            "screenReject": 0,
            "shortlistedforInterviews": 0,
            "selected": 1,
            "offersReleased": 1,
            "joined": 0,
            "yetToJoin": 0,
            # "decline": 1
        })

        response = self.client.post(reverse('Requisitions'), data=data, content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_requisistion_put(self):
        """
        This function is to test the update method
        """
        data = json.dumps({
            "skill": "AWS Cloud Engineer&DevOps",
            "superClass": "AS",
            "jobFamily": "CD",
            "yearOfExp": "5-7 yrs",
            "grade": "L5B",
            "status": "open",
            "currentWeekPriority": "Low",
            "hiringManager": "Sireesha Potla",
            "hod": "Sathyashila Muddem",
            "rrID": "1002",
            "projectClient": "Talent Pool",
            "practice": "Devops",
            "allocatedResource": "N/A",
            "PMOStatus": "N/A",
            "recruiter": "Vikash Kumar",
            "permSubconContract": "Permanent",
            "requisitionRaiseDate": "2022-08-02",
            "requirement": 1,
            "profilesShared": 706,
            "screenReject": 0,
            "shortlistedforInterviews": 0,
            "selected": 1,
            "offersReleased": 1,
            "joined": 0,
            "yetToJoin": 0,
            "decline": 1,
        })

        response = self.client.put(reverse('specific-Requisition', args=[1]), data=data,
                                   content_type="application/json")
        self.assertEqual(response.status_code, 200)

        data = json.dumps({
            "skill": "AWS Cloud Engineer&DevOps",
            "superClass": "AS",
            "jobFamily": "CD",
            "yearOfExp": "5-7 yrs",
            "grade": "L5B",
            "status": "open",
            "currentWeekPriority": "Low",
            "hiringManager": "Sireesha Potla",
            "hod": "Sathyashila Muddem",
            "rrID": "1002",
            "projectClient": "Talent Pool",
            "practice": "Devops",
            "allocatedResource": "N/A",
            "PMOStatus": "N/A",
            "recruiter": "Vikash Kumar",
            "permSubconContract": "Permanent",
            "requisitionRaiseDate": "2022-08-02",
            "requirement": 1,
            "profilesShared": 706,
            "screenReject": 0,
            "shortlistedforInterviews": 0,
            "selected": 1,
            "offersReleased": 1,
            "joined": 0,
            "yetToJoin": 0,
            # "decline": 1,
        })

        response = self.client.put(reverse('specific-Requisition', args=[1]), data=data,
                                   content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_RequisitionsAddColumn_get(self):
        """
        This test case is implemented to check if the RequisitionsAddColumn endpoint is working or not.
        :param: None
        :return: None
        """
        response = self.client.get(reverse('add-requisition-column'))
        self.assertEqual(response.status_code, 200)

class TestOfferView(TestCase):
    def test_get_offer_view(self):
        data = {}
        client = Client()
        response = self.client.put(reverse('specific-requisition', args=[1]), data=data,
                                   content_type="application/json")
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_RequisitionsAddColumn_post(self):
        """
        This function is used to test whether the column is added or not.
        :param: None
        :return: None
        """
        postData = json.dumps({
            "columnName": "ResidentialAddress",
            "columnType": "String"
        })
        response = self.client.post(reverse("add-requisition-column"), data=postData, content_type="application/json")
        self.assertEquals(response.status_code, 201)

        postData = json.dumps({
            "columnName": "ResidentialAddress",
            # "columnType": "String"
        })
        response = self.client.post(reverse("add-requisition-column"), data=postData, content_type="application/json")
        self.assertEquals(response.status_code, 400)


class OfferViewTesting(TestCase):
    client = Client()

    @classmethod
    def setUpTestData(cls):
        numberOfCandidates = 4
        for a in range(numberOfCandidates):
            Offer.objects.create(
                businessGroup="2",
                status="Offered",
                sNo=10,
                recruiter="Akanksha Gupta",
                manager="Abby Huvja",
                dateOfOffer="2022-07-04",
                dateOfJoining="2022-07-04",
                rrID=4000,
                hiringManager="Abusl Huvja",
                candidate="Srujan",
                gender="Male",
                phone="8896228554",
                email="srujan2456@gmail.com",
                practices=".net",
                skills=".net",
                offeredDesignation="Software Engineer",
                totalExp=1.2,
                workLocation="Pune",
                source="Job_Portals ",
                subSource="Naukri ",
                name="Srujan",
                offeredGrade="L2 A",
                currentOrg="Automac technology",
                currentCTC=1000000,
                offeredCTC=1000000,
                retentionBonus=100000,
                variableAmount=200000,
                relocation="Hyderabad",
                noticeBuyoutAmount="100000",
                comments="NA",
                riskClassification="NA",
                offersWeek="Week of 21 Mar'22 ",
                joiningWeek="Week of 21 Mar'22 ",
                declineWeek="Week of 21 Mar'22 "
            )
        for a in range(numberOfCandidates):
            Offer.objects.create(
                businessGroup="1",
                status="Offered",
                sNo=10,
                recruiter="Akanksha Gupta",
                manager="Abby Huvja",
                dateOfOffer="2022-07-04",
                dateOfJoining="2022-07-04",
                rrID=4001,
                hiringManager="Abusl Huvja",
                candidate="Naveen",
                gender="Male",
                phone="8896228554",
                email="naveen@gmail.com",
                practices="python",
                skills="python",
                offeredDesignation="Software Engineer",
                totalExp=1.2,
                workLocation="Pune",
                source="Job_Portals ",
                subSource="Naukri ",
                name="Srujan",
                offeredGrade="L2 A",
                currentOrg="Automac technology",
                currentCTC=1000000,
                offeredCTC=1000000,
                retentionBonus=100000,
                variableAmount=200000,
                relocation="Hyderabad",
                noticeBuyoutAmount="100000",
                comments="NA",
                riskClassification="NA",
                offersWeek="Week of 21 Mar'22 ",
                joiningWeek="Week of 21 Mar'22 ",
                declineWeek="Week of 21 Mar'22 "
            )

        listOfPractices = ["Python", "DotNet", "QA", "AIML", "BI"]
        for a in range(len(listOfPractices)):
            Offer.objects.create(
                businessGroup="1",
                status="Offered",
                sNo=10,
                recruiter="Akanksha Gupta",
                manager="Abby Huvja",
                dateOfOffer="2022-07-04",
                dateOfJoining="2022-07-04",
                rrID=4001,
                hiringManager="Abusl Huvja",
                candidate="Naveen",
                gender="Male",
                phone="8896228554",
                email="naveen@gmail.com",
                practices=listOfPractices[a],
                skills="Python",
                offeredDesignation="Software Engineer",
                totalExp=1.2,
                workLocation="Pune",
                source="Job_Portals ",
                subSource="Naukri ",
                name="Srujan",
                offeredGrade="L2 A",
                currentOrg="Automac technology",
                currentCTC=1000000,
                offeredCTC=1000000,
                retentionBonus=100000,
                variableAmount=200000,
                relocation="Hyderabad",
                noticeBuyoutAmount="100000",
                comments="NA",
                riskClassification="NA",
                offersWeek="Week of 21 Mar'22 ",
                joiningWeek="Week of 21 Mar'22 ",
                declineWeek="Week of 21 Mar'22 "
            )

        for a in range(len(listOfPractices)):
            Offer.objects.create(
                businessGroup="1",
                status="Joined",
                sNo=10,
                recruiter="Akanksha Gupta",
                manager="Abby Huvja",
                dateOfOffer="2022-07-04",
                dateOfJoining="2022-07-04",
                rrID=4001,
                hiringManager="Abusl Huvja",
                candidate="Naveen",
                gender="Male",
                phone="8896228554",
                email="naveen@gmail.com",
                practices=listOfPractices[a],
                skills="Python",
                offeredDesignation="Software Engineer",
                totalExp=1.2,
                workLocation="Pune",
                source="Job_Portals ",
                subSource="Naukri ",
                name="Srujan",
                offeredGrade="L2 A",
                currentOrg="Automac technology",
                currentCTC=1000000,
                offeredCTC=1000000,
                retentionBonus=100000,
                variableAmount=200000,
                relocation="Hyderabad",
                noticeBuyoutAmount="100000",
                comments="NA",
                riskClassification="NA",
                offersWeek="Week of 21 Mar'22 ",
                joiningWeek="Week of 21 Mar'22 ",
                declineWeek="Week of 21 Mar'22 "
            )

        for a in range(len(listOfPractices)):
            Offer.objects.create(
                businessGroup="1",
                status="OfferDeclined",
                sNo=10,
                recruiter="Akanksha Gupta",
                manager="Abby Huvja",
                dateOfOffer="2022-07-04",
                dateOfJoining="2022-07-04",
                rrID=4001,
                hiringManager="Abusl Huvja",
                candidate="Naveen",
                gender="Male",
                phone="8896228554",
                email="naveen@gmail.com",
                practices=listOfPractices[a],
                skills="Python",
                offeredDesignation="Software Engineer",
                totalExp=1.2,
                workLocation="Pune",
                source="Job_Portals ",
                subSource="Naukri ",
                name="Srujan",
                offeredGrade="L2 A",
                currentOrg="Automac technology",
                currentCTC=1000000,
                offeredCTC=1000000,
                retentionBonus=100000,
                variableAmount=200000,
                relocation="Hyderabad",
                noticeBuyoutAmount="100000",
                comments="NA",
                riskClassification="NA",
                offersWeek="Week of 21 Mar'22 ",
                joiningWeek="Week of 21 Mar'22 ",
                declineWeek="Week of 21 Mar'22 "
            )

        for a in range(len(listOfPractices)):
            Offer.objects.create(
                businessGroup="1",
                status="OfferAccepted",
                sNo=10,
                recruiter="Akanksha Gupta",
                manager="Abby Huvja",
                dateOfOffer="2022-07-04",
                dateOfJoining="2022-07-04",
                rrID=4001,
                hiringManager="Abusl Huvja",
                candidate="Naveen",
                gender="Male",
                phone="8896228554",
                email="naveen@gmail.com",
                practices=listOfPractices[a],
                skills="Python",
                offeredDesignation="Software Engineer",
                totalExp=1.2,
                workLocation="Pune",
                source="Job_Portals ",
                subSource="Naukri ",
                name="Srujan",
                offeredGrade="L2 A",
                currentOrg="Automac technology",
                currentCTC=1000000,
                offeredCTC=1000000,
                retentionBonus=100000,
                variableAmount=200000,
                relocation="Hyderabad",
                noticeBuyoutAmount="100000",
                comments="NA",
                riskClassification="NA",
                offersWeek="Week of 21 Mar'22 ",
                joiningWeek="Week of 21 Mar'22 ",
                declineWeek="Week of 21 Mar'22 "
            )

    def test_offer_GET(self):
        """
        This function is to check whether the endpoint is working or not.
        Raises an exception if the endpoint doesn't work.

        Params: None
        Returns: None
        """
        response = self.client.get(reverse('WeeklyJoiners'), {"nextorprev": "next", "day": "2022-12-28"})
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('offers'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_correct_or_not(self):
        """
        This function is to check whether the pagination is working or not.

        Params: None
        Returns: None
        """
        response = self.client.get(reverse('offers'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 3)

    def test_are_filters_working(self):
        """
        This function is to check whether the filters are working or not.

        Params: None
        Returns: None
        """
        response = self.client.get(reverse('offers'), {'practices': '.net'})
        self.assertEquals(response.json()['results'][0]['practices'], '.net')
        response_1 = self.client.get(reverse('offers'), {'practices': '.net1'})
        self.assertEquals(response_1.json()['results'], [])

    def test_offer_view_GET_specific_data(self):
        """
        This function is to check whether the endpoint is fetching a specific record or not.

        Params: None
        Returns: None
        """
        response = self.client.get(reverse('offer', args=[1]))
        self.assertEqual(response.status_code, 200)
        response_1 = self.client.get(reverse('offer', args=[1000]))
        self.assertEqual(response_1.status_code, 404)

    def test_create(self):
        """
        This function is to check whether the endpoint is added new record or not.

        Params: None
        Returns: None
        """
        url = reverse("offers")
        payload = json.dumps({
            "businessGroup": "acs",
            "status": "hk",
            "sNo": 1,
            "recruiter": "b",
            "manager": "n",
            "dateOfOffer": "2022-12-16",
            "dateOfJoining": "2022-12-18",
            "rrID": 2,
            "hiringManager": "ghhj",
            "candidate": "hjkj",
            "gender": "male",
            "phone": 7788789077,
            "email": "abc@gmail.com",
            "practices": "django",
            "skills": "python",
            "offeredDesignation": "ase",
            "totalExp": 3.0,
            "offeredGrade": "a+",
            "workLocation": "Hyderabad",
            "currentLocation": "Pune",
            "source": "linkedin",
            "subSource": "na",
            "name": "harsh",
            "offeredGride": 9900,
            "currentOrg": "acs",
            "currentCTC": 450000,
            "offeredCTC": 600000,
            "retentionBonus": 2000,
            "variableAmount": 8909,
            "relocation": "hyd",
            "noticeBuyoutAmount": 789,
            "comments": "na",
            "riskClassification": "na",
            "offersWeek": 1920,
            "joiningWeek": "4th week of july",
            "declineWeek": "na"
        })
        payload_2 = json.dumps({
            "businessGroup": "acs",
            "status": "hk",
            "sNo": 1,
            "recruiter": "b",
            "manager": "n",
            "dateOfOffer": "2022-12-16",
            "dateOfJoining": "2022-12-18",
            "rrID": 2,
            "hiringManager": "ghhj",
            "candidate": "hjkj",
            "gender": "male",
            "phone": 778878977,
            "email": "abc@gmail.com",
            "practices": "django",
            "skills": "python",
            "offeredDesignation": "ase",
            "totalExp": 3.0,
            "offeredGrade": "a+",
            "workLocation": "Hyderabad",
            "currentLocation": "Pune",
            "source": "linkedin",
            "subSource": "na",
            "name": "harsh",
            "offeredGride": 9900,
            "currentOrg": "acs",
            "currentCTC": 450000,
            "offeredCTC": 600000,
            "retentionBonus": 2000,
            "variableAmount": 8909,
            "relocation": "hyd",
            "noticeBuyoutAmount": 789,
            "comments": "na",
            "riskClassification": "na",
            "offersWeek": 1920,
            "joiningWeek": "4th week of july",
            "declineWeek": "na"
        })
        payload_3 = json.dumps({
            "businessGroup": "acs",
            "status": "hk",
            "sNo": 1,
            "recruiter": "b",
            "manager": "n",
            "dateOfOffer": "2022-12-16",
            "dateOfJoining": "2022-12-18",
            "rrID": 2,
            "hiringManager": "ghhj",
            "candidate": "hjkj",
            "gender": "male",
            "phone": 2788789077,
            "email": "abcgmail.com",
            "practices": "django",
            "skills": "python",
            "offeredDesignation": "ase",
            "totalExp": 3.0,
            "offeredGrade": "a+",
            "workLocation": "Hyderabad",
            "currentLocation": "Pune",
            "source": "linkedin",
            "subSource": "na",
            "name": "harsh",
            "offeredGride": 9900,
            "currentOrg": "acs",
            "currentCTC": 450000,
            "offeredCTC": 60000,
            "retentionBonus": 2000,
            "variableAmount": 8909,
            "relocation": "hyd",
            "noticeBuyoutAmount": 789,
            "comments": "na",
            "riskClassification": "na",
            "offersWeek": 1920,
            "joiningWeek": "4th week of july",
            "declineWeek": "na"
        })
        response = self.client.post(url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_1 = self.client.post(url, data=payload_3, content_type="application/json")
        self.assertEqual(response_1.status_code, 400)
        response_2 = self.client.post(url, data=payload_2, content_type="application/json")
        self.assertEqual(response_2.status_code, 400)
        response_3 = self.client.post(url, data=payload_3, content_type="application/json")
        self.assertEqual(response_3.status_code, 400)
        response_4 = self.client.post(url, data=payload_3, content_type="application/json")
        self.assertEqual(response_4.status_code, 400)

    def test_offer_view_PUT_specific_data(self):
        """
        This function is to check whether the endpoint is updating specific record or not.

        Params: None
        Returns: None
        """
        specific_record = json.dumps({
            "businessGroup": "1",
            "status": "Offered",
            "sNo": 1,
            "recruiter": "Akansha Gupta",
            "manager": "Ramanujan",
            "dateOfOffer": "2022-11-23",
            "dateOfJoining": "2022-12-11",
            "rrID": 1000,
            "hiringManager": "Abusl Huvja",
            "candidate": "Saikumar",
            "gender": "Male",
            "phone": "9988776644",
            "email": "saibamini@gmail.com",
            "practices": "JS_Framework",
            "skills": "React.JS",
            "offeredDesignation": "Software Engineer",
            "totalExp": 2.5,
            "offeredGrade": "L2",
            "workLocation": "Hyderabad",
            "currentLocation": "Pune",
            "source": "Job_Portals",
            "subSource": "Naukri",
            "name": "Rehire",
            "offeredGride": "P66-(P66-P74)",
            "currentOrg": "Automac Technology",
            "currentCTC": 1500000,
            "offeredCTC": 1600000,
            "retentionBonus": 100000,
            "variableAmount": 200000,
            "relocation": "Hyderabad",
            "noticeBuyoutAmount": "No",
            "comments": "Better Offer.",
            "riskClassification": "Better Offer.",
            "offersWeek": "Week of 21 Nov'22",
            "joiningWeek": "Week of 21 Dec'22",
            "declineWeek": "Week of 21 Nov'22"
        })
        specific_record_2 = json.dumps({
            "businessGroup": "1",
            "status": "Offered",
            "sNo": 1,
            "recruiter": "Akansha Gupta",
            "manager": "Ramanujan",
            "dateOfOffer": "2022-11-23",
            "dateOfJoining": "2022-12-11",
            "rrID": 1000,
            "hiringManager": "Abusl Huvja",
            "candidate": "Saikumar",
            "gender": "Male",
            "phone": "1988776644",
            "email": "saibaminigmail.com",
            "practices": "JS_Framework",
            "skills": "React.JS",
            "offeredDesignation": "Software Engineer",
            "totalExp": 2.5,
            "offeredGrade": "L2",
            "workLocation": "Hyderabad",
            "currentLocation": "Pune",
            "source": "Job_Portals",
            "subSource": "Naukri",
            "name": "Rehire",
            "offeredGride": "P66-(P66-P74)",
            "currentOrg": "Automac Technology",
            "currentCTC": 1500000,
            "offeredCTC": 160000,
            "retentionBonus": 100000,
            "variableAmount": 200000,
            "relocation": "Hyderabad",
            "noticeBuyoutAmount": "No",
            "comments": "Better Offer.",
            "riskClassification": "Better Offer.",
            "offersWeek": "Week of 21 Nov'22",
            "joiningWeek": "Week of 21 Dec'22",
            "declineWeek": "Week of 21 Nov'22"
        })
        specific_record_3 = json.dumps({
            "businessGroup": "1",
            "status": "Offered",
            "sNo": 1,
            "recruiter": "Akansha Gupta",
            "manager": "Ramanujan",
            "dateOfOffer": "2022-11-23",
            "dateOfJoining": "2022-12-11",
            "rrID": 1000,
            "hiringManager": "Abusl Huvja",
            "candidate": "Saikumar",
            "gender": "Male",
            "phone": "998877664",
            "email": "saibamini@gmail.com",
            "practices": "JS_Framework",
            "skills": "React.JS",
            "offeredDesignation": "Software Engineer",
            "totalExp": 2.5,
            "offeredGrade": "L2",
            "workLocation": "Hyderabad",
            "currentLocation": "Pune",
            "source": "Job_Portals",
            "subSource": "Naukri",
            "name": "Rehire",
            "offeredGride": "P66-(P66-P74)",
            "currentOrg": "Automac Technology",
            "currentCTC": 1500000,
            "offeredCTC": 1600000,
            "retentionBonus": 100000,
            "variableAmount": 200000,
            "relocation": "Hyderabad",
            "noticeBuyoutAmount": "No",
            "comments": "Better Offer.",
            "riskClassification": "Better Offer.",
            "offersWeek": "Week of 21 Nov'22",
            "joiningWeek": "Week of 21 Dec'22",
            "declineWeek": "Week of 21 Nov'22"
        })
        response = self.client.put(reverse('offer', args=[1]), data=specific_record, content_type="application/json")
        self.assertEquals(response.status_code, 202)
        response_2 = self.client.put(reverse('offer', args=[1]), data=specific_record_2,
                                     content_type="application/json")
        self.assertEquals(response_2.status_code, 404)
        response_3 = self.client.put(reverse('offer', args=[1]), data=specific_record_3,
                                     content_type="application/json")
        self.assertEquals(response_3.status_code, 404)
        response_4 = self.client.put(reverse('offer', args=[1]), data=specific_record_2,
                                     content_type="application/json")
        self.assertEquals(response_4.status_code, 404)
        response_5 = self.client.put(reverse('offer', args=[1]), data=specific_record_2,
                                     content_type="application/json")
        self.assertEquals(response_5.status_code, 404)

    def test_offersAddColumn_get(self):
        """
        This funtion is used to test whether the endpoints of the added column are working or not.

        Param: None
        Returns: None



        """
        response = self.client.get(reverse("add-offer-column"))
        self.assertEqual(response.status_code, 200)

    def test_offersAddColumn_post(self):
        """
        This funtion is used to test whether the column is getting added or not.

        Params: None
        Returns: None

        """
        postData = json.dumps({
            "columnName": "ResidentialAddress",
            "columnType": "String"
        })
        response = self.client.post(reverse("add-offer-column"), data=postData, content_type="application/json")
        self.assertEqual(response.status_code, 201)

        postData_2 = json.dumps({
            "columnName": "ResidentialAddress",
        })
        response = self.client.post(reverse("add-offer-column"), data=postData_2, content_type="application/json")
        self.assertEqual(response.status_code, 400)

class TestAuditOffer(TestCase):
    client = Client()

    def test_audit_offer_GET(self):
        """
        This function is to check weather the endpoint is working or not.
        Raises an exception if the endpoint doesn't work.

        Params: None
        Returns: None
        """
        response = self.client.get(reverse('audit_offer'))
        self.assertEqual(response.status_code, 200)
    
    def test_audit_offer_create(self):
        """
        This function is to check weather the endpoint is added new record or not.
        Raises an exception if the endpoint doesn't create record.
        Params: None
        Returns: None
        """
        url = reverse("audit_offer")
        payload = json.dumps({
            "operation_type": "Create",
            "modified_on": "2023-01-10T15:49:16.338899Z",
            "comment": "Offer record with id-1 has been created.",
            "offer_id": 1
        })
        response = self.client.post(url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class TestAuditDailySub(TestCase):
    client = Client()

    def test_audit_dailysub_GET(self):
        """
        This function is to check weather the endpoint is working or not.
        Raises an exception if the endpoint doesn't work.

        Params: None
        Returns: None
        """
        response = self.client.get(reverse('audit_dailysub'))
        self.assertEqual(response.status_code, 200)

    def test_audit_dailysub_create(self):
        """
        This function is to check weather the endpoint is added new record or not.
        Raises an exception if the endpoint doesn't create record.
        Params: None
        Returns: None
        """
        url = reverse("audit_dailysub")
        payload = json.dumps({
            "operation_type": "Create",
            "modified_on": "2023-01-10T15:49:16.338899Z",
            "comment": "DailySub record with id-1 has been created.",
            "dailysub_id": 1
        })
        response = self.client.post(url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class TestAuditRequisition(TestCase):
    client = Client()
    
    def test_audit_requisition_GET(self):
        """
        This function is to check weather the endpoint is working or not.
        Raises an exception if the endpoint doesn't work.

        Args: 
            None
        Returns: 
            None
        """
        response = self.client.get(reverse('audit_requisition'))
        self.assertEqual(response.status_code, 200)

    def test_audit_requisition_create(self):
        """
        This function is to check weather the endpoint is added new record or not.
        Raises an exception if the endpoint doesn't create record.
        Params: None
        Returns: None
        """
        url = reverse("audit_requisition")
        payload = json.dumps({
            "operation_type": "Create",
            "modified_on": "2023-01-10T15:49:16.338899Z",
            "comment": "Requisition record with id-1 has been created.",
            "requisition_id": 1
        })
        response = self.client.post(url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestOverallRequirementsAPIs(test.APITestCase):
    """Test Overall Requirements """

    def test_practice(self):
        """
        This method is used to check the values from the requisition
        practice and will raise exception if it doesn't find them or match
        the correct values.

        Params:none
        Returns:none

        """
        practices = [
            "AIML", "Architect", "Business_Analyst", "Cloud", "DataEngineering",
            "Devops", "Java", "JS_Framework", "Microsoft", "Mobile", "OpenSource", "PM",
            "Python", "QA", "RPM", "Scrum", "Technical_Manager", "UI", "Other"
        ]
        values = []
        url = reverse("overallrequirements")
        for practice in practices:
            response = self.client.get(url, kwargs={"practice": practice})
            values.append(response.status_code == status.HTTP_200_OK)
        self.assertEqual(all(values), True)

    def test_grand_total(self):
        """
        This function is used to test grand total of each record of the practices
        and will raise exception if found some other record.

        Params:none
        Returns:none
        """
        url = reverse("overallrequirements")
        response = self.client.get(url)
        total = {}
        for record in response.data["results"][1:-1]:
            for key in record:
                if key == "total":
                    continue
                if key in total:
                    total[key] += record[key]
                else:
                    total[key] = record[key]
        values = [
            response.data["results"][-1][key] == value for key, value in total.items()
        ]
        self.assertEqual(all(values), True)

    def test_first_row_keys(self):
        """
        This method will check thr first rows values and will raise exception if values
        doesn't match the desired column names.

        Params:none
        Returns:none

        """

        url = reverse("overallrequirements")
        response = self.client.get(url)
        keys = [
            'totalRequirementsRaised', 'approvalAwaited', 'cancelled', 'closed',
            'filled', 'filledInternally', 'onhold', 'open', 'joined', 'decline',
            'yettojoin'
        ]
        values = [key in response.data["results"][0] for key in keys]
        self.assertEqual(all(values), True)

    def test_last_row_values(self):

        """
        This method will check thr last rows values and will raise exception if values
        doesn't match the desired column names.

        Params:none
        Returns:none
        """
        url = reverse("overallrequirements")
        response = self.client.get(url)
        value = response.data["results"][-1]["practice"] == "Grand Total"
        self.assertEqual(value, True)


class Test_WeeklyJoiners(test.APITestCase):
    """Test WeeklyJoinersPracticeReport"""

    def test_next_week_offer(self):
        """
        This function is to check whether the endpoint is working or not.
        Use to check if the next three weeks date are correct
        Raises an exception if the endpoint doesn't work.

        Params: None
        Returns: None
        """
        url = reverse('WeeklyJoiners')
        kwargs = {"nextorprev": "next", "day": "2022-12-28"}
        response = self.client.get(url, kwargs)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_prev_week_offer(self):
        """
        This function is to check whether the endpoint is working or not.
        Use to check if previous three weeks date are correct.
        Raises an exception if the endpoint doesn't work.

        Params: None
        Returns: None
        """
        url = reverse('WeeklyJoiners')
        kwargs = {"nextorprev": "prev", "day": "2022-12-28"}
        response = self.client.get(url, kwargs)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_gone_weekly_status(self):
        """
        This function is to check whether the endpoint is working or not.
        Use to check if the week date is gone or will come.
        Raises an exception if the endpoint doesn't work.

        Params: None
        Returns: None
        """
        url = reverse('WeeklyJoiners')
        kwargs = {"nextorprev": "gone", "day": "2022-12-28"}
        response = self.client.get(url, kwargs)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_next_wrong_day_weekly_status(self):
        """
        This function is to check whether the endpoint is working or not.
        Raises an exception if the endpoint doesn't work
        Use to check if any wrong date is entered.

        Params: None
        Returns: None
        """
        url = reverse('WeeklyJoiners')
        kwargs = {"nextorprev": "next", "day": "2022-12-32"}
        response = self.client.get(url, kwargs)  # 500 Error
        self.assertEquals(response.status_code, 406)

    def test_week_offer_total(self):
        """
        This function is to check whether the endpoint is working or not.
        Use to check the grand total of the three weeks.
        Raises an exception if values are not true.

        Params: None
        Returns: None
        """
        values = []
        url = reverse('WeeklyJoiners')
        kwargs = {"nextorprev": "next", "day": "2022-12-28"}
        response = self.client.get(url, kwargs)
        for record in response.data["results"][1:-1]:
            keys = [k for k in record.keys() if k not in ("practices", "grandTotal")]
            values.append(sum([record[k] for k in keys]) == record["grandTotal"])
        self.assertEqual(all(values), True)



class Test_agewise_requisition(test.APITestCase):
    """ Class which tests JSON response of age wise requisition API"""

    def test(self):
        """ This method is used to check whether Criteria 1 is being fulfilled by filtering Open Keyword
            Params : None
            Return : None"""

        url = reverse("ageing-wise-requisition")
        response = self.client.get(url, kwargs={"status": "open"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_high(self):
        """ This method is used to check whether Criteria 1 is being fulfilled by filtering High Keyword
            Params : None
            Return : None"""

        url = reverse("ageing-wise-requisition")
        response = self.client.get(url, kwargs={"currentWeekPriority": "high"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_medium(self):
        """ This method is used to check whether Criteria 1 is being fulfilled by filtering Medium Keyword
            Params : None
            Return : None """

        url = reverse("ageing-wise-requisition")
        response = self.client.get(url, kwargs={"currentWeekPriority": "medium"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_low(self):
        """ This method is used to check whether Criteria 1 is being fulfilled by filtering Medium Keyword
            Params : None
            Return : None"""

        url = reverse("ageing-wise-requisition")
        response = self.client.get(url, kwargs={"currentWeekPriority": "low"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_total(self):
        """ This method is used to check whether total of high,medium and low matches grand Total
            Param: None
            Return: None"""

        url = reverse("ageing-wise-requisition")
        response = self.client.get(url)
        grand_total = 0
        for result in response.data["result"][1:-1]:
            grand_total += result["total"]
        self.assertEqual(response.data["result"][-1]["grand_total"], grand_total)


class Test_prioritywise_requisition(test.APITestCase):
    """ Class which tests JSON response of priority wise requisition API"""

    def test(self):
        """ This method is used to check whether Criteria 1 is being fulfilled by filtering Open Keyword
            Params : None
            Return : None
        """

        url = reverse("PriorityWiseRequisitionReport")
        response = self.client.get(url, kwargs={"status": "open"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_high(self):
        """ This method is used to check whether Criteria 1 is being fulfilled by filtering High Keyword
            Params : None
            Return : None
        """
        url = reverse("PriorityWiseRequisitionReport")
        response = self.client.get(url, kwargs={"currentWeekPriority": "high"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_medium(self):
        """ This method is used to check whether Criteria 1 is being fulfilled by filtering Medium Keyword
            Params : None
            Return : None
        """
        url = reverse("PriorityWiseRequisitionReport")
        response = self.client.get(url, kwargs={"currentWeekPriority": "medium"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_low(self):
        """ This method is used to check whether Criteria 1 is being fulfilled by filtering low Keyword
            Params : None
            Return : None
        """
        url = reverse("PriorityWiseRequisitionReport")
        response = self.client.get(url, kwargs={"currentWeekPriority": "low"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestAuditOffer(TestCase):
    client = Client()

    def test_audit_offer_GET(self):
        """
        This function is to check weather the endpoint is working or not.
        Raises an exception if the endpoint doesn't work.

        Params: None
        Returns: None
        """
        response = self.client.get(reverse('audit_offer'))
        self.assertEqual(response.status_code, 200)

    def test_audit_offer_create(self):
        """
        This function is to check weather the endpoint is added new record or not.
        Raises an exception if the endpoint doesn't create record.
        Params: None
        Returns: None
        """
        url = reverse("audit_offer")
        payload = json.dumps({
            "operation_type": "Create",
            "modified_on": "2023-01-10T15:49:16.338899Z",
            "comment": "Offer record with id-1 has been created.",
            "offer_id": 1
        })
        response = self.client.post(url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestAuditDailySub(TestCase):
    client = Client()

    def test_audit_dailysub_GET(self):
        """
        This function is to check weather the endpoint is working or not.
        Raises an exception if the endpoint doesn't work.

        Params: None
        Returns: None
        """
        response = self.client.get(reverse('audit_dailysub'))
        self.assertEqual(response.status_code, 200)

    def test_audit_dailysub_create(self):
        """
        This function is to check weather the endpoint is added new record or not.
        Raises an exception if the endpoint doesn't create record.
        Params: None
        Returns: None
        """
        url = reverse("audit_dailysub")
        payload = json.dumps({
            "operation_type": "Create",
            "modified_on": "2023-01-10T15:49:16.338899Z",
            "comment": "DailySub record with id-1 has been created.",
            "dailysub_id": 1
        })
        response = self.client.post(url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestAuditRequisition(TestCase):
    client = Client()

    def test_audit_requisition_GET(self):
        """
        This function is to check weather the endpoint is working or not.
        Raises an exception if the endpoint doesn't work.

        Args:
            None
        Returns:
            None
        """
        response = self.client.get(reverse('audit_requisition'))
        self.assertEqual(response.status_code, 200)

    def test_audit_requisition_create(self):
        """
        This function is to check weather the endpoint is added new record or not.
        Raises an exception if the endpoint doesn't create record.
        Params: None
        Returns: None
        """
        url = reverse("audit_requisition")
        payload = json.dumps({
            "operation_type": "Create",
            "modified_on": "2023-01-10T15:49:16.338899Z",
            "comment": "Requisition record with id-1 has been created.",
            "requisition_id": 1
        })
        response = self.client.post(url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestInterviewSelect(TestCase):
    """
     Test L1L2 Interview select report
    """
    client=Client()

    @classmethod
    def setUpTestData(cls):


        listOfPractices=["microsoft",".Net","java","aws"]
        for a in range(len(listOfPractices)):
            DailySub.objects.create(
                businessGroup=1,
                sourceDate='2022-07-01',
                sourcer='abc',
                recruiter='Feroz',
                manager='Sruesh',
                rrID=3632,
                jobLocation='Hyderabad',
                practice=listOfPractices[a],
                skill='Django',
                source='SocialMedia',
                source2='Naukri',
                fullName='abc',
                candidateName='Kishore',
                emailID='kishore@gmail.com',
                contactNo=9000270001,
                currentLocation='Hyderbad',
                experienceIn='2.0',
                currentOrg='TCS',
                currentCTC='6.0',
                expectedCTC='10',
                noticePeriod='16',
                l1InterviewDate='2022-07-04',
                l1Interviewer='Hari Varma',
                l2InterviewDate='2022-07-08',
                l2Interviewer='shaik Feroz',
                l3InterviewDate='2022-07-15',
                l3Interviewer='Suresh Kumar',
                status='Offered',
                feedback='Good Technical knowledge',
                dateOfOffer='2022-07-27',
                dateOfJoining='2022-08-22',
                dateOfDecline='2022-07-14',
                declineReasons='abc',
                week='Week of 27 June 2022',
                recordingLinkL1='abc',
                recordingLinkL2='abc',
                remarks='abc'
            )

    def test_DailySub_view_GET_InterviewSelect_Calculation_data(self):
        """
        This function is used to test whether the endpoints of an l1l2 report is working or not.
        Params: None
        Returns: None
        """
        response = self.client.get(reverse('l1l2'),{"date":"2022-07-01"})
        response_1 = self.client.get(reverse('l1l2'),{"date":"2022-12-05"})
        response_2 = self.client.get(reverse('l1l2'))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response_1.status_code, 200)
        self.assertEquals(response_2.status_code, 200)

class TestOfferstatussummaryview(TestCase):
    """
        Test offer status summary report
    """
    client = Client()

    def test_offer_status_summary_get(self):
        """
        This function is used to test whether the endpoints of an offer status summary report is working or not.
        Params: None
        Returns: None
        """
        response = self.client.get(reverse('OfferStatusSummary'),{"year":"2022"})
        response_1 = self.client.get(reverse('OfferStatusSummary'),{"year":"2023"})
        response_2 = self.client.get(reverse('OfferStatusSummary'))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response_1.status_code, 200)
        self.assertEquals(response_2.status_code, 404)

    def test_MonthWiseOffersStatus_get(self):
        """
        This function is used to test whether the endpoints of an monthly wise offer status summary report is working or not.
        Params: None
        Returns: None
        """
        response = self.client.get(reverse('Month-wise-offer-status'),{"year":"2022"})
        response_1 = self.client.get(reverse('Month-wise-offer-status'),{"year":"2023"})
        response_2 = self.client.get(reverse('Month-wise-offer-status'))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response_1.status_code, 200)
        self.assertEquals(response_2.status_code, 404)