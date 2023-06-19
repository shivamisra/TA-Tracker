from .models import Offer,DailySub,Requisition,AuditDailySub,AuditOffer,AuditRequisition
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime
from django.utils import timezone
from django.core import serializers
import json
from . import models
@receiver(pre_save, sender = Offer)
def audit_offer_handler(sender, instance, **kwargs):
    """
    This functions is used to handle AuditOffers Model.
    Whatever changes made in Offer model is recorded in AuditOffer Model.

    Args: 
        sender: Offer.
        instance: Offer Instance.
        **kwargs:
    Returns: None
    """
    
    dict = audit_tables_handler('Offer', instance)

    AuditOffer.objects.create(
        operation_type = dict['type'],
        modified_on = datetime.now(tz=timezone.utc),
        comment = dict['comment'],
        offer_id = dict['id']
    )

@receiver(pre_save, sender = DailySub)
def audit_dailysub_handler(sender, instance, **kwargs):
    """
    This functions is used to handle AuditDailySub Model.
    Whatever changes made in DailySub model is recorded in AuditDailySub Model.

    Args: 
        sender: Offer.
        instance: Offer Instance.
        **kwargs:
    Returns: None
    """
    
    dict = audit_tables_handler('DailySub', instance)
    
    AuditDailySub.objects.create(
        operation_type = dict['type'],
        modified_on = datetime.now(tz=timezone.utc),
        comment = dict['comment'],
        dailysub_id = dict['id']
    )

@receiver(pre_save, sender = Requisition)
def audit_requisition_handler(sender, instance, **kwargs):
    """
    This functions is used to handle AuditRequisition Model.
    Whatever changes made in Requisition model is recorded in AuditRequisition Model.

    Args: 
        sender: Offer.
        instance: Offer Instance.
        **kwargs:
    Returns: None
    """
    
    dict = audit_tables_handler('Requisition', instance)

    AuditRequisition.objects.create(
        operation_type = dict['type'],
        modified_on = datetime.now(tz=timezone.utc),
        comment = dict['comment'],
        requisition_id = dict['id']
    )

def audit_tables_handler(model_name, instance):
    """
    This function handles audit tables

    Args:
        model_name: Name of the table.
        instance: Instance which is updated or created.
    
    Returns:
        dict: Dictionary which contains alter type and changes made to instance.
    """
    
    model = getattr(models, model_name)
    dict = {}
    dict['type'] = ""
    dict['comment'] = ""
    if instance.id is not None:
        dict['type'] = "Update"
        dict['id'] = instance.id
        qs = model.objects.get(pk=instance.id)
        dict['comment'] = get_comment(qs, instance)
    else:
        dict['type'] = "Create"
        latest_record_id = model.objects.last()
        dict['id'] = latest_record_id.id + 1 if latest_record_id else 1
        dict['comment'] = model_name + " record with id-" + str(dict['id']) + " has been created."
    return dict

def get_comment(original, modified):
    """
    This functions is used to track the changes made to a record

    Args: 
        original: original record.
        modified: modified record.
    Returns: 
        changes made to a record.
        For example: 

        "status changed from Rejected to Offered, email changed from naveen@gmail.com to naveen@innovasolutions"
    """
    original_data = json.loads(serializers.serialize('json', [original,]))
    modified_data = json.loads(serializers.serialize('json', [modified,]))
    original_dict = original_data[0]['fields']
    modified_dict = modified_data[0]['fields']
    comment = ""
    for field in original_dict:
            if original_dict[field] != modified_dict[field]:
                comment += field + " is changed from " + str(original_dict[field]) + " to " + str(modified_dict[field]) + ", "
    return comment[:-2] if comment else "Nothing Changed"