from rest_framework import serializers
from .models import DailySub, Requisition, Offer, AuditOffer, AuditDailySub, AuditRequisition, MasterTable, GroupMaster, Downloads
from rest_framework.serializers import ValidationError
from django.core.validators import validate_email
import re


# DailySub serializer

class DailySubSerializer(serializers.ModelSerializer):
    businessGroup = serializers.CharField(max_length=255)
    sourceDate = serializers.DateField()
    sourcer = serializers.CharField(max_length=255)
    recruiter = serializers.CharField(max_length=100)
    manager = serializers.CharField(max_length=100)
    rrID = serializers.IntegerField()
    jobLocation = serializers.CharField(max_length=255)
    practice = serializers.CharField(max_length=200)
    skill = serializers.CharField(max_length=200)
    source = serializers.CharField(max_length=200)
    source2 = serializers.CharField(max_length=200)
    fullName = serializers.CharField(max_length=200)
    candidateName = serializers.CharField(max_length=200)
    emailID = serializers.CharField(max_length=200)
    contactNo = serializers.CharField(max_length=12)
    currentLocation = serializers.CharField(max_length=100)
    experienceIn = serializers.FloatField()
    currentOrg = serializers.CharField(max_length=100)
    currentCTC = serializers.FloatField()
    expectedCTC = serializers.FloatField()
    noticePeriod = serializers.IntegerField()
    l1InterviewDate = serializers.DateField()
    l1Interviewer = serializers.CharField(max_length=100)
    l2InterviewDate = serializers.DateField()
    l2Interviewer = serializers.CharField(max_length=100)
    l3InterviewDate = serializers.DateField()
    l3Interviewer = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=20)
    feedback = serializers.CharField(max_length=255)
    dateOfOffer = serializers.DateField()
    dateOfJoining = serializers.DateField()
    dateOfDecline = serializers.DateField()
    declineReasons = serializers.CharField(max_length=255)
    week = serializers.CharField(max_length=20)
    remarks = serializers.CharField(max_length=255)
    recordingLinkL1 = serializers.CharField(max_length=255)
    recordingLinkL2 = serializers.CharField(max_length=255)

    def validate_contactNo(self, data):
        """
            validation function for a phone field
            :param data:
            :return: returns data if validation is success, else raises ValidationError.
            """
        regexPattern = re.compile(
            "(91)?[6-9][0-9]{9}")  # phone number regular expression pattern.
        if not regexPattern.match(data):
            raise ValidationError("Invalid phone number entered")
        elif data[0] * len(data) == data:
            raise ValidationError("Invalid phone number entered")
        else:
            return data

    def validate(self, data):
        """
        object validation function for a expectedCTC vs currentCTC
        :param data:
        :return: returns data if validation is success, else raises ValidationError.
        """
        expectedCTC = data['expectedCTC']
        currentCTC = data['currentCTC']
        if expectedCTC > currentCTC:
            return data
        else:
            raise ValidationError(
                "Invalid CTC value for expected CTC or current CTC is entered, please check")

    def validate_emailID(self, data):
        """
        field validation function for a email field
        :param data:
        :return: returns data if validation is success, else raises ValidationError.
        """
        if not validate_email(data):
            return data
        else:
            raise ValidationError("Entered invalid email.")

    def create(self, validated_data):
        return DailySub.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.businessGroup = validated_data.get('businessGroup', instance.businessGroup)
        instance.sourceDate = validated_data.get('sourceDate', instance.sourceDate)
        instance.sourcer = validated_data.get('sourcer', instance.sourcer)
        instance.recruiter = validated_data.get('recruiter', instance.recruiter)
        instance.manager = validated_data.get('manager', instance.manager)
        instance.rrID = validated_data.get('rrID', instance.rrID)
        instance.jobLocation = validated_data.get('jobLocation', instance.jobLocation)
        instance.practice = validated_data.get('practice', instance.practice)
        instance.skill = validated_data.get('skill', instance.skill)
        instance.source = validated_data.get('source', instance.source)
        instance.source2 = validated_data.get('source2', instance.source2)
        instance.fullName = validated_data.get('fullName', instance.fullName)
        instance.candidateName = validated_data.get('candidateName', instance.candidateName)
        instance.emailID = validated_data.get('emailID', instance.emailID)
        instance.contactNo = validated_data.get('contactNo', instance.contactNo)
        instance.currentLocation = validated_data.get('currentLocation', instance.currentLocation)
        instance.experienceIn = validated_data.get('experienceIn', instance.experienceIn)
        instance.currentOrg = validated_data.get('currentOrg', instance.currentOrg)
        instance.currentCTC = validated_data.get('currentCTC', instance.currentCTC)
        instance.expectedCTC = validated_data.get('expectedCTC', instance.expectedCTC)
        instance.noticePeriod = validated_data.get('noticePeriod', instance.noticePeriod)
        instance.l1InterviewDate = validated_data.get('l1InterviewDate', instance.l1InterviewDate)
        instance.l1Interviewer = validated_data.get('l1Interviewer', instance.l1Interviewer)
        instance.l2InterviewDate = validated_data.get('l2InterviewDate', instance.l2InterviewDate)
        instance.l2Interviewer = validated_data.get('l2Interviewer', instance.l2Interviewer)
        instance.l3InterviewDate = validated_data.get(' l3InterviewDate', instance.l3InterviewDate)
        instance.l3Interviewer = validated_data.get('l3Interviewer', instance.l3Interviewer)
        instance.status = validated_data.get('status', instance.status)
        instance.feedback = validated_data.get('feedback', instance.feedback)
        instance.dateOfOffer = validated_data.get('dateOfOffer', instance.dateOfOffer)
        instance.dateOfJoining = validated_data.get('dateOfJoining', instance.dateOfJoining)
        instance.dateOfDecline = validated_data.get('dateOfDecline', instance.dateOfDecline)
        instance.declineReasons = validated_data.get('declineReasons', instance.declineReasons)
        instance.week = validated_data.get('week', instance.week)
        instance.recordingLinkL1 = validated_data.get('recordingLinkL1', instance.recordingLinkL1)
        instance.recordingLinkL2 = validated_data.get('recordingLinkL2', instance.recordingLinkL2)
        instance.remarks = validated_data.get('remarks', instance.remarks)
        instance.column_1 = validated_data.get("column_1", instance.column_1)
        instance.column_2 = validated_data.get("column_2", instance.column_2)
        instance.column_3 = validated_data.get("column_3", instance.column_3)
        instance.column_4 = validated_data.get("column_4", instance.column_4)
        instance.column_5 = validated_data.get("column_5", instance.column_5)
        instance.column_6 = validated_data.get("column_6", instance.column_6)
        instance.column_7 = validated_data.get("column_7", instance.column_7)
        instance.column_8 = validated_data.get("column_8", instance.column_8)
        instance.column_9 = validated_data.get("column_9", instance.column_9)
        instance.column_10 = validated_data.get("column_10", instance.column_10)

        instance.save()
        return instance

    class Meta:
        model = DailySub
        fields = ['id', 'businessGroup', 'sourceDate', 'sourcer', 'recruiter', 'manager', 'rrID', 'jobLocation',
                  'practice', 'skill', 'source', 'source2', 'fullName', 'candidateName', 'emailID', 'contactNo',
                  'currentLocation', 'experienceIn', 'currentOrg', 'currentCTC', 'expectedCTC', 'noticePeriod',
                  'l1InterviewDate', 'l1Interviewer', 'l2InterviewDate', 'l2Interviewer', 'l3InterviewDate',
                  'l3Interviewer', 'status', 'feedback', 'dateOfOffer', 'dateOfJoining', 'declineReasons',
                  'dateOfDecline', 'week', 'recordingLinkL1', 'recordingLinkL2', 'remarks']

    def __init__(self, *args, **kwargs):
        self._fields_to_add = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

    def get_field_names(self, *args, **kwargs):
        originalFields = super().get_field_names(*args, **kwargs)
        if self._fields_to_add:
            return tuple(list(originalFields) + list(self._fields_to_add))
        return originalFields

