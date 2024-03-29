import sys
import asyncio
import aiohttp
import time
import aiofiles

async def get_file(url, session, start_time):
    async with session.get(url,ssl=False) as response:
        if response.status == 200:
            filename = url.split('/')[-1]
            async with aiofiles.open(filename, 'wb') as f:
                content = await response.read()
                await f.write(content)
                print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")
        else:
            print(f"Failed to download {url}: HTTP status code {response.status}")


async def main(urls):
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        tasks = [get_file(url, session, start_time) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
    else:
        urls = [
            'https://images.hdqwalls.com/download/sunset-tree-red-ocean-sky-7w-2880x1800.jpg',
            'https://images.hdqwalls.com/download/mountain-reflection-in-lake-image-2880x1800.jpg',
            'https://images.hdqwalls.com/download/mountain-kingdom-2880x1800.jpg'
        ]

    asyncio.run(main(urls))