import datetime
from datetime import  date
from django.db import models


class GroupMaster(models.Model):
    group = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Requisition(models.Model):
    """
    This class contains all requisitions details
    """
    skill = models.CharField(max_length=255)
    superClass = models.CharField(max_length=255)
    jobFamily = models.CharField(max_length=255)
    yearOfExp = models.CharField(max_length=255)
    grade = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    currentWeekPriority = models.CharField(max_length=255)
    hiringManager = models.CharField(max_length=255)
    hod = models.CharField(max_length=255)
    projectClient = models.CharField(max_length=255)
    rrID = models.IntegerField()
    practice = models.CharField(max_length=255)
    allocatedResource = models.CharField(max_length=255)
    PMOStatus = models.CharField(max_length=255)
    recruiter = models.CharField(max_length=255)
    permSubconContract = models.CharField(max_length=255)
    requisitionRaiseDate = models.DateField()
    requirement = models.IntegerField()
    profilesShared = models.IntegerField()
    screenReject = models.IntegerField()
    shortlistedforInterviews = models.IntegerField()
    selected = models.IntegerField()
    offersReleased = models.IntegerField()
    joined = models.IntegerField()
    yetToJoin = models.IntegerField()
    decline = models.IntegerField()
    column_1 = models.CharField(max_length=255, default='')
    column_2 = models.CharField(max_length=255, default='')
    column_3 = models.CharField(max_length=255, default='')
    column_4 = models.CharField(max_length=255, default='')
    column_5 = models.CharField(max_length=255, default='')
    column_6 = models.CharField(max_length=255, default='')
    column_7 = models.CharField(max_length=255, default='')
    column_8 = models.CharField(max_length=255, default='')
    column_9 = models.CharField(max_length=255, default='')
    column_10 = models.CharField(max_length=255, default='')

    @property
    def tat(self):
        if self.requisitionRaiseDate <= date.today():
            return (date.today() - self.requisitionRaiseDate).days

    @property
    def openAsOnDate(self):
        if self.requirement and self.joined:
            return self.requirement - self.joined

    @property
    def days(self):
        days = ''
        tat = (datetime.date.today() - self.requisitionRaiseDate).days
        if 0 <= tat <= 30:
            days = "0-30 Days"
        elif 30 < tat <= 60:
            days = "31-60 Days"
        elif 60 < tat <= 90:
            days = "61-90 Days"
        else:
            days = "90+ Days"
        return days


class DailySub(models.Model):
    """
    This class contains all interviews details
    """
    businessGroup = models.CharField(max_length=255)
    sourceDate = models.DateField()
    sourcer = models.CharField(max_length=255)
    recruiter = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    rrID = models.IntegerField()
    jobLocation = models.CharField(max_length=255)
    practice = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    source2 = models.CharField(max_length=200)
    fullName = models.CharField(max_length=200)
    candidateName = models.CharField(max_length=200)
    emailID = models.CharField(max_length=200)
    contactNo = models.CharField(max_length=12)
    currentLocation = models.CharField(max_length=100)
    experienceIn = models.FloatField()
    currentOrg = models.CharField(max_length=100)
    currentCTC = models.FloatField()
    expectedCTC = models.FloatField()
    noticePeriod = models.IntegerField()
    l1InterviewDate = models.DateField()
    l1Interviewer = models.CharField(max_length=100)
    l2InterviewDate = models.DateField()
    l2Interviewer = models.CharField(max_length=100)
    l3InterviewDate = models.DateField()
    l3Interviewer = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    feedback = models.TextField()
    dateOfOffer = models.DateField()
    dateOfJoining = models.DateField(null=True,blank=True)
    dateOfDecline = models.DateField(null=True,blank=True)
    declineReasons = models.TextField()
    week = models.CharField(max_length=20)
    recordingLinkL1 = models.CharField(max_length=255)
    recordingLinkL2 = models.CharField(max_length=255)
    remarks = models.TextField()
    column_1 = models.CharField(max_length=255, default='')
    column_2 = models.CharField(max_length=255, default='')
    column_3 = models.CharField(max_length=255, default='')
    column_4 = models.CharField(max_length=255, default='')
    column_5 = models.CharField(max_length=255, default='')
    column_6 = models.CharField(max_length=255, default='')
    column_7 = models.CharField(max_length=255, default='')
    column_8 = models.CharField(max_length=255, default='')
    column_9 = models.CharField(max_length=255, default='')
    column_10 = models.CharField(max_length=255, default='')

class Offer(models.Model):
    """
    This class contains all offer details
    """
    businessGroup = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    sNo = models.IntegerField()
    recruiter = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    dateOfOffer = models.DateField()
    dateOfJoining = models.DateField()
    rrID = models.IntegerField()
    hiringManager = models.CharField(max_length=100)
    candidate = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    practices = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    offeredDesignation = models.CharField(max_length=100)
    totalExp = models.FloatField()
    offeredGrade = models.CharField(max_length=100)
    workLocation = models.CharField(max_length=100)
    currentLocation = models.CharField(max_length=100, default='')
    source = models.CharField(max_length=100)
    subSource = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    offeredGride = models.CharField(max_length=100, default='')
    currentOrg = models.CharField(max_length=100)
    currentCTC = models.IntegerField()
    offeredCTC = models.IntegerField()
    retentionBonus = models.IntegerField()
    variableAmount = models.IntegerField()
    relocation = models.CharField(max_length=100)
    noticeBuyoutAmount = models.CharField(max_length=100)
    comments = models.TextField()
    riskClassification = models.CharField(max_length=255)
    offersWeek = models.CharField(max_length=50)
    joiningWeek = models.CharField(max_length=50)
    declineWeek = models.CharField(max_length=50)
    column_1 = models.CharField(max_length=255, default='')
    column_2 = models.CharField(max_length=255, default='')
    column_3 = models.CharField(max_length=255, default='')
    column_4 = models.CharField(max_length=255, default='')
    column_5 = models.CharField(max_length=255, default='')
    column_6 = models.CharField(max_length=255, default='')
    column_7 = models.CharField(max_length=255, default='')
    column_8 = models.CharField(max_length=255, default='')
    column_9 = models.CharField(max_length=255, default='')
    column_10 = models.CharField(max_length=255, default='')


# class DynamicColumns(models.Model):
class MasterTable(models.Model):
    columnName = models.CharField(max_length=100)
    tableName = models.CharField(max_length=100)
    columnField = models.CharField(max_length=100)
    columnType = models.CharField(max_length=100)

class AuditOffer(models.Model):
    """
    This class contains changes made to Offers model
    """
    operation_type = models.CharField(max_length=100) #Alter Type
    modified_on = models.DateTimeField()
    comment = models.TextField()
    offer_id = models.IntegerField()

    def __str__(self):
        return self.comment

class AuditDailySub(models.Model):
    """
    This class contains changes made to Dailysubs model
    """
    operation_type = models.CharField(max_length=100) #Alter Type
    modified_on = models.DateTimeField()
    comment = models.TextField()
    dailysub_id = models.IntegerField()

    def __str__(self):
        return self.comment

class AuditRequisition(models.Model):
    """
    This class contains changes made to Requisition model
    """
    operation_type = models.CharField(max_length=100) #Alter Type
    modified_on = models.DateTimeField()
    comment = models.TextField()
    requisition_id = models.IntegerField()

    def __str__(self):
        return self.comment
    
class Downloads(models.Model):
    user_name = models.CharField(max_length=100)
    # user_id = models.IntegerField()
    path = models.CharField(max_length=500)