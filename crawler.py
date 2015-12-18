import os, re, requests, json

def crawl(url, fileformat):
	x = requests.get(url)
	z = [y for y in x]
	z2 = ''.join(z)
	format_url = '(http[^\"|^\']+.' + fileformat + '([^\"|^\'|^\b]+)?)'
	output = re.findall(format_url , z2)
	return [x[0] for x in output]

def url_cleanup(url):
	return json.loads('"'+ url + '"')

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

def fast_dl(inputurl):
	url = url_cleanup(inputurl)
	return download_file(url)

def xrenames_f_in_dir(dirname):
	paths = (os.path.join(root, filename)
        for root, _, filenames in os.walk(dirname)
        for filename in filenames)
	for path in paths:
		regexp = '((?!.mp4\?).)'
		reoutput = re.findall(regexp, path)
		if reoutput:
			name = ''.join(reoutput) 
			name = name.replace('.mp4', '' ) + '.mp4'
			print name
			os.rename(path, name)