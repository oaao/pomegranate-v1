import io_local
import juice


orders_raw, orders_config = juice.market_import('rens')
orders_structured = juice.market_distill(orders_raw, orders_config)
# orders_contextualised = market_context(orders_structured, orders_config)

io_local.write_json(orders_structured, 'indented')
