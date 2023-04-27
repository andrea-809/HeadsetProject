from cortex import Cortex

#import serial
import time
import json
from datetime import datetime

dict = {}
cont = 0
glob = 0

class Subcribe():

    # A class to subscribe data stream.
    def __init__(self):
        """
        Constructs cortex client and bind a function to handle subscribed data streams
        If you do not want to log request and response message , set debug_mode = False. The default is True
        met è quello che usiamo, data e pow potrebbero essere utili
        """   
        self.c = Cortex(user, debug_mode=True)
        self.c.bind(new_data_labels=self.on_new_data_labels)
        self.c.bind(new_met_data=self.on_new_met_data)
        self.c.bind(new_pow_data=self.on_new_pow_data)

    def do_prepare_steps(self):
        """
        Do prepare steps before training.
        Step 1: Connect a headset. For simplicity, the first headset in the list will be connected in the example.
                If you use EPOC Flex headset, you should connect the headset with a proper mappings via EMOTIV Launcher first 
        Step 2: requestAccess: Request user approval for the current application for first time.
                       You need to open EMOTIV Launcher to approve the access
        Step 3: authorize: to generate a Cortex access token which is required parameter of many APIs
        Step 4: Create a working session with the connected headset
        Returns
        -------
        None
        """
        self.c.do_prepare_steps()

    def sub(self, streams):
        """
        To subscribe to one or more data streams
        'met' : Performance metric
        'pow' : Band power

        Parameters
        ----------
        streams : list, required
            list of streams. For example, ['met', 'pow']

        Returns
        -------
        None
        """
        self.c.sub_request(streams)

    def on_new_data_labels(self, *args, **kwargs):
        """
        To handle data labels of subscribed data 
        Returns
        -------
        data: list  
              array of data labels
        name: stream name
        For example:
            met : ['eng.isActive', 'eng', 'exc.isActive', 'exc', 'lex', 'str.isActive', 'str', 'rel.isActive', 'rel', 'int.isActive', 'int', 'foc.isActive', 'foc']
            pow: ['AF3/theta', 'AF3/alpha', 'AF3/betaL', 'AF3/betaH', 'AF3/gamma', 'T7/theta', 'T7/alpha', 'T7/betaL', 'T7/betaH', 'T7/gamma', 'Pz/theta', 'Pz/alpha', 'Pz/betaL', 'Pz/betaH', 'Pz/gamma', 'T8/theta', 'T8/alpha', 'T8/betaL', 'T8/betaH', 'T8/gamma', 'AF4/theta', 'AF4/alpha', 'AF4/betaL', 'AF4/betaH', 'AF4/gamma']
        """
        data = kwargs.get('data')
        stream_name = data['streamName']
        stream_labels = data['labels']
        
       
    def on_new_met_data(self, *args, **kwargs):
        """
        To handle performance metrics data emitted from Cortex

        Returns
        -------
        data: dictionary
             The values in the array met match the labels in the array labels return at on_new_data_labels
        For example: {'met': [True, 0.5, True, 0.5, 0.0, True, 0.5, True, 0.5, True, 0.5, True, 0.5], 'time': 1627459390.4229}
        per leggere: 
        data = kwargs.get('data')
        #print(data["met"][N])
        N: 1 = engagement, 8 = relax, 12 = focus

        """

        global cont
        data = kwargs.get('data')
        print(data)
        dict[str(cont).zfill(5)] = data
        cont += 1
        #opens results file
        result_file = open('met_res.json', 'w')
        json_object = json.dump(dict, result_file)
        #closes results file
        result_file.close()
        
    
    def on_new_pow_data(self, *args, **kwargs):
        """
        To handle performance metrics data emitted from Cortex

        Returns
        -------
        data: dictionary
             The values in the array met match the labels in the array labels return at on_new_data_labels
        For example: {'met': [True, 0.5, True, 0.5, 0.0, True, 0.5, True, 0.5, True, 0.5, True, 0.5], 'time': 1627459390.4229}
        per leggere: 
        data = kwargs.get('data')
        #print(data["met"][N])
        N: 1 = engagement, 8 = relax, 12 = focus

        """
        data = kwargs.get('data')
        
        global glob
        
        print(data)
        dict[str(glob).zfill(5)] = data
        glob += 1
        #opens results file
        result_file = open('pow_res.json', 'w')
        json_object = json.dump(dict, result_file)
        #closes results file
        result_file.close()
 

user = {
    "license" : "",
    "client_id" :  "gTEWtIiUySDg11fFfB2l6Kq5gY4jZ9u7mWx2LuA4",
    "client_secret" : "QxZKdeY1hdPB8qP1aHFFshkHuePznA89KujGYBmtm3gIGvKtrhD96DDePO9v2xiyucmRAQFnf8i1drtfH7N6ctMbEnt47kEcaBJdoTJmSHv7er4ARskSsCn2umYDDgEZ",
    "debit" : 100
}

s = Subcribe()

# Do prepare steps
s.do_prepare_steps()

# sub multiple streams
# streams = ['met','pow']

# or only sub for one
streams = ['met', 'pow']

s.sub(streams)

# -----------------------------------------------------------

