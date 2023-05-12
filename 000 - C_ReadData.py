from asyncio.windows_events import NULL
from cortex import Cortex
import serial
import time
from datetime import datetime

#variabili globali: 
#   arduino, selezionare porta e baud rate corrispondenti
#   rwPath e fileName per selezionare la cartella e il file da inserire

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
rwPath = 'C:\Cerio\Arduino\Hackathon\BrainData'
#rwPath = 'C:\Users\Cerio\OneDrive - Politecnico di Milano\Hackatentativo\BrainData'

MfileName = 'MetData.txt'
PfileName = 'PowData.txt'
useFile = True
descrizioneEsperimento = ''

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
        print('{} labels are : {}'.format(stream_name, stream_labels))
        if stream_name == 'met':
            file = open(rwPath+'\\'+ MfileName,"a")
            file.writelines('Metrics:,' + stream_labels[1] + ',' + stream_labels[3] + ',' + stream_labels[4] + ',' + stream_labels[6] +
                      ',' + stream_labels[8] + ',' + stream_labels[10] + ',' + stream_labels[12] + "\n");
            file.write(descrizioneEsperimento + "\n")
            file.write('Reading begins:,' + datetime.now().strftime("%d/%m/%Y") + "\n")

            file.close()
        else:
            file = open(rwPath+'\\'+ PfileName,"a")
            file.write(descrizioneEsperimento + "\n")
            file.write('Reading begins:,' + datetime.now().strftime("%d/%m/%Y") + "\n")
            joined_string = "Waves:," + ",".join(stream_labels)
            file.writelines(joined_string + "\n");
            file.close()
        
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
        data = kwargs.get('data')
        if data["met"][0] & data["met"][2] & data["met"][5] & data["met"][7] & data["met"][9] & data["met"][11]:
            eng = data["met"][1]
            exc = data["met"][3]
            lex = data["met"][4]
            stress = data["met"][6]
            rel = data["met"][8]
            intrst = data["met"][10]
            foc = data["met"][12]
            print(data)
            if useFile:
                file = open(rwPath+'\\'+ MfileName,"a")

                #file.write(datetime.now().strftime("%H:%M:%S: ") + str(round(eng,5)) + "        " +
                #         str(round(exc,5)) + "        " + str(round(lex,5)) + str(round(stress,5)) + "        " + str(round(rel,5)) + "        " +
                #         str(round(intrst,5)) + "        " +str(round(foc,5)) + "        " + "\n")
                file.write(datetime.now().strftime("%H:%M:%S ") + ',' + str(round(eng,5)) + "," + str(round(exc,5)) + "," + str(round(lex,5)) + "," + 
                        str(round(stress,5)) + "," + str(round(rel,5)) + "," + str(round(intrst,5)) + "," +str(round(foc,5)) + "\n")

                file.close()
            dataSend(foc)


    def on_new_pow_data(self, *args, **kwargs):
        """
        To handle band power data emitted from Cortex

        Returns
        -------
        data: dictionary
             The values in the array pow match the labels in the array labels return at on_new_data_labels
        For example: {'pow': [5.251, 4.691, 3.195, 1.193, 0.282, 0.636, 0.929, 0.833, 0.347, 0.337, 7.863, 3.122, 2.243, 0.787, 0.496, 5.723, 2.87, 3.099, 0.91, 0.516, 5.783, 4.818, 2.393, 1.278, 0.213], 'time': 1627459390.1729}
        """
        data = kwargs.get('data')
        #print('pow data: {}'.format(data))
        if useFile:
            file = open(rwPath+'\\'+ PfileName,"a")
            converted_List = [str(element) for element in data['pow']]
            file.write(datetime.now().strftime("%H:%M:%S ") + ', ' + ",".join(converted_List) + "\n")

            file.close()
   


# -----------------------------------------------------------
# 
# SETTING
#   - replace your license, client_id, client_secret to user dic
#   - specify infor for record and export
#   - connect your headset with dongle or bluetooth, you should saw headset on EmotivApp
# SUBSCRIBE
#     you need to folow steps:
#         1) do_prepare_steps: for horization, connect headset and create working session.
#         2) sub(): to subscribe data, you can subscribe one stream or multiple streams
# RESULT
#   - the data labels will be retrieved at on_new_data_labels
#   - the data will be retreived at on_new_[dataStream]_data
# 
# ---------------------te--------------------------------------


#ricevi input e leggi output da arduino
def dataSend(x):
    newData = round((x+0.35)*255);
    if newData > 255:
        newData = 255;
    print(newData)
    arduino.write(bytes(str(newData), 'utf-8'))


user = {
    "license" : "",
    "client_id" : "",
    "client_secret" : "",
    "debit" : 100
}

s = Subcribe()

# Do prepare steps
s.do_prepare_steps()

# sub multiple streams
# streams = ['met','pow']

# or only sub for one
streams = ['met', 'pow']
#streams = ['met']
if useFile:
    descrizioneEsperimento = input("Descrizione esperimento:")
    #file = open(rwPath+'\\'+ MfileName,"a")
    #file.write(val + "\n")
    #file.write('Reading begins:,' + datetime.now().strftime("%d/%m/%Y") + "\n")
    #file.close()
    #file = open(rwPath+'\\'+ PfileName,"a")
    #file.write(val + "\n")
    #file.write('Reading begins:' + datetime.now().strftime("%d/%m/%Y") + "\n")
    #file.close()

s.sub(streams)
# -----------------------------------------------------------
