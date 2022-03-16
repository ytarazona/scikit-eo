# -*- coding: utf-8 -*-
# +
import numpy as np
import pandas as pd
from dbfread import DBF
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier as DT
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.naive_bayes import GaussianNB as GNB
from sklearn.neural_network import MLPClassifier as MLP
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

class calmla(object):
    
    ''' **Calibrating supervised classification in Remote Sensing**
    
    This module allows to calibrate supervised classification in satellite images
    through various algorithms and using approaches such as Set-Approach, 
    Leave-One-Out Cross-Validation (LOOCV), Cross-Validation (k-fold) and 
    Monte Carlo Cross-Validation (MCCV)'''
    
    def __init__(self, endmembers):
        
        '''
        Parameter:
            
            endmembers: Endmembers must be a matrix (numpy.ndarray) and with more than one endmember. 
                    Rows represent the endmembers and columns represent the spectral bands.
                    The number of bands must be equal to the number of endmembers.
                    E.g. an image with 6 bands, endmembers dimension should be $n*6$, where $n$ 
                    is rows with the number of endmembers and 6 is the number of bands 
                    (should be equal).
                    In addition, Endmembers must have a field (type int or float) with the names 
                    of classes to be predicted.
        
        '''
        
        self.endm = endmembers
        
        # if it is read by pandas.read_csv()
        if isinstance(self.endm, (pd.core.frame.DataFrame)):
            
            for i in np.arange(self.endm.shape[1]):
                
                if all(self.endm.iloc[:,int(i)] < 100) & all(self.endm.iloc[:,int(i)] >= 1): indx = i; break
        
        # if the file is .dbf    
        elif isinstance(self.endm, (DBF)): # isinstance() function With Inheritance
            
            self.endm = pd.DataFrame(iter(self.endm))
            
            for i in np.arange(self.endm.shape[1]):
                
                if all(self.endm.iloc[:,int(i)] < 100) & all(self.endm.iloc[:,int(i)] >= 1): indx = i; break
        
        else:
            raise TypeError('"endm" must be .csv (pandas.core.frame.DataFrame).')
        
        self.indx = indx
        
        
    def splitData(self, random_state = None):
        
        ''' This method is to separate the dataset in predictor variables and the variable 
        to be predicted.
        
        Parameter:
            
            self: Attributes of class calmla.
        
        Return:
            A dictionary with X and y.
        '''
        
        # removing the class column
        X = self.endm.drop(self.endm.columns[[self.indx]], axis = 1)
        
        # only predictor variables
        y = self.endm.iloc[:, self.indx]
        
        Xy_data = {'X': X, 'y': y}
        
        return Xy_data
    
    # Set-Approach
    
    def SA(self, split_data, models = ('svm', 'dt', 'rf'), train_size = 0.5, n_iter = 10, **kwargs):
        
        '''
        This module allows to calibrate supervised classification in satellite images 
        through various algorithms and using approaches such as Set-Approach.
        
        Parameters:
        
            split_data: A dictionary obtained from the *splitData* method of this package.
            
            models: Models to be used such as Support Vector Machine ('svm'), Decision Tree ('dt'),
            Random Forest ('rf'), Naive Bayes ('nb') and Neural Networks ('nn'). This parameter
            can be passed like models = ('svm', 'dt', 'rf', 'nb', 'nn').
            
            train_size: For splitting samples into two subsets, i.e. training data and 
            for testing data.
            
            n_iter: Number of iterations, i.e number of times the analysis is executed.
            
            **kwargs:
            
        Return:
            
        '''
        svm_error_sa = []
        dt_error_sa = []
        rf_error_sa = []
        nb_error_sa = []
        nn_error_sa = []
        
        for i in range(n_iter):
            
            # split in training and testing
            Xtrain, Xtest, ytrain, ytest = train_test_split(split_data.get('X'), 
                                                            split_data.get('y'), 
                                                            train_size = train_size, 
                                                            test_size = 1 - train_size, 
                                                            random_state = None)
            if 'svm' in models:
                # applying a support vector machine
                inst_svm = SVC(**kwargs)
        
                # model trained
                mt_svm = inst_svm.fit(Xtrain, ytrain)
        
                # Confusion matrix
                predic_Xtest = mt_svm.predict(Xtest)
        
                oa = accuracy_score(ytest, predic_Xtest)
                svm_error_sa.append(1 - oa)
            
            if 'dt' in models:
                # applying a support vector machine
                inst_dt = DT(**kwargs)
        
                # model trained
                mt_dt = inst_dt.fit(Xtrain, ytrain)
        
                # Confusion matrix
                predic_Xtest = mt_dt.predict(Xtest)
        
                oa = accuracy_score(ytest, predic_Xtest)
                dt_error_sa.append(1 - oa)
            
            if 'rf' in models:
                # applying a support vector machine
                inst_rf = RF(**kwargs)
        
                # model trained
                mt_rf = inst_rf.fit(Xtrain, ytrain)
        
                # Confusion matrix
                predic_Xtest = mt_rf.predict(Xtest)
        
                oa = accuracy_score(ytest, predic_Xtest)
                rf_error_sa.append(1 - oa)
            
            if 'nb' in models:
                # applying a support vector machine
                inst_nb = GNB(**kwargs)
        
                # model trained
                mt_nb = inst_nb.fit(Xtrain, ytrain)
        
                # Confusion matrix
                predic_Xtest = mt_nb.predict(Xtest)
        
                oa = accuracy_score(ytest, predic_Xtest)
                nb_error_sa.append(1 - oa)
            
            if 'nn' in models:
                # applying a support vector machine
                inst_nn = MLP(**kwargs)
        
                # model trained
                mt_nn = inst_nn.fit(Xtrain, ytrain)
        
                # Confusion matrix
                predic_Xtest = mt_nn.predict(Xtest)
        
                oa = accuracy_score(ytest, predic_Xtest)
                nn_error_sa.append(1 - oa)
            
            
            dic = {'svm': svm_error_sa,
                  'dt': dt_error_sa,
                  'rf': rf_error_sa,
                  'nb': nb_error_sa,
                  'nn': nn_error_sa}

            all_models = ('svm', 'dt', 'rf', 'nb', 'nn')

            for model in all_models:
                if model not in models:
                    del dic[model]
                    
        errors_setApproach = dic
        
        return errors_setApproach 
        
        
    # LOOCV
    
    def LOOCV():
        pass
    
    # CV
    
    def CV():
        pass
    
    # MCCV
    
    def MCCV():
        pass