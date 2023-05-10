import re


def loginWithCredential(cl, username, password):
    """
    Login with username and password provided
    """
    cl.login(username, password)


def getFollowerCount(client):
    """
    :return the @code int follower count 
    """
    return len(client.user_followers())


def getFollowingCount(client):
    """
    :return the @code int following count
    """
    return len(client.user_following())


def userNotFollowingBack(client):
    """
    :return a list of followers not following back
    """
    return [x for x in list(client.user_following(client.user_id).values()) if x not in list(client.user_followers(client.user_id).values())]


def printUserNotFollowingBackList(list):
    print("List of accounts not following back ----------")
    print(f"{'ID':<20} {'Username':<20} {'Full Name':<20}")
    for x in list:
        print(f"{x.pk:<20} {x.username:<20} {x.full_name:<20}")
