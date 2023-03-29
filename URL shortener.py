import pyshorteners
x=input("enter the Url link : ")
y=pyshorteners.Shortener()
z=y.tinyurl.short(x)
print(f"old Url is this : {x}")
print(f"new Url is this : {z}")


# import requests

# def shorten_url(url):
#     # Replace <YOUR_API_KEY> with your actual FLEX API key
#     api_key = "82e32acf2f349e3e44605440b1a435e619d91f00"
#     endpoint = "https://api-ssl.bitly.com/v4/shorten"

#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {api_key}"
#     }

#     data = {
#         "domain": "yourdomain.com",  # Replace with your custom domain (if you have one)
#         "originalURL": url,
#         "title": "Shortened URL"  # Replace with a title for your shortened URL
#     }

#     response = requests.post(endpoint, json=data, headers=headers)
#     if response.status_code == 200:
#         return response.json()["shortURL"]
#     else:
#         return None


# long_url = "https://www.example.com/very/long/url/that/you/want/to/shorten"
# short_url = shorten_url(long_url)
# print(short_url)


# import bitly_api

# BITLY_ACCESS_TOKEN ="82e32acf2f349e3e44605440b1a435e619d91f00"

# b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

# response = b.shorten('http://google.com/')
# print(response)

