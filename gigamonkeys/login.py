#!/usr/bin/env python

import hashlib
import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


def login(scopes):
    """
    Login with the desired scopes, using saved credentials if they
    exist and are still valid. Save credentials for future use.
    """
    filename = token_file(scopes)

    creds = load_creds(filename)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes)
            creds = flow.run_local_server(port=0)

        save_creds(filaneme, creds)

    return creds


def load_creds(filename):
    "Load saved credentials if they exist."
    if os.path.exists(filename):
        with open(filename, "rb") as token:
            return pickle.load(token)


def save_creds(filename, creds):
    "Save credentials."
    with open(filename, "wb") as token:
        pickle.dump(creds, token)


def token_file(scopes):
    "Derive the token name from the desired scopes."
    m = hashlib.sha1()
    for s in sorted(scopes):
        m.update(s.encode("utf-8"))
    return f"{m.hexdigest()}.pickle"


if __name__ == "__main__":

    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

    print(login(scopes).token)