class OfferSerialize(serializers.ModelSerializer):
    businessGroup = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=20)
    sNo = serializers.IntegerField()
    recruiter = serializers.CharField(max_length=100)
    manager = serializers.CharField(max_length=100)
    dateOfOffer = serializers.DateField()
    dateOfJoining = serializers.DateField()
    rrID = serializers.IntegerField()
    hiringManager = serializers.CharField(max_length=100)
    candidate = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=12)
    currentCTC = serializers.IntegerField()
    offeredCTC = serializers.IntegerField()
    practices = serializers.CharField(max_length=100)
    skills = serializers.CharField(max_length=100)
    offeredDesignation = serializers.CharField(max_length=100)
    totalExp = serializers.FloatField()
    offeredGrade = serializers.CharField(max_length=100)
    workLocation = serializers.CharField(max_length=100)
    currentLocation = serializers.CharField(max_length=100)
    source = serializers.CharField(max_length=100)
    subSource = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    offeredGride = serializers.CharField(max_length=100)
    currentOrg = serializers.CharField(max_length=100)
    retentionBonus = serializers.IntegerField()
    variableAmount = serializers.IntegerField()
    relocation = serializers.CharField(max_length=100)
    noticeBuyoutAmount = serializers.CharField(max_length=100)
    comments = serializers.CharField(max_length=255)
    riskClassification = serializers.CharField(max_length=255)
    offersWeek = serializers.CharField(max_length=50)
    joiningWeek = serializers.CharField(max_length=50)
    declineWeek = serializers.CharField(max_length=50)

    def validate_phone(self, data):
        """
        validation function for a phone field
        :param data: phone number to be validated.
        :return: returns data if validation is success, else raises ValidationError.
        """

        regexPattern = re.compile("(91)?[6-9][0-9]{9}")  # phone number regular expression pattern.

        if not regexPattern.match(data):
            raise ValidationError("Invalid phone number entered")
        elif data[0] * len(data) == data:
            raise ValidationError("Invalid phone number entered")
        else:
            return data

    def validate_email(self, data):
        """
        field validation function for a email field.
        :param data: email id to be validated.
        :return: returns data if validation is success, else raises ValidationError.
        """

        if not validate_email(data):
            return data
        else:
            raise ValidationError("Entered invalid email.")

    def validate(self, data):
        """
        object validation function for a offeredCTC vs currentCTC.
        :param data: validate if offeredCTC >= currentCTC.
        :return: returns data if validation is success, else raises ValidationError.
        """

        offeredCTC = data['offeredCTC']
        currentCTC = data['currentCTC']
        if offeredCTC >= currentCTC:
            return data
        else:
            raise ValidationError({"offeredCTC_VS_currentCTC":
                                       "Invalid CTC value for offered CTC or current CTC is entered, please check"})

    def create(self, validated_data):
        return Offer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.businessGroup = validated_data.get('businessGroup', instance.businessGroup)
        instance.status = validated_data.get('status', instance.status)
        instance.sNo = validated_data.get('sNo', instance.sNo)
        instance.recruiter = validated_data.get('recruiter', instance.recruiter)
        instance.manager = validated_data.get('manager', instance.manager)
        instance.dateOfOffer = validated_data.get('dateOfOffer', instance.dateOfOffer)
        instance.dateOfJoining = validated_data.get('dateOfJoining', instance.dateOfJoining)
        instance.rrID = validated_data.get('rrID', instance.rrID)
        instance.hiringManager = validated_data.get('hiringManager', instance.hiringManager)
        instance.candidate = validated_data.get('candidate', instance.candidate)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.currentCTC = validated_data.get('currentCTC', instance.currentCTC)
        instance.offeredCTC = validated_data.get('offeredCTC', instance.offeredCTC)
        instance.practices = validated_data.get('practices', instance.practices)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.offeredDesignation = validated_data.get('offeredDesignation', instance.offeredDesignation)
        instance.totalExp = validated_data.get('totalExp', instance.totalExp)
        instance.offeredGrade = validated_data.get('offeredGrade', instance.offeredGrade)
        instance.workLocation = validated_data.get('workLocation', instance.workLocation)
        instance.currentLocation = validated_data.get('currentLocation', instance.currentLocation)
        instance.source = validated_data.get('source', instance.source)
        instance.subSource = validated_data.get('subSource', instance.subSource)
        instance.name = validated_data.get('name', instance.name)
        instance.offeredGride = validated_data.get('offeredGride', instance.offeredGride)
        instance.currentOrg = validated_data.get('currentOrg', instance.currentOrg)
        instance.retentionBonus = validated_data.get('retentionBonus', instance.retentionBonus)
        instance.variableAmount = validated_data.get('variableAmount', instance.variableAmount)
        instance.relocation = validated_data.get('relocation', instance.relocation)
        instance.noticeBuyoutAmount = validated_data.get('noticeBuyoutAmount', instance.noticeBuyoutAmount)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.riskClassification = validated_data.get('riskClassification', instance.riskClassification)
        instance.offersWeek = validated_data.get('offersWeek', instance.offersWeek)
        instance.joiningWeek = validated_data.get('joiningWeek', instance.joiningWeek)
        instance.declineWeek = validated_data.get('declineWeek', instance.declineWeek)
        instance.column_1 = validated_data.get("column_1", instance.column_1)
        instance.column_2 = validated_data.get("column_2", instance.column_2)
        instance.column_3 = validated_data.get("column_3", instance.column_3)
        instance.column_4 = validated_data.get("column_4", instance.column_4)
        instance.column_5 = validated_data.get("column_5", instance.column_5)
        instance.column_6 = validated_data.get("column_6", instance.column_6)
        instance.column_7 = validated_data.get("column_7", instance.column_7)
        instance.column_8 = validated_data.get("column_8", instance.column_8)
        instance.column_9 = validated_data.get("column_9", instance.column_9)
        instance.column_10 = validated_data.get("column_10", instance.column_10)
        instance.save()

        return instance

    class Meta:
        model = Offer
        fields = ('id', 'businessGroup', 'status', 'sNo', 'recruiter', 'manager', 'dateOfOffer',
                  'dateOfJoining', 'rrID', 'hiringManager', 'candidate', 'gender', 'phone',
                  'email', 'practices', 'skills', 'offeredDesignation', 'totalExp', 'offeredGrade',
                  'workLocation', 'currentLocation', 'source', 'subSource', 'name', 'offeredGride',
                  'currentOrg', 'currentCTC', 'offeredCTC', 'retentionBonus', 'variableAmount',
                  'relocation', 'noticeBuyoutAmount', 'comments', 'riskClassification', 'offersWeek',
                  'joiningWeek', 'declineWeek')

    def __init__(self, *args, **kwargs):
        self._fields_to_add = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

    def get_field_names(self, *args, **kwargs):
        originalFields = super().get_field_names(*args, **kwargs)
        if self._fields_to_add:
            return tuple(list(originalFields) + list(self._fields_to_add))
        return originalFields

