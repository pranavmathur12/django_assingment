import csv
import pandas

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Site

from .models import Site


# fs = FileSystemStorage(location='tmp/')


# Serializer
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = "__all__"


# Viewset
class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing IAP Site List.
    """
    queryset = Site.objects.all()
    serializer_class = ProductSerializer

    # @action(detail=False, methods=['POST'])
    # def upload_data(self, request):
    #     """Upload data from CSV"""
    #     file = request.FILES["file"]

    #     content = file.read()  # these are bytes
    #     file_content = ContentFile(content)
    #     file_name = fs.save(
    #         "_tmp.csv", file_content
    #     )
    #     tmp_file = fs.path(file_name)

    #     csv_file = open(tmp_file, errors="ignore")
    #     reader = csv.reader(csv_file)
    #     next(reader)
        
    #     IAP_list = []
    #     for id_, row in enumerate(reader):
    #         (
    #             site_id,
    #             site_name,
    #             country,
    #             order_id,
    #             purchase_id,
    #             csm_name,
    #             serial,
    #             ip_address,
    #             model,
    #             macaddr
    #         ) = row
    #         macaddr = macaddr[0]+macaddr[1]+':'+macaddr[2]+macaddr[3]+':'+ macaddr[4]+macaddr[5]+':'+macaddr[6]+macaddr[7]+':'+macaddr[8]+macaddr[9]+':'+macaddr[10]+macaddr[11]+':'+macaddr[12]+macaddr[13]
    #         IAP_list.append(
    #             IAP(
    #             site_id = site_id,
    #             site_name = site_name,
    #             country = country,
    #             order_id = order_id,
    #             purchase_id = purchase_id,
    #             csm_name = csm_name,
    #             serial = serial.lower(),
    #             ip_address = ip_address,
    #             model = model,
    #             macaddr = macaddr
    #             )
    #         )

    #     IAP.objects.bulk_create(IAP_list)

    #     return Response("Successfully uploaded the data")



    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        """Upload data from CSV"""
        file = request.FILES["file"]
        excel = pandas.read_excel(file)
        Site_List = [
                Site(
                site_id = df['site_id'],
                site_name = df['site_name'],
                country = df['country'],
                order_id = df['order_id'],
                purchase_id = df['purchase_id'],
                csm_name = df['csm_name'],
                serial = df['serial'].lower(),
                ip_address = df['ip_address'],
                model = df['model'],
                macaddr = ':'.join(df['macaddr'][i:i+2] for i in range(0,12,2))
                )
                for i, df in excel.iterrows()
        ]

        Site.objects.bulk_create(Site_List)

        return Response("Successfully uploaded the data")