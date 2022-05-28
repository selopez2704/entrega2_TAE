from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from numpy import double
from RiesgoCredito.modelo import prediccion_riesgo
from RiesgoCredito.utils import valor

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def model(request):
    if request.GET:
        term = request.GET.get('term', '')
        int_rate = request.GET.get('int_rate', '')
        grade = request.GET.get('grade', '')
        emp_length = request.GET.get('emp_length', '')
        home_ownership = request.GET.get('home_ownership', '')
        annual_inc = request.GET.get('annual_inc', '')
        verification_status = request.GET.get('verification_status', '')
        purpose = request.GET.get('purpose', '')
        dti = request.GET.get('dti', '')
        inq_last_6mths = request.GET.get('inq_last_6mths', '')
        revol_util = request.GET.get('revol_util', '')
        total_acc = request.GET.get('total_acc', '')
        out_prncp = request.GET.get('out_prncp', '')
        total_pymnt = request.GET.get('total_pymnt', '')
        total_rec_int = request.GET.get('total_rec_int', '')
        last_pymnt_amnt = request.GET.get('last_pymnt_amnt', '')
        tot_cur_bal = request.GET.get('tot_cur_bal', '')
        total_rev_hi_lim = request.GET.get('total_rev_hi_lim', '')
        mths_since_earliest_cr_line = request.GET.get('mths_since_earliest_cr_line', '')
        mths_since_issue_d = request.GET.get('mths_since_issue_d', '')
        mths_since_last_pymnt_d = request.GET.get('mths_since_last_pymnt_d', '')
        mths_since_last_credit_pull_d = request.GET.get('mths_since_last_credit_pull_d', '')
        grade_A = valor("grade_A",grade)
        grade_B = valor("grade_B",grade)
        grade_C = valor("grade_C",grade)
        grade_D = valor("grade_D",grade)
        grade_E = valor("grade_E",grade)
        grade_F = valor("grade_F",grade)
        grade_G = valor("grade_G",grade)
        home_ownership_MORTGAGE = valor("home_ownership_MORTGAGE",home_ownership)
        home_ownership_NONE = valor("home_ownership_NONE",home_ownership)
        home_ownership_OTHER = valor("home_ownership_OTHER",home_ownership)
        home_ownership_OWN = valor("home_ownership_OWN",home_ownership)
        home_ownership_RENT = valor("home_ownership_RENT",home_ownership)
        verification_status_Not_Verified = valor("verification_status_Not_Verified",verification_status)
        verification_status_Source_Verified = valor("verification_status_Source_Verified",verification_status)
        verification_status_Verified = valor("verification_status_Verified",verification_status)
        purpose_car= valor('purpose_car',purpose)
        purpose_credit_card= valor('purpose_credit_card',purpose)
        purpose_debt_consolidation= valor('purpose_debt_consolidation',purpose)
        purpose_educational= valor('purpose_educational',purpose)
        purpose_home_improvement= valor('purpose_home_improvement',purpose)
        purpose_house= valor('purpose_house',purpose)
        purpose_major_purchase= valor('purpose_major_purchase',purpose)
        purpose_medical= valor('purpose_medical',purpose)
        purpose_moving= valor('purpose_moving',purpose)
        purpose_other= valor('purpose_other',purpose)
        purpose_renewable_energy= valor('purpose_renewable_energy',purpose)
        purpose_small_business= valor('purpose_small_business',purpose)
        purpose_vacation= valor('purpose_vacation',purpose)
        purpose_wedding= valor('purpose_wedding',purpose)
        
        
        dic={
                'term': int(term),
                'int_rate': float(int_rate),
                'grade': str(grade),
                'emp_length':float(emp_length),
                'home_ownership': str(home_ownership),
                'annual_inc': float(annual_inc),
                'verification_status': str(verification_status),
                'purpose': str(purpose),
                'dti': float(dti),
                'inq_last_6mths': float(inq_last_6mths),
                'revol_util': float(revol_util),
                'total_acc': float(total_acc),
                'out_prncp': float(out_prncp),
                'total_pymnt': float(total_pymnt),
                'total_rec_int': float(total_rec_int),
                'last_pymnt_amnt': float(last_pymnt_amnt),
                'tot_cur_bal': float(tot_cur_bal),
                'total_rev_hi_lim': float(total_rev_hi_lim),
                'mths_since_earliest_cr_line': float(mths_since_earliest_cr_line),
                'mths_since_issue_d': float(mths_since_issue_d),
                'mths_since_last_pymnt_d':float(mths_since_last_pymnt_d),
                'mths_since_last_credit_pull_d': float(mths_since_last_credit_pull_d),
                'grade:A': grade_A,
                'grade:B': grade_B,
                'grade:C': grade_C,
                'grade:D': grade_D,
                'grade:E': grade_E,
                'grade:F': grade_F,
                'grade:G': grade_G,
                'home_ownership:MORTGAGE': home_ownership_MORTGAGE,
                'home_ownership:NONE': home_ownership_NONE,
                'home_ownership:OTHER': home_ownership_OTHER,
                'home_ownership:OWN': home_ownership_OWN,
                'home_ownership:RENT': home_ownership_RENT,
                'verification_status:Not Verified': verification_status_Not_Verified,
                'verification_status:Source Verified': verification_status_Source_Verified,
                'verification_status:Verified': verification_status_Verified,
                'purpose:car': purpose_car,
                'purpose:credit_card': purpose_credit_card,
                'purpose:debt_consolidation': purpose_debt_consolidation,
                'purpose:educational': purpose_educational,
                'purpose:home_improvement': purpose_home_improvement,
                'purpose:house': purpose_house,
                'purpose:major_purchase': purpose_major_purchase,
                'purpose:medical': purpose_medical,
                'purpose:moving': purpose_moving,
                'purpose:other': purpose_other,
                'purpose:renewable_energy': purpose_renewable_energy,
                'purpose:small_business': purpose_small_business,
                'purpose:vacation': purpose_vacation,
                'purpose:wedding': purpose_wedding,
            }
        respuesta=prediccion_riesgo(dic)*100
    return redirect('../respuesta/'+str(respuesta))

def respuesta(request,respuesta):
    context={
        'respuesta':respuesta,
    }
    return render(request, 'respuesta.html', context)
def informe(request):
    template = loader.get_template('informe.html')
    return HttpResponse(template.render())