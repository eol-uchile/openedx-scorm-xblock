import os.path
import mimetypes

from django.http import HttpResponse

from .utils import get_scorm_storage


def proxy_scorm_media(request, block_id, sha1, file):
    """
    Render the media objects by proxy, as the files
    must be in the same domain as the LMS
    """
    guess = mimetypes.guess_type(file)
    if guess[0] is None:
      content_type = "text/html"
    else:
      content_type = guess[0]

    return HttpResponse(
      get_scorm_storage().open("scorm/{}/{}/{}".format(block_id, sha1, file)).read(),
      content_type=content_type,
      
    )