class RequisitionSerializer(serializers.ModelSerializer):
    skill = serializers.CharField(max_length=255)
    superClass = serializers.CharField(max_length=255)
    jobFamily = serializers.CharField(max_length=255)
    yearOfExp = serializers.CharField(max_length=255)
    grade = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=100)
    currentWeekPriority = serializers.CharField(max_length=255)
    hiringManager = serializers.CharField(max_length=255)
    hod = serializers.CharField(max_length=255)
    projectClient = serializers.CharField(max_length=255)
    rrID = serializers.IntegerField()
    practice = serializers.CharField(max_length=255)
    allocatedResource = serializers.CharField(max_length=255)
    PMOStatus = serializers.CharField(max_length=255)
    recruiter = serializers.CharField(max_length=255)
    permSubconContract = serializers.CharField(max_length=255)
    requisitionRaiseDate = serializers.DateField()
    requirement = serializers.IntegerField()
    profilesShared = serializers.IntegerField()
    screenReject = serializers.IntegerField()
    shortlistedforInterviews = serializers.IntegerField()
    selected = serializers.IntegerField()
    offersReleased = serializers.IntegerField()
    joined = serializers.IntegerField()
    yetToJoin = serializers.IntegerField()
    decline = serializers.IntegerField()

    class Meta:
        model = Requisition
        fields = ['id', 'skill', 'superClass', 'jobFamily', 'yearOfExp', 'grade', 'status', 'currentWeekPriority',
                  'hiringManager',
                  'hod', 'projectClient', 'rrID', 'practice', 'allocatedResource', 'PMOStatus', 'recruiter',
                  'permSubconContract',
                  'requisitionRaiseDate', 'requirement', 'profilesShared', 'screenReject', 'shortlistedforInterviews',
                  'selected',
                  'offersReleased', 'joined', 'yetToJoin', 'decline', 'tat', 'openAsOnDate', 'days']

    def __init__(self, *args, **kwargs):
        self._fields_to_add = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

    def get_field_names(self, *args, **kwargs):
        originalFields = super().get_field_names(*args, **kwargs)
        if self._fields_to_add:
            return tuple(list(originalFields) + list(self._fields_to_add))
        return originalFields

    def create(self, validated_data):
        """
        Args:
            validated_data (_type_): _description_

        Returns:
            _type_: _description_
        """
        return Requisition.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """

        Args:
            instance
            validated_data 

        Returns:
            
        """
        instance.skill = validated_data.get('skill', instance.skill)
        instance.superClass = validated_data.get('superClass', instance.superClass)
        instance.jobFamily = validated_data.get('jobfamily', instance.jobFamily)
        instance.yearOfExp = validated_data.get('yearOfExp', instance.yearOfExp)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.status = validated_data.get('status', instance.status)
        instance.currentWeekPriority = validated_data.get('currentWeekPriority', instance.currentWeekPriority)
        instance.hiringManager = validated_data.get('hiringManager', instance.hiringManager)
        instance.hod = validated_data.get('hod', instance.hod)
        instance.projectClient = validated_data.get('projectClient', instance.projectClient)
        instance.rrID = validated_data.get('rrID', instance.rrID)
        instance.practice = validated_data.get('practice', instance.practice)
        instance.allocatedResource = validated_data.get('allocatedResource', instance.allocatedResource)
        instance.PMOStatus = validated_data.get('PMOStatus', instance.PMOStatus)
        instance.recruiter = validated_data.get('recruiter', instance.recruiter)
        instance.permSubconContract = validated_data.get('permSubconContract', instance.permSubconContract)
        instance.requisitionRaiseDate = validated_data.get('requisitionRaiseDate', instance.requisitionRaiseDate)
        instance.requirement = validated_data.get('requirement', instance.requirement)
        instance.profilesShared = validated_data.get('profilesShared', instance.profilesShared)
        instance.screenReject = validated_data.get('screenReject', instance.screenReject)
        instance.shortlistedforInterviews = validated_data.get('shortlistedforInterviews',
                                                               instance.shortlistedforInterviews)
        instance.selected = validated_data.get('selected', instance.selected)
        instance.offersReleased = validated_data.get('offersReleased', instance.offersReleased)
        instance.joined = validated_data.get('joined', instance.joined)
        instance.yetToJoin = validated_data.get('yetToJoin', instance.yetToJoin)
        instance.decline = validated_data.get('decline', instance.decline)
        instance.column_1 = validated_data.get("column_1", instance.column_1)
        instance.column_2 = validated_data.get("column_2", instance.column_2)
        instance.column_3 = validated_data.get("column_3", instance.column_3)
        instance.column_4 = validated_data.get("column_4", instance.column_4)
        instance.column_5 = validated_data.get("column_5", instance.column_5)
        instance.column_6 = validated_data.get("column_6", instance.column_6)
        instance.column_7 = validated_data.get("column_7", instance.column_7)
        instance.column_8 = validated_data.get("column_8", instance.column_8)
        instance.column_9 = validated_data.get("column_9", instance.column_9)
        instance.column_10 = validated_data.get("column_10", instance.column_10)
        instance.save()

        return instance

class AuditOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditOffer
        fields = "__all__"

class AuditDailySubSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditDailySub
        fields = "__all__"

class AuditRequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditRequisition
        fields = "__all__"

class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downloads
        fields = "__all__"

class OfferAddColumnSerializer(serializers.ModelSerializer):
    columnName = serializers.CharField(max_length=100)
    columnType = serializers.CharField(max_length=100)

    tableName = "Offer"
    columnNames = MasterTable.objects.values("columnName").filter(tableName=tableName)
    columnNameList = [name["columnName"] for name in columnNames]
    columns = [f.name for f in Offer._meta.get_fields()][37:]

    def validate_columnName(self, data):
        if data in self.columnNameList:
            raise ValidationError(f"Column {data} already exists")
        else:
            return data

    def create(self, validated_data):
        fields = MasterTable.objects.values("columnField").filter(tableName=self.tableName)
        fieldList = [field["columnField"] for field in fields]
        for column in self.columns:
            if column not in fieldList:
                return MasterTable.objects.create(tableName=self.tableName, columnField=column, **validated_data)
        return MasterTable.objects.create(tableName=self.tableName, columnField="column_1", **validated_data)

    class Meta:
        model = MasterTable
        fields = ['id', 'columnName', 'columnType']

class RequisitionAddColumnSerializer(serializers.ModelSerializer):
    columnName = serializers.CharField(max_length=100)
    columnType = serializers.CharField(max_length=100)

    tableName = "Requisition"
    columnNames = MasterTable.objects.values("columnName").filter(tableName=tableName)
    columnNameList = [name["columnName"] for name in columnNames]
    columns = [f.name for f in Requisition._meta.get_fields()][27:]

    def validate_columnName(self, data):
        if data in self.columnNameList:
            raise ValidationError(f"Column {data} already exists")
        else:
            return data

    def create(self, validated_data):
        fields = MasterTable.objects.values("columnField").filter(tableName=self.tableName)
        fieldList = [field["columnField"] for field in fields]
        for column in self.columns:
            if column not in fieldList:
                return MasterTable.objects.create(tableName=self.tableName, columnField=column, **validated_data)
        return MasterTable.objects.create(tableName=self.tableName, columnField="column_1", **validated_data)

    class Meta:
        model = MasterTable
        fields = ['id', 'columnName', 'columnType']

class DailySubAddColumnSerializer(serializers.ModelSerializer):
    columnName = serializers.CharField(max_length=100)
    columnType = serializers.CharField(max_length=100)

    tableName = "DailySub"
    columnNames = MasterTable.objects.values("columnName").filter(tableName=tableName)
    columnNameList = [name["columnName"] for name in columnNames]
    columns = [f.name for f in DailySub._meta.get_fields()][38:]

    def validate_columnName(self, data):
        if data in self.columnNameList:
            raise ValidationError(f"Column {data} already exists")
        else:
            return data

    def create(self, validated_data):
        fields = MasterTable.objects.values("columnField").filter(tableName=self.tableName)
        fieldList = [field["columnField"] for field in fields]
        for column in self.columns:
            if column not in fieldList:
                return MasterTable.objects.create(tableName=self.tableName, columnField=column, **validated_data)
        return MasterTable.objects.create(tableName=self.tableName, columnField="column_1", **validated_data)

    class Meta:
        model = MasterTable
        fields = ['id', 'columnName', 'columnType']

class GroupMasterSerializer(serializers.ModelSerializer):
    """Group Master Serializer"""

    class Meta:
        model = GroupMaster
        fields = ["id","name", "value", "group"]

