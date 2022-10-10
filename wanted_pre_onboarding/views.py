import json
from django.http import JsonResponse
from django.db.models import Max
from django.db.models.functions import Coalesce
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from wanted_pre_onboarding.models import Employment, Company
from .serializers import CompanySerializer, ApplymentSerializer, EmploymentSerializer, UserSerializer


@api_view(['POST'])
def InsertApplyment(request):
    data = json.loads(request.body)
    employment_max_id = Employment.objects.aggregate(
        employment_id=Coalesce(Max('employment_id'), 1))
    employment_id = employment_max_id['employment_id']
    employment_position = data['employment_position']
    employment_reward = data['employment_reward']
    employment_use_tech = data['employment_use_tech']
    employment_content = data['employment_content']
    company_id = Company.objects.get(company_id=data['company_id'])
    employment = Employment(
        employment_id=employment_id,
        employment_position=employment_position,
        employment_reward=employment_reward,
        employment_use_tech=employment_use_tech,
        employment_content=employment_content,
        company_id=company_id

    )
    insert_flag = employment.save()
    response = {"msg": ""}
    if insert_flag > 0:
        response["msg"] = "success"
    else:
        response["msg"] = "fail"
    return JsonResponse(response)


@api_view(['POST'])
def UpdateApplyment(request):
    data = json.loads(request.body)
    employment_position = data['employment_position']
    employment_reward = data['employment_reward']
    employment_use_tech = data['employment_use_tech']
    employment_content = data['employment_content']
    employment_id = data['employment_id']
    update_flag = Employment.objects.filter(employment_id=employment_id).update(
        employment_position=employment_position,
        employment_reward=employment_reward,
        employment_use_tech=employment_use_tech,
        employment_content=employment_content,
        employment_id=employment_id
    )
    response = {"msg": ""}
    if update_flag > 0:
        response["msg"] = "success"
    else:
        response["msg"] = "fail"
    return JsonResponse(response)
