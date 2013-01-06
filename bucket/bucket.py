#!/usr/bin/env python


#
# Imports
#


#
# Constants
#


#
# Code
#
class Bucket(object):
    """
    Stores money of the user.
    """

    def __init__(self, bucketName = ""):
        """
        Constructor.

        @type  bucketName: basestring
        @param bucketName: bucket's name

        @rtype: None
        @returns: Nothing
        """
        # sanity check
        assert isinstance(bucketName, str)

        # bucket identifier
        # TODO: create a better way to assign this
        self.__bucketId = 33L

        # bucket name
        self.__bucketName = bucketName

        # total value inside the bucket
        self.__total = 0L
    # __init__()

    def add(self, entry):
        """
        Adds an entry on the bucket.

        @type  entry: Entry object
        @param entry: entry value with related data

        @rtype: int
        @returns: return code
        """
        # save value to summarize the total
        self.__total += entry.getValue()

        return 0
    # add()

    def getName(self):
        """
        Returns the bucket's name.

        @rtype: basestring
        @returns: bucket's name
        """
        return self.__bucketName
    # getName()

    def remove(self, entry):
        """
        Removes a value from bucket. In fact, is the same that adds the value
        with negative signal. This way is better to organize the data.

        @type  entry: Entry object
        @param entry: entry value with related data

        @rtype: int
        @returns: return code
        """
        # get value from entry and change it to negative
        value = entry.getValue()
        entry.setValue(value * -1)

        # save value to summarize the total
        self.__total += entry.getValue()

        return 0
    # remove()

    def total(self):
        """
        Returns the total inside the bucket.

        @rtype: float
        @returns: value inside the bucket
        """
        return self.__total
    # total()

# Bucket
