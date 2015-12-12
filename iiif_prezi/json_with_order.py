"""Hacks to get JSON with ordered entries.

For use in other iiif_prezi modules as:

  from iiif_prezi.json_with_order import json, OrderedDict 
"""

try:
    import json
except:
    # 2.5 -- FIXME/zimeon - do we care about 2.5 now?
    import simplejson as json

try:
    # Only available in 2.7+
    # This makes the code a bit messy, but eliminates the need
    # for the locally hacked ordered json encoder
    from collections import OrderedDict
except:
    # Backported...
    try:
        from ordereddict import OrderedDict
    except:
        print "You must: easy_install ordereddict"
        raise

