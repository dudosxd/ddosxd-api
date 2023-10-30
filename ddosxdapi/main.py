import requests
import aiohttp
import json


class SydneyApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.ddosxd.ru'
        self.headers = {
            'Authorization': self.api_key
        }

    def Chat(self, model, messages):
    
        data = {
            'model': model, 
            'messages': messages
        }
        
        response = requests.post(
            f'{self.base_url}/v1/chat', 
            headers=self.headers, 
            json=data
        )
        
        try:
            return response.json()
        except:
            return {
                'status':500,
                'error':'Failed to parse json'
            }

    def Prompt(self, model, prompt):
    
        data = {
            'model': model, 
            'prompt': prompt
        }
        
        response = requests.post(
            f'{self.base_url}/v1/prompt', 
            headers=self.headers, 
            json=data
        )
        
        try:
            return response.json()
        except:
            return {
                'status':500,
                'error':'Failed to parse json'
            }


    def Imagine(
        self, 
        model, 
        prompt, 
        ar='1:1', 
        negative='Bad quality', 
        userId=0
        ):
        
        data = {
            'model': model, 
            'prompt': prompt, 
            'ar': ar, 
            'negative': negative, 
            'userId':userId
        }
        
        response = requests.post(
            f'{self.base_url}/v1/image', 
            headers=self.headers, 
            json=data
        )
        
        try:
            return response.json()
        except:
            return {
                'status':500,
                'error':'Failed to parse json'
            }

    def Moderate(self, q, filters=['nsfw']):
    
        data = {
            'q': q,
            'filters': filters
        }
        
        response = requests.post(
            f'{self.base_url}/v1/moderate', 
            headers=self.headers, 
            json=data
        )
        
        try:
            return response.json()
        except:
            return {
                'status':500,
                'error':'Failed to parse json'
            }

    def ChatStream(self, model, messages):
    
        data = {
            'model': model, 
            'messages': messages,
            'stream':True
        }
        
        response = requests.post(
            f'{self.base_url}/v1/chat', 
            headers=self.headers, 
            json=data,
            stream=True
        )

        for i in response.iter_lines():
            line = i.decode('utf-8')
            if not line: continue
            line = line[6:]
            json_data = json.loads(line)
            yield json_data
        
    def PromptStream(self, model, prompt):
    
        data = {
            'model': model, 
            'prompt': prompt,
            'stream':True
        }
        
        response = requests.post(
            f'{self.base_url}/v1/prompt', 
            headers=self.headers, 
            json=data,
            stream=True
        )

        for i in response.iter_lines():
            line = i.decode('utf-8')
            if not line: continue
            line = line[6:]
            json_data = json.loads(line)
            yield json_data


class SydneyApiAsync:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.ddosxd.ru'
        self.headers = {
            'Authorization': self.api_key
        }

    async def Chat(self, model, messages):
        data = {
            'model': model, 
            'messages': messages
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f'{self.base_url}/v1/chat', 
                headers=self.headers, 
                json=data
            ) as response:
                try:
                    return await response.json()
                except:
                    return {
                        'status':500,
                        'error':'Failed to parse json'
                    }

    async def Prompt(self, model, prompt):
        data = {
            'model': model, 
            'prompt': prompt
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f'{self.base_url}/v1/prompt', 
                headers=self.headers, 
                json=data
            ) as response:
                try:
                    return await response.json()
                except:
                    return {
                        'status':500,
                        'error':'Failed to parse json'
                    }

    async def Imagine(self, model, prompt, ar='1:1', negative='Bad quality', userId=0):
        data = {
            'model': model, 
            'prompt': prompt, 
            'ar': ar, 
            'negative': negative, 
            'userId':userId
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f'{self.base_url}/v1/image', 
                headers=self.headers, 
                json=data
            ) as response:
                try:
                    return await response.json()
                except:
                    return {
                        'status':500,
                        'error':'Failed to parse json'
                    }

    async def Moderate(self, q, filters=['nsfw']):
        data = {
            'q': q,
            'filters': filters
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f'{self.base_url}/v1/moderate', 
                headers=self.headers, 
                json=data
            ) as response:
                try:
                    return await response.json()
                except:
                    return {
                        'status':500,
                        'error':'Failed to parse json'
                    }

    async def ChatStream(self, model, messages):
        data = {
            'model': model, 
            'messages': messages,
            'stream':True
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f'{self.base_url}/v1/chat', 
                headers=self.headers, 
                json=data
            ) as response:
                async for line in response.content.iter_any():
                    line = line.decode('utf-8')
                    if not line: continue
                    line = line[6:]
                    json_data = json.loads(line)
                    yield json_data

    async def PromptStream(self, model, prompt):
        data = {
            'model': model, 
            'prompt': prompt,
            'stream':True
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f'{self.base_url}/v1/prompt', 
                headers=self.headers, 
                json=data
            ) as response:
                async for line in response.content.iter_any():
                    line = line.decode('utf-8')
                    if not line: continue
                    line = line[6:]
                    json_data = json.loads(line)
                    yield json_data
