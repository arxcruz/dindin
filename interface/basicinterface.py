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
class BasicInterface(object):
    """
    Implements a basic interface to handle DinDin solution.
    """

    def __init__(self, controller):
        """
        Constructor.

        @type controller: Controller instance
        @param controller: backend app instance

        @rtype: None
        @returns: Nothing
        """
        # controller instance that contains all operations
        self.__dindin = controller
    # __init__()

    def run(self):
        """
        Main method. Shows all available options for DinDin.

        @rtype: None
        @returns: Nothing
        """
        print "Dindin personal monetary control."
        print "Available buckets: "

        # get all available buckets
        buckets = self.__dindin.listBuckets()

        # print them
        for bucket in buckets:
            print "%s - %s" % (bucket[0], str(bucket[1]))
    # run()

# BasicInterface
