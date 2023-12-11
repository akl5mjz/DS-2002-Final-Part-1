#import modules
import aiohttp
import asyncio
import sqlite3
from datetime import datetime, timedelta

#create async functions that waits a full minute before collecting data
async def wait1Minute():
    print("Waiting for 1 minute...")
    await asyncio.sleep(60)
    print("1 minute passed, now executing.")

#Create async function that pulls from our api
async def getApiData():
    apiUrl = 'https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi'
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(apiUrl) as response:
            data = await response.json()
            return data

#create async function that takes the json response from api and puts it into a database
async def insertDataIntoDatabase(cursor, data):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS api_data (
            id INTEGER PRIMARY KEY,
            factor INTEGER,
            pi REAL,
            time TEXT
        )
    ''')
    cursor.execute('INSERT INTO api_data (factor, pi, time) VALUES (?, ?, ?)',
                   (data['factor'], data['pi'], data['time']))

#create main function that runs for the full hour
async def main():
    connection = sqlite3.connect('api_data.db')
    database = connection.cursor()
    for _ in range(60):
        await wait1Minute()
        current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        data = await getApiData()
        await insertDataIntoDatabase(database, {**data, 'time': current_time})
        connection.commit()
    connection.close()

#run program
if __name__ == "__main__":
    asyncio.run(main())