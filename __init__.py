import collections
Dataset_Info = collections.namedtuple("Dataset_Info", 'data_file test_data_file categories')
class PATH(object):
    def __init__(self):
        self.Hidden_AUs = ['AU5', 'AU9', 'AU14', 'AU16', 'AU17']
        self.ABAW3 = Dataset_Info(data_file = None, test_data_file=None,
            categories= {'AU': ['AU1','AU2','AU4','AU6','AU7','AU10','AU12','AU15','AU23','AU24','AU25','AU26'],
            'EXPR': ['Neutral','Anger','Disgust','Fear','Happiness','Sadness','Surprise','Other'],
            'VA': ['valence', 'arousal']})

        
