from instagrapi import *


def loginWithCredential(username, password):
    cl = Client()
    cl.login(username, password)
