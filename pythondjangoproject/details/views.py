from django.shortcuts import render
import pandas as pd
from .models import enter_detail

import joblib
reloadModel = joblib.load('./models/RFModelforMPG.pkl')

# Create your views here.
def enterdetails(request):
    return render(request, 'pageone.html')

def predictMPG(request):
    if request.method == 'POST':
        temp_dict = {}
        temp_dict['cylinders'] = request.POST.get('cylinderval')
        temp_dict['displacement'] = request.POST.get('dispval')
        temp_dict['horsepower'] = request.POST.get('hrspwrval')
        temp_dict['weight'] = request.POST.get('wghtval')
        temp_dict['acceleration'] = request.POST.get('accval')
        temp_dict['model_year'] = request.POST.get('modelval')
        temp_dict['origin'] = request.POST.get('originval')

        temp2_dict = temp_dict.copy()
        temp2_dict['model year'] = temp_dict['model_year']

    testData=pd.DataFrame({'x':temp2_dict}).transpose()
    scoreval = reloadModel.predict(testData)[0]
    context = {"scoreval" : scoreval}
    return render(request, 'pageone.html', context)
