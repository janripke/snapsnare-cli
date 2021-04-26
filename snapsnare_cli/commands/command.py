class Command(object):
    """
    This is the base class to be used by all commands.
    """

    def execute(self, **kwargs):
        raise NotImplementedError("Plugin.execute should be defined by subclasses")
