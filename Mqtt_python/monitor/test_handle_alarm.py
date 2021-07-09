import unittest
import unittest.result

from main import handle_alarms, queue

class TestAlarm(unittest.TestCase):

    def test_one_insertion(self):
        while not queue.empty():
            queue.get()
        handle_alarms(10)
        self.assertEqual(list(queue.queue), [10])

    def test_two_insertions(self):
        while not queue.empty():
            queue.get()
        handle_alarms(10)
        handle_alarms(20)
        self.assertEqual(list(queue.queue), [10, 20])

    def test_three_insertions(self):
        while not queue.empty():
            queue.get()
        handle_alarms(10)
        handle_alarms(20)
        handle_alarms(30)
        self.assertEqual(list(queue.queue), [10, 20, 30])

    def test_four_insertions(self):
        while not queue.empty():
            queue.get()
        handle_alarms(10)
        handle_alarms(20)
        handle_alarms(30)
        handle_alarms(40)
        self.assertEqual(list(queue.queue), [10, 20, 30, 40])

    def test_four_insertions(self):
        while not queue.empty():
            queue.get()
        handle_alarms(10)
        handle_alarms(20)
        handle_alarms(30)
        result = handle_alarms(40)

        print(result)
        self.assertEqual(list(queue.queue), [30, 40])

if __name__ == "__main__":
    unittest.main()