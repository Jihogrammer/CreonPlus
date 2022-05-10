__all__ = ['models', 'utils']

from utils import CreonAPI


if __name__ == '__main__':
    import examples
    from utils.creon_manager import is_connected
    # import asyncio
    # asyncio.get_event_loop().run_until_complete(examples.example_live_price_subscribe())
    if not is_connected():
        examples.example_connect_creon()
    examples.example_min_price()
