import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix, precision_recall_curve, auc
from sklearn.feature_selection import f_classif
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from scipy.stats import chi2_contingency
import pickle
from RiesgoCredito import WoE_Binning   
import dill

def prediccion_riesgo(dic):
    #Remoto
    modelo= dill.load(open("\modelo\model.pkl", "rb"))
    #local
    #modelo= dill.load(open("RiesgoCredito\modelo\model.pkl", "rb"))
    data=pd.DataFrame(data=dic,index=[0])
    prediccion=modelo.predict_proba(data)
    return prediccion[0][1]

