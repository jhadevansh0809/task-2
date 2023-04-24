from .serializers import UserSerializers,OrganisationSerializers,PermissionSerializer,DeletePermissionSerializer
from rest_framework.generics import ListCreateAPIView,CreateAPIView,ListAPIView
from .models import User,Organisation,Permission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserList(ListCreateAPIView):
    serializer_class=UserSerializers
    queryset=User.objects.all()

    def get(self, request):
        users = User.objects.all()
        total_count = users.count()  
        try:
            try:
                limit = int(request.GET['limit'])
                offset = int(request.GET['offset'])
                users = users[offset:offset+limit]
            except:
                users = users[:limit]
        except:
            users = User.objects.all()
        
        allusers=[]
        for user in users:
            permissions=Permission.objects.filter(user_email=user.email)
            allusers.append({
                'name':user.name,
                'email':user.email,
                'access_to':[{
                    'organisation':permission.organisation_name,
                    'access_control':permission.access_level
    
                } for permission in permissions]
            })

        return Response({
            'total_count': total_count,
            'users':allusers
        })

    def post(self, request):
        try:
            name = request.data.get('name')
            email = request.data.get('email')
            if not all([name, email]):
                return Response(
                    {'error': 'Name and email are required fields'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if User.objects.filter(email=email).exists():
                return Response(
                    {'error': "User with given email already exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user = User(name=name, email=email)
            user.save()
            return Response({
                'name': user.name,
                'email': user.email,
            })
        except:
            return Response({
                'error': "User with given email already exists",
            })

class UsersWithName(APIView):
    def get(self, request):
        name=request.GET['name']
        try:
            users = User.objects.filter(name=name)
            total_count=users.count()
            allusers=[]
            for user in users:
                permissions=Permission.objects.filter(user_email=user.email)
                allusers.append({
                    'name':user.name,
                    'email':user.email,
                    'access_to':[{
                        'organisation':permission.organisation_name,
                        'access_control':permission.access_level
        
                    } for permission in permissions]
                })

            return Response({
                'total_count': total_count,
                'users':allusers
            })
        
        except User.DoesNotExist:
            return Response(
                {'error': f"user with given name not found"},
                status=status.HTTP_404_NOT_FOUND
            )



class UserDetail(APIView):
    def get(self, request):
        email=request.GET['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {'error': f"user with email {email} not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        permissions=Permission.objects.filter(user_email=user.email)
        return Response({
            'name':user.name,
            'email':user.email,
            'access_to':[{
                'organisation':permission.organisation_name,
                'access_control':permission.access_level

            } for permission in permissions]
        })


class OrganisationView(ListCreateAPIView):
    serializer_class=OrganisationSerializers
    queryset=Organisation.objects.all()

    def get(self, request):
        organisations = Organisation.objects.all()
        total_count = organisations.count()  
        try:
            try:
                limit = int(request.GET['limit'])
                offset = int(request.GET['offset'])
                organisations = organisations[offset:offset+limit]
            except:
                organisations = organisations[:limit]
        except:
            organisations = Organisation.objects.all()

        allorg=[]
        for organisation in organisations:
            permissions=Permission.objects.filter(organisation_name=organisation.name)
            allorg.append({
                'name': organisation.name,
                'users':[{
                    'user_email':permission.user_email,
                    'access_control':permission.access_level
    
                } for permission in permissions]
            })

        return Response({
            'total_count': total_count,
            'organisations': allorg
        })

    def post(self, request):
        try:
            name = request.data.get('name')
            if not all([name]):
                return Response(
                    {'error': 'Name is required a field'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if Organisation.objects.filter(name=name).exists():
                return Response(
                    {'error': "Organisation with given name already exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            organisation = Organisation(name=name)
            organisation.save()
            return Response({
                'name': organisation.name,
            })
        except:
            return Response({
                'error': "Organisation with given name already exists",
            })


class OrganisationDetail(APIView):
    def get(self, request):
        name=request.GET['name']
        try:
            organisation = Organisation.objects.get(name=name)
        except Organisation.DoesNotExist:
            return Response(
                {'error': f"Organisation with name {name} not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        permissions=Permission.objects.filter(organisation_name=organisation.name)
        return Response({
            'name': organisation.name,
                'users':[{
                    'user_email':permission.user_email,
                    'access_control':permission.access_level
    
                } for permission in permissions]
        })
    

class PermissionsListView(ListAPIView):
    serializer_class=PermissionSerializer
    queryset=Permission.objects.all()

class CreateUpdatePermissionsView(CreateAPIView):
    serializer_class = PermissionSerializer

    def post(self,request):
        try:
            user_email = request.data.get('user_email')
            organisation_name = request.data.get('organisation_name')
            access_level = request.data.get('access_level')
            if(access_level=='Read'):
                access_level='READ'
            if(access_level=='Write'):
                access_level='WRITE'
            if(access_level=='Read and Write'):
                access_level='READANDWRITE'
            if(access_level=='Admin'):
                access_level='ADMIN'
            if not all([user_email,organisation_name,access_level]):
                return Response(
                    {'error': 'You missed some required fields'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if len(Organisation.objects.filter(name=organisation_name)) is not 0:
                    if(len(User.objects.filter(email=user_email))) is not 0:
                        if(len(Permission.objects.filter(user_email=user_email,organisation_name=organisation_name,access_level=access_level)) is not 0):
                            return Response(
                            {'warning': "Permission already set"},
                             )
                        else:
                            if(len(Permission.objects.filter(user_email=user_email,organisation_name=organisation_name)) is not 0):
                                permission=Permission.objects.filter(user_email=user_email,organisation_name=organisation_name)
                                permission.delete()
                                permission=Permission(user_email=user_email,organisation_name=organisation_name,access_level=access_level)
                                permission.save()
                                return Response(
                                {'success': "Permission updated successfully"}
                                )

                            else:
                                permission=Permission(user_email=user_email,organisation_name=organisation_name,access_level=access_level)
                                permission.save()
                                return Response(
                                {'success': "Permission set successfully"}
                                )
                     
                    else:
                        return Response(
                        {'error': "User with given name doesn't exists"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                    return Response(
                        {'error': "Organisation with given name doesn't exists"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

        except:
            return Response({
                'error': "Some error occured",
            })



class DeletePermissionsView(CreateAPIView):
    serializer_class=DeletePermissionSerializer

    def post(self, request):
        user_email = request.data.get('user_email')
        organisation_name = request.data.get('organisation_name')
        if not all([user_email,organisation_name]):
            return Response(
                {'error': 'You missed some required fields'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if len(Organisation.objects.filter(name=organisation_name)) is not 0:
            if(len(User.objects.filter(email=user_email))) is not 0:
                if(len(Permission.objects.filter(user_email=user_email,organisation_name=organisation_name)) is not 0):
                    permission=Permission.objects.filter(user_email=user_email,organisation_name=organisation_name)
                    permission.delete()
                    return Response(
                    {'success': "Permission deleted successfully"}
                    )

                else:
                    return Response(
                    {'error': "No permission assigned to this user for this organization"},
                    status=status.HTTP_400_BAD_REQUEST
                    )
                
            else:
                return Response(
                {'error': "User with given name doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
                return Response(
                    {'error': "Organisation with given name doesn't exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
