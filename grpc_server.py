import grpc
from concurrent import futures
import csv_pb2_grpc as pb2_grpc
import csv_pb2 as pb2

import csv

csv_file_path = "kwh_hourly_dataset_stacked.csv"

row_number = 1

class csvEngine(pb2_grpc.csvEngineServicer):
    def __init__(self, *args, **kwargs):
        pass

    def get_next_row(self, request, context):
        global row_number
        with open(csv_file_path, "r") as file:
            csv_reader = csv.reader(file)
            
            for i, row in enumerate(csv_reader):
                if i == row_number:
                    res = {
                         "id": int(row[0]),
                         "houseID": row[1],
                         "Year" : int(row[2]),
                         "Month" : int(row[3]),
                         "DayOfYear" : int(row[4]),
                         "Date" : row[5],
                         "Weekday" : int(row[6]),
                         "Hour" : int(row[7]),
                         "Energy" : float(row[8])
                    }
                    row_number=row_number+1
                    return pb2.dataSetRow(**res)
            

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_csvEngineServicer_to_server(csvEngine(), server)
    server.add_insecure_port('[::]:5010')
    server.start()
    server.wait_for_termination()

