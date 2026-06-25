import threading
import unittest

import tests.integration.init_utils as init_utils
from tests.integration.init_utils import MERCHANT_ID

from onlinepayments.sdk.factory import Factory

REQUEST_COUNT = 10
MAX_CONNECTIONS_EQUAL_TO_REQUEST_COUNT = 10
MAX_CONNECTIONS_LESS_THAN_REQUEST_COUNT = 5
SINGLE_MAX_CONNECTION = 1


class ConnectionPoolingTest(unittest.TestCase):

    """Test connection pooling"""

    def test_connection_pool_max_equals_request_count_completes_all_requests(self):
        self._run_connection_pooling_test(REQUEST_COUNT, MAX_CONNECTIONS_EQUAL_TO_REQUEST_COUNT)

    def test_connection_pool_max_less_than_request_count_completes_all_requests(self):
        self._run_connection_pooling_test(REQUEST_COUNT, MAX_CONNECTIONS_LESS_THAN_REQUEST_COUNT)

    def test_connection_pool_single_connection_completes_all_requests(self):
        self._run_connection_pooling_test(REQUEST_COUNT, SINGLE_MAX_CONNECTION)

    def _run_connection_pooling_test(self, request_count, max_connections):
        configuration = init_utils.create_communicator_configuration(max_connections=max_connections)
        results = [None] * request_count

        communicator = Factory.create_communicator_from_configuration(configuration)

        try:
            client = Factory.create_client_from_communicator(communicator).with_client_meta_info("")
            start_event = threading.Barrier(request_count + 1)

            threads = [
                threading.Thread(target=_send_request, args=(i, start_event, client, results))
                for i in range(request_count)
            ]

            for thread in threads:
                thread.start()

            start_event.wait()

            for thread in threads:
                thread.join()

        finally:
            communicator.close()

        completed_count = sum(1 for result in results if result is not None and result.result is not None)
        self.assertEqual(request_count, completed_count)


def _send_request(index, start_event, client, results):
    start_event.wait()
    results[index] = client.merchant(MERCHANT_ID).services().test_connection()


if __name__ == '__main__':
    unittest.main()
