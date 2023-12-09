import os
from django.utils.html import format_html
from django.template.loader import get_template
from django.http import FileResponse
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize as serialized
import csv
import pandas as pd
import json
import wget


def reader(filepath):
    if os.path.exists(filepath):
        pad = pd.read_csv(filepath)
        json_list = json.loads(json.dumps(list(pad.T.to_dict().values())))
        return json_list
    else:
        return JsonResponse({"message":"Path writter not found..."})



def csvWriterSingleRow(path='', array_data=[]):
    """
        ***** Sharashell Technology limited Software Department *****

        Custom CSV writer to genenrate a csv file, with a single Row row1, row2, row3, row4
        path: A unix path to the file.
        array_data: A single row data, in a list format.
    """
    with open(path, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(array_data)


def csvResultWriter(path='', data=[], data2=[]):
    try:
        """
            ***** Sharashell Technology limited Software Department *****
            Custom CSV writer to genenrate a csv result file, with a single Row row1, row2, row3, row4
            path: A unix path to the file.
            data: A single row data, in a list format.
        """
        with open(path, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(data)
            for student_code,student_name in data2:
                filewriter.writerow([student_code,student_name])
    except Exception as e:
        return e




def csvtWriter(path='', data=[], data2=[]):
    try:
        """
            ***** Sharashell Technology limited Software Department *****
            Custom CSV writer to genenrate a csv result file, with a single Row row1, row2, row3, row4
            path: A unix path to the file.
            data: A single row data, in a list format.
        """
        with open(path, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(data)
            for std in data2:
                filewriter.writerow(std)
    except Exception as e:
        return e




def csvWriterMultipleRow(data_file=None, file_path="templates/data.csv"):
    """
        ***** Sharashell Technology limited Software Department *****

        Custom CSV writer to genenrate a csv file, with multiple Rows:
        [row1, row2, row3, row4] - first row
        [row1, row2, row3, row4] - second row
        [row1, row2, row3, row4] - third row
        [row1, row2, row3, row4] - ** infinity

        data_file: request.FILES[postfile].read().decode("utf-8")
        file_path: A unix path to the file.

        Note: request.FILES[postfile].read().decode("utf-8") works for Django or Flask.
        If you want to use it any where execpt in Django, you can apply the POST['filedata']
    
    """
    try:
        filedata = data_file
        filepath = file_path
    
        with open(filepath, 'w') as files:
            files.writelines(filedata)
            files.close()

        pad = pandas.read_csv(filepath)
        json_list = json.loads(json.dumps(list(pad.T.to_dict().values())))
        return json_list

    except Exception as e:
        return e
        # print(e)






def pdf_converter():
    try:
        context = {}
        file_format = str('pdf').lower()
        template = get_template("templateresponse/pdf_vieworder.html")
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            response = HttpResponse(
            result.getvalue(), content_type='application/{}'.format(file_format))
            result.seek(0)
            fileresponse = FileResponse(
                result, as_attachment=True, filename='report.pdf')
                # SmsAndEmailMessengerApp().CustomSiteSms()
            return response

        return None
    except:
        pass


def file_downloader(filename=None):
    try:
        file_format = str('pdf').lower()
        template = os.path.abspath('templates/csv/teacher.csv')
        fileresponse = template
        return HttpResponse('Downloading...')

    except:
        pass



def download_file(path_url=None, storage=None):
    try:
        wget.download(path_url, storage)
    except Exception as e:
        print(e)




class ModelSerializerDataOutput:        


    def __init__(self, data=None, key=None) -> None:
   
        """
        This package will will help serialize model data efficiently and,
        prepare it for html output.
        """
        try:
            self.keys = key
            self.dataWithNaturalKey = serialized('python', data, 
                use_natural_foreign_keys=True, use_natural_primary_keys=True)
            self.dataWithOutNaturalKey = serialized('python', data)
            self.combinedData = zip(self.dataWithNaturalKey, self.dataWithOutNaturalKey)
            self.container = []
            self.error = {}

        except Exception as e:
            self.error.update({"ConstructorError": e})

    
    def NaturalKeyAndNoneNaturalKeySerializer(self):
        """
        Serializer with a natural key and none natural key.

        *******
        serialized('python', model_to_serialize, 
        use_natural_foreign_keys=True, use_natural_primary_keys=True)

        ******
        serialized('python', model_to_serialize)
        """
        try: 

            for dt in self.combinedData:
            
                if (dt[0].__contains__('fields')) and (dt[1].__contains__('fields')):
                    data0 = dt[0].get('fields')
                    data1 = dt[1].get('fields')
                    for k in self.keys:

                        if (k.__contains__('name')) and (k.__contains__('config')):

                            k_name   = k.get('name')
                            k_config = k.get('config')
                            k_config = k_config.get('config')
                                
                            content = {k_name:data0.get(k_name), f'{k_name}_id':data1.get(k_name)}
                            k_config.update({'name':'NaturalKeyAndNoneNaturalKeySerializer'})
                            content.update(k_config)
                            self.container.append(content)
                        else:
                            self.error.update({"keyError":"Looking for [ {'name':'', 'config':''} ]"})

                else:
                    self.error.update({"combineDataError": "'fields':{'': ''}" })

        except Exception as e:
            self.error.update({'NaturalKeyAndNoneNaturalKeySerializer': e})
    


    def onlyNaturalKeySerializer(self):
        """
        Serializer with a natural key only.
        serialized('python', model_to_serialize)
        """
        try:
            data_item = self.dataWithNaturalKey

            for item in data_item:
                
                if (item.__contains__('fields')):
                    item = item.get('fields')

                    for key in self.keys:

                        dc_config = key.get('config')
                        dc_config.get('config')
                        dc_config.update({'name':'onlyNaturalKeySerializer'})
                        item.update(dc_config)
                    self.container.append(item)
     
          
        except Exception as e:
            self.error.update({'onlyNaturalKeySerializerError':e})


    def show(self):
        return self.container



    def errorO(self):
        return self.error