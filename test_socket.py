import asyncio
import json

async def main(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    writer.write(0x1)
    data = await reader.read(100)
    print(f'Received: {data.decode()}')
    writer.close()

address = input()
port = int(input())

asyncio.run(main(address, port))