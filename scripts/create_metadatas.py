import json
# url for images on pinata
baseUrl = "https://gateway.pinata.cloud/ipfs/QmTue2nCLt7EkERnqAe6hFeN5JNj6AatMuphFt74K6NeUT/"
path_to_metadata_folder = "C:\\Users\\Arthur\\OneDrive\\Documents\\cours\\5A\\Cybersecurity\\NFT_project\\metadatas\\generated_images_metadatas\\"
path_to_empty_metadata = "C:\\Users\\Arthur\\OneDrive\\Documents\\cours\\5A\\Cybersecurity\\NFT_project\\metadatas\\empty_metadatas.json"

# Opening JSON file
f = open(path_to_empty_metadata)
  
# returns JSON object as 
# a dictionary
metadata = json.load(f)

with open('accessories.txt') as file:
    for i, line in enumerate(file):
      name = line[:-1]

      metadata['image'] = baseUrl + f'{i}.png'
      metadata['name'] = name.capitalize() + ' duck'

      # create and save json file
      with open(f'{path_to_metadata_folder}{i}.json', 'w') as json_file:
        json.dump(metadata, json_file)