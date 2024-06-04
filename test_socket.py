import asyncio

async def main(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    writer.write('data'.encode())
    data = await reader.read(1024)
    print(f'Received: {data.decode()}')
    writer.close()

address = input()
port = int(input())

asyncio.run(main(address, port))