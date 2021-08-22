import pandas as pd
from scipy.sparse import csr_matrix
import numpy as np

from lightfm.cross_validation import random_train_test_split
from lightfm.evaluation import auc_score, precision_at_k, recall_at_k
from lightfm import LightFM
import random

med_data = pd.read_csv('df.csv', sep = ',')
med_data = med_data.sort_values('date').reset_index().drop('Unnamed: 0', axis=1)

med_data['procedure'].replace(np.nan, -1, inplace=True)
med_data['procedure'] = pd.to_numeric(med_data['procedure'])
med_data['procedure'] = pd.cut(med_data['procedure'], bins=25)

med_data['scores'] = med_data['scores'].apply(lambda x: round(x*2)/2)
med_data['scores'] = pd.qcut(med_data['scores'], 25)
med_data['doc_spec'].replace(np.nan, 'unknown', inplace=True)
med_data['price'].replace(np.nan, -1, inplace=True)
med_data['m'] = med_data.m.map(
    lambda x: 1.0*(x == 'true'))

med_data = med_data.fillna(0)

med_data_fixed = med_data.loc[med_data['scores'] == 1, ['user_id', 'order_id', 'price']]

med_data_fixed = med_data_fixed[med_data_fixed['user_id'].isin(random.sample(list(med_data_fixed['user_id'].unique()), 
                                                                                                  k=5000))]

med_data_fixed['m'] = random_train_test_split(1, 100, med_data_fixed.shape[0])
med_data_dum = pd.get_dummies(med_data_fixed, columns = ['m', 'doc_spec', 'price', 'scores', 'procedure'])

med_data_csr = csr_matrix(med_data_dum.values)

model = LightFM(loss = 'warp')
model.fit(med_data_csr['train'], epochs=30, num_threads=2)

def fooo(model, data, user_ids):
    n_items = data['train'].shape
    for user_id in user_ids:
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
        scores = model.predict(user_id, np.arange(n_items))
        top_items = data['item_labels'][np.argsort(-scores)]
        response = "Top:     "

        for x in known_positives[:3]:
            response = response + str("        %s" % x)

        response = response + "     Recommended:"
        for x in top_items[:3]:
            response = response + str("        %s" % x)

    return response
            