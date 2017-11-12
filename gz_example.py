import gzip
import StringIO
import json

x = {
    'data': [1, 2, 3]
}

json_str = json.dumps(x)

out = StringIO.StringIO()
with gzip.GzipFile(fileobj=out, mode='w') as f:
    f.write(json_str)
# This is not human readable
print out.getvalue()
# This is human readable. Need seek(0) to return pointer to beginning-of-file.
out.seek(0)
gzip.GzipFile(fileobj=out).read()
# Or:
gzip.GzipFile(fileobj=StringIO.StringIO(out.getvalue())).read()