import instagrapi as ip


def loginWithCredential(cl, username, password):
    """
    Login with username and password provided
    """
    cl.login(username, password)


def getFollowerCount(client):
    """
    :return the @code int follower co
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
    following = set(client.user_following(client.user_id).keys())
    followers = set(client.user_followers(client.user_id).keys())
    not_following_back = list(following - followers)
    return not_following_back


def printUserNotFollowingBackList(list):
    print("List of accounts not following back ----------")
    print(f"{'ID':<20} {'Username':<20} {'Full Name':<20}")
    for x in list:
        print(f"{x:<20} {ip.user_info(x).username:<20} {ip.user_info(x).fullname:<20}")
