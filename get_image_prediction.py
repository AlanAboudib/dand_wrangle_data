import requests

# get the file data
r = requests.get('https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv')

# save the data to a file
filename = 'image_predictions.tsv'

with open(filename, 'wb') as f:

    for chunk in r.iter_content(chunk_size = 128):
        f.write(chunk)
