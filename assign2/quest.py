import zlib
import base64
exec(zlib.decompress(base64.b64decode('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')))