#!/usr/bin/env python


#
# Imports
#


#
# Constants
#
USER_ATTR = ['name', 'age', 'city']


#
# Code
#
class User(object):
    """
    Represents a single user on the system.
    """

    def __init__(self, userData):
        """
        Constructor.

        @type  userData: dict
        @param userData: user data. It must have the following format:

            userData = {
                'name': "",
                'age': "",
                'city': "",
            }

        @rtype: None
        @returns: Nothing
        """
        # sanity checks
        assert isinstance(userData, dict)

        # given data has not all the required parameters: abort
        if False in [item in userData.keys() for item in USER_ATTR]:
            raise RuntimeError('User data is incomplete')

        # user id, calculated with user name
        # TODO: provide a better way to do this
        self.__userId = userData['name'].replace(" ", "")

        # personal user information
        self.__userData = {}
        for key in USER_ATTR:
            self.__userData[key] = userData[key]
    # __init__()

    def getUserData(self):
        """
        Returns the dict with all user data.

        @rtype: dict
        @returns: user data
        """
        return self.__userData
    # getUserData()

    def getUserId(self):
        """
        Returns the user id.

        @rtype: basestring
        @returns: user id
        """
        return self.__userId
    # getUserId()

    def setCity(self, city):
        """
        Sets user city.

        @type  city: basestring
        @param city: user city
        """
        # sanity check
        assert isistance(city, str)

        self.__userData['city'] = city
    # setCity()

    def setName(self, name):
        """
        Sets user name.

        @type  name: basestring
        @param name: user name
        """
        # sanity check
        assert isistance(name, str)

        self.__userData['name'] = name
    # setName()

# User
