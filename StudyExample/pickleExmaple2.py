# pickle로 저장된 데이터를 압축하고 해제_gzip
import pickle
import gzip

data = {
    'a': [1,2.0,3,4+6j],
    'b': ("charcter string", b"byte string"),
    'c': {None, True, False}
}

#save and compress
with gzip.open('testPickleFile.pickle','wb') as f:
    pickle.dump(data, f)

#load
with gzip.open('testPickleFile.pickle','rb') as f:
    data = pickle.load(f)