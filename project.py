//google-images-using-python
//importing google_images_download module
from google_images_download import google_images_download

//creating object
response = google_images_download.googleimagesdownload()

search_queries = [
'The smartphone also features an in display fingerprint sensor.', 'The pop up selfie camera is placed aligning with the rear cameras.', '''In terms of storage Vivo V15 Pro could offer up to 6GB of RAM and 128GB of onboard storage.''', 'The smartphone could be fuelled by a 3 700mAh battery.', ]

def downloadimages(query):

  arguments = {"keywords": query, 
               "format": "jpg", 
               "limit":4, 
               "print_urls":True, 
               "size": "medium", 
               "aspect_ratio: panoramic"} 
try: 
    response.download(arguments) 
  
# Handling File NotFound Error     
except FileNotFoundError:  
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit":4, 
                 "print_urls":True,  
                 "size": "medium"} 
                   
    # Providing arguments for the searched query 
    try: 
        # Downloading the photos based 
        # on the given arguments 
        response.download(arguments)  
    except: 
        pass
//Driver Code
for query in search_queries: downloadimages(query)
print()
