import logging
from kiteconnect import KiteTicker

# Initialise
kws = KiteTicker(api_key, access_token)

logging.basicConfig(filename='ticks.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def on_ticks(ws, ticks):
# Callback to receive ticks.
    logging.debug("Ticks: {}".format(ticks))

def on_connect(ws, response):
# Callback on successful connect.
# Subscribe to a list of instrument_tokens (ITC and TCS here).
    ws.subscribe([424961,136330244])

# Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, [424961])

# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
        
kws.connect()