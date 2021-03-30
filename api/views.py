from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions, DjangoObjectPermissions
from .custompermissions import MyPermission
from .customauth import CustomAuth
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from .throttling import EmonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .mypagination import *

# if one instance
def student_detail(request, pk ):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')

#if query set
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'aplication/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'aplication/json')

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)

        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'aplication/json')
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many = True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'aplication/json')
    elif request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'aplication/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'aplication/json')
    
    elif request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data = pythondata, partial = True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'aplication/json')
            
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'aplication/json')

    elif request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg' : 'Data Deleted!!'}

        return JsonResponse(res, safe=False)
        
# Class based and also using model serializer
@method_decorator(csrf_exempt, name='dispatch')
class StudentMAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)

        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentMSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'aplication/json')

        else:
            stu = Student.objects.all()
            serializer = StudentMSerializer(stu, many = True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'aplication/json')

    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentMSerializer(data = pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'aplication/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'aplication/json')
    
    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentMSerializer(stu, data = pythondata, partial = True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'aplication/json')
            
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'aplication/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg' : 'Data Deleted!!'}

        return JsonResponse(res, safe=False)

@api_view()
def hello_world(request):
    return Response({'msg': 'Hello World'})

@api_view(['POST'])
def hello_world(request):
    if request.method == 'POST':
        print(request.data)
        return Response({'msg': 'This is post rq'})

# Function but not for good browseable testing
@api_view(['GET','POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
        sid = request.data.get('id')
        if sid is not None:
            stu = Student.objects.get(id = sid)
            serializer = StudentMSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentMSerializer(stu, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentMSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer=StudentMSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

# Function but for good browseable testing
@api_view(['GET','POST', 'PUT', 'PATCH', 'DELETE'])
def studentb_api(request, pk = None):
    if request.method == 'GET':
        sid = pk
        if sid is not None:
            stu = Student.objects.get(id = sid)
            serializer = StudentMSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentMSerializer(stu, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentMSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer=StudentMSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer=StudentMSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

# class based api view

class StudentClassAPI(APIView):
    def get(self, request, pk=None,format = None):
        sid = pk
        if sid is not None:
            stu = Student.objects.get(id = sid)
            serializer = StudentMSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentMSerializer(stu, many = True)
        return Response(serializer.data)

    def post(self,request,format = None):
        serializer = StudentMSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format = None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer=StudentMSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors)

    def patch(self, request, pk, format = None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer=StudentMSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
    



# generic api view and Model Mixin 
class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
   
class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StudentRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer

    def put(self, request, partial=True, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class StudentDelete(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class StudentPatch(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)








# GENERIC IN GROUP

class StuLC(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, partial=True, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StuRUD(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, partial=True, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# Conreate View Class  and part by part api throttle 
class CsList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

class CsCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modstu'


class CsRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'


class CsUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modstu'



class Csdelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modstu'




# Conreate View Class in group 

class  CsListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer

class  CsRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer

 
# View Set Class
class StudentViewset(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentMSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentMSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentMSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer=StudentMSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors)

    def partial_update(self, request, pk, format = None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer=StudentMSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, format = None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})


# Model View Set Class
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer

# Model Read ONly View Set Class
# class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentMSerializer
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

# Permission authentication for class based view
class StudentAuthView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]

# Session authentication for class based view and Django Model Permission and custom Permission and Token Authentication and custom authentication
# and jwt authentication and throttling
class StudentSession(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer
    # authentication_classes = [CustomAuth]
    # authentication_classes = [JWTAuthentication]
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # # permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # # permission_classes = [DjangoModelPermissions]
    # # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # # permission_classes = [DjangoObjectPermissions]
    # # permission_classes = [MyPermission]

    # throttling
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_classes = [AnonRateThrottle, EmonRateThrottle]



#auth permission class based view
@api_view(['GET','POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def studentb_api_permission(request, pk = None):
    if request.method == 'GET':
        sid = pk
        if sid is not None:
            stu = Student.objects.get(id = sid)
            serializer = StudentMSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentMSerializer(stu, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentMSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer=StudentMSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer=StudentMSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

# Api filtering and search filtering and  Ordering filter and Pagination
class StuL(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentMSerializer
    # filter one method

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)

    # generic filtering
    # for per view
    # filter_backends=[DjangoFilterBackend]
    # filterset_fields = ['city']
    # filterset_fields = ['name', 'city']
    # filter_backends= [SearchFilter]
    # filter_backends= [OrderingFilter]
    # search_fields = ['^name','city']
    # ordering_fields =['name', 'city']

    # page number pagination
    pagination_class = MyPageNPagination

