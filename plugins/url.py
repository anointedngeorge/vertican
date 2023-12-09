

def local_file_url_image(code=''):
    return f"/admin/settings/gallery/fileuploader/{code}/"


def api_fetch_image(code=''):
    # return f"https://bomachgroup.com/apiadmin/api/v1/media/get-gallery-image/{code}/"
    return f"/admin/settings/gallery/get-files/{code}/"