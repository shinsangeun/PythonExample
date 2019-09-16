# 데이터를 저장하고 불러오기_pickle
import pickle

data={
    'a': [1,2.0,3,4+6j],
    'b': ("Character string",b"byte string"),
    'c': {None, True, False}
}

# save
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

#load
with open('data.pickle', 'rb') as f:
    data=pickle.load(f)