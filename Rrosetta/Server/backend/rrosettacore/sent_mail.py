#PY3#HPM#
# THIS CODE IS LARGELY TAKEN FROM A SCRIPT
#   FREELY PROVIDED GOOGLE AS PART OF THEIR API DOCUMENTATION ##

# Pulls all the sent emails from a gmail user account

#=========================

import base64

import httplib2
from bs4 import BeautifulSoup

#-------------------------
# from . import g_auth as gmail ## TURNED OF FOR DJANGO DEBUGGING

#=========================


def get_page_tokens(_userID, _service):
    """
    Takes Int, OAuth2 Service
    Returns Int
    --
    Get all the page tokens
    for all the sent emails
    for any given UserID
    """
    sent_results = _service.users().messages().list(
        labelIds='SENT', userId=_userID).execute()
    newPT = sent_results.get('nextPageToken')
    pageTokens = set()
    pageTokens.add(newPT)
    while newPT != None:
        sent_results = _service.users().messages().list(
            labelIds='SENT', userId=_userID, pageToken=newPT).execute()
        newPT = sent_results.get('nextPageToken')
        pageTokens.add(newPT)
    return pageTokens
#-------------------------


def single_access_msgs(_userID, _service):
    """
    Takes Int, OAuth2 Service
    Returns Gmail Object
    --
    Access just the first page
    of sent emails for any UserID
    """
    sent_results = _service.users().messages().list(
        labelIds='SENT', userId=_userID).execute()
    return sent_results.get('messages', [])
#-------------------------


def get_sent_bodys(_pageTokens, _credentials, _userID, _service):
    """
    Takes Int, OAuth2 Credential, Int, OAuth2 Service
    Returns List of Strings
    --
    for any given UserID
    get the credentials and service,
    pull each page of sent emails,
    collect in list
    """
    if not _pageTokens:
        print('no pages')
        sentMSGs = single_access_msgs(_userID, _service)
    else:
        sentMSGs = []
        for token in _pageTokens:
            sent_results = _service.users().messages().list(
                labelIds='SENT', userId=_userID, pageToken=token).execute()
            sentMSGs.append(sent_results.get('messages', []))

    if not sentMSGs:
        print('no sent messages')
    else:
        print('Pages: ', len(_pageTokens))
        sentIDs = []
        for page in sentMSGs:
            for MSG in page:
                sentIDs.append(MSG['id'])

    if not sentIDs:
        print('no sent IDs')
    else:
        print("IDs: ", len(sentIDs))
        sentContents = []
        for sentID in sentIDs:
            sentContents.append(_service.users().messages().get(
                userId=_userID, id=sentID).execute())

    if not sentContents:
        print('no sent msg content')
    else:
        print("contents: ", len(sentContents))
        bodys = []
        for sentContent in sentContents:
            if 'body' not in sentContent['payload'].keys():
                pass
            else:
                bodys.append(sentContent['payload']['body'])
    return bodys
#-------------------------


def read_sent_content(_bodys):
    """
    Takes List of Strings
    Returns Set of Strings
    --
    Translate Base64 encoded sent emails
    into UTF-8 encoded strings
    collected in a list of sent emails
    """
    print("bodies: ", len(_bodys))
    sent_emails = set()
    if not _bodys:
        print('no MSG bodies')
    else:
        data64s = []
        for body in _bodys:
            if 'data' not in body.keys():
                pass
            else:
                try:
                    sent_emails.add(
                        str(relaxed_decode_base64(body['data'])).encode('utf-8'))
                except:
                    pass
    return sent_emails
#-------------------------


def relaxed_decode_base64(data):
    """
    Takes String
    Returns String
    --
    Credit: This function was taken from Stack Overflow:
    https://stackoverflow.com/questions/44164829/base64-decode-specific-string-incorrect-padding-with-correct-padding
    """
    # If there is already padding we strim it as we calculate padding ourselves.
    if '=' in data:
        data = data[:data.index('=')]

    # We need to add padding, how many bytes are missing.
    missing_padding = len(data) % 4

    # We would be mid-way through a byte.
    if missing_padding == 1:
        data += 'A=='
    # Jut add on the correct length of padding.
    elif missing_padding == 2:
        data += '=='
    elif missing_padding == 3:
        data += '='

    # Actually perform the Base64 decode.
    return base64.b64decode(data)
#-------------------------

# TURNED OF FOR DJANGO DEBUGGING
# def main(_authorization_code):
#     """
#     """
#     credentials = gmail.exchange_code(_authorization_code)
#     if credentials:
#         print('not authorised')
#     else:
#         user = gmail.get_user_info(credentials)
#         if not user:
#             print('no user')
#         else:
#             service = gmail.build_service(credentials)

#     if not credentials and user and service:
#         print('not authorised')
#     else:
#         tokens = get_page_tokens(user['id'], service)
#         bodies = get_sent_bodys(tokens, credentials, user['id'], service)
#         sent_emails = read_sent_content(bodies)
#         return sent_emails
# #-------------------------

# TURNED OF FOR DJANGO DEBUGGING
# def debug():
#     """
#     """
#     service = gmail.debug()
#     credentials = gmail.get__credentials()
#     if credentials:
#         print('not authorised')
#     else:
#         user = gmail.get_user_info(credentials)
#         if not user:
#             print('no user')
#         else:
#             service = gmail.build_service(credentials)


#     if not credentials and user and service:
#         print('not authorised')
#     else:
#         tokens = get_page_tokens(user['id'], service)
#         bodies = get_sent_bodys(tokens, credentials, user['id'], service)
#         sent_emails = read_sent_content(bodies)
#         return sent_emails
# #-------------------------

#=========================

if __name__ == '__main__':
    auth_code = ''
    l = main(auth_code)
    for i in l:
        print(i)