# pomegranate

[deprecated] First learning project.

For a market analysis tool,

To get data from multiple api endpoints, store them in respective DBs, combine/filter/reorganise that data as per configs, store that secondary data as DB, and monitor its change over time

Necessary class structure:
- read http
- read local files
- read/write db
- process data [sde, orders, history] together and output reorganised secondary data (-->read/write db)
- monitor changes in secondary data [orders: update frequency per typeid, history: price/volume changes] and record that data (-->read/write db)
- input configs
