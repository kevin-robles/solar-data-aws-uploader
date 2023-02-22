import boto3
import pandas as pd
import os
import uuid
import pathlib as pl


# AWS configurations
#AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
#AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
FIREHOSE_STREAM_NAME = 'TestSolarStream'

base_dir = pl.Path(__file__).parent

file_data_path = "2011024137-2023-02-09,2023-02-09.xlsx"

# Specify the header names to be read from the excel file
headers = ['Sn', 'Time', 'batChargeToday(kWh)/70', 'batDischargeToday(kWh)/71',
          'gridBuyToday(kWh)/76', 'gridSellToday(kWh)/77', 'dailyUsed(kWh)/84',
          'pvetoday(kWh)/108', 'acTotalPower(W)/169', 'invTotalPower(W)/175',
          'loadTotalPower(W)/178', 'batteryEnergy(%)/184', 'batteryPower(W)/190']

new_cols = ["SerialNumber","Time", "BatteryChargedToday", "BatteryDischargedToday",
            "GridBuyToday", "GridSellToday", "UsageInDay", "SolarProductionToday",
            "LiveAcPower", "LiveInverterPower", "LiveLoadTotalPower", "LiveBatteryEnergyPercent",
            "LiveBatteryPower"]


# read data from an excel file
df = pd.read_excel(os.path.join(base_dir, 'data', file_data_path), header=2, usecols=headers)
df.columns = new_cols
data = df.to_json(orient='records')

partition_key = str(uuid.uuid4())

# Connect to Firehose
kinesis = boto3.client('kinesis', region_name='us-east-1')

response = kinesis.put_record(StreamName=FIREHOSE_STREAM_NAME,
                        Data=data,
                        PartitionKey=partition_key)

print(response)
