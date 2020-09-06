import pluggy

hookspec = pluggy.HookspecMarker("gutenberg")


@hookspec
def print_output(resp, kwargs):
    """Print formatted output"""
