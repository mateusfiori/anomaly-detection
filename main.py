from luminol.anomaly_detector import AnomalyDetector
from datetime import datetime
import pandas as pd

def parseTs(dataArray): 
    dataDict = dict()
    for i in dataArray:
        dataDict[datetime.strptime(i[0], '%Y-%m-%d %H:%M:%S.%f').strftime('%s')] = i[1]
    return dataDict 

def formatAnomalies(anomalies):
    return [[anomaly.exact_timestamp, anomaly.anomaly_score] for anomaly in anomalies]

def formatResult(anomalies, timeseriesDict):
    print(f'Foram encontradas {len(anomalies)} anomalias na sua série temporal.\n')
    for anomaly in anomalies:
        print(f'No timestamp {datetime.fromtimestamp(anomaly[0])} com um score de {anomaly[1]} e valor {timeseriesDict[str(anomaly[0])]}')

timeseriesDict = parseTs(pd.read_csv('./data/data.csv').values)
formatResult(formatAnomalies(AnomalyDetector(timeseriesDict).get_anomalies()), timeseriesDict)