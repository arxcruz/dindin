#!/usr/bin/env python

#
# Imports
#
import datetime


#
# Constants
#
MARKER = ";"
TIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


#
# Code
#
class Entry(object):
    """
    Represents a single entry in the system.
    """

    def __init__(self, value, tags):
        """
        Constructor.

        @type  value: float
        @param value: value to be registered

        @type  tags: list
        @param tags: tags associated with this entry

        @rtype: None
        @returns: Nothing
        """
        # get the timestamp of entry
        self.__timestamp = datetime.datetime.now()

        # configure entry with given parameters
        self.__value = value
        self.__tags = tags
    # __init__()

    def __str__(self):
        """
        Overwritten method to print an entry.

        @rtype: basestring
        @returns: a formatted entry
        """
        # sanity checks
        assert isinstance(self.__timestamp, datetime.datetime)
        assert isinstance(self.__value, float)
        assert isinstance(self.__tags, list)

        # timestamp
        value += str(self.__timestamp) + MARKER

        # value (float)
        value += str(self.__value) + MARKER

        # tags
        value += ",".join(self.__tags)

        return value
    # __str__()

    def getTags(self):
        """
        Returns all tags associated with this entry.

        @rtype: list
        @returns: list of tags associated with this entry
        """
        return self.__tags
    # getTags()

    def getTimestamp(self):
        """
        Returns the timestamp of the entry.

        @rtype: datetime.datetime
        @returns: the timestamp of when entry was created
        """
        return self.__timestamp
    # getTimestamp()

    def getValue(self):
        """
        Returns the value of this entry.

        @rtype: float
        @returns: the registered value
        """
        return self.__value
    # getValue()

    def hasTag(self, tag):
        """
        Compares the given tag with the list of entry's ones.

        @type  tag: basestring
        @param tag: tag to be verified in the list of entry's tags

        @rtype: bool
        @returns: True if the given tag is present on entry, False otherwise
        """
        return tag in self.__tags
    # hasTag()

    def set(self, value):
        """
        Gets a given string and reads its values to fit an entry object.

        @type  value: basestring
        @param value: value to be changed to an entry

        @rtype: None
        @returns: Nothing
        """
        # sanity check
        assert isinstance(value, str)

        # split line to get each value
        parameters = value.split(MARKER)

        # timestamp
        self.__timestamp = datetime.datetime.strptime(parameters[0], TIME_FORMAT)

        # value
        self.__value = float(parameters[1])

        # tags
        self.__tags = parameters[2].split(',')
    # set()

    def setTag(self, tag):
        """
        Associates tags with this entry.

        @type  tag: list
        @param tag: add the given list to current one

        @rtype: None
        @returns: Nothing
        """
        # sanity check
        assert isinstance(tag, list)

        self.__tags = list(set(self.__tags + tag))
    # setTag()

    def setValue(self, value):
        """
        Configures the value of this entry.

        @type  value: float
        @param value: entry value

        @rtype: None
        @returns: Nothing
        """
        # sanity check
        assert isinstance(value, float)

        self.__value = value
    # setValue()

# Entry
