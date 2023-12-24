from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from .models import Collegerecomment,BoysCollege,GirlsCollege
from .forms import StudentPreferencesForm
from clgpost.models import Collegepost




def recommend_colleges(request):
    recommended_colleges= []
    

    if request.method == 'POST':
        form = StudentPreferencesForm(request.POST)
        if form.is_valid():
            degree = form.cleaned_data['degree']
            min_score = form.cleaned_data['min_score']
            college_choice = form.cleaned_data['college_choice']
            Select_shift = form.cleaned_data['Select_shift']
            

            if min_score > 1100:
                form.add_error('min_score', 'Minimum marks should not exceed 1100 .')
            else:

          
           
             if college_choice == 'boys' and Select_shift == 'morning':
                recommended_colleges = BoysCollege.objects.filter(
                    Q(degree_level=degree),
                    Q(minimum_score=min_score),
                  
                )
           
          
            
                if degree == 'FSC(eng)' and min_score >= 700 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Graduate College of Science Wahdat Road, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  # Convert to list
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=730 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Graduate College of Science Wahdat Road, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 750 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Graduate College of Science Wahdat Road, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 630 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Graduate College of Science Wahdat Road, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 515 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Graduate College of Science Wahdat Road, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 575 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Graduate College of Science Wahdat Road, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)     
                else :
                   pass    


                if degree == 'FSC(eng)' and min_score >= 1030 :
                  specific_college = BoysCollege.objects.filter(name='Government College University Lahore (GCUL)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=1045 :
                  specific_college = BoysCollege.objects.filter(name='Government College University Lahore (GCUL)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 980 :
                  specific_college =  BoysCollege.objects.filter(name='Government College University Lahore (GCUL)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 940 :
                  specific_college =  BoysCollege.objects.filter(name='Government College University Lahore (GCUL)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 900 :
                  specific_college = BoysCollege.objects.filter(name='Government College University Lahore (GCUL)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 890 :
                  specific_college =  BoysCollege.objects.filter(name='Government College University Lahore (GCUL)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)



                if degree == 'FSC(eng)' and min_score >= 890:
                  specific_college =  BoysCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 900 :
                  specific_college = BoysCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 880 :
                  specific_college = BoysCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 692 :
                  specific_college =BoysCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 680 :
                  specific_college =BoysCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 660:
                  specific_college =BoysCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)   



                if degree == 'FSC(eng)' and min_score >= 890:
                  specific_college =  BoysCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 920 :
                  specific_college = BoysCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 880 :
                  specific_college = BoysCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 692 :
                  specific_college =BoysCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 680 :
                  specific_college =BoysCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 660:
                  specific_college =BoysCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)     



           
                if degree == 'FSC(eng)' and min_score >= 780 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Islamia Graduate College, Civil Lines, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 800 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Islamia Graduate College, Civil Lines, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 902 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Islamia Graduate College, Civil Lines, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 751 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Islamia Graduate College, Civil Lines, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 496 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Islamia Graduate College, Civil Lines, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 550 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Islamia Graduate College, Civil Lines, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)      


                if degree == 'FSC(eng)' and min_score >= 851:
                  specific_college =  BoysCollege.objects.filter(name='Govt. M.A.O. College, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 875 :
                  specific_college = BoysCollege.objects.filter(name='Govt. M.A.O. College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 880 :
                  specific_college = BoysCollege.objects.filter(name='Govt. M.A.O. College, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 792 :
                  specific_college =BoysCollege.objects.filter(name='Govt. M.A.O. College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 680 :
                  specific_college =BoysCollege.objects.filter(name='Govt. M.A.O. College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 663:
                  specific_college =BoysCollege.objects.filter(name='Govt. M.A.O. College, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)   



                if degree == 'FSC(eng)' and min_score >= 851:
                  specific_college =  BoysCollege.objects.filter(name='Superior College Ferozepur Road, Kalma Chowk').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 875 :
                  specific_college = BoysCollege.objects.filter(name='Superior College Ferozepur Road, Kalma Chowk').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 880 :
                  specific_college = BoysCollege.objects.filter(name='Superior College Ferozepur Road, Kalma Chowk').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 792 :
                  specific_college =BoysCollege.objects.filter(name='Superior College Ferozepur Road, Kalma Chowk').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 680 :
                  specific_college =BoysCollege.objects.filter(name='Superior College Ferozepur Road, Kalma Chowk').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 663:
                  specific_college =BoysCollege.objects.filter(name='Superior College Ferozepur Road, Kalma Chowk').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)     



                if degree == 'FSC(eng)' and min_score >= 700 :
                  specific_college = BoysCollege.objects.filter(name='Government Islamia College,  Railway Road').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=730 :
                  specific_college = BoysCollege.objects.filter(name='Government Islamia College,  Railway Road').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 770 :
                  specific_college =  BoysCollege.objects.filter(name='Government Islamia College,  Railway Road').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 630 :
                  specific_college =  BoysCollege.objects.filter(name='Government Islamia College,  Railway Road').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 515 :
                  specific_college = BoysCollege.objects.filter(name='Government Islamia College,  Railway Road').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 575 :
                  specific_college =  BoysCollege.objects.filter(name='Government Islamia College,  Railway Road').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)



                if degree == 'FSC(eng)' and min_score >= 700 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Colleges of commerce , Sabzazar').first()
                  recommended_colleges = list(recommended_colleges)  # Convert to list
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=700 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Colleges of commerce , Sabzazar').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 770 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Colleges of commerce , Sabzazar').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 630 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Colleges of commerce , Sabzazar').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 515 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Colleges of commerce , Sabzazar').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 575 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Colleges of commerce , Sabzazar').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)




                if degree == 'FSC(eng)' and min_score >= 634:
                  specific_college =  BoysCollege.objects.filter(name='Govt. Graduate College, Township, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 701 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Graduate College, Township, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 817 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Graduate College, Township, Lahore').first()
                  recommended_colleges = list(recommended_colleges)
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 775 :
                  specific_college =BoysCollege.objects.filter(name='Govt. Graduate College, Township, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 690 :
                  specific_college =BoysCollege.objects.filter(name='Govt. Graduate College, Township, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 572:
                  specific_college =BoysCollege.objects.filter(name='Govt. Graduate College, Township, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)  


                if degree == 'FSC(eng)' and min_score >= 720 :
                  specific_college = BoysCollege.objects.filter(name='Government Dayal Singh College, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=730 :
                  specific_college = BoysCollege.objects.filter(name='Government Dayal Singh College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 750 :
                  specific_college =  BoysCollege.objects.filter(name='Government Dayal Singh College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 630 :
                  specific_college =  BoysCollege.objects.filter(name='Government Dayal Singh College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 555 :
                  specific_college = BoysCollege.objects.filter(name='Government Dayal Singh College, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 565 :
                  specific_college =  BoysCollege.objects.filter(name='Government Dayal Singh College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)     





             elif college_choice == 'girls' and Select_shift == 'morning':
                recommended_colleges = GirlsCollege.objects.filter(
                    Q(degree_level=degree),
                    Q(minimum_score=min_score),
                   
                )    
                if degree == 'FSC(eng)' and min_score >= 750 :
                  specific_college = GirlsCollege.objects.filter(name='Government Degree College for women Islampura,Lahore').first()
                  recommended_colleges = list(recommended_colleges)  # Convert to list
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=780 :
                  specific_college =  GirlsCollege.objects.filter(name='Government Degree College for women Islampura,Lahore').first()
                  recommended_colleges = list(recommended_colleges)
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 850 :
                  specific_college =  GirlsCollege.objects.filter(name='Government Degree College for women Islampura,Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 660 :
                  specific_college =  GirlsCollege.objects.filter(name='Government Degree College for women Islampura,Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 550 :
                  specific_college =  GirlsCollege.objects.filter(name='Government Degree College for women Islampura,Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 600 :
                  specific_college = GirlsCollege.objects.filter(name='Government Degree College for women Islampura,Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)   


                if degree == 'FSC(eng)' and min_score >= 926 :
                  specific_college = GirlsCollege.objects.filter(name='Govt. Queen Mary Graduate College, Lahore,').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=952 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt. Queen Mary Graduate College, Lahore,').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 860 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt. Queen Mary Graduate College, Lahore,').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 700 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt. Queen Mary Graduate College, Lahore,').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 650 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt. Queen Mary Graduate College, Lahore,').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 730 :
                  specific_college = GirlsCollege.objects.filter(name='Govt. Queen Mary Graduate College, Lahore,').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)  



                if degree == 'FSC(eng)' and min_score >= 890:
                  specific_college =  GirlsCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 900 :
                  specific_college = GirlsCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 880 :
                  specific_college = GirlsCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 692 :
                  specific_college =GirlsCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 680 :
                  specific_college =GirlsCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 660:
                  specific_college =GirlsCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)     
                
                
                if degree == 'FSC(eng)' and min_score >= 880:
                  specific_college =  GirlsCollege.objects.filter(name='Superior College Muslim Town - Canal Campus').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 900 :
                  specific_college = GirlsCollege.objects.filter(name='Superior College Muslim Town - Canal Campus').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 890 :
                  specific_college = GirlsCollege.objects.filter(name='Superior College Muslim Town - Canal Campus').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 692 :
                  specific_college =GirlsCollege.objects.filter(name='Superior College Muslim Town - Canal Campus').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 680 :
                  specific_college =GirlsCollege.objects.filter(name='Superior College Muslim Town - Canal Campus').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 660:
                  specific_college =GirlsCollege.objects.filter(name='Superior College Muslim Town - Canal Campus').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)    



                if degree == 'FSC(eng)' and min_score >= 890:
                  specific_college =  GirlsCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 920 :
                  specific_college = GirlsCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 880 :
                  specific_college = GirlsCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 692 :
                  specific_college =GirlsCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 680 :
                  specific_college =GirlsCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 660:
                  specific_college =GirlsCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)    

                
                       

                if degree == 'FSC(eng)' and min_score >= 750 :
                  specific_college = GirlsCollege.objects.filter(name='Govt.Postgraduate College(W) Samanabad Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=780 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt.Postgraduate College(W) Samanabad Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 850 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt.Postgraduate College(W) Samanabad Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 660 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt.Postgraduate College(W) Samanabad Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 550 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt.Postgraduate College(W) Samanabad Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 600 :
                  specific_college = GirlsCollege.objects.filter(name='Govt.Postgraduate College(W) Samanabad Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)     
                         
                


               
                if degree == 'FSC(eng)' and min_score >= 833 :
                  specific_college = GirlsCollege.objects.filter(name='Govt. Graduate College for Women, Wahdat Colony').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=895 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt. Graduate College for Women, Wahdat Colony').first()
                  recommended_colleges = list(recommended_colleges)
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 810 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt. Graduate College for Women, Wahdat Colony').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 741 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt. Graduate College for Women, Wahdat Colony').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 690 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt. Graduate College for Women, Wahdat Colony').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 670 :
                  specific_college = GirlsCollege.objects.filter(name='Govt. Graduate College for Women, Wahdat Colony').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)    


                if degree == 'FSC(eng)' and min_score >= 700 :
                  specific_college = GirlsCollege.objects.filter(name='Govt College For Women Township Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=817 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt College For Women Township Lahore').first()
                  recommended_colleges = list(recommended_colleges)
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 710 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt College For Women Township Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 571 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt College For Women Township Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 540 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt College For Women Township Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 520 :
                  specific_college = GirlsCollege.objects.filter(name='Govt College For Women Bund Road Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)

                
                if degree == 'FSC(eng)' and min_score >= 633 :
                  specific_college = GirlsCollege.objects.filter(name='Govt Degree College for Women Gawalmandi Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=695 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt Degree College for Women Gawalmandi Lahore').first()
                  recommended_colleges = list(recommended_colleges)
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 660 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt Degree College for Women Gawalmandi Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 571 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt Degree College for Women Gawalmandi Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 540 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt Degree College for Women Gawalmandi Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 510 :
                  specific_college = GirlsCollege.objects.filter(name='Govt Degree College for Women Gawalmandi Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)  



                if degree == 'FSC(eng)' and min_score >= 733 :
                  specific_college = GirlsCollege.objects.filter(name='Govt College For Women Bund Road Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=795 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt College For Women Bund Road Lahore').first()
                  recommended_colleges = list(recommended_colleges)
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 760 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt College For Women Bund Road Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 571 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt College For Women Bund Road Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 540 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt College For Women Bund Road Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 520 :
                  specific_college = GirlsCollege.objects.filter(name='Govt College For Women Bund Road Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)  




#---------- evening based condition------------------------------------------------> 


             if college_choice == 'boys' and Select_shift == 'evening':
                recommended_colleges = BoysCollege.objects.filter(
                    Q(degree_level=degree),
                    Q(minimum_score=min_score),
                   
                )
            
           
            
                if degree == 'FSC(eng)' and min_score >= 475 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Graduate College of Science Wahdat Road, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=475 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Graduate College of Science Wahdat Road, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 600 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Graduate College of Science Wahdat Road, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 475 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Graduate College of Science Wahdat Road, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 400 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Graduate College of Science Wahdat Road, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 400 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Graduate College of Science Wahdat Road, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)     
                else:
                   pass                
           
                if degree == 'FSC(eng)' and min_score >= 680 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Islamia Graduate College, Civil Lines, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 700 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Islamia Graduate College, Civil Lines, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 750 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Islamia Graduate College, Civil Lines, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 651 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Islamia Graduate College, Civil Lines, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 496 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Islamia Graduate College, Civil Lines, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 500 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Islamia Graduate College, Civil Lines, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)   


                if degree == 'FSC(eng)' and min_score >= 980 :
                  specific_college = BoysCollege.objects.filter(name='Government College University Lahore (GCUL)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=1000 :
                  specific_college = BoysCollege.objects.filter(name='Government College University Lahore (GCUL)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 900 :
                  specific_college =  BoysCollege.objects.filter(name='Government College University Lahore (GCUL)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 890 :
                  specific_college =  BoysCollege.objects.filter(name='Government College University Lahore (GCUL)').first()
                  recommended_colleges = list(recommended_colleges)
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 795 :
                  specific_college = BoysCollege.objects.filter(name='Government College University Lahore (GCUL)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 790 :
                  specific_college =  BoysCollege.objects.filter(name='Government College University Lahore (GCUL)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)



                if degree == 'FSC(eng)' and min_score >= 800:
                  specific_college =  BoysCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 860 :
                  specific_college = BoysCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 790 :
                  specific_college = BoysCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 590 :
                  specific_college =BoysCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 580 :
                  specific_college =BoysCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 560:
                  specific_college =BoysCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)   



                if degree == 'FSC(eng)' and min_score >= 870:
                  specific_college =  BoysCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 890 :
                  specific_college = BoysCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 860 :
                  specific_college = BoysCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 692 :
                  specific_college =BoysCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 680 :
                  specific_college =BoysCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 660:
                  specific_college =BoysCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)    



                
                if degree == 'FSC(eng)' and min_score >= 475 :
                  specific_college = BoysCollege.objects.filter(name='Government Islamia College,  Railway Road').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=475 :
                  specific_college = BoysCollege.objects.filter(name='Government Islamia College,  Railway Road').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 600 :
                  specific_college =  BoysCollege.objects.filter(name='Government Islamia College,  Railway Road').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 475 :
                  specific_college =  BoysCollege.objects.filter(name='Government Islamia College,  Railway Road').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 400 :
                  specific_college = BoysCollege.objects.filter(name='Government Islamia College,  Railway Road').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 400 :
                  specific_college =  BoysCollege.objects.filter(name='Government Islamia College,  Railway Road').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)



                if degree == 'FSC(eng)' and min_score >= 600:
                  specific_college =  BoysCollege.objects.filter(name='Govt. M.A.O. College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 600 :
                  specific_college = BoysCollege.objects.filter(name='Govt. M.A.O. College, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 600 :
                  specific_college = BoysCollege.objects.filter(name='Govt. M.A.O. College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 475 :
                  specific_college =BoysCollege.objects.filter(name='Govt. M.A.O. College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 400 :
                  specific_college =BoysCollege.objects.filter(name='Govt. M.A.O. College, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 400:
                  specific_college =BoysCollege.objects.filter(name='Govt. M.A.O. College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)    



                if degree == 'FSC(eng)' and min_score >= 600:
                  specific_college =  BoysCollege.objects.filter(name='Govt. Graduate College, Township, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 690 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Graduate College, Township, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 760 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Graduate College, Township, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 690 :
                  specific_college =BoysCollege.objects.filter(name='Govt. Graduate College, Township, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 590 :
                  specific_college =BoysCollege.objects.filter(name='Govt. Graduate College, Township, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 500:
                  specific_college =BoysCollege.objects.filter(name='Govt. Graduate College, Township, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)    



                if degree == 'FSC(eng)' and min_score >= 450 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Colleges of commerce , Sabzazar').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=480 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Colleges of commerce , Sabzazar').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 500 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Colleges of commerce , Sabzazar').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 400 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Colleges of commerce , Sabzazar').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 400 :
                  specific_college = BoysCollege.objects.filter(name='Govt. Colleges of commerce , Sabzazar').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 400 :
                  specific_college =  BoysCollege.objects.filter(name='Govt. Colleges of commerce , Sabzazar').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)  



                if degree == 'FSC(eng)' and min_score >= 475 :
                  specific_college = BoysCollege.objects.filter(name='Government Dayal Singh College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 475 :
                  specific_college = BoysCollege.objects.filter(name='Government Dayal Singh College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 500 :
                  specific_college =  BoysCollege.objects.filter(name='Government Dayal Singh College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 475 :
                  specific_college =  BoysCollege.objects.filter(name='Government Dayal Singh College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 400 :
                  specific_college = BoysCollege.objects.filter(name='Government Dayal Singh College, Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 400 :
                  specific_college =  BoysCollege.objects.filter(name='Government Dayal Singh College, Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)   


#---------------evening girls------------------------------------------------->

             elif college_choice == 'girls' and  Select_shift == 'evening':
                recommended_colleges = GirlsCollege.objects.filter(
                    Q(degree_level=degree),
                    Q(minimum_score=min_score),
                    
                )    
                if degree == 'FSC(eng)' and min_score >= 660 :
                  specific_college = GirlsCollege.objects.filter(name='Government Degree College for women Islampura,Lahore').first()
                  recommended_colleges = list(recommended_colleges)  # Convert to list
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=690 :
                  specific_college =  GirlsCollege.objects.filter(name='Government Degree College for women Islampura,Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 650 :
                  specific_college =  GirlsCollege.objects.filter(name='Government Degree College for women Islampura,Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 500 :
                  specific_college =  GirlsCollege.objects.filter(name='Government Degree College for women Islampura,Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 460 :
                  specific_college =  GirlsCollege.objects.filter(name='Government Degree College for women Islampura,Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 450 :
                  specific_college = GirlsCollege.objects.filter(name='Government Degree College for women Islampura,Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)     



                if degree == 'FSC(eng)' and min_score >=790 :
                  specific_college = GirlsCollege.objects.filter(name='Govt. Queen Mary Graduate College, Lahore,').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 810 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt. Queen Mary Graduate College, Lahore,').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 725 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt. Queen Mary Graduate College, Lahore,').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 510 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt. Queen Mary Graduate College, Lahore,').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 500 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt. Queen Mary Graduate College, Lahore,').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 500 :
                  specific_college = GirlsCollege.objects.filter(name='Govt. Queen Mary Graduate College, Lahore,').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)

                if degree == 'FSC(eng)' and min_score >= 890:
                  specific_college =  GirlsCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 900 :
                  specific_college = GirlsCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 880 :
                  specific_college = GirlsCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 692 :
                  specific_college =GirlsCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 680 :
                  specific_college =GirlsCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 660:
                  specific_college =GirlsCollege.objects.filter(name='Punjab Group of Colleges ( Airline and City Campus)').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)     
                

                if degree == 'FSC(eng)' and min_score >= 870:
                  specific_college =  GirlsCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 890 :
                  specific_college = GirlsCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 800 :
                  specific_college = GirlsCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 692 :
                  specific_college =GirlsCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 600 :
                  specific_college =GirlsCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 660:
                  specific_college =GirlsCollege.objects.filter(name='Concordia College Allama Iqbal Town Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)     
                

                if degree == 'FSC(eng)' and min_score >= 850:
                  specific_college =  GirlsCollege.objects.filter(name='Superior College Muslim Town - Canal Campus').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 870 :
                  specific_college = GirlsCollege.objects.filter(name='Superior College Muslim Town - Canal Campus').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 790 :
                  specific_college = GirlsCollege.objects.filter(name='Superior College Muslim Town - Canal Campus').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Statistics)' and min_score >= 620 :
                  specific_college =GirlsCollege.objects.filter(name='Superior College Muslim Town - Canal Campus').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Ecnomics)' and min_score >= 610 :
                  specific_college =GirlsCollege.objects.filter(name='Superior College Muslim Town - Canal Campus').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)               
                elif degree == 'ICOM' and min_score >= 600:
                  specific_college =GirlsCollege.objects.filter(name='Superior College Muslim Town - Canal Campus').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)    



                if degree == 'FSC(eng)' and min_score >= 650 :
                  specific_college = GirlsCollege.objects.filter(name='Govt.Postgraduate College(W) Samanabad Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=680 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt.Postgraduate College(W) Samanabad Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 690 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt.Postgraduate College(W) Samanabad Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 560 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt.Postgraduate College(W) Samanabad Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 500 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt.Postgraduate College(W) Samanabad Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 450 :
                  specific_college = GirlsCollege.objects.filter(name='Govt.Postgraduate College(W) Samanabad Lahore').first()
                  recommended_colleges = list(recommended_colleges) 
                  recommended_colleges.append(specific_college)     
                


                if degree == 'FSC(eng)' and min_score >= 633 :
                  specific_college = GirlsCollege.objects.filter(name='Govt College For Women Township Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >= 650 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt College For Women Township Lahore').first()
                  recommended_colleges = list(recommended_colleges)
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 600 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt College For Women Township Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 509 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt College For Women Township Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 500 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt College For Women Township Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 450 :
                  specific_college = GirlsCollege.objects.filter(name='Govt College For Women Township Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)  
                

                if degree == 'FSC(eng)' and min_score >= 590 :
                  specific_college = GirlsCollege.objects.filter(name='Govt Degree College for Women Gawalmandi Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'FSC(med)' and min_score >=595 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt Degree College for Women Gawalmandi Lahore').first()
                  recommended_colleges = list(recommended_colleges)
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Phyics)' and min_score >= 560 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt Degree College for Women Gawalmandi Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICS(Statistics)' and min_score >= 471 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt Degree College for Women Gawalmandi Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)
                elif degree == 'ICS(Ecnomics)' and min_score >= 440 :
                  specific_college =  GirlsCollege.objects.filter(name='Govt Degree College for Women Gawalmandi Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college) 
                elif degree == 'ICOM' and min_score >= 410 :
                  specific_college = GirlsCollege.objects.filter(name='Govt Degree College for Women Gawalmandi Lahore').first()
                  recommended_colleges = list(recommended_colleges)  
                  recommended_colleges.append(specific_college)  
                                              
                    


               

                
               


    else:
        form = StudentPreferencesForm()

    recommended_colleges_list = list(recommended_colleges)    






    return render(request, 'recomment/recommendation.html' ,{'form': form, 'recommended_colleges': recommended_colleges_list})





